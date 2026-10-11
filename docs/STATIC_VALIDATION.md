# Offline static verification

Run from catalog root with Python 3.10+ standard library, no dependencies or network:

```bash
python3 tools/validate_catalog.py --report /tmp/catalog-report.json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Per-card: `python3 tools/validate_catalog.py --group GS04`. Inspect full case: `python3 tools/inspect_oracle.py GS04-T02`. Inputs are inert synthetic descriptions; no command executes those descriptions. Exit 0 means static checks passed, exit 1 means findings, argparse misuse exit 2. JSON output is stable for identical content; input SHA256 values bind records. Reports do not self-certify operational behavior.

Checks: required files; exactly ten frontmatter names/descriptions; original ID set/continuity/count; twelve supplemental IDs; exact original scenario alignment; individual requirement uniqueness and source headings; mandatory fields; all 212 trace rows and index entries; relative Markdown links/heading anchors; OWNER-ONLY classes; structured status consistency and unsupported positive runtime claims. Plain code examples are excluded from link parsing. The validator is a repository-specific Markdown subset checker, not a general CommonMark parser or proof of every prose sentence. Explicit dispositions and semantic review remain necessary.

Regression tests deliberately remove fields, duplicate IDs, alter headings/counts, break links, remove reserved classes and inject unsupported certification; they must produce failures. Cache reference tests mutate repository/scope/SHAs/locks/runtime, approval, integrity and action reconciliation; missing accounting remains UNKNOWN. No test sends a provider request, opens a browser or writes outside temporary local test directories.

The 212 checks measure specification coverage. The local unittest count measures validator/reference-code regressions, not 212 executed OpenHands scenarios. Report these denominators separately. Local runtime of Python validators is not OpenHands runtime certification.
