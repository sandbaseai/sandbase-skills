---
name: competitor-monitor
description: Monitor competitor websites, content changes, social activity, and market positioning through SandBase. Use when asked for competitive intelligence, competitor tracking, market positioning research, or competitive content monitoring.
---

# Competitor Monitor

Cross-channel competitive intelligence through SandBase. Track competitor website content, social media activity, news coverage, and search visibility. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Focus on observable, public behavior — don't speculate on internal strategy.
- Compare like-for-like: same time period, same metrics across competitors.
- Track multiple dimensions: content, social, search, news.
- Note what you can't observe (private channels, paid activity) as gaps.

## Workflow

### 1. Website monitoring

Use `firecrawl_scrape` or `context_dev_scrape_markdown` to extract competitor page content.
Use `firecrawl_map` to discover competitor site structure.
Use `context_dev_capture_screenshot` for visual monitoring.

### 2. Search visibility

Use `exa_search` with `include_domains` to find competitor content.
Use `dataforseo_v3_serp_google_organic_live_advanced` to check their rankings.

### 3. Social monitoring

Use `twitter_web_search_timeline` for competitor brand mentions.
Use `linkedin_web_v2_company_posts` for competitor LinkedIn activity.
Use `youtube_web_v2_channel_videos` for competitor YouTube content.

### 4. News tracking

Use `tavily_search` with competitor name and "news" topic.
Use `google_news_bulk_articles` for news coverage.

## Output

Return: competitor activity summary, content changes detected, social media presence comparison, search visibility snapshot, news coverage, and strategic observations.

## Example tasks

- "Monitor [competitor]'s website — what pages have they added or changed?"
- "Compare [our brand] vs [competitor] social media activity this month."
- "What's [competitor] ranking for that we're not?"
- "Track [competitor]'s recent news coverage and announcements."
- "Analyze [competitor]'s LinkedIn content strategy — what topics, cadence, engagement?"
