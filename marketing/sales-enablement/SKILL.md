---
name: sales-enablement
description: "Create buyer-specific sales decks, one-pagers, objection guides, demo scripts, ROI models, proposals, playbooks, and persona cards from verified product and customer evidence."
license: MIT
metadata:
  source: "https://github.com/coreyhaines31/marketingskills/tree/d4ff28a9c8d56c06809860bf2800d4f5224b52db/skills/sales-enablement"
  modified: "Condensed, removed unavailable cross-skill links, and made artifact creation host-neutral."
---

# Sales Enablement

Create the specific asset a sales team needs for a buyer, deal stage, and next decision. Do not generate every possible asset by default.

## Intake

Read supplied product positioning, customer research, call notes, pricing, security material, competitive evidence, brand guidance, and existing collateral. Establish:

- product, target account or segment, buyer role, pain, desired outcome, and differentiators;
- sales motion, deal stage, asset user, delivery context, and desired format;
- approved proof points, customer examples, pricing, claims, and confidentiality limits;
- the next decision or action the asset should enable.

Ask only for gaps that materially affect accuracy or usefulness. Never invent customer logos, quotes, metrics, certifications, integrations, pricing, or competitive claims. Use clearly labeled placeholders when approved evidence is missing.

## Choose one deliverable

| Need | Deliverable | Required outcome |
|---|---|---|
| Present the buying story | Sales deck | Slide-by-slide narrative and speaker notes |
| Leave a concise internal share | One-pager | Scannable problem, value, proof, and CTA |
| Prepare for pushback | Objection guide | Objection, underlying concern, response, proof, follow-up |
| Run a focused product session | Demo script | Timed scenes tied to discovered buyer pain |
| Quantify value | ROI model | Inputs, formulas, assumptions, scenarios, and payback |
| Formalize the offer | Proposal | Scope, responsibilities, timeline, investment, next steps |
| Standardize the motion | Playbook | ICP, qualification, discovery, proof, objections, and process |
| Equip internal champions | Persona/champion card | Role-specific priorities, messages, evidence, and objections |

Use a host document, presentation, spreadsheet, or PDF capability when the user requests a finished artifact and that capability is available. Otherwise deliver complete, format-ready content without claiming a binary file was created.

## Core structures

### Sales deck

Use a compact story: current problem → cost of inaction → relevant market shift → differentiated approach → three or four workflows → proof → implementation → value → pricing when approved → one next step. Tailor depth to the buyer; technical buyers need architecture and controls, economic buyers need value and risk, and champions need material they can repeat internally.

### One-pager

Keep it genuinely one page: buyer-specific headline, problem, approach, three differentiators, one verified proof block, and one CTA. Prefer whitespace and hierarchy over squeezing in more copy.

### Objection guide

For each objection capture the buyer's exact wording, likely concern, acknowledgement, response, evidence, and a useful follow-up question. Do not dismiss real budget, security, integration, legal, or timing constraints.

### Demo script

Map each scene to a discovery finding. Include timing, setup, workflow, intended outcome, interaction question, proof, and next step. Never bluff when a requested capability is unavailable.

### ROI model

Show user-editable inputs, units, formulas, base/conservative/upside cases, payback period, and sensitivity. Separate observed customer data from benchmarks and assumptions. Avoid double-counting time, cost, and revenue benefits.

## Output header

Start substantial deliverables with:

```markdown
**Asset:** [type]
**Audience:** [buyer/persona]
**Deal stage:** [stage]
**Decision to enable:** [decision]
**Evidence used:** [sources]
**Open placeholders:** [items or None]
```

## Quality gate

- The asset addresses one audience, stage, and next decision.
- Every material claim is sourced, user-provided, or visibly marked as a placeholder.
- Features are translated into buyer outcomes without exaggeration.
- Objections and risks are handled honestly.
- ROI math reconciles and assumptions are editable.
- The CTA is specific and proportionate to the deal stage.

## Failure handling

- If product evidence is thin, produce a discovery brief or placeholder-based draft rather than fabricated collateral.
- If sources conflict, flag the conflict and omit the contested claim until resolved.
- If the requested final format cannot be generated, provide format-ready content and state what remains to be laid out.
- Do not send collateral, contact prospects, or update a CRM without explicit authorization.
