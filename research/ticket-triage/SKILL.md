---
name: ticket-triage
description: "Triage customer-support tickets by extracting the issue, assigning a P1-P4 priority, checking available context for duplicates, recommending a route, and drafting an initial response."
license: Apache-2.0
metadata:
  source: "https://github.com/anthropics/knowledge-work-plugins/tree/77961df00a4626bc3b83850064289decd5a3b977/customer-support/skills/ticket-triage"
  modified: "Removed unavailable connector placeholders and added host-neutral, non-mutating routing rules."
---

# Ticket Triage

Turn a customer message or issue report into a consistent triage assessment. Triage recommends what should happen; it does not send replies, update a support system, or page a team unless the user explicitly requests and authorizes that action.

## Intake

Extract what is actually known:

- symptom and expected behavior;
- affected users, accounts, environment, and product area;
- start time, frequency, reproducibility, and recent changes;
- error messages, identifiers, and available workarounds;
- data-loss, security, billing, or production-impact signals.

Ask only for missing information that could change severity or routing. Treat customer emotion as context, not as proof of technical severity.

## Classification

Choose one primary category and an optional secondary category:

| Category | Scope |
|---|---|
| Bug | Existing behavior is broken or incorrect |
| How-to | Guidance or configuration help |
| Feature request | Requested behavior does not exist |
| Billing | Charges, invoices, plans, refunds, or payments |
| Account | Access, permissions, identity, or user administration |
| Integration | APIs, webhooks, OAuth, sync, or third-party systems |
| Security | Vulnerability, unauthorized access, privacy, or compliance |
| Data | Missing, duplicated, corrupted, imported, or exported data |
| Performance | Latency, timeouts, degradation, or availability |

Classify by the likely root cause when evidence supports it. Otherwise state that the category is provisional.

## Priority

| Priority | Criteria | Default response target |
|---|---|---|
| P1 Critical | Active security incident, confirmed data loss/corruption, production outage, or most users blocked | Immediate escalation; continuous coordination |
| P2 High | Core workflow blocked, major account or many users affected, and no viable workaround | Same-day active investigation |
| P3 Medium | Limited impact, partial degradation, or a workable mitigation exists | Normal prioritized queue |
| P4 Low | Cosmetic issue, general question, low-impact request, or feature idea | Normal backlog or support queue |

Use the organization's SLA when supplied; the targets above are qualitative defaults, not contractual promises. Do not lower a security or data-loss report merely because only one reporter is known. If impact is unclear, label the priority provisional and name the fact needed to confirm it.

## Duplicate and known-issue checks

When the host exposes an authorized support platform, knowledge base, project tracker, or repository search, search by exact error, symptom, customer, and product area. Record where you searched and link matches. Without those tools, mark duplicate and known-issue status as `Not checked`; never claim `No duplicate` from absence of access.

## Routing

- Frontline support: documented how-to, access recovery, and routine billing questions.
- Senior support: complex configuration, investigations, and integration troubleshooting.
- Engineering: reproducible defects, infrastructure problems, and performance regressions.
- Product: validated feature requests and workflow gaps.
- Security/privacy: vulnerability, exposure, unauthorized access, or compliance incidents.
- Finance/billing: refunds, contract disputes, and complex account adjustments.

## Output

```markdown
## Triage: [one-line summary]

**Category:** Primary / Secondary
**Priority:** P1-P4 — evidence-based reason
**Confidence:** High | Medium | Low
**Route to:** Team or queue

### Impact and evidence
- Affected scope:
- Reproduction/error details:
- Workaround:
- Duplicate/known issue: Link | Not found in [sources] | Not checked

### Missing information
- Only questions that could change priority or route

### Suggested initial response
[Acknowledge the specific impact, state what is known, avoid unsupported promises,
and give a safe workaround or next update expectation when available.]

### Internal notes
- Checks already performed
- Escalation triggers
- Recommended next diagnostic step
```

## Quality gate

- Priority follows impact and urgency, not tone or customer tier alone.
- Security, privacy, and data-loss indicators are clearly surfaced.
- Search coverage and unknowns are explicit.
- The customer response contains no invented root cause, fix, or deadline.
- No external system was mutated without authorization.

## Failure handling

- If the report may describe an active security incident, recommend immediate security escalation and avoid requesting secrets or sensitive evidence in public channels.
- If different signals imply different priorities, choose the safer provisional priority and explain the conflict.
- If the ticket is too sparse to route, provide the preliminary assessment plus the minimum diagnostic questions.
