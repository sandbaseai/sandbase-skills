---
name: google-news-research
description: Search and monitor news articles across Google News through SandBase. Use when asked for news monitoring, current events research, news coverage analysis, or media tracking.
---

# Google News Research

News discovery and monitoring through SandBase's Google News integration. Search articles by topic, track news coverage, and analyze media patterns. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

## Operating principles

- News data is time-sensitive — always note publication dates.
- Cross-reference multiple sources for accuracy.
- Distinguish news reporting from opinion and commentary.
- Cite sources with title, publication, date, and URL.

## Workflow

### 1. Search news

Use `google_news_bulk_articles` to search news articles by keyword, topic, or entity.

### 2. Analyze coverage

Look at: publication count, source diversity, timeline (accelerating/decelerating), tone.

## Output

Return: news articles (title, source, date, URL), coverage timeline, source diversity analysis, and key themes.

## Example tasks

- "What news has been published about [company/topic] in the last week?"
- "Track news coverage of [event] across major publications."
- "Compare how different media outlets are covering [topic]."
- "Find breaking news about [topic] today."
- "What's the news sentiment around [brand/person] this month?"
