---
name: tiktok-research
description: Search videos, analyze creators, track hashtags, and discover trends on TikTok through SandBase. Use when asked for TikTok research, content discovery, creator analysis, hashtag trends, viral content patterns, or short-form video strategy.
---

# TikTok Research

TikTok content and creator intelligence through SandBase. Search videos, analyze creator profiles, track hashtag performance, discover trending content, and research live streams. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use TikTok data for content research and market intelligence only.
- Preserve attribution: include video URLs, creator handles, view counts, dates.
- TikTok metrics are volatile — note observation timestamps.
- Never attempt to post, like, comment, or follow on the platform.

## Workflow

### 1. Search and discover

Use `tiktok_app_v3_general_search_result` for keyword/topic video discovery.
Use `tiktok_app_v3_hashtag_search_result` to find hashtags by keyword.
Use `tiktok_app_v3_hashtag_video_list` to get videos under a specific hashtag.
Use `tiktok_app_v3_home_feed` to see what's trending on For You.

### 2. Analyze creators

Use `tiktok_app_v3_creator_info` for creator profile and stats.
Use `tiktok_app_v3_creator_search_insights` for creator search performance.
Use `tiktok_app_v3_creator_search_insights_trend` for creator trend data.
Use `tiktok_app_v3_creator_search_insights_videos` for top-performing videos.

### 3. Analyze content

Use `tiktok_app_v3_one_video` for detailed video metrics.
Use `tiktok_app_v3_multi_video` for batch video analysis.
Use `tiktok_app_v3_music_video_list` for content using specific sounds.
Use `tiktok_app_v3_music_detail` for sound/music metadata.

### 4. Live and commerce

Use `tiktok_app_v3_live_room_info` for live stream details.
Use `tiktok_app_v3_live_ranking_list` for top live creators.
Use `tiktok_app_v3_live_room_product_list` for live commerce research.

## Output

Return: search results, creator analysis (followers, engagement, content themes), hashtag performance, trending content patterns, and competitive insights.

## Example tasks

- "Find trending TikTok videos about [topic] this week."
- "Analyze @creator's TikTok presence — follower growth, top videos, posting pattern."
- "What hashtags are performing best in the [niche] space on TikTok?"
- "Find TikTok creators in [niche] with 100K-1M followers."
- "What sounds/music are trending on TikTok right now?"
