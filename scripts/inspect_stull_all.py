import json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()
stull = json.loads(text[text.find('['):text.rfind(']')+1])

def inspect_chapter(num):
    c = next(c for c in stull if c['number'] == num)
    print(f"\n==================== STULL CAP {num}: {c['title']} ====================")
    print(c['summary'])

for n in [9, 10, 15, 16, 23, 26, 29, 32, 33, 34, 36, 38, 39, 40, 42]:
    inspect_chapter(n)
