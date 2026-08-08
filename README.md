# SandBase Skills

Downloadable Agent Skills for practical research and growth workflows. Install one into your agent project, then let your agent use its existing SandBase connection to call the required capabilities.

## Start here

1. Choose a Skill below.
2. Clone or download this repository.
3. Install the Skill into your agent project.
4. Ask your agent to use the installed Skill.

No API key belongs in a Skill, prompt, or report. The agent environment must already have an authorized SandBase connection.

## Choose a Skill

| Skill | Use it to | Install name |
|---|---|---|
| SEO Keyword Insights | Find evidence-backed keyword, content, and SERP opportunities. | `seo-keyword-insights` |
| Reddit Customer Insights | Discover customer language, pain points, and objections from public Reddit discussions. | `reddit-customer-insights` |
| Exa Deep Search | Find and extract reliable public sources for a research question. | `exa-deep-search` |
| Backlink Gap Analysis | Compare backlink evidence and identify ethical outreach or digital-PR opportunities. | `backlink-gap-analysis` |
| Competitor Content Intelligence | Identify differentiated content opportunities from public competitor coverage. | `competitor-content-intelligence` |

## Install a Skill

Use the included installer from the repository root. It supports Codex, Claude, Cursor, and a generic project structure.

```bash
python3 scripts/skillpack.py install \
  --target codex \
  --dest /path/to/your/project \
  --skills exa-deep-search
```

Preview an installation without writing files:

```bash
python3 scripts/skillpack.py install \
  --target codex \
  --dest /path/to/your/project \
  --skills exa-deep-search \
  --dry-run
```

The installer copies the selected Skill into the target project. Use `--force` only when you intend to replace an existing installed Skill.

## Use it in your agent

After installation, use the Skill by name. For example:

```text
Use $exa-deep-search to research how enterprise teams evaluate AI agents. Prefer primary sources and cite every finding.
```

Each Skill describes its workflow, evidence standards, expected output, and the SandBase capabilities it needs. Your agent performs the analysis; the Skill does not depend on a separate third-party LLM.

## Repository layout

```text
marketing/<skill>/SKILL.md       The downloadable Agent instruction
marketing/<skill>/agents/        Agent UI metadata
skills.json                      Machine-readable index of all public Skills
catalog/skills/                  Optional data for a website or marketplace
registry/data/skills/sandbase/   Optional database-registration manifests
scripts/skillpack.py             List, validate, and install Skills locally
```

Most users only need `marketing/` and the installer. The `catalog/` and `registry/` directories are for teams that run a Skill website or import Skills into the SandBase registry.

## For website and registry integrators

`skills.json` is the repository index. Each entry points to the downloadable Skill, its display metadata, and its registry manifest.

The endpoint list in `catalog/skills/<skill>.json` is display metadata. Resolve current endpoint parameters from the SandBase Capability Registry at runtime with `sandbase_describe_tool`; do not copy API parameter snapshots, prices, or credentials into this repository. The validator ensures that every catalog endpoint list exactly matches its registry manifest.

## Validate locally

```bash
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
```

These checks are offline. They do not make API calls or require credentials.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing a Skill.

## License

Apache-2.0. See [LICENSE](LICENSE).
