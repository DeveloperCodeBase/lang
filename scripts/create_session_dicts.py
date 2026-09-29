import json

g2 = json.load(open('scripts/group2_keys.json'))
sess_keys = {k: v['en'] for k, v in g2.items() if k.startswith('session.')}
print(f"Total session keys: {len(sess_keys)}")

# Let's inspect some sample keys
for k in sorted(list(sess_keys.keys()))[:15]:
    print(f"{k}: {sess_keys[k]}")
