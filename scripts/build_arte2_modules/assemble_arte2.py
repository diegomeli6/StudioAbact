# -*- coding: utf-8 -*-
"""
Assembliamo tutti i 21 capitoli in data/arte-data.js
Verifica rigorosa di sintassi, emoji, campi obbligatori.
"""

import os, sys, json, re

from scripts.build_arte2_modules.mod1_anni80 import CHAPTERS_MOD1
from scripts.build_arte2_modules.mod2_anni90 import CHAPTERS_MOD2
from scripts.build_arte2_modules.mod3_duemila import CHAPTERS_MOD3
from scripts.build_arte2_modules.mod4_monografie import CHAPTERS_MOD4

all_chapters = CHAPTERS_MOD1 + CHAPTERS_MOD2 + CHAPTERS_MOD3 + CHAPTERS_MOD4

print(f"Totale capitoli da assemblare: {len(all_chapters)}")
assert len(all_chapters) == 21, f"Errore: attesi 21 capitoli, trovati {len(all_chapters)}"

# Pattern per controllo assoluto emoji
EMOJI_PATTERN = re.compile(
    "[\U00010000-\U0010ffff\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF]",
    flags=re.UNICODE
)

total_quizzes = 0
total_flashcards = 0

for idx, c in enumerate(all_chapters):
    expected_num = idx + 1
    expected_id = f"arte-c{expected_num}"
    assert c["number"] == expected_num, f"Capitolo {idx} ha number {c['number']}, atteso {expected_num}"
    assert c["id"] == expected_id, f"Capitolo {idx} ha id {c['id']}, atteso {expected_id}"
    
    # Campi obbligatori
    for req in ["id", "number", "partNum", "partTitle", "module", "title", "subtitle", "readTime", "summary", "keyPoints", "flashcards", "openQuestions", "quiz"]:
        assert req in c, f"Manca campo {req} nel capitolo {c['id']}"
        assert c[req], f"Campo vuoto {req} nel capitolo {c['id']}"
    
    # Aggiungi examQuiz come copia o alias per consistenza con core.js
    c["examQuiz"] = c["quiz"]
    
    # Contatori
    total_quizzes += len(c["quiz"])
    total_flashcards += len(c["flashcards"])
    
    # Controllo emoji in tutto il capitolo
    serialized = json.dumps(c, ensure_ascii=False)
    m = EMOJI_PATTERN.search(serialized)
    if m:
        raise ValueError(f"EMOJI RILEVATA nel capitolo {c['id']}: {m.group(0)}")

print(f"Verifica completata con successo: {len(all_chapters)} capitoli, {total_quizzes} quiz, {total_flashcards} flashcard.")
print("Nessuna emoji rilevata nel dataset!")

# Generazione file JS
output_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "arte-data.js")
output_path = os.path.abspath(output_path)

js_content = "window.ARTE_DATA = " + json.dumps(all_chapters, ensure_ascii=False, indent=2) + ";\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"File scritto con successo in: {output_path}")
print(f"Dimensione file generato: {os.path.getsize(output_path)} bytes")
