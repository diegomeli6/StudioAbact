# -*- coding: utf-8 -*-
"""
Assemblatore Master del Dataset di Fotografia Digitale
Prof. Carmelo Bongiorno - ABPR 31 (8 CFA)
Accademia di Belle Arti di Catania
DIVIETO ASSOLUTO DI EMOJI
"""

import os
import sys
import json
import re

from mod1_tecnica import get_mod1_chapters
from mod2_teoria import get_mod2_chapters
from mod3_autori import get_mod3_chapters
from mod4_maestri import get_mod4_chapters

WORKSPACE_ROOT = "/Users/diego/Altro/Studio"
IMAGES_DIR = os.path.join(WORKSPACE_ROOT, "assets/corsi/dapl08/anno-1/fotografia-digitale/images")
OUTPUT_FILE = os.path.join(WORKSPACE_ROOT, "data/fotografia-data.js")

def check_no_emojis(text):
    # Regex per intercettare caratteri emoji comuni ed estesi
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
        "\U00002600-\U000026FF"  # misc symbols
        "]+", flags=re.UNICODE
    )
    matches = emoji_pattern.findall(text)
    if matches:
        raise ValueError(f"ERRORE CRITICO: Trovate emoji non permesse: {matches}")

def main():
    print("Avvio assemblaggio Fotografia Digitale...")
    
    ch_m1 = get_mod1_chapters()
    ch_m2 = get_mod2_chapters()
    ch_m3 = get_mod3_chapters()
    ch_m4 = get_mod4_chapters()
    
    all_chapters = ch_m1 + ch_m2 + ch_m3 + ch_m4
    total_chapters = len(all_chapters)
    print(f"Capitoli totali caricati: {total_chapters}")
    assert total_chapters == 41, f"Attesi 41 capitoli, trovati {total_chapters}"
    
    fotografia_data = {
        "title": "Fotografia Digitale",
        "code": "ABPR 31",
        "credits": "8 CFA",
        "docente": "Prof. Carmelo Bongiorno",
        "anno": "1° Anno",
        "modules": [
            {
                "id": "foto-tecnica",
                "title": "1. Tecnica & Grammatica",
                "subtitle": "Formati, sensori, esposizione, ottiche, profondità di campo, ISO, Kelvin, illuminotecnica, RAW e portfolio",
                "chapters": [c["id"] for c in ch_m1]
            },
            {
                "id": "foto-teoria",
                "title": "2. Teoria & Inconscio",
                "subtitle": "Fotografia e inconscio, critica della patografia, morte e separazione, dentro-fuori e phototherapy",
                "chapters": [c["id"] for c in ch_m2]
            },
            {
                "id": "foto-autori",
                "title": "3. I 15 Autori Contemporanei",
                "subtitle": "D'Agata, Sank, Landreth, Minkkinen, Kozerski, Bolin, Carucci, Caruana, Markosian, Toledano, Ricci, Van Agtmael, Guidi, Ventura, Hido",
                "chapters": [c["id"] for c in ch_m3]
            },
            {
                "id": "foto-maestri",
                "title": "4. I Grandi Maestri Storici",
                "subtitle": "Cartier-Bresson, Eggleston, Ghirri, Giacomelli, Basilico, Becher, Gursky, Goldin, Sherman, Salgado, Parr",
                "chapters": [c["id"] for c in ch_m4]
            }
        ],
        "chapters": all_chapters
    }
    
    # Validazione approfondita
    total_quizzes = 0
    total_flashcards = 0
    
    img_regex = re.compile(r"!\[(.*?)\]\((.*?)\)")
    found_images = []
    
    for i, ch in enumerate(all_chapters, start=1):
        assert ch["number"] == i, f"Capitolo ID {ch['id']} numero errato: {ch['number']} != {i}"
        assert len(ch["flashcards"]) == 5, f"Capitolo {i} ha {len(ch['flashcards'])} flashcards (attese 5)"
        assert len(ch["quiz"]) == 5, f"Capitolo {i} ha {len(ch['quiz'])} quiz (attesi 5)"
        assert len(ch["keyPoints"]) >= 4, f"Capitolo {i} ha pochi punti chiave"
        
        total_flashcards += len(ch["flashcards"])
        total_quizzes += len(ch["quiz"])
        
        for q in ch["quiz"]:
            assert "question" in q and len(q["question"]) > 10
            assert "options" in q and len(q["options"]) == 4
            assert "correctIndex" in q and 0 <= q["correctIndex"] <= 3
            assert "explanation" in q and len(q["explanation"]) > 10
            
        for fc in ch["flashcards"]:
            assert "question" in fc and len(fc["question"]) > 5
            assert "answer" in fc and len(fc["answer"]) > 5
            
        # Ricerca immagini nel summary
        for m in img_regex.finditer(ch["summary"]):
            src = m.group(2)
            found_images.append((ch["id"], src))
            
    print(f"Quiz totali validati: {total_quizzes}")
    print(f"Flashcard totali validate: {total_flashcards}")
    print(f"Immagini referenziate nel markdown: {len(found_images)}")
    
    # Verifica esistenza fisica delle immagini su disco
    for ch_id, src in found_images:
        # src è tipo assets/corsi/dapl08/anno-1/fotografia-digitale/images/dagata_stigma.jpg
        full_path = os.path.join(WORKSPACE_ROOT, src)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Immagine non trovata per {ch_id}: {full_path}")
    print("Tutte le immagini referenziate esistono fisicamente su disco!")
    
    # Conversione in JSON
    json_str = json.dumps(fotografia_data, ensure_ascii=False, indent=2)
    
    # Controllo severo assenza emoji
    check_no_emojis(json_str)
    print("Controllo DIVIETO ASSOLUTO DI EMOJI superato con successo: ZERO emoji trovate!")
    
    # Scrittura file data/fotografia-data.js
    js_content = f"window.FOTOGRAFIA_DATA = {json_str};\n"
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"File salvato con successo: {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)")

if __name__ == "__main__":
    main()
