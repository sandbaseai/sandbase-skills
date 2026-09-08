# SandBase WeChat Channels Research API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `wechat_channels_v2_search_channel_videos` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_channel_info` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_user_videos` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_video_detail` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_video_comments` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_live_detail` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_live_history` | See `sandbase_inspect` for details. |
| `wechat_channels_v2_user_profile` | See `sandbase_inspect` for details. |

Read-only research only. Do not take actions on external platforms.
