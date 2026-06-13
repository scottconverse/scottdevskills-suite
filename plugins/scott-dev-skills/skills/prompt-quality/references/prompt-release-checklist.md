# Prompt Release Checklist

Before shipping a prompt change, verify:

- The changed prompt has a named owner and intended behavior.
- Output contract is explicit enough for tests or review.
- Known failure examples are represented in regression cases.
- Tool-use behavior is bounded and observable.
- Safety, privacy, and side-effect rules are explicit.
- Cost or latency impact is understood when relevant.
- Downstream parsers, schemas, docs, and examples still match.
- Rollback path is clear for production prompts.

Report unresolved items as release risks, not as polish.
