# Phase 5 — definitive one-shot plan and closed admission gate

Status: **DOCUMENTED / static gate IMPLEMENTED; runtime BLOCKED, NOT EXECUTED**.
Predecessor: c69c0a594dfb2bffaa142085513835fef33bd95d. This document is not owner authorization.

## Immutable target and test limitations

Repository: zarbopiero963-droid/cloud-ai-developer-test, branch main, observed HEAD on 2026-10-11: `e4f5149c51cc6b925ff3503e97409d78bf4d12f8`. Branch API reports protected=false; no protection was changed. A technical read-only credential boundary is especially necessary. Source was read, not executed. `tests/test_smoke.py` Git blob: `b3accdfef7dd82f311d925420e1ce1c2f9aabd22`. AGENTS.md blob: `230dd265a1d32ac406a88ea11cd4c0e4885b255c`; CLAUDE.md blob: `8b8704738db7e37c4b4c017c3ee542d475b98467`.

Three unittest methods are present. Two assert checksum values (empty=0, [1,2,3]=6); repeatability compares the same calculation to itself. It does not verify the independent expected value 20 for [12,35,70]. Owner must either accept a narrowly labelled smoke test with this limitation or specifically authorize a separate fixture correction. No target file was changed here, and no three-test PASS is claimed.

## Prerequisites and owner decision

All evidence required in phases 1–4 must be reviewed; relevant security blockers must be closed. Current [admission record](../../fixtures/qualification-admission.json) deliberately contains false/UNKNOWN prerequisites. Proposed session ceiling is 600 seconds, command ceiling 60 seconds; owner must explicitly accept or shorten these. A time ceiling is not a cost ceiling.

Owner decision must identify: authenticated decision ID/channel; this exact repository and HEAD; exact operation below; exact model AND provider for main/analyzer/condenser; all-component maximum USD budget; Cloud price or explicit bounded acceptance; sufficient reconciled balance; one session only; duration; expiry; no writes/installations/production/other repositories; evidence retention; stop and cleanup. No automatic fallback, retries, additional session, recharge or guardrail change. Do not request execution approval while material security evidence is missing.

The local checklist command is safe to run now:

```sh
python3 tools/qualification_gate.py fixtures/qualification-admission.json
```

Exit 3 = BLOCKED, exit 2 = malformed/unreadable input, exit 0 = declarations complete only. It never authorizes execution, authenticates an owner, verifies an account, runs subprocesses, contacts a service or creates a session. Editing JSON booleans cannot satisfy actual evidence requirements. Ten unit test methods exercise denial and malformed/expired/scope-expanded inputs with synthetic data. Positive mock declaration is not a real approval.

## Future execution procedure — DO NOT RUN UNDER THIS MANDATE

1. Human reviewer validates signed/authenticated scoped decision, fresh account ledger, exact current target HEAD, restrictive runtime scopes and pre-provisioned skill bundle hashes. Changes to HEAD/configuration invalidate admission and require review.
2. Start one authorized OpenHands session only after those gates. Record session ID, start UTC, environment/build, stop deadline and billing baseline. No helper sessions or subagents.
3. Read root AGENTS.md, CLAUDE.md and relevant fixture documentation. Capture their paths/hashes and evidence of actual loading. Read already provisioned owner-approval, repository-discovery, atomic-workflow, python-testing and cost-control skills; capture invocation events. Missing policies/bundle => STOP, do not fetch other repos or enable Auto-Load.
4. Read-only baseline: repository identity, `git rev-parse HEAD`, `git status --porcelain`, Python version, inspected test files. Require clean initial state and approved SHA. Do not install dependencies. Set `PYTHONDONTWRITEBYTECODE=1` for the test process; logs go only to explicitly approved ephemeral evidence storage, not tracked repository files.
5. Execute exactly once, with a supervisor timeout of 60 seconds:

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
```

6. Capture full stdout/stderr, exact argv/environment, start/end UTC, exit code, collected test names and PASS/FAIL/ERROR/SKIP counts. Expected acceptance: 3 PASS, 0 FAIL, 0 ERROR, 0 SKIP, exit 0. Fewer/more tests, skip, timeout or mismatch => FAIL/STOP, no repair or retry in this session.
7. Confirm same HEAD and clean status, review action trace for unauthorized reads/writes, production/network calls, installs or extra tasks. No GitHub update from runtime: report is returned to owner. Missing complete action trace => BLOCKED for no-unauthorized-actions claim, even if Python tests pass.
8. Reconcile every model request (including analyzer/condenser) with provider request ID, served model/provider, ordinary/cache-read/cache-write/output/reasoning tokens, actual billed cost, pending/settled state; record Cloud duration/storage charges separately. Missing cost evidence => economics BLOCKED. No prompt cache PASS from generic provider support.
9. Stop the agent and session, verify terminated/idle-billing state using permitted lifecycle operation within approval, retain sanitized evidence with hashes, remove only disposable artifacts specifically authorized. Do not delete persistent workspaces, important data or resources by inference. Confirm cleanup/retention, request no further work, await owner via.

Any unknown charge, scope violation, HTTP 402, unexpected confirmation, stale evidence, unavailable stop control or ambiguity causes immediate STOP/checkpoint. Never restart automatically. In-flight charges must still be reconciled after stopping. A successful smoke result certifies only this narrow observed run, never all 212 oracles, MCP, browser, notifications, caching or H24.

## Required evidence record

Decision ID/reference; target HEAD before/after; file hashes; Python/build/environment; session start/end/ID; exact command; exit code; full output; collected/pass/fail/error/skip; agent action log; loaded instruction paths; actual skills invoked; confirmations; all model request/token/cost records; Cloud charge and settled ledger; no-write evidence; cleanup and final stopped state; owner acceptance. Store unknown values as UNKNOWN, not zero.
