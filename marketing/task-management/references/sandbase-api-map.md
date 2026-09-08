# SandBase Task Source Import API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Purpose | Capability identifier (`tool_name`) |
|---|---|
| Read a task source page as Markdown | `context_dev_scrape_markdown` |
| Extract task fields from a structured web page | `context_dev_extract_structured_data` |

Use these capabilities only when the user supplies an authorized source URL. For a local TASKS.md file or pasted text, work directly from that input.
