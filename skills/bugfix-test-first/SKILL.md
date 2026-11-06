---
name: bugfix-test-first
description: "Fix a bug by first writing a test that reproduces it, proving the test fails, then making the smallest change that turns it green without weakening any existing test. Use when the user reports a bug, pastes an error or stack trace, links a bug ticket, or says \"fix this\", \"this is broken\", \"regression\". Not for new features, refactors, or flaky-test investigations where the code is not actually wrong."
license: MIT
metadata:
  author: codertushar
  version: "1.0"
---

# Bugfix, test first

A bug is fixed when a test that used to fail now passes and nothing else got worse. Not when the error message goes away.

## Steps

1. **Restate the bug in one sentence**: input, expected behaviour, actual behaviour. If any of the three is unknown, ask the user before touching code.

2. **Find where it lives.** Read the code path from the entry point to the failure. Note the file and function you believe is wrong and why. Do not edit yet.

3. **Write the reproducing test.**
   - Put it next to the existing tests for that code, following their style and framework.
   - Name it after the behaviour, not the ticket: `returns_empty_list_when_filter_matches_nothing`, not `test_bug_123`.
   - The test must exercise the real code path. Do not mock the function under test.

4. **Run it and show it failing.** Paste the relevant failure output. If it passes, your understanding of the bug is wrong: go back to step 2. Never skip this step.

5. **Make the smallest fix** that addresses the cause found in step 2. No drive-by refactors, renames or formatting changes in the same diff.

6. **Run the new test, then the full relevant suite.** Paste the result.

7. **Hand back** with:
   - the one-sentence bug statement
   - the root cause (one or two sentences)
   - the test name and the failing output from step 4
   - the diff summary
   - anything you noticed but deliberately did not change

## Hard rules

- **Never** delete, skip, loosen or rewrite an existing assertion to make the suite pass. If an existing test conflicts with the fix, stop and ask.
- **Never** catch-and-ignore an exception as the fix.
- If you cannot reproduce the bug in a test after two honest attempts, stop and report what you tried. Do not ship a speculative fix.
- If the fix touches more than about 3 files or 50 lines, stop and confirm the approach with the user first.
