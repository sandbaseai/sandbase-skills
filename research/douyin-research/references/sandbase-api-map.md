# SandBase 抖音 API Map

通过 SandBase gateway 调用。每次调用前先用 `sandbase_describe_tool` 获取参数，再用 `sandbase_call_tool` 传入准确的 tool name。

| Tool name | 用途 |
|---|---|
| `douyin_search_general_search_v2` | 综合搜索（视频、用户、话题）。 |
| `douyin_search_video_search_v2` | 搜索视频。 |
| `douyin_search_user_search_v2` | 搜索用户/创作者。 |
| `douyin_search_challenge_search_v2` | 搜索挑战赛/话题。 |
| `douyin_search_music_search` | 搜索音乐/热门BGM。 |
| `douyin_search_live_search_v1` | 搜索直播。 |
| `douyin_search_search_suggest` | 获取搜索联想/推荐词。 |
| `douyin_search_multi_search` | 多维度综合搜索。 |
| `douyin_search_image_search_v3` | 以图搜图/视觉搜索。 |

仅用于公开内容研究。不发布或互动。
