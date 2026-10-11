"""Print a specification, or compare a supplied observation. Never invoke tools."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('id')
p.add_argument('--observation',type=Path)
a=p.parse_args()
rows=[r for f in sorted((ROOT/'fixtures/oracles').glob('*.json')) for r in json.loads(f.read_text()) if r['id']==a.id]
if len(rows)!=1:
    p.error('Unknown or duplicate oracle')
r=rows[0]
if not a.observation:
    print(json.dumps(r,indent=2))
    sys.exit(0)
obs=json.loads(a.observation.read_text())
errors=[k for k,v in r['expected'].items() if k not in obs or type(obs[k]) is not type(v) or obs[k]!=v]
print(json.dumps({'id':a.id,'scope':'SUPPLIED_OBSERVATION_COMPARISON_ONLY','mismatched_fields':errors,'verdict':'FAIL' if errors else 'PASS','runtime_certified':False},indent=2))
sys.exit(bool(errors))
