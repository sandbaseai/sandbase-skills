---
name: market-sizing-analysis
description: "Estimate TAM, SAM, and SOM with top-down, bottom-up, and value-based methods. Use for market opportunity analysis, business cases, startup planning, or investor-ready market sizing."
license: MIT
metadata:
  source: "https://github.com/wshobson/agents/tree/a30778f8c4e6b0a87567941b7cca4f534bf642b6/plugins/startup-business-analyst/skills/market-sizing-analysis"
  modified: "Condensed, made evidence-first, and removed universal venture-size assumptions."
---

# Market Sizing Analysis

Produce a transparent range for Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM). Show the calculation, evidence, assumptions, date, geography, and uncertainty; a precise number without those elements is not a defensible estimate.

## Frame the market

Define before calculating:

- customer or user and the problem being solved;
- product category and revenue model;
- geography, industry, company-size, and eligibility constraints;
- annual versus cumulative value and base currency;
- current year and forecast horizon;
- whether TAM describes revenue, transaction value, spend, users, or another unit.

Avoid category definitions so broad that unrelated spend enters the estimate. Keep different currencies, years, geographies, and market definitions separate until explicitly normalized.

## Choose methods

Use at least two methods when reliable inputs exist.

### Bottom-up

Prefer for a specific reachable customer set:

```text
TAM = sum(segment customer count × annual revenue per customer)
SAM = sum(serviceable segment count × serviceable annual revenue per customer)
SOM = reachable customers × expected annual revenue per customer
```

Derive reachable customers from sales capacity, acquisition economics, channel access, adoption, retention, and time—not from an unexplained percentage of SAM.

### Top-down

Use a reputable category total and apply non-overlapping filters:

```text
SAM = category total × geographic share × eligible-segment share × product-fit share
```

Document the source definition for every factor. Do not multiply correlated filters as if they were independent without explaining the limitation.

### Value-based

Use when the category is new or existing spend understates value:

```text
annual value/customer = avoidable cost or gain × realistically captured share
annual revenue/customer = annual value/customer × willingness-to-pay share
TAM = eligible customers × annual revenue/customer
```

Treat willingness to pay as a hypothesis unless supported by pricing research or observed transactions.

## Evidence workflow

1. Reuse user-supplied customer, CRM, pricing, and conversion data first.
2. Use authorized host search or research tools for external counts and category benchmarks when available.
3. Prefer primary sources: official statistics, filings, company disclosures, and original research methodology.
4. Record publisher, title, publication date, data year, URL, geography, unit, and any transformation.
5. Normalize currency and inflation only when needed, showing the rate and date.
6. Triangulate methods and investigate material differences instead of averaging them automatically.

## Scenarios and sensitivity

Use conservative, base, and upside scenarios for uncertain inputs. Identify which assumptions drive the result most. For each scenario show customer count, price or value, serviceability, capture logic, TAM, SAM, SOM, and horizon.

Do not use universal rules such as “SOM is always 2–5%” or “a venture market must exceed a fixed size.” Benchmarks can be context, not substitutes for company-specific reachability.

## Output

```markdown
## Market definition
## Executive range
| Metric | Conservative | Base | Upside | Unit/year |
## Bottom-up calculation
## Top-down or value-based cross-check
## SAM filters and SOM reachability model
## Sensitivity and scenario drivers
## Evidence ledger
| Input | Value | Year/market | Source | Confidence | Transformation |
## Assumptions, gaps, and next validations
```

## Quality gate

- TAM, SAM, and SOM use the same market definition and annualization basis.
- Every external numeric input has a traceable source and date.
- Calculations reconcile and units are visible.
- SOM is connected to operational capacity and a stated time horizon.
- Ranges reflect uncertainty; unsupported precision is removed.
- Conflicting estimates and weak evidence are disclosed.

## Failure handling

- If source data is unavailable, provide the formula and missing-input checklist rather than inventing values.
- If methods differ materially, explain definition and assumption differences and present both ranges.
- If only paid or inaccessible evidence is cited, mark it unverified and seek an accessible corroborating source.
