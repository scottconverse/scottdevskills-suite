---
name: agent-pipeline
description: Router for the ScottDevSkills Codex agent pipeline. Use when the user asks to understand, install, initialize, create, run, resume, validate, or inspect a manifest-driven pipeline. Prefer pipeline-init, new-run, intake, run-pipeline, show-run-status, validate-manifest, or audit-init when the requested stage is explicit.
---

# Agent Pipeline

## Purpose

Route pipeline requests to the smallest stage skill that matches intent.

## Routing

- Use `pipeline-init` to scaffold a repo for pipeline use.
- Use `intake` to capture a task without starting execution.
- Use `new-run` to create a run skeleton from templates.
- Use `validate-manifest` to check a manifest before execution.
- Use `run-pipeline` to execute or resume a run.
- Use `show-run-status` to inspect a run without mutating it.
- Use `audit-init` to scaffold dual-agent audit handoff infrastructure.

## Source Of Truth

This suite uses the namespaced Agent Pipeline for Codex materials as its source
for pipeline assets and behavior. Read `references/README.md`,
`references/USER-MANUAL.md`, or `references/ARCHITECTURE.md` only when a
concrete pipeline question needs that depth.

## Output

State the selected stage skill, why it matches, required inputs, and stop
condition. For status-only tasks, do not resume or mutate the run.
