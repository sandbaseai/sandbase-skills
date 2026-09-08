# SandBase Programmatic SEO API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Purpose | Capability identifier (`tool_name`) |
|---|---|
| Discover keyword patterns and variations | `dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live` |
| Validate shortlisted search volume | `dataforseo_v3_keywords_data_google_ads_search_volume_live` |
| Score keyword difficulty in bulk | `dataforseo_v3_dataforseo_labs_google_bulk_keyword_difficulty_live` |
| Review historical and seasonal interest | `dataforseo_v3_keywords_data_google_trends_explore_live` |
| Find keywords already associated with a target site | `dataforseo_v3_dataforseo_labs_google_keywords_for_site_live` |
| Inspect live organic results and SERP features | `dataforseo_v3_serp_google_organic_live_advanced` |

Use sampled data to validate a page-family hypothesis before scaling it. Do not publish generated pages or change a production site without explicit authorization.
