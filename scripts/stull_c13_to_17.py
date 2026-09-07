# -*- coding: utf-8 -*-
"""
High-level academic quiz and exam questions for Stull UX Design - Chapters 13 to 17.
13: Interviste agli utenti
14: Osservazione contestuale (Shadowing)
15: Sondaggi e survey (Scale Likert, bias)
16: Personas e Proto-Personas
17: Mappe dell'empatia (Says, Thinks, Does, Feels)
"""

import json

stull_c13_to_17 = {
    "stull-c13": {
        "quiz": [
            {
                "question": "Quale tipologia di formulazione delle domande deve essere rigorosamente privilegiata durante un'intervista qualitativa con un utente?",
                "options": [
                    "Domande aperte, neutre ed esplorative ('Raccontami dell'ultima volta che...', 'Cosa hai provato quando...?') che invitano alla narrazione libera",
                    "Domande chiuse con risposta secca sì/no che confermano la bontà del prodotto",
                    "Domande trabocchetto con opzioni multiple per testare la velocità di riflessione dell'utente",
                    "Domande ipotetiche sul futuro ('Compreresti questa funzione se costasse 10 euro?')"
                ],
                "correctIndex": 0,
                "explanation": "Le domande aperte favoriscono l'emersione di storie ed episodi autentici. Le domande chiuse o ipotetiche portano a risposte di compiacimento totalmente inaffidabili."
            },
            {
                "question": "Cosa si intende per 'Domanda Guidata' (Leading Question) e perché è considerata un gravissimo errore metodologico nell'intervista UX?",
                "options": [
                    "Una domanda formulata in modo tale da suggerire o influenzare implicitamente la risposta desiderata dal ricercatore (es. 'Non trovi che questa grafica sia splendida?')",
                    "Una domanda rivolta a un gruppo di turisti guidati all'interno di un museo",
                    "Una domanda formulata tramite l'uso di diagrammi di flusso visivi",
                    "Una domanda posta unicamente al direttore generale dell'azienda committente"
                ],
                "correctIndex": 0,
                "explanation": "Le leading questions inquinano i dati alla radice: l'intervistato tende inconsciamente a compiacere il ricercatore, confermando le sue speranze anziché dire la scomoda verità."
            },
            {
                "question": "In cosa consiste la regola del 'Silenzio Attivo' (o Pausa d'Imbarazzo) praticata dai bravi intervistatori UX?",
                "options": [
                    "Tacere per alcuni secondi dopo che l'utente sembra aver concluso la risposta: il silenzio spinge spontaneamente l'intervistato a elaborare, svelando spesso gli insight più sinceri e profondi",
                    "Disattivare il microfono durante la registrazione per risparmiare memoria",
                    "Ignorare le domande poste dall'utente per tutta la durata della sessione",
                    "Obbligare l'utente a rispondere unicamente attraverso gesti delle mani"
                ],
                "correctIndex": 0,
                "explanation": "Il silenzio crea spazio cognitivo: l'essere umano tende a riempire il vuoto. Trattenendo la voglia di fare la domanda successiva, si lascia emergere il retroscena inatteso."
            },
            {
                "question": "Perché chiedere all'utente 'Cosa vorresti che facesse questo software in futuro?' produce risposte poco utili?",
                "options": [
                    "Perché le persone sono pessime nel predire i propri comportamenti futuri o inventare buone soluzioni tecniche; è molto più efficace farsi raccontare i problemi reali che vivono oggi",
                    "Perché gli utenti non hanno il diritto di avanzare proposte prima del lancio",
                    "Perché le normative sui brevetti vietano di accogliere idee dai clienti",
                    "Perché il futuro non può essere rappresentato all'interno di una matrice di Kano"
                ],
                "correctIndex": 0,
                "explanation": "Celebre massima attribuita a Henry Ford: 'Se avessi chiesto alla gente cosa voleva, mi avrebbero risposto cavalli più veloci'. Il designer deve scoprire il bisogno sottostante, non chiedere la soluzione."
            },
            {
                "question": "Quale atteggiamento deve mantenere il ricercatore nei confronti delle opinioni inattese o critiche espresse dall'intervistato?",
                "options": [
                    "Curiosità radicale, sospensione del giudizio e accoglienza del feedback negativo come oro colato per migliorare il prodotto",
                    "Difendere con veemenza le scelte dell'azienda spiegando perché l'utente si sbaglia",
                    "Interrompere immediatamente l'intervista per manifesta ostilità dell'utente",
                    "Riformulare la domanda finché l'utente non ritratta la critica espressa"
                ],
                "correctIndex": 0,
                "explanation": "La critica dura è il dono più prezioso: ogni difetto scovato durante un'intervista privata è un disastro evitato sul mercato aperto dopo il lancio."
            }
        ],
        "examQuiz": [
            {
                "question": "Durante un'intervista, un utente dice: 'Questo portale è fantastico, lo userei tutti i giorni!'. Come deve trattare questa affermazione un ricercatore esperto?",
                "options": [
                    "Con scetticismo benevolo (Bias di cortesia/desiderabilità sociale): chiedere subito esempi concreti di comportamenti passati anziché fidarsi di entusiasmi verbali astratti",
                    "Riportarla immediatamente come prova del successo assoluto del progetto agli azionisti",
                    "Chiedere all'utente di firmare un assegno bancario per confermare l'affermazione",
                    "Registrare l'audio e utilizzarlo come jingle pubblicitario per la televisione"
                ],
                "correctIndex": 0,
                "explanation": "Il Mom Test di Rob Fitzpatrick: le lodi future sono gratuite. Chiedete 'Come hai risolto questo problema nelle ultime due settimane?': se non ha speso tempo o denaro, il bisogno non è reale."
            },
            {
                "question": "Qual è il numero ottimale di partecipanti per una serie di interviste qualitative in profondità prima di raggiungere la 'Saturazione dei Dati'?",
                "options": [
                    "Tra 8 e 12 partecipanti per segmento omogeneo: oltre questa soglia i pattern ricorrenti tendono a ripetersi senza apportare nuovi insight sostanziali",
                    "Almeno cinquecento persone per soddisfare i requisiti della distribuzione gaussiana",
                    "Due persone appartenenti alla stessa famiglia per garantire la coerenza",
                    "Cento persone per ogni singola funzionalità presente nell'applicazione"
                ],
                "correctIndex": 0,
                "explanation": "La saturazione qualitativa: dopo 8-10 interviste ben condotte, iniziate a sentire le stesse storie e le stesse frustrazioni. Aggiungere altre 30 persone aumenta i costi senza aggiungere novità."
            },
            {
                "question": "Cosa si intende per 'Protocollo d'Intervista' (Interview Guide) e quale grado di flessibilità deve possedere?",
                "options": [
                    "Una scaletta tematica semi-strutturata con argomenti e spunti da esplorare, che il ricercatore deve poter adattare con flessibilità seguendo le deviazioni impreviste dell'utente",
                    "Un copione rigido di cinquanta domande da leggere testualmente senza cambiare una parola",
                    "Un contratto legale vincolante che impedisce all'utente di abbandonare la stanza",
                    "Un elenco di risposte predefinite da far selezionare a crocette su un modulo cartaceo"
                ],
                "correctIndex": 0,
                "explanation": "L'intervista non è un interrogatorio di polizia: la guida è una bussola, non un binario rigido. Se l'utente tocca un tema inatteso e fecondo, il bravo intervistatore lo segue a fondo."
            }
        ]
    },
    "stull-c14": {
        "quiz": [
            {
                "question": "Cosa contraddistingue l' 'Osservazione Contestuale' (Contextual Inquiry) rispetto a un'intervista svolta in sala riunioni?",
                "options": [
                    "L'osservazione diretta dell'utente nel suo reale ambiente operativo quotidiano (ufficio, magazzino, casa, cantiere) mentre svolge le sue attività ordinarie senza filtri artificiali",
                    "La sorveglianza segreta tramite telecamere nascoste a insaputa del soggetto",
                    "Un'intervista condotta unicamente tramite messaggi vocali su smartphone",
                    "Un incontro formale in tribunale con la presenza di periti legali"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca contestuale porta il designer sul campo: vedere l'utente che combatte con post-it attaccati allo schermo, telefoni che squillano e interruzioni svela la realtà che nessuna intervista a tavolino può descrivere."
            },
            {
                "question": "In cosa consiste la tecnica di ricerca sul campo nota come 'Shadowing' (pedinamento discreto)?",
                "options": [
                    "Il ricercatore segue l'utente come un'ombra durante la sua giornata o durante un task complesso, registrando azioni, pause, imprevisti e workaround senza intervenire né giudicare",
                    "La proiezione di ombre cinesi durante le riunioni di brainstorming",
                    "L'oscuramento delle finestre del laboratorio di usabilità per evitare riflessi",
                    "L'eliminazione dei nomi dei dipendenti dai database aziendali"
                ],
                "correctIndex": 0,
                "explanation": "Nello shadowing il ricercatore osserva l'esperienza 'nel suo habitat naturale': vede dove l'utente si blocca, quali scorciatoie usa e quali strumenti paralleli adotta per sopravvivere."
            },
            {
                "question": "Cosa sono i 'Workaround' (espedienti o soluzioni di ripiego) adottati spontaneamente dagli utenti?",
                "options": [
                    "Scorciatoie ingegnose (come post-it con codici, fogli Excel paralleli, trucchi di tastiera) create dagli utenti per aggirare le lacune e le rigidità del software aziendale",
                    "Errori irreversibili di sistema che richiedono la formattazione del computer",
                    "Funzionalità avanzate introdotte dagli sviluppatori per gli utenti premium",
                    "Aggiornamenti automatici di sicurezza scaricati durante la notte"
                ],
                "correctIndex": 0,
                "explanation": "I workaround sono pepite d'oro per la UX: ogni volta che vedete un post-it attaccato al monitor con un appunto, avete trovato una grave falla del sistema che attende di essere risolta dal design."
            },
            {
                "question": "Quale modello relazionale è raccomandato per l'osservazione contestuale secondo Karen Holtzblatt (Maestro-Apprendista)?",
                "options": [
                    "Il ricercatore si pone come un umile apprendista che osserva il maestro artigiano (l'utente esperto nel suo mestiere), chiedendo spiegazioni sulle azioni compiute senza superiorità tecnica",
                    "Il ricercatore agisce come un professore severo che corregge gli errori del discente",
                    "L'utente e il ricercatore fingono di non conoscersi per tutta la durata della prova",
                    "Il ricercatore impartisce ordini su come compiere il lavoro nel minor tempo possibile"
                ],
                "correctIndex": 0,
                "explanation": "Il modello Master-Apprentice rovescia la gerarchia: l'utente è il vero esperto del proprio lavoro quotidiano; il designer è l'allievo curioso che impara come le cose vengono fatte sul serio."
            },
            {
                "question": "Perché ciò che le persone FANNO sul campo è spesso radicalmente diverso da ciò che DICHIARANO nelle interviste a tavolino?",
                "options": [
                    "Perché la memoria umana è fallace, molte azioni quotidiane sono automatismi inconsci (Sistema 1) e le persone tendono a razionalizzare o idealizzare i propri comportamenti a posteriori",
                    "Perché gli intervistati mentono deliberatamente per ingannare i ricercatori",
                    "Perché i dipendenti temono di essere licenziati se dicono la verità nelle interviste",
                    "Perché le interviste a tavolino vengono condotte unicamente sotto ipnosi"
                ],
                "correctIndex": 0,
                "explanation": "Non per malafede, ma per dimenticanza: nessuno si ricorda di aver cliccato tre volte 'Aggiorna' o di aver cercato una fattura su WhatsApp. Sul campo, l'occhio del ricercatore coglie la verità nuda."
            }
        ],
        "examQuiz": [
            {
                "question": "Durante una sessione di osservazione in un pronto soccorso ospedaliero, il ricercatore nota che le infermiere non inseriscono i dati nel tablet all'istante, ma li annotano velocemente sul guanto di lattice a penna, ricopiandoli a fine turno. Quale insight di design emerge?",
                "options": [
                    "L'interfaccia del tablet è troppo lenta, rigida o richiede troppi passaggi per i ritmi frenetici delle emergenze, costringendo il personale a un workaround estremo e rischioso",
                    "Le infermiere devono essere punite per aver violato le linee guida di igiene",
                    "Il materiale dei guanti di lattice deve essere sostituito con tessuto sintetico",
                    "L'ospedale deve vendere i tablet e ripristinare i registri cartacei del secolo scorso"
                ],
                "correctIndex": 0,
                "explanation": "Un classico trionfo della Contextual Inquiry: in sala riunioni l'ospedale diceva 'Tutti usano il tablet al letto del paziente'; sul campo scoprite che il tablet è inutilizzabile nelle emergenze. Il design deve diventare rapidissimo (Voice o 1-tap)."
            },
            {
                "question": "Cos'è l' 'Effetto Hawthorne' nell'osservazione contestuale e come si mitiga?",
                "options": [
                    "La tendenza delle persone a modificare temporaneamente il proprio comportamento ordinario sapendo di essere osservate; si mitiga prolungando l'osservazione finché l'utente non si abitua e torna naturale",
                    "Il surriscaldamento dei dispositivi mobili sotto la luce diretta dei riflettori",
                    "La cancellazione automatica dei file di log dopo otto ore di registrazione",
                    "L'ansia provocata dalla presenza di dirigenti aziendali all'interno della stanza"
                ],
                "correctIndex": 0,
                "explanation": "Nei primi 20 minuti tutti recitano la parte del 'lavoratore perfetto'. Dopo un'ora, l'effetto Hawthorne sfuma, subentra la stanchezza e riemergono i comportamenti e i vizi reali del quotidiano."
            },
            {
                "question": "Quale precauzione etica e legale è imprescindibile prima di intraprendere una sessione di shadowing contestuale in azienda?",
                "options": [
                    "Ottenere il consenso informato firmato (Consensus & Privacy), tutelare i dati sensibili dei clienti/pazienti terzi e garantire la totale riservatezza delle registrazioni e degli appunti",
                    "Pagare una commissione in contanti al sindacato di categoria",
                    "Firmare una delega che consenta al ricercatore di sostituire il lavoratore in caso di assenza",
                    "Richiedere un'autorizzazione scritta al ministero delle telecomunicazioni"
                ],
                "correctIndex": 0,
                "explanation": "L'etica è sacra: osservare le persone al lavoro tocca privacy, segreti industriali e dati personali. Il consenso informato, l'anonimizzazione dei dati e il rispetto della dignità umana sono prerequisiti inderogabili."
            }
        ]
    },
    "stull-c15": {
        "quiz": [
            {
                "question": "Qual è il principale punto di forza e il principale limite dell'utilizzo dei 'Sondaggi' (Survey) nella ricerca UX?",
                "options": [
                    "Punto di forza: raccogliere dati quantitativi su campioni amplissimi a costi ridotti; Limite: non possono spiegare il 'perché' profondo dei comportamenti e risentono fortemente di bias di formulazione",
                    "Punto di forza: consentono di osservare le espressioni facciali; Limite: costano milioni di euro",
                    "Punto di forza: sono legalmente vincolanti; Limite: funzionano solo senza connessione internet",
                    "Punto di forza: sostituiscono completamente lo sviluppo software; Limite: richiedono troppo tempo"
                ],
                "correctIndex": 0,
                "explanation": "I sondaggi scalano benissimo (10.000 risposte in un clic), ma sono superfici piatte: se formulate una domanda male o chiusa, raccoglierete dati privi di reale valore diagnostico."
            },
            {
                "question": "Cosa caratterizza una 'Scala Likert' standard all'interno di un questionario di soddisfazione o usabilità?",
                "options": [
                    "Una scala graduata di accordo/disaccordo (tipicamente a 5 o 7 punti, da 'Fortemente in disaccordo' a 'Fortemente d'accordo') con un punto neutro centrale equilibrato",
                    "Un campo di testo libero in cui l'utente può scrivere poesie o aforismi",
                    "Un interruttore binario on/off privo di gradazioni intermedie",
                    "Una scala cromatica basata sulle frequenze della luce visibile"
                ],
                "correctIndex": 0,
                "explanation": "La scala Likert (Rensis Likert, 1932) è lo standard psicometrico: permette di misurare l'intensità di un'opinione o di un atteggiamento in modo matematicamente comparabile."
            },
            {
                "question": "Cosa si intende per 'Bias di Formulazione' (Framing / Question Bias) nella redazione di un sondaggio?",
                "options": [
                    "L'errore metodologico di comporre domande che contengono già una connotazione positiva o negativa, orientando inconsapevolmente la risposta del partecipante",
                    "L'utilizzo di caratteri tipografici con un contrasto cromatico insufficiente",
                    "La mancata traduzione del questionario in lingua latina",
                    "L'invio del sondaggio a utenti privi di account sui social media"
                ],
                "correctIndex": 0,
                "explanation": "Chiedere 'Quanto è stata eccezionale la tua esperienza?' distorce il dato. La formulazione neutra corretta è: 'Valuta la tua esperienza complessiva da 1 (Pessima) a 5 (Eccellente)'."
            },
            {
                "question": "Cos'è il 'Bias di Non Risposta' (Non-Response Bias) nei sondaggi online?",
                "options": [
                    "Il fenomeno per cui chi sceglie di compilare spontaneamente il sondaggio ha spesso motivazioni estreme (molto arrabbiato o entusiasta), escludendo la visione moderata della maggioranza",
                    "Il malfunzionamento del server di posta elettronica che blocca l'invio dei messaggi",
                    "Il rifiuto dei motori di ricerca di indicizzare i form di registrazione",
                    "L'errore di battitura commesso dall'utente nel campo indirizzo email"
                ],
                "correctIndex": 0,
                "explanation": "Se su 10.000 utenti rispondono in 100 (1%), quel campione non è rappresentativo: include solo chi aveva tempo da perdere o un conto in sospeso con l'azienda."
            },
            {
                "question": "Quale regola d'oro governa la lunghezza di un sondaggio per massimizzare il tasso di completamento (Completion Rate)?",
                "options": [
                    "Mantenere il sondaggio brevissimo (massimo 3-5 minuti di compilazione, non più di 10-12 domande essenziali), comunicando in anticipo il tempo stimato",
                    "Inserire almeno cento domande dettagliate per sfruttare l'attenzione dell'utente",
                    "Nascondere il numero delle domande residue per evitare che l'utente desista",
                    "Rendere obbligatoria la compilazione di tutte le risposte aperte"
                ],
                "correctIndex": 0,
                "explanation": "L'abbandono dei sondaggi cresce esponenzialmente dopo il quarto minuto. Domande brevi, chiare, una barra di avanzamento e rispetto del tempo dell'utente sono le chiavi del successo."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda chiede nel sondaggio: 'Quanto ritieni utile e veloce la nostra applicazione?'. Quale gravissimo errore metodologico è presente in questa domanda?",
                "options": [
                    "È una domanda 'a doppio binario' (Double-Barreled Question): unisce due concetti distinti (utilità e velocità) in un'unica risposta, rendendo impossibile capire a cosa si riferisca il voto dell'utente",
                    "La domanda è troppo corta e priva di termini tecnici del settore",
                    "L'applicazione non può essere valutata senza il parere di un perito legale",
                    "I software bancari vietano l'uso della parola 'veloce' nei questionari"
                ],
                "correctIndex": 0,
                "explanation": "L'app potrebbe essere utilissima ma lentissima: se l'utente vota '2 stelle', si riferisce alla lentezza o all'inutilità? Mai unire due attributi nella stessa domanda."
            },
            {
                "question": "Perché un ricercatore dovrebbe inserire almeno una domanda aperta al termine di un questionario a risposte chiuse ('C'è qualcos'altro che vorresti dirci?')?",
                "options": [
                    "Per raccogliere 'l'ignoto ignoto' (Unknown Unknowns): problemi, aneddoti o bisogni imprevisti che il team di ricerca non aveva nemmeno immaginato di inserire nelle opzioni chiuse",
                    "Per verificare se l'utente è in grado di digitare sulla tastiera senza errori",
                    "Per aumentare artificialmente la lunghezza del documento finale",
                    "Per rispettare le linee guida del consorzio W3C sui moduli web"
                ],
                "correctIndex": 0,
                "explanation": "La casella aperta finale spesso regala le intuizioni più dirompenti: 'Il sito è bello, ma non accetta la carta aziendale e devo pagare di tasca mia'. Quello è l'insight che vale l'intero sondaggio."
            },
            {
                "question": "Come si formula una scala di opzioni per una domanda a scelta singola per garantire la validità scientifica del dato?",
                "options": [
                    "Le opzioni devono essere mutualmente esclusive (senza sovrapposizioni tra fasce) e collettivamente esaustive (coprire tutti i casi possibili, eventualmente con la voce 'Altro')",
                    "Le opzioni devono contenere parole in rima per facilitare la memorizzazione",
                    "Le risposte devono essere ordinate dalla più lunga alla più corta",
                    "Le opzioni devono essere visualizzate una alla volta a intervalli di cinque secondi"
                ],
                "correctIndex": 0,
                "explanation": "Se le fasce sono '20-30 anni' e '30-40 anni', chi ha 30 anni dove clicca? (Non mutualmente esclusive). Le opzioni devono essere impeccabili: '20-29', '30-39', '40-49'."
            }
        ]
    },
    "stull-c16": {
        "quiz": [
            {
                "question": "Cosa sono le 'Personas' (o Buyer/User Personas) ideate dal pioniere dell'interazione Alan Cooper nel 1999?",
                "options": [
                    "Modelli archetipici di utenti ideali o rappresentativi, sintetizzati rigorosamente a partire da dati reali emersi dalla ricerca, che incarnano obiettivi, comportamenti, frustrazioni e modelli mentali tipici",
                    "Attori teatrali stipendiati dall'azienda per recitare davanti ai programmatori",
                    "Profili fasulli generati da bot per gonfiare il numero dei follower sui social media",
                    "La maschera grafica utilizzata nei videogiochi per nascondere il volto del giocatore"
                ],
                "correctIndex": 0,
                "explanation": "Alan Cooper ('The Inmates Are Running the Asylum') inventò le Personas per dare un volto e un nome ai dati: smettere di parlare dell'astratto 'utente' e iniziare a progettare per 'Marco, 42 anni, che ha poco tempo'."
            },
            {
                "question": "Qual è la differenza sostanziale tra una 'Persona basata sui dati' (Data-driven Persona) e una 'Proto-Persona'?",
                "options": [
                    "La Data-driven Persona scaturisce da interviste e ricerche sul campo approfondite; la Proto-Persona è una bozza preliminare basata sulle supposizioni e credenze interne degli stakeholder, da validare in seguito",
                    "La Proto-Persona viene utilizzata solo nei prototipi cartacei e l'altra nel codice",
                    "La Proto-Persona riguarda solo i consumatori adolescenti",
                    "Non sussiste alcuna differenza, essendo sinonimi commerciali"
                ],
                "correctIndex": 0,
                "explanation": "La Proto-Persona è un ottimo punto di partenza per far emergere i pregiudizi del team interno; ma se non viene poi verificata e corretta sul campo con la ricerca reale, resta una mera allucinazione aziendale."
            },
            {
                "question": "Quale elemento NON deve costituire il cuore di una buona User Persona nella progettazione di prodotto?",
                "options": [
                    "Dettagli anagrafici arbitrari e irrilevanti (es. la marca preferita di cereali a colazione o il segno zodiacale) che non hanno alcuna influenza sul compito che l'utente deve svolgere",
                    "Gli obiettivi concreti (Goals) che la persona vuole raggiungere usando il servizio",
                    "Le frustrazioni e i dolori (Pain Points) che vive attualmente con le soluzioni esistenti",
                    "Il contesto ambientale e tecnologico in cui la persona si trova a interagire"
                ],
                "correctIndex": 0,
                "explanation": "Attenzione alle 'Personas spazzatura': riempirle di dati da rotocalco ('ama i gatti e ascolta jazz') non aiuta a decidere come strutturare un form bancario. Servono obiettivi, ostacoli e modelli mentali."
            },
            {
                "question": "A cosa serve assegnare un nome fittizio, una citazione e una fotografia a una User Persona?",
                "options": [
                    "A favorire l'empatia e la memoria collettiva del team: è molto più facile discutere chiedendosi 'Questo flusso funzionerà per Elena?' anziché dibattere sull'astratto 'target secondario'",
                    "A proteggere legalmente l'azienda da accuse di plagio industriale",
                    "A permettere agli algoritmi di machine learning di compilare i dati",
                    "A soddisfare i requisiti del consorzio W3C sui metadati delle immagini"
                ],
                "correctIndex": 0,
                "explanation": "Umanizzare i dati: 'Elena' diventa un membro silenzioso delle riunioni di design. Se il manager propone una funzione contorta, il designer può ribattere: 'Elena lavora in cantiere con i guanti, non riuscirebbe mai a usarla'."
            },
            {
                "question": "Quante Personas primarie è consigliabile definire per un singolo prodotto digitale per evitare la dispersione progettuale?",
                "options": [
                    "Da 1 a massimo 3 Personas primarie (con una chiaramente prioritaria su tutte), per mantenere un focus di progettazione affilato ed evitare il 'design per tutti'",
                    "Almeno quaranta per rappresentare qualsiasi persona sul pianeta terra",
                    "Zero: le personas sono considerate superflue nella metodologia Agile moderna",
                    "Esattamente una per ogni dipendente dell'ufficio commerciale"
                ],
                "correctIndex": 0,
                "explanation": "Chi progetta per tutti non progetta per nessuno: avere 20 personas equivale a non averne nessuna. Focalizzarsi sulla Persona primaria garantisce coerenza; le secondarie non devono danneggiare la primaria."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team di marketing crea 6 Personas basandosi esclusivamente su fasce di reddito, genere ed età (es. 'Donne 25-34 anni con reddito medio'). Perché questo approccio è inadeguato per la progettazione UX?",
                "options": [
                    "Perché i dati demografici non spiegano i comportamenti d'uso né gli obiettivi: il principe Carlo d'Inghilterra e il rocker Ozzy Osbourne hanno la stessa età, genere e reddito, ma stili di vita e modelli mentali opposti",
                    "Perché i dati demografici sono illegali secondo la legge europea sul GDPR",
                    "Perché il marketing non ha il permesso di collaborare con i programmatori",
                    "Perché le fasce di reddito non possono essere rappresentate in grafici a torta"
                ],
                "correctIndex": 0,
                "explanation": "La celebre analogia di Ozzy Osbourne e Re Carlo: demograficamente identici, ma non useranno mai un'app nello stesso modo. La UX progetta sui comportamenti, sui problemi e sugli scopi, non sul censimento anagrafico."
            },
            {
                "question": "Cosa si intende per 'Elastic User' (Utente Elastico) secondo Alan Cooper, e in che modo le Personas lo combattono?",
                "options": [
                    "La tendenza del team a 'tirare' le caratteristiche dell'utente ideale a seconda dell'argomento della discussione; la Persona fissa confini rigidi e precisi ponendo fine alle ambiguità",
                    "Un utente che naviga contemporaneamente da dieci dispositivi diversi",
                    "La capacità del cervello umano di adattarsi a qualsiasi tipo di schermo",
                    "Un cliente che cambia frequentemente idea sui prodotti da acquistare"
                ],
                "correctIndex": 0,
                "explanation": "Se il termine è 'utente', il programmatore immagina un programmatore, il grafico immagina un artista e il marketing immagina un compratore compulsivo. La Persona blocca l'elasticità: l'utente ha un volto, compiti e limiti definiti."
            },
            {
                "question": "In quale momento del ciclo di vita del prodotto una User Persona deve essere aggiornata o revisionata?",
                "options": [
                    "Quando nuove ricerche sul campo, cambiamenti di mercato o metriche analitiche mostrano che i comportamenti reali degli utenti sono mutati rispetto alle ipotesi iniziali",
                    "Ogni lunedì mattina prima dell'inizio delle attività lavorative",
                    "Soltanto quando l'azienda cambia amministratore delegato",
                    "Mai: una persona creata rimane immutabile per sempre"
                ],
                "correctIndex": 0,
                "explanation": "Le Personas sono artefatti vivi: non sono statue di marmo. Man mano che il prodotto matura e si raccolgono nuovi dati, il modello archetipico si raffina e si aggiorna per rispecchiare la realtà."
            }
        ]
    },
    "stull-c17": {
        "quiz": [
            {
                "question": "Cosa rappresenta una 'Mappa dell'Empatia' (Empathy Map) ideata da Dave Gray (XPLANE)?",
                "options": [
                    "Uno strumento visivo collaborativo a 4 quadranti che sintetizza ciò che l'utente Dice (Says), Pensa (Thinks), Fa (Does) e Sente (Feels), evidenziandone frustrazioni (Pains) e bisogni (Gains)",
                    "Una mappa geografica che mostra la posizione satellitare dei server web",
                    "Un diagramma che calcola il salario orario medio dei dipendenti aziendali",
                    "Una tabella di compatibilità tra i diversi browser internet"
                ],
                "correctIndex": 0,
                "explanation": "L'Empathy Map è un ponte formidabile: permette al team di calarsi nella sfera sensoriale ed emotiva dell'utente partendo dalle osservazioni sul campo per allineare l'intero gruppo di lavoro."
            },
            {
                "question": "Quale cruciale discrepanza consente di evidenziare il confronto tra il quadrante 'Dice' (Says) e il quadrante 'Pensa' (Thinks) in un'Empathy Map?",
                "options": [
                    "La discrepanza tra le affermazioni esteriori di facciata (spesso condizionate dalla cortesia) e i pensieri intimi, le paure o i dubbi non verbalizzati ad alta voce",
                    "L'errore di traduzione tra la lingua italiana e quella inglese",
                    "La differenza di volume vocale misurata in decibel sonori",
                    "La velocità con cui il cervello trasmette gli impulsi nervosi alle dita"
                ],
                "correctIndex": 0,
                "explanation": "In 'Dice' scriviamo: 'Il prezzo sembra onesto'; in 'Pensa' annotiamo: 'Ho paura che ci siano costi nascosti che mi addebiteranno dopo'. Questa frizione interiore guida le scelte di trasparenza del design."
            },
            {
                "question": "Cosa si registra nel quadrante 'Fa' (Does) di una Mappa dell'Empatia?",
                "options": [
                    "Le azioni fisiche e i comportamenti concreti osservati direttamente durante la ricerca (es. passa da un'app all'altra, apre una calcolatrice esterna, si stropiccia gli occhi, chiede aiuto al collega)",
                    "I comandi vocali registrati dall'assistente virtuale",
                    "Le righe di codice eseguite dal microprocessore dello smartphone",
                    "I bonifici bancari effettuati dall'amministrazione aziendale"
                ],
                "correctIndex": 0,
                "explanation": "'Does' è pura osservazione oggettiva non filtrata: cosa fa concretamente la persona con le mani, con gli occhi, con gli oggetti circostanti mentre cerca di raggiungere il suo scopo."
            },
            {
                "question": "Cosa rappresentano le sezioni inferiori 'Pains' (Dolori/Ostacoli) e 'Gains' (Vantaggi/Bisogni) nell'Empathy Map Canvas aggiornato?",
                "options": [
                    "I 'Pains' sono paure, frustrazioni, ostacoli e rischi temuti; i 'Gains' sono desideri, aspettative di successo, speranze e parametri di misurazione del proprio traguardo",
                    "I guadagni monetari e le perdite fiscali dell'impresa committente",
                    "Il peso in chilogrammi dell'hardware e il costo di spedizione postale",
                    "La memoria consumata e la velocità della scheda grafica del computer"
                ],
                "correctIndex": 0,
                "explanation": "Pains e Gains sono la benzina del valore: la nostra soluzione digitale ha successo se rimuove i dolori (allevia i Pains) e facilita il raggiungimento degli obiettivi desiderati (moltiplica i Gains)."
            },
            {
                "question": "In quale fase del workshop di design viene tipicamente utilizzata la Mappa dell'Empatia?",
                "options": [
                    "Subito dopo la fase di ricerca sul campo e prima dell'ideazione delle soluzioni, per consentire a designer, sviluppatori e product manager di sintetizzare e condividere l'empatia verso gli utenti",
                    "Al momento del rilascio finale del software sugli app store",
                    "Durante la firma del contratto di fornitura commerciale",
                    "Nella compilazione dei registri di presenza del personale"
                ],
                "correctIndex": 0,
                "explanation": "L'Empathy Map è l'attività di sintesi ideale: svuota le note di ricerca su post-it colorati, stimola discussioni appassionate e crea allineamento empatico totale prima di iniziare a disegnare wireframe."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team compila un'Empathy Map riempiendola di post-it basati unicamente su congetture interne senza aver parlato con un solo utente reale. Qual è il valore metodologico di questo manufatto?",
                "options": [
                    "Rappresenta solo una mappa delle supposizioni e dei bias interni del team, utile per identificare le proprie convinzioni ma pericolosa se non viene validata e corretta con la ricerca sul campo",
                    "È perfettamente equivalente a una mappa basata su ricerche empiriche da 100.000 euro",
                    "È illegale secondo le normative dell'Unione Europea sull'innovazione industriale",
                    "Permette di eliminare del tutto la fase di sviluppo del software"
                ],
                "correctIndex": 0,
                "explanation": "L'empatia non si inventa alla macchinetta del caffè: fare un'Empathy Map basata sulla fantasia significa mappare le proprie allucinazioni. Serve ricerca sul campo per riempirla di vita autentica."
            },
            {
                "question": "Nel quadrante 'Sente' (Feels), quale tipologia di vissuto emotivo deve essere catturata per arricchire il design?",
                "options": [
                    "Gli stati d'animo sottostanti che governano l'esperienza: ansia da prestazione, insicurezza, entusiasmo, sollievo, frustrazione o noia provati durante l'interazione",
                    "La temperatura della pelle misurata con un termometro laser",
                    "Il battito cardiaco al minuto registrato durante una corsa campestre",
                    "La pressione atmosferica all'interno dell'ufficio del ricercatore"
                ],
                "correctIndex": 0,
                "explanation": "La dimensione emozionale è decisiva: se un utente 'si sente in colpa' o 'si sente sopraffatto dall'ansia di fare un errore finanziario', il tono dell'interfaccia deve diventare rassicurante e accogliente."
            },
            {
                "question": "Come si traduce un 'Pain' identificato nell'Empathy Map (es. 'Paura di non sapere dove andranno a finire i miei dati personali') in una decisione di User Interface?",
                "options": [
                    "Inserendo un microcopy trasparente e rassicurante sotto il campo di inserimento (es. 'Non condivideremo mai i tuoi dati né invieremo spam') con un'icona a forma di lucchetto",
                    "Nascondendo del tutto la richiesta dei dati per poi prelevarli di nascosto",
                    "Aumentando il prezzo di vendita del servizio per trasmettere prestigio",
                    "Rendendo obbligatoria l'accettazione di cinquanta pagine di condizioni legali"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il filo diretto tra empatia e design esecutivo: ogni dolore mappato diventa un requisito di progetto. Conoscere la paura dell'utente permette di disinnescarla con precisione chirurgica nell'UI."
            }
        ]
    }
}

with open("scripts/stull_part4.json", "w", encoding="utf-8") as f:
    json.dump(stull_c13_to_17, f, indent=2, ensure_ascii=False)

print(f"Salvata tranche capitoli 13-17 ({len(stull_c13_to_17)} capitoli)")
