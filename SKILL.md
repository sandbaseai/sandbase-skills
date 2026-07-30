---
name: sandbase
description: Use the configured SandBase MCP tools when a request needs SandBase capabilities, including discovering available tools, retrieving live information, creating content, or completing a SandBase-backed workflow. Use when the user invokes /sandbase or asks to use SandBase.
---

# SandBase

Use the configured SandBase MCP server for relevant requests.

1. Inspect the available SandBase MCP tools when the appropriate tool is unknown.
2. Choose the smallest suitable tool and call it with only the inputs needed for the request.
3. If SandBase is not configured, a tool is unavailable, or a tool fails, explain the meaningful failure clearly. Do not fabricate a result or silently switch providers.
4. Do not change local configuration, credentials, or unrelated settings while fulfilling a request.

Examples:

- `/sandbase` — inspect SandBase's available tools before selecting a workflow.
- “Use SandBase to get the latest information about …”
- “Use SandBase to create a presentation about …”
