---
name: reddit-research
description: Search discussions, track communities, analyze posts, and discover trends on Reddit through SandBase. Use when asked for Reddit research, community analysis, trending topics, discussion monitoring, content discovery, or audience insight beyond customer-focused research.
---

# Reddit Research

General-purpose Reddit research and community intelligence through SandBase. Search across all of Reddit, monitor subreddits, analyze discussions, and discover trending content. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Read-only research. Never post, vote, comment, or message.
- Treat Reddit as qualitative community signal, not representative polling.
- Preserve provenance: post URLs, subreddit, score, date, comment count.
- Search across multiple subreddits to avoid single-community bias.

## Workflow

### 1. Discover and search

Use `reddit_app_dynamic_search` for keyword search across all of Reddit.
Use `reddit_app_search_typeahead` for community and topic discovery.
Use `reddit_app_explore_feed` for trending/recommended content.

### 2. Monitor communities

Use `reddit_app_subreddit_feed` for latest posts in a community.
Use `reddit_app_subreddit_info` for community details and rules.
Use `reddit_app_popular_feed` for site-wide popular content.
Use `reddit_app_news_feed` for news-focused content.

### 3. Analyze discussions

Use `reddit_app_post_details` for full post content and metadata.
Use `reddit_app_post_comments` for comment threads.
Use `reddit_app_comment_replies` for nested reply analysis.
Use `reddit_app_post_details_batch` for batch post analysis.

### 4. Specialized feeds

Use `reddit_app_home_feed` for personalized trending.
Use `reddit_app_games_feed` for gaming-related trends.
Use `reddit_app_community_highlights` for community-curated content.
Use `reddit_app_topic_feed` for topic-based feeds.

## Output

Return: search results, community analysis, trending topics, discussion sentiment, engagement patterns, and content themes.

## Example tasks

- "What's trending on Reddit right now across tech subreddits?"
- "Search Reddit for discussions about [topic/product] in the last week."
- "Analyze r/[subreddit] — what are the most common discussion themes?"
- "Find the most upvoted posts about [topic] in the last month."
- "What are people on Reddit saying about [company/product launch]?"
