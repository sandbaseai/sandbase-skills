# SandBase Support Evidence API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Purpose | Capability identifier (`tool_name`) |
|---|---|
| Search public status pages, documentation, and known issues | `tavily_search` |
| Read an authorized knowledge-base or incident page | `context_dev_scrape_markdown` |

Use these capabilities for public or user-authorized evidence only. Keep triage read-only unless the user separately authorizes a response, assignment, or escalation.
