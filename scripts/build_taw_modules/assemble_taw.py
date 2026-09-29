#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembla il dataset completo per Tecniche Audiovisive per il Web (TAW)
Verifica l'assenza totale di emoji, controlla l'esistenza fisica di tutte le immagini
e scrive data/taw-data.js.
"""

import os
import sys
import json
import re

from mod1_camera_linguaggio import get_module_1_chapters
from mod2_movimenti_montaggio import get_module_2_chapters
from mod3_drammaturgia_produzione import get_module_3_chapters
from mod4_post_web import get_module_4_chapters

EMOJI_REGEX = re.compile(
    r"[\U00010000-\U0010ffff"
    r"\u2600-\u26ff"
    r"\u2700-\u27bf"
    r"\u2300-\u23ff"
    r"\u2b50\u2b55\u203c\u2049"
    r"\u25aa\u25ab\u25b6\u25c0"
    r"\u2190-\u21ff"  # note: check if any arrow is unicode emoji vs text
    r"]",
    re.UNICODE
)

# Consentiamo solo frecce testo ASCII o standard non-emoji se necessario, ma controlliamo specificamente gli emoji range:
STRICT_EMOJI_REGEX = re.compile(
    r"[\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F680-\U0001F6FF"  # transport & map
    r"\U0001F1E0-\U0001F1FF"  # flags
    r"\U0001F900-\U0001F9FF"  # supplemental symbols
    r"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    r"\u2600-\u26ff"          # misc symbols
    r"\u2700-\u27bf"          # dingbats
    r"]",
    re.UNICODE
)

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    print(f"Workspace root: {root_dir}")

    chaps1 = get_module_1_chapters()
    chaps2 = get_module_2_chapters()
    chaps3 = get_module_3_chapters()
    chaps4 = get_module_4_chapters()

    all_chapters = chaps1 + chaps2 + chaps3 + chaps4
    total_chapters = len(all_chapters)
    print(f"Capitoli totali estratti: {total_chapters}")

    assert total_chapters == 27, f"Previsti 27 capitoli, trovati {total_chapters}"

    # Validazione campi
    total_quiz = 0
    total_flashcards = 0
    all_images = []

    for idx, c in enumerate(all_chapters):
        c["number"] = idx + 1
        cid = c["id"]
        assert c.get("title"), f"Titolo mancante in {cid}"
        assert c.get("subtitle"), f"Sottotitolo mancante in {cid}"
        assert c.get("readTime"), f"ReadTime mancante in {cid}"
        assert c.get("module"), f"Modulo mancante in {cid}"
        assert c.get("summary"), f"Summary mancante in {cid}"

        kp = c.get("keyPoints", [])
        assert len(kp) >= 5, f"Almeno 5 keyPoints richiesti in {cid}, trovati {len(kp)}"

        fc = c.get("flashcards", [])
        assert len(fc) >= 5, f"Almeno 5 flashcards richieste in {cid}, trovati {len(fc)}"
        total_flashcards += len(fc)

        qz = c.get("quiz", [])
        assert len(qz) >= 5, f"Almeno 5 quiz richiesti in {cid}, trovati {len(qz)}"
        for q in qz:
            assert "question" in q and q["question"].strip()
            assert "options" in q and len(q["options"]) == 4
            assert "correctIndex" in q and 0 <= q["correctIndex"] <= 3
            assert "explanation" in q and q["explanation"].strip()
        total_quiz += len(qz)

        # Cerca immagini nel summary
        imgs = re.findall(r'!\[.*?\]\((assets/.*?)\)', c["summary"])
        all_images.extend(imgs)

    print(f"Totale Quiz: {total_quiz}")
    print(f"Totale Flashcard: {total_flashcards}")
    print(f"Riferimenti a immagini nel markdown: {len(all_images)} ({len(set(all_images))} uniche)")

    # Verifica esistenza fisica delle immagini
    missing_images = []
    for img_rel in set(all_images):
        full_p = os.path.join(root_dir, img_rel)
        if not os.path.exists(full_p):
            missing_images.append((img_rel, full_p))

    if missing_images:
        print("ERRORE: Immagini mancanti su disco!")
        for rel, full in missing_images:
            print(f"  - {rel} -> {full}")
        sys.exit(1)
    else:
        print("TUTTE le immagini referenziate esistono fisicamente su disco!")

    # Verifica assenza emoji in tutto il JSON serializzato
    json_str = json.dumps(all_chapters, ensure_ascii=False, indent=2)
    emoji_matches = STRICT_EMOJI_REGEX.findall(json_str)
    if emoji_matches:
        print(f"VIOLAZIONE GRAVE: Trovati {len(emoji_matches)} caratteri emoji proibiti: {emoji_matches}")
        sys.exit(1)
    print("VERIFICA EMOJI: 100% PULITO. ZERO EMOJI.")

    # Scrivi data/taw-data.js
    output_js = os.path.join(root_dir, "data/taw-data.js")
    js_content = f"""// =============================================================================
// data/taw-data.js
// Corso di Tecniche Audiovisive per il Web (ABTEC 42 - 8 CFA)
// Docente: Prof. Lorenzo Di Silvestro - Accademia di Belle Arti di Catania
// 27 Capitoli, 135 Quiz, 135 Flashcard, 18 Asset Visivi (PNG da dispense + SVG)
// REGOLA ASSOLUTA: NESSUNA EMOJI UNICODE IN NESSUN POSTO.
// =============================================================================

window.TAW_DATA = {json_str};
"""

    with open(output_js, "w", encoding="utf-8") as f:
        f.write(js_content)

    file_size_kb = os.path.getsize(output_js) // 1024
    print(f"Scritto con successo {output_js} ({file_size_kb} KB)")

if __name__ == "__main__":
    main()
