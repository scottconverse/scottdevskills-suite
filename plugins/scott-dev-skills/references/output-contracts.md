# Output Contracts

## audit-lite

- Lead with findings ordered by severity.
- Include file and line references when available.
- Include test gaps or residual risk after findings.
- Avoid executive-report sprawl.

## audit-full

- Produce an executive verdict, severity-ranked findings, role deep dives,
  blast radius, this-sprint punch list, next-sprint watchlist, and verification
  summary.
- Every material finding must include evidence, impact, likely cause, and
  suggested fix/test.

## walkthrough

- Include route/workflow coverage, runtime evidence, UI wiring verdict,
  console/network issues, persistence/auth notes, and high-value tests.
- Classify promised features as working, partial, broken, UI-only, backend-only,
  documented-not-built, or ambiguous.

## agent-pipeline

- State run id when known, current stage, required inputs, next action, stop
  condition, and recovery path.
- Preserve manifest, scope lock, and human-gate semantics.

## prompt-quality

- Report prompt risks by category, examples, expected behavior, improved
  wording when useful, and regression/eval cases.

## context-discipline

- Identify context risk, compression strategy, files/artifacts to preserve, and
  when to hand off or narrow scope.
