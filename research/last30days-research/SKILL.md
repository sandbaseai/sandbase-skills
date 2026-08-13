---
name: last30days-research
description: Research any topic across the last 30 days using Reddit, Twitter, YouTube, Hacker News, web search, and news sources through SandBase. Use when asked for recent trends, launch reactions, competitor activity, person/company profiles, or current event analysis.
---

# Last 30 Days Research

Comprehensive recent-history research across multiple platforms through SandBase. Aggregate the last 30 days of activity on a topic from Reddit, Twitter, YouTube, news, and web search. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Cast a wide net: query at least 3-4 platforms for comprehensive coverage.
- Weight recency — more recent signals are more relevant.
- Note platform bias: Reddit skews technical, Twitter skews real-time, YouTube skews educational.
- Cross-reference findings for confidence scoring.
- Report timeline: when did mentions spike or change tone?

## Workflow

### 1. Web and news

Use `tavily_search` with `days: 30` and `topic: "news"` for news coverage.
Use `google_news_bulk_articles` for comprehensive news articles.
Use `exa_search` with date filters for high-quality web sources.

### 2. Social platforms

Use `twitter_web_search_timeline` for Twitter/X mentions and discussions.
Use `reddit_app_dynamic_search` for Reddit discussions.
Use `youtube_web_v2_general_search` for relevant YouTube content.

### 3. Synthesize timeline

Cluster findings by week, identify spikes, track sentiment changes.

## Output

Return: timeline of activity, platform-by-platform summary, key events/milestones, sentiment trend, influencer involvement, and gaps/blind spots.

## Example tasks

- "What's happened with [topic] in the last 30 days across the internet?"
- "Track [product launch] reception across all platforms over the past month."
- "How has discussion about [company] evolved on Twitter and Reddit recently?"
- "Find all significant mentions of [person] in the last 30 days."
- "What's the recent trend around [technology]? Combine news, social, and community data."
