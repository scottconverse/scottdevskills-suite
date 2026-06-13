# ScottDevSkills Agent Pipeline

ScottDevSkills includes a Codex-native Agent Pipeline for work that benefits
from explicit manifests, staged evidence, policy checks, human gates, and
repeatable run state. It is not a separate plugin. It is one part of the
ScottDevSkills suite.

## What It Is Good For

- Feature, bugfix, release, and audit-prep work where scope must stay bounded.
- Long-running implementation work that needs durable artifacts in
  `.agent-runs/<run-id>/`.
- Projects where an agent should not infer permission to skip tests, stop after
  a push, or treat green CI as the final answer.
- Reviews that need a clear handoff from implementation evidence to audit
  evidence.

Use lighter suite skills when the work is smaller:

- `audit-lite` for a fast diff review.
- `audit-full` for a release-readiness audit.
- `walkthrough` for browser/UI wiring evidence.
- `prompt-quality` for prompt and eval review.
- `context-discipline` for long-session or handoff hygiene.

## Skill Map

| Skill | Use |
| --- | --- |
| `agent-pipeline` | Router for choosing the right pipeline stage. |
| `pipeline-init` | Scaffold `.pipelines/`, policy scripts, and starter project guidance. |
| `intake` | Turn a plain-language task into draft run artifacts without starting work. |
| `new-run` | Create a manifest and scope-lock skeleton for one run. |
| `validate-manifest` | Check manifest and scope-lock readiness before execution. |
| `run-pipeline` | Execute or resume the staged run. |
| `show-run-status` | Read current run state without mutating it. |
| `audit-init` | Scaffold dual-agent audit handoff materials. |

## Installed Payload

`pipeline-init` copies from the suite's bundled payload:

- `../../p/p/` -> target project `.pipelines/`
- `../../p/s/` -> target project `scripts/policy/`

Those package paths are intentionally short to keep Windows marketplace installs
under path-length limits. Target project paths stay readable.

## Normal Flow

1. Initialize the project with `pipeline-init`.
2. Create or draft a run with `new-run` or `intake`.
3. Complete the manifest and scope lock with explicit allowed paths,
   expected outputs, rollback plan, and definition of done.
4. Validate the manifest.
5. Execute with `run-pipeline`.
6. Inspect paused or completed runs with `show-run-status`.
7. Use `audit-full` or `audit-init` when the run needs formal verification or
   cross-agent audit handoff.

## Gates And Stop Conditions

The pipeline is intentionally conservative. It stops for real gates: human
approval, failed policy, missing credentials, destructive actions, scope
conflicts, unavailable external systems, or an explicit user pause.

It does not treat these as enough to stop by themselves:

- A successful push.
- Green CI.
- Draft PR status.
- A recommended next action.
- An unresolved but unverified caveat.

The goal is not autonomy for its own sake. The goal is to make each stop
explainable, evidence-backed, and resumable.

## Validation

The suite validator checks that required payload files exist, that shipped skill
names are canonical, that public metadata matches the suite version, that
legacy standalone product strings have not leaked into active docs, and that
packaged file paths stay short enough for Windows installs.

For release validation, run the install-smoke script from `scripts/` against a
fresh Codex home after publishing the branch or tag.
