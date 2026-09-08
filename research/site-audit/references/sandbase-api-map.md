# SandBase Site Audit API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `firecrawl_map` | Discover all URLs on a site. |
| `firecrawl_crawl` | Multi-page content crawling. |
| `context_dev_crawl_sitemap` | Sitemap-based page discovery. |
| `context_dev_scrape_markdown` | Extract page content as Markdown. |
| `context_dev_scrape_html` | Extract raw HTML for technical analysis. |
| `context_dev_capture_screenshot` | Visual page assessment. |
| `dataforseo_v3_on_page_content_parsing_live` | Structured content and SEO analysis. |
| `dataforseo_v3_on_page_keyword_density_live` | Keyword usage and density. |

Start with structure discovery, then sample representative pages for detailed analysis.
