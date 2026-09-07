import glob, re, json

with open('data/stull-data.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

print("=== STULL-DATA ISPEZIONI DETTAGLIATE ===")
for c in stull:
    cid = c['id']
    num = c['number']
    title = c['title']
    summary = c.get('summary', '')
    
    # Cerca $$ o comandi LaTeX o ```
    latex_matches = re.findall(r'(\$\$[\s\S]*?\$\$|\\text\{[^}]+\}|\$[^$\n]+\$)', summary)
    code_matches = re.findall(r'```([\s\S]*?)```', summary)
    
    if latex_matches or code_matches:
        print(f"\n[Capitolo {num}: {title}] ({cid})")
        if latex_matches:
            print("   LATEX / FORMULE TROVATE:")
            for m in latex_matches:
                print("      >>>", m.replace('\n', ' '))
        if code_matches:
            print("   BLOCCHI CODICE TROVATI:")
            for b in code_matches:
                first_line = b.strip().split('\n')[0]
                print(f"      >>> ```{first_line}... ({len(b.splitlines())} righe)```")
