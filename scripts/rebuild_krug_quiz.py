# -*- coding: utf-8 -*-
"""
Rebuilds data/krug-data.js with:
1. High-level academic chapter quizzes (chap.quiz) for all 14 chapters:
   - Realistic, UX-grade distractors (no childish/absurd choices).
   - Balanced correctIndex across 0, 1, 2, 3.
2. Dedicated exam simulation questions (chap.examQuiz) for all 14 chapters:
   - Distinct, scenario-based exam questions on usability heuristics and testing.
   - Realistic distractors.
   - Balanced correctIndex across 0, 1, 2, 3.
"""

import json, re

krug_quiz_data = {
    "krug-intro": {
        "quiz": [
            {
                "question": "Cosa intende Steve Krug quando definisce l'usabilità come 'buon senso comune' (common sense)?",
                "options": [
                    "Che chiunque interagisca con un oggetto o un sito web dovrebbe poterlo utilizzare per il suo scopo senza doversi fermare a riflettere sui meccanismi dell'interfaccia",
                    "Che gli utenti devono sostenere un esame di cultura generale prima di accedere a un servizio online",
                    "Che i programmatori non devono mai consultare manuali di stile o linee guida aziendali",
                    "Che i siti web devono contenere unicamente testi elementari privi di tecnicismi"
                ],
                "correctIndex": 0,
                "explanation": "Per Krug, l'usabilità è fare in modo che le cose funzionino in modo naturale ed evidente, eliminando qualsiasi ostacolo o rompicapo cognitivo tra l'intenzione dell'utente e il risultato."
            },
            {
                "question": "Quale atteggiamento mentale accomuna i visitatori di un sito web secondo l'osservazione empirica di Steve Krug?",
                "options": [
                    "Pazienza infinita e desiderio di esplorare l'architettura tecnica del server",
                    "Fretta costante, parsimonia dell'attenzione e tendenza a dedicare pochi secondi alla scansione di una schermata",
                    "Lettura meticolosa di tutti i testi di aiuto e delle condizioni legali prima di ogni clic",
                    "Preferenza sistematica per interfacce astratte prive di indicatori visivi"
                ],
                "correctIndex": 1,
                "explanation": "Gli utenti non navigano per ammirare il design: vogliono completare un compito nel minor tempo possibile con il minimo dispendio di energia mentale."
            },
            {
                "question": "Perché Steve Krug afferma che un buon design non deve 'far sentire stupido' l'utente?",
                "options": [
                    "Perché quando un utente non riesce a trovare un comando o clicca a vuoto, attribuisce la colpa alla propria incapacità, provando frustrazione e abbandonando il servizio",
                    "Perché la legge vieta espressamente di proporre form con più di tre campi",
                    "Perché i motori di ricerca penalizzano i siti che contengono messaggi di errore",
                    "Perché gli utenti esperti non commettono mai errori di navigazione"
                ],
                "correctIndex": 0,
                "explanation": "Uno dei più grandi danni invisibili di un'interfaccia complessa è il senso di inadeguatezza che genera nell'utente: quando il design è opaco, la persona si sente disorientata e se ne va."
            },
            {
                "question": "Qual è il rapporto tra la teoria dell'usabilità e le innovazioni tecnologiche secondo Krug?",
                "options": [
                    "Le tecnologie cambiano rapidamente (schermi touch, mobile, visori), ma la psicologia e le limitazioni percettive della mente umana rimangono costanti",
                    "Ogni nuova generazione di dispositivi richiede l'azzeramento totale di tutte le leggi di usabilità precedenti",
                    "L'usabilità si applica esclusivamente ai computer desktop con mouse e tastiera",
                    "I principi ergonomici dipendono dalla velocità in gigahertz del processore centrale"
                ],
                "correctIndex": 0,
                "explanation": "I principi fondamentali di Krug restano immutati perché poggiano sulla biologia e sulla cognizione umana: l'attenzione, la memoria di lavoro a breve termine e la scansione visiva non mutano col cambiare dei gadget."
            },
            {
                "question": "Cosa caratterizza un'esperienza d'uso che rispetta il principio cardine del libro?",
                "options": [
                    "L'utente raggiunge il proprio scopo senza incontrare punti interrogativi o attriti non necessari",
                    "L'interfaccia obbliga l'utente a leggere una guida illustrata preliminare",
                    "La pagina principale presenta animazioni continue per catturare lo sguardo",
                    "Tutte le opzioni di navigazione sono nascoste all'interno di sottomenu nidificati"
                ],
                "correctIndex": 0,
                "explanation": "L'esperienza ideale è trasparente: l'utente pensa unicamente al suo obiettivo (comprare un libro, verificare un orario), mentre l'interfaccia scompare come tramite invisibile ed efficiente."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team di progettazione sostiene che il proprio target è composto da utenti 'nativi digitali' che non hanno bisogno di etichette chiare o interfacce autoevidenti. Come risponderebbe Steve Krug a questa affermazione?",
                "options": [
                    "Che si tratta di un'illusione: anche gli utenti esperti e giovani preferiscono interfacce immediate e provano fastidio di fronte a inutili complicazioni o comandi nascosti",
                    "Che ha perfettamente ragione, poiché le nuove generazioni preferiscono decifrare interfacce complesse come fossero videogiochi",
                    "Che l'usabilità deve essere applicata solo a portali destinati a persone anziane",
                    "Che sui dispositivi moderni non è più necessario testare l'usabilità con utenti reali"
                ],
                "correctIndex": 0,
                "explanation": "Krug smonta il mito dell'utente che 'ama le sfide': nessuno desidera sprecare tempo ed energie mentali per capire dove cliccare, indipendentemente dalla propria età o competenza tecnologica."
            },
            {
                "question": "In una valutazione euristica rapida di un sito web, qual è il primo indicatore che segnala una potenziale violazione del principio 'Don't Make Me Think'?",
                "options": [
                    "La presenza di elementi la cui cliccabilità o significato richiede un momento di esitazione conscia ('Sarà un bottone o un titolo?')",
                    "L'utilizzo di un logo aziendale a colori nel quadrante superiore",
                    "La presenza di un modulo di contatto con campi nome ed email",
                    "L'impiego di una barra di navigazione orizzontale fissa"
                ],
                "correctIndex": 0,
                "explanation": "Il sintomo primario di una cattiva usabilità è l'esitazione: ogni volta che l'utente deve fermarsi per capire se una scritta è un link o una semplice etichetta, il principio è stato infranto."
            },
            {
                "question": "Quale differenza intercorre tra un difetto grafico puramente estetico e un problema di usabilità secondo l'approccio pragmatico di Krug?",
                "options": [
                    "Il difetto estetico riguarda il gusto personale soggettivo; il problema di usabilità blocca o rallenta oggettivamente l'utente nel compimento di un compito",
                    "L'usabilità riguarda solo la dimensione in pixel dei pulsanti",
                    "Non sussiste alcuna distinzione, trattandosi del medesimo fenomeno",
                    "I problemi di usabilità possono essere rilevati solo tramite software di telemetria automatica"
                ],
                "correctIndex": 0,
                "explanation": "I dibattiti estetici ('questo verde è troppo brillante') sono spesso soggettivi; i problemi di usabilità sono oggettivi e misurabili: l'utente clicca sul testo sbagliato, non trova il carrello o inserisce dati errati."
            }
        ]
    },
    "krug-c1": {
        "quiz": [
            {
                "question": "Cosa stabilisce esattamente la Prima Legge dell'usabilità di Steve Krug?",
                "options": [
                    "Ogni pagina web deve essere autoevidente: comprensibile a colpo d'occhio senza richiedere sforzo conscio di decifrazione",
                    "Tutte le schermate devono contenere meno di cinquanta parole di testo",
                    "I collegamenti ipertestuali devono essere sempre colorati di blu sottolineato standard",
                    "La navigazione deve svilupparsi unicamente lungo l'asse verticale"
                ],
                "correctIndex": 0,
                "explanation": "La Prima Legge 'Non farmi pensare!' impone che chiunque guardi una schermata capisca subito cos'è, cosa fa e dove può cliccare, senza dover risolvere indovinelli visivi."
            },
            {
                "question": "In cosa differisce una pagina 'autoevidente' da una 'autoesplicativa' nella terminologia di Krug?",
                "options": [
                    "L'autoevidente si comprende istantaneamente a colpo d'occhio senza sforzo cognitivo; l'autoesplicativa richiede pochissimi secondi di lettura ma è comunque chiara e immediata",
                    "L'autoevidente è pensata solo per smartphone, mentre l'autoesplicativa è per desktop",
                    "L'autoevidente contiene solo immagini, mentre l'autoesplicativa contiene solo testo",
                    "Non sussiste alcuna differenza, essendo sinonimi stilistici"
                ],
                "correctIndex": 0,
                "explanation": "L'autoevidenza è lo stato ottimale a sforzo zero; se la natura del servizio è complessa, il piano B accettabile è renderlo autoesplicativo: con una rapida occhiata di pochi secondi l'utente ne afferra il funzionamento."
            },
            {
                "question": "Cosa intende Krug con la metafora dei 'punti interrogativi cognitivi' (question marks)?",
                "options": [
                    "Le incertezze e le esitazioni istantanee (es. 'sarà cliccabile? da dove si comincia?') che consumano il budget di attenzione e la pazienza dell'utente",
                    "I caratteri di punteggiatura errati all'interno dei testi del sito",
                    "I quiz a risposta multipla inseriti nelle sezioni formative",
                    "I messaggi di alert del sistema operativo relativi alla sicurezza"
                ],
                "correctIndex": 0,
                "explanation": "Ogni dubbio consuma una frazione di energia mentale: quando i punti interrogativi si accumulano, l'utente sperimenta stanchezza e frustrazione, aumentando la probabilità di abbandono."
            },
            {
                "question": "Quale dei seguenti elementi d'interfaccia viola palesemente la Prima Legge di Krug?",
                "options": [
                    "Un link testuale che ha lo stesso colore del testo normale e non presenta sottolineatura né indizi visivi di cliccabilità",
                    "Un pulsante primario con elevato contrasto cromatico e testo chiaro 'Procedi al pagamento'",
                    "Un logo aziendale cliccabile posto nell'angolo superiore sinistro che rimanda alla home page",
                    "Una casella di ricerca affiancata da un'icona a forma di lente di ingrandimento"
                ],
                "correctIndex": 0,
                "explanation": "Mimetizzare un link nel corpo del testo costringe l'utente a passare il mouse a tentativi (minesweeping) per scoprire se è cliccabile, accendendo inutili punti interrogativi."
            },
            {
                "question": "Perché inventare nomi stravaganti o gergali per funzioni standard (es. chiamare 'Il nostro forziere' la sezione carrello) è un grave errore di design?",
                "options": [
                    "Perché costringe l'utente a riflettere per decifrare il significato anziché consentirgli di agire in base alle convenzioni consolidate che già padroneggia",
                    "Perché i motori di ricerca non accettano parole che non appartengono al vocabolario latino",
                    "Perché i browser mobili bloccano le parole composte da più di due sillabe",
                    "Perché aumenta il costo computazionale del rendering sul server"
                ],
                "correctIndex": 0,
                "explanation": "Le convenzioni d'uso (es. 'Carrello', 'Cerca', 'Accedi') sono già cablate nella memoria dell'utente: sostituirle con nomignoli 'creativi' crea smarrimento e rallenta l'azione."
            }
        ],
        "examQuiz": [
            {
                "question": "Un designer propone di sostituire i pulsanti classici con etichette minimaliste senza rilievo, bordo o colore differenziato, affermando che 'il contesto rende ovvio cosa fare'. Quale rischio di usabilità evidenzia Krug?",
                "options": [
                    "L'interfaccia perde l'affordance percepita, costringendo l'utente a domandarsi continuamente cosa sia interattivo e cosa no, provocando attrito cognitivo",
                    "Il browser richiederà più memoria per calcolare le coordinate del puntatore mouse",
                    "Il foglio di stile CSS non potrà essere convalidato dal W3C",
                    "Le immagini raster sgraneranno sui display ad alta risoluzione"
                ],
                "correctIndex": 0,
                "explanation": "Se tutto sembra testo statico, l'utente perde la fiducia nel sistema: il design deve rendere ovvia la natura dei controlli al primo sguardo, senza richiedere verifiche manuali col cursore."
            },
            {
                "question": "In un test di usabilità qualitativo, un partecipante fissa lo schermo per 8 secondi prima di cliccare su una voce di menu, mormorando 'Spero sia quella giusta'. Come si classifica questo fenomeno nella teoria di Krug?",
                "options": [
                    "Una chiara presenza di punti interrogativi cognitivi dovuta alla mancanza di autoevidenza nell'etichetta del menu",
                    "Un comportamento fisiologico tipico della lettura approfondita",
                    "Un errore imputabile unicamente all'ansia da prestazione del partecipante",
                    "Un segnale di eccellente engagement con il contenuto informativo"
                ],
                "correctIndex": 0,
                "explanation": "L'esitazione verbale e lo sguardo incerto sono i marcatori diagnostici tipici della frizione cognitiva: l'etichetta non ha comunicato con chiarezza la destinazione della pagina."
            },
            {
                "question": "Perché Steve Krug afferma che 'sul web ogni pagina deve poter essere la homepage'?",
                "options": [
                    "Perché molti utenti arrivano direttamente sulle pagine interne tramite motori di ricerca o link diretti, senza passare dalla prima pagina del sito",
                    "Perché tutte le pagine devono avere esattamente la stessa quantità di testo",
                    "Perché la home page deve essere duplicata in ogni cartella del server web",
                    "Perché i browser non consentono di creare più di un livello gerarchico di navigazione"
                ],
                "correctIndex": 0,
                "explanation": "Grazie a Google e ai link social, gli utenti 'cadono' dentro le pagine interne: ogni schermata deve chiarire istantaneamente dove ci si trova, di cosa tratta il sito e come navigare."
            }
        ]
    },
    "krug-c2": {
        "quiz": [
            {
                "question": "Cosa descrive la realtà empirica dell'uso del web rispetto al modello ideale che molti designer continuano a immaginare?",
                "options": [
                    "I designer immaginano utenti che leggono attentamente ogni riga; nella realtà gli utenti scorrono velocemente (scanning), cercano scorciatoie e cliccano sulla prima opzione plausibile",
                    "Gli utenti leggono ogni pagina dall'inizio alla fine come fosse un saggio letterario",
                    "Gli utenti studiano prima l'albero completo del sito tramite la mappa XML",
                    "Gli utenti navigano a occhi chiusi affidandosi esclusivamente all'audio"
                ],
                "correctIndex": 0,
                "explanation": "Krug smonta l'illusione del designer: le persone non leggono le pagine web, le 'scansionano' a caccia di parole chiave che intercettino il loro bisogno immediato."
            },
            {
                "question": "Quale concetto formulato dall'economista e psicologo Herbert Simon viene impiegato da Krug per descrivere il comportamento degli utenti web?",
                "options": [
                    "Satisficing (crasi di satisfy e suffice): accontentarsi della prima opzione ragionevolmente soddisfacente anziché cercare la scelta ottima assoluta",
                    "Ottimizzazione razionale globale a minima varianza",
                    "La teoria dei giochi a informazione asimmetrica completa",
                    "La dissonanza cognitiva post-decisionale"
                ],
                "correctIndex": 0,
                "explanation": "Gli utenti non confrontano tutte le alternative per trovare la migliore: cliccano sulla prima opzione che sembra promettente, perché se funziona risparmiano tempo, e se sbagliano possono tornare indietro."
            },
            {
                "question": "Cosa intende Steve Krug con l'espressione 'Muddling through' (arrangiarsi o tirare a campare)?",
                "options": [
                    "Gli utenti utilizzano siti e software senza comprendere a fondo come funzionano realmente, costruendosi modelli empirici parziali purché consentano di raggiungere l'obiettivo",
                    "Gli sviluppatori rilasciano software incompleto senza testarlo in locale",
                    "Gli utenti abbandonano il computer per tornare a utilizzare moduli cartacei",
                    "I browser ricaricano continuamente la cache di memoria a fronte di un errore"
                ],
                "correctIndex": 0,
                "explanation": "La maggior parte delle persone usa la tecnologia senza leggerne le istruzioni: se trovano un percorso che funziona (anche se inefficiente o bizzarro), continuano a riusarlo senza problemi."
            },
            {
                "question": "Perché gli utenti web non cercano la scelta ottimale ma adottano il 'satisficing'?",
                "options": [
                    "Perché hanno fretta, la sanzione per un errore sul web è bassissima (basta premere 'Indietro') e ponderare tutte le alternative costa troppa fatica mentale",
                    "Perché i browser limitano il numero massimo di clic per sessione a dieci",
                    "Perché le pagine web cambiano colore dopo tre secondi di inattività",
                    "Perché la connessione internet si interrompe se non si clicca rapidamente"
                ],
                "correctIndex": 0,
                "explanation": "Esaminare tutto richiede sforzo; cliccare sul primo link plausibile è rapido e quasi privo di rischio: il tasto 'Back' del browser è la cintura di sicurezza universale del web."
            },
            {
                "question": "Quale conseguenza deve trarre il designer dalla consapevolezza che gli utenti fanno 'scanning' e 'satisficing'?",
                "options": [
                    "Progettare pagine pensate per la scansione rapida, con titoli chiari, testi sintetici, parole chiave evidenti e inviti all'azione inequivocabili",
                    "Obbligare l'utente a completare un questionario di lettura prima di consentire il download",
                    "Eliminare tutte le immagini per costringere gli utenti a leggere il testo",
                    "Nascondere il pulsante Indietro del browser tramite script personalizzati"
                ],
                "correctIndex": 0,
                "explanation": "Se gli utenti si comportano da scansionatori affrettati, il design deve adattarsi alla loro natura, creando cartelli visivi evidenti anziché muri di prosa compatta."
            }
        ],
        "examQuiz": [
            {
                "question": "In un test di usabilità su un portale di viaggi, tutti i partecipanti ignorano un blocco informativo centrale intitolato 'Consigli utili per la prenotazione' e vanno dritti al form. Come si spiega questo fenomeno con la teoria di Krug?",
                "options": [
                    "Gli utenti hanno una missione focalizzata (task-oriented) ed eliminano dalla loro visione periferica qualsiasi testo che assomigli a istruzioni o materiale promozionale",
                    "I partecipanti al test non sanno leggere la lingua italiana",
                    "Il monitor del computer di test aveva una risoluzione troppo elevata",
                    "Il server non ha inviato correttamente i metadati della pagina"
                ],
                "correctIndex": 0,
                "explanation": "Gli utenti filtrano selettivamente: saltano i blocchi di preambolo o istruzioni e cercano subito i controlli d'azione (campi input, calendari, pulsanti)."
            },
            {
                "question": "Perché la possibilità di tornare facilmente indietro (tasto Back efficace e privo di loop di trappola) è un cardine della psicologia del satisficing?",
                "options": [
                    "Perché rimuove l'ansia da errore: l'utente sperimenta liberamente sapendo che ogni decisione sbagliata può essere annullata in un solo millisecondo",
                    "Perché il tasto Back libera spazio nella memoria RAM del computer",
                    "Perché i motori di ricerca richiedono il tasto Back per posizionare il sito nei primi risultati",
                    "Perché i contratti commerciali impongono la reversibilità di ogni pagina web"
                ],
                "correctIndex": 0,
                "explanation": "Sapere che un errore non costa nulla incoraggia l'utente a cliccare velocemente: se un sito rompe il tasto 'Back' (es. con redirect forzati o popup trappola), l'utente perde fiducia e chiude la scheda."
            },
            {
                "question": "Cosa si intende per 'Foraging' (o Scent of Information) nel comportamento di scansione degli utenti?",
                "options": [
                    "La teoria secondo cui gli utenti seguono 'l'odore' informativo dei link (parole chiave rilevanti) come predatori a caccia, abbandonando il percorso se la traccia si fa debole o ingannevole",
                    "La scansione automatica dei codici a barre tramite fotocamera del telefono",
                    "La ricerca manuale di vulnerabilità informatiche all'interno del codice sorgente",
                    "La raccolta di recensioni positive da parte di influenzatori digitali"
                ],
                "correctIndex": 0,
                "explanation": "Formulata da Pirolli e Card (PARC), la teoria del foraging spiega che l'utente 'fiuta' il link: se l'etichetta promette bene, prosegue; se 'l'odore' sfuma, fa dietrofront."
            }
        ]
    }
}

# Add chapters 3 to 13 for Krug
krug_c3_to_13 = {
    "krug-c3": {
        "quiz": [
            {
                "question": "Quale analogia visiva utilizza Krug nel Capitolo 3 per spiegare come dobbiamo progettare le pagine web?",
                "options": [
                    "Come cartelloni pubblicitari lungo un'autostrada a 130 km/h: devono trasmettere il messaggio all'istante a chi sfreccia veloce",
                    "Come un tomo enciclopedico da consultare in una biblioteca silenziosa",
                    "Come una scacchiera in cui ogni mossa richiede dieci minuti di riflessione",
                    "Come un dipinto impressionista da contemplare da lontano"
                ],
                "correctIndex": 0,
                "explanation": "L'utente web sfreccia a tutta velocità: se il cartellone richiede concentrazione o ha scritte microscopiche, chi guida tira dritto senza aver recepito nulla."
            },
            {
                "question": "Quali sono i 5 requisiti fondamentali indicati da Krug per progettare pagine adatte a una scansione efficace?",
                "options": [
                    "Sfruttare le convenzioni, creare una gerarchia visiva chiara, suddividere in aree ben definite, rendere ovvio cosa è cliccabile ed eliminare le distrazioni inutili",
                    "Usare almeno dieci colori diversi, inserire musica di sottofondo, duplicare i menu, usare font gotici e nascondere i link",
                    "Inserire solo video, eliminare la navigazione, bloccare lo scorrimento, usare solo caratteri maiuscoli e disabilitare il mouse",
                    "Richiedere sempre login obbligatorio, mostrare pubblicità a pieno schermo, usare solo popup e rimuovere il piè di pagina"
                ],
                "correctIndex": 0,
                "explanation": "Queste 5 regole d'oro sono la cassetta degli attrezzi di Krug: trasformano una pagina caotica in un ambiente leggibile all'istante anche da un visitatore distratto."
            },
            {
                "question": "Perché le convenzioni di design (es. logo in alto a sinistra, icona del carrello, lente per la ricerca) sono preziosissime?",
                "options": [
                    "Perché funzionano: gli utenti sanno già esattamente cosa significano e dove trovarle senza dover imparare da capo le regole del vostro sito",
                    "Perché sono protette da brevetti internazionali che ne vietano la modifica",
                    "Perché riducono il consumo energetico dei router domestici",
                    "Perché impediscono agli utenti di navigare sui siti concorrenti"
                ],
                "correctIndex": 0,
                "explanation": "La creatività fuori contesto è nemica dell'usabilità: reinventare la ruota per il carrello o la ricerca genera solo confusione. Innovate solo se la nuova soluzione è nettamente superiore e autoevidente."
            },
            {
                "question": "Cosa caratterizza una gerarchia visiva chiara ed efficace in una schermata?",
                "options": [
                    "Gli elementi più importanti sono visivamente più evidenti, gli elementi logicamente correlati sono vicini o raggruppati e la subordinazione è palese (titolo > sottotitolo > corpo)",
                    "Tutti gli elementi hanno la stessa identica grandezza e colore per rispettare la parità democratica delle informazioni",
                    "I testi secondari sono più grandi dei titoli per stimolare la curiosità",
                    "La pagina è organizzata senza alcuno schema per incoraggiare la scoperta casuale"
                ],
                "correctIndex": 0,
                "explanation": "Una buona gerarchia fa risparmiare tempo: guardando la pagina si capisce subito qual è la notizia regina, quali sono le sezioni secondarie e quali i dettagli."
            },
            {
                "question": "Cosa si intende per 'rumore visivo' (visual noise) nelle pagine web?",
                "options": [
                    "Un disordine caotico in cui troppi elementi urlano contemporaneamente per attirare l'attenzione, stancando l'utente e impedendogli di concentrarsi",
                    "Il ronzio prodotto dalla ventola di raffreddamento del computer",
                    "Un effetto sonoro inserito nei videogiochi interattivi",
                    "La presenza di file audio incorporati nel markup HTML"
                ],
                "correctIndex": 0,
                "explanation": "Il rumore visivo è l'equivalente grafico di un mercato affollato: troppe icone animate, troppi colori contrastanti e margini inesistenti provocano repulsione e fuga."
            }
        ],
        "examQuiz": [
            {
                "question": "Un art director rifiuta di usare l'icona canonica della lente di ingrandimento per la barra di ricerca, sostituendola con una bussola nautica per essere 'originale'. Come commenterebbe Steve Krug questa scelta?",
                "options": [
                    "Un classico errore di vanità creativa: l'utente cerca la convenzione (la lente) e rischia di non riconoscere la barra di ricerca, generando frustrazione gratuita",
                    "Una splendida innovazione che arricchisce la personalità emotiva del brand senza alcun impatto sull'uso",
                    "Una violazione sanzionabile legalmente dalle norme sulla navigazione marittima",
                    "Una scelta ininfluente poiché nessuno usa più la ricerca interna nei siti web"
                ],
                "correctIndex": 0,
                "explanation": "Le metafore visive esotiche violano le convenzioni consolidate: l'utente non vuole interpretare enigmi poetici per compiere un'azione banale come fare una ricerca."
            },
            {
                "question": "Come si traduce nel codice CSS il principio di 'suddividere la pagina in aree chiaramente definite'?",
                "options": [
                    "Utilizzando sfondi cromatici distinti, bordi leggeri, card e un sapiente uso dello spazio negativo per separare visivamente i blocchi logici",
                    "Inserendo linee nere spesse di 20 pixel tra ogni paragrafo",
                    "Applicando l'effetto marquee a tutte le sezioni secondarie",
                    "Forzando l'apertura di una nuova finestra popup per ogni argomento"
                ],
                "correctIndex": 0,
                "explanation": "Raggruppare i contenuti in 'isole' visive (es. card con sfondo bianco su grigio chiaro) consente allo sguardo di isolare all'istante l'area d'interesse scartando il resto."
            },
            {
                "question": "Cosa rende immediatamente evidente che un elemento su schermo è cliccabile secondo le buone pratiche di usabilità?",
                "options": [
                    "La forma (a bottone tridimensionale o con padding e sfondo pieno), il colore distintivo rispetto al testo ordinario, la sottolineatura per i link e il cambio di cursore (pointer) in hover",
                    "L'inserimento di una casella di testo lampeggiante accanto a ogni parola",
                    "Un suono emesso dagli altoparlanti al passaggio del cursore",
                    "L'obbligo di fare doppio clic veloce per attivare qualsiasi collegamento"
                ],
                "correctIndex": 0,
                "explanation": "Un elemento interattivo deve 'sembrare' cliccabile: se l'utente deve indovinare o passare il cursore a tappeto per scoprire cosa risponde al clic, il design ha fallito."
            }
        ]
    },
    "krug-c4": {
        "quiz": [
            {
                "question": "Cosa stabilisce la Seconda Legge dell'usabilità di Steve Krug a proposito dei clic?",
                "options": [
                    "Non conta quante volte devo cliccare, purché ogni singolo clic sia una scelta ovvia, facile e priva di ambiguità",
                    "Nessun contenuto del sito deve mai essere posizionato a più di tre clic dalla homepage (la rigida regola dei tre clic)",
                    "Ogni pagina web deve contenere esattamente un solo collegamento ipertestuale",
                    "Gli utenti su dispositivi mobili rifiutano qualsiasi interfaccia che richieda più di due interazioni"
                ],
                "correctIndex": 0,
                "explanation": "Krug smonta il dogma della 'regola dei 3 clic': fare 4 o 5 clic immediati, guidati e privi di dubbi non pesa affatto; al contrario, un solo clic misterioso genera enorme fatica mentale."
            },
            {
                "question": "Perché la classica 'Regola dei 3 clic' è considerata un mito superato nella UX moderna?",
                "options": [
                    "Perché i test con gli utenti dimostrano che la soddisfazione e il successo dipendono dalla chiarezza del percorso, non dal conteggio aritmetico dei clic",
                    "Perché i sistemi operativi moderni impediscono di contare i clic degli utenti",
                    "Perché sui dispositivi touch non esistono i clic ma solo i tap",
                    "Perché i motori di ricerca declassano i siti con meno di 10 pagine"
                ],
                "correctIndex": 0,
                "explanation": "Non è il numero di clic che infastidisce l'utente, ma il dubbio: cliccare senza dover pensare è indolore e rapido; dover riflettere a ogni bivio svuota la pazienza."
            },
            {
                "question": "Cosa intende Krug quando paragona una serie di scelte ben progettate al gioco 'Animale, vegetale o minerale'?",
                "options": [
                    "Che ogni bivio decisionale deve essere categorico, mutualmente esclusivo e ovvio, cosicché l'utente risponda all'istante senza esitazione",
                    "Che i siti web devono parlare di scienze naturali per essere compresi da tutti",
                    "Che la classificazione dei prodotti deve seguire la tassonomia di Linneo",
                    "Che la navigazione deve essere strutturata come un videogioco a premi"
                ],
                "correctIndex": 0,
                "explanation": "Nel celebre gioco delle 20 domande, la prima partizione è limpida (è un animale, un vegetale o un minerale?). Così deve essere la navigazione: categorie nette dove non si può sbagliare."
            },
            {
                "question": "Quale situazione crea grave incertezza e rallenta l'utente nella scelta tra due voci di navigazione?",
                "options": [
                    "Quando le categorie si sovrappongono concettualmente (es. 'Lavori recenti' e 'Progetti portfolio'), lasciando l'utente nel dubbio su dove cliccare",
                    "Quando le voci di menu sono scritte con caratteri sans-serif",
                    "Quando il menu contiene meno di quattro collegamenti",
                    "Quando la barra di navigazione è posizionata in cima alla pagina"
                ],
                "correctIndex": 0,
                "explanation": "Se due categorie contengono argomenti contigui o ambigui, l'utente si blocca: 'Dove sarà quello che cerco?'. Le categorie devono essere chiaramente differenziate."
            },
            {
                "question": "Cosa rende un clic davvero 'faticoso' per l'utente?",
                "options": [
                    "Il carico cognitivo necessario per decidere se quel clic lo porterà nella direzione corretta o in un vicolo cieco",
                    "La resistenza meccanica del tasto sinistro del mouse",
                    "Il consumo energetico della batteria del computer",
                    "La presenza di file multimediali nella pagina successiva"
                ],
                "correctIndex": 0,
                "explanation": "La fatica non è fisica (muovere il dito), ma mentale: l'ansia di fare la scelta sbagliata, di finire in trappola o di dover ricominciare da capo."
            }
        ],
        "examQuiz": [
            {
                "question": "Un e-commerce di abbigliamento inserisce due voci nel menu principale: 'Moda Uomo' e 'Abbigliamento Maschile'. Un cliente vuole una giacca. Quale problema di usabilità si manifesta?",
                "options": [
                    "Ambiguità tassonomica: le etichette sono sinonimi apparenti ma rimandano a sezioni diverse, costringendo l'utente a un'ipotesi cieca",
                    "Una violazione delle norme sulla concorrenza sleale",
                    "Un errore di traduzione causato dal browser",
                    "Un problema di caching delle sessioni HTTP sul server"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il tipico fallimento del principio 'Animale, vegetale o minerale': l'utente non ha indizi razionali per scegliere l'una o l'altra e deve tirare a indovinare."
            },
            {
                "question": "Perché un percorso a 4 passaggi lineari e guidati (Wizard) per compilare una richiesta complessa è spesso preferibile a un unico schermata monolitica con 30 campi?",
                "options": [
                    "Perché suddivide il carico cognitivo in bocconi digeribili (Chunking), rassicurando l'utente sui progressi e riducendo l'ansia decisionale",
                    "Perché aumenta il numero di visualizzazioni di pagina per gli inserzionisti pubblicitari",
                    "Perché i database non supportano la memorizzazione di più di cinque campi per tabella",
                    "Perché la connessione mobile non può trasmettere più di 1 kilobyte di dati per volta"
                ],
                "correctIndex": 0,
                "explanation": "La Seconda Legge in azione: 4 schermate semplici con 5 campi ciascuna sono infinitamente più facili e meno intimidatorie di una sola pagina sterminata che spaventa al primo sguardo."
            },
            {
                "question": "In un funnel di acquisto, quale informazione elimina l'ansia dell'utente sul clic finale 'Procedi'?",
                "options": [
                    "Un riepilogo chiaro che specifica esattamente cosa accadrà al clic successivo (es. 'Nel prossimo passaggio potrai rivedere l'ordine prima di pagare')",
                    "La presenza di una fotografia del magazzino delle merci",
                    "Un contatore alla rovescia di 30 secondi che crea urgenza artificiale",
                    "Un link alle condizioni generali di contratto di 80 pagine"
                ],
                "correctIndex": 0,
                "explanation": "La trasparenza toglie la paura: rassicurare l'utente che il clic non comporterà un addebito immediato ma mostrerà prima la conferma finale elimina l'esitazione all'acquisto."
            }
        ]
    },
    "krug-c5": {
        "quiz": [
            {
                "question": "Cosa impone la Terza Legge dell'usabilità di Steve Krug riguardo ai testi sul web?",
                "options": [
                    "Elimina metà delle parole di ogni pagina. Poi elimina metà di ciò che resta",
                    "Tutti i testi devono essere scritti in rima per essere ricordati",
                    "Le pagine web devono contenere almeno duemila parole per essere indicizzate da Google",
                    "I paragrafi devono essere composti da frasi di esattamente otto parole"
                ],
                "correctIndex": 0,
                "explanation": "La Terza Legge è una provocazione salutare contro la prolissità: riducendo drasticamente il testo superfluo, si abbatte il rumore visivo ed emergono i contenuti di reale valore."
            },
            {
                "question": "Cosa intende Steve Krug con il termine dispregiativo 'Happy Talk' (chiacchiere inutili)?",
                "options": [
                    "Testi introduttivi e autocelebrativi, privi di informazioni concrete (es. 'Benvenuti nel nostro portale! Ci impegniamo ogni giorno per offrirvi...') che nessuno legge mai",
                    "Le conversazioni informali registrate durante i test di usabilità",
                    "I messaggi promozionali inviati tramite newsletter settimanali",
                    "I commenti lasciati dagli utenti sui social network aziendali"
                ],
                "correctIndex": 0,
                "explanation": "L'happy talk è fuffa editoriale: ruba spazio prezioso, rallenta chi cerca informazioni e fa sentire il sito come un depliant pubblicitario degli anni '90 anziché uno strumento utile."
            },
            {
                "question": "Perché le lunghe istruzioni d'uso scritte sulle pagine web (es. 'Per compilare il modulo, inserire prima...') sono solitamente inutili?",
                "options": [
                    "Perché nessuno le legge: gli utenti si buttano subito a compilare i campi, e se l'interfaccia è ben disegnata le istruzioni risultano superflue",
                    "Perché i browser mobili non visualizzano i testi formattati come istruzioni",
                    "Perché la legge impone di comunicare unicamente tramite simboli grafici",
                    "Perché le istruzioni aumentano i tempi di latenza del database"
                ],
                "correctIndex": 0,
                "explanation": "Il vostro obiettivo deve essere rendere i controlli autoevidenti: se un form ha bisogno di un paragrafo di istruzioni per essere compilato, il problema è il form, non l'utente."
            },
            {
                "question": "Quali benefici immediati produce il taglio drastico delle parole non necessarie in una pagina?",
                "options": [
                    "Riduce il rumore visivo, rende la pagina più corta e scansionabile e consente alle informazioni essenziali di emergere con forza",
                    "Aumenta il costo dell'abbonamento alla connessione internet",
                    "Costringe il browser a scaricare nuovi caratteri tipografici",
                    "Impedisce agli utenti di copiare il testo nella memoria del computer"
                ],
                "correctIndex": 0,
                "explanation": "Meno parole = più chiarezza: l'occhio individua istantaneamente i punti chiave, lo scrolling si riduce e l'esperienza di navigazione diventa snella e piacevole."
            },
            {
                "question": "Quale tecnica di scrittura è preferibile per presentare un elenco di requisiti o vantaggi all'interno di una pagina web?",
                "options": [
                    "Un elenco puntato sintetico con parole chiave evidenziate in grassetto all'inizio di ciascun punto",
                    "Un unico blocco di testo continuo di venti righe privo di interruzioni",
                    "Un testo scorrevole dal basso verso l'alto con velocità variabile",
                    "Un testo crittografato che si svela solo al passaggio del cursore"
                ],
                "correctIndex": 0,
                "explanation": "Gli elenchi puntati (bullet points) sono perfetti per la scansione: isolano i concetti, creano ritmo visivo e consentono di assorbire i punti chiave in una frazione di secondo."
            }
        ],
        "examQuiz": [
            {
                "question": "La homepage di una clinica medica si apre con: 'Benvenuti nel nostro sito web! Fondata nel 1982 con passione e dedizione, la nostra struttura è lieta di accogliervi nella sua nuova casa digitale...'. Come interverrebbe un UX copywriter seguendo Krug?",
                "options": [
                    "Cancellerebbe totalmente l'intero paragrafo, sostituendolo subito con i servizi primari ('Prenota visita', 'Orari prelievi', 'I nostri specialisti')",
                    "Aggiungerebbe altri due paragrafi sulla storia dei fondatori per aumentare l'autorevolezza",
                    "Convertirebbe il testo in caratteri maiuscoli lampeggianti",
                    "Sposterebbe il paragrafo all'interno di una finestra popup modale a comparsa automatica"
                ],
                "correctIndex": 0,
                "explanation": "Puro happy talk: chi visita il sito di una clinica vuole prenotare una visita o sapere dove andare, non leggere preamboli retorici. Via il superfluo, spazio ai servizi."
            },
            {
                "question": "In un modulo di registrazione, sopra il campo password c'è scritto: 'Attenzione: si prega di notare che la password deve obbligatoriamente contenere almeno otto caratteri...'. Come si riscrive secondo il principio di sintesi?",
                "options": [
                    "Con un testo microcopy conciso sotto il campo: 'Minimo 8 caratteri (inclusi 1 numero e 1 maiuscola)' che si spunta in verde man mano che i criteri sono soddisfatti",
                    "Raddoppiando la lunghezza del testo per spiegare la crittografia SHA-256",
                    "Eliminando qualsiasi indicazione e mostrando un alert di errore dopo l'invio",
                    "Richiedendo di digitare la password due volte prima di mostrarne le regole"
                ],
                "correctIndex": 0,
                "explanation": "Il microcopy efficace è breve, contestuale e visivo: niente preamboli burocratici, solo i requisiti essenziali posizionati esattamente dove serve e quando serve."
            },
            {
                "question": "Qual è il test più efficace per verificare se un testo web è troppo lungo?",
                "options": [
                    "Leggerlo ad alta voce ed eliminare ogni parola o frase che non aggiunge informazioni concrete utili al lettore per decidere o agire",
                    "Controllare se il testo occupa esattamente cento kilobyte sul disco fisso",
                    "Verificare che il numero di aggettivi superi il numero dei sostantivi",
                    "Sottoporre il testo a un software di generazione automatica di poesie"
                ],
                "correctIndex": 0,
                "explanation": "La lettura ad alta voce smaschera subito l'artificiosità e la prolissità: ciò che suona ampolloso o ridondante all'orecchio sarà ignorato con certezza sullo schermo."
            }
        ]
    },
    "krug-c6": {
        "quiz": [
            {
                "question": "Cosa intende Steve Krug con il concetto di 'Navigazione Persistente' (Persistent Navigation)?",
                "options": [
                    "L'insieme coerente di elementi di orientamento e navigazione presenti nell'identica posizione su ogni singola pagina del sito (con pochissime eccezioni come il checkout)",
                    "Una finestra popup che rimane bloccata a schermo anche quando l'utente cambia sito web",
                    "Un cookie di tracciamento che memorizza le preferenze dell'utente per dieci anni",
                    "Una barra di scorrimento verticale che non può essere mossa con il mouse"
                ],
                "correctIndex": 0,
                "explanation": "La navigazione persistente è la bussola del sito: garantisce stabilità e sicurezza psicologica, confermando all'utente che si trova sempre nello stesso luogo coerente."
            },
            {
                "question": "Quali sono i quattro elementi strutturali indispensabili che compongono la navigazione persistente standard?",
                "options": [
                    "Il Site ID (logo/marchio), le sezioni primarie, le utility di servizio (cerca, login, lingua) e l'indicatore 'Tu sei qui'",
                    "Il contatore di visite, il codice fiscale, il copyright e il link al meteo locale",
                    "La pubblicità banner, il lettore musicale, la mappa geografica e il pulsante di stampa",
                    "Il modulo dei commenti, l'orologio digitale, il convertitore di valute e il fax"
                ],
                "correctIndex": 0,
                "explanation": "Questi 4 pilastri dicono all'utente: 1) Di che sito si tratta (Logo), 2) Quali sono le macro-aree (Sezioni), 3) Quali strumenti ho (Utility), 4) Dove mi trovo in questo momento ('Tu sei qui')."
            },
            {
                "question": "Quale funzione cruciale svolge il 'Site ID' (logo aziendale) collocato nell'angolo superiore sinistro?",
                "options": [
                    "Funge da insegna identificativa del portale e da scorciatoia universale cliccabile per tornare in qualsiasi momento alla homepage con un solo clic",
                    "Serve unicamente a proteggere i diritti legali del marchio registrato",
                    "Attiva la riproduzione del file audio con l'inno aziendale",
                    "Permette di scaricare il bilancio economico dell'impresa"
                ],
                "correctIndex": 0,
                "explanation": "Il logo in alto a sinistra è la convenzione più forte del web: identifica il proprietario del sito e funge da salvagente universale per ricominciare da capo (ritorno in Home)."
            },
            {
                "question": "Cosa si intende per indicatore 'Tu sei qui' (You Are Here) all'interno di un menu di navigazione?",
                "options": [
                    "Una marcatura visiva evidente (colore di sfondo differente, contrasto accentuato, sottolineatura marcata) applicata alla voce di menu corrispondente alla sezione attiva",
                    "Le coordinate GPS calcolate dal sensore satellitare dello smartphone",
                    "Una mappa geografica interattiva collocata al centro dello schermo",
                    "Un messaggio vocale preregistrato che pronuncia il nome della pagina"
                ],
                "correctIndex": 0,
                "explanation": "Nel mondo fisico sappiamo dove siamo; nel digitale non c'è gravità né spazio: evidenziare la voce attiva nel menu àncora la persona e le impedisce di sentirsi smarrita."
            },
            {
                "question": "Quale metafora usa Krug per descrivere la navigazione nei siti web?",
                "options": [
                    "I cartelli stradali in una città sconosciuta: guidano senza farsi notare, rassicurano e permettono di orientarsi al primo colpo d'occhio",
                    "Un labirinto mitologico progettato da Dedalo per nascondere il Minotauro",
                    "Un percorso a ostacoli per atleti professionisti",
                    "Un puzzle di mille tessere da ricomporre con pazienza"
                ],
                "correctIndex": 0,
                "explanation": "La segnaletica stradale non richiede studio: una freccia e una scritta su sfondo contrastante dicono tutto in un millisecondo. Così deve operare la navigazione sul web."
            }
        ],
        "examQuiz": [
            {
                "question": "Un sito di e-commerce rimuove la navigazione persistente, le sezioni e la barra di ricerca unicamente all'interno del flusso di Checkout finale. Come valuta Steve Krug questa eccezione?",
                "options": [
                    "Corretta ed eccellente: eliminare le distruzioni durante il pagamento (Enclosed Checkout) aiuta l'utente a focalizzarsi sull'ordine evitando l'abbandono accidentale del carrello",
                    "Un gravissimo errore che viola le leggi internazionali sull'usabilità",
                    "Una scelta sbagliata poiché l'utente deve poter accedere alla homepage in qualsiasi secondo",
                    "Un comportamento illecito secondo le direttive commerciali europee"
                ],
                "correctIndex": 0,
                "explanation": "Il checkout è una delle rare eccezioni giustificate: una volta entrati nel pagamento, togliere i menu riduce le vie di fuga e le distrazioni, guidando la persona verso il completamento."
            },
            {
                "question": "Quale errore visivo si commette frequentemente nell'implementazione delle Breadcrumbs (briciole di pane)?",
                "options": [
                    "Renderle troppo grandi o colorate facendole competere con il titolo principale della pagina, oppure omettere la pagina corrente alla fine della sequenza",
                    "Posizionarle sopra il titolo dell'articolo in caratteri piccoli",
                    "Utilizzare il simbolo '>' come separatore tra i livelli gerarchici",
                    "Rendere cliccabili tutti i livelli tranne l'ultimo (la pagina attuale)"
                ],
                "correctIndex": 0,
                "explanation": "Le breadcrumbs sono un accessorio secondario: devono essere discrete, in corpo minore e in toni neutri, posizionate subito sopra il titolo H1 come comodo promemoria gerarchico."
            },
            {
                "question": "Perché un menu di navigazione non dovrebbe mai superare le 5-7 voci principali al primo livello?",
                "options": [
                    "Per rispettare i limiti della memoria di lavoro a breve termine (Legge di Miller 7±2) e consentire una scansione immediata senza sforzo cognitivo",
                    "Perché i monitor desktop non possono renderizzare più di sette parole affiancate",
                    "Perché i browser mobili nascondono automaticamente le voci successive alla settima",
                    "Perché il consorzio W3C impone sanzioni economiche ai siti con menu troppo ampi"
                ],
                "correctIndex": 0,
                "explanation": "Meno voci = più pregnanza: 5 o 6 categorie ben distinte coprono l'intero perimetro aziendale senza saturare la mente dell'utente con elenchi sterminati."
            }
        ]
    },
    "krug-c7": {
        "quiz": [
            {
                "question": "Cos'è il celebre 'Trunk Test' (Test del bagagliaio) inventato da Steve Krug?",
                "options": [
                    "Un protocollo di valutazione rapido: immagina di essere rapito, rinchiuso nel bagagliaio di un'auto e scaricato su una pagina interna casuale di un sito: riesci a capire subito dove sei e cosa puoi fare?",
                    "Un test di resistenza fisica per i computer portatili trasportati in automobile",
                    "Una procedura per verificare la velocità di caricamento delle pagine web su rete 4G",
                    "Un algoritmo per comprimere le immagini all'interno di archivi ZIP"
                ],
                "correctIndex": 0,
                "explanation": "Il Trunk Test simula l'atterraggio da motore di ricerca: se catapultati su una pagina interna profonda capite subito il sito, la sezione e cosa fare, il design ha superato la prova."
            },
            {
                "question": "A quali 6 domande fondamentali deve rispondere immediatamente una pagina per superare il Trunk Test?",
                "options": [
                    "Di che sito si tratta? Che pagina è? Quali sono le sezioni primarie? Quali opzioni ho a questo livello? Dove sono rispetto al tutto? Come faccio a cercare?",
                    "Quanto costa il dominio? Chi è il programmatore? In che linguaggio è scritto? Che versione di database usa? Quanto consuma il server? Chi è il grafico?",
                    "Che ore sono? Che tempo fa? Qual è il valore dell'indice azionario? Quanti utenti sono connessi? Qual è la velocità del Wi-Fi? Dove si trova il server?",
                    "Solo due domande: Qual è il nome dell'amministratore delegato e dove si trova la sede legale dell'impresa?"
                ],
                "correctIndex": 0,
                "explanation": "Se una schermata risponde a questi 6 quesiti nei primi 5 secondi, la navigazione è solida e l'utente non proverà mai la sensazione di disorientamento."
            },
            {
                "question": "Quale elemento grafico fornisce la risposta immediata alla domanda 'Che pagina è questa?' nel Trunk Test?",
                "options": [
                    "Un titolo di pagina chiaro, prominente (tipicamente il tag <h1>) posizionato in cima al contenuto principale e coerente con il link che lo ha generato",
                    "Un'immagine decorativa priva di testo alternativo",
                    "La data e l'ora visualizzate nell'angolo dello schermo",
                    "Il nome del file sorgente visualizzato nella barra di stato del browser"
                ],
                "correctIndex": 0,
                "explanation": "Il titolo di pagina è il cartello della stanza: se ho cliccato su 'Contatti', in cima alla pagina devo leggere cubitale 'Contattaci', senza ambiguità terminologiche."
            },
            {
                "question": "Cosa rende fallimentare l'orientamento in una pagina interna quando un utente arriva da un link esterno (es. social o Google)?",
                "options": [
                    "L'assenza del logo aziendale, un titolo generico o mancante e l'assenza di indicatori nella navigazione che chiariscano a quale macro-sezione appartenga il contenuto",
                    "La presenza di troppe fotografie ad alta risoluzione",
                    "L'utilizzo di uno sfondo bianco uniforme",
                    "La presenza di link che rimandano ad altre pagine dello stesso sito"
                ],
                "correctIndex": 0,
                "explanation": "Chi sbarca dall'esterno non ha visto la home page: se la pagina non ha logo, né titolo chiaro, né menu di contesto, l'utente si sente in un vicolo cieco ed esce subito."
            },
            {
                "question": "Come si esegue praticamente un Trunk Test durante la revisione di un progetto?",
                "options": [
                    "Si stampa o si visualizza una pagina interna a caso, ci si allontana o la si guarda per pochissimi secondi e si verifica se le 6 risposte cardine sono immediatamente visibili",
                    "Si esegue uno script automatico da terminale Linux per testare il throughput dei socket TCP",
                    "Si misura la temperatura della batteria del dispositivo mobile durante la navigazione",
                    "Si confronta il codice HTML con le direttive del manuale del linguaggio C++"
                ],
                "correctIndex": 0,
                "explanation": "È un test visivo e cognitivo fulmineo: basta guardare una pagina interna e verificare se un osservatore ingenuo indovina all'istante sito, tema e sezioni."
            }
        ],
        "examQuiz": [
            {
                "question": "Un utente atterra su un articolo tramite un link su LinkedIn. Nella testata manca il logo e c'è solo una scritta 'Blog'. Nel menu non c'è alcuna voce attiva. Quale fallimento del Trunk Test si è verificato?",
                "options": [
                    "Mancano il Site ID (identità del mittente) e l'indicatore 'Tu sei qui': l'utente non sa chi stia parlando né dove si collochi l'articolo nel portale",
                    "Un errore di routing del certificato SSL del server",
                    "La mancata installazione del font tipografico nel sistema operativo del client",
                    "Una violazione delle specifiche CSS Grid di livello 2"
                ],
                "correctIndex": 0,
                "explanation": "Senza Site ID l'utente non riconosce l'autorevolezza della fonte; senza gerarchia non sa se ci siano altri articoli affini: l'esperienza di orientamento è completamente azzerata."
            },
            {
                "question": "Perché il titolo della pagina deve coincidere concettualmente con il testo del pulsante o del link su cui si è appena cliccato?",
                "options": [
                    "Per fornire immediata conferma psicologica che il clic ha prodotto l'effetto atteso, evitando l'ansia di essere atterrati nel posto sbagliato",
                    "Per consentire ai browser di calcolare correttamente la larghezza della pagina",
                    "Perché i fogli di stile CSS non supportano testi diversi tra link e titoli",
                    "Perché altrimenti il server restituisce un codice di errore HTTP 301"
                ],
                "correctIndex": 0,
                "explanation": "Se clicco su 'Iscriviti al corso' e la pagina successiva si intitola 'Pannello di onboarding candidati', subentra un momento di smarrimento: la coerenza lessicale rassicura l'utente."
            },
            {
                "question": "Quale ruolo svolge la casella di ricerca (Search) nel Trunk Test?",
                "options": [
                    "Rappresenta una via di fuga universale: se la pagina su cui sono atterrato non è quella giusta, la barra di ricerca mi permette di tentare subito un nuovo recupero diretto",
                    "Serve unicamente per cercare termini all'interno del dizionario della lingua italiana",
                    "Viene impiegata per registrare nuovi account sul database",
                    "Permette di inviare segnalazioni di bug al team di sviluppo software"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca è la rete di salvataggio dell'utente: se atterro sulla pagina sbagliata e non capisco il menu, una casella ben visibile mi consente di digitare ciò che desidero senza abbandonare il sito."
            }
        ]
    },
    "krug-c8": {
        "quiz": [
            {
                "question": "Cosa intende Steve Krug con la metafora dei 'Contadini e dei Mandriani' (The Farmer and the Cowman Should Be Friends)?",
                "options": [
                    "I team aziendali sprecano ore in riunioni estenuanti litigando su 'cosa piace alla gente', poiché ciascun ruolo (designer, sviluppatore, marketing) proietta le proprie preferenze soggettive sugli utenti",
                    "I programmatori e i contadini condividono gli stessi orari di lavoro all'alba",
                    "L'industria alimentare è stata la prima ad adottare il Responsive Web Design",
                    "I siti web di agricoltura richiedono palette cromatiche basate su toni di marrone e verde"
                ],
                "correctIndex": 0,
                "explanation": "Come nel musical Oklahoma! dove mandriani e contadini litigano su futilità, nei team il grafico vuole l'arte, lo sviluppatore vuole l'efficienza e il marketing vuole popup, dimenticando il vero utente."
            },
            {
                "question": "Perché il concetto di 'utente medio' (average user) è un mito ingannevole e dannoso secondo Krug?",
                "options": [
                    "Perché non esiste un utente medio universale: le persone hanno abilità, motivazioni e contesti diversissimi; progettare per un'entità astratta paralizza le decisioni",
                    "Perché la media matematica richiede calcoli statistici che i designer non sanno fare",
                    "Perché tutti gli utenti web hanno esattamente le medesime abitudini di navigazione",
                    "Perché i sistemi operativi moderni non consentono la profilazione degli utenti"
                ],
                "correctIndex": 0,
                "explanation": "Tutti i membri del team credono che l'utente medio 'sia esattamente come loro'. Cercare l'utente medio porta a compromessi insipidi: bisogna progettare per utenti reali osservati sul campo."
            },
            {
                "question": "Qual è l'unico antidoto efficace per porre fine alle discussioni soggettive all'interno del team di sviluppo?",
                "options": [
                    "I test di usabilità qualitativi con persone reali: osservare gli utenti mentre cercano di usare il prodotto fa crollare istantaneamente le teorie astratte",
                    "Chiedere al dirigente più alto in grado (HiPPO) di decidere secondo il proprio gusto personale",
                    "Fare una votazione democratica a maggioranza tra i membri del team",
                    "Lanciare una moneta per scegliere tra le opzioni concorrenti"
                ],
                "correctIndex": 0,
                "explanation": "Il test con utenti è il grande pacificatore: davanti a un utente reale che non trova il pulsante, le dispute filosofiche evaporano e il team si compatta per risolvere il problema pratico."
            },
            {
                "question": "Cosa accade quando un designer proietta se stesso come modello di utente ideale?",
                "options": [
                    "Cade nella trappola dell'auto-referenzialità: presume che gli utenti notino e apprezzino gli stessi dettagli raffinati che piacciono a lui, ignorando le reali difficoltà dei profani",
                    "Garantisce che il sito web vincerà sicuramente premi internazionali di grafica",
                    "Aumenta la velocità di caricamento del codice sul server",
                    "Elimina automaticamente tutti i problemi di compatibilità mobile"
                ],
                "correctIndex": 0,
                "explanation": "Il designer conosce il software intimamente, ha monitor professionali e vista perfetta: non può simulare spontaneamente lo sguardo ingenuo e disincantato di un utente occasionale."
            },
            {
                "question": "Perché domandare agli utenti in un sondaggio 'Cosa ti piacerebbe avere in questo sito?' produce spesso risposte inaffidabili?",
                "options": [
                    "Perché le persone non sono brave a prevedere i propri comportamenti futuri o a immaginare soluzioni che non hanno mai provato; è molto più affidabile osservare cosa fanno concretamente oggi",
                    "Perché gli utenti mentono deliberatamente per compiacere i ricercatori",
                    "Perché i sondaggi online sono vietati dalle normative sulla privacy europea",
                    "Perché nessuno compila mai questionari composti da più di una domanda"
                ],
                "correctIndex": 0,
                "explanation": "Regola aurea dell'UX Research: prestate attenzione a ciò che gli utenti fanno, non a ciò che dicono. C'è un abisso tra un'opinione astratta e l'azione concreta davanti a uno schermo."
            }
        ],
        "examQuiz": [
            {
                "question": "Durante una riunione, lo sviluppatore capo afferma: 'A me i menu a discesa danno fastidio, quindi dobbiamo eliminarli'. Quale bias cognitivo sta manifestando secondo Krug?",
                "options": [
                    "La falsa equivalenza tra il proprio gusto personale e le necessità dell'intero pubblico di utilizzatori",
                    "L'effetto Dunning-Kruger sulla complessità del codice CSS",
                    "La sindrome dell'impostore applicata alla progettazione grafica",
                    "L'illusione di controllo sui server di produzione"
                ],
                "correctIndex": 0,
                "explanation": "La frase 'A me piace/A me dà fastidio' è la trappola classica: la domanda corretta non è se piaccia al programmatore o al designer, ma se aiuti gli utenti target a raggiungere i loro obiettivi."
            },
            {
                "question": "In che modo l'acronimo 'HiPPO' (Highest Paid Person's Opinion) descrive una grave minaccia per l'usabilità di un progetto?",
                "options": [
                    "Quando le decisioni di interfaccia vengono prese in base al gusto arbitrario del manager più pagato anziché sui dati e sull'osservazione empirica degli utenti",
                    "Un algoritmo per l'ottimizzazione della compressione delle immagini JPEG",
                    "Un protocollo per la crittografia delle transazioni bancarie",
                    "Un framework di programmazione per dispositivi mobili iOS"
                ],
                "correctIndex": 0,
                "explanation": "L'HiPPO è il rischio letale: se il direttore generale decide che il colore del bottone deve essere il suo colore preferito, l'usabilità cede il passo al potere gerarchico interno."
            },
            {
                "question": "Quale atteggiamento professionale deve mantenere il designer quando presenta una scelta di layout al team?",
                "options": [
                    "Motivare la soluzione collegandola a principi di percezione visiva, euristiche consolidate e risultati dei test con utenti, anziché difenderla come mera espressione artistica",
                    "Rifiutarsi di modificare qualsiasi pixel sostenendo la sacralità dell'ispirazione",
                    "Accettare passivamente qualsiasi richiesta del committente senza fornire argomentazioni tecniche",
                    "Minacciare di abbandonare il progetto se non viene approvato il layout proposto"
                ],
                "correctIndex": 0,
                "explanation": "Il professionista non difende il proprio ego ma l'efficacia della soluzione: spiegare il 'perché' funzionale (leggibilità, percorsi di scansione, dati) trasforma lo scontro in dialogo costruttivo."
            }
        ]
    },
    "krug-c9": {
        "quiz": [
            {
                "question": "Qual è la formula del 'Testing di usabilità discount' (fai-da-te) proposta da Steve Krug nel Capitolo 9?",
                "options": [
                    "Testare regolarmente con pochi utenti (3 al mese), in sessioni qualitative brevi, identificando i problemi più gravi e correggendoli subito prima della tornata successiva",
                    "Coinvolgere almeno cinquecento persone in un laboratorio scientifico a specchio unidirezionale con telecamere professionali",
                    "Affidare l'intero processo a una società di consulenza esterna con budget milionario",
                    "Eseguire i test unicamente la settimana successiva al lancio definitivo del sito web"
                ],
                "correctIndex": 0,
                "explanation": "Krug ha rivoluzionato l'industria dimostrando che un test imperfetto svolto su 3 utenti ogni mese è mille volte più utile e realizzabile di un test faraonico rimandato all'infinito."
            },
            {
                "question": "Perché 3 (o massimo 5) utenti sono sufficienti per una sessione di test qualitativo secondo Jakob Nielsen e Steve Krug?",
                "options": [
                    "Perché i primi 3 utenti scoprono quasi tutti i problemi di usabilità macroscopici e più gravi; aggiungere altri partecipanti produce riscontri ridondanti a costi crescenti",
                    "Perché i laboratori di usabilità non dispongono di più di tre sedie fisiche",
                    "Perché le leggi sulla privacy vietano di intervistare più di cinque persone al giorno",
                    "Perché i computer non possono registrare più di tre sessioni video contemporaneamente"
                ],
                "correctIndex": 0,
                "explanation": "La celebre curva di Nielsen/Krug mostra rendimenti decrescenti: i primi 3-4 utenti incontrano gli stessi ostacoli principali. È molto più intelligente correggere subito quei problemi e poi testare di nuovo con altri 3 utenti."
            },
            {
                "question": "In cosa consiste la tecnica cardine del 'Thinking Aloud' (pensare ad alta voce) durante il test?",
                "options": [
                    "Chiedere al partecipante di verbalizzare costantemente ciò che pensa, vede, cerca, si aspetta o non capisce mentre tenta di svolgere i compiti assegnati",
                    "Obbligare l'utente a leggere a voce alta tutti i testi della pagina web per valutarne la dizione",
                    "Registrare i rumori di sottofondo dell'ambiente domestico del tester",
                    "Far recitare all'utente una serie di comandi vocali per attivare l'assistente virtuale"
                ],
                "correctIndex": 0,
                "explanation": "Il Think-Aloud è la finestra nella mente dell'utente: ascoltare i suoi dubbi spontanei svela il 'perché' dei suoi comportamenti, rivelando falle invisibili all'analisi puramente statistica."
            },
            {
                "question": "Quale ruolo deve mantenere il facilitatore (moderatore) durante la conduzione di un test di usabilità?",
                "options": [
                    "Neutrale, empatico e silenzioso: deve incoraggiare l'utente a parlare senza mai suggerire dove cliccare, spiegare il sito o giustificare gli errori del sistema",
                    "Autoritario e severo: deve correggere immediatamente l'utente ogni volta che commette un errore di clic",
                    "Promozionale: deve illustrare i pregi commerciali del prodotto e convincere il partecipante ad acquistarlo",
                    "Passivo: deve abbandonare la stanza lasciando l'utente completamente solo"
                ],
                "correctIndex": 0,
                "explanation": "Il facilitatore non insegna e non guida: osserva. Se l'utente chiede 'Devo cliccare qui?', il facilitatore risponde con una domanda a specchio: 'Cosa ti aspetteresti che succeda se cliccassi lì?'."
            },
            {
                "question": "Cosa deve fare il team subito dopo aver concluso le sessioni di test della mattina?",
                "options": [
                    "Riunirsi per un debriefing (pranzo collegiale) per stilare l'elenco dei 3 problemi più gravi emersi e concordare correzioni minime da implementare subito prima del prossimo test",
                    "Scrivere una relazione accademica di duecento pagine e attendere l'approvazione del consiglio di amministrazione",
                    "Cancellare l'intero progetto e ricominciare da zero con un nuovo framework",
                    "Inviare una diffida legale agli utenti che hanno criticato l'interfaccia"
                ],
                "correctIndex": 0,
                "explanation": "Metodo 'Triage': si stila la lista dei problemi visti, si scelgono i peggiori e si decide la modifica più semplice e immediata per arginarli (spesso togliendo qualcosa o riscrivendo un testo)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un partecipante al test di usabilità esclama: 'Scusatemi, sono proprio negato con la tecnologia!'. Come deve reagire immediatamente il facilitatore?",
                "options": [
                    "Rassicurarlo subito: 'Non si preoccupi affatto, non stiamo testando lei ma il sito web. Se incontra difficoltà, la colpa è esclusivamente di come è disegnato il sistema'",
                    "Confermare l'affermazione per non interrompere il flusso spontaneo dei pensieri",
                    "Interrompere il test ed espellere il partecipante per manifesta incapacità tecnica",
                    "Spiegargli passo dopo passo come funziona il sistema operativo del computer"
                ],
                "correctIndex": 0,
                "explanation": "Regola fondamentale del briefing: rassicurare il tester. Se la persona si sente sotto esame, si chiude o si scusa; chiarire che è il sito a essere sotto processo libera la spontaneità."
            },
            {
                "question": "Qual è la differenza sostanziale tra un 'Focus Group' e un 'Test di Usabilità' secondo Steve Krug?",
                "options": [
                    "Il Focus Group raccoglie opinioni, reazioni emotive e desideri astratti di un gruppo che discute seduto attorno a un tavolo; il Test di Usabilità osserva una singola persona che usa concretamente il software per compiere compiti reali",
                    "Il Focus Group si fa online e il Test di Usabilità si fa solo su carta",
                    "Non sussiste alcuna differenza reale di metodologia",
                    "Il Focus Group è qualitativo mentre il Test di Usabilità è solo quantitativo"
                ],
                "correctIndex": 0,
                "explanation": "Errore madornale scambiare i due metodi: un Focus Group è una chiacchierata di marketing per sondare idee; un Test di usabilità è una prova sul campo per vedere se l'interfaccia funziona."
            },
            {
                "question": "Perché quando si corregge un problema di usabilità emerso da un test bisogna preferire 'la modifica minima efficace' (tweak) anziché ridisegnare l'intera sezione?",
                "options": [
                    "Perché i grandi stravolgimenti richiedono tempo, costano molto e rischiano di introdurre nuovi problemi imprevisti, mentre piccoli aggiustamenti mirati risolvono l'intoppo all'istante",
                    "Perché i browser non consentono di modificare più di dieci righe di codice a settimana",
                    "Perché i programmatori rifiutano di lavorare su sezioni già completate",
                    "Perché le normative europee vietano i cambiamenti strutturali dopo la fase beta"
                ],
                "correctIndex": 0,
                "explanation": "Krug consiglia il pragmatismo chirurgico: spesso basta togliere un'istruzione fuorviante, cambiare una parola o aggiungere una sottolineatura per risolvere il 90% del problema senza rifare tutto."
            }
        ]
    },
    "krug-c10": {
        "quiz": [
            {
                "question": "Qual è la principale sfida di usabilità introdotta dai dispositivi mobili (smartphone e tablet)?",
                "options": [
                    "La drastica riduzione dello spazio visivo a schermo disponibile, unita all'uso del tocco (dita imprecise) e a contesti d'uso caratterizzati da distrazione e mobilità",
                    "L'assenza di connessione internet ad alta velocità",
                    "L'obbligo di utilizzare caratteri tipografici in bianco e nero",
                    "L'impossibilità di elaborare immagini vettoriali SVG"
                ],
                "correctIndex": 0,
                "explanation": "Su mobile lo schermo è minuscolo, le dita coprono i contenuti (fat finger) e l'utente cammina per strada sotto la luce del sole: ogni singolo pixel e ogni tocco contano enormemente."
            },
            {
                "question": "Perché nascondere l'intera navigazione dietro un'icona 'Hamburger' può comportare un costo di usabilità significativo?",
                "options": [
                    "Perché 'Lontano dagli occhi, lontano dal cuore': ciò che non è visibile a schermo viene ignorato o dimenticato, riducendo l'esplorazione dei contenuti secondari",
                    "Perché l'icona dell'hamburger richiede troppa memoria RAM per essere disegnata",
                    "Perché gli utenti vegetariani rifiutano di toccare icone con riferimenti alla carne",
                    "Perché i sistemi operativi mobili non supportano i menu a scorrimento laterale"
                ],
                "correctIndex": 0,
                "explanation": "Sebbene salvi spazio, il menu hamburger occulta l'offerta: se le sezioni primarie non sono visibili (es. in una barra inferiore a tab), l'utente presume che il sito non le offra."
            },
            {
                "question": "Quale grave effetto collaterale ha prodotto l'avvento del 'Flat Design' esasperato sulle interfacce mobili?",
                "options": [
                    "L'eliminazione di ombre, bordi e rilievi ha reso indistinguibili gli elementi cliccabili dal testo statico, costringendo gli utenti a toccare a caso per esplorare la schermata",
                    "L'aumento vertiginoso del consumo della batteria dello smartphone",
                    "L'obbligo di utilizzare solo schermi con risoluzione 4K",
                    "La scomparsa definitiva delle fotografie a colori dalle pagine web"
                ],
                "correctIndex": 0,
                "explanation": "Il Flat Design radicale ha sacrificato l'affordance sull'altare dell'estetica minimalista: togliendo ogni indizio tridimensionale, l'utente non sa più cosa sia un pulsante e cosa sia una semplice etichetta."
            },
            {
                "question": "Cosa si intende per 'Area del Pollice' (Thumb Zone) nell'ergonomia delle interfacce smartphone?",
                "options": [
                    "L'area inferiore dello schermo che il pollice dell'utente può raggiungere comodamente con una sola mano senza dover compiere contorsioni o cambiare impugnatura",
                    "Lo spazio occupato dall'impronta digitale sul lettore biometrico",
                    "Una sezione del menu riservata ai giochi per ragazzi",
                    "Il margine di sicurezza applicato ai lati dei testi tipografici"
                ],
                "correctIndex": 0,
                "explanation": "Formulata da Steven Hoober, la Thumb Zone dimostra che i controlli primari (navigazione, azioni chiave) devono stare in basso dove il pollice arriva con naturalezza, non in cima allo schermo."
            },
            {
                "question": "Qual è la dimensione minima raccomandata per un bersaglio tattile (Touch Target) per evitare tocchi accidentali con il polpastrello?",
                "options": [
                    "Almeno 44x44 (o 48x48) pixel/punti CSS, con adeguato spazio di rispetto attorno all'elemento",
                    "Esattamente 10x10 pixel",
                    "Almeno 200x200 pixel per qualsiasi link",
                    "Un millimetro quadrato indipendentemente dalla risoluzione"
                ],
                "correctIndex": 0,
                "explanation": "Le linee guida di Apple e Google impongono circa 44-48px: le dita umane non sono puntatori mouse millimetrici, e pulsanti troppo piccoli o troppo vicini provocano tocchi errati e rabbia."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'applicazione mobile presenta link di testo fitti fitti e a distanza di 4 pixel l'uno dall'altro. Un utente tenta di cliccare su 'Termini di servizio' e apre inavvertitamente 'Elimina account'. Quale legge ergonomica è stata violata?",
                "options": [
                    "Le dimensioni minime dei touch target e le distanze di sicurezza tra bersagli tattili",
                    "La legge di conservazione della massa applicata ai dispositivi digitali",
                    "La normativa sulla crittografia dei dati personali",
                    "La compatibilità retroattiva con i dispositivi dotati di penna stilo"
                ],
                "correctIndex": 0,
                "explanation": "La precisione delle dita è limitata dal polpastrello (circa 9-10mm di larghezza fisica): se i link sono incollati, il tocco cattura il bersaglio vicino anziché quello desiderato."
            },
            {
                "question": "Perché l'interazione basata sul passaggio del mouse (:hover) è un concetto inapplicabile come requisito esclusivo su dispositivi touch?",
                "options": [
                    "Perché sui display tattili non esiste lo stato hover continuo: toccare lo schermo corrisponde direttamente a un'azione di clic (click/tap)",
                    "Perché i telefoni cellulari non supportano i fogli di stile CSS3",
                    "Perché i touch screen riconoscono solo il passaggio di oggetti metallici",
                    "Perché il browser mobile disabilita automaticamente tutte le animazioni di transizione"
                ],
                "correctIndex": 0,
                "explanation": "Su mobile non si può 'sorvolare' un elemento senza toccarlo: se un'interfaccia nasconde informazioni critiche o menu secondari sotto lo stato :hover, su smartphone risulterà inaccessibile."
            },
            {
                "question": "Quale compromesso virtuoso adotta una 'Bottom Navigation Bar' (barra di navigazione inferiore) rispetto al menu Hamburger su schermi mobili?",
                "options": [
                    "Mantiene costantemente visibili le 3-5 destinazioni primarie all'interno della comoda Thumb Zone, facilitando il passaggio immediato tra sezioni senza dover aprire alcun pannello",
                    "Occupa l'intero schermo impedendo la visualizzazione dei contenuti",
                    "Permette di riprodurre video musicali in streaming continuo",
                    "Sostituisce completamente la necessità di disporre di una homepage"
                ],
                "correctIndex": 0,
                "explanation": "La barra inferiore combina visibilità persistente ed ergonomia del pollice: l'utente vede sempre dove può andare e ci arriva con un solo tocco senza compiere acrobazie con la mano."
            }
        ]
    },
    "krug-c11": {
        "quiz": [
            {
                "question": "Qual è il punto di vista di Steve Krug sull'Accessibilità (Accessibility)?",
                "options": [
                    "Non è un onere burocratico né un compito punitivo per designer, ma un atto di cortesia umana fondamentale e la cosa giusta da fare affinché nessuno sia escluso",
                    "Un insieme di regole superflue che distruggono l'estetica moderna del sito",
                    "Un requisito riservato unicamente ai siti delle pubbliche amministrazioni statali",
                    "Una tecnologia destinata a essere sostituita dai visori di realtà virtuale"
                ],
                "correctIndex": 0,
                "explanation": "Krug invita all'empatia: rendere un sito accessibile non significa renderlo brutto, ma assicurarsi che chi naviga con disabilità visive, motorie o uditive possa fruirne senza barriere."
            },
            {
                "question": "Come naviga una persona non vedente all'interno di una pagina web?",
                "options": [
                    "Utilizzando uno Screen Reader (software di lettura a schermo) che converte il testo in sintesi vocale o su barra Braille, muovendosi da tastiera tra intestazioni, landmark e link",
                    "Facendosi leggere lo schermo da un operatore telefonico umano in tempo reale",
                    "Utilizzando monitor a raggi ultravioletti ad altissimo contrasto",
                    "Memorizzando il codice sorgente HTML prima dell'apertura del browser"
                ],
                "correctIndex": 0,
                "explanation": "Lo screen reader analizza il DOM HTML e legge ad alta voce i testi: una persona esperta ascolta a velocità impressionante, saltando da un titolo (H1, H2) all'altro per trovare l'informazione."
            },
            {
                "question": "Qual è la funzione essenziale dell'attributo 'alt' nei tag delle immagini <img> per l'accessibilità?",
                "options": [
                    "Fornire una descrizione testuale equivalente dell'immagine, che viene letta dallo screen reader quando la persona non può vedere la figura",
                    "Mostrare una scritta pubblicitaria a pagamento sopra la fotografia",
                    "Aumentare la velocità di scaricamento del file grafico dal server",
                    "Modificare la palette dei colori dell'immagine in tempo reale"
                ],
                "correctIndex": 0,
                "explanation": "Senza alt text, l'utente cieco sente leggere 'IMG_4829.jpg' o viene ignorato il senso della figura. Un alt chiaro ('Grafico a barre dell'inflazione') rende il contenuto accessibile a tutti."
            },
            {
                "question": "Cosa accade quando un'immagine ha funzione puramente decorativa (es. un arabesco di separazione o una texture)?",
                "options": [
                    "Si deve inserire un attributo alt vuoto (alt=''), segnalando allo screen reader di ignorare l'immagine e non disturbare la lettura con rumore inutile",
                    "Bisogna rimuovere completamente il tag img dal codice HTML",
                    "È obbligatorio scrivere 'Questa è una decorazione senza importanza'",
                    "Si deve collegare l'immagine a una pagina di spiegazione esterna"
                ],
                "correctIndex": 0,
                "explanation": "Un alt='' (vuoto) è fondamentale: comunica al software di sintesi di saltare la decorazione senza annunciarla, preservando la fluidità di lettura del testo circostante."
            },
            {
                "question": "Perché una buona struttura gerarchica delle intestazioni (H1, H2, H3) è la prima misura di accessibilità?",
                "options": [
                    "Perché permette agli utenti che usano lettori di schermo di scansionare la pagina saltando direttamente al capitolo d'interesse con la tastiera, esattamente come chi vede con gli occhi",
                    "Perché obbliga il browser a utilizzare caratteri tipografici con grazie",
                    "Perché impedisce ai bot automatici di scaricare i testi del sito",
                    "Perché riduce le dimensioni dei file memorizzati nel database"
                ],
                "correctIndex": 0,
                "explanation": "La gerarchia dei titoli è l'equivalente della scansione visiva: premendo il tasto 'H' da tastiera, chi non vede ascolta solo l'indice dei titoli e decide dove fermarsi ad approfondire."
            }
        ],
        "examQuiz": [
            {
                "question": "Un designer progetta un sito web in cui tutti i link cambiano stato unicamente al passaggio del mouse (:hover), senza alcuna gestione per lo stato :focus da tastiera. Chi risulterà gravemente discriminato?",
                "options": [
                    "Gli utenti con disabilità motorie che non possono usare il mouse e navigano esclusivamente tramite tastiera o puntatori a controllo oculare",
                    "I visitatori che utilizzano monitor widescreen da ufficio",
                    "Gli utenti registrati con indirizzo email aziendale",
                    "I programmatori che lavorano su sistemi operativi Linux"
                ],
                "correctIndex": 0,
                "explanation": "Chi usa il tasto 'Tab' per muoversi ha bisogno di vedere l'anello di focus (:focus-visible): se il contorno viene rimosso con 'outline: none' senza sostituto, l'utente naviga alla cieca."
            },
            {
                "question": "In un video formativo pubblicato sul sito web mancano sia i sottotitoli che la trascrizione testuale. Quale principio delle linee guida WCAG risulta violato?",
                "options": [
                    "Il principio 'Percepibile': le persone sorde o ipoudenti (e chi naviga in ambienti rumorosi o senza cuffie) sono impossibilitate ad accedere al contenuto informativo",
                    "Il principio di sovranità digitale del consumatore",
                    "La conformità con il protocollo di streaming video WebRTC",
                    "L'interoperabilità dei metadati Dublin Core"
                ],
                "correctIndex": 0,
                "explanation": "Il contenuto deve essere fruibile attraverso canali sensoriali multipli: l'audio deve avere testo equivalente (sottotitoli/trascrizione) per chi non può o non desidera ascoltare."
            },
            {
                "question": "Quale vantaggio insospettabile produce l'applicazione rigorosa dell'accessibilità anche per gli utenti normovedenti e senza disabilità?",
                "options": [
                    "Migliora l'usabilità complessiva per tutti, favorisce la SEO sui motori di ricerca, rende il sito più chiaro su schermi mobili sotto la luce del sole e accelera la navigazione",
                    "Aumenta la frequenza di aggiornamento della scheda grafica",
                    "Consente di disattivare l'uso dei certificati di sicurezza SSL",
                    "Elimina automaticamente tutti gli errori nel codice JavaScript"
                ],
                "correctIndex": 0,
                "explanation": "L'effetto 'marciapiede inclinato' (Curb Cut Effect): lo scivolo progettato per le sedie a rotelle aiuta genitori con passeggini e viaggiatori con valigie. L'accessibilità fa bene a chiunque navighi."
            }
        ]
    },
    "krug-c12": {
        "quiz": [
            {
                "question": "Cosa rappresenta la celebre metafora del 'Serbatoio della Buona Volontà' (Reservoir of Goodwill) ideata da Steve Krug?",
                "options": [
                    "La quantità finita di pazienza, benevolenza ed energia positiva che ogni utente porta con sé all'inizio della sessione di navigazione",
                    "Il saldo economico residuo sulla carta prepagata dell'utente",
                    "La capacità massima di archiviazione dei cookie nel browser",
                    "Il volume di dati scaricabili prima del rallentamento della connessione"
                ],
                "correctIndex": 0,
                "explanation": "Ogni utente entra nel sito con un serbatoio pieno a metà o a tre quarti: ogni intoppo, popup invadente o form punitivo svuota il serbatoio; quando il serbatoio è a secco, l'utente scappa."
            },
            {
                "question": "Quali elementi o pratiche di design SVUOTANO rapidamente il serbatoio della buona volontà dell'utente?",
                "options": [
                    "Nascondere informazioni basilari (come i costi di spedizione o il numero di telefono), formattazioni rigide dei campi (es. vietare spazi nei numeri), popup aggressivi e richieste premature di dati personali",
                    "Fornire risposte chiare alle domande frequenti e rendere evidenti i prezzi",
                    "Consentire all'utente di stampare la pagina in un formato pulito e leggibile",
                    "Mostrare breadcrumbs ordinate e titoli di pagina espliciti"
                ],
                "correctIndex": 0,
                "explanation": "Nulla fa arrabbiare quanto le barriere inutili: dover rifare un form perché il sito rifiuta i trattini nel CAP o non trovare i prezzi prima della registrazione prosciuga la pazienza."
            },
            {
                "question": "Quali pratiche di design RIEMPIONO o ricaricano il serbatoio della buona volontà?",
                "options": [
                    "Rendere trasparenti i costi fin dall'inizio, facilitare il recupero degli errori, risparmiare clic all'utente, fornire anteprime chiare e offrire un'esperienza impeccabile",
                    "Obbligare l'utente a guardare un video promozionale di due minuti prima dell'acquisto",
                    "Nascondere il menu di navigazione per forzare la scansione della homepage",
                    "Inviare tre email di notifica al minuto durante la compilazione del carrello"
                ],
                "correctIndex": 0,
                "explanation": "La trasparenza genera fiducia: quando un sito aiuta con garbo l'utente a risolvere un problema, scusandosi per gli errori propri senza dare la colpa al visitatore, il serbatoio si ricarica."
            },
            {
                "question": "Perché il livello iniziale del serbatoio della buona volontà varia da persona a persona?",
                "options": [
                    "Perché dipende dal contesto emotivo del visitatore, dall'urgenza del compito, dalla fiducia pregressa nel marchio e da eventuali frustrazioni vissute prima di aprire il sito",
                    "Perché viene calcolato automaticamente dalla scheda madre del computer",
                    "Perché dipende dal sistema operativo installato sullo smartphone",
                    "Perché è determinato dalla velocità in megabit della connessione a internet"
                ],
                "correctIndex": 0,
                "explanation": "Un utente che ha fretta o che ha appena litigato con un altro sito parte con un serbatoio quasi vuoto: basta un solo ostacolo insignificante per farlo esplodere e indurlo alla chiusura."
            },
            {
                "question": "Qual è la conseguenza estrema dell'esaurimento completo del serbatoio della buona volontà?",
                "options": [
                    "L'abbandono immediato del sito web, con passaggio diretto alla concorrenza e un senso duraturo di discredito verso l'azienda",
                    "Il blocco automatico del processore del computer",
                    "La disconnessione della linea telefonica domestica",
                    "La perdita di tutti i file salvati nella cartella documenti"
                ],
                "correctIndex": 0,
                "explanation": "Quando il serbatoio è vuoto non c'è appello: l'utente chiude la finestra con rabbia e difficilmente tornerà, preferendo rivolgersi a un concorrente anche più costoso ma più agevole."
            }
        ],
        "examQuiz": [
            {
                "question": "Un utente inserisce il proprio numero di carta di credito includendo gli spazi tra le cifre. Il form ricarica la pagina in rosso segnalando: 'Errore: solo cifre consentite!'. Come commenterebbe Steve Krug?",
                "options": [
                    "Un gravissimo svuotamento del serbatoio: il computer dovrebbe fare il lavoro sporco (rimuovere gli spazi con una riga di codice) anziché rimproverare l'utente per un gesto naturale",
                    "Una procedura corretta per educare gli utenti alla disciplina informatica",
                    "Un requisito obbligatorio imposto dai circuiti bancari internazionali",
                    "Un comportamento irrilevante che non produce alcun impatto sulla soddisfazione"
                ],
                "correctIndex": 0,
                "explanation": "Fate fare il lavoro al computer! Far riscrivere un numero perché l'utente ha inserito uno spazio è pura pigrizia dello sviluppatore e un insulto alla buona volontà del visitatore."
            },
            {
                "question": "Un portale immobiliare richiede la registrazione obbligatoria con email e password prima ancora di mostrare le fotografie e i prezzi delle case. Qual è la reazione tipica della maggior parte degli utenti?",
                "options": [
                    "Chiudono la scheda e cercano un altro portale che consenta di consultare le offerte liberamente, sentendo la richiesta come un'intrusione predatoria",
                    "Compilano entusiasti la registrazione condividendo tutti i propri dati",
                    "Telefonano all'agenzia immobiliare per complimentarsi della scelta",
                    "Installano un nuovo browser per verificare se l'ostacolo scompare"
                ],
                "correctIndex": 0,
                "explanation": "Non chiedete prima di dare valore: forzare la registrazione prematura genera diffidenza. Lasciate che l'utente si innamori del servizio, poi chiedete i dati quando servono davvero."
            },
            {
                "question": "Come si formula un messaggio di errore ideale per non intaccare il serbatoio della buona volontà?",
                "options": [
                    "Con un linguaggio chiaro, umano e garbato, che spiega esattamente quale sia il problema, dove si trovi e cosa fare concretamente per risolverlo, assumendosi la responsabilità",
                    "Con un codice alfanumerico crittografato come 'Error 0x004F8B' senza spiegazioni",
                    "Accusando l'utente di aver violato le condizioni di licenza del software",
                    "Chiudendo l'applicazione senza mostrare alcun avviso"
                ],
                "correctIndex": 0,
                "explanation": "I messaggi di errore devono essere costruttivi: niente 'Input non valido!', ma 'Ops, sembra che manchi la chiocciola nell'indirizzo email. Controlla e riprova'."
            }
        ]
    },
    "krug-c13": {
        "quiz": [
            {
                "question": "Quale consiglio strategico offre Steve Krug ai designer per difendere l'usabilità di fronte a manager scettici o committenti autoritari?",
                "options": [
                    "Invitarli a osservare dal vivo una sessione di test con un utente reale: nulla è più convincente della realtà empirica per sciogliere le resistenze aziendali",
                    "Scrivere lettere anonime di protesta agli azionisti dell'impresa",
                    "Applicare le modifiche di nascosto durante la notte senza avvisare nessuno",
                    "Accettare passivamente qualsiasi richiesta anche se peggiora palesemente il servizio"
                ],
                "correctIndex": 0,
                "explanation": "Portate i manager in sala di test: vedere con i propri occhi un potenziale cliente che non riesce a comprare fa scattare l'allarme di business molto più di cento slide teoriche."
            },
            {
                "question": "Cosa si intende per 'Guerre di religione' (Religious Wars) all'interno dei team di sviluppo software?",
                "options": [
                    "Dispute sterili e infinite basate su credenze soggettive e gusti estetici inconciliabili anziché su prove oggettive e verifiche sul campo",
                    "Conflitti confessionali tra colleghi di religioni diverse",
                    "Attacchi informatici condotti da gruppi estremisti contro i server web",
                    "La concorrenza economica tra società che producono sistemi operativi"
                ],
                "correctIndex": 0,
                "explanation": "Le guerre di religione aziendali ('I menu devono essere a sinistra!' 'No, in alto!') non hanno soluzione logica: si risolvono solo uscendo dalla stanza e guardando gli utenti alle prese col sistema."
            },
            {
                "question": "Perché quando si corregge un problema di interfaccia bisogna resistere alla tentazione di aggiungere 'un'altra istruzione'?",
                "options": [
                    "Perché se gli utenti non leggono le istruzioni esistenti, aggiungere altro testo aumenterà solo il rumore visivo senza risolvere la radice strutturale dell'intoppo",
                    "Perché i motori di ricerca penalizzano i siti che aggiungono più di tre parole al mese",
                    "Perché i database non possono memorizzare nuovi paragrafi",
                    "Perché il consorzio W3C vieta la pubblicazione di testi di aiuto"
                ],
                "correctIndex": 0,
                "explanation": "L'istinto errato è: 'Gli utenti sbagliano qui, mettiamo un avviso!'. Ma l'avviso verrà ignorato come tutto il resto. Bisogna sistemare il comando, non spiegare come aggirarne il difetto."
            },
            {
                "question": "Cosa contraddistingue un vero professionista dell'usabilità nel rapporto con i colleghi del team?",
                "options": [
                    "L'umiltà, il pragmatismo, la capacità di ascolto e l'attitudine a trovare compromessi funzionali intelligenti senza arroccarsi su dogmi teorici astratti",
                    "L'intransigenza assoluta e il rifiuto di parlare con gli ingegneri del software",
                    "L'uso esclusivo di termini tecnici in lingua inglese per intimidire i committenti",
                    "La pretesa di prendere qualsiasi decisione finale senza consultare gli altri reparti"
                ],
                "correctIndex": 0,
                "explanation": "L'usabilità è diplomazia applicata: un buon UX designer collabora con programmatori e marketing per trovare soluzioni realistiche che migliorino la vita degli utenti nei vincoli dati."
            },
            {
                "question": "Quale riflessione conclusiva lascia Steve Krug ai lettori di 'Don't Make Me Think'?",
                "options": [
                    "Il buon senso è la risorsa più preziosa del design: trattate i vostri utenti con rispetto, chiarezza e trasparenza, e il successo del progetto seguirà di conseguenza",
                    "La tecnologia del web è troppo complicata per essere compresa dalle persone comuni",
                    "L'usabilità diventerà superflua con l'avvento dei microprocessori a controllo mentale",
                    "Solo chi possiede una laurea in ingegneria aerospaziale può progettare siti web"
                ],
                "correctIndex": 0,
                "explanation": "La chiusa del libro è un manifesto etico: rispettare il tempo, l'attenzione e l'intelligenza delle persone che usano i nostri prodotti è il segreto autentico di ogni grande design."
            }
        ],
        "examQuiz": [
            {
                "question": "Un committente insiste per inserire un carosello di immagini rotanti automatiche gigante in cima alla homepage. Come può il designer dimostrare l'inefficacia della soluzione secondo le euristiche di usabilità?",
                "options": [
                    "Mostrando studi e test empirici che documentano la 'Banner Blindness' e il fatto che gli utenti ignorano i caroselli o non cliccano mai oltre la prima slide",
                    "Scollegando il server di sviluppo dalla rete elettrica",
                    "Sostenendo che il consorzio W3C ha vietato l'uso dei caroselli nei paesi europei",
                    "Affermando che i caroselli possono essere visti solo con monitor a tubo catodico"
                ],
                "correctIndex": 0,
                "explanation": "I dati battono le opinioni: mostrare i test (come le ricerche di Nielsen e dell'Università di Notre Dame, dove l'1% clicca sul carosello e l'89% solo sulla prima slide) convince anche i più testardi."
            },
            {
                "question": "Quando durante un test di usabilità emerge che TUTTI i partecipanti hanno avuto successo nello svolgere un compito, cosa deve concludere il team?",
                "options": [
                    "Che quella specifica funzionalità o flusso è solida e comprensibile, e si possono concentrare gli sforzi di revisione sulle altre aree problematiche del sito",
                    "Che il test era truccato e va rifatto da capo con utenti diversi",
                    "Che il compito era troppo banale e va reso più complicato per metterli alla prova",
                    "Che lo sviluppo del prodotto è definitivamente concluso"
                ],
                "correctIndex": 0,
                "explanation": "I successi nei test sono importanti quanto i fallimenti: confermano ciò che funziona, permettendo di non toccare ciò che è sano e di canalizzare l'energia dove serve davvero."
            },
            {
                "question": "Qual è il test definitivo per capire se avete applicato con successo i principi di Steve Krug a un vostro progetto web?",
                "options": [
                    "Se un amico o parente estraneo al progetto riesce a navigare, trovare informazioni e compiere azioni chiave senza mai chiedervi 'E adesso cosa devo fare?'",
                    "Se il file CSS supera le diecimila righe di codice sorgente",
                    "Se il sito web vince un trofeo in un concorso di grafica pubblicitaria",
                    "Se il costo complessivo di sviluppo ha superato il budget iniziale del cliente"
                ],
                "correctIndex": 0,
                "explanation": "La prova provata: se chiunque, senza istruzioni né spiegazioni, naviga senza esitare ed esclama 'Che comodità!', avete centrato il cuore di 'Don't Make Me Think'."
            }
        ]
    }
}

krug_quiz_data.update(krug_c3_to_13)

# Load existing krug-data.js
with open("data/krug-data.js", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"window\.KRUG_DATA\s*=\s*(\[.*\]);?", content, re.DOTALL)
if not m:
    raise Exception("Could not find window.KRUG_DATA in data/krug-data.js")

data = json.loads(m.group(1))

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
    if cid in krug_quiz_data:
        quizzes = krug_quiz_data[cid]["quiz"]
        exam_quizzes = krug_quiz_data[cid]["examQuiz"]
        
        # Balance quiz across 0, 1, 2, 3 rotato per capitolo
        for idx, q in enumerate(quizzes):
            balance_question(q, (idx + c_idx) % 4)
            
        # Balance examQuiz rotato per capitolo
        for idx, eq in enumerate(exam_quizzes):
            balance_question(eq, (idx + c_idx + 1) % 4)
            
        chap["quiz"] = quizzes
        chap["examQuiz"] = exam_quizzes
        print(f"Updated {cid}: {len(chap['quiz'])} quiz, {len(chap['examQuiz'])} examQuiz")

with open("data/krug-data.js", "w", encoding="utf-8") as f:
    f.write(f"// Don't Make Me Think (Steve Krug) - Dataset strutturato per studio e test\nwindow.KRUG_DATA = {json.dumps(data, indent=2, ensure_ascii=False)};\n")

print("Successfully rebuilt data/krug-data.js with high academic rigor and balanced options!")
