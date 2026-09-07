import json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

c33 = next(c for c in stull if c['number'] == 33)
print("=== CAPITOLO 33 SUMMARY ===")
print(c33['summary'])
