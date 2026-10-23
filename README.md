Throwaway sandbox for the code review workshop.

**This is not production code.** This repository exists only so that new hires can
practice reading diffs, leaving inline review comments, and reacting to a failing
check on a pull request. Feel free to break it, comment on it, and re-run its
checks — that is the whole point.

## What is in here

| Path | What it is for |
| --- | --- |
| `REVIEW_GUIDE.md` | Reviewer cheat-sheet: the steps a reviewer walks through on any PR |
| `.github/workflows/pr-check.yml` | The GitHub Actions check that exercises `src/expenses.py` on pull requests |
| `src/expenses.py` | The sample module added by the practice pull request (two planted defects) |

## The practice pull request

The open pull request **"Add sample expense module for review practice"** adds
`src/expenses.py`, which contains two deliberate, easy-to-spot defects:

1. `convert_to_usd()` silently swallows unknown currencies (`except KeyError: pass`).
2. `total_in_usd()` adds raw amounts together even when the ledger mixes currencies.

The `expenses-checks` action fails on that pull request **on purpose**. The red ❌ is
part of the lesson: the checks and the review comments tell the same story.

## Housekeeping

- The two planted defects are tracked as sub-issues of the
  "Review workshop follow-ups" issue.
- Everything here is disposable. Do not use it as a template for real code.
