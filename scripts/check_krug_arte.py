import json, re

print("=== KRUG DATA ===")
with open('data/krug-data.js', 'r', encoding='utf-8') as f:
    text = f.read()
start = text.find('{')
end = text.rfind('}') + 1
# krug is an object with 'chapters' dictionary
import json
krug = json.loads(text[start:end])
for cid, c in krug.get('chapters', {}).items():
    s = c.get('summary', '')
    latex = re.findall(r'(\$\$[\s\S]*?\$\$|\\text\{[^}]+\}|\$[^$\n]+\$)', s)
    code = re.findall(r'```([\s\S]*?)```', s)
    if latex or code:
        print(f"[{cid}: {c.get('title')}] latex: {len(latex)}, code: {len(code)}")

print("\n=== ARTE DATA ===")
with open('data/arte-data.js', 'r', encoding='utf-8') as f:
    text = f.read()
start = text.find('[')
end = text.rfind(']') + 1
arte = json.loads(text[start:end])
for c in arte:
    s = c.get('summary', '')
    latex = re.findall(r'(\$\$[\s\S]*?\$\$|\\text\{[^}]+\}|\$[^$\n]+\$)', s)
    code = re.findall(r'```([\s\S]*?)```', s)
    if latex or code:
        print(f"[{c.get('id')}: {c.get('title')}] latex: {len(latex)}, code: {len(code)}")
        if code:
            for b in code:
                print("   CODE BLOCK:", b.strip()[:100].replace('\n', ' '))
