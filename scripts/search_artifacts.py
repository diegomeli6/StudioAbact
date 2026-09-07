import glob, re, json

files = sorted(glob.glob('data/*.js'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # search for $$
    latex = re.findall(r'(\$\$.*?\$\$)', content, re.DOTALL)
    if latex:
        print(f'{f}: trovati {len(latex)} blocchi LaTeX ($$):')
        for l in latex:
            print('   ->', l.replace('\n', ' '))
            
    # search for single $ math
    single_dollar = re.findall(r'(?<!\$)\$([^\$\n]+)\$(?!\$)', content)
    if single_dollar:
        print(f'{f}: trovati {len(single_dollar)} inline math ($...$):')
        for s in single_dollar[:5]:
            print('   -> $', s, '$')

    # search for backslash math commands like \text{, \frac{, \times
    math_cmds = re.findall(r'(\\[a-zA-Z]+\{[^}]+\})', content)
    if math_cmds:
        print(f'{f}: trovati {len(math_cmds)} comandi matematici LaTeX:')
        for m in math_cmds:
            print('   ->', m)

    # search for markdown code blocks in texts (outside cards data)
    if 'cards' not in f:
        code_blocks = re.findall(r'(```.*?```)', content, re.DOTALL)
        if code_blocks:
            print(f'{f}: trovati {len(code_blocks)} blocchi codice (```):')
            for cb in code_blocks[:5]:
                print('   ->', cb[:80].replace('\n', ' '))
