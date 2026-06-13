# Trigger Regression Cases

The JSON cases in `tests/skill-regression/cases.json` are the runnable source.
This file is the human-readable map.

## Positive Cases

- Quick fix review triggers `audit-lite`.
- Release readiness, deep review, or multi-role audit triggers `audit-full`.
- UI walkthrough, interface wiring audit, or Playwright exploration triggers
  `walkthrough`.
- Pipeline setup or resume requests trigger the matching pipeline skill.
- Prompt linting, eval design, and prompt regression review trigger
  `prompt-quality`.
- Long session, large output, context pressure, and handoff requests trigger
  `context-discipline`.
- Enforcement template requests trigger `hardgate-templates`.

## Negative Cases

- Domain-specific civic, patent, and Amazon work should not trigger suite-only
  domain packs.
- Generic code changes should not trigger audit skills unless the user asks for
  review/audit/readiness.
- A small fix audit should not trigger `audit-full`.
- A UI walkthrough should not become repair work unless explicitly requested.

## Collision Cases

- `audit-lite` beats `audit-full` for one bug fix or a few files.
- `walkthrough` beats `audit-full` when the task is specifically runtime UI
  wiring.
- `pipeline-init` beats `agent-pipeline` when initialization is explicit.
- `run-pipeline` beats `show-run-status` when the user asks to resume or run.
