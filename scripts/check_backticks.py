import json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

for c in stull:
    s = c.get('summary', '')
    if '```' in s:
        print(f"Cap {c['number']}: {c['title']} ha blocchi codice (```)")
        parts = s.split('```')
        # ogni parte dispari è un blocco di codice
        for i in range(1, len(parts), 2):
            print(f"--- BLOCCO CODICE in Cap {c['number']} ---")
            print(parts[i][:300].strip())
            print("...")
