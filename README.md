# SandBase Skills

Downloadable Agent Skills for practical research and growth workflows. Install one into your agent project, then let your agent use its existing SandBase connection to call the required capabilities.

## Start here

1. Choose a Skill below.
2. Run one `npx` command from your agent project.
3. Ask your agent to use the installed Skill.

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

From your project root, install a Skill with the open `skills` CLI. `npx` downloads the CLI when needed; you do not need to clone this repository or run a local Python file.

```bash
npx skills add sandbaseai/sandbase-skills \
  --skill exa-deep-search \
  --agent codex
```

The default install is project-scoped. Add `--global` when you want the Skill available across all of your Codex projects:

```bash
npx skills add sandbaseai/sandbase-skills \
  --skill exa-deep-search \
  --agent codex \
  --global
```

To browse the available Skills before installing, run:

```bash
npx skills add sandbaseai/sandbase-skills --list
```

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
integrations/sandbase-registry/  Optional SandBase Registry import manifests
scripts/skillpack.py             Maintainer-only validation and inspection helper
```

Most users only need the `npx skills add` command above. `catalog/` is for teams that run a Skill website; `integrations/` is for teams that import Skills into a platform.

## For website and registry integrators

`skills.json` is the repository index. Each entry points to the downloadable Skill, its display metadata, and its optional SandBase Registry manifest under `integrations/`.

The endpoint list in `catalog/skills/<skill>.json` is display metadata. Resolve current endpoint parameters from the SandBase Capability Registry at runtime with `sandbase_describe_tool`; do not copy API parameter snapshots, prices, or credentials into this repository. The validator ensures that every catalog endpoint list exactly matches its registry manifest.

## For contributors: validate locally

```bash
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
```

These checks are offline. They do not make API calls or require credentials.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing a Skill.

## License

Apache-2.0. See [LICENSE](LICENSE).
