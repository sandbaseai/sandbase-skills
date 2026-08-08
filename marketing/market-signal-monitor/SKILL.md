---
name: market-signal-monitor
description: Monitor non-financial market, product, and audience signals across web, Reddit, search trends, and company news. Use when asked to assess emerging demand, category movement, launch signals, competitor momentum, or weekly market intelligence.
---

# Market Signal Monitor

Build a time-bounded signal brief from independent public sources. This is not financial analysis or investment advice.

## Workflow

1. Define topic, geography, time window, and the decision the brief supports.
2. Use `exa_search` or `cloudsway_search` for current web signals and `akta_news` for company or industry news.
3. Use `reddit_app_dynamic_search` for relevant public community discussion.
4. Use `dataforseo_v3_keywords_data_google_trends_explore_live` for search-interest movement when a query is available.
5. Classify signals by source, recency, strength, and uncertainty; never claim causality from a single source.

## Output

Return a dated signal timeline, converging and conflicting evidence, implications, monitoring queries, and next validation actions.
