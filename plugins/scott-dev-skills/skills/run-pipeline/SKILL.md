---
name: run-pipeline
description: Execute or resume an Agent Pipeline run from an agent-runs directory, honoring manifest order, human gates, policy checks, verification, drift detection, critique, and stop conditions. Use only when the user asks to run or resume; prefer show-run-status for read-only inspection.
---

# Run Pipeline

## Purpose

Orchestrate a manifest-driven run while preserving scope lock, stage evidence,
and human-gate semantics.

## Workflow

1. Read `references/run-pipeline.md`.
2. Locate the active run and validate manifest/scope lock before execution.
3. Execute stages in order, using role-scoped subagents where the reference
   requires isolation.
4. Stop at human gates, policy failures, verification failures, or unclear
   scope.
5. Keep run logs and status artifacts current.

## Output

State run id, completed stage, current blocker or next gate, verification
results, and exact recovery path. Do not hide failed gates.
