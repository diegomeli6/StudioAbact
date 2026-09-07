import json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

chaps = [32, 34, 36, 38, 39, 40, 42]
for num in chaps:
    c = next(c for c in stull if c['number'] == num)
    print(f"=== CAPITOLO {num}: {c['title']} ===")
    for b in re.findall(r'```([\s\S]*?)```', c['summary']):
        print(b)
        print("-" * 50)
