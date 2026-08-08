# Example Workflows

Each example uses SandBase DataForSEO capabilities as the evidence source. Inspect the current schema with `sandbase_describe_tool` before calling any listed tool.

## 1. Find SEO opportunities for a website

**User request**

```text
Find non-brand keyword opportunities for https://example.com in US English.
```

**Use these capabilities**

1. `dataforseo_v3_on_page_content_parsing_live` for the homepage and representative pages.
2. `dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live` for site-derived seed themes.
3. `dataforseo_v3_keywords_data_google_ads_search_volume_live` and `dataforseo_v3_dataforseo_labs_google_bulk_keyword_difficulty_live` for shortlisted terms.
4. `dataforseo_v3_serp_google_organic_live_advanced` for priority terms.

**Return**: a site brief, keyword clusters, evidence-labelled metrics, and recommended page types.

## 2. Expand one product topic

**User request**

```text
Research “AI agent observability” keywords for a B2B SaaS product in the United States.
```

**Use these capabilities**

1. `dataforseo_v3_dataforseo_labs_google_keyword_ideas_live` and `dataforseo_v3_dataforseo_labs_google_related_keywords_live`.
2. `dataforseo_v3_keywords_data_google_ads_search_volume_live`.
3. `dataforseo_v3_dataforseo_labs_google_bulk_keyword_difficulty_live`.
4. `dataforseo_v3_keywords_data_google_trends_explore_live` for seasonality or emerging demand.

**Return**: a shortlist grouped by problem, commercial fit, difficulty, and trend, with the market and source for each metric.

## 3. Find competitor keyword gaps

**User request**

```text
Compare our-domain.com with competitor-a.com and identify SEO gaps in US English.
```

**Use these capabilities**

1. `dataforseo_v3_dataforseo_labs_google_keywords_for_site_live` or `dataforseo_v3_dataforseo_labs_google_ranked_keywords_live` for each domain.
2. `dataforseo_v3_dataforseo_labs_google_competitors_domain_live` to validate the competitor set.
3. `dataforseo_v3_dataforseo_labs_google_domain_intersection_live` for shared or missing coverage.
4. `dataforseo_v3_serp_google_organic_live_advanced` for only the best gap candidates.

**Return**: coverage gaps, performance gaps, and the smallest set of pages that can address them. Do not claim a gap is valuable without validating commercial fit.

## 4. Improve existing content before creating new URLs

**User request**

```text
Show which pages on example.com should be improved for organic traffic before we create new articles.
```

**Use these capabilities**

1. `dataforseo_v3_dataforseo_labs_google_ranked_keywords_live` to find existing visibility.
2. `dataforseo_v3_dataforseo_labs_google_keywords_for_site_live` to connect keyword rows to the site.
3. `dataforseo_v3_on_page_content_parsing_live` for candidate pages.
4. `dataforseo_v3_serp_google_organic_live_advanced` for the primary query of each shortlisted page.

**Return**: page updates ranked by qualified demand, feasibility, and the risk of creating a competing new URL.
