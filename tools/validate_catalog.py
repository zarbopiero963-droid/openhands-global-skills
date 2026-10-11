"""Offline catalog validator. No network, subprocess, installation or agent execution."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [12, 14, 16, 18, 20, 22, 24, 24, 24, 26]
FIELDS = {'id','requirement_id','requirement','source','source_heading','normative_section','dependencies','fixture','preconditions','procedure','expected','test_type','evidence_required','criteria','cleanup','economic_limit','owner_authorization','status'}

def validate(root, group=None):
    errors = []
    allowed_groups={f'GS{i:02d}' for i in range(1,11)}|{'GS08-CACHE'}
    if group and group not in allowed_groups:
        errors.append('unknown group: '+group)
    paths = sorted((root / 'fixtures/oracles').glob('*.json'))
    records = []
    for path in paths:
        if group and path.stem != group:
            continue
        try:
            rows = json.loads(path.read_text())
            if not isinstance(rows,list) or any(not isinstance(row,dict) for row in rows):
                errors.append(path.name+': expected list of record objects')
                continue
            records.extend(rows)
            for r in rows:
                tag = r.get('id', str(path))
                for field in sorted(FIELDS):
                    if field not in r or r[field] in ('',None,[],{}):
                        errors.append(f'{tag}: missing {field}')
                if not FIELDS <= r.keys():
                    continue
                source = (root / r['source']).resolve()
                if not source.is_relative_to(root.resolve()):
                    errors.append(f'{tag}: source escapes root')
                    continue
                if not source.is_file() or r['source_heading'] not in source.read_text():
                    errors.append(f'{tag}: missing source/heading')
                elif not any(h.startswith(r['normative_section']) or h.removeprefix('## ').startswith(r['normative_section']) for h in source.read_text().splitlines() if h.startswith('## ')):
                    errors.append(f'{tag}: missing normative section')
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
    if not group:
        errors.extend(global_checks(root, records))
    errors.sort()
    hashes = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if not group or p.stem==group}
    return {'schema_version':1,'scope':'STATIC_SPECIFICATION_ONLY','group':group or 'ALL','records_checked':len(records),'runtime_tests_executed':0,'runtime_certified':0,'errors':errors,'verdict':'FAIL' if errors else 'PASS','input_sha256':hashes}

def global_checks(root, records):
    errors=[]
    mandatory=['README.md','AGENTS.md','CLAUDE.md','GLOBAL_POLICY.md','CERTIFICATION.md']
    mandatory += ['docs/'+x+'.md' for x in ['ROADMAP','ORACLE_INDEX','REQUIREMENTS_TRACEABILITY','CACHE_STRATEGY','OWNER_APPROVAL','ARCHITECTURE','COST_AND_MODELS','ARTIFACTS_AND_BROWSER','MCP_AND_NOTIFICATIONS','REPOSITORY_GUIDE','TEST_ORACLES','PREFLIGHT_ONE_SHOT_TEST','PREFLIGHT_READONLY_EVIDENCE','STATIC_VALIDATION','OWNER_DECISIONS','FINDINGS','CERTIFICATION_MATRIX','FINAL_REPORT']]
    for p in mandatory:
        if not (root/p).is_file(): errors.append('required file missing: '+p)
    skills=sorted((root/'skills').glob('*/SKILL.md'))
    if len(skills)!=10: errors.append('skill count must equal 10')
    original={}
    names=[]
    for p in skills:
        text=p.read_text()
        front=re.match(r'---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n',text)
        if not front or front[1]!=p.parent.name:
            errors.append('invalid frontmatter: '+str(p.relative_to(root)))
        else: names.append(front[1])
        for oid,scenario,expected in re.findall(r'^\| (GS\d{2}-T\d{2}) \| (.*?) \| (.*?) \|$',text,re.M):
            if oid in original: errors.append('duplicate source oracle: '+oid)
            original[oid]=scenario
    if len(set(names))!=10: errors.append('frontmatter names not unique/complete')
    base={f'GS{n:02d}-T{i:02d}' for n,c in enumerate(COUNTS,1) for i in range(1,c+1)}
    if set(original)!=base: errors.append('original 200 source IDs differ')
    cache=root/'docs/CACHE_STRATEGY.md'
    cache_ids=re.findall(r'^\| (GS08-C\d{2}) \|',cache.read_text(),re.M) if cache.is_file() else []
    if cache_ids != [f'GS08-C{i:02d}' for i in range(1,13)]: errors.append('cache 12 source IDs differ')
    requirements=[r.get('requirement_id') for r in records]
    if len(set(requirements))!=len(requirements): errors.append('duplicate requirement IDs')
    trace=root/'docs/REQUIREMENTS_TRACEABILITY.md'
    index=root/'docs/ORACLE_INDEX.md'
    trace_text=trace.read_text() if trace.is_file() else ''
    index_text=index.read_text() if index.is_file() else ''
    for r in records:
        oid=r.get('id','')
        if oid in original and r.get('fixture',{}).get('scenario')!=original[oid]: errors.append(oid+': source scenario drift')
        if len(re.findall(r'^\| '+re.escape(r.get('requirement_id',''))+r' \| '+re.escape(oid)+r' \|',trace_text,re.M))!=1: errors.append(oid+': trace missing/duplicate')
        if len(re.findall(r'^\| '+re.escape(oid)+r' \|',index_text,re.M))!=1: errors.append(oid+': index missing/duplicate')
    # Eight clauses are tested in the normative numbered contract, not a mention count.
    policy=root/'docs/OWNER_APPROVAL.md'
    clauses=re.findall(r'^([1-8])\. (.+)$',policy.read_text(),re.M) if policy.is_file() else []
    keywords=['repository','secrets','paid','production','Betfair','Delete','security','irreversible']
    if len(clauses)!=8 or any(n!=str(i) or word.lower() not in clause.lower() for i,((n,clause),word) in enumerate(zip(clauses,keywords),1)):
        errors.append('eight OWNER-ONLY clauses missing or changed')
    def slug(h):
        return re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-')
    for p in sorted(root.rglob('*.md')):
        if '.git' in p.parts: continue
        body=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
        # Inline explicit Markdown links; reference-style unsupported in this catalog.
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',body):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target): continue
            path,_,anchor=target.partition('#')
            resolved=(p.parent/path).resolve() if path else p.resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(str(p.relative_to(root))+': link escapes root'); continue
            if not resolved.exists():
                errors.append(str(p.relative_to(root))+': broken link '+target); continue
            if anchor and resolved.suffix=='.md':
                headings=re.findall(r'^#{1,6} (.+)$',resolved.read_text(),re.M)
                if anchor not in [slug(h) for h in headings]: errors.append(str(p.relative_to(root))+': missing anchor '+target)
        if re.search(r'(?im)^\s*(?:\*\*)?(?:runtime_status|operational_status)\s*[:=]\s*(?:PASS|CERTIFIED)\b',body):
            errors.append(str(p.relative_to(root))+': unsupported runtime certification claim')
    return errors

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
