import json

en = json.load(open('locales/en/features.json'))
fa = json.load(open('locales/fa/features.json'))

# Let's inspect all keys and generate French translations
print(f"Loaded features with {len(en['detail'])} detail items.")
