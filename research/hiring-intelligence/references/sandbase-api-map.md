# SandBase Hiring Intelligence API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `linkedin_web_v2_search_jobs` | See `sandbase_inspect` for details. |
| `linkedin_web_v2_job_detail` | See `sandbase_inspect` for details. |
| `linkedin_web_v2_company_profile` | See `sandbase_inspect` for details. |
| `apollo_company_job_postings` | See `sandbase_inspect` for details. |
| `apollo_company_search` | See `sandbase_inspect` for details. |

Read-only research only. Do not take actions on external platforms.
