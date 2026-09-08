---
name: topic-deep-dive
description: "Research any topic in exhaustive depth by combining web search, academic papers, social discussions, and community conversations. Produces comprehensive briefings with evidence from every available source type, confidence scoring, and identified knowledge gaps."
---

# Topic Deep Dive

Research any topic in exhaustive depth by combining web search, academic papers, social discussions, and community conversations. Produces comprehensive briefings with evidence from every available source type, confidence scoring, and identified knowledge gaps. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

## Capability identifiers

- `exa_search`
- `exa_contents`
- `tavily_search`
- `scholar_search_mixed`
- `reddit_app_dynamic_search`
- `twitter_web_search_timeline`
- `google_news_bulk_articles`

## Workflow

1. Understand the user's research question, target, and context.
2. Resolve each selected capability with `sandbase_discover`, then inspect the returned `name` with `sandbase_inspect` to confirm the schema and pricing.
3. Follow `execute_as` with `sandbase_run`; collect async results with `sandbase_run_get` as described above.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_inspect` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.
