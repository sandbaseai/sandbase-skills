---
name: competitor-content-intelligence
description: Analyze competitor content coverage and uncover differentiated content opportunities using web search, page extraction, and DataForSEO content analysis. Use when asked for competitor content research, editorial gap analysis, content brief inputs, or topic whitespace.
---

# Competitor Content Intelligence

Compare public content evidence to identify differentiated editorial and landing-page opportunities. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`. The API map fixes the workflow's tool names; Capability Registry remains authoritative for parameters and supported targets.

## Workflow

1. Define the target audience, topic, competitors, market, and conversion goal.
2. Use `exa_search` or `cloudsway_search` to discover relevant competitor pages and source coverage.
3. Use `context_dev_scrape_markdown` and `dataforseo_v3_on_page_content_parsing_live` to inspect selected pages.
4. Use `dataforseo_v3_content_analysis_search_live` to validate broader topic coverage.
5. Report coverage patterns, missing buyer questions, differentiation opportunities, and pages to improve or create.

## Output

Return a page-level evidence table, content gaps, recommended formats, and a prioritized brief backlog. Do not reproduce competitor text beyond short necessary excerpts.
