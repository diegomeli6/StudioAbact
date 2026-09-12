# -*- coding: utf-8 -*-
"""
Assemblatore finale per data/arte1-data.js
Unifica i 56 capitoli accademici di Storia dell'Arte Contemporanea 1:
- Modulo 1 (Anni '50): 17 capitoli
- Modulo 2 (Anni '60): 23 capitoli
- Modulo 3 (Anni '70): 13 capitoli
- Modulo 4 (Monografie): 3 capitoli
Totale: 56 capitoli, 280 flashcard, 560 quiz con spiegazioni filologiche.
Verifica assenza assoluta di emoji e validità dei percorsi immagini.
"""
import os
import json
import re

import mod1_data
import mod2_data
import mod3_data
import build_mod4_full

def assemble():
    all_chapters = []
    
    m1 = mod1_data.get_mod1_chapters()
    m2 = mod2_data.get_mod2_chapters()
    m3 = mod3_data.get_mod3_chapters()
    m4 = build_mod4_full.get_mod4_chapters()
    
    print(f"Mod1: {len(m1)} chaps")
    print(f"Mod2: {len(m2)} chaps")
    print(f"Mod3: {len(m3)} chaps")
    print(f"Mod4: {len(m4)} chaps")
    
    all_chapters.extend(m1)
    all_chapters.extend(m2)
    all_chapters.extend(m3)
    all_chapters.extend(m4)
    
    total = len(all_chapters)
    print(f"Total chapters assembled: {total}")
    assert total == 56, f"Expected 56 chapters, got {total}"
    
    # Check numbering and uniqueness of IDs
    seen_ids = set()
    for idx, c in enumerate(all_chapters, start=1):
        c['number'] = idx
        expected_id = f"arte1-c{idx}"
        if c['id'] != expected_id:
            print(f"Adjusting ID for chapter {idx}: {c['id']} -> {expected_id}")
            c['id'] = expected_id
        if c['id'] in seen_ids:
            raise ValueError(f"Duplicate chapter ID: {c['id']}")
        seen_ids.add(c['id'])
    
    # EMOJI CHECK
    emoji_pattern = re.compile(
        r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]|[\u25aa-\u25fe]"
    )
    
    # Validate image paths
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    missing_images = []
    
    for c in all_chapters:
        # Check text fields for emojis
        text_to_check = json.dumps(c, ensure_ascii=False)
        emojis_found = emoji_pattern.findall(text_to_check)
        if emojis_found:
            raise ValueError(f"EMOJI VIOLATION in chapter {c['id']}: {emojis_found}")
            
        # Check markdown images
        img_matches = re.findall(r'!\[.*?\]\((.*?)\)', c['summary'])
        for img in img_matches:
            full_img_path = os.path.join(root_dir, img)
            if not os.path.exists(full_img_path):
                missing_images.append((c['id'], img, full_img_path))
                
    if missing_images:
        print("WARNING: The following referenced images were not found on disk:")
        for ch_id, rel_path, full_path in missing_images:
            print(f"  [{ch_id}] {rel_path} -> {full_path}")
    else:
        print("All referenced images verified on disk successfully!")
        
    # Write to data/arte1-data.js
    out_path = os.path.join(root_dir, "data", "arte1-data.js")
    js_content = "/**\n"
    js_content += " * Archivio Dati Didattici Accademici - Storia dell'Arte Contemporanea 1\n"
    js_content += " * Corso DAPL08 - 1° Anno - Prof.ssa Ambra Stazzone\n"
    js_content += " * Struttura in 4 Moduli Monografici e Tematici (56 Capitoli completi)\n"
    js_content += " * Zero emoji - Riferimenti storiografici e apparati iconografici integrati\n"
    js_content += " */\n\n"
    js_content += "window.ARTE1_DATA = " + json.dumps(all_chapters, ensure_ascii=False, indent=2) + ";\n"
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"File data/arte1-data.js written successfully ({len(js_content)} bytes).")

if __name__ == '__main__':
    assemble()
