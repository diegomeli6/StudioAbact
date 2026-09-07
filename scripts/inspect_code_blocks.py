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
    print(f"\n=================== {p} ===================")
    cb = re.findall(r'```[\s\S]*?```', content)
    for idx, b in enumerate(cb):
        print(f"--- CODE BLOCK {idx} ---")
        print(b[:200])
        print("...")
        print(b[-100:])
    formulas = re.findall(r'\$\$[\s\S]*?\$\$', content)
    for idx, form in enumerate(formulas):
        print(f"--- FORMULA {idx} ---")
        print(repr(form))
