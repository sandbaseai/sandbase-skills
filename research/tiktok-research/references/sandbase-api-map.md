# SandBase TikTok API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `tiktok_app_v3_general_search_result` | Search videos by keyword or topic. |
| `tiktok_app_v3_hashtag_search_result` | Search for hashtags. |
| `tiktok_app_v3_hashtag_video_list` | Get videos under a hashtag. |
| `tiktok_app_v3_hashtag_detail` | Get hashtag metadata and stats. |
| `tiktok_app_v3_home_feed` | Discover trending For You content. |
| `tiktok_app_v3_creator_info` | Get creator profile and metrics. |
| `tiktok_app_v3_creator_search_insights` | Creator search performance data. |
| `tiktok_app_v3_creator_search_insights_trend` | Creator trend analytics. |
| `tiktok_app_v3_creator_search_insights_videos` | Creator top videos by search. |
| `tiktok_app_v3_one_video` | Get single video details and metrics. |
| `tiktok_app_v3_multi_video` | Batch video details. |
| `tiktok_app_v3_music_video_list` | Videos using a specific sound. |
| `tiktok_app_v3_music_detail` | Sound/music metadata. |
| `tiktok_app_v3_music_chart_list` | Trending music charts. |
| `tiktok_app_v3_live_room_info` | Live stream details. |
| `tiktok_app_v3_live_ranking_list` | Top live creators. |
| `tiktok_app_v3_live_room_product_list` | Products in a live stream. |

Read-only research only. Do not post, like, or engage on TikTok.
