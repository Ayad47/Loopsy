"""A deterministic bounded feedback loop, not a production agent runtime."""
from dataclasses import dataclass


@dataclass
class Result:
    status: str
    attempts: int
    evidence: str


def run(generate, verify, max_attempts=3, repeat_limit=2, interrupted=lambda: False):
    if max_attempts < 1 or repeat_limit < 1:
        raise ValueError("limits must be positive")
    feedback = ""
    last_failure = None
    repeats = 0
    for attempt in range(1, max_attempts + 1):
        if interrupted():
            return Result("interrupted", attempt - 1, feedback)
        try:
            candidate = generate(feedback)
            passed, evidence = verify(candidate)
        except PermissionError as exc:
            return Result("blocked", attempt, str(exc))
        if passed:
            return Result("success", attempt, evidence)
        feedback = evidence
        repeats = repeats + 1 if evidence == last_failure else 1
        last_failure = evidence
        if repeats >= repeat_limit:
            return Result("stalled", attempt, evidence)
    return Result("exhausted", max_attempts, feedback)


if __name__ == "__main__":
    result = run(lambda feedback: "42" if feedback else "41",
                 lambda value: (value == "42", "verified: 42" if value == "42" else "expected 42"))
    print(f"{result.status} after {result.attempts} attempts: {result.evidence}")

