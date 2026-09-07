# -*- coding: utf-8 -*-
"""
Applica l'aggiornamento completo di data/stull-data.js:
1. Carica le 5 tranche pulite e accademiche (c1-c43).
2. Sostituisce integralmente chap.quiz (215 domande accademiche) e chap.examQuiz (129 domande per il simulatore d'esame).
3. Bilancia matematicamente la posizione della risposta corretta (correctIndex) in modo uniforme su 0, 1, 2, 3.
4. Preserva intatti tutti i riassunti, keyPoints, flashcard e domande aperte esistenti.
"""

import json

def balance_question(q, target_idx):
    cur_idx = q["correctIndex"]
    if cur_idx != target_idx:
        opts = list(q["options"])
        opts[cur_idx], opts[target_idx] = opts[target_idx], opts[cur_idx]
        q["options"] = opts
        q["correctIndex"] = target_idx
    return q

# Carica le 5 parti pulite
all_clean = {}
for p in range(1, 6):
    fname = f"scripts/stull_clean_part{p}.json"
    with open(fname, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_clean.update(data)

print(f"Caricate {len(all_clean)} capitoli puliti con successo.")

# Carica l'attuale data/stull-data.js
with open("data/stull-data.js", "r", encoding="utf-8") as f:
    raw = f.read()

start = raw.find('[')
end = raw.rfind(']') + 1
stull_chapters = json.loads(raw[start:end])

print(f"Caricati {len(stull_chapters)} capitoli da data/stull-data.js.")

q_dist = {0: 0, 1: 0, 2: 0, 3: 0}
eq_dist = {0: 0, 1: 0, 2: 0, 3: 0}
total_quiz = 0
total_exam = 0

for c_idx, chap in enumerate(stull_chapters):
    c_id = chap["id"]
    if c_id not in all_clean:
        print(f"ATTENZIONE: {c_id} non trovato nelle tranche pulite!")
        continue
    
    clean_data = all_clean[c_id]
    
    # Bilanciamento quiz (5 per capitolo)
    new_quiz = []
    for q_idx, q in enumerate(clean_data["quiz"]):
        target = (c_idx + q_idx) % 4
        bq = balance_question(dict(q), target)
        new_quiz.append(bq)
        q_dist[bq["correctIndex"]] += 1
        total_quiz += 1
    chap["quiz"] = new_quiz
    
    # Bilanciamento examQuiz (3 per capitolo)
    new_exam = []
    for eq_idx, eq in enumerate(clean_data["examQuiz"]):
        target = (c_idx + eq_idx + 1) % 4
        beq = balance_question(dict(eq), target)
        new_exam.append(beq)
        eq_dist[beq["correctIndex"]] += 1
        total_exam += 1
    chap["examQuiz"] = new_exam

# Scrittura del file aggiornato data/stull-data.js
output_js = "// Dati di studio approfonditi estratti da 'UX_Design_Stull_Riassunto_esame.pdf'\n"
output_js += "// 43 Capitoli completi con sintesi accademiche, storie-ancora, flashcard, quiz di studio e banco d'esame bilanciati.\n"
output_js += "window.STULL_DATA = " + json.dumps(stull_chapters, indent=2, ensure_ascii=False) + ";\n"

with open("data/stull-data.js", "w", encoding="utf-8") as f:
    f.write(output_js)

print("data/stull-data.js riscritto e salvato con successo!")
print(f"Totale Quiz di studio: {total_quiz}, Distribuzione: {q_dist}")
print(f"Totale Domande d'esame: {total_exam}, Distribuzione: {eq_dist}")
