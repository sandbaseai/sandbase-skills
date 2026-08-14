# SandBase Skills

Downloadable Agent Skills for practical research and growth workflows. Install one into your agent project, then let your agent use its existing SandBase connection to call the required capabilities.

## Start here

1. Connect your agent to SandBase.
2. Choose a Skill below.
3. Run one `npx` command from your agent project.
4. Ask your agent to use the installed Skill.

No API key belongs in a Skill, prompt, or report. The agent environment must already have SandBase API access configured.

## Configure SandBase API access

These Skills use SandBase API capabilities. Configure a SandBase API key before the first task, keeping it only in your secret manager or environment configuration under `SANDBASE_API_KEY`:

```bash
export SANDBASE_API_KEY='your_sandbase_api_key'
```

Never commit this value, add it to a repository `.env` file, paste it into a chat prompt, or include it in a report. The installed Skill discovers the current API schema through authorized SandBase API access; it never needs the raw key in its instructions.

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

### DeepSeek Harness

DeepSeek Harness discovers project skills from `.dsh/skills/<skill-name>/SKILL.md`.
Install a SandBase skill, including its references, into that native discovery
root directly from npm:

```bash
npx @sandbaseai/dsh-skills add exa-deep-search --project /path/to/dsh-project
```

Then start DSH from the target project and invoke the installed skill by name,
for example `$exa-deep-search`. The skill expects the SandBase MCP tools
`sandbase_describe_tool` and `sandbase_call_tool` to already be available in
the agent environment. The installer never reads or writes API keys.

List every installable skill with:

```bash
npx @sandbaseai/dsh-skills list
```

Until the first npm release, run the identical CLI from a checkout with
`node bin/sandbase-dsh-skills.mjs`. The existing Python installer remains an
offline fallback.

#### Compatibility

- Node.js 20+ for the npm CLI, or Python 3.10+ for the fallback installer
- DeepSeek Harness versions that discover `.dsh/skills/<name>/SKILL.md`
- A configured SandBase MCP connection exposing `sandbase_describe_tool` and
  `sandbase_call_tool`

Last verified on 2026-08-14 against DeepSeek Harness commit
[`47f9438`](https://github.com/deepseek-ai/deepseek-harness/commit/47f943859bef60e4160492346772ded9b24f765a): the installer placed the complete
skill bundle in the native discovery root and preserved its references.

#### Uninstall

```bash
npx @sandbaseai/dsh-skills remove exa-deep-search --project /path/to/dsh-project
```

The command only removes the named directory after verifying that it contains
a `SKILL.md` marker.

#### Permissions and data

The installer reads the selected skill bundle and writes it beneath the target
project's `.dsh/skills` directory. It makes no network requests after npm has
downloaded the package and never reads `SANDBASE_API_KEY`. Installed skill
instructions may ask DSH to call the already configured SandBase MCP tools;
the MCP connection's own policy controls network and data access.

#### Troubleshooting

- `Unknown skill`: run `npx @sandbaseai/dsh-skills list` and use the exact name.
- `already exists`: review the installed copy, then pass `--force` if replacing
  it is intentional.
- DSH cannot see the skill: run DSH from the project passed to `--project` and
  verify `.dsh/skills/<name>/SKILL.md` exists.
- SandBase tools are unavailable: configure the SandBase MCP connection before
  invoking the skill.

## Use it in your agent

After installation, use the Skill by name. For example:

```text
Use $exa-deep-search to research how enterprise teams evaluate AI agents. Prefer primary sources and cite every finding.
```

Each Skill describes its workflow, evidence standards, expected output, and the SandBase capabilities it needs. Every endpoint is documented in the installed Skill's API map; parameters are resolved at runtime with `sandbase_describe_tool`. Your agent performs the analysis; the Skill does not depend on a separate third-party LLM.

## Repository layout

```text
marketing/<skill>/SKILL.md       The downloadable Agent instruction
marketing/<skill>/references/    Optional capability maps and deeper guidance
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
npm test
npm run package:check
```

These checks are offline. They do not make API calls or require credentials.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing a Skill.

## License

Apache-2.0. See [LICENSE](LICENSE). Report security issues privately to the
maintainers; never include API keys, private research inputs, or generated
reports in a public issue.
