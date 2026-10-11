# Phase 4 — economic qualification

Verdict: **BLOCKED / account costs NON VERIFICABILE**. Predecessor: a2acf4046767f2006b1d3328352498aad775a452. Observations dated 2026-10-11; no billable model request, recharge or OpenHands runtime creation performed.

## Account evidence

Opening https://openrouter.ai/settings/credits redirects to Sign In. OpenHands displays its login page. No authenticated account read is available. No credentials requested, revealed, changed or imported. Historical balance -$0.19, auto-top-up OFF and $1/day Guardrail are owner-reported historical evidence only.

| Required fact | Current status | Evidence required before admission |
|---|---|---|
| OpenRouter balance and available spend | UNKNOWN | dated masked credits/usage view |
| Associated API key | UNKNOWN | non-secret identifier mapped between OpenHands and OpenRouter |
| Effective guardrail and daily budget | UNKNOWN | assignments, reset boundary and remaining allowance |
| Model/provider allowlists and fallbacks | UNKNOWN | effective eligibility, exact model ID/provider |
| In-flight and unsettled cost | UNKNOWN | request ledger reconciled after completion, no pending requests |
| Cloud account plan/included credits | UNKNOWN | billing/plan page for this account |
| Sandbox duration/resource limits and charge | UNKNOWN | account-specific applicable terms and stop billing behavior |
| Workspace persistence/storage/retention | UNKNOWN | applicable policy and cost, cleanup procedure |
| Charges without OpenRouter calls | UNKNOWN | Cloud infrastructure/storage/analyzer/provider billing terms |

## Official public information, not account verification

Sources consulted 2026-10-11:

- https://www.openhands.dev/pricing : advertises a free Individual tier with BYOK or at-cost provider access, and ten daily conversations. This is not proof of the owner's plan, credits or zero marginal infrastructure/persistence costs. No sandbox billing assumption is admitted from the marketing label.
- https://openrouter.ai/~deepseek/deepseek-flash-latest : alias redirects to the latest family model and has no fixed price. Indexed snippets showed older prices; current opened page supersedes them. “DeepSeek Flash” alone does not identify the account's model.
- https://openrouter.ai/deepseek/deepseek-v4.1-flash : current provider table lists DeepSeek input $0.15/M, output $0.60/M, cache read $0.003/M. Other providers and promotional headline rates differ. This is an illustrative candidate, not the verified configured model or a recommendation to switch.
- https://openrouter.ai/docs/guides/features/guardrails/overview : key/member budgets and model/provider restrictions may overlap. Effective assignment must be checked. A reported $1/day is not a task-specific authorization or proof that one request cannot overshoot available accounting.
- https://openrouter.ai/docs/guides/best-practices/prompt-caching : usage exposes cached_tokens and cache_write_tokens; behavior and rates depend on provider. No cache hit is established for this account.

## Conditional estimate (USD)

Assumptions: illustrative fixed model/provider rates above; input includes repeated context across calls, output includes reasoning when billed; no cache savings credited; no retries. Quantities below are planning assumptions, not measured usage or upper bounds.

| Component | Assumed input tokens | Assumed output tokens | Conditional model cost |
|---|---:|---:|---:|
| Read instructions | 8000 | 500 | 0.001500 |
| Select/read skills | 6000 | 500 | 0.001200 |
| Issue Python command | 6000 | 300 | 0.001080 |
| Analyze output | 8000 | 700 | 0.001620 |
| Final report | 10000 | 1200 | 0.002220 |
| Optional condensation | 20000 | 2000 | 0.004200 |
| Optional LLM security analysis (aggregate) | 12000 | 1000 | 0.002400 |
| Total including optional components | 70000 | 6200 | 0.014220 |

Formula without caching: sum(input_i * rate_input_i + output_i * rate_output_i) / 1,000,000. Condenser and Security Analyzer may use different models/rates and multiple requests; replace their assumptions with actual configuration before admission. Overall cost adds Cloud runtime, storage, other provider charges and any applicable fees. These remain UNKNOWN, so no total maximum is certified. Parallel tools=1 does not prove absence of background model requests.

For cache accounting partition input into ordinary, cache-read and cache-write tokens according to the actual API's semantics (do not double-count writes already included in ordinary input). Apply that endpoint's respective rates. Savings = equivalent uncached cost minus reconciled actual cost; can be negative. Unknown usage or write tariff => UNKNOWN savings. Do not substitute the generic DeepSeek caching ratio for this model/provider's observed tariff. Actual cache-read/write counts and measured savings: NOT OBSERVED.

## Gate and owner evidence

Keep BLOCKED until balance covers an explicit all-component task ceiling, effective model/provider and limits are verified, in-flight requests reconciled, and Cloud charges known or expressly accepted within a ceiling by the owner. Auto-top-up, key, model and Guardrail stay unchanged. Security blockers in phase 3 also remain. No budget amount is authorized by this estimate. No paid probe, alternate key or provider bypass is permitted.
