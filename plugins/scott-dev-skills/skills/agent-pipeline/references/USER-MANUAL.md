# ScottDevSkills Agent Pipeline Manual

## Purpose

The Agent Pipeline turns broad development work into a staged, evidence-first
workflow. It gives Codex a durable run directory, explicit scope, stage outputs,
policy checks, and human gates. Use it when the cost of drift is higher than the
cost of structured setup.

## When To Use It

Use the pipeline for:

- Multi-step feature or bugfix work.
- Release preparation or module migration work.
- Work that must respect a strict allowed-path boundary.
- Tasks where implementation, verification, and audit evidence need to survive
  context changes.
- Projects where a human director wants explicit gate points.

Do not use it for:

- A small code review that fits `audit-lite`.
- A pure UI wiring check that fits `walkthrough`.
- A prompt review that fits `prompt-quality`.
- A single quick edit with obvious tests and low blast radius.

## Stage Skills

| Stage skill | Responsibility | Mutates files? |
| --- | --- | --- |
| `pipeline-init` | Adds project pipeline scaffolding and policy scripts. | Yes |
| `intake` | Drafts run artifacts from plain language. | Yes, draft files only |
| `new-run` | Creates one run skeleton from templates. | Yes |
| `validate-manifest` | Checks manifest and scope-lock readiness. | No, unless asked to fix |
| `run-pipeline` | Executes or resumes a staged run. | Yes |
| `show-run-status` | Reports run state without resuming. | No |
| `audit-init` | Adds audit-handoff infrastructure. | Yes |

## Project Initialization

`pipeline-init` orients on the project before writing anything. It identifies
whether the user supplied a PRD/spec, an existing repo, or a project
description. Then it scaffolds:

- `.pipelines/` from the bundled payload directory `../../p/p/`.
- `scripts/policy/` from the bundled payload directory `../../p/s/`.
- `.gitignore` support for `.agent-runs/`.
- Starter `AGENTS.md` guidance only when the project does not already have one.

Existing project instructions are preserved. Existing pipeline directories are
treated as re-initialization and require an explicit update decision.

## Run Creation

Use `new-run` when the pipeline type and slug are already known. It creates:

- `.agent-runs/<run-id>/manifest.yaml`
- `.agent-runs/<run-id>/scope-lock.yaml`

Use `intake` when the user has a plain-language task and needs a conservative
draft. Intake creates the same run directory plus an `intake.md` and optional
`intake-questions.md`. Intake does not validate or execute the run.

## Manifest Readiness

A run is not ready until the manifest and scope lock contain:

- A specific goal.
- Explicit allowed and forbidden paths.
- Testable expected outputs.
- A rollback plan.
- A definition of done.
- Current rung or scope-lock facts from a canonical source when applicable.

`validate-manifest` reports blockers and warnings before execution begins.

## Execution

`run-pipeline` reads `.pipelines/<pipeline-type>.yaml`, resumes from `run.log`,
and executes stages in order. Agent stages write artifacts into
`.agent-runs/<run-id>/`; policy stages run local checks; human gates ask for
approval or block feedback.

The runner is append-only for run history. It does not silently skip failed or
blocked stages. Resuming the same run reuses the log to find the next stage.

## Evidence Standards

Every meaningful stage output should include:

- What was read.
- What changed.
- What was verified.
- What remains blocked or intentionally deferred.
- File paths and line references where available.
- The next valid action.

Pipeline evidence is designed to feed directly into `audit-full` when a formal
release-readiness audit is needed.

## Failure Modes

Common failure modes:

- Manifest is vague or missing allowed paths.
- Scope lock conflicts with the user's latest request.
- Policy scripts detect path, TODO, workflow-cost, or release-doc drift.
- The run attempts to stop after green CI even though a next authorized action
  remains.
- An agent writes a sparse report without durable evidence.

In each case, the pipeline should stop with a named reason, a current stage, and
a recovery path.

## Relationship To Other Suite Skills

`agent-pipeline` is a router. It should choose a smaller stage skill whenever
the user names a specific action. `audit-full` audits the resulting repo or
release state. `walkthrough` can provide UI evidence that the verifier or audit
can cite. `context-discipline` supports handoffs when the run is long.

## Release Validation

For suite maintainers, release validation includes:

- Suite validation.
- Fresh install/list smoke checks with the current Codex CLI.
- JSON validation for regression and marketplace files.
- A short-path install smoke test.
- A long-path Windows install smoke test or an explicit documented caveat.
- A scan for stale standalone product names in active shipped docs.
