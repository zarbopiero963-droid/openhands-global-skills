# DOC-01/F04 — Requirements-to-oracles traceability map

**Scope:** static documentary crosswalk only. This does not certify the completeness, executability or correctness of any individual oracle. Canonical oracle descriptions remain in [ORACLE_INDEX.md](ORACLE_INDEX.md) and each linked SKILL.md. 200 identifiers, 10 skill-level requirement families.

## Traceability by requirement family

| Requirement family | Skill | Oracle IDs | Count | Primary guide | Supporting guides | Lots | Status |
|---|---|---|---:|---|---|---|---|
| GS-01: Owner-only authorization and fail-closed decisions | [owner-approval](../skills/owner-approval/SKILL.md) | GS-01-T01…T12 | 12 | [OWNER_APPROVAL.md](OWNER_APPROVAL.md) | [OWNER_APPROVAL.md](OWNER_APPROVAL.md), [ARCHITECTURE.md](ARCHITECTURE.md) | C,D | MAPPED_STATIC_ONLY |
| GS-02: Authorized repository scope and instruction precedence | [repository-discovery](../skills/repository-discovery/SKILL.md) | GS-02-T01…T14 | 14 | [REPOSITORY_GUIDE.md](REPOSITORY_GUIDE.md) | [REPOSITORY_GUIDE.md](REPOSITORY_GUIDE.md), [ARCHITECTURE.md](ARCHITECTURE.md) | C | MAPPED_STATIC_ONLY |
| GS-03: Sequential cards, checkpoint, lock and PR discipline | [atomic-workflow](../skills/atomic-workflow/SKILL.md) | GS-03-T01…T16 | 16 | [TEST_ORACLES.md](TEST_ORACLES.md) | [ROADMAP.md](ROADMAP.md), [ARCHITECTURE.md](ARCHITECTURE.md) | C,D | MAPPED_STATIC_ONLY |
| GS-04: Requirement evidence, current SHA, CI/review/merge gates | [github-certification](../skills/github-certification/SKILL.md) | GS-04-T01…T18 | 18 | [TEST_ORACLES.md](TEST_ORACLES.md) | [REPOSITORY_GUIDE.md](REPOSITORY_GUIDE.md), [ROADMAP.md](ROADMAP.md) | C | MAPPED_STATIC_ONLY |
| GS-05: Reproducible safe tests and regression counts | [python-testing](../skills/python-testing/SKILL.md) | GS-05-T01…T20 | 20 | [TEST_ORACLES.md](TEST_ORACLES.md) | [REPOSITORY_GUIDE.md](REPOSITORY_GUIDE.md) | B,C | MAPPED_STATIC_ONLY |
| GS-06: CDP/browser evidence and artifact delivery | [browser-e2e](../skills/browser-e2e/SKILL.md) | GS-06-T01…T22 | 22 | [ARTIFACTS_AND_BROWSER.md](ARTIFACTS_AND_BROWSER.md) | [ARTIFACTS_AND_BROWSER.md](ARTIFACTS_AND_BROWSER.md), [ROADMAP.md](ROADMAP.md) | B | MAPPED_STATIC_ONLY |
| GS-07: Durable resume, reconciliation, fencing and idempotency | [recovery-checkpoint](../skills/recovery-checkpoint/SKILL.md) | GS-07-T01…T24 | 24 | [ARCHITECTURE.md](ARCHITECTURE.md) | [ROADMAP.md](ROADMAP.md), [TEST_ORACLES.md](TEST_ORACLES.md) | A,D | MAPPED_STATIC_ONLY |
| GS-08: Cost limits, provider billing and model selection | [cost-control](../skills/cost-control/SKILL.md) | GS-08-T01…T24 | 24 | [COST_AND_MODELS.md](COST_AND_MODELS.md) | [ROADMAP.md](ROADMAP.md), [ARCHITECTURE.md](ARCHITECTURE.md) | A,B,C,D | MAPPED_STATIC_ONLY |
| GS-09: MCP discovery, scoped tool calls and bridge limits | [mcp-orchestration](../skills/mcp-orchestration/SKILL.md) | GS-09-T01…T24 | 24 | [MCP_AND_NOTIFICATIONS.md](MCP_AND_NOTIFICATIONS.md) | [ARCHITECTURE.md](ARCHITECTURE.md), [ROADMAP.md](ROADMAP.md) | D | MAPPED_STATIC_ONLY |
| GS-10: Owner notification and approval lifecycle | [owner-notifications](../skills/owner-notifications/SKILL.md) | GS-10-T01…T26 | 26 | [MCP_AND_NOTIFICATIONS.md](MCP_AND_NOTIFICATIONS.md) | [OWNER_APPROVAL.md](OWNER_APPROVAL.md), [ROADMAP.md](ROADMAP.md) | D | MAPPED_STATIC_ONLY |

## Traceability rule
Each `GSxx-Tyy` inherits its skill's **requirement family**, but that is only a provisional link. Before a test can be marked CERTIFIED, create a per-oracle record with: stable requirement ID and exact normative clause (document/heading/permalink), authorized fixture, steps, measurable expected result, observed evidence, negative/positive classification, dependency, owner gate, runtime version, cost delta and reviewer acceptance. Absence of any mandatory field means NOT_CERTIFIED.

## Known gaps
1. **F04-G01:** no unique normative requirement ID and clause link per individual oracle (200/200 need semantic review).
2. **F04-G02:** no executable fixture and exact procedure for every oracle (200/200 need test-design review).
3. **F04-G03:** some guides provide only high-level rules, not enforceable controls; technical permission and budget enforcement remain unproven.
4. **F04-G04:** current runtime model profiles, OpenHands settings and per-key billing protection have not been independently verified.
5. **F04-G05:** cross-skill overlap (owner approval, cost, recovery, notifications) needs semantic deduplication while retaining distinct test IDs.

## Acceptance of this document
- [x] Every skill mapped to a named requirement family and guide.
- [x] Oracle ranges and count sum to 200.
- [ ] Per-oracle clause-level semantic trace completed.
- [ ] Executable test fixtures and evidence complete.
- [ ] Independent semantic review and owner acceptance.

**Verdict:** PASS for the skill-family mapping only; per-oracle semantic coverage NON VERIFICABILE. No OpenHands run or paid API request performed.


## Current individual traceability — 2026-10-11

Explicit correction: the historical family ranges written as GS-01-T01 etc. use a noncanonical hyphen. Canonical IDs are GS01-T01 etc.; no IDs are renamed. Historical findings F04-G01/G02 receive the documentary disposition in [FINDINGS](FINDINGS.md). The following 212 rows supersede the historical family-only coverage limitation for **specification completeness**, not execution. Each REQ ID is a normative refinement of its exact original oracle; this is not a claim to have counted every prose clause in the repository.

| Requirement | Oracle | Full record group | Source | Detailed audit |
|---|---|---|---|---|
| REQ-GS01-T01 | GS01-T01 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t01) |
| REQ-GS01-T02 | GS01-T02 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t02) |
| REQ-GS01-T03 | GS01-T03 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t03) |
| REQ-GS01-T04 | GS01-T04 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t04) |
| REQ-GS01-T05 | GS01-T05 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t05) |
| REQ-GS01-T06 | GS01-T06 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t06) |
| REQ-GS01-T07 | GS01-T07 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t07) |
| REQ-GS01-T08 | GS01-T08 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t08) |
| REQ-GS01-T09 | GS01-T09 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t09) |
| REQ-GS01-T10 | GS01-T10 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t10) |
| REQ-GS01-T11 | GS01-T11 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t11) |
| REQ-GS01-T12 | GS01-T12 | [JSON](../fixtures/oracles/GS01.json) | [skills/owner-approval/SKILL.md](../skills/owner-approval/SKILL.md) | [Procedure](audits/GS01.md#gs01-t12) |
| REQ-GS02-T01 | GS02-T01 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t01) |
| REQ-GS02-T02 | GS02-T02 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t02) |
| REQ-GS02-T03 | GS02-T03 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t03) |
| REQ-GS02-T04 | GS02-T04 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t04) |
| REQ-GS02-T05 | GS02-T05 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t05) |
| REQ-GS02-T06 | GS02-T06 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t06) |
| REQ-GS02-T07 | GS02-T07 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t07) |
| REQ-GS02-T08 | GS02-T08 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t08) |
| REQ-GS02-T09 | GS02-T09 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t09) |
| REQ-GS02-T10 | GS02-T10 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t10) |
| REQ-GS02-T11 | GS02-T11 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t11) |
| REQ-GS02-T12 | GS02-T12 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t12) |
| REQ-GS02-T13 | GS02-T13 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t13) |
| REQ-GS02-T14 | GS02-T14 | [JSON](../fixtures/oracles/GS02.json) | [skills/repository-discovery/SKILL.md](../skills/repository-discovery/SKILL.md) | [Procedure](audits/GS02.md#gs02-t14) |
| REQ-GS03-T01 | GS03-T01 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t01) |
| REQ-GS03-T02 | GS03-T02 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t02) |
| REQ-GS03-T03 | GS03-T03 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t03) |
| REQ-GS03-T04 | GS03-T04 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t04) |
| REQ-GS03-T05 | GS03-T05 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t05) |
| REQ-GS03-T06 | GS03-T06 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t06) |
| REQ-GS03-T07 | GS03-T07 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t07) |
| REQ-GS03-T08 | GS03-T08 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t08) |
| REQ-GS03-T09 | GS03-T09 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t09) |
| REQ-GS03-T10 | GS03-T10 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t10) |
| REQ-GS03-T11 | GS03-T11 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t11) |
| REQ-GS03-T12 | GS03-T12 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t12) |
| REQ-GS03-T13 | GS03-T13 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t13) |
| REQ-GS03-T14 | GS03-T14 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t14) |
| REQ-GS03-T15 | GS03-T15 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t15) |
| REQ-GS03-T16 | GS03-T16 | [JSON](../fixtures/oracles/GS03.json) | [skills/atomic-workflow/SKILL.md](../skills/atomic-workflow/SKILL.md) | [Procedure](audits/GS03.md#gs03-t16) |
| REQ-GS04-T01 | GS04-T01 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t01) |
| REQ-GS04-T02 | GS04-T02 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t02) |
| REQ-GS04-T03 | GS04-T03 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t03) |
| REQ-GS04-T04 | GS04-T04 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t04) |
| REQ-GS04-T05 | GS04-T05 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t05) |
| REQ-GS04-T06 | GS04-T06 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t06) |
| REQ-GS04-T07 | GS04-T07 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t07) |
| REQ-GS04-T08 | GS04-T08 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t08) |
| REQ-GS04-T09 | GS04-T09 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t09) |
| REQ-GS04-T10 | GS04-T10 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t10) |
| REQ-GS04-T11 | GS04-T11 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t11) |
| REQ-GS04-T12 | GS04-T12 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t12) |
| REQ-GS04-T13 | GS04-T13 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t13) |
| REQ-GS04-T14 | GS04-T14 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t14) |
| REQ-GS04-T15 | GS04-T15 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t15) |
| REQ-GS04-T16 | GS04-T16 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t16) |
| REQ-GS04-T17 | GS04-T17 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t17) |
| REQ-GS04-T18 | GS04-T18 | [JSON](../fixtures/oracles/GS04.json) | [skills/github-certification/SKILL.md](../skills/github-certification/SKILL.md) | [Procedure](audits/GS04.md#gs04-t18) |
| REQ-GS05-T01 | GS05-T01 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t01) |
| REQ-GS05-T02 | GS05-T02 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t02) |
| REQ-GS05-T03 | GS05-T03 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t03) |
| REQ-GS05-T04 | GS05-T04 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t04) |
| REQ-GS05-T05 | GS05-T05 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t05) |
| REQ-GS05-T06 | GS05-T06 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t06) |
| REQ-GS05-T07 | GS05-T07 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t07) |
| REQ-GS05-T08 | GS05-T08 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t08) |
| REQ-GS05-T09 | GS05-T09 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t09) |
| REQ-GS05-T10 | GS05-T10 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t10) |
| REQ-GS05-T11 | GS05-T11 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t11) |
| REQ-GS05-T12 | GS05-T12 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t12) |
| REQ-GS05-T13 | GS05-T13 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t13) |
| REQ-GS05-T14 | GS05-T14 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t14) |
| REQ-GS05-T15 | GS05-T15 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t15) |
| REQ-GS05-T16 | GS05-T16 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t16) |
| REQ-GS05-T17 | GS05-T17 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t17) |
| REQ-GS05-T18 | GS05-T18 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t18) |
| REQ-GS05-T19 | GS05-T19 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t19) |
| REQ-GS05-T20 | GS05-T20 | [JSON](../fixtures/oracles/GS05.json) | [skills/python-testing/SKILL.md](../skills/python-testing/SKILL.md) | [Procedure](audits/GS05.md#gs05-t20) |
| REQ-GS06-T01 | GS06-T01 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t01) |
| REQ-GS06-T02 | GS06-T02 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t02) |
| REQ-GS06-T03 | GS06-T03 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t03) |
| REQ-GS06-T04 | GS06-T04 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t04) |
| REQ-GS06-T05 | GS06-T05 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t05) |
| REQ-GS06-T06 | GS06-T06 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t06) |
| REQ-GS06-T07 | GS06-T07 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t07) |
| REQ-GS06-T08 | GS06-T08 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t08) |
| REQ-GS06-T09 | GS06-T09 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t09) |
| REQ-GS06-T10 | GS06-T10 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t10) |
| REQ-GS06-T11 | GS06-T11 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t11) |
| REQ-GS06-T12 | GS06-T12 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t12) |
| REQ-GS06-T13 | GS06-T13 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t13) |
| REQ-GS06-T14 | GS06-T14 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t14) |
| REQ-GS06-T15 | GS06-T15 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t15) |
| REQ-GS06-T16 | GS06-T16 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t16) |
| REQ-GS06-T17 | GS06-T17 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t17) |
| REQ-GS06-T18 | GS06-T18 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t18) |
| REQ-GS06-T19 | GS06-T19 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t19) |
| REQ-GS06-T20 | GS06-T20 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t20) |
| REQ-GS06-T21 | GS06-T21 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t21) |
| REQ-GS06-T22 | GS06-T22 | [JSON](../fixtures/oracles/GS06.json) | [skills/browser-e2e/SKILL.md](../skills/browser-e2e/SKILL.md) | [Procedure](audits/GS06.md#gs06-t22) |
| REQ-GS07-T01 | GS07-T01 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t01) |
| REQ-GS07-T02 | GS07-T02 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t02) |
| REQ-GS07-T03 | GS07-T03 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t03) |
| REQ-GS07-T04 | GS07-T04 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t04) |
| REQ-GS07-T05 | GS07-T05 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t05) |
| REQ-GS07-T06 | GS07-T06 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t06) |
| REQ-GS07-T07 | GS07-T07 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t07) |
| REQ-GS07-T08 | GS07-T08 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t08) |
| REQ-GS07-T09 | GS07-T09 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t09) |
| REQ-GS07-T10 | GS07-T10 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t10) |
| REQ-GS07-T11 | GS07-T11 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t11) |
| REQ-GS07-T12 | GS07-T12 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t12) |
| REQ-GS07-T13 | GS07-T13 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t13) |
| REQ-GS07-T14 | GS07-T14 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t14) |
| REQ-GS07-T15 | GS07-T15 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t15) |
| REQ-GS07-T16 | GS07-T16 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t16) |
| REQ-GS07-T17 | GS07-T17 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t17) |
| REQ-GS07-T18 | GS07-T18 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t18) |
| REQ-GS07-T19 | GS07-T19 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t19) |
| REQ-GS07-T20 | GS07-T20 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t20) |
| REQ-GS07-T21 | GS07-T21 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t21) |
| REQ-GS07-T22 | GS07-T22 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t22) |
| REQ-GS07-T23 | GS07-T23 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t23) |
| REQ-GS07-T24 | GS07-T24 | [JSON](../fixtures/oracles/GS07.json) | [skills/recovery-checkpoint/SKILL.md](../skills/recovery-checkpoint/SKILL.md) | [Procedure](audits/GS07.md#gs07-t24) |
| REQ-GS08-C01 | GS08-C01 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c01) |
| REQ-GS08-C02 | GS08-C02 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c02) |
| REQ-GS08-C03 | GS08-C03 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c03) |
| REQ-GS08-C04 | GS08-C04 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c04) |
| REQ-GS08-C05 | GS08-C05 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c05) |
| REQ-GS08-C06 | GS08-C06 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c06) |
| REQ-GS08-C07 | GS08-C07 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c07) |
| REQ-GS08-C08 | GS08-C08 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c08) |
| REQ-GS08-C09 | GS08-C09 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c09) |
| REQ-GS08-C10 | GS08-C10 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c10) |
| REQ-GS08-C11 | GS08-C11 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c11) |
| REQ-GS08-C12 | GS08-C12 | [JSON](../fixtures/oracles/GS08-CACHE.json) | [docs/CACHE_STRATEGY.md](../docs/CACHE_STRATEGY.md) | [Procedure](audits/GS08-CACHE.md#gs08-c12) |
| REQ-GS08-T01 | GS08-T01 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t01) |
| REQ-GS08-T02 | GS08-T02 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t02) |
| REQ-GS08-T03 | GS08-T03 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t03) |
| REQ-GS08-T04 | GS08-T04 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t04) |
| REQ-GS08-T05 | GS08-T05 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t05) |
| REQ-GS08-T06 | GS08-T06 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t06) |
| REQ-GS08-T07 | GS08-T07 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t07) |
| REQ-GS08-T08 | GS08-T08 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t08) |
| REQ-GS08-T09 | GS08-T09 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t09) |
| REQ-GS08-T10 | GS08-T10 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t10) |
| REQ-GS08-T11 | GS08-T11 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t11) |
| REQ-GS08-T12 | GS08-T12 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t12) |
| REQ-GS08-T13 | GS08-T13 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t13) |
| REQ-GS08-T14 | GS08-T14 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t14) |
| REQ-GS08-T15 | GS08-T15 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t15) |
| REQ-GS08-T16 | GS08-T16 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t16) |
| REQ-GS08-T17 | GS08-T17 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t17) |
| REQ-GS08-T18 | GS08-T18 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t18) |
| REQ-GS08-T19 | GS08-T19 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t19) |
| REQ-GS08-T20 | GS08-T20 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t20) |
| REQ-GS08-T21 | GS08-T21 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t21) |
| REQ-GS08-T22 | GS08-T22 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t22) |
| REQ-GS08-T23 | GS08-T23 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t23) |
| REQ-GS08-T24 | GS08-T24 | [JSON](../fixtures/oracles/GS08.json) | [skills/cost-control/SKILL.md](../skills/cost-control/SKILL.md) | [Procedure](audits/GS08.md#gs08-t24) |
| REQ-GS09-T01 | GS09-T01 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t01) |
| REQ-GS09-T02 | GS09-T02 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t02) |
| REQ-GS09-T03 | GS09-T03 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t03) |
| REQ-GS09-T04 | GS09-T04 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t04) |
| REQ-GS09-T05 | GS09-T05 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t05) |
| REQ-GS09-T06 | GS09-T06 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t06) |
| REQ-GS09-T07 | GS09-T07 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t07) |
| REQ-GS09-T08 | GS09-T08 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t08) |
| REQ-GS09-T09 | GS09-T09 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t09) |
| REQ-GS09-T10 | GS09-T10 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t10) |
| REQ-GS09-T11 | GS09-T11 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t11) |
| REQ-GS09-T12 | GS09-T12 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t12) |
| REQ-GS09-T13 | GS09-T13 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t13) |
| REQ-GS09-T14 | GS09-T14 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t14) |
| REQ-GS09-T15 | GS09-T15 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t15) |
| REQ-GS09-T16 | GS09-T16 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t16) |
| REQ-GS09-T17 | GS09-T17 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t17) |
| REQ-GS09-T18 | GS09-T18 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t18) |
| REQ-GS09-T19 | GS09-T19 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t19) |
| REQ-GS09-T20 | GS09-T20 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t20) |
| REQ-GS09-T21 | GS09-T21 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t21) |
| REQ-GS09-T22 | GS09-T22 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t22) |
| REQ-GS09-T23 | GS09-T23 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t23) |
| REQ-GS09-T24 | GS09-T24 | [JSON](../fixtures/oracles/GS09.json) | [skills/mcp-orchestration/SKILL.md](../skills/mcp-orchestration/SKILL.md) | [Procedure](audits/GS09.md#gs09-t24) |
| REQ-GS10-T01 | GS10-T01 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t01) |
| REQ-GS10-T02 | GS10-T02 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t02) |
| REQ-GS10-T03 | GS10-T03 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t03) |
| REQ-GS10-T04 | GS10-T04 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t04) |
| REQ-GS10-T05 | GS10-T05 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t05) |
| REQ-GS10-T06 | GS10-T06 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t06) |
| REQ-GS10-T07 | GS10-T07 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t07) |
| REQ-GS10-T08 | GS10-T08 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t08) |
| REQ-GS10-T09 | GS10-T09 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t09) |
| REQ-GS10-T10 | GS10-T10 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t10) |
| REQ-GS10-T11 | GS10-T11 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t11) |
| REQ-GS10-T12 | GS10-T12 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t12) |
| REQ-GS10-T13 | GS10-T13 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t13) |
| REQ-GS10-T14 | GS10-T14 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t14) |
| REQ-GS10-T15 | GS10-T15 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t15) |
| REQ-GS10-T16 | GS10-T16 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t16) |
| REQ-GS10-T17 | GS10-T17 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t17) |
| REQ-GS10-T18 | GS10-T18 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t18) |
| REQ-GS10-T19 | GS10-T19 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t19) |
| REQ-GS10-T20 | GS10-T20 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t20) |
| REQ-GS10-T21 | GS10-T21 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t21) |
| REQ-GS10-T22 | GS10-T22 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t22) |
| REQ-GS10-T23 | GS10-T23 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t23) |
| REQ-GS10-T24 | GS10-T24 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t24) |
| REQ-GS10-T25 | GS10-T25 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t25) |
| REQ-GS10-T26 | GS10-T26 | [JSON](../fixtures/oracles/GS10.json) | [skills/owner-notifications/SKILL.md](../skills/owner-notifications/SKILL.md) | [Procedure](audits/GS10.md#gs10-t26) |
