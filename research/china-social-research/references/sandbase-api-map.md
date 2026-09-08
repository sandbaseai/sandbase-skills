# SandBase China Social Research API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `weibo_web_search` | See `sandbase_inspect` for details. |
| `douyin_search_general_search_v2` | See `sandbase_inspect` for details. |
| `xiaohongshu_app_v2_search_notes` | See `sandbase_inspect` for details. |
| `bilibili_web_general_search` | See `sandbase_inspect` for details. |
| `zhihu_web_hot_list` | See `sandbase_inspect` for details. |
| `kuaishou_app_search_comprehensive` | See `sandbase_inspect` for details. |

Read-only research only. Do not take actions on external platforms.
