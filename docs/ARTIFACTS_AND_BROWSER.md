# Browser E2E and artifact delivery

## Proven in earlier sandbox audit
Headless Chromium/CDP could capture authentic PNG viewport/full-page and PDF/DevTools trace without Xvfb. A PNG was displayed and downloadable through OpenVSCode on Android; OpenHands inline chat image delivery remained unconfirmed/failed in observed UI. Those observations are not a guarantee for future sandboxes.

## Procedure
Only open approved URL or local data page. Capture screenshot, record UTC, dimensions, byte count, SHA256, source commit and browser version. Save to an authorized workspace artifacts path, never public storage by default. Test preview and authenticated download separately; require user confirmation for Android inline delivery. Keep private URLs and session tokens out of reports.

## Limitations
No Xvfb, standalone Playwright/Selenium, Docker daemon or Windows GUI certified in the observed sandbox. Headless web screenshots are not Windows desktop GUI tests. No upload to GitHub, Telegram or external storage without scoped owner approval.

## Retention
Do not assume workspace survives sandbox deletion. Export evidence before cleanup using authenticated user-approved mechanism. Never put secrets in images or trace files.
