---
name: stock-analysis
description: "Research public companies and listed securities with current market, company, ownership, and filing data through SandBase. Use for ticker analysis, price-performance comparisons, insider activity, or an evidence-backed investment research brief; do not use for trade execution or personalized financial advice."
---

# Stock Analysis

Build a current, traceable research view of a public company or listed security. Separate sourced facts from calculations and interpretation, state the data timestamp, and avoid presenting a directional opinion as personalized financial advice.

Read [the SandBase API map](references/sandbase-api-map.md) before retrieving live data. It defines the supported MCP and REST transports and the rules for dynamic capability discovery.

## Scope the request

Resolve the following from the request or state reasonable defaults:

- security name, ticker, exchange, and market region;
- question to answer: company overview, price behavior, valuation context, ownership, filings, comparison, or full brief;
- analysis window and comparison benchmark;
- currency and whether prices should be adjusted for splits and distributions;
- output depth and whether the user wants raw data, a concise answer, or a reusable report.

Disambiguate tickers before making paid calls when the symbol could refer to multiple exchanges or instruments. Do not silently treat an ADR, index, fund, option, or cryptocurrency as common stock.

## Retrieve evidence through SandBase

Choose one available transport from the API map. Use SandBase for live external data; do not call the original Manus runtime or substitute a provider-specific credential.

1. Discover capabilities for the specific evidence needed, such as company profile, price history, analyst or valuation context, holders or insider transactions, and regulatory filings.
2. Inspect every selected capability immediately before execution. The live schema and pricing are authoritative; model names and parameters must not be guessed from examples or prior runs.
3. Use the smallest capability set that answers the question. Before a multi-call paid batch, summarize the selected endpoints, call count, and known or estimated cost for confirmation.
4. Execute only the approved calls. Preserve each response, source timestamp, endpoint name, and run ID in an evidence ledger.
5. Poll an asynchronous run by its returned ID until it reaches a terminal state. Never create a duplicate call merely because a run is still pending.

If neither SandBase transport is available, do not fabricate current prices or company facts. Ask for a user-provided export, or provide an analysis template that clearly marks live-data fields as unavailable.

## Select the minimum dataset

| Request | Evidence to retrieve |
|---|---|
| Company overview | Identity, exchange, industry, business description, reporting currency, and latest profile timestamp |
| Price or trend | Timestamped OHLC/adjusted-close series, volume when relevant, corporate actions, and chosen benchmark |
| Technical context | Price series sufficient for the requested indicators; compute indicators transparently when raw data is available |
| Valuation or analyst view | Current metric definitions, reporting period, peer or sector context, rating date, and source provenance |
| Ownership or insider activity | Holder or transaction records, role, transaction type, date, quantity/value, and reporting basis |
| Filings | Form type, filing date, reporting period, issuer identity, and source document URL |
| Comparison | The same fields, currency treatment, interval, and date window for every security |

Do not require an unrelated profile or analyst call when one focused dataset is enough. For broad due diligence, gather at least company identity, price history, the latest relevant filing, and the risk factors needed to support the requested conclusion.

## Normalize and calculate

- Preserve raw values and units. Record currency, timezone, exchange session, and whether prices are adjusted.
- Align comparison series to common trading dates and a common starting value before calculating relative performance.
- Calculate returns from the selected price convention and show the formula or method. Do not mix adjusted and unadjusted series.
- Treat missing values, stale quotes, suspended trading, corporate actions, and differing fiscal calendars explicitly.
- Label provider-produced scores, targets, and ratings as third-party estimates with their observation date.
- Prefer primary filing documents for accounting claims. Use profile or market-data summaries as navigation aids, not as substitutes for the filing when wording matters.

For computed indicators, state the lookback, sampling interval, and whether the current incomplete bar was excluded. Never infer support, resistance, fair value, or insider sentiment from a single opaque score without explaining the evidence.

## Analyze without overclaiming

Organize the answer around the user's decision rather than dumping every field:

1. **Identity and as-of time** — instrument, exchange, currency, market status, and latest observation.
2. **What changed** — price, volume, operating, filing, or ownership signals over the requested window.
3. **Why it may matter** — evidence-backed interpretation with plausible alternative explanations.
4. **Risks and gaps** — stale or missing data, conflicting sources, concentration, liquidity, event, accounting, or comparability risks.
5. **Next checks** — the few facts that would most change the conclusion.

When asked whether a security is a "buy," translate the request into a non-personalized scenario analysis. Present bull, base, and bear considerations or explicit decision criteria; do not claim certainty, guarantee returns, or execute a trade.

## Final handoff

Return:

- a direct answer with the as-of date and market timezone;
- a compact table of the most decision-relevant facts and calculations;
- source or filing links when returned by SandBase;
- the SandBase endpoint names and run IDs used;
- assumptions, missing data, and material limitations;
- a clear distinction between sourced facts, derived calculations, and interpretation.

Do not claim a live-data analysis succeeded if any required run is pending, failed, or returned an empty result.
