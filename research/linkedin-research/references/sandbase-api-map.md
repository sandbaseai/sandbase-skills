# SandBase LinkedIn API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `linkedin_web_v2_company_profile` | Get company details, size, industry, specialties. |
| `linkedin_web_v2_company_posts` | Get a company's recent posts and engagement. |
| `linkedin_web_v2_user_profile` | Get professional profile and background. |
| `linkedin_web_v2_user_posts` | Get a user's posts and content activity. |
| `linkedin_web_v2_search_jobs` | Search job postings by keyword, location, company. |
| `linkedin_web_v2_job_detail` | Get full job posting details and requirements. |
| `linkedin_web_v2_post_detail` | Get detailed post metrics. |
| `linkedin_web_v2_post_comments` | Get comments and reactions on a post. |

Read-only research only. Do not connect, message, or apply on behalf of the user.
