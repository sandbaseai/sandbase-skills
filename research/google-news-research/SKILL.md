---
name: google-news-research
description: Search and monitor news articles across Google News through SandBase. Use when asked for news monitoring, current events research, news coverage analysis, or media tracking.
---

# Google News Research

News discovery and monitoring through SandBase's Google News integration. Search articles by topic, track news coverage, and analyze media patterns. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

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
