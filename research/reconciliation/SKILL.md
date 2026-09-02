---
name: reconciliation
description: "Reconcile bank, general-ledger, subledger, intercompany, or third-party transaction data; classify differences, age open items, and produce a review-ready reconciliation report."
license: Apache-2.0
metadata:
  source: "https://github.com/anthropics/knowledge-work-plugins/tree/77961df00a4626bc3b83850064289decd5a3b977/finance/skills/reconciliation"
  modified: "Adapted into a host-neutral, auditable data-matching workflow with non-destructive safeguards."
---

# Reconciliation

Compare two balances or transaction populations and explain every difference. Work from copies or derived artifacts; never edit source accounting records or post adjustments. A qualified reviewer must approve financial conclusions and entries.

## Intake

Identify:

- reconciliation type: bank-to-GL, GL-to-subledger, intercompany, or third-party;
- account/entity, period end, currency, timezone, and source systems;
- control totals for each population;
- stable transaction identifiers and available amount/date/description fields;
- organization-approved amount, date, FX, and rounding tolerances;
- materiality, aging, owner, and escalation rules.

If column mappings are ambiguous, show candidate mappings and obtain confirmation before matching.

## Prepare the data

1. Preserve raw values and row identifiers.
2. Normalize dates, currencies, signs, whitespace, and identifier casing in derived fields.
3. Detect duplicates, reversals, voids, missing values, and out-of-period records.
4. Tie each source population to its stated control total before matching.
5. Keep excluded rows in an exception table with the reason for exclusion.

## Match in controlled passes

Use the strongest evidence first and ensure a row is consumed at most once:

1. Exact stable identifier plus amount.
2. Exact amount and date within the approved tolerance, supported by counterparty or description.
3. Documented one-to-many or many-to-one groupings whose amounts reconcile.
4. Probable matches for human review; do not present fuzzy similarity alone as confirmed.

For every match retain source row IDs, rule, variance, and confidence. Never silently widen tolerances to force a zero difference.

## Classify open items

- Timing difference: valid item expected to clear without an adjustment.
- Adjustment required: supported error, fee, interest, duplicate, omission, or misclassification.
- Investigation required: insufficient evidence, dispute, stale item, or recurring unexplained difference.

Age open items from their origin date into organization-defined buckets. If no policy exists, use provisional `0–30`, `31–60`, `61–90`, and `90+` day buckets and label them as defaults.

## Output

```markdown
## Reconciliation summary
| Source A total | Source B total | Matched | Open A | Open B | Final difference |

## Matched items
| Match ID | Source A rows | Source B rows | Rule | Amount | Variance | Confidence |

## Open and reconciling items
| Item ID | Source | Description | Amount | Origin date | Age | Category | Owner | Action |

## Control-total bridge
Starting balance + documented reconciling items = adjusted balance

## Exceptions and data-quality issues
## Proposed adjustments for review
## Sign-off fields
Prepared by / date; reviewed by / date
```

Suggested adjustments must include rationale and supporting rows, and must be clearly labeled `Proposed—not posted`.

## Quality gate

- Both populations tie to their control totals or show a quantified source gap.
- Each source row is matched, open, or excluded exactly once.
- Matches remain reproducible from logged rules and source IDs.
- Adjusted balances reconcile within the approved tolerance.
- Aging uses the correct origin date and period end.
- No source records or accounting systems were changed.

## Failure handling

- If totals do not tie, report the source gap before transaction matching.
- If multiple candidate matches exist, keep them unresolved for review.
- If currency or sign treatment is unknown, stop amount matching and request confirmation.
- If the user requests posting an entry, treat that as a separate authorized workflow and preserve review controls.
