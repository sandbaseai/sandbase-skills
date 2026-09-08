---
name: site-audit
description: Audit a website's content, structure, SEO health, and technical setup through SandBase. Use when asked for website audit, content audit, SEO health check, site structure analysis, or technical assessment.
---

# Site Audit

Comprehensive website auditing through SandBase. Crawl sites, analyze content, check SEO fundamentals, and assess structure. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

## Operating principles

- Start with site structure before diving into page-level analysis.
- Prioritize issues by impact: broken critical pages > SEO optimizations > nice-to-haves.
- Sample representative pages rather than auditing every page on large sites.
- Report both findings and actionable recommendations.

## Workflow

### 1. Discover site structure

Use `firecrawl_map` to list all pages on the site.
Use `context_dev_crawl_sitemap` for sitemap-based discovery.

### 2. Crawl and extract content

Use `firecrawl_crawl` for multi-page content extraction.
Use `context_dev_scrape_markdown` for individual page content.

### 3. SEO analysis

Use `dataforseo_v3_on_page_content_parsing_live` for structured content analysis.
Use `dataforseo_v3_on_page_keyword_density_live` for keyword optimization.

### 4. Visual and technical

Use `context_dev_capture_screenshot` for visual assessment.
Use `context_dev_scrape_html` for technical HTML analysis.

## Output

Return: site structure overview, page count, content assessment, SEO findings (title tags, headings, keyword usage), technical issues, and prioritized action items.

## Example tasks

- "Audit [website] — structure, content quality, and SEO health."
- "How many pages does [website] have and what types of content?"
- "Check the SEO basics for [URL] — title, headings, keyword density."
- "Crawl [website] and identify thin or duplicate content pages."
- "Take screenshots of [website]'s key pages for a visual audit."
