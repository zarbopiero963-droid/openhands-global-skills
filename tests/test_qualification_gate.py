import copy
from datetime import datetime, timezone
import unittest
from tools.qualification_gate import CHECKS, COMMAND, REPO, evaluate

class QualificationGateTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 11, tzinfo=timezone.utc)
        self.record = dict.fromkeys(CHECKS, True)
        self.record.update(repository=REPO, command=COMMAND, head='a'*40,
            model_id='synthetic/model', provider='synthetic', owner_decision_id='mock-1',
            owner_evidence_reference='synthetic-only', budget_usd=.1, available_balance_usd=.2,
            duration_seconds=600, sessions=1, approval_consumed=False, writes_allowed=False,
            expires_utc='2026-10-12T00:00:00Z')
    def test_complete_declarations_never_authorize_execution(self):
        r=evaluate(self.record,self.now)
        self.assertEqual(r['verdict'],'DECLARATIONS_COMPLETE')
        self.assertIs(r['execution_authorized'],False)
    def test_each_missing_gate_blocks(self):
        for key in CHECKS:
            with self.subTest(key=key):
                r=copy.deepcopy(self.record); del r[key]
                self.assertIn(key,evaluate(r,self.now)['blockers'])
    def test_truthy_string_cannot_pass_security(self):
        self.record['security_verified']='true'
        self.assertIn('security_verified',evaluate(self.record,self.now)['blockers'])
    def test_scope_or_command_expansion_blocks(self):
        for key,value in [('repository','synthetic/forbidden'),('command',COMMAND+'; echo extra'),('writes_allowed',True),('sessions',2)]:
            with self.subTest(key=key):
                r=dict(self.record);r[key]=value
                self.assertIn(key,evaluate(r,self.now)['blockers'])
    def test_budget_nonfinite_negative_and_boolean_block(self):
        for value in (float('nan'),float('inf'),-1,0,True,'0.1'):
            with self.subTest(value=value):
                r=dict(self.record,budget_usd=value)
                self.assertIn('budget_usd',evaluate(r,self.now)['blockers'])
    def test_insufficient_balance_blocks(self):
        self.record['available_balance_usd']=.01
        self.assertIn('available_balance_usd',evaluate(self.record,self.now)['blockers'])
    def test_expiry_missing_naive_and_expired_block(self):
        for value in (None,'invalid','2026-10-12T00:00:00','2026-10-10T00:00:00Z'):
            with self.subTest(value=value):
                r=dict(self.record,expires_utc=value)
                self.assertIn('expires_utc',evaluate(r,self.now)['blockers'])
    def test_replayed_approval_blocks(self):
        self.record['approval_consumed']=True
        self.assertIn('approval_consumed',evaluate(self.record,self.now)['blockers'])
    def test_duration_and_unpinned_head_block(self):
        self.record.update(duration_seconds=601,head='main')
        self.assertTrue({'duration_seconds','head'} <= set(evaluate(self.record,self.now)['blockers']))
    def test_malformed_root_blocks(self):
        self.assertEqual(evaluate([],self.now)['verdict'],'BLOCKED')
