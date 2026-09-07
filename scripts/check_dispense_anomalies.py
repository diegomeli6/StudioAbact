import json, re

with open('data/dispense-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
disp = json.loads(text[start:end])

for c in disp:
    s = c.get('summary', '')
    cid = c.get('id')
    num = c.get('number')
    title = c.get('title')
    
    # Cerca $$, comandi LaTeX o ```
    latex_matches = re.findall(r'(\$\$[\s\S]*?\$\$|\\text\{[^}]+\}|\$[^$\n]+\$)', s)
    code_matches = re.findall(r'```([\s\S]*?)```', s)
    
    if latex_matches or code_matches:
        print(f"\n[DISPENSE Cap {num}: {title}] ({cid})")
        if latex_matches:
            print("   LATEX:")
            for m in latex_matches:
                print("      >>>", m.replace('\n', ' '))
        if code_matches:
            print("   CODE BLOCKS:")
            for b in code_matches:
                first_line = b.strip().split('\n')[0]
                print(f"      >>> ```{first_line}... ({len(b.splitlines())} righe)```")
