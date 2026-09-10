# -*- coding: utf-8 -*-
"""
Master Assembly Script for Storia dell'Arte Contemporanea Dataset
Compiles Modulo 1 (Anni '80), Modulo 2 (Anni '90), Modulo 3 (Anni Duemila), and Modulo 4 (Monografie & Fonti Mancanti)
into the production file `data/arte-data.js`.
Performs rigorous structural, numerical, and file-integrity validation.
"""

import os
import json
import re

from anni80_part1 import get_part1_chapters
from anni80_part2 import get_part2_chapters
from anni80_part3 import get_part3_chapters
from anni90_part1 import get_anni90_part1_chapters
from anni90_part2 import get_anni90_part2_chapters
from duemila_generator import get_duemila_chapters
from monografie_generator import get_monografie_chapters

def assemble_and_validate():
    print("=== ASSEMBLE STORIA DELL'ARTE CONTEMPORANEA DATASET ===")
    
    all_chapters = []
    
    # Modulo 1: Anni '80 (19 capitoli)
    c_80_1 = get_part1_chapters()
    c_80_2 = get_part2_chapters()
    c_80_3 = get_part3_chapters()
    mod1 = c_80_1 + c_80_2 + c_80_3
    print(f"Modulo 1 (Anni '80): {len(mod1)} capitoli caricati.")
    all_chapters.extend(mod1)
    
    # Modulo 2: Anni '90 (14 capitoli)
    c_90_1 = get_anni90_part1_chapters()
    c_90_2 = get_anni90_part2_chapters()
    mod2 = c_90_1 + c_90_2
    print(f"Modulo 2 (Anni '90): {len(mod2)} capitoli caricati.")
    all_chapters.extend(mod2)
    
    # Modulo 3: Duemila (7 capitoli)
    mod3 = get_duemila_chapters()
    print(f"Modulo 3 (Duemila): {len(mod3)} capitoli caricati.")
    all_chapters.extend(mod3)
    
    # Modulo 4: Monografie (6 capitoli)
    mod4 = get_monografie_chapters()
    print(f"Modulo 4 (Monografie): {len(mod4)} capitoli caricati.")
    all_chapters.extend(mod4)
    
    total = len(all_chapters)
    print(f"Totale complessivo capitoli: {total}")
    assert total == 46, f"Expected exactly 46 chapters, got {total}"
    
    # Validation
    errors = []
    warnings = []
    used_ids = set()
    img_pattern = re.compile(r'!\[.*?\]\((assets/arte/.*?)\)')
    
    for idx, c in enumerate(all_chapters):
        expected_num = idx + 1
        cid = c.get('id')
        num = c.get('number')
        mod = c.get('module')
        
        # ID check
        if not cid:
            errors.append(f"Capitolo {expected_num}: manca 'id'")
        elif cid in used_ids:
            errors.append(f"Capitolo {expected_num}: id duplicato '{cid}'")
        used_ids.add(cid)
        
        # Number check
        if num != expected_num:
            errors.append(f"Capitolo {expected_num}: number è {num}, atteso {expected_num}")
            
        # Module check
        if mod not in ['anni80', 'anni90', 'duemila', 'monografie']:
            errors.append(f"Capitolo {cid}: modulo sconosciuto '{mod}'")
            
        # Titles and text
        if not c.get('title'):
            errors.append(f"Capitolo {cid}: manca 'title'")
        if not c.get('subtitle'):
            errors.append(f"Capitolo {cid}: manca 'subtitle'")
        if not c.get('summary') or len(c['summary']) < 200:
            errors.append(f"Capitolo {cid}: 'summary' troppo breve o assente")
            
        # Keypoints
        kp = c.get('keyPoints', [])
        if len(kp) < 3:
            errors.append(f"Capitolo {cid}: keyPoints ha solo {len(kp)} elementi")
            
        # Flashcards (must be >= 5)
        fc = c.get('flashcards', [])
        if len(fc) < 5:
            errors.append(f"Capitolo {cid}: flashcards ha solo {len(fc)} elementi (minimo 5)")
        for fi, f in enumerate(fc):
            q_text = f.get('question') or f.get('front')
            a_text = f.get('answer') or f.get('back')
            if not q_text or not a_text:
                errors.append(f"Capitolo {cid} flashcard {fi+1}: domanda o risposta vuota")
            f['question'] = q_text
            f['answer'] = a_text
            f['front'] = q_text
            f['back'] = a_text
                
        # Open Questions (2)
        oq = c.get('openQuestions', [])
        if len(oq) < 2:
            errors.append(f"Capitolo {cid}: openQuestions ha solo {len(oq)} elementi (minimo 2)")
            
        # Quiz Studio (5 questions, 4 options each, correctIndex in 0..3)
        qz = c.get('quiz', [])
        if len(qz) != 5:
            errors.append(f"Capitolo {cid}: quiz ha {len(qz)} domande anziché 5")
        for qi, q in enumerate(qz):
            opts = q.get('options', [])
            cidx = q.get('correctIndex')
            if len(opts) != 4:
                errors.append(f"Capitolo {cid} quiz {qi+1}: ha {len(opts)} opzioni anziché 4")
            if cidx not in [0, 1, 2, 3]:
                errors.append(f"Capitolo {cid} quiz {qi+1}: correctIndex non valido ({cidx})")
            if not q.get('explanation'):
                errors.append(f"Capitolo {cid} quiz {qi+1}: manca spiegazione")
                
        # Exam Quiz (5 questions, 4 options each, correctIndex in 0..3)
        eqz = c.get('examQuiz', [])
        if len(eqz) != 5:
            errors.append(f"Capitolo {cid}: examQuiz ha {len(eqz)} domande anziché 5")
        for eqi, eq in enumerate(eqz):
            opts = eq.get('options', [])
            cidx = eq.get('correctIndex')
            if len(opts) != 4:
                errors.append(f"Capitolo {cid} examQuiz {eqi+1}: ha {len(opts)} opzioni anziché 4")
            if cidx not in [0, 1, 2, 3]:
                errors.append(f"Capitolo {cid} examQuiz {eqi+1}: correctIndex non valido ({cidx})")
            if not eq.get('explanation'):
                errors.append(f"Capitolo {cid} examQuiz {eqi+1}: manca spiegazione")
                
        # Image link check
        summary = c.get('summary', '')
        for img_match in img_pattern.findall(summary):
            if not os.path.exists(img_match):
                warnings.append(f"Capitolo {cid}: immagine referenziata non trovata sul disco: '{img_match}'")
                
    print(f"\nRisultato Validazione:")
    print(f"- Errori: {len(errors)}")
    print(f"- Avvisi: {len(warnings)}")
    
    if warnings:
        for w in warnings:
            print("  [AVVISO]", w)
            
    if errors:
        for e in errors:
            print("  [ERRORE]", e)
        raise ValueError(f"Validazione fallita con {len(errors)} errori.")
        
    # Write output to data/arte-data.js
    out_file = os.path.abspath("data/arte-data.js")
    js_content = "// =========================================================================\n"
    js_content += "// DATASET STORIA DELL'ARTE CONTEMPORANEA (46 CAPITOLI COMPLETI)\n"
    js_content += "// Modulo 1: Anni '80 (Elena Del Drago) - Cap 1..19\n"
    js_content += "// Modulo 2: Anni '90 (Francesco Bernardelli) - Cap 20..33\n"
    js_content += "// Modulo 3: Duemila (Francesco Bonami) - Cap 34..40\n"
    js_content += "// Modulo 4: Grandi Monografie & Fonti Mancanti (Cattelan, Hirst, Banksy, Ai Weiwei, Eliasson, Chevalier) - Cap 41..46\n"
    js_content += "// =========================================================================\n\n"
    js_content += "window.ARTE_DATA = " + json.dumps(all_chapters, ensure_ascii=False, indent=2) + ";\n"
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"\nSUCCESS: Dataset scritto correttamente in {out_file}")
    file_size_kb = os.path.getsize(out_file) / 1024
    print(f"Dimensione file: {file_size_kb:.1f} KB")

if __name__ == '__main__':
    assemble_and_validate()
