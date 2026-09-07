import re

files = [
    'scripts/build_stull_p1_complete.py',
    'scripts/build_stull_p2_complete.py',
    'scripts/build_stull_p3_complete.py',
    'scripts/build_stull_p4_complete.py'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"=== {p} ===")
    cb = re.findall(r'```[\s\S]*?```', content)
    print(f"Code blocks found: {len(cb)}")
    for b in cb:
        print("  BLOCK:", repr(b[:60]), "... len:", len(b))
    formulas = re.findall(r'\$\$[\s\S]*?\$\$', content)
    print(f"$$ formulas found: {len(formulas)}")
    for form in formulas:
        print("  FORMULA:", repr(form))
    singles = re.findall(r'(?<!\$)\$([^\$\n]+)\$(?!\$)', content)
    print(f"Single $ found: {len(singles)}")
    for s in singles:
        if any(k in s for k in ['\\', 'approx', 'pm', 'log', 'times', 'cdot']):
            print("  MATH SINGLE:", repr(s))
