---
name: meeting-minutes
description: "Turn meeting transcripts, recordings, or notes into concise minutes with decisions, action items, owners, due dates, unresolved questions, and follow-up steps."
license: MIT
metadata:
  source: "https://github.com/github/awesome-copilot/tree/6a8fa297b0fe652bd3d7c8946554dc146846b20e/skills/meeting-minutes"
  modified: "Condensed and adapted for host-neutral artifact creation and privacy-safe handling."
---

# Meeting Minutes

Create a factual, action-oriented record from the material the user provides. Optimize for decisions and follow-through rather than a verbatim transcript.

## Inputs

Use any available combination of:

- meeting title, date, duration, organizer, and attendees;
- agenda, transcript, recording-derived text, chat log, or rough notes;
- intended audience and desired output location or format.

Infer harmless formatting details when reasonable. If missing context would materially change ownership, deadlines, or a recorded decision, ask a focused question or mark the field `TBD`; do not block on optional metadata.

## Workflow

1. Identify the meeting objective and source material.
2. Separate explicit decisions, proposals, open questions, risks, and action items.
3. Preserve names, dates, ticket IDs, links, and quoted commitments exactly when supplied.
4. Assign an owner or due date only when stated or clearly confirmed. Otherwise use `TBD`.
5. Draft the concise schema below, omitting empty optional sections.
6. Check every claim against the source and flag unclear or conflicting passages.

## Output

```markdown
# [Meeting title]

**Date:** YYYY-MM-DD

**Participants:** ...

**Source:** transcript | notes | chat | mixed

## Outcome
[One to three sentences]

## Decisions
- **D1:** Decision — approver; rationale if recorded

## Action items
| ID | Action | Owner | Due | Completion criteria |
|---|---|---|---|---|
| A1 | ... | ... | YYYY-MM-DD or TBD | ... |

## Discussion notes
- **Agenda item:** factual summary

## Open questions
- Question — owner or next step

## Risks and blockers
- Risk — impact — mitigation owner

## Follow-up
- Next meeting or review step
```

For a short meeting, keep only Outcome, Decisions, Action items, and Open questions. Use timestamps when they help reviewers find the source passage.

## Privacy and actions

- Exclude incidental personal data, credentials, private side conversations, and sensitive details that are not needed in the record.
- Do not send, publish, upload, or create tracker items unless the user explicitly requests that external action.
- If the user asks to add action items to `TASKS.md`, use the task-management workflow and preserve the minutes as the source of truth.

## Quality gate

- Decisions are distinguished from suggestions and unresolved proposals.
- Every action item has an action and an owner/due status, even if that status is `TBD`.
- No participant is assigned work based only on inference.
- Dates and names are internally consistent.
- The minutes are concise and traceable to the supplied material.

## Failure handling

- If the source is incomplete, produce partial minutes and list the gaps.
- If speakers or owners are ambiguous, retain the ambiguity instead of choosing a person.
- If sources disagree, show the conflict and request review before presenting a decision as final.
