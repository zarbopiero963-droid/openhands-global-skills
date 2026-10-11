# LLM cost, quota and budget runbook

## Observed problem
OpenHands history reached hundreds of thousands of input tokens per request, with expensive repeated context and several large OpenRouter charges. Avoid assuming zero because OpenHands telemetry shows zero; provider billing is authoritative.

## Current user-reported configuration (not re-verified here)
OpenRouter Guardrail OpenHands-Cost-Control, key OpenHands, $1/day, ten allowlisted models, ZDR enforced, prompt injection Flag, one sensitive-info preset. OpenHands condenser was proposed at 60 events / 40000 tokens; current saved values not independently verified. Do not claim per-request hard cap.

## Before task
Read provider balance, recent spend, active requests, guardrail and applicable budget. Record timestamp, model ID, max cost approved, request and sandbox eligibility. Prefer deterministic tools, scoped prompts, one agent, one tool call at a time, no broad recursive scans.

## During task
Use economical compatible profile for ordinary work; never automatically escalate to expensive models without explicit owner authorization. Cap scope, stop when near budget, avoid redundant context and uncontrolled retries. Summarization itself may cost tokens and may lose context; preserve policy and checkpoints outside conversation history.

## On 402 / budget uncertainty
Stop. No top-up, no fallback to paid model, no automatic retry. Report remaining work, evidence and cost ambiguity.

## After task
Compare OpenRouter actual cost and tokens with pre-run baseline; separately record Cloud sandbox and external service costs. Account for pending/in-flight requests. No inference of zero from absent telemetry.


## Historical evidence correction — 2026-10-11

The master issue's owner-screenshot record names key **OpenHands1** and reports condenser saved at 60 events / 40000 tokens, balance -$0.19 and Auto Top-Up OFF on 2026-10-10. The earlier key shorthand and proposed-setting description above are historical, not fresh account facts. Current balance, in-flight charges, effective guardrail, actual model/provider identity and Cloud eligibility remain UNKNOWN. No authenticated billing inspection or paid call was performed in this mandate. FIN-01 remains BLOCKED.
