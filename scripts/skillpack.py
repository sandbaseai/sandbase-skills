#!/usr/bin/env python3
"""List, validate, and install the SandBase Skills collection."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "skills.json"
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TARGET_DIRS = {
    "codex": Path(".codex/skills"),
    "claude": Path(".claude/skills"),
    "cursor": Path(".cursor/skills"),
    "generic": Path("skills"),
}


def load_catalog() -> dict:
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot read {CATALOG_PATH.name}: {error}") from error
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("skills"), list):
        raise ValueError("skills.json must use schema_version 1 and contain a skills array")
    return catalog


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return None
    fields: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_skill(entry: dict) -> list[str]:
    errors: list[str] = []
    name = entry.get("name")
    relative_path = entry.get("path")
    if not isinstance(name, str) or not SKILL_NAME_RE.fullmatch(name):
        return [f"Invalid skill name: {name!r}"]
    if not isinstance(relative_path, str):
        return [f"{name}: missing path"]
    skill_dir = REPO_ROOT / relative_path
    skill_file = skill_dir / "SKILL.md"
    if not skill_dir.is_dir() or not skill_file.is_file():
        return [f"{name}: SKILL.md not found at {relative_path}"]
    fields = frontmatter(skill_file.read_text(encoding="utf-8"))
    if not fields:
        errors.append(f"{name}: invalid YAML frontmatter delimiters")
    elif fields.get("name") != name:
        errors.append(f"{name}: frontmatter name must equal catalog name")
    elif not fields.get("description"):
        errors.append(f"{name}: frontmatter description is required")
    return errors


def validate_catalog(catalog: dict) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in catalog["skills"]:
        if not isinstance(entry, dict):
            errors.append("skills.json contains a non-object skill entry")
            continue
        name = entry.get("name")
        if name in seen:
            errors.append(f"Duplicate skill name: {name}")
            continue
        seen.add(name)
        errors.extend(validate_skill(entry))
    return errors


def selected_entries(catalog: dict, requested: str | None) -> list[dict]:
    by_name = {entry["name"]: entry for entry in catalog["skills"]}
    if not requested:
        return list(by_name.values())
    names = [item.strip() for item in requested.split(",") if item.strip()]
    unknown = [name for name in names if name not in by_name]
    if unknown:
        raise ValueError(f"Unknown skill(s): {', '.join(unknown)}")
    return [by_name[name] for name in names]


def command_list(catalog: dict) -> int:
    for entry in catalog["skills"]:
        print(f"{entry['name']}\t{entry.get('category', 'uncategorized')}\t{entry.get('description', '')}")
    return 0


def command_validate(catalog: dict) -> int:
    errors = validate_catalog(catalog)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(catalog['skills'])} skill(s).")
    return 0


def command_install(catalog: dict, args: argparse.Namespace) -> int:
    errors = validate_catalog(catalog)
    if errors:
        print("Cannot install an invalid collection.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    entries = selected_entries(catalog, args.skills)
    destination = Path(args.dest).expanduser().resolve() / TARGET_DIRS[args.target]
    operations: list[tuple[Path, Path]] = []
    for entry in entries:
        source = REPO_ROOT / entry["path"]
        target = destination / entry["name"]
        if target.exists() and not args.force:
            print(f"Refusing to overwrite {target}; use --force to replace it.", file=sys.stderr)
            return 1
        operations.append((source, target))
    for source, target in operations:
        print(f"Install {source.relative_to(REPO_ROOT)} -> {target}")
    if args.dry_run:
        print("Dry run: no files changed.")
        return 0
    destination.mkdir(parents=True, exist_ok=True)
    for source, target in operations:
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
    print(f"Installed {len(operations)} skill(s) into {destination}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="list catalog skills")
    commands.add_parser("validate", help="validate catalog and skill frontmatter")
    install = commands.add_parser("install", help="copy skills into a local agent project")
    install.add_argument("--target", choices=TARGET_DIRS, required=True)
    install.add_argument("--dest", required=True, help="destination project root")
    install.add_argument("--skills", help="comma-separated catalog skill names; default: all")
    install.add_argument("--dry-run", action="store_true", help="print planned copies only")
    install.add_argument("--force", action="store_true", help="replace an existing installed skill")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        catalog = load_catalog()
        if args.command == "list":
            return command_list(catalog)
        if args.command == "validate":
            return command_validate(catalog)
        return command_install(catalog, args)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
