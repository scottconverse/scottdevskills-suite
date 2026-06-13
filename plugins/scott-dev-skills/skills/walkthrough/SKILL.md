---
name: walkthrough
description: Playwright-driven product walkthrough and interface wiring audit for finished or nearly finished frontends. Use for UI walkthroughs, route exploration, product readiness checks, button/control wiring, console/network review, screenshots, and frontend behavior versus docs. Prefer audit-full for broad non-UI release audits.
---

# Walkthrough

## Purpose

Audit the running interface as a real user and adversarial QA reviewer. Determine
what works, what is cosmetic, what is broken, and what diverges from docs,
design, source, tests, or backend capabilities.

## Activation Boundaries

Use when the user asks for a walkthrough, interface wiring audit, Playwright
exploration, product UI readiness check, or cross-check of frontend behavior.
Default to audit mode and do not fix source unless explicitly asked.

## Workflow

1. Build a product model from docs, specs, routes, components, state, APIs,
   schemas, tests, fixtures, and design references.
2. Start the app using repo-discovered scripts and capture setup failures.
3. Explore primary routes, workflows, forms, state-changing actions, navigation,
   mobile/desktop layouts, empty/loading/error/success states, and permissions.
4. Inspect console errors, failed requests, broken assets, persistence behavior,
   route guards, and frontend/backend mismatches.
5. Compare UI promises against implemented system behavior and test coverage.
6. Write the report using `references/report-template.md`.

## Evidence Standard

Use screenshots, traces, console/network logs, accessibility snapshots, DOM
inspection, source references, tests, and docs. For repeated patterns, audit a
representative sample and state the pattern scope.

## References

- `references/report-template.md` for report shape.
- `references/route-inventory.md` for route coverage.
- `references/playwright-evidence.md` for runtime evidence.
- `references/ui-wiring-checklist.md` for wiring checks.
- `references/failure-modes.md` for blocked walkthrough handling.
- `../../references/output-contracts.md#walkthrough` for required sections.
