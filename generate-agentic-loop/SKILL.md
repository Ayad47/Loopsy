---
name: generate-agentic-loop
description: Design or implement bounded, self-correcting agent execution loops with verification, resource limits, and recoverable state. Use when a user asks to build or improve an agent loop or its execution harness.
---

# Generate agentic loops

Translate the user's objective into an executable loop and an operational harness. Adapt to the requested language, platform, tools, and risk; do not assume Python or background processes are available.

1. Define the objective, scope, authorized actions, measurable acceptance criteria, and independent verification. Identify dependencies and assumptions. If success cannot be objectively verified, report the limitation and require a suitable review instead of claiming success.
2. Select a pattern appropriate to the task: maker-checker, tool/error feedback, or a long-running loop with persisted state. Separate the agent's observe → act → verify → refine cycle from the harness that enforces permissions, limits, and tool execution.
3. Define explicit terminal outcomes: success, iteration limit, budget limit, stall, blocker, interruption, and execution error. Success requires all acceptance checks to pass; a model's unsupported PASS is not sufficient. Return the outcome, evidence, last verified result, and remaining work.
4. Set finite iteration and time limits and, when usage can be measured, token and cost limits. Check limits before each operation and account for actual usage afterward; document any overshoot or unenforceable limit. Bound tool calls with timeouts. Never claim a hard cost cap when the provider cannot enforce one.
5. Preserve actionable failure evidence, including exact errors where safe, and use it to choose the next action. Detect repeated failures and unchanged outputs, but do not mistake an identical output for a stall before evaluating it. Halt after a configurable consecutive repeat threshold; distinguish transient failures from missing permissions or credentials. Do not retry irreversible actions without idempotency or reconciliation.
6. Compact context into an objective, constraints, verified facts and evidence references, current failures, recent attempts, and next action. Keep essential instructions and authorization boundaries. Store large artifacts externally only where available and authorized; redact secrets and apply appropriate retention. Summaries must not invent verified facts. Background memory curation is optional and must not silently change governing instructions.
7. Implement and test the requested solution. Cover successful verification, failed verification, exhaustion, repeated failure, interruption, and budget accounting as applicable. State what was tested and what remains unverified. Never represent a template as production-ready without integration and operational validation.

When producing a design, include the chosen architecture, state and action interfaces, verification evidence, stop conditions, resource enforcement, recovery behavior, and assumptions. When implementing, adapt these contracts to the actual environment and expose configuration rather than inventing credentials or permissions.

