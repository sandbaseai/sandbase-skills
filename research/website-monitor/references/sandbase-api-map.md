# SandBase Website Monitor API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `firecrawl_scrape` | See `sandbase_inspect` for details. |
| `context_dev_capture_screenshot` | See `sandbase_inspect` for details. |
| `strale_ssl_check` | See `sandbase_inspect` for details. |
| `strale_header_security_check` | See `sandbase_inspect` for details. |
| `strale_website_health` | See `sandbase_inspect` for details. |
| `strale_page_speed_test` | See `sandbase_inspect` for details. |

Read-only research only. Do not take actions on external platforms.
