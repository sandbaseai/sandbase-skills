# SandBase Programmatic SEO API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Discover keyword patterns and variations | `dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live` |
| Validate shortlisted search volume | `dataforseo_v3_keywords_data_google_ads_search_volume_live` |
| Score keyword difficulty in bulk | `dataforseo_v3_dataforseo_labs_google_bulk_keyword_difficulty_live` |
| Review historical and seasonal interest | `dataforseo_v3_keywords_data_google_trends_explore_live` |
| Find keywords already associated with a target site | `dataforseo_v3_dataforseo_labs_google_keywords_for_site_live` |
| Inspect live organic results and SERP features | `dataforseo_v3_serp_google_organic_live_advanced` |

Use sampled data to validate a page-family hypothesis before scaling it. Do not publish generated pages or change a production site without explicit authorization.
