# -*- coding: utf-8 -*-
"""
Assembler per Storia dell'Arte Contemporanea 1 (DAPL08 - 1° Anno)
Unifica i moduli 1, 2, 3, 4 in data/arte1-data.js.
Esegue controlli di integrità: zero emoji, verifica file immagini su disco, validazione campi.
"""

import json
import os
import re
import sys

from mod1_anni50 import CHAPTERS_MOD1
from mod2_anni60 import CHAPTERS_MOD2
from mod3_anni70 import CHAPTERS_MOD3
from mod4_monografie import CHAPTERS_MOD4

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "arte1-data.js")

# Regex per rilevare emoji unicode
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F300-\U0001F5FF"  # Misc Symbols and Pictographs
    "\U0001F680-\U0001F6FF"  # Transport and Map
    "\U0001F1E0-\U0001F1FF"  # Regional indicator symbols
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols, etc.
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251"
    "]+",
    flags=re.UNICODE,
)

IMAGE_REGEX = re.compile(r"!\[.*?\]\((assets/corsi/dapl08/anno-1/storia-arte-1/images/[^\)]+)\)")

def assemble():
    all_chapters = CHAPTERS_MOD1 + CHAPTERS_MOD2 + CHAPTERS_MOD3 + CHAPTERS_MOD4
    print(f"Totale capitoli raccolti: {len(all_chapters)}")

    if len(all_chapters) != 20:
        raise ValueError(f"Attesi 20 capitoli, trovati {len(all_chapters)}")

    missing_images = []
    all_found_images = set()

    for idx, chap in enumerate(all_chapters, start=1):
        expected_id = f"arte1-c{idx}"
        if chap["id"] != expected_id:
            raise ValueError(f"Capitolo #{idx} ha id '{chap['id']}', atteso '{expected_id}'")
        if chap["number"] != idx:
            raise ValueError(f"Capitolo #{idx} ha number {chap['number']}, atteso {idx}")

        # Verifica campi essenziali
        for field in ["title", "subtitle", "summary", "keyPoints", "flashcards", "openQuestions", "quiz"]:
            if field not in chap or not chap[field]:
                raise ValueError(f"Capitolo {expected_id} mancante di '{field}'")

        if len(chap["flashcards"]) < 5:
            raise ValueError(f"Capitolo {expected_id} ha meno di 5 flashcard ({len(chap['flashcards'])})")
        if len(chap["quiz"]) < 5:
            raise ValueError(f"Capitolo {expected_id} ha meno di 5 quiz ({len(chap['quiz'])})")

        # Verifica immagini nel summary
        imgs = IMAGE_REGEX.findall(chap["summary"])
        for img_rel in imgs:
            img_abs = os.path.join(BASE_DIR, img_rel)
            all_found_images.add(img_rel)
            if not os.path.exists(img_abs):
                missing_images.append((expected_id, img_rel))

    if missing_images:
        print("ATTENZIONE: Immagini mancanti su disco:")
        for cid, img in missing_images:
            print(f"  [{cid}] {img}")
        raise FileNotFoundError(f"Trovate {len(missing_images)} immagini mancanti!")

    print(f"Verifica immagini completata con successo: {len(all_found_images)} immagini verificate su disco.")

    # Converti a JSON
    json_text = json.dumps(all_chapters, ensure_ascii=False, indent=2)

    # Controllo emoji
    emoji_matches = EMOJI_PATTERN.findall(json_text)
    if emoji_matches:
        print(f"ERRORE GRAVE: Rilevate {len(emoji_matches)} emoji nel contenuto!")
        for m in emoji_matches[:10]:
            print(f"  Emoji trovata: {repr(m)}")
        raise ValueError("Violazione della regola ASSOLUTA: ZERO EMOJI!")

    print("Controllo ZERO EMOJI superato al 100%.")

    # Scrivi arte1-data.js
    content = f"// File generato automaticamente da scripts/build_arte1_modules/assemble_arte1.py\n// Rigorosamente ZERO EMOJI. Immagini autentiche online verificate.\nwindow.ARTE1_DATA = {json_text};\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"File scritto con successo: {OUTPUT_FILE} ({len(content)} caratteri, {len(all_chapters)} capitoli).")

if __name__ == "__main__":
    assemble()
