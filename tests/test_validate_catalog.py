import json
from pathlib import Path
import shutil
import tempfile
import unittest
from tools.validate_catalog import validate, ROOT

class CatalogMutationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'catalog'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def change_record(self,fn):
        p=self.root/'fixtures/oracles/GS04.json';rows=json.loads(p.read_text());fn(rows);p.write_text(json.dumps(rows))
    def rejects(self,fragment):
        report=validate(self.root)
        self.assertEqual(report['verdict'],'FAIL')
        self.assertTrue(any(fragment in e for e in report['errors']),report['errors'])
    def test_valid_catalog(self):
        report=validate(self.root);self.assertEqual(report['errors'],[]);self.assertEqual(report['records_checked'],212)
    def test_missing_required_document(self):
        (self.root/'AGENTS.md').unlink();self.rejects('required file missing')
    def test_bad_frontmatter(self):
        p=self.root/'skills/python-testing/SKILL.md';p.write_text(p.read_text().replace('name: python-testing','name: wrong'))
        self.rejects('invalid frontmatter')
    def test_duplicate_id(self):
        self.change_record(lambda rows:rows.append(rows[0]));self.rejects('duplicate oracle IDs')
    def test_gap_in_id(self):
        self.change_record(lambda rows:rows.pop());self.rejects('ID mismatch')
    def test_missing_procedure(self):
        self.change_record(lambda rows:rows[0].pop('procedure'));self.rejects('missing procedure')
    def test_empty_assertions(self):
        self.change_record(lambda rows:rows[0].update(expected={}));self.rejects('missing expected')
    def test_missing_source_heading(self):
        self.change_record(lambda rows:rows[0].update(source_heading='## Invented section'));self.rejects('missing source/heading')
    def test_missing_normative_section(self):
        self.change_record(lambda rows:rows[0].update(normative_section='## Invented rule'));self.rejects('missing normative section')
    def test_source_scenario_drift(self):
        self.change_record(lambda rows:rows[0]['fixture'].update(scenario='Different behavior'));self.rejects('source scenario drift')
    def test_broken_markdown_link(self):
        p=self.root/'README.md';p.write_text(p.read_text()+'\n[Broken](no-such-file.md)\n');self.rejects('broken link')
    def test_broken_anchor(self):
        p=self.root/'README.md';p.write_text(p.read_text()+'\n[Broken](AGENTS.md#absent-heading)\n');self.rejects('missing anchor')
    def test_missing_trace_row(self):
        p=self.root/'docs/REQUIREMENTS_TRACEABILITY.md';p.write_text('\n'.join(x for x in p.read_text().splitlines() if not x.startswith('| REQ-GS04-T01 |')))
        self.rejects('trace missing/duplicate')
    def test_missing_owner_category(self):
        p=self.root/'docs/OWNER_APPROVAL.md';p.write_text(p.read_text().replace('8. Perform irreversible','8. Perform ordinary'))
        self.rejects('eight OWNER-ONLY')
    def test_unsupported_runtime_state(self):
        self.change_record(lambda rows:rows[0]['status'].update(runtime_certified=True));self.rejects('unsupported status')
    def test_unsupported_runtime_claim(self):
        p=self.root/'README.md';p.write_text(p.read_text()+'\nruntime_status: CERTIFIED\n');self.rejects('unsupported runtime certification claim')
    def test_unapproved_spend(self):
        self.change_record(lambda rows:rows[0]['economic_limit'].update(external_spend_usd=1));self.rejects('unapproved spending')
    def test_missing_cache_case(self):
        p=self.root/'fixtures/oracles/GS08-CACHE.json';rows=json.loads(p.read_text());rows.pop();p.write_text(json.dumps(rows));self.rejects('ID mismatch')

    def test_source_escape_rejected(self):
        self.change_record(lambda rows:rows[0].update(source='../outside.md'));self.rejects('source escapes root')
    def test_unknown_group_rejected(self):
        self.assertEqual(validate(self.root,'TYPO')['verdict'],'FAIL')
    def test_invalid_record_shape(self):
        (self.root/'fixtures/oracles/GS04.json').write_text('[42]');self.rejects('expected list of record objects')
    def test_repeatable_error_order(self):
        self.change_record(lambda rows:rows[0].update(procedure=[],expected={},cleanup=''))
        self.assertEqual(validate(self.root),validate(self.root))
