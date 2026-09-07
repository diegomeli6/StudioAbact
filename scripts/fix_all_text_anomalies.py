# -*- coding: utf-8 -*-
"""
Script per bonificare tutti i testi da residui di codice, comandi LaTeX non renderizzabili ($$),
blocchi di codice ASCII superflui e formattazioni rotte nei 5 dataset della piattaforma.
"""

import json, re

# ==============================================================================
# 1. BONIFICA data/stull-data.js
# ==============================================================================
print("1. Bonifica data/stull-data.js...")
with open("data/stull-data.js", "r", encoding="utf-8") as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

for c in stull:
    num = c.get("number")
    s = c.get("summary", "")

    # Capitolo 6: Formula del Contesto (quella segnalata esplicitamente dall'utente)
    if num == 6:
        s = s.replace(
            "$$\\text{Esperienza} = f(\\text{Evento}, \\text{Tempo}, \\text{Contesto})$$",
            "> **Formula del Contesto**: **Esperienza = f(Evento, Tempo, Contesto)**"
        )
        s = s.replace(
            "$$Esperienza = f(Evento, Tempo, Contesto)$$",
            "> **Formula del Contesto**: **Esperienza = f(Evento, Tempo, Contesto)**"
        )

    # Capitolo 9: Stabilità
    if num == 9:
        s = s.replace("$\\times$", "×")
        s = s.replace(
            "$$8.760 \\times 0.01 = 87.6 \\text{ ore di blocco all'anno!}$$",
            "> **8.760 ore × 0,01 = 87,6 ore di blocco all'anno** *(oltre 3 giorni e mezzo di disservizio continuo!)*"
        )

    # Capitolo 10: Velocità
    if num == 10:
        s = s.replace(
            "$$\\text{Velocità Percepita} = \\frac{\\text{Aspettativa} + \\text{Feedback}}{\\text{Latenza Reale}}$$",
            "> **Velocità Percepita = (Aspettativa + Feedback) / Latenza Reale**"
        )
        s = s.replace(
            "$$T = b \\cdot \\log_2(n + 1)$$",
            "> **Legge di Hick-Hyman**: **T = b · log₂(n + 1)** *(dove T è il tempo di reazione, n il numero di opzioni e b una costante empirica)*"
        )

    # Capitolo 15: Pigrizia
    if num == 15:
        s = s.replace("$17 \\times 24$", "17 × 24")

    # Capitolo 16: Memoria
    if num == 16:
        s = s.replace("$7 \\pm 2$", "7 ± 2")

    # Capitolo 23: Rilevanza
    if num == 23:
        s = s.replace(
            "$$\\text{Rilevanza} = \\text{Bisogno Soggettivo} \\times \\text{Tempestività} \\times \\text{Valore Percepito}$$",
            "> **Formula della Rilevanza**: **Bisogno Soggettivo × Tempestività × Valore Percepito**"
        )

    # Capitolo 26: Prezzo
    if num == 26:
        s = s.replace("Solo Stampa 125$", "Solo Stampa 125 $")
        s = s.replace("Web + Stampa a 125$", "Web + Stampa a 125 $")

    # Capitolo 29: Waterfall, Agile e Lean
    if num == 29:
        s = s.replace("$\\rightarrow$", "→")

    # Capitolo 32: Ricerca quantitativa (Fallacia del tiratore texano)
    if num == 32:
        texan_block = (
            "```\n"
            "[Fallacia del Tiratore Texano]\n"
            "Spara a caso sulla parete di un fienile -> Poi disegna il bersaglio attorno al gruppo di fori più fitto\n"
            "(Nelle analitiche: si scandagliano milioni di log a posteriori finché non si trova una correlazione casuale,\n"
            "spacciandola per un comportamento utente intenzionale).\n"
            "```"
        )
        clean_texan = (
            "> **La Fallacia del Tiratore Texano**:\n"
            "> Un tiratore spara a caso sulla parete di un fienile e poi disegna il bersaglio attorno al gruppo di fori più fitto.\n"
            "> *Nel web analytics accade lo stesso*: si scandagliano milioni di log di navigazione a posteriori finché non si trova una correlazione casuale, spacciandola erroneamente per un comportamento utente intenzionale."
        )
        s = s.replace(texan_block, clean_texan)

    # Capitolo 33: Ricerca con la calcolatrice (Tabella McResources con $ rotti)
    if num == 33:
        s = s.replace("$10,93 \\text{ all'ora}$", "10,93 $ all'ora")
        s = s.replace("$\\approx 22.730 \\$$", "circa 22.730 $")
        s = s.replace("$10,72 \\text{/h}$", "10,72 $/ora")
        s = s.replace("$- 22.290 \\$$", "- 22.290 $")
        s = s.replace("$13,51 \\text{/h}$", "13,51 $/ora")
        s = s.replace("$- 702,52 \\$$", "- 702,52 $")
        s = s.replace("$18,85 \\text{/h}$", "18,85 $/ora")
        s = s.replace("$- 980,20 \\$$", "- 980,20 $")
        s = s.replace("$-1.242,72 \\$$", "-1.242,72 $")

    # Capitolo 34: Ricerca qualitativa (Battuta della pantera rosa)
    if num == 34:
        pink_panther_block = (
            "```\n"
            "[La battuta della Pantera Rosa]\n"
            "Clouseau: «Il suo cane morde?» - Portiere: «No.»\n"
            "(Il cane azzanna la mano di Clouseau)\n"
            "Clouseau: «Aveva detto che il suo cane non mordeva!» - Portiere: «Quello non è il mio cane.»\n"
            "-> Morale: Se poni domande chiuse e imprecise, otterrai risposte letterali ma fuorvianti.\n"
            "```"
        )
        clean_pink_panther = (
            "> **L'aneddoto della Pantera Rosa**:\n"
            "> - **Ispettore Clouseau**: *«Il suo cane morde?»*\n"
            "> - **Portiere**: *«No.»*\n"
            "> *(Il cane azzanna la mano di Clouseau)*\n"
            "> - **Clouseau**: *«Aveva detto che il suo cane non mordeva!»*\n"
            "> - **Portiere**: *«Quello non è il mio cane.»*\n"
            ">\n"
            "> **Morale metodologica**: Se nelle interviste poni domande chiuse e imprecise, otterrai risposte letterali ma del tutto fuorvianti per la progettazione."
        )
        s = s.replace(pink_panther_block, clean_pink_panther)

    # Capitolo 36: Documentazione (Continuum di fedeltà)
    if num == 36:
        fidelity_block = (
            "```\n"
            "ASTRATTO (Bassa Fedeltà) -------------> CONCRETO (Alta Fedeltà)\n"
            "                     [MAPPE] ---------> [MOCK-UP] ---------> [PROTOTIPI]\n"
            "                    (Concetto)          (Estetica)         (Interazione)\n"
            "```"
        )
        clean_fidelity = (
            "> **Continuum di Fedeltà Progettuale**:\n"
            "> **1. Mappe Concettuali** *(Astratto / Bassa Fedeltà — definiscono il concetto)* →\n"
            "> **2. Mock-up Visivi** *(Media Fedeltà — definiscono l'estetica e la gerarchia)* →\n"
            "> **3. Prototipi Interattivi** *(Concreto / Alta Fedeltà — definiscono l'interazione reale)*"
        )
        s = s.replace(fidelity_block, clean_fidelity)

    # Capitolo 38: Mappare il percorso (4 Fasi)
    if num == 38:
        journey_block = (
            "```\n"
            "[CONSAPEVOLEZZA] ------> [ACQUISIZIONE] ------> [CONVERSIONE] ------> [FIDELIZZAZIONE]\n"
            " (Scoperta bisogno)        (Valutazione info)     (Scambio di valore)     (Ritorno e fiducia)\n"
            "```"
        )
        clean_journey = (
            "> **Le 4 Fasi Canoniche del Viaggio dell'Utente**:\n"
            "> **1. Consapevolezza** *(scoperta del bisogno)* →\n"
            "> **2. Acquisizione** *(valutazione delle informazioni)* →\n"
            "> **3. Conversione** *(scambio di valore e acquisto)* →\n"
            "> **4. Fidelizzazione** *(supporto, ritorno e fiducia nel tempo)*"
        )
        s = s.replace(journey_block, clean_journey)

    # Capitolo 39: Mappare la conoscenza (Schema entità)
    if num == 39:
        entity_block = (
            "```\n"
            "[UTENTE] --------(sottoscrive)--------> [POLIZZA ASSICURATIVA]\n"
            "   |                                            |\n"
            "(possiede)                                  (copre)\n"
            "   v                                            v\n"
            "[VEICOLO] <-------(è coinvolto in)-------- [SINISTRO STRADALE]\n"
            "```"
        )
        clean_entity = (
            "> **Esempio di Mappa delle Entità e Relazioni (Dominio Assicurativo)**:\n"
            "> - **Utente** *(sottoscrive)* → **Polizza Assicurativa**\n"
            "> - **Polizza Assicurativa** *(copre)* → **Sinistro Stradale**\n"
            "> - **Utente** *(possiede)* → **Veicolo**\n"
            "> - **Veicolo** *(è coinvolto in)* → **Sinistro Stradale**"
        )
        s = s.replace(entity_block, clean_entity)

    # Capitolo 40: Modello di Kano (Grafico ASCII)
    if num == 40:
        kano_block = (
            "```\n"
            "Soddisfazione Utente (+)\n"
            "         ^                     / (Fattori Entusiasmanti - Delighters)\n"
            "         |                    /\n"
            "         |                   /\n"
            "         |                  /   (Fattori Lineari - Performance)\n"
            "         |=================/==================> Implementazione (+)\n"
            "         |                /\n"
            "         |               /   (Fattori Indispensabili - Must-be)\n"
            "         v              /\n"
            "Insoddisfazione (-)\n"
            "```"
        )
        clean_kano = (
            "> **Rappresentazione Concettuale degli Assi di Kano**:\n"
            "> - **Asse Verticale**: Soddisfazione dell'utente (dalla profonda frustrazione al totale entusiasmo).\n"
            "> - **Asse Orizzontale**: Grado di implementazione funzionale (da assente a eccellente).\n"
            "> - *Curve*: **Delighters** (in alto a sinistra, stupore esponenziale), **Performance** (diagonale lineare), **Must-be** (in basso a destra, insoddisfazione catastrofica se assente)."
        )
        s = s.replace(kano_block, clean_kano)

    # Capitolo 42: Test utente (Laboratorio vs Remoto)
    if num == 42:
        test_block = (
            "```\n"
            "[TEST IN LABORATORIO]\n"
            "Ambiente controllato, monitor retina perfetti, banda ultra-rapida, facilitatore accanto.\n"
            "-> Rischio: Finzione asettica. L'utente si sente sotto esame e usa macchine infinitamente più potenti delle sue.\n\n"
            "[TEST DA REMOTO NON PRESIDIATO O SINCRONO]\n"
            "L'utente usa il suo computer reale, nel suo salotto, con la connessione reale, mentre il figlio piange.\n"
            "-> Vantaggio immenso: Si scopre il reale divario tecnologico (browser obsoleti, schermi piccoli, distrazioni ambientali).\n"
            "```"
        )
        clean_test = (
            "> **Confronto: Test in Laboratorio vs Test da Remoto**:\n"
            "> - **Test in Laboratorio (Presidiato)**: Ambiente controllato, monitor retina perfetti, connessione ultra-veloce, facilitatore presente. *Rischio*: Finzione asettica; l'utente si sente sotto esame e usa macchine più potenti di quelle domestiche.\n"
            "> - **Test da Remoto (Ecologico)**: L'utente usa il suo computer reale, nel suo ambiente quotidiano, con la propria connessione e le distrazioni reali. *Vantaggio immenso*: Rivelazione del divario tecnologico reale (browser obsoleti, schermi a bassa risoluzione, estensioni attive)."
        )
        s = s.replace(test_block, clean_test)

    c["summary"] = s

# Salvataggio di stull-data.js
output_stull = "// Dati di studio approfonditi estratti da 'UX_Design_Stull_Riassunto_esame.pdf'\n"
output_stull += "// 43 Capitoli completi con sintesi accademiche, storie-ancora, flashcard, quiz di studio e banco d'esame bilanciati.\n"
output_stull += "window.STULL_DATA = " + json.dumps(stull, indent=2, ensure_ascii=False) + ";\n"

with open("data/stull-data.js", "w", encoding="utf-8") as f:
    f.write(output_stull)
print("-> data/stull-data.js bonificato con successo!")

# ==============================================================================
# 2. BONIFICA data/dispense-data.js
# ==============================================================================
print("\n2. Bonifica data/dispense-data.js...")
with open("data/dispense-data.js", "r", encoding="utf-8") as f:
    text_d = f.read()

start_d = text_d.find('[')
end_d = text_d.rfind(']') + 1
disp = json.loads(text_d[start_d:end_d])

for c in disp:
    num = c.get("number")
    s = c.get("summary", "")
    
    # Cap 2: Formula UX
    if num == 2:
        s = s.replace(
            "$$\\text{Interfaccia} + \\text{Comportamento} + \\text{Flusso} = \\text{User Experience (UX)}$$",
            "> **La Formula Fondante della UX**: **Interfaccia + Comportamento + Flusso = User Experience (UX)**"
        )
    
    # Cap 13: Formula Ethan Marcotte
    if num == 13:
        s = s.replace(
            "$$\\text{Target} \\div \\text{Context} = \\text{Result (\\%)}$$",
            "> **La Formula del Layout Fluido (Ethan Marcotte)**: **Target ÷ Context = Result (%)**"
        )
        
    c["summary"] = s

output_disp = "// Dispense del professore strutturate per lo studio approfondito del Web Design\n"
output_disp += "window.DISPENSE_DATA = " + json.dumps(disp, indent=2, ensure_ascii=False) + ";\n"

with open("data/dispense-data.js", "w", encoding="utf-8") as f:
    f.write(output_disp)
print("-> data/dispense-data.js bonificato con successo!")

# ==============================================================================
# 3. BONIFICA data/progetto-cards-data.js
# ==============================================================================
print("\n3. Bonifica data/progetto-cards-data.js...")
with open("data/progetto-cards-data.js", "r", encoding="utf-8") as f:
    text_c = f.read()

start_c = text_c.find('[')
end_c = text_c.rfind(']') + 1
cards = json.loads(text_c[start_c:end_c])

for m in cards:
    mid = m.get("id")
    s = m.get("summary", "")
    
    if mid == "cards-m2":
        s = s.replace(
            "$$\\text{Larghezza totale} = \\text{width} + \\text{padding-left} + \\text{padding-right} + \\text{border-left} + \\text{border-right}$$",
            "> **Box Model Tradizionale (`content-box`)**:\n> **Larghezza totale** = width + padding-left + padding-right + border-left + border-right"
        )
        s = s.replace(
            "$$\\text{Content effettivo} = \\text{width dichiarata} - (\\text{padding} + \\text{border})$$",
            "> **Box Model Moderno (`border-box`)**:\n> **Larghezza totale a schermo** = width dichiarata *(padding e bordi sono incorporati internamente)*"
        )
    m["summary"] = s

output_cards = "// Moduli didattici basati sul codice reale di Progetto_Esame_Cards\n"
output_cards += "window.CARDS_DATA = " + json.dumps(cards, indent=2, ensure_ascii=False) + ";\n"

with open("data/progetto-cards-data.js", "w", encoding="utf-8") as f:
    f.write(output_cards)
print("-> data/progetto-cards-data.js bonificato con successo!")

# ==============================================================================
# 4. BONIFICA data/arte-data.js
# ==============================================================================
print("\n4. Bonifica data/arte-data.js...")
with open("data/arte-data.js", "r", encoding="utf-8") as f:
    text_a = f.read()

start_a = text_a.find('[')
end_a = text_a.rfind(']') + 1
arte = json.loads(text_a[start_a:end_a])

for c in arte:
    cid = c.get("id")
    s = c.get("summary", "")
    
    if cid == "arte-c3":
        c3_block = (
            "```\n"
            "[IL NEOESPRESSIONISMO TEDESCO]\n"
            "  ├── GEORG BASELITZ     --> Capovolgimento della figura: la pittura si svincola dal soggetto\n"
            "  ├── ANSELM KIEFER      --> Memoria storica, cenere, piombo, paglia e miti wagneriani\n"
            "  ├── SIGMAR POLKE       --> Ironia corrosiva, retini tipografici raster, veleni e alchimia visiva\n"
            "  └── JÖRG IMMENDORFF    --> Café Deutschland: allegorie politiche della divisione nazionale\n"
            "```"
        )
        clean_c3 = (
            "> **I Protagonisti del Neoespressionismo Tedesco**:\n"
            "> - **Georg Baselitz**: *Capovolgimento della figura* — la pittura si svincola dal primato del soggetto.\n"
            "> - **Anselm Kiefer**: *Memoria storica e materica* — l'elaborazione del passato tedesco attraverso piombo, cenere e paglia.\n"
            "> - **Sigmar Polke**: *Alchimia visiva e ironia* — contaminazione tra retini tipografici raster, veleni e pittura.\n"
            "> - **Jörg Immendorff**: *Café Deutschland* — allegorie politiche e teatrali della Germania divisa dal Muro."
        )
        s = s.replace(c3_block, clean_c3)
        
    if cid == "arte-c10":
        c10_block = (
            "```\n"
            "[IL GIOCO DEI NOMI E DEGLI INDIZI]\n"
            "CIF AMOTAN II  ----(Anagramma perfetto)---->  «I AM FICTION»  (Io sono finzione!)\n"
            "APISTOS (Naufragio dell'Incredibile) ------>  Unbelievable / Non credibile\n"
            "```"
        )
        clean_c10 = (
            "> **La Chiave della Finzione di Damien Hirst (Indizi e Anagrammi)**:\n"
            "> - **Cif Amotan II**: Anagramma perfetto di *«I AM FICTION»* (Io sono finzione!).\n"
            "> - **Apistos** (nome della nave naufragata): In greco antico significa letteralmente *«Incredibile / Non credibile»*."
        )
        s = s.replace(c10_block, clean_c10)

    c["summary"] = s

output_arte = "// Dataset Storia dell'Arte Contemporanea (Anni '80, Hirst/YBAs, Eliasson, Chevalier)\n"
output_arte += "window.ARTE_DATA = " + json.dumps(arte, indent=2, ensure_ascii=False) + ";\n"

with open("data/arte-data.js", "w", encoding="utf-8") as f:
    f.write(output_arte)
print("-> data/arte-data.js bonificato con successo!")

print("\nBONIFICA COMPLETATA AL 100% SU TUTTI I DATASET!")
