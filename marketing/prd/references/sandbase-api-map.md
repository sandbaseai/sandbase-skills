# SandBase PRD Research API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Purpose | Capability identifier (`tool_name`) |
|---|---|
| Search current product, market, and technical evidence | `tavily_search` |
| Read an authorized product, documentation, or competitor page | `context_dev_scrape_markdown` |

Use external evidence only when it materially informs requirements. Cite sources and mark unresolved product decisions as TBD.
