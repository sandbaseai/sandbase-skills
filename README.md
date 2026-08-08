# SandBase Skills

A versioned collection of downloadable Agent Skills that turn SandBase capabilities into repeatable workflows. Each skill is self-contained, but all SandBase-backed skills require an authorized SandBase connection when used outside a SandBase Agent.

## Included skills

| Skill | Purpose |
|---|---|
| `seo-keyword-insights` | Research keywords, competition, demand, and SERP-backed page opportunities with SandBase SEO capabilities. |
| `reddit-customer-insights` | Turn public Reddit discussions into customer-language, pain-point, and objection research. |
| `exa-deep-search` | Search, extract, and compare high-quality public sources with Exa. |
| `backlink-gap-analysis` | Find ethical backlink and digital-PR gaps from backlink evidence. |
| `competitor-content-intelligence` | Compare public competitor coverage and identify differentiated content opportunities. |
| `market-signal-monitor` | Monitor non-financial web, community, news, and search-interest signals. |

## Web catalog metadata

The repository exposes display-ready data in `skills.json` and a detailed record per Skill under `catalog/skills/`. A website can render the skill detail page directly from this data: title, description, tags, compatibility, install prompt, action buttons, pricing label, and an expandable Tools & Endpoints list.

`operation` is a human-readable provider operation for display. Calls must still go through the SandBase MCP gateway using `tool_name`; the web UI can obtain current parameter fields from `sandbase_describe_tool` when a row expands.

Every detailed record also includes `examples`, `configuration`, `notes`, `related_skills`, and `agent_tests`. These map directly to a Skill detail page: Overview, Install, Tools & Endpoints, Example Tasks, Configuration, Notes, Related Skills, and **Test in Agent**.

## Endpoint schemas

Each endpoint binding uses SandBase Capability Registry as the authoritative source for its current input schema. A page resolves the binding's `capability_id` at runtime and renders `inputSchema`. The first reference implementation is `seo-keyword-insights` → `keyword_suggestions`.

## Registry example

`registry/data/skills/sandbase/seo-keyword-insights/plugin.json` is the registration template for the first public Skill. It declares the stable endpoint bindings in `unified_schema.required_endpoints`, organizes them into `workflow_groups`, and defines secret-free `test_presets`. Keep its endpoint set identical to the detailed catalog; parameters remain in Capability Registry and are not copied into this file.

## Test in SandBase Agent

Agent-test declarations live in each catalog record and are indexed by `evals/<skill-id>.json`. A product surface can send a selected test's `prompt` to a SandBase Agent, allow only `allowed_tools`, capture its trace and final response, and evaluate every `assertions` item. Tests marked `read-only` must not invoke write, posting, or account-changing capabilities.

The package CLI validates the test declarations offline:

```bash
python3 scripts/skillpack.py test --skill seo-keyword-insights
python3 scripts/skillpack.py show seo-keyword-insights
```

## Install locally

Clone or download this repository, then install into an agent project:

```bash
python3 scripts/skillpack.py install --target codex --dest /path/to/project
```

Supported targets are `codex`, `claude`, `cursor`, and `generic`. The installer copies skills into the target's project-level skills directory and refuses to overwrite existing skills unless `--force` is passed.

```bash
python3 scripts/skillpack.py list
python3 scripts/skillpack.py validate
python3 scripts/skillpack.py install --target codex --dest /path/to/project --skills seo-keyword-insights --dry-run
python3 scripts/skillpack.py install --target codex --dest /path/to/project --skills seo-keyword-insights
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
