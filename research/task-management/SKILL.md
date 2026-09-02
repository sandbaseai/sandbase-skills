---
name: task-management
description: "Manage a shared TASKS.md file for project tasks, commitments, waiting items, and completed work. Use when the user asks to add, review, update, prioritize, or complete repository-local tasks."
license: Apache-2.0
metadata:
  source: "https://github.com/anthropics/knowledge-work-plugins/tree/77961df00a4626bc3b83850064289decd5a3b977/productivity/skills/task-management"
  modified: "Adapted for host-neutral file operations and non-destructive retention."
---

# Task Management

Use a `TASKS.md` file as a small, human-editable task tracker. Work with the file directly using the host's ordinary file tools; no dashboard, plugin, or external service is required.

## Scope and authorization

- Use `TASKS.md` in the current project unless the user names another file.
- Read-only questions do not authorize creating or editing the file. If it is missing, report that and offer the template.
- A request to add, update, move, or complete a task authorizes only that requested edit.
- Preserve user-authored sections, comments, ordering, and fields that this Skill does not understand.
- Never delete old completed tasks automatically. Archive or remove them only when the user asks.

## Default format

Create this structure only when an edit is requested and no task file exists:

```markdown
# Tasks

## Active

## Waiting On

## Someday

## Done
```

Use compact task records:

```markdown
- [ ] **Task title** — context; owner: Name; due: YYYY-MM-DD
  - Optional detail or dependency
```

Omit fields the user did not provide. Do not invent owners or deadlines. Mark completed tasks as:

```markdown
- [x] ~~Task title~~ — completed: YYYY-MM-DD
```

## Workflow

1. Read the current file before answering or editing.
2. Identify the requested task unambiguously. If multiple tasks match a completion or move request, ask which one.
3. Apply the smallest possible change. Keep valid custom formatting when practical.
4. Re-read the changed section and confirm that the task appears exactly once.
5. Summarize what changed and surface overdue or blocked work only when relevant.

For a status request, summarize `Active` and `Waiting On` first, call out explicit deadlines, and distinguish overdue dates from dates that are merely approaching.

When extracting tasks from a meeting or conversation, propose a list before writing it. Add the tasks only after the user approves or explicitly requests the addition.

## Quality gate

- Every added task has a clear action, not a vague topic.
- Dates use ISO `YYYY-MM-DD` when an exact date is known.
- Completed tasks are not duplicated in `Active`.
- Unknown details remain omitted or explicitly unknown rather than guessed.
- No unrelated file content changed.

## Failure handling

- If the task file cannot be parsed safely, show the ambiguous portion and ask before restructuring it.
- If an edit conflicts with newer file content, re-read and reapply only the intended change.
- If the user requests reminders or external task synchronization, explain that this Skill manages the file only and use another available capability only with the user's authorization.
