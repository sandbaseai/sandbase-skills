# SandBase Competitor Monitor API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `firecrawl_scrape` | Extract competitor page content. |
| `firecrawl_map` | Discover competitor site structure. |
| `context_dev_scrape_markdown` | Extract page as clean Markdown. |
| `context_dev_capture_screenshot` | Visual page monitoring. |
| `exa_search` | Find competitor content by domain. |
| `dataforseo_v3_serp_google_organic_live_advanced` | Check competitor search rankings. |
| `twitter_web_search_timeline` | Monitor competitor Twitter mentions. |
| `linkedin_web_v2_company_posts` | Track competitor LinkedIn activity. |
| `youtube_web_v2_channel_videos` | Monitor competitor YouTube content. |
| `tavily_search` | Search competitor news coverage. |
| `google_news_bulk_articles` | Track competitor news articles. |

Compare like-for-like across same time periods and metrics.
