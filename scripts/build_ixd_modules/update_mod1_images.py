#!/usr/bin/env python3
# -*- coding: utf-8 -*-

FILE_PATH = "/Users/diego/Altro/Studio/scripts/build_ixd_modules/mod1_fondamenti_design_thinking.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if '"id": "ixd-c2",' in line:
        pass
    # We can detect "module": "ixd-fondamenti-design-thinking" after each chapter ID
    # and insert the image field if not already present.

# Let's do a structured regex replacement on the full string
content = "".join(lines)

image_map = {
    "ixd-c1": "schema_interaction_matrix.svg",
    "ixd-c2": "design_thinking_fasi.png",
    "ixd-c3": "schema_design_thinking_diamond.svg",
    "ixd-c4": "interaction_matrix_raw.png",
    "ixd-c5": "design_thinking_iterativo.png",
    "ixd-c6": "peak_end_rule.png",
    "ixd-c7": "esperienza_fasi.png",
}

for cid, img in image_map.items():
    pattern = f'("id": "{cid}",.*?("module": "ixd-fondamenti-design-thinking",))'
    # Check if image already exists
    if f'"image": "assets/corsi/dapl08/anno-1/interaction-design/images/{img}"' not in content:
        import re
        def repl(match):
            return match.group(1) + f'\n            "image": "assets/corsi/dapl08/anno-1/interaction-design/images/{img}",'
        content = re.sub(f'("id": "{cid}".*?"module": "ixd-fondamenti-design-thinking",)', repl, content, count=1, flags=re.DOTALL)
        print(f"Aggiornato {cid} con {img}")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("mod1_fondamenti_design_thinking.py aggiornato con successo!")
