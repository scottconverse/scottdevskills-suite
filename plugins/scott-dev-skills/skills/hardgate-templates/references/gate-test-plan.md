# Gate Test Plan

Every gate needs tests for:

- Positive case: compliant behavior passes.
- Negative case: prohibited behavior fails.
- Boundary case: similar allowed behavior does not overfire.
- Missing-context case: gate fails closed or asks for context as designed.
- Recovery case: user or agent can see what must change.

For active hooks or policy scripts, include a dry run before installation and a
rollback path after installation.
