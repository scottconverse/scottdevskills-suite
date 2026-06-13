# Walkthrough Failure Modes

## App Does Not Start

Record the attempted setup path, failing script, missing dependency or
environment variable, and whether static route/source review can continue.

## Auth Blocks Exploration

Look for seed users, test fixtures, auth bypass docs, mocked providers, or
unauthenticated routes. If unavailable, report auth as a blocker and continue
with source review.

## Missing Services

Identify required databases, queues, APIs, object storage, or local services.
Classify screens depending on them as blocked or partially testable.

## Flaky Or Slow UI

Retry once when reasonable, then distinguish deterministic defects from flaky
behavior. Do not hide flakiness behind a passing retry.

## No Browser Tool

Continue with source, test, route, and build review. State that runtime wiring
coverage is incomplete.
