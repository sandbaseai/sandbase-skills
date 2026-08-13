---
name: domain-intelligence
description: "Research any domain with WHOIS data, DNS records, SSL certificate details, domain age, reputation scoring, and security header analysis. Covers ownership research, infrastructure mapping, security assessment, and competitive domain analysis."
---

# Domain Intelligence

Research any domain with WHOIS data, DNS records, SSL certificate details, domain age, reputation scoring, and security header analysis. Covers ownership research, infrastructure mapping, security assessment, and competitive domain analysis. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `strale_whois_lookup`
- `strale_dns_lookup`
- `strale_ssl_check`
- `strale_domain_age_check`
- `strale_domain_reputation`
- `strale_header_security_check`

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
