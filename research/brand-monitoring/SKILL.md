---
name: brand-monitoring
description: Monitor brand mentions, sentiment, and reputation across Twitter, Reddit, news, and social platforms through SandBase. Use when asked for brand monitoring, reputation tracking, social listening, PR coverage analysis, or competitive brand intelligence.
---

# Brand Monitoring

Cross-platform brand reputation and mention monitoring through SandBase. Track what's being said about a brand across Twitter, Reddit, news sources, and Chinese platforms. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Monitor across multiple platforms for complete coverage.
- Separate factual mentions from sentiment/opinion.
- Track both brand name and common misspellings/abbreviations.
- Note platform-specific context (Twitter = real-time, Reddit = community depth, News = authority).
- Keep client brand strategy and competitor lists confidential.

## Workflow

### 1. Twitter monitoring

Use `twitter_web_search_timeline` to search brand mentions and hashtags.
Use `twitter_web_trending` to check if brand is trending.

### 2. Reddit monitoring

Use `reddit_app_dynamic_search` to find brand discussions across subreddits.

### 3. News monitoring

Use `tavily_search` with topic "news" and brand name.
Use `google_news_bulk_articles` for comprehensive news coverage.

### 4. Chinese platform monitoring (if applicable)

Use `xiaohongshu_app_v2_search_notes` for brand mentions on Xiaohongshu.
Use `weibo_web_search` for Weibo brand mentions.

### 5. Synthesize

Aggregate mentions by platform, sentiment, volume, and trends.

## Output

Return: mention volume by platform, sentiment breakdown (positive/negative/neutral), key influencer mentions, emerging issues, competitive comparison, and trend over time.

## Example tasks

- "Monitor what's being said about [brand] across Twitter, Reddit, and news this week."
- "What's the sentiment toward [brand] on social media right now?"
- "Has [brand] been mentioned in any negative news recently?"
- "Compare social mentions between [our brand] and [competitor brand]."
- "Track [product launch] reception across Twitter, Reddit, and 小红书."
