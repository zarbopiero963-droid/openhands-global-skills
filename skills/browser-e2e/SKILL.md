---
name: browser-e2e
description: Run authorized browser E2E checks with Chromium/CDP, screenshots, PDF, traces, artifact integrity and safe delivery without claiming unsupported GUI or production coverage.
---

# GS-06 — Browser E2E and screenshot evidence

## Purpose and boundaries
Reusable browser-testing procedure for approved local pages or authorized web applications. This skill is guidance, not permission to navigate new private sites, authenticate to production, upload artifacts, install packages, or use paid browser services. Read `GLOBAL_POLICY.md`, `docs/OWNER_APPROVAL.md`, `docs/ARTIFACTS_AND_BROWSER.md` and `CERTIFICATION.md`. The only GitHub repository approved for qualification tests is `zarbopiero963-droid/cloud-ai-developer-test`.

## Trigger
Use for UI regression, headless browser interaction, screenshot/PDF/trace evidence, rendering defects, browser-based integration tests and artifact delivery. Distinguish web browser automation from native desktop automation and Windows GUI testing.

## Phase 1 — Safe preflight
1. Record exact approved target, test objective, allowed domains/origins, authentication policy, cost ceiling, timeouts, environment and repository SHA if applicable.
2. Detect installed browser executable and version, CDP endpoint availability, browser tool support, headless/headed capability, display variables, `/dev/shm`, free disk and artifact location. Recheck each sandbox; do not assume the prior OpenHands image persists.
3. Inspect existing project scripts and dependency manifests without installing Playwright/Selenium/Xvfb automatically. A browser tool integrated into the Agent Server does not prove standalone packages exist in shell Python/Node.
4. Prefer an isolated local HTML/`data:` fixture for initial certification. Block production login, Betfair LIVE, private customer data, paid websites and cross-origin external navigation without explicit owner authorization.
5. Set per-command and per-page timeouts; cap screenshot dimensions and trace size. Disable or constrain external requests for local fixtures and avoid recording secrets.

## Phase 2 — Browser interaction
1. Launch Chromium headless with the available supported tool or local CDP endpoint, using a dedicated temporary profile.
2. Record viewport, device scale factor, URL/origin, browser version and start UTC.
3. Navigate only to approved target; wait for a deterministic DOM condition rather than arbitrary sleeps.
4. Execute documented interactions (click, input, selection, navigation) and assert before/after DOM state. Do not treat successful clicks as proof of business correctness.
5. If a target needs real credentials, writes, purchases or production services, stop and request scoped owner approval. Do not bypass CAPTCHA, authentication or application policy.
6. Capture console errors, failed requests and network restrictions when permitted. Keep HTTP responses and sensitive headers redacted.

## Phase 3 — Evidence capture
- Viewport screenshot: authentic browser PNG with dimensions and SHA-256.
- Full-page screenshot: record dimensions and whether lazy-loaded content was rendered.
- PDF: record valid PDF signature, page count if verifiable and file hash.
- CDP trace: record trace format, timestamp, size, event types and sanitization. CDP trace is **not** a Playwright trace.
- rrweb recording: record event JSON and limitations. rrweb is **not** automatically MP4/WebM.
- Visual assertions: compare with an approved baseline and explicit tolerance; without a baseline or vision proof, do not assert pixel parity or visual comprehension.
- Include exact source commit, environment, browser build, commands, URL allowlist, UTC, expected/observed oracle, findings and artifact path.

## Phase 4 — Artifact delivery and retention
1. Save only authorized evidence to a workspace artifact directory; never put credentials in filenames, metadata, screenshots or logs.
2. Validate PNG signature, dimensions, byte size and SHA-256 **after saving**. A generated in-memory image is not automatically a downloadable artifact.
3. Separately verify: (a) file exists; (b) authenticated file API returns same bytes; (c) OpenVSCode/Files preview works; (d) Android user can download; (e) image appears inline in chat. Do not collapse these into one PASS.
4. A private authenticated File API URL is not a public download link; never embed session keys or create public URLs without owner approval.
5. Record retention policy and export evidence before sandbox cleanup; do not assume a deleted sandbox retains files. Clean only test-created temporary HTML/profiles/processes and preserve approved artifacts until owner confirmation.
6. Uploading to GitHub issue/PR, Telegram, email, cloud storage or another provider requires separate destination authorization and sanitized content.

## Phase 5 — GUI limitations
Headless Chromium/CDP may work without Xvfb. Xvfb is needed only for workflows requiring a Linux display server; it does not emulate Windows. If Xvfb, standalone Playwright/Selenium, drivers, Docker daemon, native Windows GUI or video encoding are unavailable, mark the corresponding coverage BLOCKED/NON VERIFICABILE. Never claim native Windows/Betfair trading tests from web screenshots.

## Output contract
```yaml
card: GS-06
authorized_target: <local fixture or approved URL>
repository_sha: <SHA or NOT_APPLICABLE>
browser_version: <version or UNKNOWN>
mode: HEADLESS | HEADED | UNKNOWN
viewport: <width x height>
test_steps: []
assertions: []
console_findings: []
artifacts:
  - type: PNG | PDF | CDP_TRACE | RRWEB | VIDEO
    path: <workspace path or IN_MEMORY>
    sha256: <hash or UNKNOWN>
    bytes: <integer or UNKNOWN>
    delivery:
      saved: PASS | FAIL | UNKNOWN
      authenticated_download: PASS | FAIL | UNKNOWN
      android_download: PASS | FAIL | UNKNOWN
      inline_chat: PASS | FAIL | UNKNOWN
cost_delta: UNKNOWN
cleanup: <result>
verdict: PASS | FAIL | BLOCKED | NON_VERIFICABILE
evidence_utc: <ISO8601>
```

## Atomic test oracles — documentation only
| ID | Fixture | Expected oracle |
|---|---|---|
| GS06-T01 | Local static HTML | Chromium loads, DOM text asserted |
| GS06-T02 | Local button click | DOM state changes exactly as expected |
| GS06-T03 | Viewport screenshot | Valid PNG, correct dimensions and SHA |
| GS06-T04 | Full-page screenshot | Valid full-page PNG and measured dimensions |
| GS06-T05 | Local PDF generation | Valid PDF bytes and hash |
| GS06-T06 | CDP trace | Valid trace, explicitly not Playwright trace |
| GS06-T07 | rrweb recording | JSON event format, not claimed MP4 |
| GS06-T08 | Saved PNG vs API download | Identical bytes/hash |
| GS06-T09 | Android Files/OpenVSCode | User confirms preview/download |
| GS06-T10 | Inline OpenHands chat image | User confirms visible inline image; otherwise FAIL/BLOCKED |
| GS06-T11 | Private file URL without session | Denied, no public exposure |
| GS06-T12 | External unapproved URL | Block before navigation |
| GS06-T13 | Secret-bearing page | Redaction or no capture; no leaked artifact |
| GS06-T14 | Browser crash or timeout | No false PASS, cleanup attempted |
| GS06-T15 | Missing Xvfb | Headed GUI BLOCKED, headless remains eligible |
| GS06-T16 | Missing standalone Playwright/Selenium | Report gap, no installation |
| GS06-T17 | Windows GUI requirement | Explicit external runner requirement |
| GS06-T18 | Screenshot baseline mismatch | Finding with expected/actual and tolerance |
| GS06-T19 | Missing artifact after sandbox deletion | Retention FAIL/NON VERIFICABILE, no invented persistence |
| GS06-T20 | Unauthorized external artifact upload | No upload; owner approval required |
| GS06-T21 | Large trace exceeds resource budget | Stop/limit capture, preserve partial evidence |
| GS06-T22 | Browser session closes | Verify browser process/CDP endpoint stopped |

## Certification
For every oracle record exact environment, approved target, UTC, browser version, command/tool, expected/observed result, evidence hash, negative cases, cost and cleanup. Previous sandbox audit established Chromium/CDP PNG generation and authenticated download in a particular session, but not this skill's end-to-end execution. **Status: DOCUMENTED and published; GS-06 runtime certification NOT PERFORMED.**
