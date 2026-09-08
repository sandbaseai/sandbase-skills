# SandBase 抖音 API Map

下列能力标识仅用于检索，不是直接调用的 MCP 工具名。先用 `sandbase_discover(q: "<供应商和能力>")` 查找匹配端点，再将返回的 `name` 传给 `sandbase_inspect`，读取当前 `inputSchema`、价格和 `execute_as`。按模板调用 `sandbase_run`，将 `execute_as.arguments.name` 作为 `name`，并传入符合 schema 的 `arguments`。若返回 `run_id`，在任务预算内通过 `sandbase_run_get(run_id: "<返回的 run_id>")` 查询至 `completed` 或 `failed`；超出预算时报告待完成状态，失败时报告错误，不自动重复提交。

| Capability identifier | 用途 |
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
