# -*- coding: utf-8 -*-
"""
Assemblatore unificato per il dataset completo di Edward Stull - UX Design (Capitoli 1 to 43).
Fonde Parte I, Parte II, Parte III e Parte IV con validazione rigorosa dello schema.
Genera data/stull-data.js.
"""

import json

with open('scripts/stull_part1_complete.json', encoding='utf-8') as f:
    p1 = json.load(f)

with open('scripts/stull_part2_complete.json', encoding='utf-8') as f:
    p2 = json.load(f)

with open('scripts/stull_part3_complete.json', encoding='utf-8') as f:
    p3 = json.load(f)

with open('scripts/stull_part4_complete.json', encoding='utf-8') as f:
    p4 = json.load(f)

all_chapters = p1 + p2 + p3 + p4

print(f"Totale capitoli uniti: {len(all_chapters)}")

# Validazione rigorosa
assert len(all_chapters) == 43, f"Errore: attesi 43 capitoli, trovati {len(all_chapters)}"

for idx, ch in enumerate(all_chapters, start=1):
    assert ch["number"] == idx, f"Errore numerazione capitolo: atteso {idx}, trovato {ch['number']}"
    assert ch["id"] == f"stull-c{idx}", f"Errore ID capitolo: atteso stull-c{idx}, trovato {ch['id']}"
    assert len(ch["summary"]) > 2500, f"Capitolo {idx} summary troppo breve ({len(ch['summary'])} caratteri)"
    assert len(ch["keyPoints"]) >= 5, f"Capitolo {idx} keyPoints insufficienti ({len(ch['keyPoints'])})"
    assert len(ch["flashcards"]) >= 3, f"Capitolo {idx} flashcards insufficienti ({len(ch['flashcards'])})"
    assert len(ch["quiz"]) == 5, f"Capitolo {idx} quiz errato ({len(ch['quiz'])})"
    assert len(ch["examQuiz"]) == 3, f"Capitolo {idx} examQuiz errato ({len(ch['examQuiz'])})"
    assert len(ch["openQuestions"]) >= 1, f"Capitolo {idx} openQuestions mancante ({len(ch['openQuestions'])})"
    assert len(ch["anchorTitle"]) > 0, f"Capitolo {idx} anchorTitle mancante"
    assert len(ch["anchorText"]) > 0, f"Capitolo {idx} anchorText mancante"

print("Tutti i 43 capitoli hanno superato la validazione formale dello schema.")

# Generazione del file JavaScript
js_content = "// Dati di studio completi e approfonditi estratti da 'UX_Design_Stull_Riassunto_esame.pdf'\n"
js_content += "// 43 Capitoli integrali con sintesi accademiche, storie-ancora, concetti, leggi, flashcard, quiz e banchi d'esame.\n"
js_content += "window.STULL_DATA = " + json.dumps(all_chapters, ensure_ascii=False, indent=2) + ";\n"

with open('data/stull-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"File data/stull-data.js generato con successo! ({len(js_content)} caratteri, {len(js_content.encode('utf-8'))} bytes)")
