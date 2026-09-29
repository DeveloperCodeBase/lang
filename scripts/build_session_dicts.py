import json

g2 = json.load(open('scripts/group2_keys.json'))
ar = json.load(open('locales/ar/live.json'))
fa = json.load(open('locales/fa/live.json'))

def get_leaf_dict(d, p=''):
    res = {}
    for k, v in d.items():
        sub = f'{p}.{k}' if p else k
        if isinstance(v, dict):
            res.update(get_leaf_dict(v, sub))
        else:
            res[sub] = v
    return res

ar_sess = get_leaf_dict(ar['session'], 'session')
fa_sess = get_leaf_dict(fa['session'], 'session')
en_sess = {k: v['en'] for k, v in g2.items() if k.startswith('session.')}

print(f"Loaded {len(en_sess)} session keys.")
