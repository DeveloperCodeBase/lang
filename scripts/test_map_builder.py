import json

with open('scripts/group1_keys.json') as f:
    g1 = json.load(f)
with open('scripts/group2_keys.json') as f:
    g2 = json.load(f)

all_keys = {**g1, **g2}
print(f"Total keys to map: {len(all_keys)}")
