---
name: multi-source-search
description: Parallel multi-source search combining Web, Academic, Tavily, Exa, and Cloudsway results with cross-source validation. Use when asked for comprehensive research requiring multiple perspectives, fact-checking, or thorough topic coverage.
---

# Multi-Source Search

Parallel multi-source research through SandBase. Query multiple search backends simultaneously, cross-validate findings, and deliver comprehensive research with confidence scoring. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use multiple sources to validate claims — single-source findings are hypotheses.
- Score confidence based on source agreement: 3+ sources = high, 2 = medium, 1 = low.
- Each source has strengths: Exa for semantic relevance, Tavily for recency, Scholar for academic rigor, Cloudsway for broad coverage.
- Cite which source(s) back each finding.

## Workflow

### 1. Search across sources

Use `tavily_search` for current web results with recency control.
Use `exa_search` for semantic, high-quality source discovery.
Use `scholar_search_mixed` for academic and web combined.
Use `cloudsway_search` for broad web coverage.

### 2. Deep extraction (if needed)

Use `exa_contents` to extract content from selected Exa results.
Use `tavily_extract` to extract content from selected URLs.

### 3. Synthesize

Cross-reference findings, note agreements and disagreements, produce confidence-scored summary.

## Output

Return: findings organized by confidence level, source map, agreements/disagreements between sources, and research gaps.

## Example tasks

- "Research [topic] thoroughly — use at least 3 different search sources."
- "Fact-check this claim: [statement]. Cross-reference multiple sources."
- "Find everything published about [topic] in the last month across web and academic sources."
- "Compare what different sources say about [controversial topic]."
- "Deep research on [company/product] — web, academic, and news perspectives."
