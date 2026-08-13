---
name: serp-analysis
description: Analyze Google search results, SERP features, and organic rankings through SandBase DataForSEO. Use when asked for SERP analysis, Google ranking research, search feature identification, or organic visibility assessment.
---

# SERP Analysis

Google Search Engine Results Page analysis through SandBase. Inspect live organic rankings, identify SERP features, discover related searches, and analyze autocomplete suggestions. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- SERP data is a snapshot — rankings change. Note the observation timestamp.
- Distinguish organic results from paid, featured snippets, and other SERP features.
- Specify country, language, and device for accurate results.
- Use related searches and autocomplete for query expansion research.

## Workflow

### 1. Inspect organic SERP

Use `dataforseo_v3_serp_google_organic_live_advanced` to get live organic results for a query.

### 2. Discover related queries

Use `dataforseo_v3_serp_google_related_searches_live_advanced` to find related searches.
Use `dataforseo_v3_serp_google_autocomplete_live_advanced` for autocomplete suggestions.

## Output

Return: top organic results (title, URL, position, SERP features), featured snippets, People Also Ask, related searches, and competitive analysis.

## Example tasks

- "What's ranking on page 1 of Google for [keyword] in the US?"
- "What SERP features appear for [keyword]? (featured snippet, videos, images, PAA)"
- "Find Google autocomplete suggestions for [seed keyword]."
- "What related searches does Google show for [query]?"
- "Compare the SERP for [keyword A] vs [keyword B] — who ranks for both?"
