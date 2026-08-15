# SandBase Skills

[![GitHub stars](https://img.shields.io/github/stars/sandbaseai/sandbase-skills?style=social)](https://github.com/sandbaseai/sandbase-skills/stargazers)
[![skills.sh flagship](https://img.shields.io/badge/skills.sh-flagship%20indexed-000000)](https://skills.sh/sandbaseai/sandbase-skills/multi-source-search)
[![AgentSkill.sh directory](https://img.shields.io/badge/AgentSkill.sh-security--scanned_directory-0f766e)](https://agentskill.sh/@sandbaseai)
[![Release](https://img.shields.io/github/v/release/sandbaseai/sandbase-skills)](https://github.com/sandbaseai/sandbase-skills/releases/latest)
[![Discussions](https://img.shields.io/github/discussions/sandbaseai/sandbase-skills)](https://github.com/sandbaseai/sandbase-skills/discussions)
[![License](https://img.shields.io/github/license/sandbaseai/sandbase-skills)](LICENSE)

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português](./README.pt-BR.md)

**88 installable Agent Skills** for research, social intelligence, marketing, and business workflows. Install into any compatible agent (DeepSeek Harness, Claude Code, Codex, Cursor, Gemini CLI) and start working immediately. The flagship research Skill works with host-provided search tools; connect SandBase when you want broader provider coverage.

## What are Skills?

A Skill is an instruction file that teaches an AI agent how to do one specific job. Each Skill defines a repeatable workflow, evidence rules, and output format. Portable Skills can use capabilities already provided by the host agent; specialized social, market, and data workflows can add SandBase providers when configured.

## Quick Start

```bash
# Try it without installing: generate the complete Skill prompt
npx skills use sandbaseai/sandbase-skills@multi-source-search

# Or install it into Codex
npx skills add sandbaseai/sandbase-skills --skill multi-source-search --agent codex

# Use it with your agent's existing web/search tools
# "Fact-check this claim with independent sources and validate the evidence ledger"
```

`multi-source-search` needs no SandBase account when the host agent already provides
search and page-reading tools. For specialized social, market, and data-provider Skills,
set `SANDBASE_API_KEY` in your environment—never in a prompt or committed file.

### DeepSeek Harness

From the root of a DeepSeek Harness project:

```bash
npx --yes github:sandbaseai/sandbase-skills add multi-source-search
dsh web
```

The installer copies the complete Skill to `.dsh/skills/multi-source-search`,
DeepSeek Harness's project-scoped discovery directory. It runs directly from the
GitHub source, so no npm publication or SandBase account is required.

### Claude Code marketplace

Install all 88 Skills as a native Claude Code plugin:

```text
/plugin marketplace add sandbaseai/sandbase-skills
/plugin install sandbase-skills@sandbase-agent-skills
```

The marketplace manifest lists every Skill explicitly, so Claude Code can discover
them on demand without copying directories by hand.

### Verify research output offline

The [`multi-source-search`](research/multi-source-search/SKILL.md) Skill produces an
evidence ledger that can be checked before you trust or share its synthesis:

See the [complete worked example](examples/branch-protection-research.md), which
cross-checks one claim against primary documentation from GitHub, GitLab, and Atlassian.

```bash
python3 research/multi-source-search/scripts/validate_report.py \
  examples/verifiable-research-report.json
# VALID: 3 source(s), 1 claim(s), 2 provider(s)
```

The validator rejects unknown or duplicate sources, inflated confidence, unused
evidence, and high-confidence claims that still have a declared conflict. It runs
offline and checks internal consistency; it does not claim that a source is true.

## Try a Real Workflow

Install the matching Skill, then give your agent one of these tasks:

| Skill | Example task | What you get | Install |
| --- | --- | --- | --- |
| [`twitter-intelligence`](research/twitter-intelligence/SKILL.md) | “Compare sentiment and recurring complaints for Brand A and Brand B on X this month.” | Source-linked posts, trends, accounts, and a structured comparison | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/twitter-intelligence) |
| [`multi-source-search`](research/multi-source-search/SKILL.md) | “Verify the strongest evidence for and against this market claim.” | Cross-checked web and academic findings with disagreements called out | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/multi-source-search) |
| [`competitor-monitor`](research/competitor-monitor/SKILL.md) | “Track three competitors’ pricing, launches, content, and social activity.” | A dated competitive-intelligence brief with observed changes | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/competitor-monitor) |
| [`seo-content-brief`](research/seo-content-brief/SKILL.md) | “Build a writer-ready brief for this target keyword.” | Search intent, competing pages, required subtopics, and differentiation angles | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/seo-content-brief) |
| [`github-profile-research`](research/github-profile-research/SKILL.md) | “Assess this engineering team’s open-source activity.” | Repository, language, contribution, star, and activity analysis | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/github-profile-research) |
| [`youtube-research`](research/youtube-research/SKILL.md) | “Map the leading channels and audience questions in this niche.” | Video and channel discovery, transcript evidence, and comment themes | [skills.sh](https://www.skills.sh/sandbaseai/sandbase-skills/youtube-research) |

## Skill Catalog (88 Skills)

### Social Intelligence (14 Skills)

Research and monitor conversations across every major social platform.

| Skill | Platform | Use it to |
|---|---|---|
| `twitter-intelligence` | Twitter/X | Search tweets, track trends, analyze users, monitor sentiment |
| `youtube-research` | YouTube | Search videos, analyze channels, extract transcripts, read comments |
| `instagram-research` | Instagram | Analyze profiles, track hashtags, research content strategies |
| `tiktok-research` | TikTok | Search videos, analyze creators, track hashtag challenges |
| `linkedin-research` | LinkedIn | Research companies, professionals, job markets |
| `reddit-research` | Reddit | Search discussions, monitor communities, discover trends |
| `xiaohongshu-research` | Xiaohongshu (RED) | Search notes, analyze creators, track consumer trends |
| `weibo-research` | Weibo | Monitor hot searches, track trending topics, analyze sentiment |
| `douyin-research` | Douyin | Search videos, analyze creators, track challenges |
| `wechat-channels-research` | WeChat Channels | Search videos, analyze live streams |
| `wechat-mp-research` | WeChat Official Accounts | Research articles, analyze accounts |
| `wechat-search` | WeChat | Search across WeChat ecosystem |
| `china-social-research` | Multi-platform | Cross-platform China social research |
| `community-research` | Reddit + Telegram | Online community analysis |

### Search & Research (17 Skills)

Find, validate, and synthesize information from multiple sources.

| Skill | Use it to |
|---|---|
| `multi-source-search` | Cross-validate research with host search tools and optional Tavily, Exa, Scholar, and Cloudsway coverage |
| `tavily-deep-research` | Advanced web search with content extraction and site mapping |
| `exa-deep-search` | Semantic search and source extraction with Exa |
| `exa-similar-finder` | Find pages similar to any URL |
| `academic-research` | Search scholarly papers with AI-powered explanations |
| `academic-trend-research` | Track emerging research areas and breakthrough papers |
| `google-news-research` | Monitor news articles and media coverage |
| `web-scraper` | Scrape pages, crawl sites, extract structured data |
| `last30days-research` | Multi-platform research for the last 30 days |
| `topic-deep-dive` | Exhaustive multi-source topic research |
| `event-tracker` | Track events in real-time across platforms |
| `trend-spotter` | Spot emerging trends across platforms |
| `news-aggregator` | Aggregate news from multiple sources |
| `market-research` | Comprehensive market intelligence |
| `newsletter-research` | Discover industry newsletters and publications |
| `podcast-research` | Find podcasts and episodes by topic |
| `content-ideation` | Generate data-backed content ideas |

### Business Intelligence (20 Skills)

Company research, sales intelligence, and competitive analysis.

| Skill | Use it to |
|---|---|
| `apollo-company-research` | Search companies, enrich profiles, track hiring |
| `akta-company-research` | Research companies via employee and product reviews |
| `company-enrichment` | Enrich company data from multiple sources |
| `google-maps-reviews` | Analyze local business reviews |
| `product-intelligence` | Cross-platform product market research |
| `product-review-extractor` | Extract and analyze product reviews at scale |
| `competitive-pricing` | Benchmark pricing against competitors |
| `pricing-page-analyzer` | Extract and analyze competitor pricing |
| `review-aggregator` | Aggregate reviews from multiple platforms |
| `startup-research` | Research startups with funding, team, and traction |
| `hiring-intelligence` | Analyze hiring patterns and talent competition |
| `talent-sourcing` | Source candidates by skills and expertise |
| `lead-research` | Build complete prospect profiles |
| `outreach-builder` | Build verified outreach lists |
| `email-outreach-prep` | Prepare personalized email outreach |
| `sales-intelligence` | Account intelligence for sales conversations |
| `partnership-research` | Qualify potential partners with data |
| `industry-landscape` | Map any industry's competitive landscape |
| `local-market-research` | Research local markets with reviews and social data |
| `data-enrichment` | Fill data gaps with verified intelligence |

### Marketing & Content (15 Skills)

Brand monitoring, influencer marketing, and content strategy.

| Skill | Use it to |
|---|---|
| `brand-monitoring` | Track brand mentions across all platforms |
| `kol-discovery` | Find and evaluate influencers across platforms |
| `influencer-analytics` | Analyze influencer performance with engagement data |
| `social-listening` | Monitor conversations about any topic globally |
| `competitor-content-intelligence` | Find differentiated content opportunities |
| `competitor-monitor` | Monitor competitor launches, pricing, campaigns, and market signals |
| `thought-leadership-monitor` | Track industry voices and their content |
| `pr-media-monitor` | Track press mentions and media narrative |
| `content-performance` | Analyze content performance across platforms |
| `audience-research` | Understand target audiences from community data |
| `social-proof-research` | Find authentic testimonials and endorsements |
| `competitor-ad-research` | Research competitor advertising strategies |
| `hashtag-tracker` | Track hashtag performance across platforms |
| `crisis-monitor` | Detect and assess crises before they escalate |
| `reddit-customer-insights` | Discover customer language and pain points |

### Marketing & SEO (5 Skills)

Search engine optimization, SERP analysis, and technical auditing.

| Skill | Use it to |
|---|---|
| `seo-keyword-insights` | Build evidence-backed keyword strategies with DataForSEO |
| `backlink-gap-analysis` | Find ethical backlink gaps against competitors |
| `serp-analysis` | Analyze live Google SERP results and features |
| `seo-content-brief` | Generate SERP-backed content briefs |
| `site-audit` | Audit website content, structure, and SEO health |

### Tools & Utilities (17 Skills)

Practical tools for everyday agent tasks.

| Skill | Use it to |
|---|---|
| `email-validator` | Verify email deliverability and reputation |
| `domain-intelligence` | Research domains (WHOIS, DNS, SSL, security) |
| `domain-analyzer` | Complete domain analysis from DNS to SEO |
| `tech-stack-detector` | Identify what tech powers any website |
| `screenshot-capture` | Capture screenshots of any URL |
| `url-to-markdown` | Convert web pages to clean Markdown |
| `youtube-transcript` | Extract transcripts from YouTube videos |
| `document-parser` | Parse PDFs and documents to text |
| `content-translator` | Translate text between languages |
| `sentiment-analyzer` | Analyze sentiment in any text |
| `weather-lookup` | Check weather conditions worldwide |
| `flight-tracker` | Track flight status in real time |
| `currency-converter` | Convert currencies with live rates |
| `github-profile-research` | Research developer GitHub profiles |
| `npm-package-research` | Evaluate npm packages before installing |
| `cve-lookup` | Look up security vulnerabilities by CVE |
| `website-monitor` | Monitor websites for changes and health |

## Install

```bash
# Install any Skill by name
npx skills add sandbaseai/sandbase-skills --skill <skill-name> --agent codex

# Global install (available across all projects)
npx skills add sandbaseai/sandbase-skills --skill <skill-name> --agent codex --global

# Browse available Skills
npx skills add sandbaseai/sandbase-skills --list
```

## Supported Agents

Skills work with any agent that implements the Agent Skills specification:

- **Claude Code** — `~/.claude/skills/`
- **OpenAI Codex** — `~/.codex/skills/`
- **Cursor** — `~/.cursor/skills/`
- **Gemini CLI** — `~/.gemini/skills/`
- **OpenClaw, Hermes, Amp, Devin** — via `npx skills add`

## How It Works

```
User Question → Agent reads SKILL.md → Uses host tools and/or SandBase → Validates evidence → Answer
```

1. You ask a question or give a task
2. Your agent reads the installed Skill's instructions
3. The Skill starts with compatible search or browser tools already available to the host
4. When configured, SandBase adds provider-specific capabilities via `sandbase_describe_tool` → `sandbase_call_tool`
5. The agent executes the workflow, validates structured evidence, and delivers the result

## SandBase Ecosystem

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) — run
  persistent agent sessions with sandboxed tools, resumable streams, artifacts,
  cancellation, audit, and replay in your own infrastructure.

## Pricing

Skills themselves are free and open source (Apache-2.0). `multi-source-search`
can use compatible host-provided tools without a SandBase account. Optional SandBase
API calls are usage-based — typically $0.001–$0.01 per call. A typical research task
using those calls costs $0.05–$0.20.

See [sandbase.ai/pricing](https://sandbase.ai/pricing) for current rates.

## Repository Layout

```
research/<skill>/SKILL.md           Agent instruction file
research/<skill>/references/        API maps and workflow guidance
marketing/<skill>/                  Original marketing skills
catalog/skills/                     Web display metadata
integrations/sandbase-registry/     Platform registry manifests
scripts/skillpack.py                Validation helper
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing a Skill.

```bash
# Validate locally
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
```

## License

Apache-2.0. See [LICENSE](LICENSE).

---

**Built for [SandBase](https://sandbase.ai)** — One API key. Every data source. 88 installable agent skills.
