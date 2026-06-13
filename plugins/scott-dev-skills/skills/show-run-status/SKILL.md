---
name: show-run-status
description: Summarize an Agent Pipeline run from its run directory without resuming or mutating it. Use for status, current stage, blockers, next gate, or handoff summaries. Prefer run-pipeline when the user asks to execute or resume.
---

# Show Run Status

## Purpose

Give a read-only status summary of a pipeline run.

## Workflow

1. Find the requested or current run directory.
2. Inspect manifest, scope lock, logs, stage artifacts, stop reports, and gates.
3. Do not run stages, repair files, or update state.

## Output

State run id, pipeline type, current stage, last completed stage, blockers,
required human decision, and next valid action.
