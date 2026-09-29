#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modulo 1: Fotocamera e Linguaggio Cinematografico (Capitoli 1-6)
Nessuna emoji. Solo testo accademico rigoroso e riferimenti visivi.
"""

def get_module_1_chapters():
    return [
        {
            "id": "taw-c1",
            "number": 1,
            "title": "Struttura della Macchina Fotografica",
            "subtitle": "Componenti essenziali, Reflex vs Visione Diretta, Analogico e Digitale",
            "readTime": "8 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. Architettura Fondamentale del Dispositivo di Ripresa

La macchina fotografica e da presa costituisce l'interfaccia tecnologica primaria tra l'ambiente fenomenico e la superficie di registrazione dell'immagine. Dal punto di vista strutturale e funzionale, il dispositivo e organizzato in tre sotto-sistemi interdipendenti:

1. **Il Corpo Macchina (Camera Body)**:
   - Funge da camera oscura sigillata a tenuta di luce (*light-tight chamber*).
   - Nelle fotocamere digitali, alloggia il **sensore d'immagine** (CMOS o CCD), il convertitore analogico-digitale (ADC), il processore d'immagine (Image Signal Processor - ISP) e l'unita di memoria/bus dati.
   - Nelle cineprese e fotocamere analogiche, contiene il vano di caricamento della pellicola, i rocchetti dentati di trascinamento e la griffa di avanzamento fotogramma per fotogramma.
2. **Il Gruppo Ottico (Obiettivo)**:
   - Sistema ottico composto da lenti convergenti e divergenti raggruppate in gruppi acromatici.
   - Determina l'angolo di campo (*Field of View*), l'apertura massima del diaframma a iride e la risoluzione ottica (MTF - *Modulation Transfer Function*).
   - Puo essere a focale fissa (*prime lens*) o variabile (*zoom lens*).
3. **Il Sistema di Mirino e Visualizzazione (Viewfinder)**:
   - Permette all'operatore di comporre il quadro, verificare la messa a fuoco e monitorare l'esposizione prima e durante l'acquisizione.

---

### 2. Sistemi Ottici: Reflex (DSLR) vs Visione Diretta (Mirrorless / Telemetro)

La distinzione fondamentale tra i dispositivi di ripresa risiede nel percorso ottico che la luce compie dall'obiettivo all'occhio dell'operatore:

| Parametro Comparativo | Sistema Reflex (SLR / DSLR) | Visione Diretta / Mirrorless (MILC) |
| :--- | :--- | :--- |
| **Principio Ottico** | Specchio mobile a 45 gradi + Pentaprisma / Pentaspecchio | Nessun elemento meccanico riflettente: lettura continua del sensore |
| **Tipo di Mirino** | Mirino Ottico Diretto (OVF) TTL (*Through The Lens*) | Mirino Elettronico (EVF) OLED o Display LCD posteriore |
| **Latenza e Blackout** | Zero ritardo ottico; blackout dello specchio durante lo scatto | Minima latenza di refresh; nessun oscuramento meccanico continuativo |
| **Anteprima Parametri** | Visione analogica della scena (nessuna simulazione esposizione reale) | WYSIWYG: anteprima istantanea di ISO, WB, profondita di campo e istogramma |
| **Ingombro e Meccanica** | Corpo piu spesso (tiraggio flangia elevato ~44mm); vibrazioni dello specchio | Corpo ultracompatto (tiraggio ridotto ~16-20mm); assenza di micro-mosso meccanico |

---

### 3. Transizione Tecnologica: Pellicola Fotochimica vs Sensore Elettronico

- **Fotografia Analogica**:
  - Il supporto di registrazione e l'emulsione fotosensibile alogenuro d'argento stesa su supporto in triacetato di cellulosa o poliestere.
  - La reazione e chimico-fisica irreversibile: formazione dell'immagine latente e successiva rivelazione in bagno chimico di sviluppo e fissaggio.
  - Caratterizzata dalla grana (*grain*) organica causata dai cristalli d'argento e da una curva di risposta tonale (*curva Hurter-Driffield*) morbida sulle alte luci.
- **Fotografia Digitale**:
  - Il supporto e una matrice fito-sensibile di fotodiodi organizzati secondo il pattern di Bayer (RGGB).
  - Conversione fotoni -> carica elettrica -> tensione -> codice numerico binario discreto a 12, 14 o 16 bit.
  - Vantaggi sistemici: azzeramento dei tempi di sviluppo chimico, controllo real-time del segnale, memorizzazione su memorie a stato solido non distruttive e possibilita di post-produzione computazionale avanzata.""",
            "keyPoints": [
                "I tre componenti cardine di una macchina fotografica sono corpo macchina, obiettivo e mirino.",
                "Nelle Reflex (DSLR), uno specchio a 45 gradi devia la luce al pentaprisma per la visione ottica diretta TTL.",
                "Nelle fotocamere a visione diretta ed elettroniche (Mirrorless), il mirino elettronico legge direttamente il flusso digitale del sensore.",
                "L'analogico sfrutta reazioni chimiche su cristalli di alogenuro d'argento con grana organica e curva tonale analogica.",
                "Il digitale converte i fotoni in cariche elettriche tramite fotodiodi campionati in forma binaria numerica discreta."
            ],
            "flashcards": [
                {
                    "question": "Quali sono le tre macro-componenti strutturali di una fotocamera?",
                    "answer": "Corpo macchina (ospita sensore/pellicola e processore), obiettivo (gruppo ottico e diaframma) e mirino/display di visualizzazione."
                },
                {
                    "question": "Come funziona il mirino ottico TTL di una macchina reflex?",
                    "answer": "Uno specchio mobile a 45 gradi devia il fascio ottico proveniente dall'obiettivo verso un pentaprisma che raddrizza l'immagine e la invia all'oculare."
                },
                {
                    "question": "Qual e il vantaggio operativo principale del mirino elettronico (EVF) rispetto al mirino ottico?",
                    "answer": "Offre un'anteprima reale (WYSIWYG) dell'esposizione, del bilanciamento del bianco, del profilo colore e della profondita di campo prima dello scatto."
                },
                {
                    "question": "Cosa determina la grana nella fotografia analogica a pellicola?",
                    "answer": "La dimensione e la distribuzione statistica casuale dei cristalli microscopici di alogenuri d'argento sospesi nell'emulsione gelatinosa."
                },
                {
                    "question": "In cosa consiste il campionamento nei sensori digitali?",
                    "answer": "Nella quantizzazione della carica elettrica accumulata da ogni singolo fotodiodo in un valore numerico binario a 12, 14 o 16 bit."
                }
            ],
            "quiz": [
                {
                    "question": "Nelle fotocamere reflex a specchio (DSLR), quale elemento raddrizza otticamente l'immagine capovolta proveniente dall'obiettivo?",
                    "options": [
                        "Il pentaprisma (o pentaspecchio)",
                        "Il filtro passa-basso ottico",
                        "L'otturatore a tendina planofocale",
                        "Il processore d'immagine CMOS"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il pentaprisma a riflessione totale interna raddrizza l'immagine sia sull'asse verticale che orizzontale prima di inoltrarla all'oculare del mirino."
                },
                {
                    "question": "Quale caratteristica fisica differenzia in modo strutturale le fotocamere mirrorless dalle reflex?",
                    "options": [
                        "L'assenza dello specchio mobile e un tiraggio flangia notevolmente piu ridotto",
                        "L'impossibilita di cambiare obiettivo",
                        "L'assenza totale del diaframma nell'ottica",
                        "L'uso esclusivo di pellicola chimica al posto del silicio"
                    ],
                    "correctIndex": 0,
                    "explanation": "Eliminando la cassa specchio ribaltabile, le mirrorless riducono drasticamente la distanza tra flangia dell'innesto e piano focale (tiraggio)."
                },
                {
                    "question": "Cosa accade fisicamente durante lo scatto in una fotocamera reflex tradizionale?",
                    "options": [
                        "Lo specchio si alza rapidamente provocando un momentaneo blackout nel mirino ottico",
                        "Il mirino ottico aumenta la sua luminosita del 200%",
                        "L'obiettivo si chiude completamente all'infinito",
                        "Il pentaprisma ruota sull'asse orizzontale"
                    ],
                    "correctIndex": 0,
                    "explanation": "Lo specchio deve ribaltarsi verso l'alto per consentire alla luce di raggiungere l'otturatore e il sensore/pellicola, oscurando temporaneamente il mirino."
                },
                {
                    "question": "Qual e la matrice di filtri colore piu comune utilizzata sui sensori digitali CMOS?",
                    "options": [
                        "Matrice di Bayer con schema RGGB",
                        "Filtro a gradiente neutro ND4",
                        "Matrice ortocromatica di Fresnel",
                        "Prisma dicroico a 3 canali separati"
                    ],
                    "correctIndex": 0,
                    "explanation": "La matrice di Bayer intercala filtri rossi, verdi (doppi per simulare la sensibilita dell'occhio umano) e blu sopra i fotositi monocromatici."
                },
                {
                    "question": "Quale vantaggio offre il controllo istantaneo dell'istogramma nel mirino elettronico?",
                    "options": [
                        "Permette di valutare scientificamente l'esposizione e prevenire la bruciatura delle alte luci o il clipping delle ombre",
                        "Aumenta la risoluzione nativa in megapixel del sensore",
                        "Riduce la lunghezza focale dell'obiettivo montato",
                        "Aumenta la velocita dell'otturatore meccanico"
                    ],
                    "correctIndex": 0,
                    "explanation": "L'istogramma visualizza in tempo reale la distribuzione spettrale delle luminosita nel quadro, consentendo correzioni esposimetriche precise."
                }
            ]
        },
        {
            "id": "taw-c2",
            "number": 2,
            "title": "Il Triangolo dell'Esposizione",
            "subtitle": "ISO, Diaframma, Tempo di Otturazione e Legge di Reciprocita",
            "readTime": "9 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. Definizione Scientifica dell'Esposizione

L'esposizione fotografica (valutata in Exposure Value - EV) e la quantita totale di energia luminosa incidente per unita di superficie che raggiunge il supporto fotosensibile (pellicola o sensore digitale):

$$H = E \\times t$$

dove $E$ e l'illuminamento sul piano focale e $t$ e il tempo di esposizione. Per ottenere una corretta densita tonale (esposizione calibrata sul 18% di riflettanza di grigio medio standard), l'operatore controlla tre variabili interconnesse che formano il cosiddetto **Triangolo dell'Esposizione**:

![Schema del Triangolo dell'Esposizione](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/triangolo_esposizione.png)

---

### 2. Le Tre Variabili del Triangolo

#### 1. Sensibilita ISO
- **Definizione**: Quantifica la reattivita alla luce del sensore (amplificazione del segnale analogico pre-ADC) o della pellicola (dimensione dei granuli di alogenuro).
- **Scala standard**: 100, 200, 400, 800, 1600, 3200, 6400 ISO (ogni passaggio raddoppia la sensibilita = +1 stop EV).
- **Trade-off qualitativo**:
  - *ISO bassi (50-100)*: Massima gamma dinamica, elevato rapporto segnale/rumore (SNR), resa cromatica pura.
  - *ISO alti (1600-6400+)*: Necessari con scarsa luce, ma introducono rumore elettronico (rumore di luminanza e crominanza) e degradano la gamma dinamica.

#### 2. Apertura del Diaframma (f-stop)
- **Definizione**: Meccanismo a lamelle metalliche all'interno dell'obiettivo che regola il diametro della pupilla d'ingresso.
- **Rapporto focale**: 
  $$f/N = \\frac{\\text{Lunghezza Focale}}{\\text{Diametro Apertura Netta}}$$
- **Scala normalizzata**: f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, f/16, f/22.
- **Trade-off linguistico**:
  - *Aperture ampie (f/1.4 - f/2.8)*: Grande quantita di luce, profondita di campo ridotta (*bokeh* selettivo, isolamento del soggetto dallo sfondo).
  - *Aperture strette (f/8 - f/16)*: Minore quantita di luce, estesa profondita di campo (paesaggi e architettura dove tutto deve essere nitido). Oltre f/16 interviene la perdita di nitidezza per diffrazione ottica.

#### 3. Tempo di Esposizione / Shutter Speed
- **Definizione**: Intervallo temporale durante il quale l'otturatore espone il sensore al flusso luminoso.
- **Scala standard**: ... 1/1000s, 1/500s, 1/250s, 1/125s, 1/60s, 1/30s, 1/15s, 1/8s, 1s ...
- **Trade-off dinamico**:
  - *Tempi rapidi (1/500s - 1/8000s)*: Congelamento istantaneo dell'azione e di soggetti ad alta velocita; annullamento del micromosso.
  - *Tempi lenti (1/30s - vari secondi)*: Registrazione del movimento continuo sotto forma di scia luminosa o mosso creativo (*motion blur*).

---

### 3. La Legge di Reciprocita (Bunsen-Roscoe)

La legge di reciprocita stabilisce che un'esposizione identica puo essere ottenuta combinando diversamente tempo e diaframma:

$$\\text{Esposizione Costante} = \\text{Apertura} \\times \\text{Tempo}$$

Se si chiude il diaframma di 1 stop (es. da f/2.8 a f/4, dimezzando la luce), per mantenere la medesima esposizione e tassativo raddoppiare il tempo di scatto (es. da 1/250s a 1/125s) oppure raddoppiare la sensibilita ISO (da 200 a 400).

Nel video e nel cinema web interviene inoltre la **Regola dei 180 Gradi dell'Otturatore** (*180-Degree Shutter Rule*): per ottenere un motion blur naturale che imiti la persistenza retinica umana, il tempo di otturazione deve essere calcolato come:

$$\\text{Tempo} = \\frac{1}{2 \\times \\text{Frame Rate}}$$

A 24 o 25 fps, l'otturatore deve essere impostato inderogabilmente a 1/48s o 1/50s.""",
            "keyPoints": [
                "L'esposizione e determinata dall'interazione di tre fattori: ISO, Diaframma e Tempo di Otturazione.",
                "Il diaframma f-stop e inversamente proporzionale all'apertura: numeri f piu piccoli indicano aperture piu ampie e minore profondita di campo.",
                "La sensibilita ISO amplifica il segnale del sensore ma valori elevati introducono rumore termico e di quantizzazione.",
                "Il tempo di otturazione controlla la resa del movimento, da congelato a mosso dinamico (motion blur).",
                "Nel cinema e nel video web la regola dell'otturatore a 180 gradi impone un tempo di scatto pari al doppio del frame rate (es. 1/50s a 25 fps)."
            ],
            "flashcards": [
                {
                    "question": "Quali sono i tre parametri costitutivi del Triangolo dell'Esposizione?",
                    "answer": "Sensibilita ISO, apertura del diaframma (f-stop) e tempo di esposizione (shutter speed)."
                },
                {
                    "question": "Cosa indica un numero f-stop basso (es. f/1.8) rispetto a uno alto (es. f/16)?",
                    "answer": "f/1.8 indica un'apertura fisica piu ampia che fa passare molta luce e produce profondita di campo ridotta; f/16 e un'apertura stretta con ampia profondita di campo."
                },
                {
                    "question": "Qual e la conseguenza dell'aumento incontrollato del valore ISO in condizioni di buio?",
                    "answer": "Aumento del rumore elettronico di luminanza e crominanza con contemporanea perdita di contrasto e gamma dinamica."
                },
                {
                    "question": "In cosa consiste la Legge di Reciprocita nell'esposizione fotografica?",
                    "answer": "Nell'equivalenza di esposizione ottenibile compensando la variazione di un parametro (es. -1 stop di diaframma) con l'incremento di un altro (es. +1 stop di tempo)."
                },
                {
                    "question": "Qual e la regola dell'otturatore a 180 gradi nel video a 24 o 25 frame al secondo?",
                    "answer": "Impostare lo shutter speed a 1/(2 * fps), ovvero 1/48s a 24 fps o 1/50s a 25 fps, per garantire una sfocatura di movimento naturale."
                }
            ],
            "quiz": [
                {
                    "question": "Se si passa da un'apertura f/4 a un'apertura f/2.8 a parita di ISO e tempo, cosa accade alla quantita di luce incidente?",
                    "options": [
                        "Raddoppia (+1 stop pieno)",
                        "Si dimezza (-1 stop pieno)",
                        "Quadruplica (+2 stop pieni)",
                        "Rimane rigorosamente invariata"
                    ],
                    "correctIndex": 0,
                    "explanation": "Nella scala normalizzata dei diaframmi, il passaggio da f/4 a f/2.8 corrisponde all'apertura di uno stop intero, consentendo l'ingresso del doppio della luce."
                },
                {
                    "question": "Quale combinazione di parametri e ideale per un ritratto cinematografico con soggetto isolato su sfondo fortemente sfocato?",
                    "options": [
                        "Diaframma molto aperto (f/1.8 o f/2.8) e focale medio-tele",
                        "Diaframma chiuso a f/16 e grandangolare spinto",
                        "ISO 12800 con diaframma a f/22",
                        "Tempo di scatto di 1/2 secondo con treppiede a f/11"
                    ],
                    "correctIndex": 0,
                    "explanation": "Un diaframma ampiamente aperto unito a una lunghezza focale medio-lunga crea una ridotta profondita di campo che stacca nitidamente il soggetto dallo sfondo."
                },
                {
                    "question": "Perche nell'acquisizione video a 25 frame al secondo non e consigliabile usare un tempo di 1/1000s in scene convenzionali?",
                    "options": [
                        "Perche elimina completamente il motion blur, rendendo il movimento eccessivamente scattoso e innaturale (effetto stroboscopico)",
                        "Perche impedisce al sensore di registrare i canali colore",
                        "Perche il file video MP4 generato non sarebbe compatibile con il web",
                        "Perche aumenterebbe istantaneamente la profondita di campo dell'ottica"
                    ],
                    "correctIndex": 0,
                    "explanation": "Un tempo troppo rapido annulla il fisiologico motion blur, generando movimenti a scatti innaturali per l'occhio umano privi di fluidita cinematografica."
                },
                {
                    "question": "Quale fenomeno ottico degrada la nitidezza dell'immagine quando si utilizzano aperture di diaframma estremamente chiuse come f/22 o f/32?",
                    "options": [
                        "La diffrazione ottica della luce sul bordo delle lamelle del diaframma",
                        "L'aberrazione cromatica longitudinale",
                        "La vignettatura ottica agli angoli del fotogramma",
                        "La distorsione geometrica a barilotto"
                    ],
                    "correctIndex": 0,
                    "explanation": "Quando la luce attraversa un foro microscopico (diaframma molto chiuso), le onde luminose diffrangono allargando il punto airy e riducendo il micro-contrasto."
                },
                {
                    "question": "Se si imposta la macchina da ISO 100 a ISO 400, quanti stop di sensibilita si sono guadagnati?",
                    "options": [
                        "2 stop (da 100 a 200 e da 200 a 400)",
                        "1 stop",
                        "4 stop",
                        "3 stop"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il raddoppio della sensibilita ISO corrisponde a 1 stop: da 100 a 200 e +1 stop, da 200 a 400 e un ulteriore +1 stop, per un guadagno complessivo di 2 stop."
                }
            ]
        },
        {
            "id": "taw-c3",
            "number": 3,
            "title": "Gli Obiettivi e la Lunghezza Focale",
            "subtitle": "Angolo di campo, Prospettiva, Grandangoli, Teleobiettivi e Macro",
            "readTime": "8 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. Lunghezza Focale ed Angolo di Campo

La **lunghezza focale** (espressa in millimetri, mm) e la distanza fisica tra il centro ottico dell'obiettivo (punto nodale posteriore) e il piano focale del sensore quando l'ottica e focheggiata all'infinito. La lunghezza focale determina due proprieta visive essenziali:

1. **L'Ingrandimento (*Magnification*)**: Rapporto tra le dimensioni lineari dell'immagine proiettata sul sensore e quelle del soggetto reale.
2. **L'Angolo di Campo (*Field of View - FOV*)**: Porzione di spazio angolare che l'obiettivo puo raccogliere e proiettare sul cerchio di copertura del sensore.

Tra lunghezza focale e angolo di campo vige una relazione geometrica strettamente inversa:
- Focale corta = Ampio angolo di campo visivo.
- Focale lunga = Angolo di campo ristretto ed elevato fattore di ingrandimento.

---

### 2. Tassonomia delle Ottiche Fotografiche e Cinematografiche

Su formato standard Full Frame (36x24mm), gli obiettivi si classificano rigorosamente in:

| Tipologia Ottica | Gamma Focale | Angolo di Campo | Caratteristiche Prospettiche e Linguistiche |
| :--- | :--- | :--- | :--- |
| **Fisheye (Occhio di Pesce)** | 8 - 15 mm | 180° o superiore | Deformazione curvilinea emisferica marcata, distorsione a barilotto non corretta. |
| **Grandangolare** | 16 - 35 mm | 100° - 63° | Spiccata dilatazione dei piani prospettici; enfatizza il primo piano e allontana lo sfondo. Ideale per ambienti stretti, architettura, paesaggio. |
| **Normale / Standard** | 40 - 55 mm (~50mm) | 47° - 43° | Riproduce le relazioni prospettiche naturali della visione monoculare umana. Bassa distorsione, resa realistica e sobria. |
| **Medio-Teleobiettivo** | 85 - 135 mm | 28° - 18° | Focale principe del ritratto cinematografico. Comprime delicatamente i piani senza deformare i tratti fisionomici, isola il soggetto. |
| **Super-Teleobiettivo** | 200 - 600+ mm | 12° - 4° | Schiacciamento prospettico estremo; sfondo e soggetto appaiono vicini e bidimensionali. Riprese naturalistiche, sportive, dettagli inaccessibili. |
| **Macro** | 50 - 100 mm Macro | Variabile | Schema ottico corretto per distanze di messa a fuoco ravvicinatissime, con rapporto di riproduzione nativo 1:1 (*life-size*). |

---

### 3. Prospettiva e Compressione dei Piani

Un assunto critico del linguaggio audiovisivo e che **la prospettiva non e determinata dalla lunghezza focale, ma esclusivamente dalla distanza tra la fotocamera e il soggetto**. 
- Avvicinandosi fisicamente con un grandangolo, le distanze relative tra elementi vicini e lontani appaiono enormemente dilatate.
- Allontanandosi con un teleobiettivo per mantenere la medesima inquadratura del soggetto principale, i piani spaziali di sfondo si avvicinano visivamente e le distanze si comprimono (*schiacciamento prospettico*).

Nelle ottiche cinematografiche professionali (*cine-lenses*), assumono inoltre rilevanza parametri peculiari:
- **T-stop (Transmission Stop)**: Misura fotometrica reale della luce trasmessa (che tiene conto dell'assorbimento delle lenti), fondamentale per evitare sbalzi di esposizione nel montaggio tra lenti diverse.
- **Focus Breathing**: Variazione indesiderata dell'angolo di campo durante il cambio di fuoco, minimizzata nelle ottiche cinema dedicate.""",
            "keyPoints": [
                "La lunghezza focale e la distanza tra il centro ottico dell'obiettivo e il sensore con messa a fuoco all'infinito.",
                "Focali corte (grandangoli) offrono angoli di campo ampi e dilatano la percezione delle distanze prospettiche.",
                "L'obiettivo normale (circa 50mm su Full Frame) riproduce la prospettiva naturale dell'occhio umano.",
                "I teleobiettivi comprimono i piani spaziali ravvicinando apparentemente il fondo al primo piano.",
                "Nelle ottiche per cinema e video, il T-stop misura la trasmissione reale di luce e si azzera il focus breathing."
            ],
            "flashcards": [
                {
                    "question": "Cos'e la lunghezza focale di un obiettivo?",
                    "answer": "La distanza in millimetri tra il centro ottico posteriore della lente e il sensore quando l'obiettivo e focheggiato all'infinito."
                },
                {
                    "question": "Quale effetto prospettico produce un obiettivo grandangolare da 20mm?",
                    "answer": "Offre un campo visivo ampio ed enfatizza la profondita, allontanando lo sfondo e ingigantendo gli oggetti molto vicini."
                },
                {
                    "question": "Cosa caratterizza un obiettivo standard (circa 50mm su sensore 35mm Full Frame)?",
                    "answer": "Un angolo di campo e relazioni prospettiche analoghi a quelli della visione naturale monoculare dell'occhio umano."
                },
                {
                    "question": "Perche i teleobiettivi (es. 85mm o 105mm) sono preferiti per i ritratti?",
                    "answer": "Perche consentono di stare a giusta distanza dal soggetto evitando le distorsioni prospettiche del volto (come il naso ingrandito) e comprimendo armoniosamente i lineamenti."
                },
                {
                    "question": "Cosa indica il valore T-stop rispetto al comune f-stop?",
                    "answer": "Il T-stop quantifica la luce reale effettivamente trasmessa dall'ottica al sensore al netto delle perdite per riflettanza e assorbimento vetroso."
                }
            ],
            "quiz": [
                {
                    "question": "Quale focale e considerata 'normale' su un sensore fotografico Full Frame 35mm (36x24mm)?",
                    "options": [
                        "Circa 50 mm (uguale alla diagonale del formato di 43mm)",
                        "14 mm",
                        "200 mm",
                        "300 mm"
                    ],
                    "correctIndex": 0,
                    "explanation": "L'ottica normale ha una focale all'incirca pari alla diagonale del sensore (43.3mm per il full frame, convenzionalmente arrotondata a 50mm)."
                },
                {
                    "question": "Cosa accade ai piani di profondita quando si utilizza un teleobiettivo spinto (es. 300mm)?",
                    "options": [
                        "Si verifica una compressione prospettica che fa apparire lo sfondo molto vicino al soggetto in primo piano",
                        "Lo sfondo si allontana all'infinito espandendo lo spazio",
                        "L'immagine subisce una forte curvatura a barilotto",
                        "La profondita di campo diventa infinita da 1 metro a infinito"
                    ],
                    "correctIndex": 0,
                    "explanation": "I teleobiettivi riducono l'angolo visivo e comprimono le distanze apparenti tra piani successivi, appiattendo la prospettiva tridimensionale."
                },
                {
                    "question": "Che cosa si intende per 'focus breathing' in un obiettivo durante una ripresa video?",
                    "options": [
                        "Il cambio involontario dell'inquadratura (zoom fittizio) mentre si ruota la ghiera di messa a fuoco",
                        "L'infiltrazione di polvere tra i gruppi ottici",
                        "L'oscillazione automatica del diaframma",
                        "La perdita di calibrazione del motore autofocus"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il breathing e la variazione di lunghezza focale effettiva e di campo visivo durante il passaggio del fuoco da un piano all'altro."
                },
                {
                    "question": "Quale caratteristica distingue un obiettivo macro autentico?",
                    "options": [
                        "La capacita di raggiungere un rapporto di riproduzione 1:1 sul sensore a distanza ravvicinata",
                        "La presenza di una lente addizionale grandangolare fissa",
                        "L'assenza della ghiera di messa a fuoco manuale",
                        "Un angolo di campo fisso di almeno 180 gradi"
                    ],
                    "correctIndex": 0,
                    "explanation": "Un vero obiettivo macro consente di riprodurre sul sensore un oggetto nelle sue esatte dimensioni reali (rapporto di ingrandimento 1:1)."
                },
                {
                    "question": "Da cosa dipende rigorosamente la prospettiva di un'inquadratura?",
                    "options": [
                        "Unicamente dalla posizione della cinepresa nello spazio rispetto al soggetto e allo sfondo",
                        "Dalla marca dell'obiettivo impiegato",
                        "Dal numero di lamelle che compongono il diaframma a iride",
                        "Dal tipo di file RAW o JPEG registrato"
                    ],
                    "correctIndex": 0,
                    "explanation": "La prospettiva e puramente geometrica: dipende solo dal punto di vista della camera rispetto agli elementi della scena; l'ottica si limita a ritagliarne una porzione."
                }
            ]
        },
        {
            "id": "taw-c4",
            "number": 4,
            "title": "La Scala dei Piani: Dal Primo Piano al Dettaglio",
            "subtitle": "Primo Piano, Primissimo Piano, Particolare e Dettaglio (Cut In)",
            "readTime": "9 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. Il Concetto di 'Piano' nel Linguaggio Audiovisivo

Nel sistema di codificazione cinematografica, l'**Inquadratura (*Shot*)** costituisce l'unita atomica del film, definita temporalmente dallo spazio compreso tra un REC e uno STOP e visivamente dalla porzione di spazio ritagliata dai quattro bordi del quadro.

Le inquadrature si ripartiscono convenzionalmente in due grandi famiglie:
1. **I Piani**: Inquadrature in cui la misura e definita dal **rapporto di proporzione con la figura umana**.
2. **I Campi**: Inquadrature in cui la misura e definita dal **rapporto con l'ambiente circostante e il paesaggio**.

---

### 2. Analisi Morfologica dei Piani Stretti

#### Primo Piano (Close Up - CU)
- **Delimitazione anatomica**: Inquadra il personaggio dal collo o dalla sommita delle spalle in su.
- **Funzione drammatica**: Crea una dimensione d'intimita immediata, rescinde temporaneamente la consapevolezza dell'ambiente circostante e costringe lo spettatore a focalizzarsi sull'interiorita, sulle emozioni e sui conflitti del personaggio.
- **Regola compositiva**: Raramente centrato (si applica la regola dei terzi per orientare la direzione dello sguardo verso l'area libera del fotogramma, *lead room*). Se occorre tagliare, la convenzione impone di tagliare leggermente la fronte/calotta cranica, **mai recidere il mento**.

![Primo Piano (Close Up)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/primo_piano.png)

---

#### Primissimo Piano (Extreme Close Up - ECU)
- **Delimitazione anatomica**: Il quadro e interamente occupato dal solo volto, tagliato appena sopra le sopracciglia e sotto la linea del labbro inferiore o sul mento.
- **Funzione drammatica**: Massima intensita psicologica e voyeuristica. L'attenzione e canalizzata sui micro-segnali mimici: lo sguardo, la contrazione della pupilla, il tremito labiale. Cancella ogni riferimento spaziale oggettivo.

![Primissimo Piano (Extreme Close Up)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/primissimo_piano.png)

---

### 3. La Differenza tra Particolare e Dettaglio (Cut In)

Sul piano lessicale e teorico esiste una distinzione tassativa spesso confusa nel gergo comune:

#### Il Particolare
- **Definizione**: Inquadratura estremamente ravvicinata su **una porzione anatomica del corpo umano o animale** (es. un occhio, una mano che trema, un tatuaggio sul polso, un piede che preme l'acceleratore).

![Particolare su corpo umano](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/particolare.png)

---

#### Il Dettaglio
- **Definizione**: Inquadratura ravvicinata focalizzata su **un oggetto inanimato** (es. l'orologio che scandisce l'ora x, una pistola appoggiata sul tavolo, una lettera aperta, la lancetta del contachilometri).
- **Funzione narrativa**: Fornisce un'informazione diegetica cruciale, spesso anticipando un colpo di scena (*foreshadowing*) o chiarendo un indizio invisibile nei campi ampi.

![Dettaglio su oggetto inanimato](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/dettaglio.png)""",
            "keyPoints": [
                "I piani cinematografici sono misurati in base alla porzione di figura umana inclusa nel quadro.",
                "Il Primo Piano (Close Up) va dalle spalle/collo in su ed esalta l'introspezione psicologica ed emotiva.",
                "Nel Primo Piano non si deve mai tagliare il mento: l'eventuale taglio compositivo avviene sulla fronte.",
                "Il Primissimo Piano (Extreme Close Up) isola gli occhi e la bocca, annullando totalmente il contesto spaziale.",
                "Il Particolare riguarda una frazione del corpo umano, mentre il Dettaglio riguarda un oggetto inanimato."
            ],
            "flashcards": [
                {
                    "question": "Cosa definisce la scala dei piani rispetto a quella dei campi?",
                    "answer": "I piani prendono come parametro di riferimento e proporzione la figura umana; i campi prendono come parametro l'ambiente circostante."
                },
                {
                    "question": "Quali sono i confini anatomici del Primo Piano (Close Up)?",
                    "answer": "Dal collo o dall'attaccatura delle clavicole/spalle fino alla sommita del capo."
                },
                {
                    "question": "Qual e la regola canonica di inquadratura se la testa del personaggio eccede i bordi del fotogramma?",
                    "answer": "Tagliare la sommita del cranio/fronte, preservando sempre intatta la linea del mento."
                },
                {
                    "question": "Qual e la differenza terminologica tra Particolare e Dettaglio?",
                    "answer": "Il Particolare isola una parte del corpo umano o vivente; il Dettaglio isola un oggetto inanimato."
                },
                {
                    "question": "Quale funzione psicologica svolge il Primissimo Piano (Extreme Close Up)?",
                    "answer": "Porta al culmine la tensione emotiva e la partecipazione dello spettatore, concentrando l'attenzione sui micro-movimenti espressivi del volto."
                }
            ],
            "quiz": [
                {
                    "question": "In un Primo Piano convenzionale, dove e opportuno effettuare un eventuale taglio compositivo della testa?",
                    "options": [
                        "Nella parte alta della fronte/capelli, senza mai tagliare il mento",
                        "Sotto il naso, escludendo gli occhi",
                        "Recidendo orizzontalmente il mento a meta",
                        "All'altezza esatta della gola"
                    ],
                    "correctIndex": 0,
                    "explanation": "Tagliare il mento conferisce una sensazione di soffocamento visivo sgradevole; la regola classica impone di sacrificare la calotta cranica se il volto e molto ravvicinato."
                },
                {
                    "question": "Se la cinepresa inquadra a pieno schermo una mano che stringe nervosamente un anello, di che tipo di inquadratura si tratta?",
                    "options": [
                        "Particolare (poiche il soggetto primario e una porzione del corpo umano)",
                        "Totale d'azione",
                        "Campo Lunghissimo",
                        "Piano Americano"
                    ],
                    "correctIndex": 0,
                    "explanation": "L'inquadratura ravvicinata di una parte anatomica dell'attore (mano, occhio, dita) si definisce rigorosamente 'Particolare'."
                },
                {
                    "question": "Un'inquadratura strettissima che mostra l'innesco di una bomba a orologeria e formalmente definita:",
                    "options": [
                        "Dettaglio (Cut In su oggetto inanimato)",
                        "Particolare",
                        "Mezzo Primo Piano",
                        "Establishing Shot"
                    ],
                    "correctIndex": 0,
                    "explanation": "La messa a fuoco ravvicinata su un oggetto materiale inanimato prende il nome tecnico di Dettaglio."
                },
                {
                    "question": "Cosa caratterizza il Primissimo Piano (Extreme Close Up) dal punto di vista dello spazio filmico circostante?",
                    "options": [
                        "Annulla completamente qualsiasi relazione visiva con l'ambiente e lo spazio geografico",
                        "Mostra la figura umana interamente immersa nel paesaggio naturale",
                        "Mantiene sempre visibili le mani e i gesti del personaggio",
                        "Coincide sempre con il master shot della scena"
                    ],
                    "correctIndex": 0,
                    "explanation": "L'Extreme Close Up riempie il fotogramma con il solo volto, cancellando ogni riferimento all'ambiente circostante a favore della pura dimensione psicologica."
                },
                {
                    "question": "Perche nel Primo Piano il volto dell'attore non viene solitamente posizionato al centro geometrico perfetto del quadro?",
                    "options": [
                        "Per lasciare spazio vuoto nella direzione verso cui il personaggio rivolge lo sguardo (lead room), rendendo la composizione armonica e naturale",
                        "Per motivi di risparmio di banda nella compressione digitale",
                        "Perche gli obiettivi reflex non riescono a focheggiare al centro",
                        "Per evitare riflessi nell'oculare del mirino"
                    ],
                    "correctIndex": 0,
                    "explanation": "Applicando la regola dei terzi, si lascia aria di sguardo (lead room o nose room) nella direzione verso cui il soggetto e rivolto per dare respiro all'azione."
                }
            ]
        },
        {
            "id": "taw-c5",
            "number": 5,
            "title": "Piani Intermedi e Figura Umana",
            "subtitle": "Mezzo Busto, Piano Medio, Piano Americano (Cowboy Shot) e Figura Intera",
            "readTime": "9 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. I Piani di Transizione: Uomo e Contesto Immediato

Mentre i piani stretti isolano il volto, i piani intermedi costruiscono la dialettica visiva tra il personaggio, la sua gestualita corporea e l'ambiente immediato con cui interagisce.

---

### 2. Tipologie di Piani Intermedi

#### 1. Mezzo Primo Piano / Mezzo Busto (Medium Close Up - MCU)
- **Delimitazione anatomica**: Inquadra il personaggio dal petto in su.
- **Caratteristiche**: Lascia aria sopra la testa (*headroom*) e permette di scorgere elementi contestuali dello sfondo. E il piano standard dei telegiornali, delle interviste broadcast e dei dialoghi a media distanza emotiva.

![Mezzo Primo Piano (Medium Close Up)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/mezzo_primo_piano.png)

---

#### 2. Piano Medio / Mezza Figura (Mid Shot - MS)
- **Delimitazione anatomica**: La figura umana e ripresa dalla vita (cintura) in su.
- **Caratteristiche**: Pone in perfetto equilibrio la mimica facciale e il movimento delle braccia e delle mani. E ideale per conversazioni tra due o tre personaggi (*Two Shot / Three Shot*) e per mostrare azioni pratiche (scrivere, maneggiare un oggetto).

![Piano Medio (Mid Shot)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/piano_medio.png)

---

#### 3. Piano Americano (Cowboy Shot - MLS)
- **Delimitazione anatomica**: Taglia la figura umana appena **sopra o sotto il ginocchio** (mai esattamente sull'articolazione del ginocchio).
- **Genesi storica e linguistica**: Nacque a Hollywood negli anni '30-'40 nei capolavori del cinema Western (John Ford, Howard Hawks). I registi necessitavano di un'inquadratura che mantenesse visibili sia le espressioni dei pistoleri, sia la fondina con il revolver allacciata alla coscia durante i duelli. 
- Oggi e un piano narrativo fondamentale per scene d'azione, duelli e confronti dinamici.

![Piano Americano (Cowboy Shot)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/piano_americano.png)

---

#### 4. Figura Intera (Full Shot - FS)
- **Delimitazione anatomica**: La figura umana e rappresentata per intero, dai piedi alla testa.
- **Proporzione aurea classica**: La convenzione compositiva prescrive circa **2/3 di fotogramma occupati dalla figura umana e 1/3 di aria** distribuito armonicamente tra lo spazio sotto i piedi e l'aria sopra la testa.
- **Funzione**: Identifica la postura corporea, il movimento nello spazio scenico e l'abbigliamento completo del personaggio. Costituisce il confine di transizione verso i Campi ambientali.

![Figura Intera (Full Shot)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/figura_intera.png)""",
            "keyPoints": [
                "Il Mezzo Busto (Medium Close Up) inquadra dal petto in su ed e tipico dei dialoghi informativi e televisivi.",
                "Il Piano Medio (Mid Shot) taglia all'altezza della vita, bilanciando espressioni del volto e gestualita delle mani.",
                "Il Piano Americano taglia sopra il ginocchio; nacque nel genere Western per inquadrare la pistola nella fondina.",
                "La Figura Intera (Full Shot) mostra il personaggio completo dai piedi al capo.",
                "Nella Figura Intera si applica la proporzione 2/3 figura umana e 1/3 aria distribuita tra testa e piedi."
            ],
            "flashcards": [
                {
                    "question": "Da dove taglia la figura umana il Mezzo Primo Piano (Mezzo Busto)?",
                    "answer": "Dalla meta del torace / petto in su, lasciando una quantita controllata di aria sopra la testa."
                },
                {
                    "question": "Qual e il limite anatomico del Piano Medio (Mid Shot)?",
                    "answer": "La linea della vita / cintura: inquadra la figura umana dalla vita in su."
                },
                {
                    "question": "Perche nacque il 'Piano Americano' nel cinema?",
                    "answer": "Perche nei film Western era indispensabile inquadrare contemporaneamente il volto dell'attore e la fondina con la pistola allacciata al femore sopra il ginocchio."
                },
                {
                    "question": "Quale proporzione si usa convenzionalmente per comporre la Figura Intera?",
                    "answer": "Due terzi dello spazio verticale per la figura umana e un terzo di aria complessiva ripartita tra piedi e testa."
                },
                {
                    "question": "Qual e il pericolo compositivo da evitare nel taglio del Piano Americano?",
                    "answer": "Non tagliare mai esattamente sulla linea dell'articolazione del ginocchio, ma leggermente sopra o sotto di essa."
                }
            ],
            "quiz": [
                {
                    "question": "Quale genere cinematografico ha storicamente imposto la codifica del 'Piano Americano'?",
                    "options": [
                        "Il genere Western classico americano",
                        "Il musical di Broadway",
                        "Il cinema espressionista tedesco",
                        "Il neorealismo italiano"
                    ],
                    "correctIndex": 0,
                    "explanation": "I registi dei film Western avevano l'esigenza impellente di mostrare il duello mantenendo a fuoco sia lo sguardo del cowboy sia la pistola nel fodero alla coscia."
                },
                {
                    "question": "Dove si arresta la cornice inferiore nel Piano Medio classico (Mid Shot)?",
                    "options": [
                        "All'altezza della cintura / vita del personaggio",
                        "Sulle caviglie",
                        "Sotto la gola",
                        "Esattamente sulla sommita del ginocchio"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il Piano Medio inquadra la persona dalla vita in su, rendendo pienamente visibile la gestualita manuale pur conservando la lettura del volto."
                },
                {
                    "question": "Qual e la ripartizione standard dell'altezza del fotogramma in una Figura Intera (Full Shot)?",
                    "options": [
                        "2/3 occupati dall'altezza della figura umana e 1/3 di aria suddivisa tra testa e piedi",
                        "90% aria e 10% figura umana",
                        "1/2 figura umana e 1/2 sfondo vuoto",
                        "La testa e i piedi devono toccare fisicamente i bordi superiore e inferiore"
                    ],
                    "correctIndex": 0,
                    "explanation": "La regola classica richiede respiro compositivo: circa 2/3 dedicati al corpo umano per intero e 1/3 distribuito tra margine inferiore e margine superiore."
                },
                {
                    "question": "Quale tipo di inquadratura e piu funzionale per mostrare un'interazione dinamica a due (Two Shot) in una conversazione al tavolino di un bar?",
                    "options": [
                        "Piano Medio (Mid Shot)",
                        "Primissimo Piano",
                        "Campo Lunghissimo",
                        "Particolare"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il Piano Medio accoglie comodamente due attori seduti al tavolo, permettendo di seguire contemporaneamente dialoghi, mimica e gesti."
                },
                {
                    "question": "Cosa si intende per 'Headroom' nella composizione di un Mezzo Busto cinematografico?",
                    "options": [
                        "Lo spazio vuoto lasciato intenzionalmente tra la sommita del capo dell'attore e il bordo superiore dell'inquadratura",
                        "Il volume della traccia audio della voce narrante",
                        "La distanza tra gli occhi dell'attore e la luce principale",
                        "Il tempo di riverbero acustico della stanza"
                    ],
                    "correctIndex": 0,
                    "explanation": "L'headroom (o aria in testa) e lo spazio verticale libero necessario sopra la testa per evitare che l'inquadratura appaia compressa o tagliata male."
                }
            ]
        },
        {
            "id": "taw-c6",
            "number": 6,
            "title": "La Scala dei Campi e lo Spazio Fuori Campo",
            "subtitle": "Totale (Master), Campo Medio, Lungo, Lunghissimo e la dialettica In/Out",
            "readTime": "10 min",
            "module": "taw-camera-linguaggio",
            "summary": """### 1. La Dialettica tra Campo e Fuori Campo

Nel cinema, il **Campo** e tutto cio che si trova all'interno della cornice delimitata dai quattro bordi del fotogramma. Il **Fuori Campo (*Off-Screen Space*)** e tutto cio che, pur essendo escluso dalla vista, appartiene alla realta diegetica del film e interagisce attivamente con l'immagine.
Secondo la celebre teorizzazione di Noel Burch, esistono sei segmenti di fuori campo:
1. I quattro bordi dello schermo (a destra, a sinistra, in alto, in basso).
2. Lo spazio situato dietro la scenografia (oltre porte, finestre, pareti).
3. Lo spazio collocato dietro la macchina da presa (il punto di vista dello spettatore/regista).

La tensione filmica nasce spesso da elementi che entrano dal fuori campo o da sguardi, suoni ed ombre di entita non ancora mostrate.

---

### 2. Tassonomia della Scala dei Campi

#### 1. Il Totale (Master Shot)
- **Definizione**: E lo spartiacque assoluto tra la scala dei piani e la scala dei campi. Inquadra **tutto l'ambiente in cui si svolge l'azione scenica**, contenendo tutti i personaggi coinvolti.
- **Funzione sul set**: Viene registrato come inquadratura guida (*Master*) dell'intera sequenza per consentire agli attori di recitare la scena per intero; successivamente si registrano i piani ravvicinati (*coverage*) che verranno innestati nel montaggio.

![Totale (Master Shot)](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/totale_master.png)

---

#### 2. Campo Medio (Medium Long Shot)
- **Definizione**: La figura umana e l'ambiente circostante si trovano in una condizione di **perfetto equilibrio ponderale**. L'azione drammatica e chiaramente leggibile nel contesto immediato.
- **Uso pratico**: Sul set la dicitura 'campo medio' viene sovente assimilata a totale o campo lungo a seconda delle proporzioni architettoniche.

![Campo Medio](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/campo_medio.png)

---

#### 3. Campo Lungo (Long Shot - LS)
- **Definizione**: L'ambiente e l'architettura circostante predominano nettamente sulla figura umana. Tuttavia, il personaggio rimane distintamente visibile, identificabile e monitorabile nei suoi spostamenti.
- **Funzione**: Contestualizza le traiettorie dei personaggi nel paesaggio o nella citta; stabilisce il respiro narrativo e la distanza dell'osservatore.

![Campo Lungo](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/campo_lungo.png)

---

#### 4. Campo Lunghissimo (Extreme Long Shot - ELS)
- **Definizione**: L'ambiente naturale o metropolitano e l'assoluto protagonista dell'inquadratura. L'estensione prospettica e cosi vasta che l'essere umano risulta invisibile o ridotto a un dettaglio microscopico.
- **Funzione estetica ed esistenziale**: Esprime il sentimento del Sublime, l'isolamento dell'uomo di fronte alle forze della natura, la solitudine o l'infinita vastita dello spazio cosmico/geografico (es. i paesaggi della Monument Valley di John Ford o le distese desertiche di *Lawrence d'Arabia* di David Lean).

![Campo Lunghissimo](assets/corsi/dapl08/anno-1/tecniche-audiovisive/images/campo_lunghissimo.png)""",
            "keyPoints": [
                "Il Campo e lo spazio delimitato dal quadro; il Fuori Campo e lo spazio invisibile ma diegeticamente attivo.",
                "Il Totale (Master) inquadra l'intero ambiente d'azione ed e l'architettura portante su cui si monta la scena.",
                "Nel Campo Medio figura umana e ambiente hanno pari peso visivo e l'azione e chiaramente leggibile.",
                "Nel Campo Lungo domina l'ambiente, ma la persona e perfettamente riconoscibile.",
                "Nel Campo Lunghissimo l'ambiente domina in modo assoluto e la presenza umana e infinitesimale o assente."
            ],
            "flashcards": [
                {
                    "question": "Cosa si intende per Fuori Campo (Off-Screen Space)?",
                    "answer": "Tutto cio che e escluso dai bordi visibili del quadro ma che esiste nell'universo del racconto e influenza la scena attraverso suoni, sguardi o entrate."
                },
                {
                    "question": "Qual e il ruolo del Totale (Master Shot) nella lavorazione di una scena?",
                    "answer": "Inquadrare l'intera area d'azione e tutti i personaggi per fornire la continuita temporale e spaziale su cui inserire i piani stretti."
                },
                {
                    "question": "Qual e la caratteristica distintiva del Campo Medio?",
                    "answer": "L'equilibrio dimensionale tra la figura umana e l'ambiente circostante, con l'azione scenica pienamente riconoscibile."
                },
                {
                    "question": "Cosa differenzia un Campo Lungo da un Campo Lunghissimo?",
                    "answer": "Nel Campo Lungo il personaggio e ancora chiaramente individuabile nell'ambiente; nel Lunghissimo l'ambiente e dominante assoluto e l'umano e invisibile o puntiforme."
                },
                {
                    "question": "Quale sentimento estetico e storicamente associato al Campo Lunghissimo?",
                    "answer": "Il sentimento del Sublime, della solitudine esistenziale e della sproporzione tra la vastita della natura e l'individuo."
                }
            ],
            "quiz": [
                {
                    "question": "In quale inquadratura l'ambiente naturale e protagonista indiscusso e la figura umana e assente o ridotta a un punto impercettibile?",
                    "options": [
                        "Campo Lunghissimo (Extreme Long Shot)",
                        "Campo Medio",
                        "Totale (Master)",
                        "Figura Intera"
                    ],
                    "correctIndex": 0,
                    "explanation": "Nel Campo Lunghissimo lo sguardo spazia su orizzonti immensi in cui la figura umana annega nel paesaggio, esaltando la vastita dell'ambiente."
                },
                {
                    "question": "Perche il 'Totale' viene tradizionalmente battezzato 'Master Shot' dalla troupe sul set cinematografico?",
                    "options": [
                        "Perche e la ripresa complessiva che registra l'intera sequenza dall'inizio alla fine, fungendo da matrice di montaggio",
                        "Perche viene scattata solo dal produttore esecutivo",
                        "Perche richiede un obiettivo da un milione di euro",
                        "Perche e l'unica inquadratura che non ha bisogno di audio"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il Master Shot serve da scheletro strutturale per il montatore per orientarsi nello spazio prima di staccare sui raccordi e sui primi piani."
                },
                {
                    "question": "Quanti segmenti di spazio fuori campo ha teorizzato lo studioso Noel Burch?",
                    "options": [
                        "6 segmenti (i 4 lati del quadro, lo spazio dietro la scenografia e lo spazio dietro la mdp)",
                        "Solo 2 (destra e sinistra)",
                        "12 segmenti come le ore del quadrante",
                        "Nessuno, il fuori campo non e classificabile"
                    ],
                    "correctIndex": 0,
                    "explanation": "Noel Burch formalizza 6 zone: i quattro bordi del frame, l'area invisibile oltre la scenografia/sfondo e lo spazio retrostante la camera (dove risiede l'operatore)."
                },
                {
                    "question": "Quale elemento filmico puo evocare con massima efficacia la presenza del Fuori Campo senza mostrare visivamente l'azione?",
                    "options": [
                        "Il sonoro diegetico (es. passi minacciosi, uno sparo fuori scena, una voce lontana) e lo sguardo attento dell'attore",
                        "L'aumento della frequenza dei fotogrammi a 120 fps",
                        "L'esportazione del file in codec ProRes 4444",
                        "La chiusura dell'otturatore a 360 gradi"
                    ],
                    "correctIndex": 0,
                    "explanation": "Il suono acusmatico (di cui si sente la fonte senza vederla) e la direzione dello sguardo degli attori sono i motori primari del fuori campo."
                },
                {
                    "question": "In un Campo Lungo cinematografico:",
                    "options": [
                        "L'ambiente e dominante, ma l'azione e la figura umana rimangono chiaramente percepibili e leggibili",
                        "La figura umana e tagliata dalle ginocchia in su",
                        "Non e possibile utilizzare alcuna illuminazione artificiale",
                        "La durata dell'inquadratura non puo superare i 2 secondi"
                    ],
                    "correctIndex": 0,
                    "explanation": "Nel Campo Lungo l'ambiente prevale visivamente ma la figura umana mantiene una dimensione sufficiente per essere individuata e seguita nei movimenti."
                }
            ]
        }
    ]

if __name__ == "__main__":
    chaps = get_module_1_chapters()
    print(f"Modulo 1 generato con successo: {len(chaps)} capitoli.")
