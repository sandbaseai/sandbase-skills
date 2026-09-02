---
name: variance-analysis
description: "Decompose budget, forecast, period-over-period, revenue, expense, and operating variances into quantified drivers with reconciled bridge tables and decision-ready commentary."
license: Apache-2.0
metadata:
  source: "https://github.com/anthropics/knowledge-work-plugins/tree/77961df00a4626bc3b83850064289decd5a3b977/finance/skills/variance-analysis"
  modified: "Condensed and adapted for host-neutral spreadsheet analysis with explicit sign and reconciliation rules."
---

# Variance Analysis

Explain what changed, why it changed, and whether it is likely to persist. All analyses must be reviewable from the supplied data. This Skill supports finance workflows but does not replace accounting or financial review.

## Intake and normalization

Establish:

- metric, period, comparison basis, currency, and reporting unit;
- whether positive means favorable or merely numerically higher;
- actual, budget, forecast, and prior-period fields available;
- business dimensions such as product, region, customer, department, or account;
- organization-specific materiality thresholds.

Validate totals, duplicates, missing values, signs, period coverage, and unit consistency before decomposing. Preserve source data; perform transformations in a separate table or artifact.

## Calculations

Always compute:

```text
variance_amount = actual - comparison
variance_percent = variance_amount / abs(comparison)
```

When the comparison value is zero, report the percentage as `N/M` rather than dividing by zero. Label favorable/unfavorable separately because the interpretation differs for revenue, cost, and non-financial metrics.

### Price and volume

For `Revenue = Price × Volume`, use one documented convention:

```text
volume_effect = (actual_volume - comparison_volume) × comparison_price
price_effect  = (actual_price - comparison_price) × actual_volume
```

Then verify:

```text
volume_effect + price_effect = actual_revenue - comparison_revenue
```

If product or customer mix matters, calculate effects at the lowest reliable segment level and aggregate. State the ordering convention because price, volume, and mix allocations can differ while producing the same total.

### Other drivers

- Payroll: headcount, compensation rate, level/department mix, hiring timing, attrition, and one-time costs.
- Operating expense: volume-driven, discretionary, contractual/fixed, timing, and non-recurring spend.
- Gross margin: price, unit cost, volume, product/customer mix, freight, and foreign exchange.
- Recurring revenue: new business, expansion, contraction, churn, price, and FX.

Never label an unexplained residual as a causal driver. Call it `unexplained` and make it an investigation item.

## Materiality and prioritization

Use thresholds supplied by the organization. Otherwise present an explicit provisional threshold and invite confirmation. Prioritize by absolute impact, percentage impact, unexpected direction, recurrence, and decision relevance—not by percentage alone.

## Output

```markdown
## Variance summary
| Metric | Comparison | Actual | Variance | Variance % | F/U | Material? |

## Driver bridge
| Driver | Amount | Evidence | Recurring? | Owner/action |

## Reconciliation
Starting value + sum(driver amounts) = ending value
Unexplained residual = ...

## Management commentary
[Metric] was [favorable/unfavorable] by [amount/percent], primarily due to
[quantified drivers]. [One-time/continuing outlook]. [Action or monitoring step].

## Assumptions and data gaps
```

When a charting capability is available, generate a waterfall only after the bridge reconciles. Keep the calculation table alongside the visual.

## Quality gate

- Source totals tie to reported comparison and actual values.
- Driver effects sum to the total variance within a disclosed rounding tolerance.
- Sign convention and favorable/unfavorable logic are explicit.
- Commentary names quantified business causes, not circular observations.
- One-time, timing, and recurring effects are distinguished.
- Unknown causes remain visible as residuals.

## Failure handling

- If data is too aggregated for causal decomposition, provide the total variance and request the minimum additional dimensions.
- If source totals do not tie, stop driver attribution and report the reconciliation gap.
- If periods or currencies differ, do not compare until the user confirms a normalization method.
