# SandBase Influencer Analytics API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `tiktok_app_v3_creator_info` | See `sandbase_inspect` for details. |
| `instagram_v3_user_profile` | See `sandbase_inspect` for details. |
| `instagram_v3_user_posts` | See `sandbase_inspect` for details. |
| `youtube_web_v2_channel_videos` | See `sandbase_inspect` for details. |
| `youtube_web_v2_channel_description` | See `sandbase_inspect` for details. |
| `bilibili_web_user_profile` | See `sandbase_inspect` for details. |
| `kuaishou_app_one_user_v2` | See `sandbase_inspect` for details. |

Read-only research only. Do not take actions on external platforms.
