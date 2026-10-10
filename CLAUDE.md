# CLAUDE.md — OpenHands Global Skills

This file complements [AGENTS.md](AGENTS.md); it does not supersede platform safety rules or owner approvals. The catalog is repository-independent and is not itself a permission grant.

## Operating sequence
1. Verify owner-approved repository and exact task scope.
2. Read AGENTS.md, GLOBAL_POLICY.md and applicable skill files; resolve conflicts conservatively.
3. Choose the smallest set of skills. Work on **one atomic card only**, and stop when a manual 'via' is required.
4. Before any external action, check owner-only categories, least-privilege tool scope, cost and idempotency.
5. Use deterministic tools for discovery and validation; avoid sending large histories to the model.
6. Produce reproducible evidence with commit SHA, oracle, command/tool, UTC, observed result, limitations and costs.
7. Report DOCUMENTED / IMPLEMENTED / TESTED / CERTIFIED independently. Do not declare success from narrative alone.

## Hard stop conditions
Unknown repository authorization; owner-only operation without scoped approval; secrets/production access; unexpected charge; HTTP 402; stale or missing evidence; ambiguous external write; policy conflict; failed safety gate. Stop, checkpoint and request owner decision without bypass or silent retry.

## Budget and caching
Use the approved economical model when qualified; no automatic costly fallback. OpenRouter $1/day Guardrail is reported as configured but runtime enforcement is unverified. Follow docs/COST_AND_MODELS.md and docs/CACHE_STRATEGY.md. Cache only scope-safe immutable data, revalidate mutable state and owner approvals.

## Testing
The only prospective execution test repository is `zarbopiero963-droid/cloud-ai-developer-test` after explicit authorization. Never infer permission to access other projects. Do not activate Auto-Load, H24 automations, MCP bridges, paid services or production connections from these instructions.

## Reporting
For each atomic step include what changed, what was verified, what remains unknown, and the exact owner decision needed. Then wait.
