---
name: prd
description: "Create decision-ready product requirements documents for software and AI features, including scope, user flows, measurable requirements, acceptance criteria, risks, rollout, and evaluation."
license: MIT
metadata:
  source: "https://github.com/github/awesome-copilot/tree/6a8fa297b0fe652bd3d7c8946554dc146846b20e/skills/prd"
  modified: "Adapted for host-neutral discovery, evidence handling, and flexible PRD depth."
---

# Product Requirements Document

Convert a product idea or existing brief into requirements that product, design, engineering, data, security, and go-to-market stakeholders can review and implement.

## Intake

Collect or infer:

- problem, affected users, current workflow, and urgency;
- desired outcome and measurable success signals;
- in-scope and out-of-scope behavior;
- platform, integrations, data, privacy, accessibility, budget, and timeline constraints;
- known dependencies, risks, and unresolved decisions.

Read supplied research, tickets, specifications, and repository context before asking questions. Ask only when a missing choice would materially change scope. Mark unresolved product decisions `TBD` with an owner or validation step; do not invent constraints.

## Workflow

1. State the problem and evidence without prescribing a solution prematurely.
2. Define personas or actors and their end-to-end flows.
3. Separate goals, requirements, non-goals, assumptions, and open questions.
4. Write testable functional and non-functional requirements.
5. Define success metrics with baseline, target, measurement window, and owner when known.
6. Identify dependencies, failure modes, security/privacy concerns, rollout controls, and rollback conditions.
7. For AI features, specify data boundaries, model/tool behavior, evaluation cases, human review, latency/cost targets, and unsafe or abstention behavior.
8. Review for contradictions, unmeasurable language, and hidden scope.

## Output

Scale the document to the decision. Use this full structure for substantial work:

```markdown
# PRD: [Product or feature]

## Executive summary
## Problem and evidence
## Goals and success metrics
## Users and user journeys
## Scope
### In scope
### Non-goals
## Requirements
### Functional
### Non-functional
## Acceptance criteria
## Data, integrations, security, privacy, and accessibility
## AI behavior and evaluation (when applicable)
## Dependencies and operational readiness
## Rollout, rollback, and monitoring
## Risks and mitigations
## Open questions and decisions
```

Use stable requirement IDs such as `FR-1`, `NFR-1`, and `AC-1` when traceability matters. Link acceptance criteria to requirements rather than duplicating them.

## Quality gate

- Requirements describe observable behavior and avoid vague words such as “fast,” “easy,” or “smart” without a measure.
- Success metrics distinguish business outcomes from operational health metrics.
- Every critical user flow has failure and recovery behavior.
- Non-goals protect the agreed scope.
- AI quality claims have an evaluation method and dataset or sampling plan.
- Facts from research or repository inspection are cited; assumptions are labeled.

## Failure handling

- If evidence is insufficient, write a clearly labeled draft and a prioritized discovery list.
- If stakeholders or sources conflict, preserve both positions and identify the decision owner.
- If the user requests implementation as well as a PRD, finish or confirm the requirements boundary before making code changes that depend on unresolved choices.
