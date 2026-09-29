#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembla i 4 moduli di Interaction Design (IxD) in data/interaction-data.js
Verifica l'assenza totale di emoji, la validita di tutti i path immagine e la completezza didattica.
"""

import os
import sys
import json
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mod1_fondamenti_design_thinking import get_module_1_chapters
from mod2_user_research import get_module_2_chapters
from mod3_teoria_sociologia import get_module_3_chapters
from mod4_strumenti_prototipazione import get_module_4_chapters

WORKSPACE_ROOT = "/Users/diego/Altro/Studio"
OUTPUT_FILE = os.path.join(WORKSPACE_ROOT, "data/interaction-data.js")

def main():
    print("=== ASSEMBLAGGIO INTERACTION DESIGN (IxD) ===")
    
    m1 = get_module_1_chapters()
    m2 = get_module_2_chapters()
    m3 = get_module_3_chapters()
    m4 = get_module_4_chapters()
    
    all_chapters = m1 + m2 + m3 + m4
    print(f"Capitoli totali caricati: {len(all_chapters)}")
    
    # 1. Verifica numerazione sequenziale
    for idx, chap in enumerate(all_chapters, 1):
        if chap["number"] != idx:
            print(f"ERRORE NUMERAZIONE: Capitolo {chap['id']} ha numero {chap['number']}, atteso {idx}")
            sys.exit(1)
            
    # 2. Verifica Flashcards e Quiz
    total_flashcards = sum(len(c["flashcards"]) for c in all_chapters)
    total_quiz = sum(len(c["quiz"]) for c in all_chapters)
    print(f"Flashcards totali: {total_flashcards} (attese 140)")
    print(f"Quiz totali: {total_quiz} (attesi 140)")
    
    if total_flashcards != 140 or total_quiz != 140:
        print("ATTENZIONE: Conteggio quiz o flashcards difforme da 140!")
        
    # 3. Verifica esistenza file immagini
    missing_images = []
    checked_images = 0
    for chap in all_chapters:
        img = chap.get("image")
        if img:
            full_path = os.path.join(WORKSPACE_ROOT, img)
            checked_images += 1
            if not os.path.exists(full_path):
                missing_images.append((chap["id"], img, full_path))
                
    print(f"Immagini collegate verificate: {checked_images}")
    if missing_images:
        print("ERRORE IMMAGINI MANCANTI:")
        for cid, img, fp in missing_images:
            print(f"  - [{cid}] {img} -> NON ESISTE sul disco ({fp})")
        sys.exit(1)
    else:
        print("Tutte le immagini collegate esistono fisicamente sul disco!")

    # 4. Validazione Assoluta Zero Emoji
    emoji_regex = re.compile(
        r'[\U00010000-\U0010ffff\u2600-\u27bf\u2300-\u23ff\u2b50\ufe0f]'
    )
    
    json_str = json.dumps(all_chapters, ensure_ascii=False, indent=2)
    emojis_found = emoji_regex.findall(json_str)
    if emojis_found:
        print(f"ERRORE GRAVE: Trovate {len(emojis_found)} emoji nel dataset IxD!")
        print(f"Emoji rilevate: {set(emojis_found)}")
        sys.exit(1)
    print("VALIDAZIONE ZERO EMOJI: 100% SUPERATA! Nessun carattere emoji nel dataset.")

    # 5. Scrittura del file data/interaction-data.js
    header = """// =============================================================================
// data/interaction-data.js
// Corso di Interaction Design (ABTEC 42 - 8 CFA)
// Docente: Prof. Giulio Interlandi - Accademia di Belle Arti di Catania
// 28 Capitoli, 140 Quiz, 140 Flashcard, 15 Asset Visivi (PNG da dispense + SVG)
// REGOLA ASSOLUTA: NESSUNA EMOJI UNICODE IN NESSUN POSTO.
// =============================================================================

window.INTERACTION_DATA = """

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(header + json_str + ";\n")
        
    file_size_kb = os.path.getsize(OUTPUT_FILE) / 1024
    print(f"File {OUTPUT_FILE} generato con successo! ({file_size_kb:.1f} KB)")
    print("=== ASSEMBLAGGIO COMPLETATO CON SUCCESSO! ===")

if __name__ == "__main__":
    main()
