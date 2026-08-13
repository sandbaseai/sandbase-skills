---
name: youtube-transcript
description: "Extract full transcripts and captions from YouTube videos for content analysis, summarization, note-taking, and repurposing. Supports multiple languages and auto-generated captions. Ideal for research, content creation, and accessibility workflows."
---

# YouTube Transcript

Extract full transcripts and captions from YouTube videos for content analysis, summarization, note-taking, and repurposing. Supports multiple languages and auto-generated captions. Ideal for research, content creation, and accessibility workflows. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `agentbody_youtube_transcript`
- `youtube_web_v2_video_captions`
- `youtube_web_v2_video_captions_result`

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
