# SandBase Cash-Flow Input API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Purpose | Capability identifier (`tool_name`) |
|---|---|
| Extract structured AR, AP, cash, or cost data from an authorized report page | `context_dev_extract_structured_data` |
| Read an authorized report page as Markdown | `context_dev_scrape_markdown` |

Use supplied or authorized data only. Keep forecasts separate from source records and label assumptions, missing opening cash, and confidence limits.
