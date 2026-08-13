---
name: pricing-page-analyzer
description: "Extract and analyze pricing information from competitor websites. Identifies pricing tiers, features per tier, billing models, and positioning relative to market alternatives. Ideal for competitive pricing strategy and market positioning research."
---

# Pricing Page Analyzer

Extract and analyze pricing information from competitor websites. Identifies pricing tiers, features per tier, billing models, and positioning relative to market alternatives. Ideal for competitive pricing strategy and market positioning research. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `strale_pricing_page_extract`
- `context_dev_extract_structured_data`

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
