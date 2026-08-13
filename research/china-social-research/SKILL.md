---
name: china-social-research
description: "Research any topic across China's major social platforms — Weibo, Douyin, Xiaohongshu, Bilibili, and Zhihu — simultaneously. Aggregates discussion volume, sentiment, key opinion leaders, and platform-specific trends for comprehensive China market intelligence."
---

# China Social Research

Research any topic across China's major social platforms — Weibo, Douyin, Xiaohongshu, Bilibili, and Zhihu — simultaneously. Aggregates discussion volume, sentiment, key opinion leaders, and platform-specific trends for comprehensive China market intelligence. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `weibo_web_search`
- `douyin_search_general_search_v2`
- `xiaohongshu_app_v2_search_notes`
- `bilibili_web_general_search`
- `zhihu_web_hot_list`
- `kuaishou_app_search_comprehensive`

## Workflow

1. Understand the user's research question, target, and context.
2. Call `sandbase_describe_tool` for each selected tool to confirm parameter schema.
3. Call `sandbase_call_tool` with the exact tool_name and schema-defined arguments.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_describe_tool` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.
