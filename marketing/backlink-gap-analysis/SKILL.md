---
name: backlink-gap-analysis
description: Find and prioritize ethical backlink and digital-PR opportunities using SandBase DataForSEO backlink data. Use when asked to analyze backlink profiles, find referring-domain gaps, compare link competitors, or prepare a link-outreach target list.
---

# Backlink Gap Analysis

Use backlink evidence to find relevant, reachable link-building opportunities. This Skill calls the named DataForSEO backlink capabilities in [the SandBase API map](references/sandbase-api-map.md) through the SandBase MCP gateway. In a SandBase Agent, run the capabilities directly. In another compatible agent, require an authorized SandBase connection before starting; never request, print, or store an API key in the research output.

Do not send outreach or create links — this Skill is read-only research. Read [example workflows](references/example-workflows.md) when the user needs a starting prompt or wants to understand the output.

## Operating principles

- Recommend only ethical, relevant link opportunities. Exclude PBNs, link farms, paid-link schemes, and manipulative tactics.
- Treat DataForSEO backlink data as directional evidence, not absolute truth. Backlink databases are sampled and may be days to weeks behind reality.
- Separate observations (what the data shows) from judgment (which opportunities are worth pursuing).
- Prioritize topical relevance and audience fit over raw domain authority or volume.
- Keep user domains, competitor details, and strategy confidential unless sharing is explicitly requested.

## Workflow

### 1. Frame the analysis

Collect or infer: the target domain, market/industry, 2–5 competitor domains, link-building constraints (no paid links, no guest post farms, etc.), and the goal (authority building, specific page promotion, digital PR angles, or general gap analysis).

Classify the request as one or more of:
- **Profile audit**: understand the target's current backlink health
- **Gap analysis**: find where competitors have links the target doesn't
- **Asset discovery**: identify which target pages attract links (or could)
- **Prospect prioritization**: build a ranked outreach target list
- **Anchor assessment**: evaluate anchor-text health and risk

### 2. Select and call SandBase capabilities

Read [the SandBase API map](references/sandbase-api-map.md) before selecting tools. Use the listed `tool_name` through the SandBase gateway:

1. Call `sandbase_describe_tool` for the selected `tool_name` and read its current input schema.
2. Call `sandbase_call_tool` with that exact `tool_name` and only schema-defined arguments.
3. Keep the tool name, target domain, and query parameters with the returned data.

### 3. Profile the target domain

Use `dataforseo_v3_backlinks_summary_live` and `dataforseo_v3_backlinks_referring_domains_live`:

| What to extract | Why it matters |
|---|---|
| Total backlinks and referring domains | Baseline authority signal |
| Domain rank / authority score | Contextualizes difficulty of gap-closing |
| New vs. lost links trend | Health trajectory |
| Top referring domain types | Reveals current acquisition pattern |
| Dofollow vs. nofollow ratio | Link equity distribution |

Tips:
- Compare the target's profile size against competitors before diving into gaps — a 10x size difference changes strategy.
- Note if the target has strong links in one topic area but not another (topical authority gaps).
- Flag unnatural patterns early (sudden spikes, high % from one country, anchor over-optimization).

### 4. Identify competitor link sources

Use `dataforseo_v3_backlinks_competitors_live` and `dataforseo_v3_backlinks_backlinks_live`:

| Strategy | Tool and approach |
|---|---|
| Find link competitors | `backlinks_competitors_live` — identifies domains competing for similar link sources |
| Inspect competitor-earned links | `backlinks_backlinks_live` for each competitor — reveals specific pages linking to them |
| Compare acquisition patterns | Look at link type (editorial, directory, resource page, PR mention) |

Tips:
- Focus on links from the last 12 months for actionable opportunities (older links may be from defunct sites).
- Look for referring domains that link to 2+ competitors but not the target — highest-probability gaps.
- Distinguish editorial links (earned through content quality) from structural links (directories, profiles) — they require different acquisition strategies.
- Note the content type that earned the link (data, tool, guide, news mention) — this reveals what assets to create.

### 5. Assess relevance and linkable assets

Use `dataforseo_v3_backlinks_anchors_live` and `dataforseo_v3_backlinks_domain_pages_live`:

**Anchor text analysis:**
- Healthy profile: diverse anchors, brand-heavy, natural language
- Risk signals: over-optimized exact-match anchors, foreign-language spam anchors
- Opportunity signals: competitors with branded anchors from editorial coverage

**Domain pages analysis:**
- Which target pages already attract links? (potential to amplify)
- Which competitor pages attract the most links? (asset patterns to replicate)
- What page types earn links? (tools, data, guides, research, free resources)

### 6. Rank and filter prospects

Score each prospect on a transparent framework:

| Dimension | Question | Signal |
|---|---|---|
| Topical relevance | Does this domain cover the target's industry? | Content overlap with target |
| Audience fit | Would the linking site's readers be potential customers? | Traffic quality, not just DA |
| Linking pattern | Does this domain actually link out? | History of editorial or resource links |
| Accessibility | Can this link be earned ethically? | Editorial guidelines, contact info |
| Asset fit | Does the target have (or could create) content this site would link to? | Content gap analysis |
| Risk | Is there any manipulation, spam, or penalty risk? | Spam score, link neighborhood |

Exclude prospects that:
- Have no topical relevance to the target
- Show signs of being link farms or PBNs
- Only link to sites through paid arrangements
- Are in completely different languages or markets (unless intentional)

## Output

Return a structured analysis:

### Profile summary

| Metric | Target | Competitor 1 | Competitor 2 |
|---|---|---|---|
| Referring domains | ... | ... | ... |
| Domain authority | ... | ... | ... |
| New links (30d) | ... | ... | ... |
| Top link type | ... | ... | ... |

### Priority prospects

| # | Referring domain | Topical fit | Links to competitors | Suggested angle | Difficulty | Priority |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |

### Recommended assets to create

Content or tools the target should build to attract links from the identified prospect pool.

### Anchor health assessment

Current state and any recommendations for anchor diversification.

### Exclusions

Prospects reviewed but excluded, with reasons (keeps the analysis auditable).

### Evidence gaps and next steps

What data is missing, and the smallest action to improve the analysis.

## Tips for better results

- **Start with competitors, not the target**: The most actionable insights come from what competitors have earned that the target hasn't.
- **Quality over quantity**: 10 highly relevant prospects are worth more than 100 generic directories.
- **Look for "link-earning events"**: Product launches, data publications, tool releases, and newsworthy announcements that earned competitors links.
- **Check the linker's linking behavior**: A site that regularly links out in editorial content is far more accessible than one that rarely includes external links.
- **Consider the full funnel**: Not all valuable links come from high-DA sites. Niche industry blogs with engaged audiences can drive qualified traffic and relevance signals.

## Failure handling

- If SandBase is unavailable or unauthorized, report the failed capability and ask the user to connect or authorize SandBase; do not silently substitute a direct provider API.
- If a domain returns no data, it may be too new, too small, or using a subdomain format the API doesn't recognize. Try with/without www, or note the data gap.
- If competitor data is sparse, the competitor may be too small for the backlink database. Suggest alternative competitors or note the limitation.
- If all prospects are low-relevance, recommend authority-building strategies (content creation, digital PR) before link outreach.

## Quality gate

Before delivering, verify that:

- Every recommended prospect has a clear topical relevance justification.
- Excluded prospects are documented with reasons.
- The analysis distinguishes editorial links from structural/directory links.
- Risk factors (spam, manipulation) are flagged for any borderline prospects.
- Recommendations are actionable: each has a suggested angle or asset type.
- The output honestly states what the data can and cannot prove.
