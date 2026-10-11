"""Offline catalog validator. No network, subprocess, installation or agent execution."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [12, 14, 16, 18, 20, 22, 24, 24, 24, 26]
FIELDS = {'id','requirement_id','requirement','source','source_heading','dependencies','fixture','preconditions','procedure','expected','test_type','evidence_required','criteria','cleanup','economic_limit','owner_authorization','status'}

def validate(root, group=None):
    errors = []
    paths = sorted((root / 'fixtures/oracles').glob('*.json'))
    records = []
    for path in paths:
        if group and path.stem != group:
            continue
        try:
            rows = json.loads(path.read_text())
            records.extend(rows)
            for r in rows:
                tag = r.get('id', str(path))
                for field in FIELDS:
                    if field not in r or r[field] in ('',None,[],{}):
                        errors.append(f'{tag}: missing {field}')
                if not FIELDS <= r.keys():
                    continue
                source = root / r['source']
                if not source.is_file() or r['source_heading'] not in source.read_text():
                    errors.append(f'{tag}: missing source/heading')
                elif not re.search(r'^\| '+re.escape(tag)+r' \|', source.read_text(), re.M):
                    errors.append(f'{tag}: missing original oracle')
                if r['requirement_id'] != 'REQ-'+tag:
                    errors.append(f'{tag}: wrong requirement ID')
                if not r['expected'] or any(not isinstance(k,str) for k in r['expected']):
                    errors.append(f'{tag}: assertions absent')
                if r['test_type'] not in ('POSITIVE','NEGATIVE','MIXED'):
                    errors.append(f'{tag}: invalid test type')
                if set(r['criteria']) != {'PASS','FAIL','BLOCKED'}:
                    errors.append(f'{tag}: incomplete verdict rules')
                status = r['status']
                if status != {'documented':True,'fixture_implemented':True,'runtime_implemented':False,'runtime_tested':False,'runtime_certified':False,'runtime_gate':'BLOCKED'}:
                    errors.append(f'{tag}: unsupported status; runtime evidence/acceptance not supplied')
                if r['economic_limit']['external_spend_usd'] != 0:
                    errors.append(f'{tag}: unapproved spending')
        except (ValueError,TypeError,KeyError) as exc:
            errors.append(f'{path.name}: {exc}')
    ids = [r.get('id') for r in records]
    if len(ids) != len(set(ids)):
        errors.append('duplicate oracle IDs')
    expected = {f'GS{n:02d}-T{i:02d}' for n,c in enumerate(COUNTS,1) for i in range(1,c+1)} | {f'GS08-C{i:02d}' for i in range(1,13)}
    if group:
        expected = {x for x in expected if (x.startswith('GS08-C') if group=='GS08-CACHE' else x.startswith(group+'-T'))}
    if set(ids) != expected:
        errors.append(f'ID mismatch missing={sorted(expected-set(ids))} extra={sorted(set(ids)-expected)}')
    hashes = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if not group or p.stem==group}
    return {'schema_version':1,'scope':'STATIC_SPECIFICATION_ONLY','group':group or 'ALL','records_checked':len(records),'runtime_tests_executed':0,'runtime_certified':0,'errors':errors,'verdict':'FAIL' if errors else 'PASS','input_sha256':hashes}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--group')
    p.add_argument('--report',type=Path)
    a=p.parse_args()
    result=validate(ROOT,a.group)
    output=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.report:
        a.report.write_text(output)
    print(output,end='')
    return bool(result['errors'])

if __name__=='__main__':
    sys.exit(main())
