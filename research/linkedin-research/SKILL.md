---
name: linkedin-research
description: Research companies, professionals, job markets, and industry content on LinkedIn through SandBase. Use when asked for LinkedIn research, company analysis, professional profiling, job market research, or B2B competitive intelligence.
---

# LinkedIn Research

LinkedIn professional intelligence through SandBase. Research companies, analyze professional profiles, track industry content, and monitor job markets. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Use LinkedIn data for professional research and B2B intelligence only.
- Respect professional privacy — report on public information only.
- Preserve context: include company names, titles, dates, and engagement.
- Never attempt to connect, message, or apply on behalf of the user.

## Workflow

### 1. Company research

Use `linkedin_web_v2_company_profile` for company details (size, industry, description, specialties).
Use `linkedin_web_v2_company_posts` for company content strategy and engagement.

### 2. Professional research

Use `linkedin_web_v2_user_profile` for professional background and current role.
Use `linkedin_web_v2_user_posts` for thought leadership and content activity.

### 3. Job market research

Use `linkedin_web_v2_search_jobs` to find open positions by keyword, location, or company.
Use `linkedin_web_v2_job_detail` for detailed job requirements and qualifications.

### 4. Content analysis

Use `linkedin_web_v2_post_detail` for specific post metrics.
Use `linkedin_web_v2_post_comments` for professional discourse and reactions.

## Output

Return: company overview, team structure insights, content strategy analysis, job market signals, and competitive positioning.

## Example tasks

- "Research [company] on LinkedIn — size, industry positioning, recent posts."
- "What is [person]'s professional background and current role?"
- "Find open [role] positions at companies in [industry] in [location]."
- "What content is [company] posting on LinkedIn? Analyze their strategy."
- "Compare hiring patterns between [company A] and [company B]."
