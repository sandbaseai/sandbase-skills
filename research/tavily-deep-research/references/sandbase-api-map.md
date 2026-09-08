# SandBase Tavily API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `tavily_search` | AI-optimized web search with depth control, topic filtering, and domain filtering. |
| `tavily_extract` | Extract clean, readable content from one or more URLs. |
| `tavily_map` | Discover site structure and list all pages on a website. |

Use appropriate search depth for the task. Cite all sources with URLs.
