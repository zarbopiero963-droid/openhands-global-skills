# Phase 1 — baseline reproduction and critical static audit

Verdict: **PASS_WITH_GAPS**. Baseline is exactly `b758d9370c36fa73b364d8016ddfecfd5f63c171`, published as main at acquisition. Initial checkout clean; no later commit is substituted for baseline. This is a fresh critical reproduction in an immutable `git archive`, by the same assistant context, not an independent human or external reviewer certification.

## Reproduced claims

| Claim | New evidence | Result |
|---|---|---|
| 45 local tests | [execution](../../evidence/qualification-20261011/baseline-reproduction.json), [complete output](../../evidence/qualification-20261011/baseline-tests.log) | 45 collected, 45 PASS, 0 FAIL, 0 ERROR, 0 SKIP, exit 0; Python 3.12.14 |
| 212 specifications | [per-oracle audit](../../evidence/qualification-20261011/oracle-review.json) | 200 original + 12 supplemental; 212 unique IDs |
| Original manifest | independent SHA256 of archived files | 64/64 match |
| 31 files final publication | `git diff-tree --no-commit-id --name-only -r b758d937` | 31 changed paths; proves commit content count, not the prior agent's historical readback action |
| Existing static validator | [baseline output](../../evidence/qualification-20261011/baseline-validator.log) | exit 0, 212 records; insufficient by itself for semantic certification |

## Reproduced defects and remediation

[Adversarial reproduction](../../evidence/qualification-20261011/baseline-adversarial.json) was performed on disposable copies, not by altering original oracle expectations.

- QA-01: numeric `procedure=7` and list-valued `expected` wrongly PASS. Add typed schema checks before semantic logic.
- QA-02: string-valued fixture triggers AttributeError instead of a deterministic report. Reject malformed records before traversal.
- QA-03: requirement changed to unrelated text wrongly PASS. Require retention of the exact original expected-oracle clause and reject extra unmapped trace rows. This is a lexical consistency check, not an NLP proof of all semantics.
- QA-04: the 212 fixtures are inert scenario specifications. They are not executable OpenHands adapters. The per-case record explicitly preserves this limitation. Standardized observations can be fabricated if supplied by a dishonest reporter; the comparator cannot authenticate traces.
- QA-05: GS03-T06 / GS07-T13 specify the safe BLOCKED fallback without a lock backend. They do not demonstrate successful lock acquisition or fencing. GS08-C01 supplies the UNKNOWN-evidence path, not a measured provider cache hit. These are runtime subcase gaps, not evidence of a functioning implementation.

No oracle was relaxed. Original 212 assertion records are unchanged. Six adversarial regression tests were added. After retaining the original missing-field diagnostics, the updated suite passes **51 tests**; [execution](../../evidence/qualification-20261011/phase1-execution.json), [log](../../evidence/qualification-20261011/phase1-tests.log). The first remediation run's two diagnostic-compatibility failures are preserved in `remediation-first-run.log`; acceptance assertions were not changed to hide them.

## Documentary/semantic scope

Reviewed all ten source skills and all 212 scenario/assertion pairs, policy, root instructions, guides, traceability, audit supplements, findings and roadmap. Each record has the requested fields; exact expected values are tied to synthetic setup. Common dependencies OWNER_SCOPE, ECONOMIC_GATE, TRACE_CAPTURE are admission gates, not evidence that integrations exist. Detailed platform dependencies are refined in Phase 2 routing.

The prior 212 documentary PASS is reproducible as structural completeness/traceability only. Independent verdict is PASS_WITH_GAPS, not blanket semantic or operational certification. Runtime adaptations, raw trace provenance, current platform behavior and owner acceptance remain blocked.

The optional security-scan skill was read, but its required `scan-prologue.md` reference could not be resolved by the skill provider. No standard skill scan or worker run is claimed; the source audit here is performed directly within the user's mandate, without subagents, production probes or paid tools.
