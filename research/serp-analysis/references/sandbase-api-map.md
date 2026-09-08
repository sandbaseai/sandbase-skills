# SandBase SERP Analysis API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `dataforseo_v3_serp_google_organic_live_advanced` | Live Google organic SERP with all features. |
| `dataforseo_v3_serp_google_related_searches_live_advanced` | Related searches for a query. |
| `dataforseo_v3_serp_google_autocomplete_live_advanced` | Google autocomplete suggestions. |

Specify country, language, and device for accurate results. SERP data is real-time snapshot.
