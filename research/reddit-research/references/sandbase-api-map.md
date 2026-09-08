# SandBase Reddit API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `reddit_app_dynamic_search` | Search posts, comments, and communities by keyword. |
| `reddit_app_search_typeahead` | Discover communities and search suggestions. |
| `reddit_app_explore_feed` | Discover trending/recommended content. |
| `reddit_app_subreddit_feed` | Get latest posts from a subreddit. |
| `reddit_app_subreddit_info` | Get community details, rules, and stats. |
| `reddit_app_popular_feed` | Site-wide popular content. |
| `reddit_app_news_feed` | News-focused Reddit content. |
| `reddit_app_home_feed` | Personalized trending feed. |
| `reddit_app_games_feed` | Gaming-related trends. |
| `reddit_app_topic_feed` | Topic-based content feed. |
| `reddit_app_community_highlights` | Community-curated highlights. |
| `reddit_app_post_details` | Full post content and metadata. |
| `reddit_app_post_details_batch` | Batch post details. |
| `reddit_app_post_comments` | Comment threads for a post. |
| `reddit_app_comment_replies` | Nested comment replies. |

Read-only research only. Do not post, vote, comment, or message.
