# SandBase YouTube API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `youtube_web_v2_general_search` | Search videos by keyword or topic. |
| `youtube_web_v2_general_search_v2` | Enhanced video search with additional filters. |
| `youtube_web_v2_search_channels` | Search for channels by keyword. |
| `youtube_web_v2_search_suggestions` | Get search autocomplete suggestions. |
| `youtube_web_v2_shorts_search` | Search YouTube Shorts. |
| `youtube_web_v2_video_info` | Get video metadata, stats, and description. |
| `youtube_web_v2_video_comments` | Get video comments for sentiment analysis. |
| `youtube_web_v2_video_comment_replies` | Get replies to a specific comment. |
| `youtube_web_v2_video_captions` | Request video caption/transcript extraction. |
| `youtube_web_v2_video_captions_result` | Retrieve extracted captions. |
| `youtube_web_v2_related_videos` | Find videos related to a given video. |
| `youtube_web_v2_channel_videos` | List a channel's video catalog. |
| `youtube_web_v2_channel_shorts` | List a channel's Shorts. |
| `youtube_web_v2_channel_description` | Get channel description and metadata. |
| `youtube_web_v2_channel_community_posts` | Get channel community posts. |
| `youtube_web_v2_channel_id` | Resolve channel ID from URL or name. |

Use for research and analysis only. Do not upload, comment, or engage on YouTube.
