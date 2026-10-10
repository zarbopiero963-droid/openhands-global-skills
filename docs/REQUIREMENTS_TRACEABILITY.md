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
