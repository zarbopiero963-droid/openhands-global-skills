import json
from pathlib import Path
import tempfile
import shutil
import unittest
from tools.validate_catalog import ROOT,validate

class IndependentAuditRegressionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'catalog'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def mutate(self,field,value):
        p=self.root/'fixtures/oracles/GS04.json';rows=json.loads(p.read_text());rows[0][field]=value;p.write_text(json.dumps(rows))
        result=validate(self.root)
        self.assertEqual(result['verdict'],'FAIL')
        return result
    def test_numeric_procedure_rejected(self):self.mutate('procedure',7)
    def test_list_assertions_rejected(self):self.mutate('expected',['anything'])
    def test_wrong_fixture_type_reported_not_crash(self):self.mutate('fixture','wrong')
    def test_requirement_not_related_to_source_rejected(self):self.mutate('requirement','unrelated text')
    def test_wrong_id_type_reported_not_crash(self):self.mutate('id',['wrong'])
    def test_unmapped_trace_row_rejected(self):
        p=self.root/'docs/REQUIREMENTS_TRACEABILITY.md';p.write_text(p.read_text()+'\n| REQ-GS99-T01 | GS99-T01 | unmapped |\n')
        self.assertIn('unmapped or missing trace requirements',validate(self.root)['errors'])
