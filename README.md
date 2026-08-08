# SandBase Skills

A versioned collection of downloadable Agent Skills that turn SandBase capabilities into repeatable workflows. Each skill is self-contained, but all SandBase-backed skills require an authorized SandBase connection when used outside a SandBase Agent.

## Included skills

| Skill | Purpose |
|---|---|
| `seo-keyword-research` | Research keywords, competition, demand, and SERP-backed page opportunities with SandBase SEO capabilities. |

## Install locally

Clone or download this repository, then install into an agent project:

```bash
python3 scripts/skillpack.py install --target codex --dest /path/to/project
```

Supported targets are `codex`, `claude`, `cursor`, and `generic`. The installer copies skills into the target's project-level skills directory and refuses to overwrite existing skills unless `--force` is passed.

```bash
python3 scripts/skillpack.py list
python3 scripts/skillpack.py validate
python3 scripts/skillpack.py install --target codex --dest /path/to/project --skills seo-keyword-research --dry-run
python3 scripts/skillpack.py install --target codex --dest /path/to/project --skills seo-keyword-research
```

After installation, connect SandBase in the agent environment. In a SandBase Agent, the installed Skill can call the configured SandBase capabilities directly. Do not add API keys to a Skill, project file, prompt, or report.

## Test locally

Run the offline package test suite:

```bash
python3 -m unittest discover -s tests -v
```

The tests validate the catalog, Skill frontmatter, internal references, SandBase API-map safety rules, and installer dry-run behavior. They do not make live API calls or require credentials.

## Add a Skill

Create each new Skill under a product area, for example `marketing/<skill-name>/`. Include a `SKILL.md` with the required `name` and `description` frontmatter, then add it to `skills.json`. Run `python3 scripts/skillpack.py validate` and the tests before publishing.
