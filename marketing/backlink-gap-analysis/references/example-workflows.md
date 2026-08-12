# Example Workflows

Each example uses SandBase DataForSEO backlink capabilities as the evidence source. Inspect the current schema with `sandbase_describe_tool` before calling any listed tool.

## 1. Full backlink gap analysis

**User request**

```text
Compare our-domain.com with competitor-a.com and competitor-b.com. Find ethical backlink gaps we can pursue.
```

**Use these capabilities**

1. `dataforseo_v3_backlinks_summary_live` for all three domains — establish baseline profiles.
2. `dataforseo_v3_backlinks_competitors_live` for our-domain.com — identify additional link competitors.
3. `dataforseo_v3_backlinks_referring_domains_live` for each competitor — find domains linking to them.
4. `dataforseo_v3_backlinks_backlinks_live` for competitor pages with the most links — understand what earned them.
5. `dataforseo_v3_backlinks_anchors_live` for our-domain.com — check anchor health.

**Return**: a profile comparison table, 10–15 prioritized prospects (sites that link to competitors but not the target), suggested asset types, and exclusions with reasons.

## 2. Linkable asset discovery

**User request**

```text
What types of content earn links in the developer tools space? Show me what's working for competitors.
```

**Use these capabilities**

1. `dataforseo_v3_backlinks_domain_pages_live` for 2–3 competitors — find their most-linked pages.
2. `dataforseo_v3_backlinks_backlinks_live` for those top pages — understand what types of sites link to them and why.
3. `dataforseo_v3_backlinks_anchors_live` for those pages — see how linkers describe the content.

**Return**: a page-type analysis (e.g., "open-source tools earn 3x more links than blog posts"), specific asset patterns to replicate, and a recommended creation priority.

## 3. Anchor text health check

**User request**

```text
Audit the anchor text profile for our-domain.com and flag any risks.
```

**Use these capabilities**

1. `dataforseo_v3_backlinks_summary_live` for baseline metrics.
2. `dataforseo_v3_backlinks_anchors_live` for the full anchor distribution.
3. `dataforseo_v3_backlinks_referring_domains_live` filtered to see which domains contribute problematic anchors.

**Return**: anchor distribution breakdown (brand, URL, exact-match, partial-match, generic, other), risk assessment, comparison to competitor anchor patterns, and recommendations.

## 4. Digital PR prospect list

**User request**

```text
Build a list of publications and blogs that cover our industry and link to competitors. I need an outreach target list.
```

**Use these capabilities**

1. `dataforseo_v3_backlinks_competitors_live` to identify the link competitor set.
2. `dataforseo_v3_backlinks_backlinks_live` for each competitor — filter for editorial and news links.
3. `dataforseo_v3_backlinks_referring_domains_live` — identify domains that link to 2+ competitors.

**Return**: a ranked prospect list with domain, topic focus, linking pattern (how they link: roundups, news mentions, resource pages), contact suggestion (editorial guidelines if visible), and a priority score.

## 5. New site authority baseline

**User request**

```text
We just launched. Our competitor has a strong backlink profile. What's our realistic path to closing the gap?
```

**Use these capabilities**

1. `dataforseo_v3_backlinks_summary_live` for the competitor.
2. `dataforseo_v3_backlinks_referring_domains_live` for the competitor — categorize by type (editorial, directory, tool, community).
3. `dataforseo_v3_backlinks_domain_pages_live` for the competitor — identify their link magnets.

**Return**: a realistic timeline assessment, the 3 most replicable link acquisition channels, quick wins (directories, profiles, communities), and a content strategy to earn editorial links over 6–12 months.
