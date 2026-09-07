# -*- coding: utf-8 -*-
"""
Generazione completa, accademica e integrale di Parte II: Siamo tutti esseri umani (Capitoli 12 to 19)
per Edward Stull - UX Design.
Nessuna omissione: psicologia cognitiva, fisiologia umana, percezione, memoria, flusso,
accessibilità, storytelling, autori, date, esperimenti storici e domande d'esame.
"""

import json

with open('scripts/stull_existing_questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

def get_q(num):
    return questions_data[str(num)]

chapters_p2 = []

# ==========================================
# CAPITOLO 12: Percezione
# ==========================================
q12 = get_q(12)
c12_summary = """### Contesto Filosofico e Fondamenti della Percezione Umana
La realtà oggettiva del mondo fisico e la realtà soggettiva vissuta dall'essere umano non coincidono mai in modo perfetto: **la nostra esperienza è determinata interamente da ciò che percepiamo e dal modo in cui il cervello decodifica gli stimoli sensoriali**.
Nel design delle interfacce grafiche (UI), comprendere i meccanismi neurofisiologici della percezione visiva è il prerequisito per guidare l'attenzione dell'utente, prevenire fraintendimenti ed evitare errori operativi.

### La Storia-Ancora: John Milton e il «Paradiso Perduto» (1667)
Nel suo capolavoro epico *Paradiso Perduto*, il poeta inglese John Milton scrisse una delle massime più profonde della letteratura universale:
> *«La mente è un luogo a se stessa, e in se stessa può fare dell'Inferno un Paradiso, e del Paradiso un Inferno»*.

Milton compose questi versi in un'epoca di laceranti guerre civili, con un re decapitato (Carlo I) e un altro esiliato. Ma soprattutto, **Milton scrisse quando era già completamente cieco**. Non poteva più ricevere stimoli luminosi dalla retina, eppure percepiva il mondo, la politica, il dolore e la bellezza con una lucidità interiore sbalorditiva.
> **Il significato per la UX**: Gli esseri umani non si limitano a "registrare" passivamente pixel, font e colori su uno schermo: **costruiscono attivamente il significato nella propria mente**. Se il design visivo è incoerente, la mente dell'utente fabbricherà un modello distorto che condurrà inevitabilmente a errori e frustrazione.

### I Due Processi Percettivi: Bottom-Up vs Top-Down
La scienza cognitiva suddivide l'elaborazione percettiva in due grandi direttrici complementari:
1. **Elaborazione Bottom-Up (Dal Basso verso l'Alto - Guidata dai Dati)**:
   - Ha origine dagli organi di senso periferici: fotoni che colpiscono la retina, onde sonore nel timpano, sensazioni termiche o tattili.
   - *Esempio del fuoco*: vediamo il guizzo arancione della fiamma, udiamo lo scoppiettio della legna, annusiamo il fumo, sentiamo il calore sulla pelle. La mente aggrega questi singoli frammenti sensoriali grezzi e conclude: *«C'è un falò»*.
   - *Nel Web*: un banner rosso vivo lampeggiante o un pulsante gigante a contrasto elevato catturano la retina per via puramente fisiologica (bottom-up).
2. **Elaborazione Top-Down (Dall'Alto verso il Basso - Guidata dai Concetti)**:
   - È guidata dalle aspettative pregresse, dalla memoria a lungo termine, dalla cultura e dal contesto.
   - *Esempio*: se vediamo un'ombra informe muoversi in un vicolo buio dopo aver guardato un film horror, il nostro cervello interpreta l'ombra come una minaccia letale; se la vediamo nel nostro giardino, pensiamo al gatto del vicino.
   - *Nel Web*: l'utente vede una parola blu sottolineata e assume immediatamente che sia un link cliccabile (top-down), prima ancora di aver analizzato i singoli pixel.

### Le Leggi della Gestalt (Psicologia della Forma)
All'inizio del Novecento, gli psicologi tedeschi della **Gestalt** (Wertheimer, Koffka, Köhler) dimostrarono che *«Il tutto è diverso dalla somma delle singole parti»*. Il cervello raggruppa istintivamente gli elementi visivi secondo leggi immutabili:

| Legge della Gestalt | Principio Percettivo |
| :--- | :--- |
| **1. Prossimità** | Gli elementi spazialmente vicini vengono percepiti come parte del medesimo gruppo o unità logica. |
| **2. Somiglianza** | Gli elementi che condividono forma, colore o stile vengono percepiti come aventi la medesima funzione. |
| **3. Continuità** | L'occhio segue percorsi, linee e curve naturali percependo gli elementi allineati come continui. |
| **4. Chiusura** | Il cervello completa automaticamente le figure incomplete, percependo forme chiuse anche con buchi. |
| **5. Figura / Sfondo** | La mente separa istintivamente l'oggetto in primo piano (figura focale) dallo sfondo retrostante. |
| **6. Destino Comune** | Elementi che si muovono nella medesima direzione vengono percepiti come un unico gruppo coerente. |

*L'errore comune di spaziatura nei form*: se in un modulo la distanza verticale tra il campo e la sua etichetta è di 20px, e la distanza tra il campo e l'etichetta successiva è anch'essa di 20px, la **Legge di Prossimità** viene violata: l'utente non sa a quale campo appartenga l'etichetta e compila i dati errati. L'etichetta deve essere visibilmente più vicina al proprio campo rispetto a qualsiasi altro elemento.

### La Legge di Weber e la JND (Just Noticeable Difference)
Formulata dal fisiologo tedesco **Ernst Heinrich Weber** nell'Ottocento, la **Legge di Weber** stabilisce che:
> *La nostra sensibilità agli stimoli non risponde alle differenze assolute, ma alle differenze RELATIVE rispetto all'intensità dello stimolo di partenza.*
> La **JND (Just Noticeable Difference)** è la minima quantità di variazione necessaria affinché il cambiamento venga percepito coscientemente nel 50% dei casi.

*L'insidia dei due pulsanti simili*: se affianchiamo due pulsanti primari con un blu scuro (#003366) e un blu notte (#002244), la variazione è sotto la soglia JND: l'utente non coglie la gerarchia e percepisce solo un'incoerenza casuale. Al contrario, per segnalare una differenza gerarchica netta (es. Salva vs Annulla), la differenza visiva deve superare abbondantemente la JND (es. pulsante pieno blu cobalto contro pulsante trasparente con bordo grigio chiaro o testo semplice).

### Affordance Reale vs Percepita (Gibson vs Norman)
- **James Gibson (1979)**: l'affordance è una relazione ecologica oggettiva tra organismo e ambiente (la ninfea galleggiante offre alla rana la possibilità di posarvisi, indipendentemente dalla sua consapevolezza).
- **Don Norman (1988)**: nella UX digitale conta l'**affordance percepita**: come le proprietà grafiche (ombre, gradienti, rilievi, stati hover) segnalano intuitivamente all'utente che un rettangolo sullo schermo può essere premuto, trascinato o digitato.

### Domande di Riflessione Progettuale
- Quali raggruppamenti della Gestalt ho generato, intenzionalmente o involontariamente, in questa schermata?
- La spaziatura e la somiglianza cromatica comunicano una relazione logica anche dove non dovrebbe sussistere?
- La differenza visiva tra elementi primari e secondari supera in modo inequivocabile la soglia JND di Weber?
- Gli utenti con deficit visivi o schermi a bassa luminosità riusciranno a decodificare la figura dallo sfondo?"""

c12_key_points = [
    "La percezione costruisce l'esperienza: Milton scrisse il Paradiso Perduto da cieco, a dimostrazione che il significato nasce nella mente e non nei soli occhi.",
    "Bottom-Up (stimoli sensoriali grezzi che salgono dalla retina) vs Top-Down (aspettative, cultura e modelli mentali che scendono a interpretare il segnale).",
    "Le Leggi della Gestalt: Prossimità, Somiglianza, Continuità, Chiusura, Figura/Sfondo e Destino Comune governano l'organizzazione spontanea degli elementi a schermo.",
    "La violazione della Prossimità nei form (spaziatura identica tra etichette e campi successivi) causa confusione cognitiva ed errori di digitazione.",
    "Legge di Weber e JND (Just Noticeable Difference): percepiamo variazioni relative, non assolute; gerarchie visive devono superare nettamente la soglia percettiva.",
    "L'insidia dei due pulsanti simili: sfumature quasi identiche confondono l'utente; l'azione primaria e secondaria richiedono contrasto inequivocabile.",
    "Affordance reale (Gibson) vs Affordance percepita (Norman): a schermo il designer deve esplicitare i signifier per comunicare cosa è interattivo."
]

chapters_p2.append({
    "id": "stull-c12", "number": 12, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Percezione", "readTime": "12 min",
    "anchorTitle": q12["anchorTitle"], "anchorText": q12["anchorText"],
    "summary": c12_summary, "keyPoints": c12_key_points,
    "flashcards": q12["flashcards"], "quiz": q12["quiz"], "openQuestions": q12["openQuestions"], "examQuiz": q12["examQuiz"]
})

# ==========================================
# CAPITOLO 13: Attenzione
# ==========================================
q13 = get_q(13)
c13_summary = """### L'Attenzione Umana: Una Risorsa Scarsa e Fluttuante
L'attenzione non è un faro perenne che illumina uniformemente tutto il campo visivo: **è un raggio laser estremamente concentrato, volatile e facilmente esausto**.
Nel Web Design, uno dei fallimenti più gravi è presumere che gli utenti scansionino ordinatamente ogni elemento presente sulla pagina. Gli utenti guardano solo ciò che attira il loro raggio attentivo in base al compito immediato, ignorando letteralmente tutto il resto.

### La Storia-Ancora: Il Pawpaw dell'Ohio
Il *Pawpaw* (*Asimina triloba*) è il più grande frutto commestibile autoctono degli Stati Uniti: una sorta di mango delle foreste temperate, con sapore di crema pasticcera alla banana e mango. Nonostante cresca rigoglioso lungo le rive dei fiumi dell'Ohio e della Pennsylvania, milioni di escursionisti ci passano accanto per tutta la vita senza vederlo mai. Perché? Le sue foglie verdi larghe e la buccia mimetica lo fondono completamente con il sottobosco circostante. Finché qualcuno non vi addestra lo sguardo mostrandovene uno da vicino, il pawpaw rimane totalmente invisibile.
> **Il significato per la UX**: Se un pulsante fondamentale, un link critico o un'avvertenza di sicurezza si mimetizzano cromaticamente o strutturalmente con lo sfondo della schermata (come il pawpaw nel bosco), per l'utente **quell'elemento semplicemente non esiste**, a prescindere dalla sua importanza oggettiva.

### Esperimenti Fondamentali: Il Gorilla Invisibile e il Test di Stroop
1. **L'Esperimento del Gorilla Invisibile (Christopher Chabris & Daniel Simons, 1999 - da Ulric Neisser, anni '70)**:
   - Ai partecipanti viene mostrato un breve video con due squadre (una in maglia bianca e una in maglia nera) che si passano un pallone da basket, con il compito preciso di contare a mente il numero esatto di passaggi effettuati dalla squadra bianca.
   - A metà video, una persona travestita da gorilla entra al centro della scena, si batte i pugni sul petto per nove secondi e si allontana lentamente.
   - **Risultato sbalorditivo**: oltre il **50% dei partecipanti non vede affatto il gorilla**.
   - Questo fenomeno prende il nome di **Cecità da Disattenzione (*Inattentional Blindness*)**: quando la mente è focalizzata su un compito ad alto carico cognitivo, il cervello cancella attivamente stimoli visivi enormi ma inattesi. Nel web design, questo spiega la *Banner Blindness*: gli utenti ignorano completamente interi quadranti dello schermo che somigliano a pubblicità.

2. **La Cecità al Cambiamento (*Change Blindness*)**:
   - L'incapacità dell'osservatore di notare modifiche anche vistose della scena se queste avvengono durante una breve interruzione visiva (es. un refresh di pagina, un battito di ciglia o uno scatto di layout). Se un errore modifica un testo in un angolo mentre l'utente guarda altrove, l'utente non saprà mai che qualcosa è cambiato.

3. **Il Test di Stroop (J. Ridley Stroop, 1935)**:
   - Ai soggetti viene presentata una lista di nomi di colori stampati con inchiostro cromaticamente discordante (es. la parola «ROSSO» stampata con inchiostro verde; «VERDE» stampato in giallo; «BLU» stampato in rosso), con l'istruzione di pronunciare ad alta voce il *colore dell'inchiostro* ignorando il testo.
   - Si verifica un ritardo sistematico nei tempi di risposta e un'impennata di errori a causa dell'**Interferenza Cognitiva**: la lettura del testo alfabetico è un processo automatico del Sistema 1 che interferisce con il compito analitico di denominazione del colore.
   - *Implicazione UX*: mai usare indicatori cromatici discordanti con le convenzioni (es. un pulsante di conferma colorato di rosso cupo o un messaggio d'errore colorato di verde smeraldo).

### Le Tipologie di Attenzione nel Software
- **Attenzione Selettiva**: la capacità di filtrare i disturbi ambientali e concentrarsi su un singolo segnale rilevante (es. compilare un IBAN escludendo le notifiche).
- **Attenzione Divisa (Multitasking)**: un mito biologico; gli umani non svolgono compiti cognitivi in parallelo, ma compiono un continuo e sfibrante *Task Switching* (passaggio rapido da un canale all'altro), con una pesante perdita di efficienza.
- **Attenzione Mantenuta (Sustained Attention)**: la capacità di rimanere vigili su un compito monotono; dura mediamente circa **10 minuti**, dopodiché l'accuratezza precipita fisiologicamente.

### Domande di Riflessione Progettuale
- L'elemento primario della mia pagina risalta immediatamente o è mimetizzato come il pawpaw dell'Ohio?
- Sto pretendendo dall'utente un'attenzione divisa impossibile o sto proteggendo il suo focus su un singolo compito?
- Ho evitato discordanze visive in stile Stroop (colori contrari al significato semantico)?
- Se un elemento della pagina cambia stato in modo asincrono, come attiro lo sguardo dell'utente per evitare la cecità al cambiamento?"""

c13_key_points = [
    "L'attenzione è una risorsa fisiologica limitata: gli utenti non guardano tutto, ma scandagliano solo ciò che risponde al loro obiettivo immediato.",
    "La metafora del Pawpaw dell'Ohio: il frutto commestibile più grande d'America resta invisibile se mimetizzato; elementi critici non visibili a colpo d'occhio non esistono.",
    "Cecità da disattenzione (Esperimento del Gorilla di Simons e Chabris): il 50% delle persone non nota un gorilla se impegnato a contare passaggi; base della Banner Blindness.",
    "Cecità al cambiamento (Change Blindness): modifiche non notate se avvengono fuori dal raggio attentivo immediato durante aggiornamenti di pagina.",
    "Test di Stroop (1935): l'interferenza cognitiva tra parola e colore ritarda le decisioni; vietato usare codici cromatici contrastanti con le convenzioni (es. verde per errore).",
    "Attenzione selettiva vs divisa: il multitasking è una finzione che frammenta l'energia mentale; l'attenzione mantenuta decade dopo circa 10 minuti continui."
]

chapters_p2.append({
    "id": "stull-c13", "number": 13, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Attenzione", "readTime": "10 min",
    "anchorTitle": q13["anchorTitle"], "anchorText": q13["anchorText"],
    "summary": c13_summary, "keyPoints": c13_key_points,
    "flashcards": q13["flashcards"], "quiz": q13["quiz"], "openQuestions": q13["openQuestions"], "examQuiz": q13["examQuiz"]
})

# ==========================================
# CAPITOLO 14: Flusso
# ==========================================
q14 = get_q(14)
c14_summary = """### Lo Stato di Flusso: L'Esperienza Ottimale
Uno dei contributi più fecondi della psicologia contemporanea al design interattivo è il concetto di **Flow (Stato di Flusso o Esperienza Ottimale)**, formulato dallo psicologo ungherese-statunitense **Mihaly Csikszentmihalyi** nel 1975.
Il Flusso è uno stato di coscienza in cui l'individuo è totalmente immerso in un'attività:
- L'attenzione è indivisa e assorbita dal compito;
- La percezione soggettiva del tempo si altera (le ore sembrano volare via come minuti);
- Si sperimenta un senso profondo di controllo, gratificazione e serenità operativa;
- Le preoccupazioni quotidiane e le distrazioni evaporano.

Nel Web e nelle applicazioni digitali (scrittura, programmazione, gaming, gestione di flussi finanziari), **progettare per il Flusso significa permettere all'utente di portare a termine sequenze di azioni complesse senza mai incontrare intoppi artificiali o interruzioni sgradevoli**.

### La Storia-Ancora: Pac-Man e le Monete d'Oro
Nel celebre cabinato arcade del 1980 ideato da Toru Iwatani, la pizza gialla *Pac-Man* naviga all'interno di un labirinto inseguita da quattro fantasmini colorati (Blinky, Pinky, Inky e Clyde). La genialità psicologica del gameplay risiede nei puntini (*dot* o «monete d'oro»):
- Il labirinto è costellato di 244 pallini regolari che Pac-Man inghiotte in una sequenza ritmica costante (*«waka-waka»*), intervallati da 4 pillole speciali (*Power Pellet*) che ribaltano temporaneamente il rapporto di potere permettendo di mangiare i fantasmi.
> **Il significato per la UX**: Le «monete d'oro» di Pac-Man incarnano il concetto di **micro-ricompensa continua e ritmica**. Durante un percorso operativo digitale (es. la compilazione di una procedura multi-step o un onboarding), ogni piccolo passaggio completato con successo agisce come una moneta d'oro: rilascia dopamina, conferma che stiamo avanzando nella giusta direzione e sostiene il Flusso dell'azione.

### Il Modello di Csikszentmihalyi: Il Canale di Flusso
Csikszentmihalyi rappresenta il Flusso come un canale dinamico delimitato da due baratri psicologici opposti:

> **Il Canale di Flusso (Mihaly Csikszentmihalyi)**:
> - **Ansia / Frustrazione**: si scatena quando la sfida imposta dall'interfaccia supera di gran lunga le abilità dell'utente.
> - **Noia / Disinteresse**: si manifesta quando l'abilità dell'utente è elevata ma il compito è banale, lento o ripetitivo.
> - **Canale di Flusso (Esperienza Ottimale)**: l'equilibrio dinamico in cui la complessità cresce proporzionalmente alla padronanza acquisita.

- **Ansia e Frustrazione**: si manifestano quando la sfida imposta dall'interfaccia (es. una procedura fiscale complicatissima con gergo incomprensibile e validazioni oscure) supera di gran lunga le competenze dell'utente. L'utente si sente inadeguato e abbandona.
- **Noia e Disinteresse**: si manifestano quando il compito è eccessivamente banale, lento o ripetitivo per il livello dell'utente (es. dover confermare ogni singola azione con tre click e schermate intermedie).
- **Il Canale di Flusso**: l'esperienza bilanciata in cui la complessità dei passaggi cresce in modo proporzionale alla padronanza acquisita dall'utente.

### La Larghezza di Banda dell'Attenzione e il Costo dell'Interruzione
Csikszentmihalyi ha quantificato matematicamente la **capacità massima di elaborazione del sistema nervoso cosciente**:
**Larghezza di Banda dell'Attenzione ≈ 110 bit al secondo (bit/s)**
Per comprendere una persona che ci parla sono necessari circa 60 bit/s. Questo significa che non abbiamo la banda biologica per elaborare simultaneamente due flussi complessi di informazioni.

*Il costo letale delle interruzioni*: quando un utente si trova immerso nel Flusso (es. sta scrivendo un saggio su un editor o analizzando dati contabili), un'interruzione arbitraria (come un pop-up modale al centro dello schermo che chiede: *«Ti piace la nostra app? Lascia una recensione!»*) distrugge istantaneamente il canale di flusso. Le ricerche dimostrano che **occorrono in media dai 15 ai 23 minuti per riconquistare il medesimo livello di concentrazione profonda** dopo un'interruzione esterna.
I pattern corretti prevedono:
- **Salvataggio automatico silenzioso in background** (senza bloccare lo schermo con finestre d'attesa);
- **Feedback non intrusivi** (notifiche discrete a scomparsa (*toast message*) negli angoli dello schermo);
- **Eliminazione di modali pubblicitarie o sondaggi** durante lo svolgimento di compiti core.

### Domande di Riflessione Progettuale
- Sto sostenendo il Flusso dell'utente fornendo micro-feedback ritmici ("monete d'oro") lungo il percorso?
- Il livello di complessità dell'interfaccia è perfettamente calibrato sulle competenze del mio target o genera ansia?
- Ci sono finestre di dialogo modali, pop-up di iscrizione o interruzioni asincrone che spezzano brutalmente l'attenzione?
- Il salvataggio dei dati avviene in modo trasparente e continuo o costringe l'utente a fermarsi?"""

c14_key_points = [
    "Il concetto di Flow (Mihaly Csikszentmihalyi, 1975): stato di immersione totale, concentrazione indivisa, distorsione temporale e gratificazione intrinseca.",
    "La metafora di Pac-Man e le monete d'oro: micro-ricompense continue, ritmiche e visibili sostengono il flusso e incentivano il completamento del percorso.",
    "Il Canale di Flusso: l'equilibrio dinamico che naviga tra l'Ansia (sfida troppo ardua rispetto all'abilità) e la Noia (compito troppo banale e farraginoso).",
    "Larghezza di banda dell'attenzione a circa 110 bit/s: limite biologico che impedisce l'elaborazione parallela di compiti complessi.",
    "Il costo distruttivo delle interruzioni: finestre modali e pop-up spezzano il flusso; servono fino a 20 minuti per ritrovare la concentrazione perduta.",
    "Pattern di protezione del Flow: salvataggio automatico in background, toast notification non bloccanti e rimozione di ostacoli intermedi."
]

chapters_p2.append({
    "id": "stull-c14", "number": 14, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Flusso", "readTime": "9 min",
    "anchorTitle": q14["anchorTitle"], "anchorText": q14["anchorText"],
    "summary": c14_summary, "keyPoints": c14_key_points,
    "flashcards": q14["flashcards"], "quiz": q14["quiz"], "openQuestions": q14["openQuestions"], "examQuiz": q14["examQuiz"]
})

# ==========================================
# CAPITOLO 15: Pigrizia
# ==========================================
q15 = get_q(15)
c15_summary = """### La Pigrizia come Principio di Efficienza Biologica
Nel linguaggio comune la "pigrizia" è considerata un vizio morale o una colpa. Nella psicologia cognitiva e nello User Experience Design, **la pigrizia è una virtù progettuale e una suprema forma di efficienza evolutiva**.
L'essere umano si è evoluto per milioni di anni in ambienti con risorse caloriche scarse: il cervello (che pesa appena il 2% del corpo ma consuma oltre il 20% del glucosio totale) ha sviluppato meccanismi implacabili per **risparmiare energia cognitiva ogni volta che è materialmente possibile**.
Quando un utente si comporta in modo "pigro" di fronte a un'applicazione — evitando di leggere lunghi paragrafi, rifiutando di compilare moduli prolissi o scegliendo la prima opzione disponibile — non sta manifestando disinteresse: sta applicando la più razionale delle strategie di sopravvivenza.

### La Storia-Ancora: La Capra di Montagna
Le capre di montagna che popolano le pareti scoscese delle Montagne Rocciose o delle Alpi non "scalano" le vette nel senso atletico ed eroico del termine: ci camminano, corrono e saltellano con naturalezza disarmante.
La capra non sceglie il percorso a caso, ma non si ferma neppure a calcolare sofisticate tabelle di rischio: **cerca semplicemente il punto d'appoggio più comodo, stabile e vicino, il sentiero naturale che richiede il minimo dispendio muscolare**.
> **Il significato per la UX**: Nella progettazione digitale, creare un'interfaccia a minimo sforzo è il massimo pregio professionale. **La pigrizia dell'utente è pura efficienza**: ottenere il massimo risultato desiderato con il minor consumo di calorie cerebrali e muscolari.

### Il Principio del Minimo Sforzo (George Kingsley Zipf, 1894/1949)
Formulato dal linguista e filologo George Zipf, il **Principio del Minimo Sforzo (*Principle of Least Effort*)** è uno dei pilastri della moderna scienza dell'informazione:
> *Ogni individuo adotterà invariabilmente la linea d'azione che comporta il minor dispendio probabile di lavoro medio.*
> Nella ricerca di informazioni, le persone usano il metodo più rapido e accessibile a loro disposizione, e **smettono di cercare non appena trovano una risposta minimamente soddisfacente**, rifiutando di esplorare opzioni teoricamente ottimali ma faticose da reperire.

### L'Euristica del Satisficing (Herbert Simon, Premio Nobel 1978)
Il concetto di Zipf si salda con la teoria fondamentale della razionalità limitata dell'economista e psicologo **Herbert Simon**, che coniò il celebre neologismo **Satisficing** (fusione tra *satisfy*, soddisfare, e *suffice*, bastare):
- Gli esseri umani **non ottimizzano** (*maximizing*), ovvero non analizzano tutte le 100 alternative possibili per trovare la scelta perfetta in assoluto;
- Gli esseri umani **si accontentano della prima opzione che supera la soglia minima di accettabilità** (*satisficing*).
*Esempio nell'e-commerce*: quando un utente cerca un'auto a noleggio, se la terza auto mostrata in elenco risponde ai suoi requisiti di prezzo e capienza, la prenota all'istante, rifiutando di scorrere le restanti 40 offerte che potrebbero fargli risparmiare 3 euro al prezzo di mezz'ora di comparazioni faticose.

### I Due Sistemi di Kahneman: Sistema 1 e Sistema 2
Il comportamento di satisficing è governato dal **Sistema 1** (il pensiero veloce, automatico, inconscio e privo di sforzo teorizzato da Daniel Kahneman in *Pensieri lenti e veloci*).
Il **Sistema 2** (il pensiero lento, analitico, razionale, concentrato e faticoso) viene attivato solo come extrema ratio, quando il Sistema 1 si scontra con un ostacolo imprevisto o una contraddizione palese. Costringere l'utente ad attivare il Sistema 2 per compiere un'operazione banale genera frustrazione e spinge all'abbandono.

### Teoria del Carico Cognitivo (John Sweller) e Impostazioni Predefinite (Smart Defaults)
La teoria di John Sweller distingue tre tipologie di carico mentale:
1. **Carico Intrinseco**: lo sforzo mentale ineliminabile richiesto dalla complessità della materia stessa (es. comprendere la differenza tra una franchigia assicurativa e un massimale);
2. **Carico Estraneo (Parassita)**: lo sforzo inutile generato da una cattiva progettazione dell'interfaccia (es. layout disordinato, font minuscoli, campi duplicati);
3. **Carico Pertinente**: l'energia impiegata per apprendere e consolidare schemi mentali utili.

*Il potere degli Smart Defaults (Impostazioni Predefinite Intelligenti)*:
Poiché l'utente è biologicamente guidato dal minimo sforzo, **l'opzione preselezionata di default viene accettata in oltre l'80-90% dei casi**.
- Se un'app per donazioni benefiche imposta di default *«Donazione mensile ricorrente (disattivabile quando vuoi con un click)»*, le adesioni ricorrenti si moltiplicano rispetto all'opzione di donazione una tantum;
- Se un gestionale compila automaticamente il CAP in base all'indirizzo e salva i dati fiscali già digitati in passato, l'utente completerà l'operazione con gratitudine e fidelizzazione.

### Domande di Riflessione Progettuale
- Sto rispettando la naturale pigrizia dell'utente offrendogli il percorso più agevole e diretto?
- Quali dati già noti al sistema sto costringendo l'utente a ridigitare inutilmente da capo?
- Ho predisposto impostazioni predefinite intelligenti (Smart Defaults) che sollevano l'utente da decisioni banali?
- La mia interfaccia favorisce il satisficing rapido o impone estenuanti comparazioni analitiche?"""

c15_key_points = [
    "La pigrizia è una virtù di efficienza biologica: il cervello umano economizza costantemente il dispendio calorico e cognitivo.",
    "La metafora della Capra di Montagna: l'animale non compie scalate eroiche ma cerca l'appoggio più naturale e vicino per non sprecare energie.",
    "Il Principio del Minimo Sforzo (George Zipf, 1894): l'individuo sceglie sempre la linea d'azione più economica per raggiungere l'obiettivo.",
    "Satisficing di Herbert Simon (Premio Nobel 1978): le persone non ottimizzano cercando la perfezione, ma scelgono la prima opzione sufficientemente buona.",
    "Sistema 1 (veloce e automatico) vs Sistema 2 (lento e faticoso): le interfacce migliori permettono al Sistema 1 di completare il task senza sforzo.",
    "Teoria del Carico Cognitivo di Sweller: azzerare il carico estraneo (layout confuso, moduli ripetuti) per non saturare la memoria di lavoro.",
    "La potenza degli Smart Defaults: l'opzione preselezionata di default viene confermata dalla quasi totalità degli utenti per risparmiare tempo."
]

chapters_p2.append({
    "id": "stull-c15", "number": 15, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Pigrizia", "readTime": "8 min",
    "anchorTitle": q15["anchorTitle"], "anchorText": q15["anchorText"],
    "summary": c15_summary, "keyPoints": c15_key_points,
    "flashcards": q15["flashcards"], "quiz": q15["quiz"], "openQuestions": q15["openQuestions"], "examQuiz": q15["examQuiz"]
})

# ==========================================
# CAPITOLO 16: Memoria
# ==========================================
q16 = get_q(16)
c16_summary = """### L'Architettura della Memoria Umana nel Design
La memoria umana non è un disco rigido digitale che salva file in modo indelebile e infallibile. **È un sistema biologico dinamico, fallibile, selettivo e soggetto a un rapido e inesorabile decadimento temporale**.
Nel Web Design, imporre all'utente il compito di ricordare informazioni da una schermata all'altra (codici d'ordine, opzioni selezionate in precedenza, password complesse, numerazioni seriali) è la ricetta sicura per generare errori, disorientamento e abbandono del funnel.

### La Storia-Ancora: L'Esperimento di Peterson & Peterson (1959)
Nel celebre esperimento condotto dagli psicologi Lloyd e Margaret Peterson all'Università dell'Indiana nel 1959, ai soggetti partecipanti venivano mostrati brevissimi trigrammi di consonanti privi di significato semantico (es. *CHJ, KDF, ZQR*). Subito dopo la visualizzazione, ai soggetti veniva chiesto di contare all'indietro a voce alta di tre in tre partendo da un numero casuale (es. 492, 489, 486...) per impedire la ripetizione subvocalica (*rehearsal*).
I risultati sul decadimento della **Memoria a Breve Termine (STM)** sconvolsero la comunità scientifica:
- Dopo soli **6 secondi** di distrazione numerica, i partecipanti ricordavano appena il **50%** dei trigrammi;
- Dopo soli **12 secondi**, il ricordo crollava al **15%**;
- Dopo **18 secondi**, il ricordo era azzerato al **10%** o scomparso del tutto.
> **Il significato per la UX**: La memoria di lavoro umana ha una durata effimera: **senza ripetizione o ancoraggio visivo, l'informazione svanisce nel nulla in meno di 10-15 secondi**. Se un'applicazione costringe l'utente a leggere un codice di tracciamento o un coupon su una pagina e a ridigitarlo a memoria nella pagina successiva, oltre la metà degli utenti sbaglierà o abbandonerà il flusso.

### Le Tre Strutture della Memoria
1. **Memoria Sensoriale**: conserva per una frazione di secondo l'impronta visiva (memoria iconica) o uditiva (memoria ecoica) dello stimolo;
2. **Memoria a Breve Termine / Memoria di Lavoro (Working Memory)**: lo spazio di elaborazione attivo ma limitato, gestito dall'ippocampo e dalla corteccia prefrontale;
3. **Memoria a Lungo Termine**: il magazzino permanente delle conoscenze, accessibile attraverso richiami e associazioni.

### Ippocampo vs Amigdala: Due Circuiti Mnemonici
Stull illustra una distinzione neuroanatomica cruciale per il designer:
- **Ippocampo**: è la sede della **memoria dichiarativa ed esplicita** (fatti, numeri, concetti astratti, passaggi procedurali razionali). Elabora lentamente e richiede energia.
- **Amigdala**: è il nucleo della **memoria emotiva e implicita** (paura, minaccia, entusiasmo, allarme).
*L'esperimento della luce blu*: se a una scossa elettrica viene associata una luce blu, l'amigdala memorizza la risposta di paura istantaneamente e in modo indelebile. Un paziente con lesione all'ippocampo non saprà spiegare a parole perché la luce blu sia pericolosa (memoria dichiarativa compromessa), ma il suo corpo suderà per l'ansia non appena la luce si accende (memoria emotiva dell'amigdala intatta).
*Implicazione UX*: una brutta esperienza su un sito (es. un addebito a sorpresa sulla carta) viene fissata dall'amigdala come un trauma: l'utente non ricorderà i dettagli del layout, ma proverà un'immediata repulsione viscerale ogni volta che rivedrà quel brand.

### La Capacità della Memoria di Lavoro: Da Miller (7 ± 2) a Cowan (4 Chunk)
Nel 1956 lo psicologo **George Miller** pubblicò il celebre articolo *«The Magical Number Seven, Plus or Minus Two»*, sostenendo che la memoria a breve termine potesse trattenere 7 ± 2 elementi (chunk).
La ricerca contemporanea (in particolare gli studi rigorosi di **Nelson Cowan nel 2010**) ha dimostrato che la stima di Miller era eccessivamente ottimistica per stimoli complessi:
> **Il limite reale della Memoria di Lavoro è di circa 4 CHUNK di informazioni indipendenti**.
> Il **Chunking** è la tecnica di raggruppamento di singole unità di dato in blocchi logici significativi:
> - Una sequenza numerica a 12 cifre senza spazi (*402319854712*) satura e distrugge la memoria di lavoro;
> - La medesima sequenza formattata a blocchi (*4023 - 1985 - 4712*) viene percepita come 3 chunk, perfettamente gestibili dalla mente umana.

### La Sesta Euristica di Nielsen: Riconoscimento Superiore al Richiamo (Recognition over Recall)
> *«Rendere visibili oggetti, azioni e opzioni. L'utente non deve dover ricordare informazioni da una parte all'altra dell'interfaccia. Le istruzioni per l'uso del sistema devono essere visibili o facilmente recuperabili quando necessario»*.

- **Richiamo a memoria (*Recall*)**: tipico delle interfacce a riga di comando (CLI) in cui l'utente deve ricordare a mente sintassi esatte (`grep -rn "pattern" /path`);
- **Riconoscimento visivo (*Recognition*)**: tipico delle moderne interfacce grafiche (GUI) e dei menu, in cui l'utente si limita a riconoscere l'opzione cercata tra quelle presentate visivamente a schermo.
*Applicazioni pratiche*:
- Mostrare la **cronologia degli articoli visti di recente** con miniature fotografiche in un e-commerce;
- Visualizzare un **pannello di riepilogo fisso (*Order Summary*)** durante tutto il checkout, mostrando chiaramente prezzi, taglia, colore e indirizzo prescelto.

### Domande di Riflessione Progettuale
- Sto costringendo l'utente a ricordare codici, passaggi o dati da una schermata all'altra?
- Le sequenze alfanumeriche complesse (carte di credito, telefoni, seriali) sono strutturate con la tecnica del chunking?
- Sto applicando il principio del Riconoscimento visivo o sto pretendendo uno sforzo di Richiamo mnemonico a vuoto?
- Quali reazioni emotive (amigdala) la pagina di conferma o di errore sta fissando nella memoria duratura dell'utente?"""

c16_key_points = [
    "L'estrema fragilità della memoria a breve termine: l'esperimento di Peterson & Peterson (1959) dimostra che dopo 6s ricordiamo il 50% e dopo 12s solo il 15%.",
    "Ippocampo (memoria dichiarativa di fatti e passaggi razionali) vs Amigdala (memoria emotiva e reazioni di allarme): le brutte esperienze creano traumi emotivi duraturi.",
    "Dal 'Magico Numero 7 ± 2' di Miller (1956) al limite reale di Nelson Cowan (2010): la memoria di lavoro trattiene mediamente solo 4 chunk informativi.",
    "La tecnica del Chunking: raggruppare codici lunghi in blocchi leggibili (es. carte di credito o telefoni) abbatte gli errori di inserimento.",
    "Sesta euristica di Nielsen: Riconoscimento superiore al Richiamo (Recognition over Recall); riconoscere visivamente un elemento costa zero fatica rispetto a ricordarlo a mente.",
    "Strumenti anti-sovraccarico nel web: carrelli con riepilogo perenne visibile, cronologia di navigazione fotografica e compilazione automatica dei dati noti."
]

chapters_p2.append({
    "id": "stull-c16", "number": 16, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Memoria", "readTime": "11 min",
    "anchorTitle": q16["anchorTitle"], "anchorText": q16["anchorText"],
    "summary": c16_summary, "keyPoints": c16_key_points,
    "flashcards": q16["flashcards"], "quiz": q16["quiz"], "openQuestions": q16["openQuestions"], "examQuiz": q16["examQuiz"]
})

# ==========================================
# CAPITOLO 17: Razionalizzazione
# ==========================================
q17 = get_q(17)
c17_summary = """### La Natura Post-Hoc delle Decisioni Umane
Nel pensiero razionalista classico si assumeva che l'essere umano valutasse le scelte in modo analitico: ponderando benefici, calcolando probabilità e agendo di conseguenza.
Le neuroscienze cognitive e l'economia comportamentale hanno smentito radicalmente questo mito: **la stragrande maggioranza delle decisioni umane viene presa in modo emotivo, impulsivo e subconscio; la razionalità interviene soltanto a posteriori (*post-hoc*), fabbricando argomentazioni logiche per giustificare ciò che il sentimento o l'impulso hanno già deciso**.

### La Storia-Ancora: François Mitterrand e gli Zigoli Ortolani (1995)
La notte di Capodanno del 1995, l'ex presidente francese François Mitterrand — ormai malato terminale di cancro alla prostata a pochi giorni dalla morte — organizzò un ultimo banchetto segreto con i suoi più cari amici. La portata culminante della cena furono gli **zigoli ortolani** (*ortolans*): minuscoli uccelli canori protetti per legge, la cui caccia e degustazione erano severamente proibite dal parlamento per crudeltà e rischio estinzione. Secondo il secolare rituale gastronomico francese, gli ortolani vengono catturati, accecati, ingrassati a forza nel buio con fichi e annegati nell'Armagnac, per poi essere mangiati interi (ossa comprese) mentre i commensali coprono il proprio volto con un grande tovagliolo bianco di lino (ufficialmente per trattenere gli aromi, metaforicamente per nascondere la propria vergogna e ingordigia allo sguardo di Dio).
> **Il significato per la UX**: Mitterrand — uomo di raffinatissima cultura giuridica e presidente della Repubblica che aveva promulgato le leggi di tutela ambientale — violò deliberatamente la legge per compiacere un desiderio viscerale, razionalizzando il gesto come l'estremo omaggio alla tradizione gastronomica della Francia. **Quando le persone compiono una scelta mossa dal desiderio, la loro mente troverà sempre una giustificazione logica inattaccabile per assolversi**.

### La Teoria della Dissonanza Cognitiva (Leon Festinger, 1957)
La razionalizzazione poggia sulle fondamenta della celebre teoria psicologica di **Leon Festinger**:
> La **Dissonanza Cognitiva** è lo stato di profondo disagio e tensione psicologica vissuto da una persona quando si trova a sostenere due convinzioni tra loro contraddittorie, oppure quando **il suo comportamento reale entra in conflitto aperto con i suoi valori o con la sua immagine di sé**.

Per sanare questa dolorosa discrepanza emotiva, l'individuo non ammette quasi mai di aver sbagliato: **ristruttura le proprie convinzioni post-hoc per renderle compatibili con l'azione compiuta**.
- *La volpe e l'uva di Esopo*: la volpe non potendo raggiungere l'uva afferma che è acerba;
- *L'acquirente impulsivo*: dopo aver speso 1.200 euro per l'ultimo modello di smartphone, anziché ammettere la spesa superflua si convince che *«ne aveva assoluta necessità per lavorare in modo più sicuro ed efficiente»*.

### La Razionalizzazione Post-Acquisto nel Web Design (Buyer's Remorse)
Immediatamente dopo aver cliccato sul pulsante *«Paga ora»*, l'utente viene assalito da un'ondata di vulnerabilità e ansia nota come **Rimorso dell'Acquirente (*Buyer's Remorse*)**: *«Ho fatto bene? Il prodotto arriverà davvero? È una truffa? Ho sprecato i miei risparmi?»*.
Se in questo istante critico l'interfaccia mostra solo una schermata bianca o una scritta secca (*«Transazione 4820 eseguita»*), il panico si diffonde.
**Il design di una grande UX interviene attivamente a supporto della razionalizzazione post-acquisto**:
1. **Riaffermare la bontà della scelta**: mostrare messaggi rassicuranti e festosi (*«Complimenti per la tua scelta! Ti sei appena assicurato un prodotto artigianale d'eccellenza»*);
2. **Social Proof (Riprova Sociale)**: mostrare brevi estratti di recensioni a cinque stelle di altri acquirenti entusiasti;
3. **Trasparenza logistica totale**: visualizzare immediatamente la mappa interattiva di spedizione, la data stimata di consegna e il riepilogo chiaro di tutto ciò che accadrà nelle prossime 24 ore;
4. **Impatto positivo**: in acquisti etici o donazioni, ribadire l'effetto concreto generato (*«Grazie a questo acquisto hai contribuito a piantare 10 alberi nella foresta amazzonica»*).

### Il Bias di Conferma (Confirmation Bias)
Il **Bias di Conferma** è la tendenza sistematica a ricercare, interpretare e memorizzare solo le evidenze che confermano le nostre convinzioni preesistenti, ignorando attivamente le prove contrarie.
- Condiziona gli utenti, che cercano recensioni positive per convalidare ciò che vogliono comprare;
- Condiziona drammaticamente i designer: durante i test con gli utenti, i team tendono a considerare le lodi come prove scientifiche della bravura del design e a liquidare le difficoltà degli utenti come *«distrazione isolata di un partecipante incompetente»*.

### Domande di Riflessione Progettuale
- La mia pagina di conferma acquisto supporta attivamente la razionalizzazione post-acquisto o abbandona l'utente all'ansia del rimorso?
- Sto fornendo all'utente motivazioni razionali solide (dati, impatto, risparmio) per difendere la sua scelta emotiva di fronte a se stesso o al suo capo?
- Come ricercatore, sto interpretando i risultati dei test con rigore o sto cadendo nella trappola del bias di conferma?"""

c17_key_points = [
    "Le decisioni umane sono prevalentemente emotive e subconsce; la razionalità interviene a posteriori (post-hoc) per fabbricare giustificazioni logiche.",
    "La metafora di Mitterrand e gli zigoli ortolani: di fronte a un desiderio viscerale, anche la mente più autorevole scavalca le proprie regole e razionalizza la trasgressione.",
    "Dissonanza Cognitiva (Leon Festinger, 1957): il disagio provocato dal conflitto tra azioni e convinzioni viene placato ristrutturando le proprie opinioni a posteriori.",
    "Buyer's Remorse (Rimorso dell'Acquirente): l'ansia acuta che coglie l'utente subito dopo un acquisto importante richiede un supporto UX dedicato.",
    "Best practice nella schermata di conferma: rassicurare sulla bontà della scelta, mostrare la riprova sociale (social proof) ed esplicitare chiaramente i prossimi passaggi logistici.",
    "Bias di Conferma: la tendenza a registrare solo le conferme delle proprie idee pregresse condiziona pericolosamente sia il consumatore che il ricercatore UX."
]

chapters_p2.append({
    "id": "stull-c17", "number": 17, "partNum": 2, "partTitle": "Parte I — Siamo tutti esseri umani",
    "title": "Razionalizzazione", "readTime": "9 min",
    "anchorTitle": q17["anchorTitle"], "anchorText": q17["anchorText"],
    "summary": c17_summary, "keyPoints": c17_key_points,
    "flashcards": q17["flashcards"], "quiz": q17["quiz"], "openQuestions": q17["openQuestions"], "examQuiz": q17["examQuiz"]
})

# ==========================================
# CAPITOLO 18: Accessibilità
# ==========================================
q18 = get_q(18)
c18_summary = """### L'Accessibilità (a11y): Il Riconoscimento dei Bisogni Umani
L'accessibilità digitale non è un atto di carità filantropica, una concessione paternalistica né un mero adempimento burocratico per evitare sanzioni legali: **l'accessibilità è la progettazione universale di prodotti e servizi affinché siano pienamente fruibili da qualsiasi essere umano, indipendentemente dalle sue abilità fisiche, sensoriali o cognitive**.
La celebre definizione di **Cynthia Waddell e Chieko Asakawa** (e ripresa da Viscardi) stabilisce:
> *«L'accessibilità non è un favore per una minoranza sfortunata: è il riconoscimento fondamentale che persone diverse hanno bisogni diversi in contesti diversi»*.

I dati statistici smontano l'illusione che l'accessibilità riguardi "poche persone":
- Solo negli Stati Uniti, oltre il **12,8% della popolazione complessiva** (pari a un cittadino su sei!) convive con una disabilità permanente certificata (visiva, uditiva, motoria o cognitiva);
- In Europa e nel mondo le percentuali sono analoghe e in costante crescita a causa del progressivo invecchiamento demografico.

### La Storia-Ancora: Le Strade Interstatali Americane (Eisenhower, 1956)
Nel 1956 il presidente Dwight D. Eisenhower firmò il *Federal-Aid Highway Act*, avviando la costruzione della più grande rete infrastrutturale del pianeta: il sistema delle autostrade interstatali (*Interstate Highway System*).
Il progetto non fu concepito solo per auto da corsa veloci guidate da piloti esperti: fu progettato a tavolino con standard di sicurezza universali per permettere il transito a carri pesanti, camioncini agricoli, famiglie inesperte e convogli militari d'emergenza in caso di catastrofe.
> **L'Effetto Scivolo del Marciapiede (*Curb-Cut Effect*)**:
> Negli anni Settanta, i movimenti per i diritti delle persone con disabilità ottennero che i marciapiedi urbani venissero dotati di scivoli inclinati alle intersezioni per consentire il passaggio delle sedie a rotelle.
> Il risultato empirico superò ogni previsione: **gli scivoli vennero utilizzati quotidianamente e con immenso sollievo dalla stragrande maggioranza della popolazione sana**: genitori con passeggini per bambini, viaggiatori con valigie a rotelle, corrieri con carrelli di merci pesanti, fattorini in bicicletta e anziani con la spesa.
> **La legge aurea dell'accessibilità**: quando si progetta per persone con disabilità estreme, **l'intera esperienza complessiva migliora esponenzialmente per tutti gli utenti indistintamente**.

### Le Tre Categorie di Disabilità: Permanenti, Temporanee, Situazionali
La disabilità non è una caratteristica fissa dell'individuo, ma una discrepanza tra il corpo umano e la progettazione dell'ambiente circostante:

| Tipo di Disabilità | Esempio Motorio | Esempio Visivo | Esempio Uditivo |
| :--- | :--- | :--- | :--- |
| **Permanente** | Amputazione o paralisi di un braccio | Cecità totale o grave ipovisione | Sordità profonda dalla nascita |
| **Temporanea** | Frattura del braccio destro con gesso per 6 settimane | Infezione agli occhi con cataratta o post-operazione laser | Infezione acuta dell'orecchio medio con perdita uditiva |
| **Situazionale** | Genitore che tiene in braccio un neonato mentre cucina | Camminare sotto il sole a picco con display abbagliato | Trovarsi in un bar rumoroso o in metropolitana senza cuffie |

Progettare un'interfaccia accessibile utilizzabile con una sola mano, con contrasti forti e con sottotitoli video protegge l'utente in tutti questi scenari quotidiani.

### Le Linee Guida WCAG 2.1 e i Quattro Principi P.O.U.R.
Lo standard internazionale di riferimento emanato dal W3C (Consorzio World Wide Web) è articolato sui quattro principi fondanti dell'acronimo **P.O.U.R.**:
1. **Percepibile (Perceivable)**: le informazioni e i componenti dell'interfaccia devono essere presentati in modalità che l'utente possa percepire attraverso almeno uno dei suoi sensi:
   - Alternativa testuale (*attributo alt*) per tutte le immagini non decorative;
   - Trascrizioni e sottotitoli (*captions*) per tutti i contenuti audio e video.
2. **Utilizzabile (Operable)**: i componenti dell'interfaccia e la navigazione devono essere azionabili con diverse modalità di input:
   - **Accessibilità totale da tastiera**: qualsiasi funzione deve essere attivabile con i tasti `Tab`, frecce e `Invio`, senza richiedere per forza un mouse;
   - Mantenimento visibile del bordo di focus (`outline: auto`, mai soppresso con `outline: none` senza alternativa);
   - Nessun carosello multimediale a scorrimento automatico rapido privo di pulsante di pausa/stop.
3. **Comprensibile (Understandable)**: le informazioni e le operazioni a schermo devono essere chiare, leggibili e prevedibili:
   - Indicazione della lingua naturale del documento (`<html lang="it">`);
   - Istruzioni e messaggi di errore chiari e collocati accanto al campo interessato.
4. **Robusto (Robust)**: il codice HTML deve essere semanticamente valido e compatibile con un'ampia varietà di agenti utente e tecnologie assistive (*Screen Reader* come NVDA, JAWS o VoiceOver).

### Contrasto Cromatico e Daltonismo
- **Livello WCAG AA**: rapporto di contrasto cromatico minimo di **4,5:1** per il testo normale e di **3:0:1** per il testo grande (> 18pt o 14pt grassetto) e gli elementi grafici interattivi.
- **Daltonismo (cecità ai colori)**: colpisce circa l'**8% della popolazione maschile** globale (deuteranopia e protanopia, cecità al rosso e al verde).
  - *Regola tassativa*: **mai affidare la trasmissione di un'informazione critica unicamente al cambiamento di colore** (es. colorare di rosso un campo errato senza aggiungere un'icona di allarme e un testo esplicito).

### Il Fondamento Filosofico: Il Velo di Ignoranza di John Rawls
Il grande filosofo politico **John Rawls** (in *A Theory of Justice*, 1971) propose un celebre esperimento mentale: se dovessimo progettare le regole fondamentali di una società senza sapere in anticipo quale posizione occuperemo in essa (se saremo sani o malati, ricchi o poveri, vedenti o non vedenti, giovani o anziani) — trovandoci dietro un **«Velo di Ignoranza»** — la decisione più razionale e vantaggiosa sarebbe progettare un sistema equo e inclusivo per chiunque.
Allo stesso modo, il designer non sa quando egli stesso o i suoi cari si troveranno anziani, con le mani tremanti o ipovedenti: progettare un'interfaccia accessibile è l'investimento più intelligente per il futuro di tutti.

### Domande di Riflessione Progettuale
- Posso navigare e completare l'intero acquisto sulla mia piattaforma usando esclusivamente la tastiera senza toccare il mouse?
- Il rapporto di contrasto tra testo e sfondo supera la soglia minima di 4,5:1 su tutte le schermate?
- Le immagini informative sono provviste di attributi alt accurati e i video contengono sottotitoli completi?
- L'indicazione di un errore dipende solo dal colore rosso o è supportata da icone e testi descrittivi?"""

c18_key_points = [
    "L'accessibilità (a11y) è la progettazione universale per tutti: il 12,8% della popolazione USA convive con una disabilità permanente; l'invecchiamento rende il tema vitale.",
    "La metafora dell'Interstate Highway System e il Curb-Cut Effect: progettare scivoli per sedie a rotelle ha migliorato la vita di genitori con passeggini, viaggiatori e anziani.",
    "Disabilità Permanente (amputazione/cecità), Temporanea (frattura di un braccio/infezione) e Situazionale (sole abbacinante/neonato in braccio): tutti sperimentano limitazioni.",
    "I 4 principi WCAG (P.O.U.R.): Percepibile (testo alternativo e sottotitoli), Utilizzabile (tastiera e focus visivo), Comprensibile (chiarezza e coerenza) e Robusto (HTML semantico).",
    "Rapporto di contrasto minimo WCAG AA: 4,5:1 per testo normale e 3:1 per testo grande; divieto assoluto di usare solo il colore per comunicare errori.",
    "Il Velo di Ignoranza di John Rawls applicato alla UX: progettare l'interfaccia senza sapere chi saremo garantisce la massima equità e fruibilità universale."
]

chapters_p2.append({
    "id": "stull-c18", "number": 18, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Accessibilità", "readTime": "11 min",
    "anchorTitle": q18["anchorTitle"], "anchorText": q18["anchorText"],
    "summary": c18_summary, "keyPoints": c18_key_points,
    "flashcards": q18["flashcards"], "quiz": q18["quiz"], "openQuestions": q18["openQuestions"], "examQuiz": q18["examQuiz"]
})

# ==========================================
# CAPITOLO 19: Storytelling
# ==========================================
q19 = get_q(19)
c19_summary = """### Il Potere della Narrazione nella Progettazione d'Esperienza
Gli esseri umani non sono macchine logiche che computano elenchi puntati: **gli esseri umani sono creature narrative (*Homo Narrans*)**. Da millenni, attorno al fuoco delle caverne fino agli schermi degli smartphone, il cervello umano utilizza le storie per codificare la realtà, memorizzare pericoli, sviluppare empatia e attribuire significato all'esistenza.
Nel Web Design, lo **Storytelling** non consiste nell'inserire lunghi testi romanzati all'interno delle schermate, ma nello **strutturare l'intero percorso dell'utente come un arco narrativo coerente, avvincente e privo di stonature**.

### La Storia-Ancora: La Retorica di Aristotele e il Viaggio dell'Eroe
Nel IV secolo a.C., nel suo trattato sulla *Retorica*, **Aristotele** codificò i tre pilastri della persuasione e della comunicazione umana:
1. **Ethos (Autorevolezza e Credibilità morale del narratore)**: la fiducia che l'interfaccia ispira attraverso il design professionale, l'onestà e la reputazione;
2. **Pathos (Empatia e Coinvolgimento Emotivo)**: la capacità di toccare i sentimenti, i desideri profondi e le speranze del pubblico;
3. **Logos (Argomentazione Logica e Razionale)**: la solidità delle prove fattuali, la chiarezza dei dati, la convenienza economica e la trasparenza tecnica;
4. *(A cui si aggiunge il **Kairos**, il senso opportuno del tempismo e dell'istante propizio).*

A questa triade si unisce la struttura narrativa classica dei **Tre Atti** (Impostazione, Confronto/Crisi, Risoluzione) e il celebre modello mitologico del **Viaggio dell'Eroe (*Monomyth*)** teorizzato dall'antropologo **Joseph Campbell** ne *L'eroe dai mille volti* (1949).

### Chi è il Vero Eroe della Storia?
L'errore più grossolano commesso dal marketing tradizionale e dalle aziende autoreferenziali è posizionare il proprio brand o il proprio prodotto come l'Eroe della storia (*«Siamo i leader di mercato dal 1975, abbiamo vinto 40 premi, siamo i migliori!»*).
Agli utenti non importa nulla dei trionfi dell'azienda: **nella loro mente, l'Eroe è sempre e solo l'UTENTE STESSO**.
- **L'Utente è l'Eroe**: una persona che si trova nel proprio mondo ordinario, affronta una sfida difficile (ristrutturare casa, curare una malattia, pianificare le finanze) e cerca disperatamente un aiuto;
- **Il Brand è la Guida / il Mentore** (il Gandalf o l'Obi-Wan Kenobi della situazione): non compie l'impresa al posto dell'eroe, ma gli consegna la mappa magica, gli attrezzi indispensabili e il consiglio saggio per superare la prova.

### Lo Storytelling nell'Onboarding (Accoglienza del Nuovo Utente)
L'esperienza di **Onboarding** (il primo avvio dell'applicazione) deve essere modellata esattamente come l'atto iniziale di una narrazione:
- Non gettare l'utente in una stanza buia piena di controlli inesplicabili;
- Non soffocarlo con 10 schermate di tutorial teorici bloccanti che nessuno leggerà mai;
- **Far vivere all'utente il suo primo successo operativo immediato (*Aha! Moment*)**: fargli creare il primo documento, fargli inviare il primo messaggio, fargli assaporare la vittoria.

### Tono di Voce (Tone of Voice) e il Paradosso dell'Allarme «Tutto OK»
Il **Tone of Voice (TOV)** definisce la personalità linguistica dell'interfaccia. Deve essere coerente, empatico e contestuale.
- *L'errore dell'umorismo fuori luogo*: se un'applicazione bancaria o medica fallisce un'operazione critica (es. un bonifico urgente bloccato) e mostra l'illustrazione di un buffo gattino con la scritta ironica *«Ops! Qualcosa è andato storto nei nostri biscottini! Riprova più tardi con un sorriso!»*, l'utente proverà un'ondata di furia omicida. Nei momenti di errore critico, il tono deve essere sobrio, trasparente, responsabile e operativo.

> **La metafora dell'«Allarme Tutto OK» (The Simpsons)**:
> In un celebre episodio dei Simpson, Homer inventa un congegno per la sicurezza domestica: *«L'Allarme Tutto OK»*, una sirena assordante che suona a tutto volume ogni tre secondi per rassicurare gli abitanti che *«non c'è nessun pericolo, tutto va bene!»*.
> Se l'interfaccia disturba continuamente l'utente con banner, notifiche e pop-up non necessari per comunicare ovvietà, genera desensibilizzazione da allarme (*Alert Fatigue*): quando si verificherà un errore vero, nessuno ci farà più caso.

### Domande di Riflessione Progettuale
- Nella narrazione del mio prodotto, chi ricopre il ruolo dell'Eroe: la mia azienda o l'utente reale?
- Sto fornendo all'utente una mappa chiara (come una saggia guida) per superare i suoi ostacoli?
- Il tono di voce del testo è adeguato alla gravità del contesto o risulta irritantemente giocoso nei momenti di crisi?
- L'onboarding fa assaporare immediatamente il trionfo del primo task completato?"""

c19_key_points = [
    "Lo Storytelling nella UX struttura l'interazione come un arco narrativo coerente e avvincente per connettere la mente dell'utente al prodotto.",
    "La Retorica di Aristotele: Ethos (autorevolezza e credibilità morale), Pathos (coinvolgimento emotivo) e Logos (prove razionali e dati fattuali).",
    "Il Viaggio dell'Eroe (Joseph Campbell): l'utente è sempre l'Eroe della narrazione; il prodotto/brand è il Mentore che gli fornisce gli strumenti per trionfare.",
    "L'Onboarding come rito di passaggio: far vivere subito all'utente il primo momento di successo operativo (Aha! Moment) anziché bloccarlo con noiosi tutorial.",
    "Tone of Voice contestuale: l'umorismo fuori luogo nei messaggi di errore critici (es. pagamenti falliti) distrugge la fiducia e fa infuriare l'utente.",
    "La trappola dell'Allarme 'Tutto OK' (Homer Simpson): notifiche continue e inutili generano Alert Fatigue, rendendo invisibili i veri messaggi di pericolo."
]

chapters_p2.append({
    "id": "stull-c19", "number": 19, "partNum": 2, "partTitle": "Parte II — Siamo tutti esseri umani",
    "title": "Storytelling", "readTime": "11 min",
    "anchorTitle": q19["anchorTitle"], "anchorText": q19["anchorText"],
    "summary": c19_summary, "keyPoints": c19_key_points,
    "flashcards": q19["flashcards"], "quiz": q19["quiz"], "openQuestions": q19["openQuestions"], "examQuiz": q19["examQuiz"]
})

with open('scripts/stull_part2_complete.json', 'w', encoding='utf-8') as f:
    json.dump(chapters_p2, f, ensure_ascii=False, indent=2)

print(f"Completata generazione Parte II: {len(chapters_p2)} capitoli salvati in scripts/stull_part2_complete.json")
