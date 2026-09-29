import sys, json
sys.path.insert(0, '.')

from scripts.dict_es_1 import MAP_ES_1
from scripts.dict_es_2 import MAP_ES_2
from scripts.dict_es_3 import MAP_ES_3
from scripts.dict_es_4a import MAP_ES_4A
from scripts.dict_es_4b import MAP_ES_4B
from scripts.dict_es_missing import MAP_ES_MISSING
from scripts.dict_es_final import MAP_ES_FINAL

from scripts.dict_zh_1 import MAP_ZH_1
from scripts.dict_zh_2 import MAP_ZH_2
from scripts.dict_zh_3 import MAP_ZH_3
from scripts.dict_zh_4a import MAP_ZH_4A
from scripts.dict_zh_4b import MAP_ZH_4B
from scripts.dict_zh_missing import MAP_ZH_MISSING
from scripts.dict_zh_final import MAP_ZH_FINAL

map_es = {}
for m in [MAP_ES_1, MAP_ES_2, MAP_ES_3, MAP_ES_4A, MAP_ES_4B, MAP_ES_MISSING, MAP_ES_FINAL]:
    map_es.update(m)
map_es["session.media.retry"] = "Reintentar"

map_zh = {}
for m in [MAP_ZH_1, MAP_ZH_2, MAP_ZH_3, MAP_ZH_4A, MAP_ZH_4B, MAP_ZH_MISSING, MAP_ZH_FINAL]:
    map_zh.update(m)
map_zh["session.media.retry"] = "重试"

with open('locales/fa/live.json', encoding='utf-8') as f:
    fa_live = json.load(f)

def build_tree(fa_sub, trans_map, path=''):
    if isinstance(fa_sub, dict):
        res = {}
        for k, v in fa_sub.items():
            subpath = f'{path}.{k}' if path else k
            res[k] = build_tree(v, trans_map, subpath)
        return res
    else:
        if path in trans_map:
            return trans_map[path]
        else:
            raise KeyError(f"Missing translation for leaf {path}")

tree_es = build_tree(fa_live, map_es)
tree_zh = build_tree(fa_live, map_zh)

with open('locales/es/live.json', 'w', encoding='utf-8') as f:
    json.dump(tree_es, f, ensure_ascii=False, indent=2)
print("Successfully generated locales/es/live.json")

with open('locales/zh-Hans/live.json', 'w', encoding='utf-8') as f:
    json.dump(tree_zh, f, ensure_ascii=False, indent=2)
print("Successfully generated locales/zh-Hans/live.json")
