"""Pure reference cache decisions for synthetic input, NOT an OpenHands integration."""
import hashlib
from decimal import Decimal, InvalidOperation

IMMUTABLE = {'github_blob','deterministic','checkpoint'}
ALWAYS_FRESH = {'approval','quota','live','ci','review','branch','permissions','budget'}
COMMON = ('repository','authorization_scope','policy_sha','schema_version')
KEYS = {
 'github_blob': COMMON+('commit_sha','path','blob_sha'),
 'deterministic': COMMON+('code_sha','input_sha','lock_sha','runtime','environment','parameters'),
 'checkpoint': COMMON+('checkpoint_id','revision','action_ledger_sha'),
}

def digest(payload):
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def reuse(candidate, current):
    """Reject unknown, stale, cross-scope or unsafe data. No cache I/O occurs."""
    if candidate.get('secret_scan') != 'CLEAN' or current.get('secret_scan') != 'CLEAN':
        return {'reuse':False,'reason':'SECRET_OR_UNSCANNED'}
    kind = candidate.get('kind')
    if kind in ALWAYS_FRESH:
        return {'reuse':False,'reason':'FRESH_READ_REQUIRED'}
    if kind not in IMMUTABLE or current.get('kind') != kind:
        return {'reuse':False,'reason':'UNSUPPORTED_KIND'}
    if current.get('approval_valid') is not True:
        return {'reuse':False,'reason':'APPROVAL_INVALID'}
    for key in KEYS[kind]:
        if key not in candidate or key not in current or candidate[key] in (None,'','UNKNOWN') or candidate[key] != current[key]:
            return {'reuse':False,'reason':'KEY_MISMATCH:'+key}
    payload = candidate.get('payload')
    if not isinstance(payload,str) or candidate.get('sha256') != digest(payload):
        return {'reuse':False,'reason':'INTEGRITY_FAILURE'}
    if kind == 'checkpoint' and (current.get('ambiguous_actions') != 0 or current.get('reconciled') is not True):
        return {'reuse':False,'reason':'RECONCILIATION_REQUIRED'}
    return {'reuse':True,'reason':'IMMUTABLE_MATCH'}

def prompt_evidence(record, current=None):
    """Validate supplied accounting metadata; never attest provider authenticity."""
    if current is not None and any(not current.get(k) or current.get(k) != record.get(k) for k in ('model','provider')):
        return {'status':'UNKNOWN','cache_hit_claim':False,'reason':'MODEL_PROVIDER_CHANGED'}
    keys=('model','provider','request_id','observed_utc','usage_source','cache_read_tokens','cache_write_tokens','input_tokens','output_tokens','billed_usd')
    if any(k not in record or record[k] is None or record[k]=='UNKNOWN' for k in keys):
        return {'status':'UNKNOWN','cache_hit_claim':False}
    for k in ('cache_read_tokens','cache_write_tokens','input_tokens','output_tokens'):
        if type(record[k]) is not int or record[k]<0:
            return {'status':'INVALID','cache_hit_claim':False}
    # Provider schemas differ: require documented token semantics; don't assume
    # cache-write tokens must fit inside a particular vendor's input count.
    if not record.get('token_semantics') or record.get('support_verified') is not True:
        return {'status':'UNKNOWN','cache_hit_claim':False}
    try:
        cost=Decimal(str(record['billed_usd']))
        if not cost.is_finite() or cost<0: raise ValueError('cost')
    except (InvalidOperation,ValueError):
        return {'status':'INVALID','cache_hit_claim':False}
    return {'status':'METADATA_COMPLETE_NOT_RUNTIME_PROOF','cache_hit_claim':False,'reported_cache_read_tokens':record['cache_read_tokens'],'reported_cache_write_tokens':record['cache_write_tokens'],'input_tokens':record['input_tokens'],'output_tokens':record['output_tokens'],'billed_usd':str(cost)}

def savings(record):
    """Compare non-overlapping, equivalent workloads using final billed costs."""
    if record.get('equivalent_workload') is not True or record.get('billing_final') is not True or record.get('nonoverlapping') is not True:
        return {'status':'UNKNOWN'}
    names=('uncached_billed','cached_billed','extra_storage','extra_revalidation','extra_summarization')
    try:
        values=[Decimal(str(record[k])) for k in names]
        if any(not n.is_finite() or n<0 for n in values): raise ValueError('cost')
    except (KeyError,ValueError,InvalidOperation):
        return {'status':'UNKNOWN'}
    # cached_billed already includes provider cache-write/read charges.
    net=values[0]-sum(values[1:])
    return {'status':'MEASURED_INPUT_COMPARISON','net_savings_usd':str(net)}
