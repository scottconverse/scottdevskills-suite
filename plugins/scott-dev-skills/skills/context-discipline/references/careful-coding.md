# Careful Coding

Before non-trivial edits, trace:

- Callers and entrypoints.
- Runtime context and data flow.
- Shared helpers, contracts, schemas, and generated files.
- UI render paths and backend persistence paths.
- Tests that should fail if the change is wrong.
- Migration, compatibility, and rollback concerns.
- Nearby patterns the repo already uses.

After edits, self-audit against the original intent, blast radius, and tests.
