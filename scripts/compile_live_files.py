import sys, json
sys.path.insert(0, '.')

from scripts.dict_es_1 import MAP_ES_1
from scripts.dict_es_2 import MAP_ES_2
from scripts.dict_es_3 import MAP_ES_3
from scripts.dict_es_4a import MAP_ES_4A
from scripts.dict_es_4b import MAP_ES_4B

from scripts.dict_zh_1 import MAP_ZH_1
from scripts.dict_zh_2 import MAP_ZH_2
from scripts.dict_zh_3 import MAP_ZH_3
from scripts.dict_zh_4a import MAP_ZH_4A
from scripts.dict_zh_4b import MAP_ZH_4B

map_es = {}
map_es.update(MAP_ES_1)
map_es.update(MAP_ES_2)
map_es.update(MAP_ES_3)
map_es.update(MAP_ES_4A)
map_es.update(MAP_ES_4B)

map_zh = {}
map_zh.update(MAP_ZH_1)
map_zh.update(MAP_ZH_2)
map_zh.update(MAP_ZH_3)
map_zh.update(MAP_ZH_4A)
map_zh.update(MAP_ZH_4B)

with open('locales/fa/live.json') as f:
    fa_live = json.load(f)

def get_leaf_dict(d, p=''):
    res = {}
    for k, v in d.items():
        sub = f'{p}.{k}' if p else k
        if isinstance(v, dict):
            res.update(get_leaf_dict(v, sub))
        else:
            res[sub] = v
    return res

fa_leaves = get_leaf_dict(fa_live)
print(f"Total fa leaves: {len(fa_leaves)}")
print(f"Total es mapped: {len(map_es)}")
print(f"Total zh mapped: {len(map_zh)}")

missing_es = set(fa_leaves.keys()) - set(map_es.keys())
missing_zh = set(fa_leaves.keys()) - set(map_zh.keys())
print(f"Missing in ES: {len(missing_es)}")
if missing_es:
    print("ES missing sample:", sorted(list(missing_es))[:10])
print(f"Missing in ZH: {len(missing_zh)}")
if missing_zh:
    print("ZH missing sample:", sorted(list(missing_zh))[:10])
