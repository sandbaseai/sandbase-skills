---
name: cash-flow-snapshot
description: "Forecast 30/60/90-day cash flow from CSV, spreadsheet, or authorized accounting data, with timing uncertainty, cumulative balances, named liquidity risks, and an auditable output table."
license: Apache-2.0
metadata:
  source: "https://github.com/anthropics/knowledge-work-plugins/tree/77961df00a4626bc3b83850064289decd5a3b977/small-business/skills/cash-flow-snapshot"
  modified: "Made CSV-first and host-neutral; corrected confidence-band and cash-balance calculations."
---

# Cash Flow Snapshot

Build an auditable 30/60/90-day forecast from attached tabular data or an authorized accounting connector available to the host. CSV or spreadsheet input is the portable default; no named connector is required. This analysis is not financial advice and should be reviewed before financing or payment decisions.

## Required data

At minimum map:

- transaction or due date;
- amount;
- direction (`inflow` or `outflow`);
- description.

Useful optional fields include transaction ID, counterparty, invoice date, expected receipt date, paid/cleared status, recurring flag, category, currency, and historical invoice/receipt pairs. Obtain opening cash balance and as-of date before making claims about ending liquidity or ability to meet a payment.

Show the proposed column mapping when headers are ambiguous. Never combine currencies without an explicit FX source, date, and conversion rule.

## Prepare the forecast

1. Exclude settled items from future flows while retaining them for historical timing analysis.
2. Detect duplicate rows, reversed transactions, invalid dates, and sign inconsistencies.
3. Estimate each inflow date from its due date plus counterparty-specific historical payment lag when at least three usable observations exist.
4. With thinner history, use a clearly labeled user-supplied or provisional timing assumption; do not present it as learned behavior.
5. Detect likely recurring fixed costs only when at least three consistent periods support the pattern, and show the inferred list for review.
6. Assign expected flows to `0–30`, `31–60`, and `61–90` day windows from the as-of date.

## Uncertainty calculation

For a window with uncertain inflows:

```text
band_percent = weighted timing standard deviation / weighted average payment lag
low_inflows  = expected inflows × (1 - band_percent)
high_inflows = expected inflows × (1 + band_percent)
low_net      = low_inflows - expected outflows
high_net     = high_inflows - expected outflows
```

Cap a displayed percentage band at 50% and flag wider or unstable estimates as insufficient data. If mean lag is one day or less, do not divide by zero; use observed settlement variance or a labeled low-variance assumption. Apply uncertainty to the affected flows rather than multiplying the final net value.

Calculate cumulative liquidity separately:

```text
expected ending cash = opening cash + cumulative expected net flow
low ending cash      = opening cash + cumulative low net flow
high ending cash     = opening cash + cumulative high net flow
```

Without opening cash, report net cash flow only and state that ending cash and payroll coverage cannot be determined.

## Risks

Rank no more than five named risks by estimated impact:

- a historically late payer moving a receipt beyond a required payment;
- low-case ending cash falling below zero or a user-supplied reserve threshold;
- payroll, tax, debt, or major vendor obligations not covered by cash on hand;
- concentration in one customer or uncertain inflow;
- thin, stale, incomplete, or single-currency-assumption data.

Do not recommend delaying a payment, borrowing, or changing financing without clearly separating the observation from professional advice.

## Output

Always provide a concise summary and an auditable table. If the host has spreadsheet creation capability and the user wants a workbook, create:

1. `Summary`: window inflows, outflows, net flow, cumulative ending cash, and low/high cases.
2. `Detail`: normalized transactions, expected dates, source IDs, window, and running balance.
3. `Risks`: risk, impact, affected date/window, evidence, and validation action.

Otherwise return the same tables as Markdown or CSV. Use `cash-flow-snapshot-YYYY-MM-DD` as the artifact basename.

## Quality gate

- The as-of date, opening balance status, currency, and data sources are explicit.
- Detail rows sum to every summary window.
- Expected, low, and high calculations are reproducible and ordered correctly.
- Past/settled transactions are not counted as future cash.
- Risk dates reconcile to the running cash balance.
- Assumptions and inferred recurring items are visible.

## Failure handling

- If columns are ambiguous, pause calculation and confirm the mapping.
- If data is insufficient, produce a deterministic expected-case schedule plus a missing-data list instead of false confidence bands.
- If a connector fails, retain any verified rows already obtained and request a CSV/spreadsheet export; do not require a particular provider.
