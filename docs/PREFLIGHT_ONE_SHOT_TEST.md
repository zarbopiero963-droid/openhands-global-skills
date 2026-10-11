# PREFLIGHT-08 — One-shot OpenHands qualification (PLAN ONLY)

**State: BLOCKED / NOT AUTHORIZED TO EXECUTE.** This is a design document. It does not authorize creating a Cloud sandbox, conversation, automation, provider request, paid resource, or running a test.

## Exact scope
- Repository: `zarbopiero963-droid/cloud-ai-developer-test`, and no other repository.
- Intended test: read `AGENTS.md`, `CLAUDE.md`, `docs/SMOKE_FIXTURE.md`, run one deterministic `unittest` invocation against `tests/test_smoke.py`, report evidence, then STOP for owner decision.
- Planned command, **not executed**: `python -m unittest discover -s tests -p 'test_*.py' -v`.
- Baseline: previously observed commit `e4f5149c51cc6b925ff3503e97409d78bf4d12f8`; re-read remote HEAD immediately before any future test and stop if changed until re-reviewed.
- Do not edit files, create PR/branch, push, merge, deploy, contact production, or follow links to other repositories.
- Marketplace Auto-Load stays OFF; no subagents; concurrency 1.

## Economic hard gates (all required before execution)
1. Owner must approve a **specific maximum total USD for this one test** and decide personally whether to fund OpenRouter. No recharge or purchase by agent.
2. Read current OpenRouter balance, API key scope, Guardrail, current daily usage, pending/in-flight requests and model pricing from authoritative read-only sources. Previous owner screenshot showed **-$0.19** balance and Auto Top-Up OFF; these are historical observations, not a fresh balance.
3. Confirm the configured model is an allowed, working tool-calling profile. No automatic fallback to GPT-6.1 Sol or other costly model.
4. Confirm OpenHands Cloud sandbox access and charges **for this account** independently of OpenRouter. Cloud GET quota is not proof of free sandbox eligibility; previous Lotto A status was NON VERIFICABILE.
5. Establish an enforceable per-test spending ceiling if available; a $1/day Guardrail does not guarantee a $1 single-request ceiling or prevent all in-flight overshoot.
6. If any economic item remains UNKNOWN, **STOP**. Do not attempt a 'free test' to discover whether it costs money.

## Security and environment hard gates
- Verify test repo-only GitHub token permission, no production credentials, no Betfair LIVE/Neon/Render access and no unintended side-effecting tool permissions.
- Check Confirmation Mode ON and current policy, but never treat a prompt confirmation as technical enforcement.
- Verify Python interpreter, available disk, workspace path, expected sandbox lifetime, outbound-network restrictions and log capture before test.
- Prefer local-only test execution with egress technically restricted. If outbound isolation cannot be proven, record limitation and request owner decision rather than claim no network possible.
- Validate that `AGENTS.md` and `CLAUDE.md` are read and respected, not simply present on disk.
- Preserve baseline and approved evidence without secrets. Do not assume sandbox artifact retention after deletion.

## Single execution sequence — only after separate approval
1. Capture UTC and baseline provider costs/credits, in-flight requests, exact repo HEAD and runtime metadata.
2. Open one approved OpenHands session/sandbox **only if economic eligibility and test budget are verified**.
3. Read only the four test repo files and classify owner-only restrictions.
4. Run one `unittest` command with bounded timeout; no installs, network calls, external writes or retries.
5. Record stdout/stderr, exit code, number of collected/passed/failed/skipped tests, Python version, environment, elapsed time and tool trace. Expected 3 PASS / 0 FAIL / 0 ERROR, but do not claim until observed.
6. Check working tree and external action ledger; verify no unauthorized GitHub mutations, production calls or paid side effects.
7. Re-read provider actual billed cost and any Cloud charges, accounting for delayed/in-flight billing.
8. Stop the agent; report DOCUMENTED / IMPLEMENTED / TESTED / CERTIFIED separately. No automatic second task.

## Stop / rollback
Immediate STOP for HTTP 402/429, unexpected spend, missing owner approval, unknown Cloud billing, model escalation, external write, unauthorized repository, secret exposure, HEAD mismatch, test failure or ambiguous response. Cancel a running task if possible; stopping an agent may not reverse an already billed request. No deletion of important resources. Clean only test-created temporary files after verifying their ownership and preserving authorized evidence.

## Evidence and decision record
```yaml
card: PREFLIGHT-08
status: BLOCKED
repository: zarbopiero963-droid/cloud-ai-developer-test
baseline_head: e4f5149c51cc6b925ff3503e97409d78bf4d12f8
owner_test_authorization: MISSING
owner_budget_usd: UNKNOWN
openrouter_balance_current: UNKNOWN
openhands_cloud_billing_eligibility: NON_VERIFICABILE
tool_permissions: NON_VERIFICABILE
runtime_isolation: NON_VERIFICABILE
test_executed: false
expected_tests: 3
observed_tests: NOT_RUN
actual_test_cost: NOT_MEASURED
next_action: STOP_AND_REQUEST_OWNER_DECISION_AFTER_PREFLIGHT
```

## Acceptance
This document is complete as a **proposed one-shot test plan**. It is not a successful economic preflight or runtime certification. Owner sign-off is required for the exact execution and cost ceiling, and separate verification must resolve all blockers.


## Read-only plan completion — 2026-10-11

Qualification remote `main` reread through GitHub: `e4f5149c51cc6b925ff3503e97409d78bf4d12f8`. Four fixture files match the prior blob identities recorded in issue #1. No test executed and no repository write made. Local private clone was unavailable without CLI credentials; existing authorized GitHub connector provided read-only file access. This does not establish a clean remote working tree or sandbox availability.

### Skill selection without cross-repository access

Before a future session, owner must approve and verify the exact preloaded catalog snapshot/skill versions. The running test may read only the qualification repository and that approved installed instruction snapshot; it must not fetch this catalog or any other repository. Auto-Load remains OFF. Expected minimal selection: repository-discovery for baseline, python-testing for the three unittest cases, atomic-workflow for one task and STOP, with owner-approval/cost-control gates applicable. Record selections and rationale from the actual agent trace; marketplace visibility alone does not prove invocation. If the installed snapshot is unavailable, BLOCKED; do not silently enable Auto-Load.

### Exact fixture acceptance and limitation

Expected collected method IDs: `test_empty_input`, `test_known_vector`, `test_repeatability`; expected process exit 0 with 3 tests, 0 failures, 0 errors and 0 skips. Run once with a 60-second caller timeout and `PYTHONDONTWRITEBYTECODE=1`; no dependency installation. The third case compares the function with itself and has no independent arithmetic oracle. It can support only a narrow repeatability observation, not checksum correctness. An owner decision must either authorize replacement with expected value 20 for [12,35,70], or explicitly accept limited smoke scope. No such change is made here.

Before launch, capture baseline allowlisted files/digests, denied network and write instrumentation, interpreter version and provider/Cloud accounting. After run, compare working-tree and tool/network ledgers independently of unittest output. Capture agent stop completion, late/in-flight billing and exact model/provider IDs. Success of 3 tests does not certify scope isolation, cost controls or all global skills. Missing instrumentation is BLOCKED, not PASS. Separate admission steps that can be verified before creating a sandbox from in-sandbox checks; creation itself requires owner budget/Cloud eligibility first.
