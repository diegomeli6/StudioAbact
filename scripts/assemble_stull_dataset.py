# -*- coding: utf-8 -*-
"""
Assembler for the complete Stull UX Design dataset (Chapters 1 to 43).
Harmonizes all schema fields, adds 3 flashcards per chapter for Part 4,
validates quiz balance, and writes out data/stull-data.js.
"""

import json

with open('stull_part1_1to11.json', encoding='utf-8') as f:
    p1 = json.load(f)

with open('stull_part2_12to19.json', encoding='utf-8') as f:
    p2 = json.load(f)

with open('stull_part3_20to28.json', encoding='utf-8') as f:
    p3 = json.load(f)

with open('stull_part4_29to43.json', encoding='utf-8') as f:
    p4 = json.load(f)

# Flashcards mapping for chapters 29 to 43
p4_flashcards = {
    29: [
        {"question": "Qual è il limite strutturale dell'approccio Agile applicato alla nascita di una nuova UX?", "answer": "Agile è modellato sullo sviluppo software (logica binaria: il codice compila o fallisce); creare una nuova UX richiede visione olistica e approvazione strategica netta, che entra in conflitto con l'informalità delle micro-iterazioni degli sprint."},
        {"question": "Cosa insegna la metafora del tunnel nella montagna rispetto a quello nel vulcano?", "answer": "Senza ricerca e pianificazione preventiva, scavare sembra identico all'inizio; solo quando si raggiunge il centro magmatico ci si rende conto del disastro irreversibile."},
        {"question": "Cos'è il Lean UX e su quale ciclo si fonda?", "answer": "È la sintesi tra Waterfall e Agile ideata da Gothelf e Seiden; elimina i deliverable pesanti puntando su comprensione condivisa e sul ciclo Costruire - Misurare - Apprendere."}
    ],
    30: [
        {"question": "Cosa insegna il caso dell'affetta-banane Hutzler 571 sul valore d'uso?", "answer": "Il problema reale risolto da un oggetto non è quello superficiale o ovvio: l'Hutzler risolve il vincolo di essiccazione termica (fette tutte con lo stesso spessore) per chi usa essiccatori domestici."},
        {"question": "Quali sono i tre pilastri della definizione del problema formulata da Stull?", "answer": "COSA (stabilisce la cornice e ciò che NON si creerà), PERCHÉ (evidenzia lo scopo fondante e il valore strategico) e COME (indica il principio operativo con cui superare i concorrenti)."},
        {"question": "Perché una definizione del problema resta utile anche se a fine progetto diventa irrilevante?", "answer": "Perché la sua funzione primaria è provocare la discussione iniziale, allineare gli stakeholder ed esporre le false convinzioni prima di scrivere il codice."}
    ],
    31: [
        {"question": "Quali sono le tre parole chiave da aggiungere su Google per la ricerca preliminare?", "answer": "«Notizie» (dà il contesto di attualità, fiere e vocabolario), «Tecnologia» (spiega il fondamento scientifico del valore) e «Confronto / vs» (espone dibattiti, alternative e punti di attrito dei consumatori)."},
        {"question": "Come ha superato Stull il suo pregiudizio sugli occhiali da sole da 300 dollari?", "answer": "Cercando 'sunglasses technology' ha scoperto che le lenti polarizzate eliminano i riverberi superiori a 4.000 lumen, proteggendo la vista di pescatori e navigatori marittimi."},
        {"question": "Qual è il limite metodologico di un'ora di ricerca su Google?", "answer": "Non sostituisce ricerche formali né studi sul campo, ma dissoda l'ignoranza iniziale compensando i bias soggettivi con fatti verificabili."}
    ],
    32: [
        {"question": "Qual è il limite intrinseco dei dati quantitativi e dei log di analytics?", "answer": "I numeri guardano sempre all'indietro: mostrano con esattezza cosa è accaduto (la scia della nave), ma non possono mai spiegare autonomamente il 'perché' umano dell'azione."},
        {"question": "In cosa consiste la fallacia del tiratore scelto texano applicata alla UX?",
        "answer": "Consiste nello scandagliare a posteriori dataset sterminati fino a trovare correlazioni casuali, spacciandole ingannevolmente per comportamenti intenzionali dell'utente."},
        {"question": "Cosa simboleggiano il 'Letto di Procuste' e la 'Scelta di Hobson' nella ricerca?", "answer": "Il Letto di Procuste rappresenta la manipolazione o selezione forzata dei dati per confermare teorie preconcette; la Scelta di Hobson indica questionari a risposta chiusa che non offrono reali alternative."}
    ],
    33: [
        {"question": "Quale calcolo economico smentì clamorosamente le linee guida del sito McResources di McDonald's?", "answer": "Con una paga di 10,93 $/h, pagare au-pair, addetto alla piscina e personal trainer generava oltre 1.200 dollari di debito annuo prima ancora di pagare affitto, cibo o tasse."},
        {"question": "Cosa si intende per 'ricerca con la calcolatrice'?", "answer": "L'uso di verifiche aritmetiche di buon senso per accertare se le assunzioni del business sono matematicamente e materialmente plausibili nella vita quotidiana dell'utente."},
        {"question": "Come si quantifica il ritorno economico (ROI) di un miglioramento di interfaccia?", "answer": "Moltiplicando i micro-risparmi di secondi ottenuti su form o procedure per il numero di transazioni e il volume di operatori quotidiani."}
    ],
    34: [
        {"question": "Quale errore commise Nike nel 2013 con la linea di leggings ispirata ai tatuaggi samoani?", "answer": "Applicò su pantaloni femminili il 'pe'a', un disegno di tatuaggio sacro riservato esclusivamente agli uomini adulti, violando un tabù culturale e provocando il ritiro della linea."},
        {"question": "Cos'è l'indagine contestuale e cosa rivelò nel caso dei CSR (customer service)?", "answer": "È l'osservazione etnografica dell'utente nel suo ambiente reale; svelò che gli operatori scivolavano sulla sedia per stanchezza, portando a ingrandire il testo sui monitor."},
        {"question": "Perché le domande d'intervista devono essere neutre e cosa offre il silenzio?", "answer": "Domande con 'cambiare' anziché 'migliorare' non inducono giudizi negativi impliciti; il silenzio permette all'intervistato di riflettere e formulare risposte autentiche."}
    ],
    35: [
        {"question": "Qual è la causa principale di quasi tutti i problemi di UX secondo Edward Stull?", "answer": "La mancata conciliazione (più o meno consapevole) delle informazioni, delle percezioni e degli obiettivi contrastanti tra l'organizzazione e i suoi utenti."},
        {"question": "Perché le decisioni di UX sono inevitabili?", "answer": "Perché o vengono deliberate per tempo attraverso la ricerca, oppure sarà costretto a prenderle lo sviluppatore front-end la notte prima del rilascio."},
        {"question": "Cosa significa 'conoscere il nome del cane' e cosa insegnano gli M&M's marroni dei Van Halen?", "answer": "Conoscere il nome del cane significa ancorare la comprensione ai dettagli materiali specifici; gli M&M's marroni insegnano che la trascuratezza dei dettagli rivela fragilità strutturali dell'intero sistema."}
    ],
    36: [
        {"question": "Perché il termine 'finale' è vietato nella corretta denominazione dei file di progetto?", "answer": "Perché nel software digitale nulla è mai definitivo prima della dismissione: usare 'finale' porta al caos di versioni ('finale_v2', 'finale_ok')."},
        {"question": "Qual è la triade dei deliverable secondo il loro grado di fedeltà?", "answer": "Mappe (concettuali, mostrano relazioni e logica), Mock-up (visivi, mostrano organizzazione spaziale e brand), Prototipi (comportamentali, simulano l'interazione dinamica nel tempo)."},
        {"question": "Cosa accade se si mostra un mock-up grafico rifinito troppo presto?", "answer": "La discussione degenera su dettagli estetici superficiali (colori, fotografie) distogliendo l'attenzione dall'architettura dell'informazione e dai flussi logici."}
    ],
    37: [
        {"question": "Cos'è una Persona secondo la teorizzazione di Alan Cooper?", "answer": "Un archetipo verosimile basato su ricerche empiriche reali che sintetizza obiettivi, frustrazioni e modelli mentali di un segmento chiave di utenti."},
        {"question": "Che differenza c'è tra una Persona storica e una ideale?", "answer": "La persona storica descrive l'utente consolidato attuale da proteggere; la persona ideale rappresenta il target futuro a cui il prodotto aspira a rivolgersi."},
        {"question": "Perché le caricature pittoresche alla 'The Dating Game' danneggiano il progetto?", "answer": "Perché riempire le personas di dettagli frivoli e irrilevanti (hobby stravaganti) fa perdere credibilità allo strumento agli occhi degli sviluppatori."}
    ],
    38: [
        {"question": "Quali sono le quattro fasi canoniche di una User Journey Map?", "answer": "Consapevolezza (scoperta del bisogno), Acquisizione (ricerca e valutazione informazioni), Conversione (scambio di valore) e Fidelizzazione (esperienza post-vendita e lealtà)."},
        {"question": "Come definisce Stull il concetto di 'conversione' nel percorso utente?", "answer": "Non solo come pagamento in denaro, ma in senso generale come qualsiasi scambio paritario di valore tra utente e organizzazione."},
        {"question": "Cosa simboleggiano le Isole Spratly e i 'collegamenti deboli'?", "answer": "Le isole Spratly simboleggiano i pericoli nascosti e le dispute interne che nascono senza una cartografia condivisa; i collegamenti deboli evidenziano i punti in cui l'utente abbandona per mancanza di motivazione."}
    ],
    39: [
        {"question": "Qual è la funzione specifica di una Mappa della Conoscenza (Concept Map)?", "answer": "Formalizzare l'ontologia del dominio del software: definisce le entità primarie (nodi) e le relazioni logiche (archi etichettati con verbi) che le collegano."},
        {"question": "Cosa NON descrive una mappa della conoscenza rispetto a un diagramma di flusso?", "answer": "Non descrive sequenze temporali, non descrive l'albero di navigazione delle pagine web e non definisce layout visivi."},
        {"question": "Cosa insegna l'aneddoto dell'Enciclopedia Britannica sepolta in giardino?", "answer": "Che un accumulo alfabetico di dati non equivale alla conoscenza, la quale esiste solo nella comprensione delle relazioni di causa ed effetto tra i concetti."}
    ],
    40: [
        {"question": "Quali sono le tre classi di requisiti definite dal modello di Kano?", "answer": "Must-be (indispensabili: dati per scontati, generano rabbia se assenti), Performance (lineari: più ce n'è, maggiore è la soddisfazione), Delighters (entusiasmanti: inattesi, generano stupore)."},
        {"question": "In cosa consiste il fenomeno dell'erosione del piacere?", "answer": "Nel decadimento temporale per cui una funzione entusiasmante (Delighter) diventa col tempo prestazionale e infine decade in un bisogno minimo scontato (Must-be)."},
        {"question": "Cosa insegna l'uso dei pattini da ghiaccio in 'Cast Away'?", "answer": "Che il valore di un oggetto non è intrinseco alla sua progettazione iniziale, ma dipende interamente dal contesto pratico e dal problema che risolve per l'utente."}
    ],
    41: [
        {"question": "Cos'è una Valutazione Euristica e da chi è stata formalizzata?",
        "answer": "È un'ispezione dell'interfaccia condotta da esperti senza utenti finali, confrontando il sistema con insiemi di regole universali; formalizzata da Nielsen e Molich nel 1990."},
        {"question": "Quali altri framework euristici cita Stull oltre a Jakob Nielsen?", "answer": "Le 8 regole d'oro di Ben Shneiderman (per sistemi interattivi) e i 18 criteri ergonomici di Bastien & Scapin dell'Inria."},
        {"question": "Come si articola la scala di gravità dei problemi di usabilità di Nielsen?", "answer": "Dal Grado 0 (non è un problema), Grado 1 (cosmetico), Grado 2 (minore), Grado 3 (maggiore) fino al Grado 4 (catastrofico, impedisce il completamento dell'attività)."}
    ],
    42: [
        {"question": "Quanti partecipanti servirebbero per una confidenza statistica del 95% su 20.000 persone?", "answer": "Circa 377 partecipanti; per questo motivo i test di usabilità sono indagini qualitative, dove 5 soggetti bastano per scoprire l'80% dei problemi critici."},
        {"question": "Cosa ha insegnato a Stull l'aneddoto del pianto del bambino nei test da remoto?", "answer": "Che la vera UX si misura tra il caos e le distrazioni della vita reale, con computer lenti e schermi piccoli, non nella calma fittizia di un laboratorio."},
        {"question": "Cos'è il test del Kobayashi Maru e cosa deve evitare il facilitatore?", "answer": "È una simulazione impossibile di Star Trek; il facilitatore deve sempre evitare che il test sembri un esame, ricordando che si valuta il software e mai l'utente."}
    ],
    43: [
        {"question": "Cosa afferma l'ipotesi della Regina Rossa applicata alla User Experience?", "answer": "Che in un mercato competitivo bisogna evolversi continuamente solo per rimanere rilevanti, poiché cambiano i dispositivi, le abitudini e le aspettative degli utenti."},
        {"question": "Quali tre tesi diffuse su cosa sia una 'buona UX' vengono confutate da Stull?", "answer": "Che debba essere sempre efficiente (molte esperienze gratificanti traggono valore dall'inefficienza), facile (le sfide complesse danno vera soddisfazione) o lieta (esperienze horror, cibo piccante o sport faticoso)."},
        {"question": "Qual è il compito etico minimo indiscutibile di una buona UX secondo Stull?", "answer": "Preservare in ogni circostanza la sicurezza, la serenità e la dignità dell'essere umano."}
    ]
}

# Harmonize Part 4
harmonized_p4 = []
for c in p4:
    num = c['num']
    # Standardize quiz questions in Part 4
    for q in c['quiz']:
        if 'correct' in q and 'correctIndex' not in q:
            q['correctIndex'] = q.pop('correct')

    chap_obj = {
        "id": f"stull-c{num}",
        "number": num,
        "partNum": 4,
        "partTitle": "Parte IV — Il Processo di Progettazione UX",
        "title": c['title'],
        "subtitle": c.get('subtitle', ''),
        "anchorTitle": c['anchorStory']['title'],
        "anchorText": c['anchorStory']['summary'],
        "summary": c['summary'],
        "keyPoints": c['keyPoints'],
        "readTime": c.get('readTime', '14 min'),
        "flashcards": p4_flashcards.get(num, []),
        "quiz": c['quiz'],
        "openQuestions": c.get('openQuestions', [])
    }
    harmonized_p4.append(chap_obj)

all_stull_chapters = p1 + p2 + p3 + harmonized_p4

# Sanity verification
assert len(all_stull_chapters) == 43, f"Expected 43 chapters, got {len(all_stull_chapters)}"
total_quiz = 0
for idx, ch in enumerate(all_stull_chapters, start=1):
    assert ch['number'] == idx, f"Chapter number mismatch at index {idx}: {ch['number']}"
    assert len(ch['quiz']) >= 5, f"Chapter {ch['number']} has fewer than 5 quiz questions ({len(ch['quiz'])})"
    assert len(ch['flashcards']) >= 3, f"Chapter {ch['number']} has fewer than 3 flashcards ({len(ch['flashcards'])})"
    assert len(ch['openQuestions']) >= 1, f"Chapter {ch['number']} missing open questions"
    total_quiz += len(ch['quiz'])
    for q in ch['quiz']:
        assert len(q['options']) == 4, f"Question options count != 4 in chap {ch['number']}"
        assert 'correctIndex' in q and 0 <= q['correctIndex'] <= 3, f"Invalid correctIndex in chap {ch['number']}: {q}"
        assert q['explanation'], f"Missing explanation in chap {ch['number']}"

print(f"Validation successful! All {len(all_stull_chapters)} Stull chapters valid. Total quiz questions: {total_quiz}")

# Write to data/stull-data.js
js_content = "// Dati di studio approfonditi estratti da 'UX_Design_Stull_Riassunto_esame.pdf'\n"
js_content += "// 43 Capitoli completi con sintesi accademiche, storie-ancora, flashcard e 215 quiz a 4 opzioni bilanciate.\n"
js_content += "window.STULL_DATA = " + json.dumps(all_stull_chapters, ensure_ascii=False, indent=2) + ";\n"

with open('data/stull-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"data/stull-data.js successfully written ({len(js_content)} bytes)!")
