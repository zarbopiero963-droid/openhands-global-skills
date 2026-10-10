# GS-08-CACHE — Multilayer caching design and certification plan

**Status: DOCUMENTED / NOT IMPLEMENTED / NOT RUNTIME CERTIFIED.** This is an addendum to [GS-08 Cost Control](../skills/cost-control/SKILL.md). No new LLM calls, service, repository access or paid infrastructure is authorized.

## Goals and invariants
Reduce repeated OpenRouter input, repository reads and redundant computations without sacrificing correctness. A cache hit is never proof that the underlying resource remains current. Owner permissions, budget, security policies, production state, live odds, CI statuses and pending approvals must be revalidated from authoritative sources at each sensitive action.

## Layer 1 — Provider prompt caching
- Determine the **actual** OpenRouter model ID, upstream provider, cache-read/write support, cache retention, prices and routing stability before assuming savings.
- Keep stable system/skill instructions first, volatile task-specific content later; avoid timestamps and changing tool output in reusable prefixes.
- Record prompt_tokens, completion_tokens, cache_read_tokens, cache_write_tokens, request ID, billed cost and UTC as returned by authoritative provider.
- Do not infer a cache hit from identical prompts, or double-subtract savings already reflected in billed cost.
- Different models/providers, changed prompts, or privacy settings may invalidate cache; cross-provider reuse is not assumed.
- Never send secrets just to warm a cache; no paid warm-up without explicit owner authorization.

## Layer 2 — Immutable GitHub content
- Key immutable blobs by repository identity + commit SHA + path + blob SHA; content at a pinned SHA may be reused after integrity verification.
- Mutable refs (main, PR head, issue text, review threads, CI status, branch protection) must be refreshed before any dependent decision.
- Cache negative lookups only briefly, with explicit expiry; absence of AGENTS.md/CLAUDE.md may become stale.
- Never reuse private repository content across another repo or authorization scope.

## Layer 3 — Deterministic results
- Cache pure calculations keyed by code SHA, input digest, dependency lock hash, runtime version, environment and parameters.
- Test results are evidence for the exact recorded environment only; never promote a cached PASS to current-head merge readiness.
- Time-sensitive/live results (odds, production health, credentials, quota) require fresh authoritative reads.

## Layer 4 — Checkpoints and artifacts
- Store sanitized durable checkpoint ID, last verified action, current card, evidence hashes and next safe step in an owner-approved location.
- Reconcile ambiguous writes and revalidate approval, SHA and budget after resume.
- Artifacts need hashes, retention policy, access control and cleanup. Workspace persistence after sandbox deletion is not assumed.

## Layer 5 — Invalidation and security
Invalidate or revalidate on: new commit/branch SHA; file or lockfile changes; instruction/policy changes; model/provider/version changes; tool schema changes; approval expiry/scope changes; changed costs/quotas; failed integrity checks; or security finding. Use explicit versioned cache schema, TTL for mutable metadata and scoped access controls. Never cache raw tokens, API keys, private session headers or unredacted logs.

## Cost model
`net_savings = avoided_billed_calls - cache_write_or_storage_cost - revalidation_cost - summarization_cost`. All terms require measured values; unknown values remain UNKNOWN. Provider cache pricing and hit rates must be measured on an approved bounded test, not assumed.

## Atomic qualification cases
| ID | Case | Expected oracle |
|---|---|---|
| GS08-C01 | Identical stable prompt prefix on compatible model | Measured cache-read tokens or UNKNOWN |
| GS08-C02 | Model/provider switched | No unsupported cross-provider cache claim |
| GS08-C03 | Changed policy or AGENTS.md | Cached context invalidated |
| GS08-C04 | Same immutable blob SHA | Safe reuse after scope/hash check |
| GS08-C05 | Mutable PR head changed | Re-fetch, stale review/test invalidated |
| GS08-C06 | Test environment/lock hash changed | Cached test result not reused as current PASS |
| GS08-C07 | Owner approval expired | Cached approval rejected |
| GS08-C08 | Secret appears in cache candidate | Reject/redact; no persistence |
| GS08-C09 | Cache result corrupted | Hash failure and safe fallback |
| GS08-C10 | Cached live or quota information | Fresh read before action |
| GS08-C11 | Checkpoint after ambiguous write | Reconcile; no duplicate |
| GS08-C12 | Compare cost with and without cache | Provider-billed net savings measured, no double count |

## Evidence and exit gates
For each case record model/provider version, source SHA, scope, key/TTL, expected and observed result, request IDs, input/output/cache token fields, billed cost, storage cost, UTC, evidence and owner acceptance. Pure static checks can be certified separately from provider runtime behavior. No blanket 100% or hard-cost guarantee without execution evidence.
