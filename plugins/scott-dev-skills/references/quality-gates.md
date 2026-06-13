# Quality Gates

Use these gates across the suite when a skill needs a shared standard.

## Evidence

- Findings must cite observable evidence: file and line, runtime behavior,
  command result, screenshot, trace, console log, network result, test result,
  schema, spec, or reproduced workflow.
- Separate observed fact from inference. Label likely causes as likely causes,
  not proof.
- Do not report vague categories. Name the user path, component, endpoint,
  test, route, or artifact that failed.

## Severity

- Critical: data loss, security exposure, production outage, broken release
  gate, or a workflow that cannot be completed.
- High: important user workflow broken, misleading finished-looking UI,
  major regression, missing guardrail, or test gap hiding material risk.
- Medium: partial behavior break, confusing UX, brittle implementation, or
  docs/tests that would mislead maintainers.
- Low: local polish, naming, small docs mismatch, or low-risk cleanup.

## Decision Complete Plans

- State the goal, concrete success criteria, in-scope work, out-of-scope work,
  implementation approach, acceptance checks, and assumptions.
- Do not leave the implementer to choose file ownership, public interfaces,
  verification strategy, or compatibility behavior when those choices affect
  outcome.

## Acceptance Criteria

- Prefer behavior and evidence over implementation taste.
- Include happy path, failure path, edge case, and regression case when risk is
  meaningful.
- Tie each criterion to a test, manual check, or explicit non-testable
  inspection.
