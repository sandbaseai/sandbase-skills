# SandBase Web Scraper API Map

Use these tools through the SandBase gateway. Before each call, use `sandbase_describe_tool` to obtain current parameters, then use `sandbase_call_tool` with the exact tool name.

| Tool name | Use it for |
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
