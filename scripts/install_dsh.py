#!/usr/bin/env python3
"""Install SandBase skills into a DeepSeek Harness project."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def available_skills() -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for skill_file in REPO_ROOT.glob("*/**/SKILL.md"):
        relative = skill_file.relative_to(REPO_ROOT)
        if relative.parts[0] not in {"marketing", "research"}:
            continue
        skills[skill_file.parent.name] = skill_file.parent
    return dict(sorted(skills.items()))


def install_skill(name: str, project: Path, *, force: bool = False) -> Path:
    skills = available_skills()
    source = skills.get(name)
    if source is None:
        raise ValueError(f'Unknown skill "{name}". Use --list to see available skills.')

    destination = project.resolve() / ".dsh" / "skills" / name
    if destination.exists():
        if not force:
            raise FileExistsError(
                f"{destination} already exists. Pass --force to replace it."
            )
        shutil.rmtree(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return destination


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install SandBase Agent Skills into .dsh/skills."
    )
    parser.add_argument("skill", nargs="?", help="Skill name to install")
    parser.add_argument(
        "--project", type=Path, default=Path.cwd(), help="DSH project root"
    )
    parser.add_argument("--force", action="store_true", help="Replace an existing skill")
    parser.add_argument("--list", action="store_true", help="List available skills")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    skills = available_skills()

    if args.list:
        if args.json:
            print(json.dumps({"skills": list(skills)}, indent=2))
        else:
            print("\n".join(skills))
        return 0

    if not args.skill:
        raise SystemExit("skill is required unless --list is used")

    try:
        destination = install_skill(args.skill, args.project, force=args.force)
    except (ValueError, FileExistsError) as error:
        raise SystemExit(str(error)) from error

    result = {"skill": args.skill, "destination": str(destination)}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Installed {args.skill} to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
