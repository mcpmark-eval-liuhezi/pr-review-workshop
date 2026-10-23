# Reviewer cheat-sheet

Throwaway sandbox for the code-review workshop (see `README.md`). Use this page as
your walkthrough script when you review the practice pull request
"Add sample expense module for review practice" — and as a general checklist for
reviewing any pull request afterwards.

## Reviewer checklist

### 1. Read the pull request before the diff

Open the pull request and read the summary plus any linked issues or prior comments
before clicking **Files changed**. GitHub's own reviewer quickstart says to
"read through the pull request summary and any relevant comments or issues to build
context for reviewing"
(repo `github/docs`, file `content/pull-requests/get-started/reviewing-pull-requests-quickstart.md`).

### 2. Look at the checks

Glance at the status checks in the merge box. A red ❌ is a hint about where to look,
not a substitute for reading the code. In this sandbox the `expenses-checks` workflow
fails on purpose until the two planted defects are fixed — when a check is red,
open the failing job's log and read the failure message before you comment.

### 3. Read every changed file, line by line

Work through the diff top to bottom, including the parts that look boring. Ask two
questions per hunk: *what does this change do?* and *what could it break?* For the
practice PR, that second question is what surfaces both planted defects.

### 4. Start a review, and comment inline on the exact lines

Click the **+** on the line you are commenting on and choose **Start a review** so
your comments collect as pending instead of posting one at a time. Per the GitHub
quickstart, "Pending comments are visible only to you until you submit the review."

### 5. Suggest the fix, not just the problem

Where you know the exact change you want, put it in a suggestion block so the author
can apply it in one click; otherwise describe the desired behaviour precisely enough
that "fixed" is unambiguous.

### 6. Watch your tone — reviewers are the front door

Kubernetes spells out its reviewer expectations in repo `kubernetes/community`,
file `contributors/guide/expectations.md`: "Because reviewers are often the first
points of contact between new members of the community and can significantly impact
the first impression of the Kubernetes community, reviewers are especially important
in shaping the Kubernetes community." Critique the code, never the person, and prefer
questions to verdicts ("what happens when currency is missing?" beats "this is wrong").

### 7. Respond promptly

From the same Kubernetes file: "Reviewers are expected to respond in a timely fashion
to PRs that are assigned to them." If you cannot review, say so and hand the PR back
rather than letting it sit.

### 8. Submit the review with a decision

Write a short summary, then pick one of the three decisions (definitions quoted from
the GitHub quickstart): **Comment** "leaves feedback without explicitly approving or
requesting changes"; **Approve** "signals that the changes are ready to merge";
**Request changes** "flags feedback the author must address before merging." The
reviewer of the practice PR uses **Comment** and lists what must be fixed before merge.

### 9. Review commit messages too

Realm's contributing guide (repo `realm/realm-swift`, file `CONTRIBUTING.md`) asks for
specific commit-message formatting because "Following these guidelines helps with
the review process, searching commit logs and documentation of implementation
details." A commit message should convey the rationale of the change, not just that
something changed.

### 10. File the follow-ups

Anything you noticed but are not blocking on gets written down as an issue, so the
conversation does not have to live in the diff forever. In this repo the two planted
defects are attached as sub-issues of the "Review workshop follow-ups" issue.

## Real-world sources used in this guide

1. `github/docs` — `content/pull-requests/get-started/reviewing-pull-requests-quickstart.md`
2. `kubernetes/community` — `contributors/guide/expectations.md`
3. `realm/realm-swift` — `CONTRIBUTING.md`

## The two planted defects in this sandbox

| # | Where | Defect | What a reviewer should ask for |
| --- | --- | --- | --- |
| 1 | `src/expenses.py`, `convert_to_usd` | `except KeyError: pass` silently swallows unknown currencies | Raise (or otherwise surface) the error instead of returning `None` |
| 2 | `src/expenses.py`, `total_in_usd` | Raw amounts are summed with no conversion, mixing currencies | Convert each amount to USD via `convert_to_usd` before summing |
