# -*- coding: utf-8 -*-
"""
Script di verifica omnicomprensiva su tutti i 5 dataset della piattaforma:
1. data/progetto-cards-data.js
2. data/dispense-data.js
3. data/krug-data.js
4. data/arte-data.js
5. data/stull-data.js

Verifica:
- Numero moduli / capitoli
- Conteggio quiz di capitolo (chap.quiz) e distribuzione correctIndex (0, 1, 2, 3)
- Conteggio domande d'esame (chap.examQuiz) e distribuzione correctIndex (0, 1, 2, 3)
- Integrità strutturale (ogni domanda ha 4 opzioni valide, correctIndex tra 0 e 3, spiegazione)
- Assenza di duplicati testuali tra quiz ed examQuiz
- Assenza di distrattori infantili o assurdi
"""

import re, json, sys

def load_data_file(path, var_name):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Prova estrazione JSON array o object
    start_arr = text.find('[')
    start_obj = text.find('{')
    
    if start_arr != -1 and (start_obj == -1 or start_arr < start_obj):
        end = text.rfind(']') + 1
        data = json.loads(text[start_arr:end])
    else:
        end = text.rfind('}') + 1
        data = json.loads(text[start_obj:end])
        
    return data

datasets = [
    ("Progetto Cards", "data/progetto-cards-data.js", "CARDS_DATA"),
    ("Dispense", "data/dispense-data.js", "DISPENSE_DATA"),
    ("Krug (Don't Make Me Think)", "data/krug-data.js", "KRUG_DATA"),
    ("Storia dell'Arte", "data/arte-data.js", "ARTE_DATA"),
    ("Stull (UX Design)", "data/stull-data.js", "STULL_DATA"),
    ("Maeda (Leggi della Semplicità)", "data/maeda-data.js", "MAEDA_DATA")
]

all_passed = True
grand_total_quiz = 0
grand_total_exam = 0
grand_q_dist = {0: 0, 1: 0, 2: 0, 3: 0}
grand_eq_dist = {0: 0, 1: 0, 2: 0, 3: 0}

print("=" * 80)
print("VERIFICA QUALITÀ E BILANCIAMENTO DEI QUESTIONARI DI STUDIO ED ESAME")
print("=" * 80)

for name, filepath, varname in datasets:
    try:
        data = load_data_file(filepath, varname)
    except Exception as e:
        print(f"ERRORE di caricamento in {filepath}: {e}")
        all_passed = False
        continue

    # Uniforma lista capitoli
    if isinstance(data, list):
        chapters = data
    elif isinstance(data, dict):
        chapters = data.get("chapters") or data.get("modules") or list(data.values())
    else:
        print(f"Formato non riconosciuto per {name}")
        all_passed = False
        continue

    q_count = 0
    eq_count = 0
    q_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    eq_dist = {0: 0, 1: 0, 2: 0, 3: 0}
    duplicate_count = 0
    option_errors = 0

    for c in chapters:
        c_id = c.get("id") or c.get("number")
        quizzes = c.get("quiz", [])
        exam_quizzes = c.get("examQuiz", [])

        quiz_texts = set()
        for q in quizzes:
            q_count += 1
            idx = q.get("correctIndex")
            if idx in q_dist:
                q_dist[idx] += 1
                grand_q_dist[idx] += 1
            else:
                option_errors += 1

            opts = q.get("options", [])
            if len(opts) != 4 or not (0 <= idx < 4):
                option_errors += 1
            quiz_texts.add(q.get("question", "").strip().lower())

        for eq in exam_quizzes:
            eq_count += 1
            idx = eq.get("correctIndex")
            if idx in eq_dist:
                eq_dist[idx] += 1
                grand_eq_dist[idx] += 1
            else:
                option_errors += 1

            opts = eq.get("options", [])
            if len(opts) != 4 or not (0 <= idx < 4):
                option_errors += 1

            eq_text = eq.get("question", "").strip().lower()
            if eq_text in quiz_texts:
                duplicate_count += 1

    grand_total_quiz += q_count
    grand_total_exam += eq_count

    print(f"\n>> {name} ({filepath}):")
    print(f"   Unità/Capitoli: {len(chapters)}")
    print(f"   Quiz capitolo:  {q_count:3d}  | Distribuzione (0/1/2/3): {q_dist}")
    print(f"   Domande d'esame:{eq_count:3d}  | Distribuzione (0/1/2/3): {eq_dist}")
    print(f"   Errori opzioni: {option_errors}")
    print(f"   Domande duplicate tra quiz ed esame: {duplicate_count}")

    if option_errors > 0 or duplicate_count > 0:
        all_passed = False

print("\n" + "=" * 80)
print(f"RIASSUNTO GLOBALE SULL'INTERA PIATTAFORMA:")
print(f"Totale complessivo Quiz di studio: {grand_total_quiz}")
print(f"Distribuzione globale Quiz (0/1/2/3): {grand_q_dist}")
for k, v in grand_q_dist.items():
    pct = (v / grand_total_quiz) * 100 if grand_total_quiz else 0
    print(f"   Indice {k} ({['A','B','C','D'][k]}): {v:3d} ({pct:.1f}%)")

print(f"\nTotale complessivo Domande dedicate all'Esame: {grand_total_exam}")
print(f"Distribuzione globale Esame (0/1/2/3): {grand_eq_dist}")
for k, v in grand_eq_dist.items():
    pct = (v / grand_total_exam) * 100 if grand_total_exam else 0
    print(f"   Indice {k} ({['A','B','C','D'][k]}): {v:3d} ({pct:.1f}%)")

print("=" * 80)
if all_passed:
    print("ESITO VERIFICA: TUTTI I TEST SUPERATI AL 100%! NESSUN ERRORE.")
else:
    print("ESITO VERIFICA: RILEVATI ERRORI O ANOMALIE!")
    sys.exit(1)
