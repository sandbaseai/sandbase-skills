---
name: youtube-research
description: Search videos, analyze channels, extract captions, read comments, and discover trends on YouTube through SandBase. Use when asked for YouTube research, video discovery, channel analysis, content strategy research, comment sentiment, or video transcript extraction.
---

# YouTube Research

Comprehensive YouTube content research through SandBase. Search videos and channels, analyze engagement, extract captions for content analysis, and discover trends. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

## Operating principles

- Use YouTube data for content research and competitive intelligence, not for manipulation.
- Preserve attribution: include video URLs, channel names, view counts, and dates.
- Separate metrics (views, likes, comments) from qualitative judgments about content quality.
- Captions are useful for topic extraction but may contain transcription errors.

## Workflow

### 1. Search and discover

Use `youtube_web_v2_general_search` for keyword/topic video discovery.
Use `youtube_web_v2_search_channels` to find channels in a niche.
Use `youtube_web_v2_search_suggestions` for query expansion and trend signals.
Use `youtube_web_v2_shorts_search` for short-form content discovery.

### 2. Analyze videos

Use `youtube_web_v2_video_info` for detailed video metadata and metrics.
Use `youtube_web_v2_video_comments` and `youtube_web_v2_video_comment_replies` for audience sentiment.
Use `youtube_web_v2_video_captions` to extract transcripts for content analysis.
Use `youtube_web_v2_related_videos` to understand recommendation patterns.

### 3. Analyze channels

Use `youtube_web_v2_channel_videos` for a channel's content catalog.
Use `youtube_web_v2_channel_description` for channel positioning.
Use `youtube_web_v2_channel_shorts` for short-form strategy analysis.
Use `youtube_web_v2_channel_community_posts` for community engagement.

## Output

Return: search results summary, top videos with metrics, channel analysis, content patterns, audience sentiment from comments, and trend indicators.

## Example tasks

- "Find the most popular videos about [topic] in the last month."
- "Analyze [channel name]'s content strategy — posting frequency, top performers, topics."
- "Extract the transcript from this YouTube video: [URL]."
- "What are people saying in the comments of [video URL]?"
- "Find YouTube channels covering [niche] with 10K-100K subscribers."
