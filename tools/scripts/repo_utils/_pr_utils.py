# ===================================================================
# tools/scripts/repo_utils/_pr_utils.py
# ===================================================================
"""Shared "gh CLI is usable + caller has enough repo permission",
"is the current branch actually ready to push", and "what's this
PR's actual state" logic used by submit_pr.py, check_pr.py,
approve_pr.py, merge_pr.py, and pr_submit_plugin.py. Kept separate
so those entry points differ only in what they actually do (nothing,
report, approve, merge, or chain submit_pr behind a stricter
pre-flight hook), while the repeated preflight checks stay identical
and get fixed in one place.
"""

import json
import shutil
import subprocess
import sys

# CheckRun conclusions that count as passing. Anything else once a
# check is COMPLETED (FAILURE, CANCELLED, TIMED_OUT, ACTION_REQUIRED,
# STALE) counts as failed.
PASSING_CONCLUSIONS = {"SUCCESS", "NEUTRAL", "SKIPPED"}

# Legacy commit-status (StatusContext) states that mean "still
# running" -- statusCheckRollup can return either CheckRun entries
# (status + conclusion) or older StatusContext entries (state only).
PENDING_STATUS_STATES = {"PENDING"}


def run(cmd, cwd):
  return subprocess.run(
    cmd, cwd=cwd, check=True, text=True, capture_output=True
  )


def check_auth_and_permission(workspace_root, min_permission, tool_name):
  if shutil.which("gh") is None:
    print(
      f"{tool_name}: 'gh' is not on PATH -- install the GitHub CLI "
      "(https://cli.github.com/).",
      file=sys.stderr,
    )
    sys.exit(1)

  try:
    run(["gh", "auth", "status"], workspace_root)
  except subprocess.CalledProcessError as e:
    print(
      f"{tool_name}: not authenticated -- run `gh auth login` first.",
      file=sys.stderr,
    )
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

  try:
    permission = run(
      [
        "gh",
        "repo",
        "view",
        "--json",
        "viewerPermission",
        "-q",
        ".viewerPermission",
      ],
      workspace_root,
    ).stdout.strip()
  except subprocess.CalledProcessError as e:
    print(
      f"{tool_name}: could not determine repo permission.",
      file=sys.stderr,
    )
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

  if permission not in min_permission:
    print(
      f"{tool_name}: insufficient permission ({permission}) -- need "
      f"one of {sorted(min_permission)}.",
      file=sys.stderr,
    )
    sys.exit(1)

  return permission


def get_viewer_login(workspace_root):
  cmd = ["gh", "api", "user", "-q", ".login"]
  return run(cmd, workspace_root).stdout.strip()


def _check_outcome(check):
  """Returns ('pending'|'passed'|'failed', name) for one
  statusCheckRollup entry, handling both the modern CheckRun shape
  (status + conclusion) and the legacy StatusContext shape (state
  only).
  """
  name = check["name"]
  status = check.get("status")
  if status is not None:
    if status != "COMPLETED":
      return "pending", name
    passed = check.get("conclusion") in PASSING_CONCLUSIONS
    return ("passed" if passed else "failed"), name

  state = check.get("state")
  if state in PENDING_STATUS_STATES:
    return "pending", name
  return ("passed" if state == "SUCCESS" else "failed"), name


def fetch_pr_status(workspace_root, pr_number, tool_name):
  """Fetches state/author/reviewDecision/statusCheckRollup for one
  PR and returns it as a dict with the checks pre-categorized into
  pending_checks/passed_checks/failed_checks name lists. Exits (does
  not raise) if the PR can't be looked up at all.
  """
  try:
    pr = run(
      [
        "gh",
        "pr",
        "view",
        str(pr_number),
        "--json",
        "state,author,reviewDecision,statusCheckRollup",
      ],
      workspace_root,
    ).stdout
  except subprocess.CalledProcessError as e:
    print(f"{tool_name}: could not look up PR #{pr_number}.", file=sys.stderr)
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

  data = json.loads(pr)
  outcomes = [_check_outcome(c) for c in data.get("statusCheckRollup", [])]
  data["pending_checks"] = [
    name for outcome, name in outcomes if outcome == "pending"
  ]
  data["passed_checks"] = [
    name for outcome, name in outcomes if outcome == "passed"
  ]
  data["failed_checks"] = [
    name for outcome, name in outcomes if outcome == "failed"
  ]
  return data


def check_clean_branch(workspace_root, base, tool_name):
  """Returns the current branch name after confirming it's not a
  detached HEAD, not the same as `base`, and the working tree is
  clean. Shared by submit_pr.py's own pre-push guard and
  pr_submit_plugin.py's stricter pre-flight hook (which additionally
  checks the local branch tip matches its pushed origin tip -- that
  extra check has no other caller, so it stays local to that hook).
  """
  branch = run(
    ["git", "branch", "--show-current"], workspace_root
  ).stdout.strip()
  if not branch:
    print(
      f"{tool_name}: not on a branch (detached HEAD) -- aborting.",
      file=sys.stderr,
    )
    sys.exit(1)
  if branch == base:
    print(
      f"{tool_name}: current branch is '{branch}', same as base -- "
      "aborting.",
      file=sys.stderr,
    )
    sys.exit(1)

  status = run(["git", "status", "--porcelain"], workspace_root).stdout
  if status.strip():
    print(
      f"{tool_name}: working tree is not clean -- commit or stash "
      "changes first.",
      file=sys.stderr,
    )
    sys.exit(1)

  return branch
