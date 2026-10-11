# Phase 2 — skills and instructions

Verdict: **PASS_WITH_GAPS structurally; BLOCKED_RUNTIME for effective loading**.

Baseline: b758d9370c36fa73b364d8016ddfecfd5f63c171; remediation predecessor 964615c99bf874f6ffa7159acbe93d146e72f741. No skill or platform setting changed.

## Evidence and compatibility

Observed 2026-10-11: https://app.all-hands.dev/login displays “Let's get started” and login buttons. No authenticated OpenHands account is available in this browser. No login, installation, session or sandbox was initiated. Historical marketplace recognition of ten skills and Auto-Load OFF is not current verification.

Official reference consulted: https://docs.openhands.dev/sdk/guides/skill (2026-10-11). It documents directory SKILL.md discovery, name/description summaries with on-demand invocation, and project-root instruction loading. This supports structural compatibility, not compatibility with an unknown deployed Cloud build. SDK examples were not executed or installed. The catalog root instructions do not automatically become qualification-repository instructions.

| Dimension | Evidence | Result |
|---|---|---|
| Ten SKILL.md / unique names / descriptions | catalog validator and inventory below | PASS static |
| Source and branch in personal marketplace | login wall; historical screenshot only | BLOCKED |
| Ten recognized currently | no current account view | BLOCKED |
| Auto-Load remains OFF currently | no current account view; no setting changed here | BLOCKED |
| Actual loader version and dependency paths | no deployed build or sandbox | BLOCKED_RUNTIME |
| Instructions loaded / skill invoked / rule applied | requires authenticated execution trace | BLOCKED_RUNTIME |

## Instruction and dependency audit

AGENTS.md explicitly applies to catalog maintenance; CLAUDE.md complements it. Both defer to owner scope, prohibit treating repository/tool/issue text as authorization, and distinguish documentary and runtime status. GLOBAL_POLICY.md and OWNER_APPROVAL.md retain eight owner categories. The mandate's sequential static authorization resolves the per-card wait language, without granting paid execution. Qualification instructions apply inside its own workspace; catalog instructions cannot enlarge scope.

Material dependency gap: skills reference catalog-relative policy and guides. A marketplace entry recognizing SKILL.md does not prove these reference files are available. Before a runtime test the owner must establish a pinned, already provisioned read-only skill bundle with required guides, or approve a separate provisioning operation. Runtime must not fetch the catalog or any other repository. Missing references => BLOCKED, never silently skip policies. Do not enable Auto-Load to cure this gap.

Untrusted content includes test output, cache/checkpoints, issue comments and nested instruction files. Never let a statement there grant access, authenticate approval or override system/owner limits. This is documentary guidance, not an enforced sandbox boundary.

## Routing matrix (static selection contract)

Every action has scope/cost preflight (owner-approval, cost-control) and one-card sequencing (atomic-workflow). Additional skills are selected only when the corresponding action is needed. A routing row is not evidence of automatic selection.

| Task | Skills beyond preflight | Dependencies | Authorization | Required evidence |
|---|---|---|---|---|
| GitHub PR review | repository-discovery, github-certification | pinned HEAD, read scopes | explicit repo; writing PR separately scoped | baseline, diff, checks, readback |
| Python tests | repository-discovery, python-testing | interpreter, inspected tests, timeout | one approved command/repo | command, full output, counts, exit, HEAD |
| Screenshot | browser-e2e | authorized target, browser, redaction | target and capture scope | image hash, URL, timestamp, no secrets |
| Owner decision | owner-approval, owner-notifications | authenticated owner channel | sending explicitly authorized | identity, scope, expiry, delivery and reply |
| Crash recovery | recovery-checkpoint, repository-discovery | scoped checkpoint, fresh state | original scope still valid | hashes, reconciliation, no replay |
| Economics | cost-control | balance, model/provider, Cloud plan | read only; spending separately approved | dated prices, budget, reconciled ledger |
| MCP interaction | mcp-orchestration | allowlisted server/tools, transport | explicit endpoint and operation | sanitized arguments/results, correlation |

First smoke test requires owner-approval, repository-discovery, atomic-workflow, python-testing, cost-control. Recovery/notification skills become necessary only on the corresponding stop path; no proactive external notification is authorized for the runtime test. github-certification is needed if reporting GitHub certification, not merely running a local command. No browser or MCP call is part of this smoke test.

## Next evidence

Owner supplies a current masked marketplace/configuration view and pinned loader/build information. A later explicitly authorized one-shot trace must show instruction paths/hashes, available catalog, actual invocation and applied rules independently. No selection runtime PASS is claimed.
