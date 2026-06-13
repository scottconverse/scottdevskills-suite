# Prompt Lint Rules

Check prompts for:

- Ambiguous role, task, audience, or success criteria.
- Contradictory instructions or priority inversions.
- Missing output schema, examples, or failure behavior.
- Hidden dependency on unavailable context.
- Tool-use instructions without tool availability or stop conditions.
- Overbroad autonomy, unsafe side effects, or missing confirmation gates.
- Prompt injection exposure when user or retrieved text is included.
- Excessive context that can be moved into references, files, or examples.
- Eval claims without test cases.
- Cost-sensitive tasks without model, budget, or scope guidance.

Prefer small edits tied to specific risks over broad rewrites.
