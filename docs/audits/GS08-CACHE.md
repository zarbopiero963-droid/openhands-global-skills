# GS08-CACHE — supplemental individual specifications

[Shared protocol](PROTOCOL.md). [Full records](../../fixtures/oracles/GS08-CACHE.json). Twelve cases, separate from 200 original IDs. Pure reference checks do not implement OpenRouter caching.

## GS08-C01

REQ-GS08-C01: For Identical stable prompt prefix on compatible model, MUST satisfy Measured cache-read tokens or UNKNOWN. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 1, row GS08-C01.

Setup: Same prompt twice; actual provider/model support and usage absent.

Procedure: Inspect required provider usage fields; unknown data cannot establish hit.

Assertions: `{"status": "UNKNOWN", "cache_hit_claim": false}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C02

REQ-GS08-C02: For Model/provider switched, MUST satisfy No unsupported cross-provider cache claim. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 1, row GS08-C02.

Setup: Candidate model/provider M1/P1; next request M2/P2.

Procedure: Invalidate prefix eligibility and obtain new support evidence; do not reuse P1 hit claim.

Assertions: `{"cross_provider_hit_claim": false, "support_revalidation_required": true}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C03

REQ-GS08-C03: For Changed policy or AGENTS.md, MUST satisfy Cached context invalidated. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 5, row GS08-C03.

Setup: Candidate policy_sha=A; current policy_sha=B.

Procedure: Compare policy/instruction revision in each cache key.

Assertions: `{"reuse": false, "reason": "KEY_MISMATCH:policy_sha"}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C04

REQ-GS08-C04: For Same immutable blob SHA, MUST satisfy Safe reuse after scope/hash check. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 2, row GS08-C04.

Setup: Same github_blob repository/scope/commit/path/blob digest and clean payload; second variant same bytes but repo-B.

Procedure: Check integrity and exact key; deny cross-repository variant.

Assertions: `{"same_scope_reuse": true, "cross_repo_reuse": false}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C05

REQ-GS08-C05: For Mutable PR head changed, MUST satisfy Re-fetch, stale review/test invalidated. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 2, row GS08-C05.

Setup: Mutable branch/PR head candidate A; live ref B.

Procedure: Require fresh read and invalidate stale review/test readiness.

Assertions: `{"reuse": false, "reason": "FRESH_READ_REQUIRED"}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C06

REQ-GS08-C06: For Test environment/lock hash changed, MUST satisfy Cached test result not reused as current PASS. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 3, row GS08-C06.

Setup: Deterministic result lock_sha=A versus current B; repeat runtime version change.

Procedure: Reject either changed environment key; never promote cached test to current head.

Assertions: `{"changed_lock_reuse": false, "changed_runtime_reuse": false}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C07

REQ-GS08-C07: For Owner approval expired, MUST satisfy Cached approval rejected. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 5, row GS08-C07.

Setup: Cached approval expired; current approval_valid=false.

Procedure: Reject approval cache unconditionally; revalidate owner channel.

Assertions: `{"reuse": false, "reason": "FRESH_READ_REQUIRED"}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C08

REQ-GS08-C08: For Secret appears in cache candidate, MUST satisfy Reject/redact; no persistence. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 5, row GS08-C08.

Setup: Cache candidate flagged secret_scan=FOUND; payload sentinel only.

Procedure: Reject before persistence; no real secret used.

Assertions: `{"reuse": false, "reason": "SECRET_OR_UNSCANNED"}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C09

REQ-GS08-C09: For Cache result corrupted, MUST satisfy Hash failure and safe fallback. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 5, row GS08-C09.

Setup: Payload bytes differ from stored SHA256.

Procedure: Recompute digest and reject corrupt entry; report safe re-fetch need without doing network I/O.

Assertions: `{"reuse": false, "reason": "INTEGRITY_FAILURE"}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C10

REQ-GS08-C10: For Cached live or quota information, MUST satisfy Fresh read before action. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 3, row GS08-C10.

Setup: Cache kind live or quota with unexpired TTL.

Procedure: Require authoritative fresh read despite TTL and reject reuse.

Assertions: `{"live_reuse": false, "quota_reuse": false}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C11

REQ-GS08-C11: For Checkpoint after ambiguous write, MUST satisfy Reconcile; no duplicate. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Layer 4, row GS08-C11.

Setup: Checkpoint ambiguous_actions=1,reconciled=false; separate resolved variant count=0,reconciled=true.

Procedure: Reject unresolved resume; accept metadata only after matching key/integrity and reconciliation. No action replay.

Assertions: `{"ambiguous_reuse": false, "reconciled_reuse": true, "replayed_actions": 0}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

## GS08-C12

REQ-GS08-C12: For Compare cost with and without cache, MUST satisfy Provider-billed net savings measured, no double count. Unknown provider evidence must block a cache-hit certification.

Source: [CACHE_STRATEGY](../CACHE_STRATEGY.md), Cost model, row GS08-C12.

Setup: Equivalent disjoint finalized workloads: uncached billed 1.00, cached billed 0.40 including cache-write, storage 0.05, revalidation 0.05, summarization 0.10.

Procedure: Compute net once from billed totals; preserve separate read/write token fields; omit field to verify UNKNOWN.

Assertions: `{"net_savings_usd": "0.40", "missing_cost_status": "UNKNOWN", "cache_write_double_subtracted": false}`. Runtime BLOCKED; requirements for evidence/cleanup/budget/approval are in the full record.

