---
name: product-intelligence
description: "Research products across Amazon, Google Shopping, and Xiaohongshu to understand pricing, reviews, market positioning, and consumer sentiment. Covers competitive product analysis, pricing benchmarks, feature comparison, and customer satisfaction signals."
---

# Product Intelligence

Research products across Amazon, Google Shopping, and Xiaohongshu to understand pricing, reviews, market positioning, and consumer sentiment. Covers competitive product analysis, pricing benchmarks, feature comparison, and customer satisfaction signals. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `amazon_bulk_product_details`
- `amazon_bulk_reviews_multi_region`
- `google_shopping_bulk_products`
- `xiaohongshu_app_v2_search_products`
- `xiaohongshu_app_v2_product_reviews`
- `strale_product_reviews_extract`

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
