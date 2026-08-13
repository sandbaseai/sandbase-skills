---
name: kol-discovery
description: Discover and evaluate KOLs (Key Opinion Leaders) and creators across TikTok, Instagram, YouTube, and Xiaohongshu through SandBase. Use when asked for influencer research, creator outreach lists, KOL evaluation, or partnership prospecting.
---

# KOL Discovery

Cross-platform influencer and creator discovery through SandBase. Find, evaluate, and compare creators across TikTok, Instagram, YouTube, and Xiaohongshu. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Evaluate creators by engagement rate, not just follower count.
- Cross-platform presence indicates established creators.
- Engagement rate = (likes + comments) / followers for each platform.
- Focus on content relevance and audience fit, not vanity metrics.
- Respect creator privacy — only report on public information.

## Workflow

### 1. Discover on TikTok

Use `tiktok_app_v3_general_search_result` to search by niche keyword.
Use `tiktok_app_v3_creator_info` for creator profile and stats.
Use `tiktok_app_v3_creator_search_insights` for performance data.

### 2. Discover on Instagram

Use `instagram_v3_general_search` to find creators by keyword.
Use `instagram_v3_user_profile` for profile details and metrics.
Use `instagram_v3_user_posts` to evaluate content quality and engagement.
Use `instagram_v3_similar_users` to find more creators in the same niche.

### 3. Discover on YouTube

Use `youtube_web_v2_search_channels` to find channels by niche.
Use `youtube_web_v2_channel_videos` to evaluate content and consistency.
Use `youtube_web_v2_channel_description` for channel positioning.

### 4. Discover on 小红书

Use `xiaohongshu_app_v2_search_users` to find creators.
Use `xiaohongshu_app_v2_user_info` for profile and fan count.
Use `xiaohongshu_app_v2_user_posted_notes` for content analysis.

## Output

Return: ranked creator list with metrics (followers, engagement rate, content fit), cross-platform presence, content style assessment, and outreach recommendation.

## Example tasks

- "Find 10 TikTok creators in the [niche] space with 50K-500K followers."
- "Evaluate @[creator] across all platforms — followers, engagement, content fit for [brand]."
- "Build an influencer outreach list for a [product category] launch in [market]."
- "Find 小红书 KOLs who post about [category] with high engagement."
- "Compare creator engagement rates between TikTok and Instagram for [niche]."
