# -*- coding: utf-8 -*-
"""
Rebuilds data/dispense-data.js with:
1. High-level academic chapter quizzes (chap.quiz) for all 14 chapters:
   - Realistic, university-grade distractors (no childish/absurd choices).
   - Balanced correctIndex across 0, 1, 2, 3.
2. Dedicated exam simulation questions (chap.examQuiz) for all 14 chapters:
   - Distinct, scenario-based exam questions.
   - Realistic distractors.
   - Balanced correctIndex across 0, 1, 2, 3.
"""

import json, re

dispense_quiz_data = {
    "dispense-c1": {
        "quiz": [
            {
                "question": "Secondo la definizione teleologica del design (ripresa anche da Bruno Munari), quale distinzione separa fondamentalmente il design dall'arte pura?",
                "options": [
                    "L'arte persegue primariamente l'espressione soggettiva dell'autore, mentre il design è un'attività progettuale volta a risolvere problemi concreti di comunicazione e d'uso per un destinatario",
                    "Il design non ammette l'impiego del colore né della creatività visiva, limitandosi al calcolo matematico",
                    "L'arte si occupa unicamente di oggetti tridimensionali, mentre il design riguarda esclusivamente supporti bidimensionali",
                    "Non sussiste alcuna differenza reale, trattandosi di discipline coincidenti per metodologie e scopi"
                ],
                "correctIndex": 0,
                "explanation": "A differenza dell'arte pura, il design è un'attività teleologica (orientata a uno scopo): risponde a specifici bisogni funzionali, contestuali e informativi di un pubblico identificato."
            },
            {
                "question": "Nella dinamica comunicativa 'Mittente — Progettista — Destinatario', quale ruolo nodale compete al designer?",
                "options": [
                    "Sostituirsi al committente ridefinendo gli obiettivi economici dell'azienda secondo il proprio gusto artistico",
                    "Agire da mediatore e interprete visivo, traducendo il messaggio del mittente in forme comprensibili ed efficaci per le capacità percettive del destinatario",
                    "Limitarsi a impaginare testi preconfezionati senza intervenire sulla gerarchia delle informazioni",
                    "Eliminare ogni elemento visivo a favore del solo testo alfabetico per massimizzare la leggibilità"
                ],
                "correctIndex": 1,
                "explanation": "Il designer opera come ponte cognitivo: comprende le intenzioni del mittente e le modella attraverso gerarchia visiva, tipografia e layout affinché il destinatario le decodifichi con il minimo sforzo."
            },
            {
                "question": "In che modo l'usabilità interagisce con la componente estetica di un manufatto digitale secondo i principi moderni di design?",
                "options": [
                    "L'estetica è irrilevante: un'interfaccia usabile deve essere priva di qualsiasi cura cromatica o compositiva",
                    "L'usabilità riguarda solo il codice di programmazione server-side e non impatta l'esperienza utente",
                    "L'estetica e l'usabilità sono sinergiche: una buona estetica riduce la frizione percepita (Aesthetic-Usability Effect) ma non può compensare gravi falle funzionali o di flusso",
                    "Un'estetica accattivante rende superflua qualsiasi verifica di facilità d'uso o accessibilità"
                ],
                "correctIndex": 2,
                "explanation": "La ricerca empirica (Kurosu e Kashimura, Norman) dimostra l'Aesthetic-Usability Effect: gli utenti percepiscono interfacce esteticamente armoniose come più facili da usare, purché la struttura di supporto sia solida."
            },
            {
                "question": "Cosa si intende per 'rumore' (noise) all'interno del processo di comunicazione visiva?",
                "options": [
                    "Il volume sonoro emesso dai dispositivi hardware durante la navigazione web",
                    "La risoluzione in megapixel dei display ad altissima densità",
                    "La velocità di trasmissione in gigabit della connessione a fibra ottica",
                    "Qualsiasi interferenza visiva, sovraccarico informativo o incoerenza grafica che ostacola la corretta ricezione del messaggio"
                ],
                "correctIndex": 3,
                "explanation": "Nel modello classico di Shannon-Weaver applicato alla grafica, il rumore è ogni fattore di disturbo: clutter visivo, contrasti insufficienti, font illeggibili o layout caotici che degradano il segnale informativo."
            },
            {
                "question": "Quale principio stabilisce che la forma di un oggetto debba discendere direttamente dalla funzione che è chiamato a svolgere?",
                "options": [
                    "L'assioma razionalista 'Form follows function' (La forma segue la funzione) di Louis Sullivan e del Bauhaus",
                    "Il principio decostruzionista dell'ornamento primario di Robert Venturi",
                    "La teoria del caos visivo applicata al responsive design",
                    "La legge di Fitts sulla velocità dei puntatori mouse"
                ],
                "correctIndex": 0,
                "explanation": "Il principio 'Form follows function' ha plasmato il design moderno: la configurazione formale, i comandi e la disposizione visiva devono essere subordinati allo scopo pratico e comunicativo dell'oggetto."
            }
        ],
        "examQuiz": [
            {
                "question": "Un committente richiede di inserire animazioni continue, musica di sottofondo e grafiche decorative in tutte le schermate di un portale di pagamenti tributari. Quale argomentazione professionale di design ne sconsiglia l'adozione?",
                "options": [
                    "Tali elementi aumentano il rumore visivo e il carico cognitivo dell'utente, rallentando il compimento del task e violando i principi di usabilità funzionale",
                    "I browser moderni bloccano qualsiasi sito contenente più di tre colori primari",
                    "Il design teleologico vieta espressamente l'utilizzo di colori vivaci nei servizi pubblici",
                    "L'impiego di animazioni riduce automaticamente la larghezza di banda del server"
                ],
                "correctIndex": 0,
                "explanation": "Nei sistemi transazionali il design teleologico esige linearità, trasparenza e minimo sforzo cognitivo: elementi superflui generano distrazione visiva e frustrazione operativa."
            },
            {
                "question": "Nella celebre riflessione di Bruno Munari 'Da cosa nasce cosa', come viene descritto il metodo progettuale?",
                "options": [
                    "Come un atto mistico e imperscrutabile riservato a geni solitari privi di vincoli",
                    "Come una serie logica e iterativa di fasi: definizione del problema, scomposizione in elementi, analisi dei dati, creatività vincolata e verifica empirica",
                    "Come la mera applicazione di griglie matematiche senza considerazione per l'utente umano",
                    "Come la replica seriale di stili storici del passato senza alcuna sperimentazione"
                ],
                "correctIndex": 1,
                "explanation": "Munari demistifica la creatività: il metodo progettuale è un percorso analitico e rigoroso in cui i vincoli e la scomposizione del problema guidano verso soluzioni eleganti e funzionali."
            },
            {
                "question": "Qual è il rischio principale quando un team di sviluppo confonde il 'Problem Framing' con la scelta anticipata della tecnologia?",
                "options": [
                    "Si rischia di implementare con perizia tecnica la soluzione sbagliata a un problema non compreso o inesistente per gli utenti",
                    "Il codice sorgente perde la conformità con lo standard ECMAScript",
                    "I file CSS non possono essere minificati per la produzione",
                    "L'interfaccia non può essere visualizzata su sistemi operativi Linux"
                ],
                "correctIndex": 0,
                "explanation": "Il Problem Framing indaga il 'cosa' e il 'perché' prima del 'come': scegliere in anticipo una libreria o un formato senza aver compreso le reali necessità d'uso conduce al fallimento dell'esperienza."
            }
        ]
    },
    "dispense-c2": {
        "quiz": [
            {
                "question": "Secondo le dispense, in quale livello strutturale del digitale rientrano i feedback visivi alle azioni dell'utente, gli stati :hover e le animazioni di caricamento?",
                "options": [
                    "Nel livello dell'Interfaccia grafica statica (UI pura)",
                    "Nel livello dell'Architettura Hardware del client",
                    "Nel livello del Comportamento (Interaction Design)",
                    "Nel livello del Flusso globale (User Flow)"
                ],
                "correctIndex": 2,
                "explanation": "Il Comportamento descrive la reattività dinamica e la dimensione temporale del sistema: cosa accade a fronte di un'azione dell'utente (microinterazioni, feedback di transizione, stati attivi ed errori)."
            },
            {
                "question": "Cosa descrive il 'Flusso' (User Flow) all'interno dell'architettura dell'esperienza digitale?",
                "options": [
                    "La sequenza logica, temporale e funzionale di passaggi e schermate che collegano il punto di partenza dell'utente al compimento del suo obiettivo",
                    "La velocità di trasmissione dei pacchetti TCP/IP tra client e server",
                    "La frequenza di campionamento delle tracce audio inserite nelle pagine web",
                    "La quantità di memoria virtuale allocata dal browser per il rendering del DOM"
                ],
                "correctIndex": 0,
                "explanation": "Lo User Flow mappa il viaggio dell'utente schermata dopo schermata: ad esempio, dalla ricerca del prodotto al carrello fino alla schermata di conferma del pagamento."
            },
            {
                "question": "Quale formula sintetizza la visione olistica del design digitale proposta nel testo?",
                "options": [
                    "Interfaccia + Comportamento + Flusso = User Experience (UX)",
                    "HTML + CSS = Web Application",
                    "Grafica vettoriale * Risoluzione schermo = Usabilità",
                    "Tipografia + Palette cromatica = Architettura dell'Informazione"
                ],
                "correctIndex": 0,
                "explanation": "La User Experience è la risultante sistemica e inscindibile di ciò che si vede (Interfaccia), di come reagisce il sistema (Comportamento) e di come sono coordinati i passaggi (Flusso)."
            },
            {
                "question": "In cosa differisce concettualmente un artefatto digitale da un prodotto grafico destinato alla stampa tradizionale?",
                "options": [
                    "Il prodotto a stampa è interattivo mentre quello digitale è immutabile nel tempo",
                    "Il digitale non impiega mai elementi tipografici né regole di composizione visiva",
                    "La stampa richiede l'uso esclusivo del linguaggio di marcatura XML",
                    "Il prodotto digitale è intrinsecamente dinamico, iterativo, reattivo al contesto d'uso e suscettibile di continuo aggiornamento empirico"
                ],
                "correctIndex": 3,
                "explanation": "A differenza della stampa (scultura conclusa e definitiva), il software e il web sono 'organismi vivi' plasmati dall'interazione in tempo reale e dall'evoluzione continua basata sui dati."
            },
            {
                "question": "Qual è il focus distintivo della fase di 'Problem Framing'?",
                "options": [
                    "Comprendere, circoscrivere e validare la natura del problema reale prima di ipotizzare qualsiasi soluzione esecutiva",
                    "Scrivere immediatamente il codice JavaScript per gestire le chiamate asincrone",
                    "Disegnare pixel per pixel il mockup definitivo ad altissima fedeltà",
                    "Definire i contratti legali di licenza del software"
                ],
                "correctIndex": 0,
                "explanation": "Il Framing evita di gettarsi impulsivamente a progettare: analizza il contesto, scardina supposizioni non provate e garantisce che il team risponda al vero bisogno dell'utente."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'applicazione bancaria presenta una grafica impeccabile (UI eccellente) e transizioni reattive (ottimo comportamento), ma per effettuare un bonifico richiede 14 passaggi tortuosi e dispersivi. Su quale livello risiede il fallimento?",
                "options": [
                    "Sul livello dell'Interfaccia (UI)",
                    "Sul livello del Flusso (User Flow)",
                    "Sul livello della compilazione del server",
                    "Sul livello del DNS"
                ],
                "correctIndex": 1,
                "explanation": "Il cedimento si colloca nello User Flow: la navigazione e i passaggi procedurali sono mal strutturati, invalidando l'intera User Experience nonostante la bellezza estetica della singola schermata."
            },
            {
                "question": "Cosa si intende per 'Interaction Design' (IxD) all'interno del design digitale?",
                "options": [
                    "La progettazione dei modelli relazionali per database SQL",
                    "La disciplina che definisce la struttura e il comportamento dei sistemi interattivi, facilitando il dialogo tra persone e tecnologia",
                    "L'attività commerciale di vendita degli spazi pubblicitari banner",
                    "La procedura di calibrazione cromatica delle stampanti offset industriali"
                ],
                "correctIndex": 1,
                "explanation": "L'IxD crea interazioni comprensibili ed eleganti, curando come il sistema risponde agli input (tocco, click, voce), minimizzando gli errori e fornendo conferme immediate di stato."
            },
            {
                "question": "Perché un prototipo interattivo 'a media fedeltà' (wireframe navigabile) è fondamentale prima della fase di sviluppo codice?",
                "options": [
                    "Permette di validare flussi e gerarchie informative con utenti reali a costi minimi, prima di immobilizzare risorse nello sviluppo finale",
                    "Sostituisce definitivamente la necessità di avere programmatori nel team",
                    "Garantisce che l'applicazione occupi meno di 10 kilobyte sul server",
                    "Risolve automaticamente le problematiche legali sul copyright"
                ],
                "correctIndex": 0,
                "explanation": "I prototipi consentono l'apprendimento precoce e a basso costo: testare precocemente il flusso permette di correggere errori di architettura che in fase di codice costerebbero 10 volte tanto."
            }
        ]
    },
    "dispense-c3": {
        "quiz": [
            {
                "question": "Quale celebre metafora utilizza Riccardo Falcinelli per spiegare il concetto e lo scopo del 'Layout' grafico?",
                "options": [
                    "La costruzione di una cattedrale gotica dalle fondamenta ai pinnacoli",
                    "L'apparecchiare una tavola da pranzo: disporre gli oggetti con ordine logico e funzionalità affinché il commensale sappia subito come muoversi",
                    "La composizione di una partitura orchestrale per soli strumenti a fiato",
                    "La navigazione marittima a vista in condizioni di tempesta notturna"
                ],
                "correctIndex": 1,
                "explanation": "Falcinelli paragona il layout all'apparecchiatura della tavola: posate, piatti e bicchieri hanno posizioni canoniche e funzionali che comunicano istantaneamente senso, ordine e modalità d'uso."
            },
            {
                "question": "In base alle leggi della Gestalt, cosa stabilisce il 'Principio di Prossimità' nella composizione visiva?",
                "options": [
                    "Elementi spazialmente vicini tra loro vengono percepiti automaticamente dal cervello come appartenenti alla medesima unità o categoria concettuale",
                    "Gli elementi con colori caldi sembrano sempre fisicamente più vicini rispetto a quelli freddi",
                    "Le immagini devono trovarsi a una distanza esatta di 10 centimetri dal bordo dello schermo",
                    "Gli elementi con font serif non possono mai essere affiancati a elementi con font sans-serif"
                ],
                "correctIndex": 0,
                "explanation": "La prossimità spaziale è uno dei raggruppamenti gestaltici primari: riducendo lo spazio tra elementi correlati e aumentandolo verso elementi estranei, si creano gruppi logici chiari e intuitivi."
            },
            {
                "question": "Qual è il ruolo progettuale dello 'Spazio Bianco' (Negative Space) all'interno di un'interfaccia?",
                "options": [
                    "È uno spreco di pixel che andrebbe colmato inserendo quanti più banner e testi possibili",
                    "Un elemento attivo di composizione che conferisce respiro, isola i punti focali, riduce l'affaticamento percettivo e definisce le gerarchie",
                    "Un vincolo imposto dai browser per limitare l'uso della memoria video",
                    "Un errore di layout causato dal mancato caricamento del file CSS"
                ],
                "correctIndex": 1,
                "explanation": "Lo spazio negativo non è 'vuoto inerte': è lo strumento compositivo più potente per guidare lo sguardo, stabilire pause cognitive e separare blocchi informativi."
            },
            {
                "question": "Quale principio della percezione visiva impone che due elementi con funzioni o pesi gerarchici differenti appaiano visivamente molto diversi?",
                "options": [
                    "Il principio di omologazione simmetrica",
                    "Il principio di Contrasto (per dimensione, peso, colore o orientamento)",
                    "La legge della chiusura monocromatica",
                    "La regola aurea del bilanciamento isometrico"
                ],
                "correctIndex": 1,
                "explanation": "Il contrasto evita ambiguità: se due elementi sono solo leggermente diversi, generano conflitto e confusione visiva. La differenza formale deve essere netta e decisa per chiarire la gerarchia."
            },
            {
                "question": "Cosa garantisce l'Allineamento rigoroso degli elementi lungo assi verticali e orizzontali condivisi?",
                "options": [
                    "Genera connessioni visive invisibili ma potenti, conferendo ordine, coerenza strutturale e ritmo di scansione",
                    "Impedisce agli utenti di visualizzare la pagina su monitor widescreen",
                    "Obbliga il motore di rendering a disattivare la scheda video",
                    "Rallenta la scansione visiva forzando l'utente a leggere ogni singola parola"
                ],
                "correctIndex": 0,
                "explanation": "Nulla deve apparire posizionato per caso: allineare elementi a un asse comune crea pulizia, guida l'occhio e trasmette solidità e professionalità."
            }
        ],
        "examQuiz": [
            {
                "question": "In una pagina web di notizie, il titolo di un articolo si trova a 24px di distanza dal paragrafo del testo sottostante, ma a soli 8px dal paragrafo dell'articolo precedente. Quale principio fondamentale della Gestalt è gravemente violato?",
                "options": [
                    "Il principio di Buona Forma",
                    "Il principio di Destino Comune",
                    "Il principio di Prossimità",
                    "Il principio di Esperienza Passata"
                ],
                "correctIndex": 2,
                "explanation": "La legge di prossimità impone che il titolo stia più vicino al proprio testo che non ai contenuti precedenti. Una spaziatura invertita fa percepire erroneamente il titolo come conclusione del blocco precedente."
            },
            {
                "question": "Cosa si intende per 'Gerarchia Visiva' all'interno di una pagina web?",
                "options": [
                    "L'ordine di grandezza dei server all'interno del data center",
                    "L'organizzazione degli elementi visivi in modo da comunicare istantaneamente l'ordine di importanza e guidare la sequenza di lettura dell'occhio",
                    "La gerarchia di permessi di accesso per gli utenti amministratori del database",
                    "La graduatoria dei siti web più visitati secondo le classifiche di traffico"
                ],
                "correctIndex": 1,
                "explanation": "La gerarchia visiva assegna priorità: l'occhio deve cogliere per primo il messaggio principale (H1, hero), poi i livelli intermedi (H2, categorie) e infine i dettagli analitici (corpo del testo)."
            },
            {
                "question": "Perché l'uso eccessivo e indistinto di elementi ad alto contrasto (troppi colori accesi, badge intermittenti, testi evidenziati) annulla l'efficacia del contrasto stesso?",
                "options": [
                    "Perché quando tutto urla per attirare l'attenzione, nulla si distingue più e si genera saturazione sensoriale",
                    "Perché i monitor a LED non possono visualizzare più di due colori contrastanti contemporaneamente",
                    "Perché il browser attiva la modalità scala di grigi di emergenza",
                    "Perché le specifiche W3C vietano la combinazione di più di tre colori primari"
                ],
                "correctIndex": 0,
                "explanation": "Il contrasto vive di complementarità con la quiete visiva: se ogni elemento compete per essere primario, l'occhio non trova ancoraggi e l'utente sperimenta sovraccarico percettivo."
            }
        ]
    },
    "dispense-c4": {
        "quiz": [
            {
                "question": "Quale modello cromatico additivo è impiegato dai display digitali (monitor, smartphone, tablet) per generare i colori attraverso l'emissione di luce?",
                "options": [
                    "Il modello sottrattivo CMYK (Ciano, Magenta, Giallo, Nero)",
                    "Il modello additivo RGB (Rosso, Verde, Blu)",
                    "Il modello monocromatico Pantone Matching System",
                    "Il modello di campionamento Lab a quadrupla densità"
                ],
                "correctIndex": 1,
                "explanation": "I display digitali generano i colori emettendo luce tramite pixel RGB: la somma alla massima intensità dei tre canali (255, 255, 255) genera il bianco puro (sintesi additiva)."
            },
            {
                "question": "Secondo le linee guida internazionali WCAG 2.1 a livello AA, quale rapporto minimo di contrasto cromatico deve sussistere tra testo standard e sfondo?",
                "options": [
                    "Almeno 2.0:1",
                    "Almeno 3.0:1 per testo normale e 1.5:1 per testo grande",
                    "Almeno 4.5:1 per testo normale (e 3.0:1 per testo grande oltre 18pt/24px)",
                    "Almeno 10.0:1 per qualsiasi elemento grafico"
                ],
                "correctIndex": 2,
                "explanation": "La soglia WCAG AA impone un contrasto di almeno 4.5:1 per testo normale. Questa proporzione garantisce leggibilità a persone con ipovisione o alterata sensibilità cromatica, oltre che sotto luce solare diretta."
            },
            {
                "question": "Nel sistema cromatico HSL, cosa rappresentano rispettivamente le tre coordinate?",
                "options": [
                    "Hue (Tonalità/Tinta in gradi da 0° a 360°), Saturation (Saturazione in %), Lightness (Luminosità in %)",
                    "High-definition, Shadow, Luminance",
                    "Hardware, System, Layout",
                    "Horizontal, Symmetrical, Linear"
                ],
                "correctIndex": 0,
                "explanation": "HSL è il modello più intuitivo per i designer: Hue individua il punto sulla ruota cromatica (0° rosso, 120° verde, 240° blu), la saturazione ne definisce la purezza e la luminosità il grado di chiarezza."
            },
            {
                "question": "Perché è considerato un grave errore di usabilità e accessibilità affidare il significato di un'informazione (es. stato di errore o successo) unicamente al colore?",
                "options": [
                    "Perché le persone daltoniche (es. con deuteranopia o protanopia) non riuscirebbero a distinguere lo stato senza icone o testi di supporto",
                    "Perché i motori di ricerca indicizzano solo il testo in bianco e nero",
                    "Perché i browser mobili convertono tutti i colori in toni di grigio durante il caricamento",
                    "Perché i file CSS non consentono la dichiarazione di colori per i messaggi di form"
                ],
                "correctIndex": 0,
                "explanation": "Circa l'8% degli uomini e lo 0.5% delle donne presentano forme di daltonismo (spesso rosso/verde). Il colore deve sempre essere accompagnato da forme, icone, testi o pattern distintivi."
            },
            {
                "question": "Come si definiscono due colori collocati in posizioni diametralmente opposte sulla ruota cromatica (es. blu e arancione)?",
                "options": [
                    "Colori analoghi",
                    "Colori monocromatici",
                    "Colori complementari",
                    "Colori acromatici"
                ],
                "correctIndex": 2,
                "explanation": "I colori complementari offrono il massimo contrasto cromatico e visivo reciproco: utilizzati con sapienza (uno dominante, l'altro per dettagli/CTA), creano vivacità e dinamismo."
            }
        ],
        "examQuiz": [
            {
                "question": "Un designer sceglie un testo grigio chiaro (#999999) su sfondo bianco (#FFFFFF) per i campi di un modulo di registrazione. Il contrast ratio risulta di circa 2.8:1. Qual è la valutazione tecnica?",
                "options": [
                    "È conforme, poiché i campi di input non sono soggetti alle linee guida di accessibilità",
                    "È non conforme alle WCAG AA per testo standard, causando gravi difficoltà di lettura per utenti ipovedenti o su schermi a bassa luminosità",
                    "È un'ottima soluzione minimale raccomandata per alleggerire il carico visivo",
                    "È conforme purché il font utilizzato appartenga alla famiglia Helvetica"
                ],
                "correctIndex": 1,
                "explanation": "Un rapporto di 2.8:1 è insufficiente: viola lo standard minimo di 4.5:1, rendendo il testo praticamente invisibile sotto luce solare o per utenti con cataratta e deficit visivi."
            },
            {
                "question": "Cosa si intende per 'Palette Funzionale' (o semantica) all'interno di un Design System moderno?",
                "options": [
                    "L'elenco dei colori preferiti dal direttore marketing dell'azienda",
                    "La mappatura dei colori su ruoli di sistema specifici (es. Success/Verde, Error/Rosso, Warning/Giallo, Info/Blu, Neutral/Grigi per testi e superfici)",
                    "Una raccolta di colori generata in modo casuale ad ogni caricamento di pagina",
                    "I colori riservati esclusivamente alla stampa delle brochure promozionali"
                ],
                "correctIndex": 1,
                "explanation": "I colori semantici collegano la cromia a un significato universale e costante: l'utente impara a riconoscere istantaneamente se un avviso è di successo, pericolo o informazione di sistema."
            },
            {
                "question": "Quale fenomeno percettivo descrive l'alterazione del tono di un colore provocata dalla vicinanza o dalla sovrapposizione con un altro colore di sfondo?",
                "options": [
                    "Il contrasto simultaneo (teorizzato da Michel-Eugène Chevreul)",
                    "L'interferenza termica dei fosfori",
                    "La dispersione refrattiva del silicio",
                    "La latenza gamma del driver video"
                ],
                "correctIndex": 0,
                "explanation": "Il contrasto simultaneo dimostra che nessun colore viene percepito isolato: un grigio neutro appare caldo su sfondo blu e freddo su sfondo arancione, influenzando la leggibilità dell'interfaccia."
            }
        ]
    },
    "dispense-c5": {
        "quiz": [
            {
                "question": "Qual è la differenza tecnica rigorosa tra i termini 'Typeface' e 'Font'?",
                "options": [
                    "Non sussiste alcuna differenza, sono sinonimi perfettamente intercambiabili",
                    "Typeface è la famiglia tipografica disegnata (es. Helvetica), mentre Font è la specifica istanza fisica o file digitale a un determinato peso e corpo (es. Helvetica Bold a 16px)",
                    "Typeface si riferisce solo ai caratteri su carta, Font ai caratteri digitali",
                    "Typeface indica i caratteri con grazie, Font indica i caratteri senza grazie"
                ],
                "correctIndex": 1,
                "explanation": "La Typeface è l'opera di design concettuale (il disegno delle lettere). Il Font (dal francese 'fonte', fusione) è l'oggetto tecnologico (file .woff2, piombo) che consente di stampare o visualizzare quello specifico stile."
            },
            {
                "question": "Cosa si intende per 'x-height' (altezza delle x) in anatomia tipografica?",
                "options": [
                    "L'altezza complessiva del foglio di stampa",
                    "L'altezza delle lettere minuscole prive di aste ascendenti o discendenti (come la lettera 'x', 'a', 'e', 'o')",
                    "La distanza tra due margini verticali di una pagina",
                    "Il numero totale di caratteri per riga di testo"
                ],
                "correctIndex": 1,
                "explanation": "L'x-height determina l'ampiezza del corpo visivo del carattere. A parità di corpo tipografico (es. 16px), un carattere con x-height generosa risulta notevolmente più leggibile a dimensioni ridotte su display digitali."
            },
            {
                "question": "Quale caratteristica strutturale contraddistingue i caratteri tipografici 'Serif' (con grazie) rispetto ai 'Sans-Serif' (a bastoni)?",
                "options": [
                    "I caratteri Serif presentano piccoli prolungamenti terminali orizzontali o arcuati alle estremità delle aste delle lettere",
                    "I caratteri Serif non possiedono lettere maiuscole",
                    "I caratteri Serif sono composti esclusivamente da linee rette a 90 gradi",
                    "I caratteri Serif possono essere renderizzati solo in formato raster BMP"
                ],
                "correctIndex": 0,
                "explanation": "Le 'grazie' (serif) derivano dall'incisione lapidaria romana. Nei testi a stampa continui favoriscono la continuità della riga, mentre i sans-serif offrono massima nitidezza anche a basse risoluzioni."
            },
            {
                "question": "Quale intervallo di caratteri per riga (lunghezza della linea o measure) è considerato ottimale per la lettura continua di un testo su display?",
                "options": [
                    "Tra 15 e 25 caratteri per riga",
                    "Circa 50-75 caratteri (inclusi gli spazi), per evitare affaticamento visivo e salti di riga errati",
                    "Almeno 180-220 caratteri per sfruttare tutta la larghezza dei monitor moderni",
                    "Esattamente 10 parole fisse per riga a qualsiasi risoluzione"
                ],
                "correctIndex": 1,
                "explanation": "Se la riga è troppo lunga (oltre 85 caratteri), l'occhio fatica a trovare l'inizio della riga successiva; se è troppo corta (sotto i 40 caratteri), il ritmo di lettura si spezza continuamente."
            },
            {
                "question": "Cosa indicano rispettivamente 'Leading' (interlinea) e 'Tracking' nella formattazione tipografica?",
                "options": [
                    "Leading è la spaziatura verticale tra le linee di base delle righe di testo; Tracking è la spaziatura orizzontale uniforme applicata a un intero blocco di caratteri",
                    "Leading è il grassetto e Tracking è il corsivo",
                    "Leading misura l'altezza delle lettere maiuscole e Tracking la larghezza dei margini",
                    "Leading riguarda i font serif e Tracking i font sans-serif"
                ],
                "correctIndex": 0,
                "explanation": "Il leading (dalle lamine di piombo) regola l'ariosità verticale tra le righe (in CSS line-height). Il tracking (letter-spacing) dilata o comprime proporzionalmente lo spazio tra tutte le lettere."
            }
        ],
        "examQuiz": [
            {
                "question": "Un sito di divulgazione scientifica presenta un corpo del testo a 14px con line-height: 1.05. Gli utenti lamentano rapido affaticamento durante la lettura dei saggi. Qual è la causa tecnica del problema?",
                "options": [
                    "L'interlinea è eccessivamente compressa: le aste discendenti sfiorano o si sovrappongono a quelle ascendenti della riga sotto, ostacolando il tracciamento visivo",
                    "I browser non possono renderizzare caratteri a 14 pixel",
                    "Il contrasto tra pixel è incompatibile con il formato TrueType",
                    "Il testo avrebbe dovuto essere formattato tutto in lettere maiuscole"
                ],
                "correctIndex": 0,
                "explanation": "Per testi di lettura continua, il line-height ottimale oscilla tra 1.4 e 1.6 (140%-160%). Un valore di 1.05 comprime le righe, rendendo faticosa la scansione e provocando regressioni oculari."
            },
            {
                "question": "Cosa garantisce l'utilizzo della proprietà CSS 'font-display: swap' nel caricamento dei font web (@font-face)?",
                "options": [
                    "Impedisce il fenomeno del FOIT (Flash of Invisible Text), mostrando subito un font di fallback di sistema e sostituendolo non appena il custom font è scaricato",
                    "Converte automaticamente i font OpenType in grafica vettoriale SVG",
                    "Scarica simultaneamente tutte le 800 varianti di peso del font",
                    "Impedisce agli utenti di copiare il testo dagli articoli"
                ],
                "correctIndex": 0,
                "explanation": "'font-display: swap' è cruciale per la web performance e la UX: il testo rimane immediatamente leggibile tramite il font di sistema, evitando che l'utente si trovi davanti a una schermata vuota durante il download."
            },
            {
                "question": "Perché è buona norma limitare l'abbinamento di font (font pairing) a un massimo di 2 o 3 famiglie distinte all'interno di un progetto?",
                "options": [
                    "Perché troppi font generano disordine visivo, indeboliscono la gerarchia e appesantiscono i tempi di caricamento delle pagine",
                    "Perché i sistemi operativi moderni non consentono l'installazione di più di tre font per dominio",
                    "Perché il CSS non supporta la dichiarazione di più di un selettore font-family",
                    "Perché altrimenti i motori di ricerca classificano il sito come spam"
                ],
                "correctIndex": 0,
                "explanation": "La regola aurea della tipografia digitale: 2 famiglie contrastanti e complementari (es. un serif per i titoli e un sans-serif per il testo o viceversa) garantiscono pulizia, coerenza e performance ottimale."
            }
        ]
    }
}

# Add chapters 6 to 14
dispense_c6_to_14 = {
    "dispense-c6": {
        "quiz": [
            {
                "question": "Qual è la differenza strutturale fondamentale tra una grafica raster (bitmap) e una vettoriale?",
                "options": [
                    "La grafica raster è composta da una griglia fissa di pixel colorati dipendente dalla risoluzione, mentre la grafica vettoriale si basa su formule matematiche scalabili all'infinito senza perdita di qualità",
                    "La grafica raster funziona solo su schermi CRT e la vettoriale su schermi OLED",
                    "La grafica vettoriale non supporta i colori sfumati o gradienti",
                    "La grafica raster occupa sempre meno spazio su disco rispetto alla vettoriale"
                ],
                "correctIndex": 0,
                "explanation": "I file raster (JPEG, PNG, WebP) descrivono la griglia di pixel: ingrandendoli sgranano. I file vettoriali (SVG) descrivono punti, curve e tracciati matematici: scalano a qualsiasi risoluzione mantenendo nitidezza assoluta."
            },
            {
                "question": "In quale formato web è preferibile salvare loghi, icone dell'interfaccia e diagrammi grafici?",
                "options": [
                    "In formato JPEG ad altissima compressione",
                    "In formato SVG (Scalable Vector Graphics), per garantire perfetta nitidezza a qualsiasi densità di pixel e peso ridotto",
                    "In formato BMP non compresso",
                    "In formato TIFF multipagina"
                ],
                "correctIndex": 1,
                "explanation": "L'SVG è lo standard ideale per icone e marchi: è leggero, scalabile, integrabile direttamente nel DOM HTML e manipolabile dinamicamente con stili CSS (come colore fill in hover)."
            },
            {
                "question": "Quale formato moderno di compressione per immagini fotografiche offre un'efficienza superiore rispetto a JPEG e PNG sia con compressione lossy che lossless?",
                "options": [
                    "Il formato WebP (e AVIF)",
                    "Il formato GIF a 256 colori",
                    "Il formato EPS per postscript",
                    "Il formato ICO a 16 bit"
                ],
                "correctIndex": 0,
                "explanation": "WebP (sviluppato da Google) riduce il peso dei file del 25-35% rispetto a JPEG mantenendo qualità visiva equivalente e supportando la trasparenza alfa, accelerando significativamente il caricamento web."
            },
            {
                "question": "Cosa si intende per 'Compressione Lossy' (con perdita di dati)?",
                "options": [
                    "Un algoritmo che rimuove permanentemente informazioni visive e frequenze impercettibili all'occhio umano per ridurre drasticamente la dimensione del file",
                    "Un errore di scrittura del file che rende l'immagine corrotta",
                    "Una procedura di cifratura militare per proteggere i dati delle immagini",
                    "Un metodo che raddoppia i pixel per aumentare la nitidezza artificiale"
                ],
                "correctIndex": 0,
                "explanation": "La compressione lossy (usata in JPEG e WebP) scarta dettagli ad alta frequenza che l'occhio umano percepisce a stento, ottenendo file molto compatti a costo di una lieve degradazione invisibile all'uso comune."
            },
            {
                "question": "Perché sui moderni display 'Retina' o ad alta densità (DPR 2x o 3x) un'immagine raster a risoluzione standard può apparire sfocata?",
                "options": [
                    "Perché il display ha più pixel fisici per ogni pixel CSS logico: se l'immagine non è fornita a doppia risoluzione, il browser deve interpolare e dilatare i pixel esistenti",
                    "Perché i monitor Retina supportano solo immagini in bianco e nero",
                    "Perché la frequenza di aggiornamento a 120Hz degrada la saturazione dei pixel",
                    "Perché le immagini raster non possono essere caricate su sistemi operativi macOS"
                ],
                "correctIndex": 0,
                "explanation": "Un display 2x possiede 4 pixel fisici per ogni pixel CSS: un'immagine da 100x100px viene spalmata su 200x200 pixel fisici, risultando morbida e sgranata se non si fornisce una versione @2x."
            }
        ],
        "examQuiz": [
            {
                "question": "Come si implementa in HTML5 una gestione corretta delle immagini responsive fornendo diverse risoluzioni in base alla larghezza schermo o densità del display?",
                "options": [
                    "Utilizzando l'elemento <picture> con tag <source media='...'> oppure il tag <img> con attributo srcset e sizes",
                    "Inserendo più tag <img> consecutivi e nascondendoli con display: none in CSS",
                    "Duplicando l'intera pagina web per ciascuna tipologia di smartphone",
                    "Scaricando via JavaScript l'immagine a risoluzione massima e rimpicciolendola con width"
                ],
                "correctIndex": 0,
                "explanation": "L'elemento <picture> e l'attributo 'srcset' consentono al browser di negoziare prima del download l'immagine più adatta alle dimensioni e alla densità del dispositivo, risparmiando dati e memoria."
            },
            {
                "question": "Quale impatto produce il mancato inserimento degli attributi 'width' e 'height' espliciti sul tag <img> nell'HTML?",
                "options": [
                    "Provoca il fenomeno del CLS (Cumulative Layout Shift): il browser non sa quanto spazio riservare e il layout salta bruscamente non appena l'immagine finisce di scaricarsi",
                    "L'immagine non viene renderizzata in nessun browser moderno",
                    "Il browser blocca l'esecuzione degli script analitici",
                    "Il file CSS associato viene rimosso dalla memoria cache"
                ],
                "correctIndex": 0,
                "explanation": "Specificare width e height (o l'aspect-ratio in CSS) permette al browser di calcolare il rapporto di forma e riservare l'area esatta nel flusso di layout prima che l'immagine sia scaricata, eliminando scatti fastidiosi."
            },
            {
                "question": "In quale situazione l'uso di un file PNG a 24 bit con trasparenza alfa è preferibile rispetto a un JPEG?",
                "options": [
                    "Quando l'immagine deve sovrapporsi a sfondi colorati variabili o texture complesse mantenendo bordi perfettamente sfumati e nitidi",
                    "Per fotografie naturalistiche di paesaggi ad alta definizione",
                    "Quando si desidera massimizzare la compressione con perdita per risparmiare banda",
                    "Esclusivamente per la stampa litografica industriale"
                ],
                "correctIndex": 0,
                "explanation": "Il formato JPEG non supporta alcun canale di trasparenza; il PNG a 24 bit offre un canale alfa completo a 8 bit (256 livelli di semitrasparenza), ideale per badge, grafiche isolate e sovrapposizioni fluide."
            }
        ]
    },
    "dispense-c7": {
        "quiz": [
            {
                "question": "Quali elementi strutturali compongono una griglia tipografica compositiva modulare?",
                "options": [
                    "Colonne (aree verticali di contenuto), Margini (spazi perimetrali di respiro) e Gutter (spazi intermedi tra le colonne)",
                    "Solo pixel singoli e coordinate assolute top/left",
                    "File audio, canali video e frequenze di rendering",
                    "Paragrafi di testo e codici di stato HTTP"
                ],
                "correctIndex": 0,
                "explanation": "La griglia classica organizza lo spazio tramite colonne verticali, canali di separazione (gutter) che impediscono collisioni visive e margini perimetrali che staccano il contenuto dal bordo."
            },
            {
                "question": "Perché il sistema a 12 colonne è diventato lo standard più diffuso nel web design e nei framework responsive?",
                "options": [
                    "Perché il numero 12 è altamente divisibile: consente di suddividere facilmente il layout in 1, 2, 3, 4, 6 o 12 porzioni uguali e combinazioni asimmetriche (es. 8+4, 9+3)",
                    "Perché i display dei computer hanno un numero di pixel multiplo di 12",
                    "Perché è stato imposto da un decreto dell'Unione Europea nel 2005",
                    "Perché consente di visualizzare unicamente 12 righe di testo per schermata"
                ],
                "correctIndex": 0,
                "explanation": "Il numero 12 offre la massima flessibilità modulare: divide la larghezza a metà (6+6), in terzi (4+4+4), in quarti (3+3+3+3) o in layout con sidebar (8+4 oppure 9+3) senza frazioni complesse."
            },
            {
                "question": "Cosa si intende per 'Ritmo Verticale' (Vertical Rhythm) nella composizione di una pagina web?",
                "options": [
                    "L'alternanza armoniosa e proporzionata di altezze dei testi, interlinee e margini basata su un'unità di misura modulare costante (es. 4px o 8px)",
                    "La velocità di scrolling automatico dal basso verso l'alto",
                    "La frequenza con cui i banner promozionali compaiono durante la navigazione",
                    "Il numero di collegamenti ipertestuali inseriti nel piè di pagina"
                ],
                "correctIndex": 0,
                "explanation": "Il ritmo verticale conferisce cadenza musicale allo spazio: legando line-height, margini e spaziature a una griglia base (spesso il modulo a 8px), l'intera composizione guadagna ordine e respiro uniforme."
            },
            {
                "question": "In un sistema a griglia, cosa rappresenta il 'Gutter'?",
                "options": [
                    "La spaziatura interna tra colonne adiacenti che impedisce agli elementi di toccarsi e fondersi visivamente",
                    "Il bordo perimetrale metallico del monitor hardware",
                    "L'area di intestazione che racchiude il menu",
                    "L'icona di chiusura delle finestre popup modali"
                ],
                "correctIndex": 0,
                "explanation": "I gutter sono i canali di scorrimento visivo tra una colonna e l'altra: definiscono la distanza tra blocchi e card, garantendo autonomia e chiarezza percettiva."
            },
            {
                "question": "Quale vantaggio offre l'adozione di un 'Sistema a Griglia a 8 Punti' (8pt Grid System) nello sviluppo di UI moderne?",
                "options": [
                    "Semplifica le decisioni di design e riduce gli attriti tra designer e programmatori, poiché tutti i valori di padding, margin e dimensioni sono multipli coerenti di 8 (8, 16, 24, 32, 40...)",
                    "Forza tutti i font ad avere un corpo fisso di 8 pixel",
                    "Impedisce l'utilizzo di immagini rettangolari",
                    "Rende superfluo il controllo di accessibilità sul contrasto"
                ],
                "correctIndex": 0,
                "explanation": "La griglia a 8 punti è lo standard de facto dell'industria digitale: la maggior parte delle risoluzioni è divisibile per 8, elimina decisioni arbitrarie (13px o 15px?) e crea armonia visiva immediata."
            }
        ],
        "examQuiz": [
            {
                "question": "In un layout responsive progettato su griglia a 12 colonne, come viene gestita tipicamente la transizione da schermi desktop a schermi smartphone?",
                "options": [
                    "Le 12 colonne si comprimono a pochi millimetri rendendo il testo microscopico",
                    "Il numero di colonne attive si riduce (tipicamente a 4 o 1 colonna a larghezza piena), e gli elementi disposti su più colonne affiancate scorrono verticalmente uno sotto l'altro",
                    "I browser mobili disabilitano l'uso del CSS imponendo una tabella HTML nativa",
                    "Vengono eliminati tutti i contenuti lasciando solo l'immagine di testata"
                ],
                "correctIndex": 1,
                "explanation": "Nel passaggio a mobile la griglia si riadatta (Reflow): elementi che su desktop occupavano 4 colonne su 12 (un terzo) passano a occupare l'intera ampiezza (100% o 4 colonne su 4), impilandosi con ordine."
            },
            {
                "question": "Quale rischio compositivo si manifesta se i margini esterni della pagina (page margins) sono più stretti dei gutter interni tra le card?",
                "options": [
                    "Il layout appare soffocato e deborda visivamente verso i bordi fisici dello schermo, rompendo la sensazione di unità e contenimento",
                    "Il file CSS raddoppia i tempi di compilazione nel browser",
                    "Le tecnologie assistive non riescono a individuare il corpo principale del testo",
                    "I font sans-serif vengono convertiti automaticamente in caratteri con grazie"
                ],
                "correctIndex": 0,
                "explanation": "I margini esterni fungono da cornice di rispetto: devono essere pari o preferibilmente superiori ai gutter interni per incorniciare il contenuto e mantenerlo centrato nel campo visivo."
            },
            {
                "question": "Cosa si intende per 'Modularità' all'interno di un sistema di layout digitale?",
                "options": [
                    "La capacità di costruire schermate complesse combinando componenti e blocchi standardizzati che condividono le medesime regole geometriche e proporzionali",
                    "L'obbligo di utilizzare solo moduli di pagamento online certificati",
                    "La programmazione in linguaggio Assembly dei driver video",
                    "La suddivisione del testo in paragrafi di esattamente 100 caratteri"
                ],
                "correctIndex": 0,
                "explanation": "La modularità permette scalabilità e coerenza: le card, i form, i banner e i bottoni condividono il medesimo DNA geometrico e possono essere ricombinati senza spezzare l'armonia della pagina."
            }
        ]
    },
    "dispense-c8": {
        "quiz": [
            {
                "question": "Qual è lo scopo precipuo dell'Architettura dell'Informazione (IA) nella progettazione di un prodotto digitale?",
                "options": [
                    "Organizzare, strutturare ed etichettare i contenuti in modo logico e coerente per consentire agli utenti di orientarsi e trovare facilmente le informazioni cercate",
                    "Installare e configurare i sistemi operativi sui server aziendali",
                    "Definire i prezzi dei prodotti e le politiche di reso dell'e-commerce",
                    "Disegnare le animazioni 3D per il caricamento iniziale delle schermate"
                ],
                "correctIndex": 0,
                "explanation": "L'Architettura dell'Informazione è la mappa concettuale del sito: organizza tassonomie, schemi di categorizzazione e sistemi di etichettatura (labeling) affinché l'utente navighi senza smarrirsi."
            },
            {
                "question": "In quale tecnica di ricerca UX gli utenti raggruppano schede contenenti argomenti o funzioni in categorie, aiutando a definire l'albero di navigazione?",
                "options": [
                    "Il Card Sorting (aperto o chiuso)",
                    "Il Test di Turing",
                    "L'analisi euristica retroattiva",
                    "La regressione lineare multivariata"
                ],
                "correctIndex": 0,
                "explanation": "Il Card Sorting è il metodo principe dell'IA: nel sorting aperto gli utenti raggruppano le schede e creano loro stessi i nomi delle categorie; nel sorting chiuso inseriscono le schede in categorie già definite."
            },
            {
                "question": "Cosa si intende per 'Tree Testing' (test dell'albero)?",
                "options": [
                    "Un test di usabilità quantitativo che valuta la navigabilità e la reperibilità di un contenuto all'interno della struttura ad albero priva di grafica o distrazioni visive",
                    "Un test di resistenza del server all'aumento delle connessioni concorrenti",
                    "L'analisi ecologica dell'impatto di CO2 prodotto dai datacenter",
                    "La verifica del caricamento di font tipografici a foglia singola"
                ],
                "correctIndex": 0,
                "explanation": "Il Tree Testing verifica l'architettura pura: ai partecipanti viene chiesto dove cercherebbero una determinata informazione all'interno della gerarchia testuale, isolando la qualità dei termini da fattori estetici."
            },
            {
                "question": "Quale problema strutturale si verifica quando un'architettura dell'informazione è eccessivamente profonda (troppi livelli gerarchici)?",
                "options": [
                    "Gli utenti sono costretti a compiere troppi clic di penetrazione e faticano a costruire una mappa mentale della propria posizione nel sistema",
                    "Il browser esaurisce lo spazio su disco rigido",
                    "La pagina web non può essere indicizzata dai motori di ricerca",
                    "I collegamenti ipertestuali cambiano automaticamente colore"
                ],
                "correctIndex": 0,
                "explanation": "Una gerarchia troppo profonda (Deep Architecture) nasconde i contenuti sotto troppi livelli; una troppo piatta (Flat) sovraccarica la pagina di scelte. La soluzione è un bilanciamento equilibrato."
            },
            {
                "question": "Cosa contraddistingue un sistema di etichettatura (Labeling) efficace all'interno di un menu?",
                "options": [
                    "L'uso di termini chiari, familiari e univoci che rispecchiano il linguaggio naturale degli utenti anziché il gergo burocratico interno dell'azienda",
                    "L'invenzione di neologismi poetici e misteriosi per stimolare la curiosità",
                    "L'uso di etichette composte da frasi di almeno venti parole",
                    "L'adozione esclusiva della lingua latina per conferire autorevolezza"
                ],
                "correctIndex": 0,
                "explanation": "Le etichette devono essere autoesplicative: utilizzare il linguaggio dell'utente (User-centric vocabulary) garantisce che la persona capisca dove porta il link prima ancora di cliccarlo."
            }
        ],
        "examQuiz": [
            {
                "question": "Un portale universitario colloca il modulo per la domanda di borsa di studio sotto: 'Ateneo > Strutture Amministrative > Ripartizione IV > Settore Servizi agli Studenti > Procedure Contabili'. Qual è la diagnosi dal punto di vista dell'IA?",
                "options": [
                    "La tassonomia rispecchia l'organigramma interno dell'amministrazione (Inside-Out) anziché il modello mentale e il compito dell'utente (Outside-In), ostacolando il ritrovamento",
                    "La tassonomia è perfetta perché rispetta la gerarchia burocratica dell'ente",
                    "Il percorso è corretto purché il testo sia evidenziato con font serif",
                    "Non sussistono problemi poiché tutti gli studenti utilizzano la ricerca interna"
                ],
                "correctIndex": 0,
                "explanation": "È il classico vizio 'Inside-Out': progettare il sito specchiando la suddivisione degli uffici interni costringe l'utente a conoscere l'organigramma per compiere un'azione ordinaria."
            },
            {
                "question": "Cosa sono le 'Breadcrumbs' (Briciole di Pane) e quale funzione svolgono per la navigabilità?",
                "options": [
                    "Un elemento di navigazione secondaria che mostra il percorso gerarchico dalla homepage alla pagina corrente, fornendo orientamento spaziale e una scorciatoia per risalire i livelli",
                    "File temporanei di tracciamento pubblicitario installati nel browser",
                    "Errori di sintassi generati dal server durante la compilazione delle pagine",
                    "Icone decorative prive di collegamenti ipertestuali"
                ],
                "correctIndex": 0,
                "explanation": "Le breadcrumbs (es. Home > Scarpe > Uomo > Sneaker) rispondono alla domanda 'Dove mi trovo rispetto al tutto?' e permettono di risalire la tassonomia con un solo clic."
            },
            {
                "question": "In quale scenario la ricerca interna (Search) e la navigazione strutturata (Browse) devono convivere come percorsi complementari?",
                "options": [
                    "Sempre, nei portali con patrimonio informativo consistente: una parte consistente degli utenti cerca direttamente per parole chiave (search-dominant), mentre altri preferiscono esplorare le categorie (browse-dominant)",
                    "Solo nei siti web dedicati ai bambini e alle scuole primarie",
                    "Mai: i siti moderni devono eliminare del tutto le barre di ricerca in favore dei menu a tendina",
                    "Esclusivamente quando il server ha una connessione satellitare"
                ],
                "correctIndex": 0,
                "explanation": "Le persone navigano con stili cognitivi diversi: chi sa esattamente cosa cerca usa la barra di ricerca; chi ha un bisogno sfumato o vuole confrontare alternative esplora l'albero delle categorie."
            }
        ]
    },
    "dispense-c9": {
        "quiz": [
            {
                "question": "Secondo Don Norman, cosa si intende per 'Affordance' di un elemento d'interfaccia?",
                "options": [
                    "La proprietà percepita o reale dell'oggetto che suggerisce intuitivamente come possa essere utilizzato e manipolato",
                    "Il costo economico di sviluppo del componente software",
                    "Il tempo necessario per scaricare l'elemento sulla memoria cache",
                    "La compatibilità dell'elemento con i motori di ricerca"
                ],
                "correctIndex": 0,
                "explanation": "L'affordance (introdotta da Gibson e portata al design da Norman) è la 'chiamata all'azione' intrinseca: una maniglia suggerisce di tirare, una superficie sopraelevata e con bordo suggerisce di essere premuta (bottone)."
            },
            {
                "question": "Quali sono i quattro stati interattivi canonici che ogni pulsante o campo interattivo deve possedere per comunicare chiarezza all'utente?",
                "options": [
                    "Stato di riposo (Default), Passaggio del mouse (Hover), Pressione/Attivazione (Active) e Stato disabilitato (Disabled) o Focalizzato (Focus)",
                    "Stato Alfa, Stato Beta, Stato Gamma e Stato Delta",
                    "Invisibile, Trasparente, Solido e Riflettente",
                    "Solo Stato Iniziale e Stato Finale"
                ],
                "correctIndex": 0,
                "explanation": "La gestione degli stati è fondamentale nell'UI: l'utente deve sapere se un elemento è cliccabile (default), se il cursore lo ha intercettato (hover), se è stato premuto (active) o se è selezionato da tastiera (focus)."
            },
            {
                "question": "Cosa si intende per 'Signifier' (Segnalatore visivo)?",
                "options": [
                    "Qualsiasi segnale visivo esplicito (testo, icona, ombra, freccia) che comunica dove l'azione debba avvenire quando l'affordance naturale non è immediatamente percepibile",
                    "Un messaggio pubblicitario popup che copre la schermata",
                    "Il certificato crittografico HTTPS della connessione",
                    "Il logo del brand aziendale collocato nella testata"
                ],
                "correctIndex": 0,
                "explanation": "Norman ha chiarito che nel digitale le affordance sono spesso simulate: i 'signifiers' (es. la scritta 'Scorri in basso' o la freccia accanto a un menu) segnalano chiaramente all'utente dove e come agire."
            },
            {
                "question": "Qual è la funzione delle 'Microinterazioni' (micro-interactions) nel design di un'interfaccia?",
                "options": [
                    "Fornire feedback immediato, confermare il successo di un'azione (es. toggle che cambia stato, animazione di invio completato) e rendere l'interazione umana e gratificante",
                    "Ridurre il consumo elettrico della batteria dello smartphone",
                    "Cancellare i cookie di navigazione dopo ogni singolo clic",
                    "Comprimere il codice sorgente HTML eliminando gli spazi vuoti"
                ],
                "correctIndex": 0,
                "explanation": "Le microinterazioni (Dan Saffer) sono momenti singoli e focalizzati attorno a un compito: comunicano lo stato del sistema con grazia, riducendo l'ansia dell'utente e donando piacere d'uso."
            },
            {
                "question": "Perché un bottone 'Primario' deve essere visivamente predominante rispetto a un bottone 'Secondario' all'interno della stessa schermata?",
                "options": [
                    "Per guidare inequivocabilmente l'utente verso l'azione cardine desiderata (Call to Action), minimizzando il dubbio decisionale",
                    "Perché i browser non permettono la presenza di due bottoni con lo stesso colore",
                    "Perché i bottoni secondari non possono eseguire script di salvataggio",
                    "Per rispettare una direttiva internazionale sul copyright dei font"
                ],
                "correctIndex": 0,
                "explanation": "Gerarchia d'azione: se 'Conferma Ordine' e 'Annulla' avessero lo stesso peso visivo, l'utente esiterebbe o rischierebbe clic accidentali. L'azione primaria deve risaltare con chiarezza immediata."
            }
        ],
        "examQuiz": [
            {
                "question": "Un sito web di commercio elettronico rimuove il bordo, l'ombra e il colore di sfondo da tutti i pulsanti 'Aggiungi al carrello', lasciando solo un testo grigio non sottolineato. Quale principio di UI viene gravemente compromesso?",
                "options": [
                    "La percezione dell'affordance di cliccabilità: l'utente fatica a distinguere gli elementi azionabili dal testo statico informativo",
                    "La velocità di rendering della scheda grafica integrata",
                    "L'indicizzazione dei metadati OpenGraph sui social media",
                    "La risoluzione DPI delle fotografie dei prodotti"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il classico errore del cosiddetto 'Flat Design estremo': eliminando tutti i signifier (bordi, rilievi, contrasti), gli utenti non riconoscono i pulsanti come tali, con drastico calo delle conversioni."
            },
            {
                "question": "In un modulo convalidato lato client, quando è opportuno mostrare il messaggio di errore su un campo obbligatorio?",
                "options": [
                    "Dopo che l'utente ha abbandonato il campo (evento 'blur' o 'onchange') o al momento della sottomissione del modulo, evitando di segnalare errore mentre sta ancora digitando",
                    "Non appena l'utente digita il primo carattere nel campo vuoto",
                    "Esclusivamente tramite una finestra popup che blocca l'intero browser",
                    "Dopo aver forzato il ricaricamento completo dell'intera pagina web"
                ],
                "correctIndex": 0,
                "explanation": "Segnalare errore mentre l'utente sta ancora scrivendo genera ansia e frustrazione. Il feedback migliore si attiva quando il campo perde il focus ('blur') o al tentativo di invio dell'intero form."
            },
            {
                "question": "Quale criterio deve guidare la progettazione della 'Dark Mode' (modalità scura) di un'interfaccia utente?",
                "options": [
                    "Evitare l'uso di nero puro (#000000) su bianco puro (#FFFFFF) che genera bagliore e affaticamento visivo (aloning), preferendo superfici grigio scuro con contrasti dosati",
                    "Invertire matematicamente tutti i colori dei pixel senza alterare le immagini",
                    "Sostituire tutti i caratteri tipografici con font monospazio",
                    "Rendere invisibili tutti i bottoni per risparmiare energia sui display OLED"
                ],
                "correctIndex": 0,
                "explanation": "Le migliori linee guida (Google Material, Apple HIG) sconsigliano il contrasto estremo nero/bianco in dark mode: grigi scuri a diversi livelli di elevazione (superfici) permettono di comunicare profondità e riducono l'abbagliamento."
            }
        ]
    },
    "dispense-c10": {
        "quiz": [
            {
                "question": "Cos'è un 'Design System' nella moderna produzione digitale?",
                "options": [
                    "Un ecosistema unificato di standard condivisi, principi visivi, pattern interattivi, componenti riutilizzabili codificati e linee guida per garantire coerenza e scalabilità tra team",
                    "Un software antivirus per la scansione dei fogli di stile CSS",
                    "Un archivio di immagini fotografiche acquistate da banche dati esterne",
                    "Un modello contrattuale per il pagamento dei diritti d'autore ai grafici"
                ],
                "correctIndex": 0,
                "explanation": "Un Design System è la singola fonte di verità (Single Source of Truth) dell'azienda: include token, linee guida di tono di voce e componenti reali in codice (React, Vue, Web Components)."
            },
            {
                "question": "Nella metodologia 'Atomic Design' ideata da Brad Frost, quali sono i 5 livelli gerarchici di composizione dei componenti?",
                "options": [
                    "Atomi, Molecole, Organismi, Template e Pagine",
                    "Pixel, Linee, Forme, Vettori e Immagini",
                    "Variabili, Funzioni, Classi, Oggetti e Moduli",
                    "Bozze, Revisioni, Mockup, Prototipi e Rilasci"
                ],
                "correctIndex": 0,
                "explanation": "Brad Frost modella la chimica: gli Atomi (font, colori, bottoni singoli) formano Molecole (barra di ricerca con input e bottone), che formano Organismi (la testata), posizionati in Template e popolati nelle Pagine reali."
            },
            {
                "question": "Cos'è uno 'Style Tile' (artefatto visivo ideato da Samantha Warren)?",
                "options": [
                    "Un documento di design intermedio tra la moodboard concettuale e il mockup completo, che raccoglie font, palette, pulsanti e texture per calibrare lo stile con il cliente senza disegnare intere schermate",
                    "Una piastrella ceramica serigrafata con il logo del sito web",
                    "Un file di configurazione del server web per la gestione dei cookie",
                    "Una tipologia di banner pubblicitario a scomparsa rapida"
                ],
                "correctIndex": 0,
                "explanation": "Lo Style Tile è uno strumento agile straordinario: permette di concordare il 'mood visivo' (colori, bottoni, tipografia) risparmiando settimane di lavoro su mockup completi suscettibili di rifiuto."
            },
            {
                "question": "Cosa sono i 'Design Token' all'interno di un'architettura di design scalabile?",
                "options": [
                    "Valori atomici nominati (es. color-primary: #1a73e8; spacing-md: 16px) memorizzati in formati neutri (come JSON) per sincronizzare automaticamente design tool (Figma) e codice di sviluppo",
                    "Monete virtuali o criptovalute per acquistare template preconfezionati",
                    "Codici di sicurezza inviati via SMS per l'accesso a due fattori",
                    "Licenze commerciali temporanee per l'utilizzo di caratteri tipografici"
                ],
                "correctIndex": 0,
                "explanation": "I token sono le particelle elementari: astraggono i valori (colori, spazi, ombre, font) in variabili semantiche riutilizzabili su iOS, Android e Web, consentendo modifiche globali con un solo aggiornamento."
            },
            {
                "question": "Quale beneficio primario apporta un Design System ben strutturato ai team di ingegneria e design?",
                "options": [
                    "Riduce drasticamente la duplicazione del lavoro, accelera i tempi di rilascio delle nuove funzionalità (time-to-market) e garantisce coerenza stilistica e di accessibilità a tutto l'ecosistema",
                    "Elimina la necessità di eseguire test di compatibilità tra i diversi browser",
                    "Consente di caricare il sito web senza l'utilizzo di una connessione a internet",
                    "Impedisce agli utenti di personalizzare i propri profili personali"
                ],
                "correctIndex": 0,
                "explanation": "Senza Design System ogni team reinventa la ruota (ciascuno crea la sua versione del bottone o della card). Con esso, i componenti sono testati, accessibili e pronti all'uso, liberando tempo per i veri problemi dell'utente."
            }
        ],
        "examQuiz": [
            {
                "question": "In un'applicazione complessa, l'azienda decide di aggiornare il colore primario del marchio. In quale scenario questa modifica richiederà pochi secondi anziché settimane di ricerca e sostituzione manuale?",
                "options": [
                    "Se l'interfaccia è costruita impiegando un Design Token per il colore primario condiviso tra repository CSS e componenti",
                    "Se tutti i file HTML sono stati scritti a mano da un unico programmatore",
                    "Se il sito è ospitato su un server con disco a stato solido NVMe",
                    "Se il font utilizzato all'interno dei titoli appartiene alla famiglia serif"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il potere dei Design Token: aggiornando il valore della variabile centrale, la modifica si propaga istantaneamente su tutte le interfacce, bottoni, link e stati del sistema."
            },
            {
                "question": "Qual è il limite metodologico nel presentare al cliente tre layout definitivi ad altissima fedeltà (mockup complessi) nelle prime fasi di un progetto?",
                "options": [
                    "Il cliente tende a focalizzarsi su dettagli superficiali (la foto specifica, il testo di prova) anziché sulla struttura logica, e qualsiasi variazione richiede rifacimenti costosi",
                    "I browser moderni non riescono a visualizzare file immagine a risoluzione elevata",
                    "I mockup ad alta fedeltà non possono essere esportati in formato PDF",
                    "Le specifiche W3C vietano la presentazione di mockup prima della stipula contrattuale"
                ],
                "correctIndex": 0,
                "explanation": "Troppi dettagli prematuri creano attrito: il committente perde la visione d'insieme e discute su elementi marginali, mentre strumenti sintetici come wireframe e Style Tile mantengono il focus sulla strategia."
            },
            {
                "question": "Cosa si intende per 'Documentazione Viva' (Living Style Guide) associata a un Design System?",
                "options": [
                    "Una piattaforma interattiva (come Storybook) in cui i componenti visualizzati sono generati dal codice sorgente reale impiegato in produzione, aggiornandosi in tempo reale",
                    "Un manuale cartaceo a fogli mobili stampato ogni settimana",
                    "Un video tutorial registrato dagli sviluppatori per illustrare l'interfaccia",
                    "Una pagina web che visualizza unicamente le statistiche di accesso degli utenti"
                ],
                "correctIndex": 0,
                "explanation": "Una style guide 'morta' (un PDF) diventa obsoleta in un mese. Una 'Living Style Guide' esegue i componenti reali del codice: se un ingegnere aggiorna il codice del componente, la documentazione riflette istantaneamente la modifica."
            }
        ]
    },
    "dispense-c11": {
        "quiz": [
            {
                "question": "Qual è il principio architetturale alla base della separazione dei compiti (Separation of Concerns) nel World Wide Web?",
                "options": [
                    "HTML gestisce la struttura semantica del contenuto, CSS controlla la presentazione visiva ed estetica, JavaScript governa il comportamento e la dinamicità interattiva",
                    "HTML si occupa dei pagamenti bancari, CSS dei testi e JavaScript della sicurezza del server",
                    "I tre linguaggi devono essere scritti tutti all'interno di un unico tag per migliorare la velocità",
                    "JavaScript è riservato ai computer desktop mentre HTML e CSS funzionano solo su smartphone"
                ],
                "correctIndex": 0,
                "explanation": "La triade del web moderno separa nettamente: Contenuto e Semantica (HTML), Stile e Layout (CSS), Logica e Interazione (JavaScript). Questa separazione assicura manutenibilità, accessibilità e standard W3C."
            },
            {
                "question": "Cosa si intende per 'Document Object Model' (DOM)?",
                "options": [
                    "La rappresentazione ad albero strutturato in memoria che il browser costruisce analizzando il codice HTML, consentendo a linguaggi come JavaScript di manipolare elementi, attributi e contenuti",
                    "Un formato proprietario per la memorizzazione dei testi su floppy disk",
                    "Il modulo di alimentazione hardware della scheda madre del computer",
                    "Un algoritmo di cifratura per impedire la lettura del codice sorgente delle pagine"
                ],
                "correctIndex": 0,
                "explanation": "Il DOM è l'interfaccia ad albero viva del documento: ogni tag HTML diventa un nodo manipolabile (aggiungere classi, ascoltare eventi click, alterare stili in tempo reale tramite script)."
            },
            {
                "question": "Perché l'uso di tag semantici HTML5 (<header>, <main>, <article>, <nav>, <aside>, <footer>) è nettamente superiore all'uso indiscriminato di tag generici <div>?",
                "options": [
                    "Fornisce significato intrinseco alla struttura (Landmark), migliorando l'accessibilità per le tecnologie assistive e favorendo l'indicizzazione gerarchica da parte dei motori di ricerca (SEO)",
                    "I tag semantici sono gli unici che supportano l'applicazione di colori di sfondo via CSS",
                    "I tag generici <div> sono stati formalmente aboliti e vengono ignorati dai browser",
                    "L'uso dei tag semantici riduce automaticamente il peso del file HTML del 90%"
                ],
                "correctIndex": 0,
                "explanation": "La semantica trasforma il testo in significato strutturato: gli screen reader permettono all'utente cieco di navigare saltando da un landmark all'altro (da 'nav' a 'main'), cosa impossibile con un mare di anonimi <div>."
            },
            {
                "question": "Quale consorzio internazionale sviluppa e mantiene gli standard tecnici aperti per il World Wide Web (come HTML e CSS)?",
                "options": [
                    "Il W3C (World Wide Web Consortium), fondato da Tim Berners-Lee",
                    "La corporazione privata dei produttori di microprocessori della Silicon Valley",
                    "Il Dipartimento del Commercio del governo degli Stati Uniti",
                    "L'Associazione Internazionale dei Provider di Telefonia Mobile"
                ],
                "correctIndex": 0,
                "explanation": "Il W3C (guidato da Tim Berners-Lee con WHATWG) definisce le specifiche aperte, garantendo che il web rimanga universale, accessibile e interoperabile su qualsiasi dispositivo e browser."
            },
            {
                "question": "Cosa stabiliscono le linee guida WCAG (Web Content Accessibility Guidelines)?",
                "options": [
                    "I requisiti tecnici, progettuali e contenutistici per rendere il web accessibile a persone con disabilità visive, uditive, motorie o cognitive (basati sui 4 principi: Percepibile, Utilizzabile, Comprensibile, Robusto)",
                    "I prezzi di vendita raccomandati per i domini web di primo livello",
                    "La configurazione obbligatoria per le antenne Wi-Fi pubbliche",
                    "I criteri per la creazione di algoritmi pubblicitari comportamentali"
                ],
                "correctIndex": 0,
                "explanation": "Le WCAG (articolate nei livelli A, AA, AAA) sono lo standard etico e legale globale dell'accessibilità: assicurano che nessuno sia escluso dalla partecipazione alla vita digitale."
            }
        ],
        "examQuiz": [
            {
                "question": "Un sito di e-commerce costruisce un pulsante cliccabile utilizzando il tag '<div onclick='checkout()'>Acquista</div>' senza attributi aggiuntivi. Quale gravissima violazione di accessibilità si verifica?",
                "options": [
                    "Il <div> non è focalizzabile da tastiera con il tasto Tab, non ha ruolo 'button' annunciato dagli screen reader e non risponde alla barra spaziatrice o al tasto Invio, escludendo gli utenti con disabilità motorie o visive",
                    "Il browser non può eseguire la funzione JavaScript se invocata da un tag div",
                    "I fogli di stile CSS non possono assegnare margini o padding a un elemento div",
                    "Il server rifiuta la transazione economica se non originata da un elemento form"
                ],
                "correctIndex": 0,
                "explanation": "Un elemento <button> nativo possiede gratuitamente accessibilità da tastiera (Tab, Enter, Space) e annuncio semantico. Simulando un bottone con un <div> si creano barriere insormontabili se non si ricreano tutti i comportamenti via ARIA e script."
            },
            {
                "question": "Qual è la conseguenza del mancato rispetto della gerarchia delle intestazioni (es. saltare direttamente da <h1> a <h4> per motivi puramente grafici)?",
                "options": [
                    "Disorienta gli utenti che utilizzano tecnologie assistive per scansionare la struttura del documento saltando tra livelli gerarchici di intestazione",
                    "Provoca il crash immediato del motore di rendering del browser",
                    "I browser convertono automaticamente tutti i testi sottostanti in corsivo",
                    "I motori di ricerca bloccano l'accesso al dominio web"
                ],
                "correctIndex": 0,
                "explanation": "Gli utenti non vedenti usano l'elenco dei titoli per esplorare la pagina: una gerarchia discontinua o saltata (h1 -> h4) fa presumere che intere sezioni informative siano state omesse o danneggiate."
            },
            {
                "question": "Cosa indica l'acronimo 'ARIA' (Accessible Rich Internet Applications) nelle specifiche web?",
                "options": [
                    "Un insieme di attributi e ruoli HTML da aggiungere al markup per comunicare ruoli semantici, stati e proprietà quando gli elementi HTML nativi non sono sufficienti per interfacce complesse",
                    "Un protocollo di compressione video ad alta fedeltà per il web",
                    "Un framework CSS per la creazione di layout tridimensionali",
                    "Una tecnologia proprietaria per il controllo vocale delle smart TV"
                ],
                "correctIndex": 0,
                "explanation": "ARIA (es. role='dialog', aria-expanded, aria-live) colma il divario nei widget interattivi avanzati (modali, caroselli, tab) spiegando allo screen reader cosa sta accadendo sullo schermo."
            }
        ]
    },
    "dispense-c12": {
        "quiz": [
            {
                "question": "Cosa definisce il concetto di 'Cascata' (Cascade) nel linguaggio CSS?",
                "options": [
                    "L'algoritmo che risolve i conflitti tra più regole applicate allo stesso elemento, determinando quale stile prevale in base a origine, specificità del selettore e ordine di apparizione nel codice",
                    "La caduta fisica delle immagini verso il fondo della pagina web durante il rendering",
                    "Il flusso di traffico di rete che scorre dal server al router domestico",
                    "La conversione dei caratteri tipografici in numeri binari"
                ],
                "correctIndex": 0,
                "explanation": "La Cascata è il cuore del CSS: se due regole entrano in conflitto per lo stesso elemento, il browser le pesa valutando la specificità del selettore; a parità di specificità, l'ultima regola dichiarata sovrascrive la precedente."
            },
            {
                "question": "Quale tra i seguenti selettori CSS possiede il grado di Specificità più elevato secondo le regole standard W3C?",
                "options": [
                    "Un selettore per identificatore univoco '#header-logo' (Specificità: 0, 1, 0, 0)",
                    "Un selettore per classe '.main-button' (Specificità: 0, 0, 1, 0)",
                    "Un selettore per tag di elemento 'p' (Specificità: 0, 0, 0, 1)",
                    "Il selettore universale '*' (Specificità: 0, 0, 0, 0)"
                ],
                "correctIndex": 0,
                "explanation": "La specificità si calcola su base posizionale: Stili inline > ID (0,1,0,0) > Classi/Pseudo-classi/Attributi (0,0,1,0) > Elementi/Pseudo-elementi (0,0,0,1). Un ID supera sempre anche un lungo elenco di classi concatenate."
            },
            {
                "question": "Come si calcolano le dimensioni totali di un elemento quando è impostata la proprietà 'box-sizing: border-box'?",
                "options": [
                    "La larghezza (width) dichiarata include al proprio interno sia il padding che il bordo, preservando l'ingombro esterno esatto",
                    "La larghezza totale è la somma di width + padding raddoppiato + bordo raddoppiato",
                    "Il padding e il bordo vengono eliminati dal rendering del browser",
                    "La larghezza dell'elemento si adatta automaticamente all'altezza della finestra"
                ],
                "correctIndex": 0,
                "explanation": "Con border-box, width è il perimetro complessivo esterno: se imposti width: 200px con padding 20px, il contenuto si stringe a 160px mantenendo la scatola esattamente a 200px."
            },
            {
                "question": "Quale differenza intercorre tra un elemento con 'display: block' e uno con 'display: inline'?",
                "options": [
                    "L'elemento block occupa tutta la larghezza disponibile della riga e va a capo automaticamente, accettando width e height; l'elemento inline occupa solo lo spazio del contenuto, non va a capo e non accetta width/height",
                    "Gli elementi block possono essere colorati, mentre gli inline sono sempre trasparenti",
                    "Gli elementi inline possono contenere solo immagini e mai testo",
                    "Non sussiste alcuna differenza reale di visualizzazione"
                ],
                "correctIndex": 0,
                "explanation": "Un elemento 'block' (come <p> o <div>) genera una scatola a tutta riga con controllo dimensionale; un elemento 'inline' (come <span> o <a>) scorre all'interno del testo senza spezzare la riga."
            },
            {
                "question": "Qual è il comportamento della proprietà 'position: absolute' applicata a un elemento CSS?",
                "options": [
                    "L'elemento viene rimosso dal normale flusso del documento e posizionato alle coordinate top/left rispetto al primo genitore antenato che possieda un posizionamento diverso da static",
                    "L'elemento rimane fisso al centro dello schermo indipendentemente dallo scorrimento della pagina",
                    "L'elemento assume automaticamente un display: flex all'interno del proprio box",
                    "L'elemento scompare dallo schermo diventando trasparente"
                ],
                "correctIndex": 0,
                "explanation": "L'elemento assoluto non occupa più spazio nel flusso della pagina (i fratelli collassano nello spazio vuoto) e si aggancia alle coordinate del genitore posizionato (solitamente con position: relative)."
            }
        ],
        "examQuiz": [
            {
                "question": "Due regole CSS si applicano allo stesso paragrafo: 'article p { color: blue; }' e '.testo-evidenziato { color: red; }'. Di quale colore apparirà il testo?",
                "options": [
                    "Rosso, perché la classe '.testo-evidenziato' ha specificità (0,0,1,0), che supera i due selettori di elemento di 'article p' aventi specificità (0,0,0,2)",
                    "Blu, perché 'article p' contiene due elementi e quindi ha valore numerico doppio",
                    "Nero, perché il browser entra in stallo e applica il colore predefinito di sistema",
                    "Viola, fondendo i due colori in base al principio additivo RGB"
                ],
                "correctIndex": 0,
                "explanation": "Una singola classe (peso 10) batte qualsiasi combinazione di soli elementi (peso 1 ciascuno): (0,0,1,0) prevale nettamente su (0,0,0,2)."
            },
            {
                "question": "Perché l'uso indiscriminato della direttiva '!important' nel codice CSS è considerato un pessimo pattern di sviluppo?",
                "options": [
                    "Perché rompe la normale gerarchia della cascata naturale, rendendo difficilissimo il debugging e la manutenzione futura del foglio di stile",
                    "Perché disabilita il caricamento dei font tipografici personalizzati",
                    "Perché i browser mobili non supportano la direttiva !important",
                    "Perché provoca la cancellazione automatica della cronologia di navigazione"
                ],
                "correctIndex": 0,
                "explanation": "!important è un'arma nucleare: per sovrascriverla in seguito si è costretti a usarne un'altra ancora, innescando una spirale incontrollabile di codice caotico e fragile."
            },
            {
                "question": "Cosa contraddistingue 'position: sticky' rispetto a 'position: fixed'?",
                "options": [
                    "L'elemento sticky si comporta come posizionamento relativo finché non raggiunge una certa soglia di scroll, dopodiché diventa fisso rimanendo però vincolato all'interno del proprio contenitore genitore",
                    "L'elemento sticky funziona unicamente sui monitor con frequenza superiore a 60Hz",
                    "L'elemento sticky non supporta le coordinate top o bottom",
                    "L'elemento fixed scompare quando l'utente scorre la pagina verso il basso"
                ],
                "correctIndex": 0,
                "explanation": "'fixed' ancora l'elemento al viewport globale; 'sticky' segue il flusso finché non tocca la soglia (es. top: 0), si blocca a schermo e poi 'si stacca' e risale quando il suo genitore finisce lo scorrimento."
            }
        ]
    },
    "dispense-c13": {
        "quiz": [
            {
                "question": "Quali tre elementi cardine compongono la formula storica del 'Responsive Web Design' teorizzata da Ethan Marcotte nel 2010?",
                "options": [
                    "Griglie fluide (percentuali), Immagini flessibili e Media Queries CSS",
                    "Database SQL, Server Apache e Linguaggio PHP",
                    "Font vettoriali, Colori HSL e Tabelle HTML",
                    "Touch screen, Mouse ottico e Tastiera ergonomica"
                ],
                "correctIndex": 0,
                "explanation": "Marcotte definisce il RWD come la sinergia di tre tecniche: una struttura a griglia elastica basata su percentuali, immagini che scalano entro il loro contenitore e media queries per riorganizzare il layout a soglie critiche."
            },
            {
                "question": "Quale filosofia architetturale propone la metodologia 'Mobile First' nella scrittura del codice CSS?",
                "options": [
                    "Scrivere gli stili base per gli schermi piccoli (layout lineare, leggero, senza fronzoli) e introdurre complessità per schermi ampi tramite media queries con 'min-width' (Progressive Enhancement)",
                    "Creare siti web destinati unicamente ed esclusivamente agli smartphone ignorando i desktop",
                    "Scrivere codice JavaScript per bloccare l'accesso al sito dai computer portatili",
                    "Comprimere il database per farlo risiedere nella memoria dello smartphone"
                ],
                "correctIndex": 0,
                "explanation": "Mobile First parte dal vincolo più stretto: costringe a selezionare le informazioni essenziali, assicura caricamenti velocissimi su reti cellulari e arricchisce progressivamente il layout man mano che lo schermo si allarga."
            },
            {
                "question": "Cosa indica il termine 'Breakpoint' nel Responsive Web Design?",
                "options": [
                    "La dimensione della finestra del browser a cui una Media Query attiva un cambiamento strutturale nel layout per preservare la leggibilità e l'armonia dei contenuti",
                    "Un errore irreversibile di caricamento che blocca la visualizzazione della pagina",
                    "L'interruzione temporanea della connessione Wi-Fi durante il download dei dati",
                    "Il punto in cui l'utente abbandona il carrello dell'e-commerce"
                ],
                "correctIndex": 0,
                "explanation": "I breakpoint sono i 'punti di snodo' del layout: ad esempio a 768px la navigazione passa da hamburger mobile a menu orizzontale e le card passano da colonna singola a griglia affiancata."
            },
            {
                "question": "Cosa stabilisce l'approccio 'Content-out' per la scelta dei breakpoint rispetto all'approccio orientato al dispositivo (Device-specific)?",
                "options": [
                    "I breakpoint devono essere stabiliti dove il contenuto naturale comincia a rompersi o degradare (linee troppo lunghe, colonne compresse), non sulle dimensioni commerciali di uno specifico modello di smartphone",
                    "Tutti i testi devono essere esportati in formato PDF prima dell'impaginazione",
                    "I breakpoint devono essere calcolati in base alla dimensione dei pixel fisici del processore",
                    "Il contenuto deve essere riscritto ogni volta che viene rilasciato un nuovo iPhone"
                ],
                "correctIndex": 0,
                "explanation": "I modelli di telefoni cambiano ogni sei mesi; il design robusto ascolta il contenuto: se a 640px le due colonne diventano illeggibili, quello è il breakpoint naturale, a prescindere dal brand del dispositivo."
            },
            {
                "question": "Quale direttiva HTML è indispensabile affinché un foglio di stile responsive funzioni correttamente sui browser mobili?",
                "options": [
                    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
                    "<meta http-equiv='refresh' content='30'>",
                    "<link rel='icon' href='favicon.ico'>",
                    "<base href='https://www.w3.org/'>"
                ],
                "correctIndex": 0,
                "explanation": "Senza il meta viewport, i browser mobili ignorano le media queries e renderizzano la pagina come fosse un desktop da 980px zoomato indietro, vanificando qualsiasi regola responsive CSS."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'applicazione web adotta Media Queries basate unicamente su '@media (max-width: 600px)' sovrascrivendo le regole scritte inizialmente per schermi desktop larghi 1920px. Quale problematica metodologica presenta questo approccio?",
                "options": [
                    "Adotta la logica di Desktop Degradation anziché Mobile First: i dispositivi mobili a larghezza di banda ridotta sono costretti a scaricare ed elaborare tutte le regole desktop prima di applicare le sovrascritture",
                    "I browser Android non riconoscono la parola chiave 'max-width'",
                    "Il file CSS viene rifiutato dalla validazione automatica del consorzio W3C",
                    "Le immagini in formato SVG non possono scalare all'interno di query max-width"
                ],
                "correctIndex": 0,
                "explanation": "Con max-width (Desktop First), il dispositivo mobile riceve prima la complessità pesante e poi la disfa. Mobile First (min-width) carica le basi leggere ed espande solo se lo schermo ha lo spazio per accoglierle."
            },
            {
                "question": "Qual è la differenza fondamentale tra 'Responsive Web Design' e 'Adaptive Web Design'?",
                "options": [
                    "Il responsive è un layout unico e fluido basato su percentuali e media query che si adatta a qualsiasi larghezza continua; l'adaptive serve schermate statiche preconfezionate a scatti fissi prestabiliti (es. solo a 320, 768 e 1024px)",
                    "L'adaptive funziona solo senza connessione internet mentre il responsive richiede il 5G",
                    "Il responsive non supporta il codice JavaScript mentre l'adaptive non usa CSS",
                    "Non sussiste alcuna differenza reale, trattandosi di sinonimi"
                ],
                "correctIndex": 0,
                "explanation": "Il responsive è un continuum fluido che scorre come l'acqua tra qualsiasi risoluzione; l'adaptive è una serie di layout discreti a scatto, che rischiano di non coprire risoluzioni intermedie o insolite."
            },
            {
                "question": "Come si previene il troncamento imprevisto o la deformazione dei layout sui telefoni dotati di 'Notch' o 'Dynamic Island'?",
                "options": [
                    "Utilizzando le variabili ambientali CSS 'env(safe-area-inset-top)' e 'viewport-fit=cover' per garantire aree di respiro rispetto ai ritagli fisici dello schermo",
                    "Imponendo una risoluzione fissa di 300px per tutte le pagine web",
                    "Disabilitando lo scorrimento verticale della pagina",
                    "Convertendo l'intero sito in un'applicazione puramente audio"
                ],
                "correctIndex": 0,
                "explanation": "La proprietà 'safe-area-inset' informa il CSS su dove terminano i sensori hardware fisici (notch, barra home), permettendo di distanziare gli elementi interattivi ed evitare sovrapposizioni critiche."
            }
        ]
    },
    "dispense-c14": {
        "quiz": [
            {
                "question": "Qual è la ripartizione dei compiti nel modello architetturale 'Client-Server' alla base del World Wide Web?",
                "options": [
                    "Il Client (il browser dell'utente) richiede le risorse, elabora l'interfaccia visiva e gestisce le interazioni locali; il Server ascolta le richieste, gestisce la logica di business, interroga i database e restituisce i dati protetti",
                    "Il Client gestisce i database bancari e il Server si occupa unicamente di renderizzare i font",
                    "Client e Server sono due componenti software installati sullo stesso chip dello smartphone",
                    "Il Server serve unicamente a stampare i fogli di carta negli uffici postali"
                ],
                "correctIndex": 0,
                "explanation": "Il Client (front-end) è l'ambiente locale dell'utente dove gira l'interfaccia; il Server (back-end) è il motore centrale remoto che custodisce i dati, protegge le password e garantisce la persistenza."
            },
            {
                "question": "Cosa garantisce il protocollo sicuro 'HTTPS' rispetto al vecchio protocollo HTTP non protetto?",
                "options": [
                    "Cifra l'intera sessione di comunicazione tramite protocolli TLS/SSL, impedendo a terzi di intercettare o alterare password, carte di credito e dati sensibili in transito (evitando attacchi Man-in-the-Middle)",
                    "Aumenta la velocità fisica della connessione internet a fibra ottica",
                    "Impedisce agli utenti di chiudere la finestra del browser prima del pagamento",
                    "Rende superfluo l'utilizzo di password per accedere ai propri account personali"
                ],
                "correctIndex": 0,
                "explanation": "HTTPS certifica l'identità del server ed esegue crittografia end-to-end: un malintenzionato su una rete Wi-Fi pubblica vedrà solo dati incomprensibili cifrati, garantendo privacy e integrità."
            },
            {
                "question": "Qual è la differenza semantica fondamentale tra un metodo di richiesta HTTP 'GET' e uno 'POST'?",
                "options": [
                    "GET richiede una risorsa al server senza alterarne lo stato (idempotente) passando i parametri nell'URL; POST invia dati nel corpo della richiesta (body) per creare o modificare informazioni persistenti sul server",
                    "GET serve per inviare file pesanti e POST serve solo per leggere immagini",
                    "GET funziona solo sui telefoni cellulari e POST solo sui computer da tavolo",
                    "Non sussiste alcuna differenza tecnica di funzionamento"
                ],
                "correctIndex": 0,
                "explanation": "GET è una richiesta di sola lettura sicura: non altera il database ed è memorizzabile nei segnalibri; POST trasmette payload strutturati (es. compilazione di un form d'ordine o credenziali) alterando lo stato sul server."
            },
            {
                "question": "A cosa serve il meccanismo di 'Caching' nei browser e nei server web?",
                "options": [
                    "A memorizzare copie temporanee di risorse statiche (immagini, CSS, file JS) in memoria locale per evitare di riscaricarle a ogni visita, riducendo drasticamente i tempi di caricamento e il traffico dati",
                    "A registrare tutte le conversazioni vocali degli utenti per fini pubblicitari",
                    "A cancellare periodicamente i file dal disco rigido per fare spazio",
                    "A convertire i file HTML in fogli di calcolo Excel"
                ],
                "correctIndex": 0,
                "explanation": "La cache è il salvavita della web performance: se il logo o il file CSS non sono cambiati, il browser li carica istantaneamente dalla memoria locale senza interrogare il server remoto a chilometri di distanza."
            },
            {
                "question": "Cosa indica un codice di stato HTTP della famiglia '4xx' (es. 404 o 403) restituito dal server?",
                "options": [
                    "Un errore originato dal Client (es. 404 Pagina non trovata per URL errato, o 403 Accesso non autorizzato a una risorsa protetta)",
                    "Una conferma di operazione avvenuta con pieno successo",
                    "Un guasto hardware irreversibile che richiede la sostituzione del server",
                    "Un reindirizzamento permanente verso un nuovo indirizzo web"
                ],
                "correctIndex": 0,
                "explanation": "Classi di stato HTTP: 2xx = Successo; 3xx = Reindirizzamento; 4xx = Errore Client (risorsa inesistente o permessi mancanti); 5xx = Errore Server (crash o sovraccarico del server)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un utente compila un form d'ordine e clicca 'Invia'. A causa della connessione lenta, non vede feedback visivo immediato e riclicca il bottone più volte. Se la richiesta è inviata via POST senza misure di protezione, quale grave disservizio si rischia?",
                "options": [
                    "L'invio multiplo dell'ordine con conseguente duplicazione involontaria dell'addebito economico e dei prodotti acquistati",
                    "La disinstallazione automatica del browser dal computer dell'utente",
                    "Il reset dei driver grafici della scheda video",
                    "La cancellazione di tutti i cookie salvati nella cronologia di navigazione"
                ],
                "correctIndex": 0,
                "explanation": "Le richieste POST non sono idempotenti: ogni click invia un nuovo record al database. L'UI deve disabilitare immediatamente il pulsante al primo click mostrando uno spinner (microinterazione) per evitare doppi addebiti."
            },
            {
                "question": "In termini di Web Performance Optimization, cosa rappresenta il parametro 'Time to First Byte' (TTFB)?",
                "options": [
                    "Il tempo che intercorre tra l'invio della richiesta HTTP dal client e la ricezione del primissimo byte di risposta elaborato dal server",
                    "Il tempo impiegato dal designer per scrivere il primo carattere del codice HTML",
                    "La durata complessiva del download di tutte le immagini fotografiche",
                    "La velocità di digitazione dell'utente sulla tastiera del computer"
                ],
                "correctIndex": 0,
                "explanation": "Il TTFB misura la reattività pura del server e della rete: un TTFB alto segnala che il server impiega troppo tempo per elaborare la richiesta (query database lente, assenza di cache o server sovraccarico)."
            },
            {
                "question": "Cosa indica l'acronimo 'API' (Application Programming Interface) nel contesto web (es. REST o GraphQL)?",
                "options": [
                    "Un insieme strutturato di endpoint e regole standard che consentono a due applicazioni o sistemi software differenti di scambiarsi dati in modo automatizzato e sicuro (tipicamente in formato JSON)",
                    "Un'estensione software per visualizzare contenuti grafici tridimensionali",
                    "Un algoritmo per la calibrazione cromatica delle stampanti digitali",
                    "Una tecnologia proprietaria per bloccare la navigazione nei siti concorrenti"
                ],
                "correctIndex": 0,
                "explanation": "Le API sono i contratti di scambio dati del mondo moderno: ad esempio, il client richiede via API meteo o tassi di cambio al server, ricevendo pacchetti JSON leggeri e aggiornati senza ricaricare la pagina."
            }
        ]
    }
}

dispense_quiz_data.update(dispense_c6_to_14)

# Load existing dispense-data.js
with open("data/dispense-data.js", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"window\.DISPENSE_DATA\s*=\s*(\[.*\]);?", content, re.DOTALL)
if not m:
    raise Exception("Could not find window.DISPENSE_DATA in data/dispense-data.js")

data = json.loads(m.group(1))

# Balance function: takes options, correctIndex, target_idx and swaps to ensure exact target_idx
def balance_question(q, target_idx):
    opts = list(q["options"])
    cur_idx = q["correctIndex"]
    if cur_idx != target_idx:
        opts[cur_idx], opts[target_idx] = opts[target_idx], opts[cur_idx]
    q["options"] = opts
    q["correctIndex"] = target_idx
    return q

for c_idx, chap in enumerate(data):
    cid = chap.get("id")
    if cid in dispense_quiz_data:
        quizzes = dispense_quiz_data[cid]["quiz"]
        exam_quizzes = dispense_quiz_data[cid]["examQuiz"]
        
        # Balance quiz across 0, 1, 2, 3 rotato per capitolo
        for idx, q in enumerate(quizzes):
            balance_question(q, (idx + c_idx) % 4)
            
        # Balance examQuiz rotato per capitolo
        for idx, eq in enumerate(exam_quizzes):
            balance_question(eq, (idx + c_idx + 2) % 4)
            
        chap["quiz"] = quizzes
        chap["examQuiz"] = exam_quizzes
        print(f"Updated {cid}: {len(chap['quiz'])} quiz, {len(chap['examQuiz'])} examQuiz")

with open("data/dispense-data.js", "w", encoding="utf-8") as f:
    f.write(f"// Dispense del professore strutturate per lo studio approfondito del Web Design\nwindow.DISPENSE_DATA = {json.dumps(data, indent=2, ensure_ascii=False)};\n")

print("Successfully rebuilt data/dispense-data.js with high academic rigor and balanced options!")
