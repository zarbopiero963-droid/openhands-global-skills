---
name: recovery-checkpoint
description: Persist safe, auditable task checkpoints and resume after interruption without duplicate external actions, stale permissions or unbounded retries.
---

# GS-07 — Recovery, checkpoints and idempotency

## Purpose
Enable safe continuation of authorized development work after agent pauses, sandbox termination, timeouts, crashes or model failures. **This skill is documentation and procedure, not a durable scheduler, transactional lock or recovery engine.** Read `GLOBAL_POLICY.md`, `docs/OWNER_APPROVAL.md`, `CERTIFICATION.md`, `skills/atomic-workflow/SKILL.md` and `skills/cost-control/SKILL.md`. Do not infer that OpenHands conversation persistence guarantees sandbox filesystem persistence.

## Invocation and prerequisites
Invoke before long or externally mutating tasks, after each completed atomic card, before an owner decision, and at resume. Confirm exact authorized repository, card, baseline SHA, storage scope, allowed GitHub writes, budget and credentials. Runtime qualification only on `zarbopiero963-droid/cloud-ai-developer-test` after specific authorization. Never inspect Pickfair, MatchPilot, Betfair LIVE or production by inference.

## Persistence model and trust boundaries
- **Conversation events**: useful context, not authoritative action ledger.
- **Workspace filesystem**: may be ephemeral; persistence after sandbox destruction is not assumed.
- **GitHub issue/comment or authorized durable store**: candidate checkpoint destination, only when explicitly approved; a comment is not a transactional lock.
- **External side effects**: source of truth is the external system's current state, not the agent's memory.
- **Secrets**: never write token values, passwords, session headers, production connection strings or unredacted logs to checkpoints.

## Checkpoint schema
```yaml
schema_version: 1
checkpoint_id: <stable unique ID>
task_id: <task ID>
card_id: <GS/LOT ID>
repository: <authorized owner/repo>
branch: <branch>
baseline_head: <SHA>
last_verified_head: <SHA or UNKNOWN>
working_tree_state: CLEAN | DIRTY | UNKNOWN
working_tree_fingerprint: <hash or UNKNOWN>
scope: <approved paths/actions>
owner_approval_ids: []
owner_decisions_pending: []
budget:
  ceiling_usd: <amount or UNKNOWN>
  spent_usd: <amount or UNKNOWN>
  provider_source: <source or UNKNOWN>
actions:
  - action_id: <stable idempotency key>
    kind: <commit/comment/push/PR/test/other>
    target: <resource>
    state: PLANNED | SENT | CONFIRMED | AMBIGUOUS | FAILED
    remote_identifier: <ID/SHA or UNKNOWN>
    evidence: <permalink or redacted log>
findings: []
evidence: []
next_safe_step: <specific step or STOP>
updated_utc: <ISO8601>
```
Do not invent unknown values or report `CONFIRMED` without remote evidence. Hashes are integrity indicators, not proof of semantic correctness.

## Before an external side effect
1. Validate owner authorization, repository scope, cost and credentials.
2. Read current external state and check whether an equivalent action already exists.
3. Allocate stable action ID; write an intent checkpoint to approved durable storage **if authorized and available**.
4. If no durable checkpoint or safe idempotency mechanism exists for a non-idempotent action, stop or request an explicitly approved alternative.
5. Execute only one authorized side effect; record request/response without secrets.
6. Re-read external state and mark `CONFIRMED` only after independently verifying its actual effect.
7. On timeout or ambiguous response, mark `AMBIGUOUS`; do not retry blindly.

## Resume algorithm
1. Load latest **verified** checkpoint from authorized durable storage. If unavailable or corrupt, mark BLOCKED and reconstruct from read-only evidence; never claim automatic recovery.
2. Recheck current owner approvals (scope, target, expiry, one-shot use), repository HEAD, working tree, CI, external resources, quota and budget. A prior approval may no longer be valid.
3. Reconcile each `SENT` or `AMBIGUOUS` action against the external service using IDs/SHA and relevant metadata. If existence cannot be proven or disproven, stop for owner decision.
4. Recompute dependencies and next safe step; invalidate tests/reviews affected by changed HEAD.
5. Resume only within original scope and available budget; no automatic expensive-model escalation or paid retry.
6. Persist reconciliation outcome and record recovery duration and evidence. Do not start a second worker without verified locking.

## Concurrency, leases and idempotency
A GitHub issue label, checkbox or textual `RUNNING` state is not an atomic lease. Require a real compare-and-swap/transactional lock with expiration and fencing for multi-worker operation, and prove that stale workers cannot write after lease loss. If unavailable, allow only one worker and mark multi-worker safety NOT VERIFIED. Exactly-once side effects are not guaranteed by generic retry logic; use service-specific idempotency and reconciliation.

## Failure policy
- **Crash/timeout:** preserve or reconstruct state, do not duplicate external action.
- **HTTP 402 / budget uncertainty:** stop; no paid retry or top-up.
- **Unauthorized repository or production target:** PENDING_OWNER; no access.
- **Checkpoint mismatch/corruption:** BLOCKED, preserve evidence and ask owner.
- **Partial cleanup:** record remaining resources and risk; never delete important resources without owner approval.
- **Unknown sandbox retention:** mark NON VERIFICABILE until tested.

## Atomic oracles — documentation only
| ID | Scenario | Expected oracle |
|---|---|---|
| GS07-T01 | Checkpoint schema with all mandatory fields | Valid, versioned, no invented values |
| GS07-T02 | Secret accidentally included | Rejected/redacted; no secret persisted |
| GS07-T03 | Save checkpoint to authorized durable store | Read-after-write matches exact content |
| GS07-T04 | Sandbox destroyed after checkpoint | Restore from durable store, not local assumptions |
| GS07-T05 | Crash before external action | Safe continuation without duplicate |
| GS07-T06 | Crash after action succeeds but before response | Remote reconciliation, no duplicate |
| GS07-T07 | Timeout on issue comment | AMBIGUOUS; check existing comment before retry |
| GS07-T08 | Remote HEAD changed during pause | Rebaseline, invalidate affected tests |
| GS07-T09 | Owner approval expired | Stop, request new scoped decision |
| GS07-T10 | One-shot approval already consumed | No replay |
| GS07-T11 | Budget exhausted / HTTP 402 | Stop, no top-up or paid retry |
| GS07-T12 | Corrupt or missing checkpoint | BLOCKED, no fabricated recovery |
| GS07-T13 | Two workers race for same task | One verified lock holder or BLOCKED |
| GS07-T14 | Stale worker attempts write after lease loss | Fencing rejects write |
| GS07-T15 | GitHub checkbox claims task lock | Not accepted as concurrency guarantee |
| GS07-T16 | External action exists with different payload | Conflict reported, no overwrite |
| GS07-T17 | Checkpoint contains stale branch/ref | No execution until reconciled |
| GS07-T18 | Local workspace lost but GitHub record exists | Recover metadata; unpersisted files marked LOST |
| GS07-T19 | Retryable read-only GET fails transiently | Bounded retry within approved budget and limits |
| GS07-T20 | Side-effecting POST returns 5xx | Reconcile before any retry |
| GS07-T21 | Partial cleanup after test | Report residual artifacts; no destructive owner-only action |
| GS07-T22 | Restart resumes at next card with pending owner gate | Owner-dependent step remains paused |
| GS07-T23 | No external checkpoint storage authorized | Prepare report; no false persistence claim |
| GS07-T24 | Multi-hour idle with no scheduler | H24 autonomy remains NOT CERTIFIED |

## Evidence and acceptance
Capture exact fixture/ref/SHA, checkpoint revision, before/after state, action ID, remote response and reconciliation, timestamps UTC, sanitized logs, negative cases, cost delta, cleanup and owner acceptance. Separate DOCUMENTED / IMPLEMENTED / TESTED / CERTIFIED. **Current status: DOCUMENTED and published; runtime recovery, persistence, concurrency and H24 behavior NOT CERTIFIED.**
