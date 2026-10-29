import unittest
from examples.repair_loop import run


class LoopTests(unittest.TestCase):
    def test_feedback_enables_success(self):
        result = run(lambda feedback: "42" if feedback else "41",
                     lambda value: (value == "42", "ok" if value == "42" else "expected 42"))
        self.assertEqual((result.status, result.attempts, result.evidence), ("success", 2, "ok"))

    def test_repeated_failure_stalls(self):
        result = run(lambda _: "bad", lambda _: (False, "same error"))
        self.assertEqual((result.status, result.attempts), ("stalled", 2))

    def test_distinct_failures_exhaust_limit(self):
        errors = iter(["one", "two", "three"])
        result = run(lambda _: next(errors), lambda value: (False, value))
        self.assertEqual((result.status, result.attempts, result.evidence), ("exhausted", 3, "three"))

    def test_interrupt_before_action(self):
        result = run(lambda _: self.fail("must not run"), lambda _: (True, ""), interrupted=lambda: True)
        self.assertEqual((result.status, result.attempts), ("interrupted", 0))

    def test_missing_permission_blocks(self):
        def generate(_):
            raise PermissionError("missing credential")
        result = run(generate, lambda _: (True, ""))
        self.assertEqual((result.status, result.evidence), ("blocked", "missing credential"))

    def test_identical_candidate_can_pass(self):
        checks = iter([(False, "transient"), (True, "verified")])
        result = run(lambda _: "same", lambda _: next(checks))
        self.assertEqual(result.status, "success")


if __name__ == "__main__":
    unittest.main()

