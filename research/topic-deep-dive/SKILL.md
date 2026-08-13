---
name: topic-deep-dive
description: "Research any topic in exhaustive depth by combining web search, academic papers, social discussions, and community conversations. Produces comprehensive briefings with evidence from every available source type, confidence scoring, and identified knowledge gaps."
---

# Topic Deep Dive

Research any topic in exhaustive depth by combining web search, academic papers, social discussions, and community conversations. Produces comprehensive briefings with evidence from every available source type, confidence scoring, and identified knowledge gaps. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `exa_search`
- `exa_contents`
- `tavily_search`
- `scholar_search_mixed`
- `reddit_app_dynamic_search`
- `twitter_web_search_timeline`
- `google_news_bulk_articles`

## Workflow

1. Understand the user's research question, target, and context.
2. Call `sandbase_describe_tool` for each selected tool to confirm parameter schema.
3. Call `sandbase_call_tool` with the exact tool_name and schema-defined arguments.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_describe_tool` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.
