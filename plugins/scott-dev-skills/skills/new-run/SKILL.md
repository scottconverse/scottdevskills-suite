---
name: new-run
description: Create a new Agent Pipeline run skeleton from installed templates without executing it. Use when the user wants a fresh pipeline run, manifest, or scope-lock scaffold. Prefer intake for loose task capture and run-pipeline for executing or resuming an existing run.
---

# New Run

## Purpose

Create the minimum durable run structure needed for later execution.

## Workflow

1. Read `references/new-run.md`.
2. Choose the pipeline template from task type and repo context.
3. Create or describe the run id, manifest, scope lock, and intake linkage.
4. Stop before executing stages.

## Output

State the run id, created artifacts, selected template, remaining required
fields, and next valid stage.
