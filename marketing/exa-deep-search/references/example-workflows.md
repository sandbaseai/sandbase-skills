# Example Workflows

Each example uses SandBase Exa capabilities as the evidence source. Resolve capability identifiers with `sandbase_discover`, then use `sandbase_inspect` to read the current schema and pricing before executing its `execute_as` template through `sandbase_run`. Treat any example options as intent to map to the inspected schema; use `sandbase_run_get` for async results.

## 1. Current landscape scan

**User request**

```text
Find the last 30 days of reliable sources about AI agent observability. Give me a five-source brief with gaps.
```

**Use these capabilities**

1. Resolve `exa_search` and request a supported deep search mode, a publication window starting 30 days ago, highlights, summaries, and 10 results using the inspected schema.
2. Select the top 5 most relevant, authoritative results.
3. Optionally use the discovered `exa_contents` capability to request full text for the 2–3 sources that need deeper analysis, if supported.

**Return**: a source map table, 3–5 key findings with citations, disagreements between sources, and suggested follow-up queries.

## 2. Trusted-source deep research

**User request**

```text
Research how enterprise teams evaluate AI agents. Prefer company and academic sources; exclude vendor blogs.
```

**Use these capabilities**

1. Resolve `exa_search` and request deep search with summaries, restricted to trusted domains such as arxiv.org, hbr.org, and mckinsey.com, excluding known vendor blogs. Map these options to the inspected schema.
2. Run 2–3 refined queries focusing on: evaluation criteria, enterprise deployment challenges, ROI measurement.
3. Use the discovered `exa_contents` capability to request highlights about evaluation criteria for the most promising results, if supported by the inspected schema.

**Return**: findings organized by evaluation dimension, with source quality assessment and gaps where academic/enterprise evidence is thin.

## 3. Competitive argument comparison

**User request**

```text
Compare the public arguments for and against retrieval-augmented generation. Cite each source.
```

**Use these capabilities**

1. `exa_search` with query describing "arguments in favor of RAG for production LLM applications", using a deep search mode supported by the inspected schema.
2. `exa_search` with query describing "limitations and criticisms of RAG architecture", using a deep search mode supported by the inspected schema.
3. Use the discovered `exa_contents` capability to request highlights focused on advantages and limitations for selected URLs, using supported schema options.

**Return**: a two-column comparison (for/against), each point citing its source, with a synthesis of where the debate stands and what evidence is missing.

## 4. Recent news monitoring

**User request**

```text
Find recent funding announcements in the AI developer tools space from the last 7 days.
```

**Use these capabilities**

1. Resolve `exa_search` and request news from the last 7 days, 15 results, and highlights using the inspected schema.
2. Query variations: "AI developer tools startup funding round", "Series A B C AI coding tools".

**Return**: a chronological list with company, amount, round, investors (when available), and source URL. Note which details are confirmed vs. reported by a single source.

## 5. Specific-page extraction

**User request**

```text
Extract the pricing and feature comparison from these three competitor pages: [URL1, URL2, URL3].
```

**Use these capabilities**

1. Resolve `exa_contents` and request full text for the three URLs, with a content limit if the inspected schema supports one.
2. If `exa_contents` is unavailable, use the discovered `exa_search` capability restricted to those domains, with highlights if supported by its inspected schema.

**Return**: a structured comparison table extracted from the pages, noting where information was unavailable or behind authentication.
