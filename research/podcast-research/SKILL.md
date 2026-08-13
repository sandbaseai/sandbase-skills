---
name: podcast-research
description: "Research podcasts, episodes, and audio content by searching YouTube (where most podcasts crosspost), web sources, and transcript databases. Discover relevant shows, track guest appearances, and analyze topic coverage in the podcast ecosystem."
---

# Podcast Research

Research podcasts, episodes, and audio content by searching YouTube (where most podcasts crosspost), web sources, and transcript databases. Discover relevant shows, track guest appearances, and analyze topic coverage in the podcast ecosystem. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `youtube_web_v2_general_search`
- `youtube_web_v2_video_captions`
- `exa_search`
- `tavily_search`

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
