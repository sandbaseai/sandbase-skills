# SandBase Instagram API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `instagram_v3_general_search` | Search accounts, hashtags, and places. |
| `instagram_v3_user_profile` | Get user profile details and stats. |
| `instagram_v3_user_posts` | Get a user's recent posts. |
| `instagram_v3_user_reels` | Get a user's Reels. |
| `instagram_v3_user_highlights` | Get a user's story highlights. |
| `instagram_v3_user_stories` | Get a user's current stories. |
| `instagram_v3_hashtag_posts` | Get posts for a specific hashtag. |
| `instagram_v3_post_info` | Get detailed post information and metrics. |
| `instagram_v3_post_info_by_code` | Get post info using shortcode. |
| `instagram_v3_post_comments` | Get comments on a post. |
| `instagram_v3_post_likes` | Get accounts that liked a post. |
| `instagram_v3_explore` | Discover trending content on Explore. |
| `instagram_v3_location_posts` | Find posts at a specific location. |
| `instagram_v3_music_posts` | Find posts using specific audio/music. |
| `instagram_v3_search_hashtags` | Search for hashtags. |
| `instagram_v3_similar_users` | Find similar accounts. |

Read-only research only. Do not follow, like, comment, or message.
