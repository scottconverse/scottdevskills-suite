# Eval Design

For prompt regression testing, define:

- Task name and purpose.
- Input cases for happy path, boundary path, malformed input, adversarial input,
  and known failure reproduction.
- Expected output contract and disallowed output.
- Scoring method: exact match, rubric, schema validation, tool-call check, human
  review, or hybrid.
- Minimum pass threshold and examples of acceptable variance.
- Fixture ownership and update rules.

Keep evals small enough to run often. Add more cases when failures reveal new
classes of risk.
