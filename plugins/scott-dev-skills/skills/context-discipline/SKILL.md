---
name: context-discipline
description: Manage long Codex sessions, large tool output, context pressure, handoffs, scope locks, and careful coding discipline. Use when the session is getting long, output is large, token burn is a concern, state must be preserved, or non-trivial code work needs blast-radius tracing. Do not use for normal short tasks.
---

# Context Discipline

## Purpose

Keep long development sessions coherent, cheap enough, and recoverable.

## Workflow

1. Identify the context risk: large output, unclear scope, long-running task,
   cross-file blast radius, or imminent handoff.
2. Prefer targeted reads, search, summaries, durable artifacts, and subagent
   isolation over loading broad output into context.
3. For non-trivial code work, trace callers, runtime paths, data contracts,
   tests, and likely blast radius before editing.
4. Preserve state in a handoff artifact when work must continue later.
5. Recommend narrowing scope when the context budget is hiding risk.

## References

- `references/large-output.md` for output triage.
- `references/handoff.md` for handoff content.
- `references/careful-coding.md` for pre-edit analysis.
- `../../references/output-contracts.md#context-discipline` for output shape.

## Output

State the context risk, the containment move, the preserved state or artifact,
and the next safe unit of work.
