---
name: douyin-research
description: 通过 SandBase 搜索抖音视频、分析创作者、追踪话题趋势。适用于抖音内容研究、达人分析、挑战赛追踪、直播研究等场景。
---

# 抖音研究

抖音内容与创作者研究工具。搜索视频、分析达人、追踪挑战赛和话题趋势。使用前请阅读 [API 映射表](references/sandbase-api-map.md)。

## 调用 SandBase 能力

每次调用前先使用 `sandbase_describe_tool` 获取当前参数 schema，再使用 `sandbase_call_tool` 传入准确的 `tool_name`。

## 操作原则

- 仅用于公开内容的研究和分析，不发布或互动。
- 保留归因：视频链接、作者、播放量、发布时间。
- 抖音数据时效性强，热点内容变化快。

## 工作流

### 1. 搜索与发现

使用 `douyin_search_general_search_v2` 综合搜索（视频、用户、话题）。
使用 `douyin_search_video_search_v2` 搜索视频。
使用 `douyin_search_user_search_v2` 搜索用户/创作者。
使用 `douyin_search_challenge_search_v2` 搜索挑战赛/话题。
使用 `douyin_search_music_search` 搜索音乐。
使用 `douyin_search_live_search_v1` 搜索直播。

### 2. 内容分析

使用抖音 app-v3 相关接口获取视频详情和互动数据。

### 3. 趋势追踪

使用 `douyin_search_search_suggest` 获取搜索联想词。
使用挑战赛搜索追踪话题趋势。

## 输出

返回：搜索结果概览、视频热度分析、创作者画像、话题趋势、内容策略洞察。

## 示例任务

- "搜索抖音上关于 [话题] 的热门视频。"
- "找出 [品类] 领域的抖音头部达人。"
- "追踪 #[挑战赛] 的参与量和热度变化。"
- "分析 [品牌] 在抖音上的内容营销策略。"
- "最近抖音上有哪些爆款内容模式？"
