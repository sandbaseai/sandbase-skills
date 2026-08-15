# Verified research example: branch protection across Git hosts

**Question:** Do GitHub, GitLab, and Bitbucket Cloud all provide branch protection controls?

**Search date:** 2026-08-15

## Finding

**High confidence:** GitHub, GitLab, and Bitbucket Cloud each document controls that
restrict changes to selected branches. The names and exact capabilities differ:

- GitHub calls them *branch protection rules* and can require reviews or passing status checks.
- GitLab uses *protected branches* to control pushes, merges, deletion, and force pushes.
- Bitbucket Cloud uses *branch permissions* or *branch restrictions* to control write and merge access.

## Evidence ledger

| ID | Independent publisher | Primary source | Relevant evidence |
| --- | --- | --- | --- |
| `s1` | GitHub | [Managing protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches) | Documents branch protection rules, required reviews, and status checks. |
| `s2` | GitLab | [Protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/) | Documents controls for pushing, merging, deletion, review, and force pushes. |
| `s3` | Atlassian | [Use branch permissions](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/) | Documents branch-specific write and merge permissions and restrictions. |

The three sources are independent product publishers. All support the narrow claim,
so the report records three independent sources, no conflict, and high confidence.

## Limits

- The platforms use different names and plan-specific feature boundaries.
- This comparison establishes feature availability, not equivalence between every option.
- Only host web search and page-opening capabilities were available; optional SandBase
  Tavily, Exa, and Scholar coverage was disclosed as unavailable.

## Reproduce the validation

The adjacent [JSON evidence ledger](./verifiable-research-report.json) contains the
machine-checkable result:

```bash
python3 research/multi-source-search/scripts/validate_report.py \
  examples/verifiable-research-report.json
# VALID: 3 source(s), 1 claim(s), 2 provider(s)
```

The validator checks internal consistency offline. It does not claim that any source
is true; readers can open the linked primary documentation and assess it directly.
