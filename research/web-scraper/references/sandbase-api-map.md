# SandBase Web Scraper API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `context_dev_scrape_markdown` | Extract page content as clean Markdown. |
| `context_dev_scrape_html` | Extract raw HTML. |
| `context_dev_capture_screenshot` | Capture page screenshot. |
| `context_dev_scrape_images` | Extract images from a page. |
| `context_dev_scrape_fonts` | Extract font information. |
| `context_dev_crawl_site` | Crawl a site following links. |
| `context_dev_crawl_sitemap` | Crawl via sitemap. |
| `context_dev_extract_product` | Extract structured product data. |
| `context_dev_extract_products` | Extract product listings. |
| `context_dev_extract_structured_data` | Extract custom structured data with schema. |
| `context_dev_extract_styleguide` | Extract design/brand styleguide. |
| `context_dev_retrieve_brand` | Retrieve brand assets and info. |
| `firecrawl_scrape` | Advanced single-page scrape with options. |
| `firecrawl_crawl` | Multi-page site crawl. |
| `firecrawl_map` | Discover all URLs on a site. |
| `firecrawl_search` | Search within crawled content. |
| `firecrawl_batch` | Batch scraping operations. |

Respect website terms of service. These tools handle rate limiting automatically.
