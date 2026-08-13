---
name: twitter-intelligence
description: Search tweets, analyze trends, monitor users, and gather social intelligence from Twitter/X through SandBase. Use when asked for Twitter research, social listening, trend analysis, influencer monitoring, sentiment tracking, or competitor social intelligence.
---

# Twitter Intelligence

Full-spectrum Twitter/X research and social listening through SandBase. Search public tweets, discover trends, analyze user profiles, and monitor discussions — all read-only, never posts or engages. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use Twitter data as social signal evidence, not as representative public opinion.
- Separate observations (tweet volume, engagement, accounts posting) from interpretation (sentiment, trend direction).
- Preserve attribution: include tweet URLs, usernames, dates, and engagement metrics.
- Never post, like, retweet, follow, or engage on behalf of the user.
- Keep monitored accounts and strategy confidential unless sharing is requested.

## Workflow

### 1. Frame the research

Classify the request:
- **Trend discovery**: what's trending, emerging topics
- **Topic monitoring**: track discussions around a keyword or brand
- **User analysis**: profile, content, followers, engagement patterns
- **Sentiment tracking**: how people feel about a topic or brand
- **Competitor intelligence**: what competitors post and how audiences respond

### 2. Search tweets

Use `twitter_web_search_timeline` for keyword-based tweet discovery:
- Search for brand names, product names, hashtags, or topic phrases
- Use negative keywords to filter noise
- Compare search results for competitors side by side

Use `twitter_bulk_tweet_search` for higher-volume batch searches.

### 3. Discover trends

Use `twitter_web_trending` to find what's trending globally or by location.

### 4. Analyze users

Use `twitter_web_user_profile` for account details (bio, follower count, verified status).
Use `twitter_web_user_media` and tweet timeline tools for content analysis.
Use `twitter_web_user_followers` / `twitter_web_user_followings` for network analysis.

### 5. Deep-dive tweets

Use `twitter_web_tweet_detail` for specific tweet metrics and thread context.
Use `twitter_web_latest_post_comments` or `twitter_web_post_comments` for reply analysis.

## Output

Return: search scope, tweet volume summary, key accounts involved, sentiment signals, trend indicators, engagement patterns, and evidence gaps.

## Example tasks

- "What are people saying about [brand] on Twitter this week?"
- "Find trending topics in the AI/tech space right now."
- "Analyze @competitor's Twitter presence — posting frequency, engagement, top content."
- "Monitor mentions of [product launch] and summarize sentiment."
- "Who are the most influential voices discussing [topic] on Twitter?"

## Failure handling

- If SandBase is unavailable, report the failure and do not substitute a direct API.
- If searches return few results, try broader terms or related hashtags.
- If a user account is private/suspended, note the gap and continue with available data.
