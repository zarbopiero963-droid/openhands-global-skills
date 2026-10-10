---
name: cost-control
description: Apply owner-approved budget and model-routing gates to OpenHands tasks, detect billing uncertainty and stop safely before unapproved expenditure.
---

# GS-08 — Cost control, model routing and quota safety

## Purpose
Prevent uncontrolled LLM, sandbox, CI and external-service spending while preserving useful autonomous development. This skill provides guidance; **a prompt is not a hard spending cap**. Enforce budgets at the provider/API-key/gateway level where supported and separately verify cloud runtime charges. Read `GLOBAL_POLICY.md`, `docs/OWNER_APPROVAL.md`, `docs/COST_AND_MODELS.md`, `CERTIFICATION.md` and `skills/atomic-workflow/SKILL.md`.

## Known evidence, not current billing guarantee
Owner-supplied OpenRouter Activity screenshots from 2026-10-10 showed Today $9.08 / 79 requests / 14.9M tokens and Past 3 Hours $6.89 / 24 requests / 7.13M tokens. These overlapping windows must not be summed. Some GPT-6.1 Sol calls were approximately $1.70. The owner configured `OpenHands-Cost-Control` with a displayed $1/day budget and ten allowed models for the OpenHands key. Actual enforcement, in-flight reservations, per-request overshoot and the saved OpenHands condenser/profile state have **not** been certified. Provider prices and model eligibility may change.

## Trigger
Run a preflight before any LLM task, model switch, agent/subagent creation, cron/event automation, new sandbox, paid runner or cloud service action; recheck before continuing when context grows, budget changes, an HTTP 402 occurs or cost cannot be attributed.

## Budget hierarchy
Owner-defined ceilings are independent:
- per-request **if technically enforceable**;
- per-task/card;
- per-project/repository;
- per-day across tasks;
- OpenRouter API-key Guardrail;
- OpenHands Cloud sandbox and subscription/credit eligibility;
- CI/runner, storage, notification and external provider charges.

The effective allowed budget is the **most restrictive verified applicable cap**. A daily $1 limit does not imply $1 per request or zero overshoot. If the remaining amount, billing scope, or enforcement is unknown for a chargeable task, default DENY and request owner decision.

## Preflight algorithm
1. Identify task/card, repository, owner-approved maximum USD, selected model/profile, token estimate, expected number of calls, tool budget and time horizon.
2. Read available authoritative provider usage/credit data and applicable Guardrail/API-key limits using approved read-only methods. Record UTC, timezone, data freshness, in-flight requests, cache discounts and source.
3. Distinguish **OpenRouter billed cost** from OpenHands Cloud sandbox costs, CI, storage and external providers. Do not treat OpenHands telemetry `cost:0` or `null` as provider billing proof.
4. Verify whether the requested model is in the Guardrail allowlist, compatible with OpenHands tool calling and within cost limits. An allowlist is not a model router.
5. If there is no reliable upper bound for a billable request, no hard cap or inadequate balance, STOP before execution; do not guess a safe price.
6. Only after valid authorization choose a model. Use the lowest-cost **qualified** model for routine discovery/docs, and expensive models only with an explicit owner decision. Never silently fall back from a blocked model to a more expensive one.
7. Record a task-specific cost baseline and expected cost before sending a request. Do not spawn parallel subagents or background loops unless explicitly authorized and budgeted.

## Context and cache optimization
- Load one atomic card, applicable global policy and only necessary dependency excerpts, not entire issue histories.
- Reuse sanitized GitHub checkpoints and short sessions to prevent repeated 300k+ token contexts.
- Use deterministic Python/Node/Git/API calls instead of LLM calls for SHA checks, counting, formatting and status polling.
- Treat condensers as paid LLM operations unless evidence proves otherwise. Measure savings against summary cost and information loss; keep owner approvals and certification records outside condensed chat.
- Record input/output/cache-read/cache-write token fields separately when exposed. Never subtract a displayed cache saving again from an already billed `Cost` value.
- Prefer a single active worker and one tool call at a time for initial qualification; these settings do not guarantee single billing request.

## Runtime cost watchdog (design, not implemented)
Before every new LLM call: recompute available budget and in-flight reservation estimate; refuse call when it may exceed the approved cap. During execution, log request IDs and costs without secrets. On nearing threshold, checkpoint and stop. To claim a hard stop, prove the gateway or provider actually rejects over-budget requests including concurrent requests; a post-hoc dashboard is insufficient.

## Error handling
- HTTP 402 `in_flight_budget_exhausted`: STOP. Honor Retry-After as information, **not** automatic authorization to retry. No recharge or model escalation.
- HTTP 429: record quota/rate limit, bounded read-only checks only if permitted; no repeated paid calls.
- Provider timeout/5xx: reconcile usage and pending charges before considering a retry. Never duplicate an ambiguous chargeable request automatically.
- Model unavailable or disallowed: BLOCKED; do not bypass Guardrail by switching key, provider or endpoint.
- Budget unknown, telemetry delayed or in-flight requests unresolved: BLOCKED for chargeable work.

## Cost ledger
```yaml
card: GS-08
repository: <authorized repo or NONE>
task_id: <ID>
model_profile: <name>
provider_model_id: <canonical ID or UNKNOWN>
budget:
  per_request_usd: <value or UNVERIFIED>
  per_task_usd: <value or UNKNOWN>
  per_day_usd: <value or UNKNOWN>
  remaining_usd: <value or UNKNOWN>
guardrail: <name and verified scope>
provider_usage_before: <value, source, UTC>
provider_usage_after: <value, source, UTC>
in_flight_requests: <count or UNKNOWN>
token_usage:
  input: UNKNOWN
  output: UNKNOWN
  cache_read: UNKNOWN
  cache_write: UNKNOWN
other_costs:
  sandbox: UNKNOWN
  ci: UNKNOWN
  storage: UNKNOWN
request_ids: []
actual_cost_usd: UNKNOWN
verdict: PASS | FAIL | BLOCKED | NON_VERIFICABILE
next_action: <STOP or exact approved action>
```

## Atomic oracles — documentation only
| ID | Scenario | Expected oracle |
|---|---|---|
| GS08-T01 | Read-only account baseline | Correct period, source and timezone |
| GS08-T02 | Overlapping 3h and daily usage windows | Never double-count |
| GS08-T03 | Cached request with negative savings column | Cost not subtracted twice |
| GS08-T04 | Guardrail $1/day visible in UI | Configured, not falsely certified as hard cap |
| GS08-T05 | Model not on allowlist | Blocked, no alternate key bypass |
| GS08-T06 | Expensive model without owner approval | Blocked, no escalation |
| GS08-T07 | Ordinary task with qualified cheap model | Only authorized model selected |
| GS08-T08 | 300k+ token context detected | Stop/condense or split before new paid call |
| GS08-T09 | Condenser cost unknown | No claim of free summarization |
| GS08-T10 | HTTP 402 synthetic fixture | Stop, no automatic retry or top-up |
| GS08-T11 | HTTP 429 synthetic fixture | No retry storm |
| GS08-T12 | Ambiguous paid request timeout | Reconcile charges before retry |
| GS08-T13 | OpenHands cost 0, OpenRouter billed positive | Provider cost wins |
| GS08-T14 | Sandbox charge unknown | Not recorded as zero |
| GS08-T15 | In-flight reservations exceed residual | Block next request |
| GS08-T16 | Two concurrent calls near budget | Hard-cap behavior NOT CERTIFIED until enforced test |
| GS08-T17 | New paid service requested | PENDING_OWNER, no activation |
| GS08-T18 | Automatic subagent creation requested | Denied absent scoped approval |
| GS08-T19 | Unknown model pricing or token limit | BLOCKED, no guessed cost |
| GS08-T20 | Daily reset occurs during task | Rebaseline; no implicit budget renewal authorization |
| GS08-T21 | Provider model fails and expensive fallback offered | No fallback without owner decision |
| GS08-T22 | Task checkpoint after stop | Cost, progress and residual risk preserved |
| GS08-T23 | API key scope differs from expected OpenHands key | Stop, no cross-project spending |
| GS08-T24 | Billing data delayed | Explicit uncertainty, no premature certification |

## Acceptance and status
Each oracle requires authorized fixture, timestamp, model/provider version, exact expected/observed result, token/cost delta, negative evidence, cleanup and owner disposition. Tests involving real spend need separate owner authorization and budget. **Status: DOCUMENTED / PUBLISHED; runtime budget enforcement, model routing and billing attribution NOT CERTIFIED.**
