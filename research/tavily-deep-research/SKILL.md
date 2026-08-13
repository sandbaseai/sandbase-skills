---
name: tavily-deep-research
description: Advanced web search, content extraction, and site mapping through Tavily via SandBase. Use when asked for web research, URL content extraction, full article reading, news search, or site structure discovery.
---

# Tavily Deep Research

Advanced web search and content extraction through SandBase's Tavily integration. Search the web with depth control, extract clean content from URLs, and discover site structures. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use Tavily for current, real-time web information that the model's training data may not cover.
- Cite sources with URLs for every factual claim.
- Use appropriate search depth: basic for quick checks, advanced for thorough research.
- Extract full content only when necessary — search snippets are often sufficient.

## Workflow

### 1. Search the web

Use `tavily_search` with parameters:
- `search_depth`: "basic" for quick validation, "advanced" for thorough research
- `topic`: "general", "news", or "finance" to focus results
- `days`: limit to recent results (e.g., 7 for past week)
- `max_results`: 5-20 depending on coverage needs
- `include_domains` / `exclude_domains`: filter by source

### 2. Extract content

Use `tavily_extract` to get clean, readable content from specific URLs.
- Use when search snippets aren't enough and full article text is needed.
- Works on most public web pages — not paywalled content.

### 3. Map site structure

Use `tavily_map` to discover all pages on a website.
- Use for competitor site analysis or content auditing.
- Returns site structure and page list.

## Output

Return: search results with source URLs, extracted content summaries, site maps when relevant, and confidence indicators.

## Example tasks

- "Search the web for the latest news about [topic] in the last 7 days."
- "Extract the full content from this article: [URL]."
- "Research [topic] — find 10 authoritative sources and summarize key findings."
- "Map all pages on [website URL] to understand their content structure."
- "Find recent news about [company] and summarize the key developments."
