import json, os

fa = json.load(open('locales/fa/live.json'))
en = json.load(open('locales/en/live.json'))

print(f"FA keys: {len(fa)}, EN keys: {len(en)}")
