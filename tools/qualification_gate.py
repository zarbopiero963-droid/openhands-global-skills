"""Offline checklist validator, NOT an authorization or Cloud enforcement system."""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re

REPO = 'zarbopiero963-droid/cloud-ai-developer-test'
COMMAND = "python -m unittest discover -s tests -p 'test_*.py' -v"
CHECKS = ('phases_reviewed', 'security_verified', 'scope_verified',
          'skills_bundle_verified', 'cloud_cost_resolved', 'model_verified',
          'ledger_reconciled', 'stop_cleanup_defined', 'owner_evidence_verified')

def positive_number(value):
    return type(value) in (int, float) and math.isfinite(value) and value > 0

def evaluate(record, now=None):
    """Only checks supplied declarations; never trusts them as platform proof."""
    now = now or datetime.now(timezone.utc)
    if not isinstance(record, dict):
        return {'verdict': 'BLOCKED', 'blockers': ['record must be object'], 'execution_authorized': False}
    blockers = [key for key in CHECKS if record.get(key) is not True]
    if record.get('repository') != REPO: blockers.append('repository')
    if record.get('command') != COMMAND: blockers.append('command')
    if not re.fullmatch('[0-9a-f]{40}', str(record.get('head', ''))): blockers.append('head')
    for key in ('model_id', 'provider', 'owner_decision_id', 'owner_evidence_reference'):
        if not isinstance(record.get(key), str) or record[key].strip() in ('', 'UNKNOWN', 'PENDING'):
            blockers.append(key)
    budget = record.get('budget_usd')
    if not positive_number(budget): blockers.append('budget_usd')
    balance = record.get('available_balance_usd')
    if not positive_number(balance) or (positive_number(budget) and balance < budget):
        blockers.append('available_balance_usd')
    duration = record.get('duration_seconds')
    if type(duration) is not int or not 1 <= duration <= 600: blockers.append('duration_seconds')
    if type(record.get('sessions')) is not int or record['sessions'] != 1: blockers.append('sessions')
    if record.get('approval_consumed') is not False: blockers.append('approval_consumed')
    if record.get('writes_allowed') is not False: blockers.append('writes_allowed')
    try:
        expires = datetime.fromisoformat(record['expires_utc'].replace('Z', '+00:00'))
        if expires.tzinfo is None or expires <= now: blockers.append('expires_utc')
    except (KeyError, ValueError, TypeError, AttributeError):
        blockers.append('expires_utc')
    return {'verdict': 'BLOCKED' if blockers else 'DECLARATIONS_COMPLETE',
            'blockers': sorted(set(blockers)), 'execution_authorized': False,
            'limitation': 'No identity authentication, ledger verification, permission enforcement or session creation. Human verifies evidence before any separate execution.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    try:
        result = evaluate(json.loads(args.record.read_text()))
    except (OSError, ValueError) as exc:
        print(json.dumps({'verdict': 'INVALID_INPUT', 'error': str(exc), 'execution_authorized': False}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True, indent=2))
    return 3 if result['blockers'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
