---
name: standup-from-activity
description: "Write a standup update (yesterday / today / blockers) from the user's real activity: git commits, pull requests, and review activity, plus any notes they give. Use when the user says \"standup\", \"what did I do yesterday\", \"daily update\", \"write my status\", or pastes rough notes to turn into an update. Not for weekly reports to management or timesheets."
license: MIT
metadata:
  author: codertushar
  version: "1.0"
---

# Standup from activity

The update must only contain things that actually happened. If the activity is thin, the update is short. Never pad.

## Steps

1. **Work out the window.** Default to the previous working day (Friday when today is Monday). Use the user's local timezone; ask if unknown.

2. **Collect activity** for the user only, within the window:
   - Commits: `git log --author="<user>" --since=<start> --until=<end> --all --no-merges --format='%h %ad %s' --date=local` in each repo the user names (default: the current repo).
   - Pull requests: if the `gh` CLI is available, `gh search prs --author=@me --updated=">=<start-date>"` and `gh search prs --reviewed-by=@me --updated=">=<start-date>"`.
   - Anything the user pastes (meetings, notes, tickets).

3. **Group by outcome, not by commit.** Five commits on one feature become one line about that feature. Use the PR title or ticket as the anchor.

4. **Draft** in this exact format:

   ```
   Yesterday
   - <outcome> (<PR link or ticket>)
   Today
   - <plan>
   Blockers
   - <blocker, or "None">
   ```

   - "Today" comes from open PRs awaiting the user, review requests, and what the user tells you. If you have nothing to base it on, write `- <fill in>` rather than guessing.
   - Each line: max about 15 words, starts with a verb, no internal jargon the reader won't know.

5. **Show the draft and the raw activity you used**, so the user can see nothing was invented.

## Rules

- Never claim something is "done" or "merged" unless the data shows it.
- Skip noise: merge commits, formatting-only commits, dependency bot PRs (unless the user handled a breaking one).
- If there is no activity at all in the window, say so and ask the user what to report.
