---
name: email-validator
description: "Validate email addresses for deliverability, check reputation scores, verify MX records, and assess email-sending safety. Covers deliverability checks, reputation scoring, bounce risk assessment, and bulk validation for outreach campaign preparation."
---

# Email Validator

Validate email addresses for deliverability, check reputation scores, verify MX records, and assess email-sending safety. Covers deliverability checks, reputation scoring, bounce risk assessment, and bulk validation for outreach campaign preparation. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `strale_email_validate`
- `strale_email_deliverability_check`
- `strale_email_reputation_score`
- `strale_mx_lookup`

## Workflow

1. Understand the user's research question, target, and context.
2. Call `sandbase_describe_tool` for each selected tool to confirm parameter schema.
3. Call `sandbase_call_tool` with the exact tool_name and schema-defined arguments.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_describe_tool` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.
