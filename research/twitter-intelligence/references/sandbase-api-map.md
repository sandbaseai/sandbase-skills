# SandBase Twitter API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `twitter_web_search_timeline` | Search tweets by keyword, hashtag, or phrase. |
| `twitter_web_trending` | Discover trending topics globally or by location. |
| `twitter_web_user_profile` | Get user profile details (bio, stats, verified). |
| `twitter_web_tweet_detail` | Get full tweet details with engagement metrics. |
| `twitter_web_user_followers` | List a user's followers. |
| `twitter_web_user_followings` | List accounts a user follows. |
| `twitter_web_user_media` | Get a user's media posts. |
| `twitter_web_user_tweet_replies` | Get a user's replies. |
| `twitter_web_latest_post_comments` | Get recent replies to a tweet. |
| `twitter_web_post_comments` | Get all replies to a tweet. |
| `twitter_web_retweet_user_list` | See who retweeted a tweet. |
| `twitter_bulk_tweet_search` | High-volume batch tweet search. |
| `twitter_bulk_followers` | Batch follower data retrieval. |

Read-only research only. Do not post, like, retweet, or follow on behalf of the user.
