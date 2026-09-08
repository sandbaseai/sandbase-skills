---
name: similarweb-analytics
description: "Analyze estimated website traffic, engagement, rankings, channel mix, and geographic distribution through SandBase. Use for domain benchmarking, acquisition-channel analysis, or traffic trend research; do not present third-party estimates as first-party analytics."
---

# Similarweb Analytics

Turn third-party website traffic estimates into a comparable, decision-focused analysis. Keep the requested domain, time window, device scope, geography, and metric definitions consistent, and distinguish observed estimates from conclusions.

Read [the SandBase API map](references/sandbase-api-map.md) before retrieving data. It defines the supported MCP and REST transports and the runtime discovery contract.

## Define the comparison

Resolve or state:

- canonical root domains and any explicitly included subdomains;
- analysis window using complete calendar periods when possible;
- device scope, geography, and traffic granularity;
- target metrics and comparison domains;
- whether the user needs a snapshot, trend, channel diagnosis, geographic mix, or reusable report.

Normalize input domains by removing protocols, paths, query strings, and fragments. Keep materially different properties, regional domains, and app traffic separate unless the user explicitly wants them combined.

## Retrieve evidence through SandBase

Choose one available transport from the API map. Use SandBase for live external traffic data; do not call the original Manus runtime or request a direct Similarweb credential.

1. Discover only the capabilities needed for the question: visits, unique visitors, engagement, global rank, traffic sources, or country distribution.
2. Inspect each selected capability immediately before execution. Follow its live schema, date limits, device and geography definitions, price, and execution mode.
3. Use the fewest calls that produce a fair comparison. Before a multi-call paid batch, show the endpoint names, domains, periods, call count, and known or estimated cost for confirmation.
4. Execute the approved batch and keep an evidence ledger containing endpoint, arguments, response timestamp, run ID, metric definition, and unit.
5. Poll an asynchronous result by its returned ID. Never submit a duplicate because a run is still pending.

If neither SandBase transport is available, ask for an authorized export from Similarweb, Ahrefs, Semrush, DataForSEO, or first-party analytics. Continue with that supplied data only when its definitions are clear; otherwise return a data-requirements template instead of inventing traffic values.

## Select the minimum dataset

| Question | Evidence to retrieve |
|---|---|
| How large is the site? | Estimated visits and/or unique visitors for a complete period, with device and geography scope |
| Is traffic growing? | A consistent monthly series across the requested window |
| Is engagement changing? | Bounce rate, pages per visit, visit duration, and their definitions for the same period |
| Which channels drive visits? | Channel shares or volumes for the same device scope and window |
| Where is the audience? | Country share or traffic by country with coverage limits |
| Which site is stronger? | The same metrics, dates, scopes, and units for every domain |
| How visible is the site? | Global or category rank with the observation month and ranking definition |

Do not retrieve every available metric by default. A focused snapshot usually needs traffic magnitude, trend, and one diagnostic dimension; add other calls only when they can change the decision.

## Normalize and validate

- Compare only overlapping periods and the same granularity. Label partial or missing months.
- Preserve metric units and distinguish counts, shares, rates, ranks, and durations.
- Do not add desktop and mobile values unless the inspected schemas establish that they are disjoint and additive.
- Treat channel shares as compositional data: verify that covered categories are comparable and explain omitted or residual traffic.
- Use weighted calculations when combining periods; do not average monthly rates blindly when denominators differ.
- For rankings, remember that a lower number is a stronger rank. Do not calculate percentage growth on ranks as if they were traffic volumes.
- Record source coverage and estimation limits. Third-party traffic estimates may differ materially from first-party analytics, especially for small sites.

Flag a result when a sudden jump coincides with a methodology, domain, device, geography, or coverage change. Do not attribute causality from traffic correlation alone.

## Analyze the result

Lead with the answer most relevant to the user's decision:

1. **Scope and freshness** — domains, period, device, geography, and latest complete month.
2. **Traffic scale and direction** — level, absolute change, percentage change, and consistency.
3. **Engagement quality** — whether engagement metrics corroborate or complicate the traffic trend.
4. **Acquisition mix** — concentration, channel gains or losses, and plausible implications.
5. **Geographic mix** — major markets, changes, and localization implications.
6. **Uncertainty** — estimation risk, missing data, schema differences, and alternative explanations.

For competitor comparisons, include both absolute and indexed views when useful. State which domain was used as the baseline and avoid declaring a winner from one metric.

## Final handoff

Return:

- a concise conclusion with the exact period and scope;
- a comparison or trend table with units;
- the few most decision-relevant findings and caveats;
- SandBase logical capability names and run IDs;
- derived calculations with formulas or clear methods;
- missing data and the next measurement that would most reduce uncertainty.

Do not claim a live analysis completed while a required run is pending, failed, or returned no usable data.
