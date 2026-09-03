---
name: task-management
description: Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.
---

# Task Management

Tasks are tracked in a simple `TASKS.md` file that both you and the user can edit.

When task sources are supplied as web pages, read [the SandBase API map](references/sandbase-api-map.md) and use only the capabilities listed there. Resolve each current input schema with `sandbase_describe_tool` before calling it through `sandbase_call_tool`.

## File Location

**Always use `TASKS.md` in the current working directory.**

- If it exists, read it and make only user-requested edits
- If it doesn't exist, offer the template below; create it when the user asks to add or manage tasks

## Optional Dashboard

If the project already provides a task dashboard, it may be used with the same
`TASKS.md` file. Do not create or copy dashboard assets unless the user requests
that separately and a valid source asset is available.

## Format & Template

When creating a new TASKS.md, use this exact template (without example tasks):

```markdown
# Tasks

## Active

## Waiting On

## Someday

## Done
```

Task format:
- `- [ ] **Task title** - context, for whom, due date`
- Sub-bullets for additional details
- Completed: `- [x] ~~Task~~ (date)`

## How to Interact

**When user asks "what's on my plate" / "my tasks":**
- Read TASKS.md
- Summarize Active and Waiting On sections
- Highlight anything overdue or urgent

**When user says "add a task" / "remind me to":**
- Add to Active section with `- [ ] **Task**` format
- Include context if provided (who it's for, due date)

**When user says "done with X" / "finished X":**
- Find the task
- Change `[ ]` to `[x]`
- Add strikethrough: `~~task~~`
- Add completion date
- Move to Done section

**When user asks "what am I waiting on":**
- Read the Waiting On section
- Note how long each item has been waiting

## Conventions

- **Bold** the task title for scannability
- Include "for [person]" when it's a commitment to someone
- Include "due [date]" for deadlines
- Include "since [date]" for waiting items
- Sub-bullets for additional context
- Keep completed items for at least ~1 week; clear or archive them only when the user requests it

## Extracting Tasks

When summarizing meetings or conversations, offer to add extracted tasks:
- Commitments the user made ("I'll send that over")
- Action items assigned to them
- Follow-ups mentioned

Ask before adding - don't auto-add without confirmation.
