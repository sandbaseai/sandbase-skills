# SandBase DataForSEO Keyword Search API Map

Use these SandBase `tool_name` values through `sandbase_call_tool`. They are the SEO capability set observed for this Skill. Before each call, use `sandbase_describe_tool` for the current input schema; SandBase owns authentication, API routing, and provider credentials.

## Site understanding

| Purpose | tool_name |
|---|---|
| Parse a page into structured content or Markdown | `dataforseo_v3_on_page_content_parsing_live` |
| Analyze existing page keyword density | `dataforseo_v3_on_page_keyword_density_live` |

Start a site-based research request with `dataforseo_v3_on_page_content_parsing_live` for the homepage and representative product, use-case, pricing, docs, or content pages.

## Keyword discovery

| Purpose | tool_name |
|---|---|
| Expand a seed with keyword suggestions and metrics | `dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live` |
| Generate keyword ideas with volume and CPC | `dataforseo_v3_dataforseo_labs_google_keyword_ideas_live` |
| Find related terms with shared SERP patterns | `dataforseo_v3_dataforseo_labs_google_related_keywords_live` |
| Generate Google Ads ideas from seed keywords | `dataforseo_v3_keywords_data_google_ads_keywords_for_keywords_live` |
| Generate Google Ads ideas from a site | `dataforseo_v3_keywords_data_google_ads_keywords_for_site_live` |
| Find Google autocomplete queries | `dataforseo_v3_serp_google_autocomplete_live_advanced` |
| Find related Google searches | `dataforseo_v3_serp_google_related_searches_live_advanced` |

## Demand and feasibility

| Purpose | tool_name |
|---|---|
| Retrieve Google Ads search volume and competition | `dataforseo_v3_keywords_data_google_ads_search_volume_live` |
| Retrieve Bing seed-keyword ideas | `dataforseo_v3_keywords_data_bing_keywords_for_keywords_live` |
| Retrieve Bing site-keyword ideas | `dataforseo_v3_keywords_data_bing_keywords_for_site_live` |
| Retrieve Bing search volume | `dataforseo_v3_keywords_data_bing_search_volume_live` |
| Score keyword difficulty in bulk | `dataforseo_v3_dataforseo_labs_google_bulk_keyword_difficulty_live` |
| Retrieve historical monthly search volume | `dataforseo_v3_dataforseo_labs_google_historical_search_volume_live` |
| Retrieve Google Trends interest over time | `dataforseo_v3_keywords_data_google_trends_explore_live` |

Use a small, diverse seed set for discovery. Validate only shortlisted candidates with demand and difficulty tools; do not convert unavailable data into an estimate.

## Target-site visibility and competitor intelligence

| Purpose | tool_name |
|---|---|
| Find keywords a site ranks for | `dataforseo_v3_dataforseo_labs_google_keywords_for_site_live` |
| Retrieve a domain's ranked keywords | `dataforseo_v3_dataforseo_labs_google_ranked_keywords_live` |
| Identify competing domains | `dataforseo_v3_dataforseo_labs_google_competitors_domain_live` |
| Compare keyword overlap between two domains | `dataforseo_v3_dataforseo_labs_google_domain_intersection_live` |
| Find SERP competitors for a keyword set | `dataforseo_v3_dataforseo_labs_google_serp_competitors_live` |

For domain tools, normalize domains to the schema's expected form, typically without a protocol or `www`. Use the same market and language across a comparison.

## SERP validation

| Market / engine | tool_name |
|---|---|
| Google organic | `dataforseo_v3_serp_google_organic_live_advanced` |
| Google related searches | `dataforseo_v3_serp_google_related_searches_live_advanced` |
| Bing organic | `dataforseo_v3_serp_bing_organic_live_advanced` |
| Baidu organic | `dataforseo_v3_serp_baidu_organic_live_advanced` |
| Naver organic | `dataforseo_v3_serp_naver_organic_live_advanced` |
| Yahoo organic | `dataforseo_v3_serp_yahoo_organic_live_advanced` |
| Yandex organic | `dataforseo_v3_serp_yandex_organic_live_regular` |

Inspect organic SERPs for priority terms and the strongest term in each cluster. Choose the engine that matches the research market. Use platform or community-search tools only when the request specifically calls for them; they are not a replacement for organic SERP evidence.

## Gateway call pattern

```text
1. sandbase_describe_tool({ name: "<tool_name>" })
2. sandbase_call_tool({
     name: "<tool_name>",
     arguments: { /* only current schema-defined fields */ }
   })
```

Do not call provider URLs directly. Do not expose authorization values, generated credentials, or raw customer exports.
