# Loopsy

**Build AI agent loops that verify their work and stop when they are stuck.**

Loopsy is an agent skill for designing self-correcting AI workflows with verification, bounded retries, and clear stop conditions. It guides a coding agent; it is not itself an autonomous runtime or a guarantee of safe execution.

## Quick start

Copy the [skill folder](generate-agentic-loop/) to `.agents/skills/generate-agentic-loop/` in your project, then reload your agent if needed. Ask:

> Use generate-agentic-loop to build a loop that repairs a failing test. Stop after three attempts, verify with the test suite, and report evidence and remaining failures.

Actual behavior depends on the agent, tools, and environment. Review generated code before running it.

## Try the example

```sh
python examples/repair_loop.py
python -m unittest discover -s tests -v
```

The deterministic example verifies a candidate, feeds a failure into the next attempt, and stops on success or a limit. [Read the walkthrough](examples/README.md). It uses no model, network, or credentials and does not measure AI performance.

## Compatibility and evaluation

The skill passed the Codex structure validator. Codex installation and other agent integrations have not yet been tested end to end. See [evaluation](EVALUATION.md) for evidence and limitations.

## Principles

- Separate the agent cycle from the harness enforcing limits.
- Require evidence for success and preserve useful failure information.
- Stop on exhaustion, repeated failure, interruption, or a blocker.
- Compact state without inventing facts or discarding authorization boundaries.
- Report limits that cannot be enforced instead of promising hard caps.

See [contributing](CONTRIBUTING.md), [changelog](CHANGELOG.md), and [license](LICENSE).

