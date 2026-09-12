# -*- coding: utf-8 -*-
import json, re

# Let extract all chapters by parsing the python files or importing them
files = [
    ("scripts/mod1_data.py", ["arte1-c1", "arte1-c2", "arte1-c3"]),
    ("scripts/build_mod1.py", ["arte1-c4"]),
    ("scripts/append_mod1_part2.py", ["arte1-c5", "arte1-c6"]),
    ("scripts/append_mod1_part3.py", ["arte1-c7", "arte1-c8"]),
    ("scripts/append_mod1_part4.py", ["arte1-c9", "arte1-c10"]),
    ("scripts/append_mod1_part5.py", ["arte1-c11", "arte1-c12"]),
    ("scripts/append_mod1_part6.py", ["arte1-c13", "arte1-c14"]),
    ("scripts/append_mod1_final.py", ["arte1-c15", "arte1-c16", "arte1-c17"]),
]

all_chaps = []

for fpath, ids in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    # Find dictionaries in content
    # Each chapter starts with chaps.append({\n    "id": "arte1-c...
    # or chapters.append({\n    "id": ...
    for cid in ids:
        pattern = r"(?:chaps|chapters)\.append\((\{[\s\S]*?\"id\":\s*\"" + cid + r"\"[\s\S]*?\n\})\)"
        match = re.search(pattern, content)
        if match:
            dict_str = match.group(1)
            # Evaluate dict
            local_vars = {"partNum": 1, "partTitle": "1. Arte Contemporanea Anni '50: Informale, Espressionismo Astratto e Spazialismo", "module": "anni50"}
            chap = eval(dict_str, {}, local_vars)
            all_chaps.append(chap)
            print(f"Loaded {cid}: {chap['title']}")
        else:
            print(f"FAILED to match {cid} in {fpath}")

print(f"\nTotal chapters loaded for Modulo 1: {len(all_chaps)}")

with open("scripts/mod1_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("# Modulo 1 Completo: Anni Cinquanta (Capitoli 1 - 17)\n\n")
    f.write("import json\n\n")
    f.write("partNum = 1\n")
    f.write("partTitle = \"1. Arte Contemporanea Anni '50: Informale, Espressionismo Astratto e Spazialismo\"\n")
    f.write("module = \"anni50\"\n\n")
    f.write("_CHAPS = " + json.dumps(all_chaps, ensure_ascii=False, indent=4) + "\n\n")
    f.write("def get_mod1_chapters():\n")
    f.write("    return _CHAPS\n")

print("Successfully generated clean scripts/mod1_data.py with all 17 chapters!")
