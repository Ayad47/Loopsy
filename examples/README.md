# Feedback loop example

The objective is to produce `42`. The first candidate is `41`, so the verifier returns `expected 42`. The generator receives that evidence and returns `42`; verification passes and the loop stops.

This is a minimal deterministic demonstration, not a production harness. It does not enforce time, token, or cost budgets, persist state, invoke models, or manage side effects. Real integrations need those controls where relevant.

