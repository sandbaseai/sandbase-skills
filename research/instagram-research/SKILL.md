---
name: instagram-research
description: Search content, analyze profiles, track hashtags, and research competitors on Instagram through SandBase. Use when asked for Instagram research, influencer analysis, hashtag tracking, content strategy research, or competitor social monitoring.
---

# Instagram Research

Instagram content and creator research through SandBase. Search posts, analyze profiles, track hashtag trends, and gather competitive intelligence. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use Instagram data for market research and competitive intelligence only.
- Preserve attribution: include post URLs, usernames, engagement metrics, dates.
- Respect user privacy — focus on public accounts and public content.
- Never attempt to follow, like, comment, or message on behalf of the user.

## Workflow

### 1. Search and discover

Use `instagram_v3_general_search` to find accounts, hashtags, and places.
Use `instagram_v3_hashtag_posts` to track content around specific hashtags.
Use `instagram_v3_explore` to discover trending content.

### 2. Analyze profiles

Use `instagram_v3_user_profile` for account details (bio, followers, post count).
Use `instagram_v3_user_posts` for recent content and engagement patterns.
Use `instagram_v3_user_reels` for Reels strategy analysis.
Use `instagram_v3_user_highlights` for curated content themes.

### 3. Analyze content

Use `instagram_v3_post_info` for detailed post metrics (likes, comments, caption).
Use `instagram_v3_post_comments` for audience sentiment and engagement quality.
Use `instagram_v3_post_likes` to see who engages with content.

### 4. Location and music research

Use `instagram_v3_location_posts` for location-based content discovery.
Use `instagram_v3_music_posts` to find content using specific audio.

## Output

Return: search results, profile analysis (followers, engagement rate, content themes), hashtag performance, content patterns, and competitive positioning.

## Example tasks

- "Analyze @competitor's Instagram — posting frequency, engagement rate, content themes."
- "Find top posts for #[hashtag] in the last week."
- "Who are the top Instagram influencers in [niche] with 50K-500K followers?"
- "What content format performs best for [brand] on Instagram?"
- "Track how [campaign hashtag] is performing in terms of post volume and engagement."
