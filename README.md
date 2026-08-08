# SandBase Skills

A public collection of downloadable Agent Skills. Each Skill turns SandBase capabilities into a focused, repeatable workflow and requires an authorized SandBase connection.

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

The repository exposes a display-ready index in `skills.json` and a detailed record per Skill under `catalog/skills/`. A website can render cards and detail pages directly from this data: title, description, tags, install prompt, pricing label, examples, configuration, and an expandable Tools & Endpoints list.

`operation` is a human-readable provider operation for display. Calls must go through the SandBase MCP gateway using `tool_name`; the UI resolves current parameters from Capability Registry with `sandbase_describe_tool` when a row expands. The repository deliberately does not copy endpoint parameter snapshots, pricing, or API keys into Skills.

## Endpoint schemas

Each endpoint binding uses SandBase Capability Registry as the authoritative source for its current input schema. A page resolves the binding by `tool_name` at runtime and renders the returned `inputSchema`. An optional `capability_id` can improve database joins, but must not replace the live lookup.

## Registry example

Each `registry/data/skills/sandbase/<skill-id>/plugin.json` file is a database-registration manifest. It declares the stable endpoint bindings in `unified_schema.required_endpoints` and optional workflow groups or safe starter presets. Its endpoint set must exactly match the detailed catalog; parameters remain in Capability Registry.

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

The tests validate the catalog, registry manifests, Skill frontmatter, internal references, SandBase API-map safety rules, and installer dry-run behavior. They do not make live API calls or require credentials.

## Add a Skill

Create each new Skill under a product area, for example `marketing/<skill-name>/`. Include a `SKILL.md` with the required `name` and `description` frontmatter, then add it to `skills.json`. Run `python3 scripts/skillpack.py validate` and the tests before publishing.
