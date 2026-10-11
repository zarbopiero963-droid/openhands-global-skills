import copy
import unittest
from tools.cache_policy import reuse, digest, prompt_evidence, savings

class CachePolicyTests(unittest.TestCase):
    def setUp(self):
        self.c={'kind':'github_blob','repository':'repo-A','authorization_scope':'scope-A','policy_sha':'p1','schema_version':1,'commit_sha':'A','path':'README.md','blob_sha':'blob-A','payload':'hello','sha256':digest('hello'),'secret_scan':'CLEAN'}
        self.now=dict(self.c,approval_valid=True)
    def test_immutable_match(self):
        self.assertEqual(reuse(self.c,self.now),{'reuse':True,'reason':'IMMUTABLE_MATCH'})
    def test_cross_repository_denied(self):
        self.now['repository']='repo-B';self.assertFalse(reuse(self.c,self.now)['reuse'])
    def test_scope_changes_denied(self):
        self.now['authorization_scope']='scope-B';self.assertFalse(reuse(self.c,self.now)['reuse'])
    def test_policy_change_invalidates(self):
        self.now['policy_sha']='p2';self.assertEqual(reuse(self.c,self.now)['reason'],'KEY_MISMATCH:policy_sha')
    def test_commit_path_blob_each_invalidates(self):
        for key in ('commit_sha','path','blob_sha','schema_version'):
            with self.subTest(key=key):
                current=dict(self.now);current[key]='different'
                self.assertFalse(reuse(self.c,current)['reuse'])
    def test_unknown_key_denied(self):
        del self.now['blob_sha'];self.assertFalse(reuse(self.c,self.now)['reuse'])
    def test_secret_or_unscanned_rejected(self):
        for status in ('FOUND','UNKNOWN',None):
            with self.subTest(status=status):
                self.c['secret_scan']=status;self.assertFalse(reuse(self.c,self.now)['reuse'])
    def test_corrupt_payload_rejected(self):
        self.c['payload']='corrupt';self.assertEqual(reuse(self.c,self.now)['reason'],'INTEGRITY_FAILURE')
    def test_mutable_data_always_fresh_even_matching(self):
        for kind in ('approval','quota','live','ci','review','branch','permissions','budget'):
            with self.subTest(kind=kind):
                self.c['kind']=kind;self.now['kind']=kind
                self.assertEqual(reuse(self.c,self.now)['reason'],'FRESH_READ_REQUIRED')
    def test_expired_approval_blocks_immutable(self):
        self.now['approval_valid']=False;self.assertEqual(reuse(self.c,self.now)['reason'],'APPROVAL_INVALID')
    def test_deterministic_environment_invalidation(self):
        c=dict(self.c,kind='deterministic',code_sha='A',input_sha='input',lock_sha='lock',runtime='3.11',environment='linux',parameters='{}')
        now=dict(c,approval_valid=True)
        self.assertTrue(reuse(c,now)['reuse'])
        for k in ('code_sha','input_sha','lock_sha','runtime','environment','parameters'):
            with self.subTest(key=k):
                changed=dict(now);changed[k]='changed';self.assertFalse(reuse(c,changed)['reuse'])
    def test_checkpoint_requires_reconciliation(self):
        c=dict(self.c,kind='checkpoint',checkpoint_id='C',revision=1,action_ledger_sha='L')
        now=dict(c,approval_valid=True,ambiguous_actions=1,reconciled=False)
        self.assertEqual(reuse(c,now)['reason'],'RECONCILIATION_REQUIRED')
        now.update(ambiguous_actions=0,reconciled=True)
        self.assertTrue(reuse(c,now)['reuse'])
    def test_missing_provider_fields_unknown(self):
        self.assertEqual(prompt_evidence({'model':'M'}),{'status':'UNKNOWN','cache_hit_claim':False})
    def complete_usage(self):
        return dict(model='M',provider='P',request_id='R',observed_utc='2026-10-11T00:00:00Z',usage_source='synthetic',cache_read_tokens=80,cache_write_tokens=20,input_tokens=100,output_tokens=10,billed_usd='0.40',token_semantics='synthetic specification',support_verified=True)
    def test_complete_metadata_still_not_runtime_proof(self):
        out=prompt_evidence(self.complete_usage())
        self.assertFalse(out['cache_hit_claim']);self.assertEqual(out['reported_cache_read_tokens'],80)
        self.assertEqual(out['status'],'METADATA_COMPLETE_NOT_RUNTIME_PROOF')
    def test_invalid_token_counts(self):
        for v in (-1,True,'80'):
            with self.subTest(v=v):
                r=self.complete_usage();r['cache_read_tokens']=v
                self.assertEqual(prompt_evidence(r)['status'],'INVALID')
    def test_unsupported_provider_unknown(self):
        r=self.complete_usage();r['support_verified']=False
        self.assertEqual(prompt_evidence(r)['status'],'UNKNOWN')
    def test_nonfinite_cost_invalid(self):
        for v in ('NaN','Infinity','-1'):
            r=self.complete_usage();r['billed_usd']=v
            self.assertEqual(prompt_evidence(r)['status'],'INVALID')
    def ledger(self):
        return dict(equivalent_workload=True,billing_final=True,nonoverlapping=True,uncached_billed='1.00',cached_billed='0.40',extra_storage='0.05',extra_revalidation='0.05',extra_summarization='0.10')
    def test_net_savings_no_double_subtraction(self):
        r=self.ledger();r['displayed_discount']='0.30';r['cache_write_already_billed']='0.10'
        self.assertEqual(savings(r)['net_savings_usd'],'0.40')
    def test_negative_savings_preserved(self):
        r=self.ledger();r['cached_billed']='2.00';self.assertEqual(savings(r)['net_savings_usd'],'-1.20')
    def test_unknown_pending_overlapping_costs(self):
        for k in ('equivalent_workload','billing_final','nonoverlapping','cached_billed'):
            with self.subTest(key=k):
                r=self.ledger();del r[k];self.assertEqual(savings(r)['status'],'UNKNOWN')
    def test_inputs_not_mutated(self):
        before=copy.deepcopy(self.c);reuse(self.c,self.now);self.assertEqual(self.c,before)

    def test_model_provider_change_invalidates_claim(self):
        r=self.complete_usage()
        for current in ({'model':'M2','provider':'P'},{'model':'M','provider':'P2'}):
            with self.subTest(current=current):
                self.assertEqual(prompt_evidence(r,current)['reason'],'MODEL_PROVIDER_CHANGED')
    def test_read_write_tokens_kept_separate(self):
        out=prompt_evidence(self.complete_usage())
        self.assertEqual(out['reported_cache_read_tokens'],80)
        self.assertEqual(out['reported_cache_write_tokens'],20)
        self.assertEqual(out['input_tokens'],100)
