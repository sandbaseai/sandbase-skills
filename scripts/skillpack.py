#!/usr/bin/env python3
"""List, validate, and install the public SandBase Skills collection."""

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
    if catalog.get("schema_version") != 2 or not isinstance(catalog.get("skills"), list):
        raise ValueError("skills.json must use schema_version 2 and contain a skills array")
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
    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.is_file():
        errors.append(f"{name}: agents/openai.yaml is required")
    else:
        agent_text = agent_file.read_text(encoding="utf-8")
        if f'display_name: "{entry.get("display_name", "")}"' not in agent_text:
            errors.append(f"{name}: Agent display_name must match the catalog")
        if f"${name}" not in agent_text:
            errors.append(f"{name}: Agent default_prompt must mention ${name}")
    fields = frontmatter(skill_file.read_text(encoding="utf-8"))
    if not fields:
        errors.append(f"{name}: invalid YAML frontmatter delimiters")
    elif fields.get("name") != name:
        errors.append(f"{name}: frontmatter name must equal catalog name")
    elif not fields.get("description"):
        errors.append(f"{name}: frontmatter description is required")
    metadata_path = entry.get("metadata_path")
    if not isinstance(metadata_path, str):
        errors.append(f"{name}: metadata_path is required")
        return errors
    metadata_file = REPO_ROOT / metadata_path
    try:
        metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{name}: cannot read web metadata: {error}")
        return errors
    if metadata.get("schema_version") != 1 or metadata.get("id") != name:
        errors.append(f"{name}: web metadata schema_version or id is invalid")
    if not metadata.get("display_name") or not metadata.get("description"):
        errors.append(f"{name}: web metadata requires display_name and description")
    api = metadata.get("api", {})
    schema_resolution = api.get("schema_resolution")
    if (
        not isinstance(schema_resolution, dict)
        or schema_resolution.get("source") != "sandbase-capability-registry"
        or schema_resolution.get("lookup") != "sandbase_describe_tool"
    ):
        errors.append(f"{name}: API schema_resolution must use sandbase_describe_tool")
    endpoints = api.get("endpoints")
    if not isinstance(endpoints, list) or not endpoints:
        errors.append(f"{name}: web metadata must declare API endpoints")
    else:
        for endpoint in endpoints:
            if not isinstance(endpoint, dict) or not endpoint.get("tool_name") or not endpoint.get("operation"):
                errors.append(f"{name}: every API endpoint requires tool_name and operation")
                continue
    registry_path = entry.get("registry_path")
    if not isinstance(registry_path, str):
        errors.append(f"{name}: registry_path is required")
        return errors
    registry_file = REPO_ROOT / registry_path
    try:
        plugin = json.loads(registry_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{name}: cannot read registry manifest: {error}")
        return errors
    if plugin.get("name") != f"sandbase/{name}" or plugin.get("type") != "skill":
        errors.append(f"{name}: registry manifest name or type is invalid")
    required = plugin.get("unified_schema", {}).get("required_endpoints")
    displayed = [endpoint.get("tool_name") for endpoint in endpoints if isinstance(endpoint, dict)]
    if not isinstance(required, list) or set(required) != set(displayed) or len(required) != len(displayed):
        errors.append(f"{name}: catalog endpoints must exactly match registry required_endpoints")
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


def command_show(catalog: dict, skill_name: str) -> int:
    entries = selected_entries(catalog, skill_name)
    if len(entries) != 1:
        raise ValueError("show accepts exactly one skill")
    metadata_path = REPO_ROOT / entries[0]["metadata_path"]
    print(metadata_path.read_text(encoding="utf-8"))
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
    show = commands.add_parser("show", help="print display-ready metadata for one skill")
    show.add_argument("skill")
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
        if args.command == "show":
            return command_show(catalog, args.skill)
        return command_install(catalog, args)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
