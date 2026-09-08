# SandBase Backlink API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `dataforseo_v3_backlinks_summary_live` | Summarize a domain or page backlink profile. |
| `dataforseo_v3_backlinks_referring_domains_live` | List referring domains and their backlink evidence. |
| `dataforseo_v3_backlinks_competitors_live` | Find domains competing for similar backlinks. |
| `dataforseo_v3_backlinks_backlinks_live` | Inspect individual competitor-earned backlinks. |
| `dataforseo_v3_backlinks_anchors_live` | Assess anchor-text patterns and topical relevance. |
| `dataforseo_v3_backlinks_domain_pages_live` | Identify pages that attract links and potential asset patterns. |

Do not use these read-only research tools to send outreach, create links, or alter a third-party site.
