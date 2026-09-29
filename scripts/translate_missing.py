import json

with open('scripts/missing_364.json') as f:
    missing = json.load(f)

print(f"Loaded {len(missing)} keys to translate")
