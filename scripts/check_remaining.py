import json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()
stull = json.loads(text[text.find('['):text.rfind(']')+1])

for num in [32, 34, 36]:
    c = next(c for c in stull if c['number'] == num)
    print(f"=== CAPITOLO {num} backticks ===")
    parts = c['summary'].split('```')
    for i in range(1, len(parts), 2):
        print(f"[{i}]:", repr(parts[i][:150]))
