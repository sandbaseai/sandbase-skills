---
name: web-scraper
description: Scrape web pages, crawl sites, extract structured data, and capture screenshots through SandBase. Use when asked to extract content from URLs, crawl websites, get structured data from pages, take screenshots, or convert web pages to markdown.
---

# Web Scraper

Universal web scraping and data extraction through SandBase. Scrape individual pages, crawl entire sites, extract structured data, and capture visual snapshots. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Respect robots.txt and rate limits — these tools handle that automatically.
- Use the lightest tool for the job: markdown scrape before full crawl.
- Structured data extraction is best for product pages, directories, and lists.
- Screenshots are useful for visual verification and design research.

## Workflow

### 1. Single page extraction

Use `context_dev_scrape_markdown` for clean Markdown output (best for articles, docs).
Use `context_dev_scrape_html` for raw HTML (best for structure analysis).
Use `firecrawl_scrape` for advanced single-page extraction with options.

### 2. Site crawling

Use `firecrawl_crawl` to crawl multiple pages following links.
Use `firecrawl_map` to discover all URLs on a site.
Use `context_dev_crawl_site` for site-wide content extraction.
Use `context_dev_crawl_sitemap` for sitemap-based crawling.

### 3. Structured data extraction

Use `context_dev_extract_structured_data` for custom schema extraction from pages.
Use `context_dev_extract_product` for single product data.
Use `context_dev_extract_products` for product listing pages.

### 4. Visual and metadata

Use `context_dev_capture_screenshot` for visual page snapshots.
Use `context_dev_scrape_images` for image extraction.
Use `context_dev_scrape_fonts` for typography analysis.
Use `context_dev_retrieve_brand` for brand asset extraction.

## Output

Return: extracted content in requested format, structured data as JSON, screenshot URLs, or crawl results with page list.

## Example tasks

- "Extract the content from this article as clean Markdown: [URL]."
- "Crawl [website] and list all their product pages."
- "Extract product name, price, and description from this page: [URL]."
- "Take a screenshot of [URL] at desktop resolution."
- "Map all pages on [website] and categorize by content type."
