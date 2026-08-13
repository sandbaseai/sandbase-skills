---
name: site-audit
description: Audit a website's content, structure, SEO health, and technical setup through SandBase. Use when asked for website audit, content audit, SEO health check, site structure analysis, or technical assessment.
---

# Site Audit

Comprehensive website auditing through SandBase. Crawl sites, analyze content, check SEO fundamentals, and assess structure. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

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
