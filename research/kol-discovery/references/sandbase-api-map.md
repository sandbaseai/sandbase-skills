# SandBase KOL Discovery API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `tiktok_app_v3_general_search_result` | Search TikTok by niche keyword. |
| `tiktok_app_v3_creator_info` | Get TikTok creator profile and stats. |
| `tiktok_app_v3_creator_search_insights` | Creator performance analytics. |
| `instagram_v3_general_search` | Search Instagram creators. |
| `instagram_v3_user_profile` | Get Instagram profile and metrics. |
| `instagram_v3_user_posts` | Evaluate content and engagement. |
| `instagram_v3_similar_users` | Find similar creators. |
| `youtube_web_v2_search_channels` | Search YouTube channels by niche. |
| `youtube_web_v2_channel_videos` | Evaluate channel content. |
| `youtube_web_v2_channel_description` | Channel positioning info. |
| `xiaohongshu_app_v2_search_users` | Search 小红书 creators. |
| `xiaohongshu_app_v2_user_info` | Get creator profile and stats. |
| `xiaohongshu_app_v2_user_posted_notes` | Evaluate content quality. |

Evaluate engagement rate and content fit, not just follower count.
