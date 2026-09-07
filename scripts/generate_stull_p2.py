# -*- coding: utf-8 -*-
"""
High-level academic quiz and exam questions for Stull UX Design - Part 2 (Chapters 11 to 20).
"""

import json

stull_c11_to_20 = {
    "stull-c11": {
        "quiz": [
            {
                "question": "Qual è la distinzione metodologica fondamentale tra 'Ricerca Primaria' e 'Ricerca Secondaria' nella UX Research?",
                "options": [
                    "La ricerca primaria raccoglie dati originali di prima mano direttamente dagli utenti sul campo; la ricerca secondaria (desk research) analizza sintesi, report, benchmark e letteratura già esistenti",
                    "La ricerca primaria riguarda solo le persone maggiorenni e la secondaria i minori",
                    "La ricerca primaria si svolge esclusivamente all'interno di uffici governativi",
                    "La ricerca secondaria non può utilizzare fonti reperite su internet"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca secondaria sintetizza ciò che il mondo già conosce; la ricerca primaria scende sul campo per colmare i vuoti specifici del nostro prodotto attraverso l'indagine diretta con gli utenti."
            },
            {
                "question": "Perché un buon ricercatore UX dovrebbe iniziare sempre da una solida 'Ricerca Secondaria' (Desk Research)?",
                "options": [
                    "Per evitare di 'reinventare la ruota', risparmiare budget prezioso, mappare i pattern consolidati e formulare ipotesi di ricerca primaria molto più mirate e consapevoli",
                    "Perché la ricerca secondaria è l'unica legalmente valida per i contratti commerciali",
                    "Perché parlare con gli utenti finali è considerato superfluo se esistono già libri di testo",
                    "Per consentire agli sviluppatori di terminare il software prima della fase di design"
                ],
                "correctIndex": 0,
                "explanation": "Iniziare dalla desk research evita di sprecare ore chiedendo agli utenti cose già note a livello di settore, permettendo di focalizzare le interviste primarie sui reali dilemmi non risolti."
            },
            {
                "question": "Quale rischio insidioso si corre affidandosi ESCLUSIVAMENTE alla ricerca secondaria senza fare ricerca primaria?",
                "options": [
                    "I dati secondari possono essere obsoleti, basati su contesti culturali o demografici differenti e incapaci di cogliere le peculiarità uniche del vostro target specifico",
                    "I motori di ricerca bloccano l'accesso alle fonti bibliografiche",
                    "Le ricerche secondarie contengono sempre virus informatici",
                    "Si rischia una sanzione amministrativa per mancata intervista agli utenti"
                ],
                "correctIndex": 0,
                "explanation": "I report di settore parlano di medie astratte e mercati generali. Ciò che funziona per l'e-commerce in America nel 2018 potrebbe rivelarsi fallimentare per i vostri utenti in Italia oggi."
            },
            {
                "question": "Cosa si intende per 'Triangolazione dei Dati' nella ricerca applicata all'esperienza utente?",
                "options": [
                    "L'uso combinato di fonti e metodologie differenti (es. ricerca secondaria + interviste qualitative + analytics quantitativi) per convalidare un insight incrociando prospettive diverse",
                    "Il calcolo della posizione geografica dell'utente tramite tre celle telefoniche",
                    "L'impaginazione dei report su layout grafici triangolari",
                    "La suddivisione del budget di ricerca in tre parti uguali tra i dirigenti"
                ],
                "correctIndex": 0,
                "explanation": "La triangolazione conferisce rigore scientifico: se l'analytics dice COSA accade, l'intervista spiega PERCHÉ accade e la letteratura conferma il fenomeno, la decisione di design è solidissima."
            },
            {
                "question": "Quali delle seguenti fonti costituiscono un classico esempio di 'Ricerca Secondaria'?",
                "options": [
                    "Report di istituti di ricerca (Gartner, Nielsen Norman Group), articoli accademici, analisi di concorrenti, recensioni sugli app store e dati censuari ISTAT",
                    "Una sessione di shadowing dal vivo a casa di un utente",
                    "Un'intervista approfondita semi-strutturata condotta dal ricercatore",
                    "Un test di usabilità moderato in laboratorio con registrazione eye-tracking"
                ],
                "correctIndex": 0,
                "explanation": "Tutto ciò che è stato raccolto, elaborato o pubblicato da terzi prima del nostro intervento costituisce materiale prezioso di desk research secondaria."
            }
        ],
        "examQuiz": [
            {
                "question": "Un committente afferma: 'Non serve spendere soldi per intervistare gli utenti; abbiamo comprato un report di McKinsey sul mercato dell'automotive da 5.000 euro'. Come argomenta il ricercatore UX la necessità della ricerca primaria?",
                "options": [
                    "Il report di mercato fotografa tendenze macroeconomiche generali, ma non può svelare le difficoltà concrete di interazione, i punti di attrito e i modelli mentali degli utenti che useranno la specifica app del brand",
                    "I report di McKinsey sono notoriamente privi di qualsiasi fondamento scientifico",
                    "La ricerca primaria costa molto meno rispetto all'acquisto di un report",
                    "La legge impone di intervistare almeno cento persone fisiche per ogni brevetto software"
                ],
                "correctIndex": 0,
                "explanation": "I dati macro non aiutano a decidere come etichettare un pulsante o come snellire un flusso: il report dice quanti compreranno auto elettriche, la ricerca primaria rivela perché non riescono a prenotare la ricarica dall'app."
            },
            {
                "question": "Quale problema metodologico sorge quando si utilizzano recensioni pubbliche dell'App Store come unica fonte di ricerca secondaria?",
                "options": [
                    "Il bias di polarizzazione: le recensioni spontanee riflettono quasi esclusivamente gli utenti estremamente entusiasti o, molto più spesso, quelli furiosi per un bug, ignorando la maggioranza silenziosa",
                    "Le recensioni online sono scritte tutte da bot automatici programmati",
                    "Gli app store cancellano tutte le recensioni negative ogni quarantotto ore",
                    "I dati delle recensioni non possono essere esportati in formato tabellare"
                ],
                "correctIndex": 0,
                "explanation": "La polarizzazione spontanea esclude la fascia media: chi usa l'app normalmente e incontra piccoli attriti quotidiani raramente scrive una recensione a 1 stella, tenendosi la frustrazione per sé."
            },
            {
                "question": "In quale fase del processo di Design Thinking (Double Diamond) la ricerca secondaria esprime il suo massimo valore strategico?",
                "options": [
                    "Nella prima fase di Scoperta (Discover), per inquadrare il territorio, definire i trend, individuare i vuoti di conoscenza e formulare le domande corrette per la ricerca sul campo",
                    "Nella fase finale di consegna del codice agli sviluppatori",
                    "Durante il collaudo dei server di staging",
                    "Nel momento in cui si decide il prezzo delle azioni societarie in borsa"
                ],
                "correctIndex": 0,
                "explanation": "All'inizio del diamante divergente: la desk research apre il panorama, fissa lo stato dell'arte e impedisce al team di perdersi o fare indagini alla cieca su problemi già ampiamente risolti."
            }
        ]
    },
    "stull-c12": {
        "quiz": [
            {
                "question": "Qual è la differenza epistemologica fondamentale tra 'Ricerca Quantitativa' e 'Ricerca Qualitativa'?",
                "options": [
                    "La ricerca quantitativa misura 'Quanto?' e 'Cosa succede?' su larga scala numerica; la ricerca qualitativa indaga 'Perché?' e 'Come?' esplorando motivazioni, significati, emozioni e contesti profondi",
                    "La quantitativa si fa con il computer e la qualitativa con carta e penna",
                    "La quantitativa è gratuita e la qualitativa richiede costosi abbonamenti software",
                    "La qualitativa viene svolta unicamente da psicologi laureati con master clinico"
                ],
                "correctIndex": 0,
                "explanation": "La formula aurea: i dati quantitativi tracciano i sintomi (es. l'80% abbandona al terzo step); i dati qualitativi diagnosticano la malattia (l'utente spiega che il campo codice fiscale sembrava una richiesta di pagamento)."
            },
            {
                "question": "Quale delle seguenti metodologie appartiene tipicamente all'ambito della ricerca QUALITATIVA?",
                "options": [
                    "Interviste individuali in profondità, osservazione contestuale e test di usabilità con metodo think-aloud",
                    "A/B testing con un milione di visitatori sul carrello",
                    "Analisi statistica delle frequenze di rimbalzo su Google Analytics",
                    "Tracciamento aggregato dei log del server web"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca qualitativa va in profondità su campioni piccoli: cerca la ricchezza del dettaglio, la sfumatura espressiva e la causa prima del comportamento umano."
            },
            {
                "question": "Quale delle seguenti metodologie appartiene invece all'ambito della ricerca QUANTITATIVA?",
                "options": [
                    "A/B testing, web analytics su grandi volumi, survey con scale Likert validate e calcolo del System Usability Scale (SUS)",
                    "Focus group esplorativo aperto con brainstorming guidato",
                    "Diari di bordo compilati liberamente da tre utenti",
                    "Interviste narrative informali davanti a un caffè"
                ],
                "correctIndex": 0,
                "explanation": "Il mondo quantitativo lavora su numeri, distribuzioni, medie e significatività statistica: permette di generalizzare tendenze su popolazioni ampie riducendo il margine d'errore."
            },
            {
                "question": "Perché un grafico di Google Analytics da solo non può spiegare il motivo per cui gli utenti non completano un acquisto?",
                "options": [
                    "Perché l'analytics registra il comportamento esteriore oggettivo (il drop-off), ma è cieco rispetto ai pensieri, ai dubbi, ai fraintendimenti o alle paure che hanno bloccato la persona",
                    "Perché Google Analytics è vietato dalle normative di tutela dei consumatori",
                    "Perché i dati analitici vengono aggiornati una sola volta all'anno",
                    "Perché l'analytics traccia solo le visite provenienti da computer desktop"
                ],
                "correctIndex": 0,
                "explanation": "I numeri dicono DOVE la nave affonda, non PERCHÉ c'è la falla. Solo parlando con chi era a bordo si scopre che il pulsante sembrava disabilitato o che la voce di costo finale sembrava ingannevole."
            },
            {
                "question": "Cosa si intende per approccio a 'Metodi Misti' (Mixed Methods) nella ricerca UX matura?",
                "options": [
                    "L'integrazione ciclica di qualitativo e quantitativo: usare il qualitativo per scoprire problemi e bisogni profondi, e il quantitativo per validarne la scala e misurare l'impatto delle soluzioni",
                    "Mescolare programmatori e designer nello stesso ufficio open space",
                    "Eseguire ricerche sia in lingua italiana che in lingua inglese contemporaneamente",
                    "Utilizzare software proprietari insieme a librerie open source"
                ],
                "correctIndex": 0,
                "explanation": "Il connubio vincente: il qualitativo genera ipotesi e comprensione umana; il quantitativo misura la frequenza del fenomeno e certifica se la soluzione implementata funziona su larga scala."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team nota attraverso l'analytics che la pagina 'Prezzi' ha un tasso di abbandono dell'85%. Il manager propone di fare 10 varianti grafiche alla cieca per fare A/B test. Quale approccio metodologico più efficiente suggerisce la UX?",
                "options": [
                    "Condurre subito 5 test di usabilità qualitativi per ascoltare cosa confonde o spaventa gli utenti su quella pagina, e solo dopo aver capito la causa progettare 2 varianti mirate da testare quantitativamente",
                    "Cancellare del tutto la pagina prezzi per eliminare il problema alla radice",
                    "Raddoppiare il budget pubblicitario per portare più visitatori sulla pagina",
                    "Ignorare il dato poiché una percentuale dell'85% è considerata ottimale"
                ],
                "correctIndex": 0,
                "explanation": "A/B testare alla cieca senza insight qualitativo è come lanciare freccette nel buio: 5 interviste da 20 minuti rivelano subito l'inghippo, risparmiando mesi di test statistici a vuoto."
            },
            {
                "question": "Quale rischio cognitivo corre un team che si affida unicamente a 'metriche di vanità' quantitative (es. numero di visualizzazioni di pagina o download totali dell'app)?",
                "options": [
                    "Scambiare l'attenzione superficiale per successo reale, ignorando che gli utenti abbandonano l'app dopo il primo giorno perché non ne comprendono l'utilità o la trovano ingestibile",
                    "Ricevere sanzioni da parte delle autorità antitrust europee",
                    "Consumare tutta la larghezza di banda del server di produzione",
                    "Non poter accedere alle statistiche sul traffico di rete mobile"
                ],
                "correctIndex": 0,
                "explanation": "Le metriche di vanità gonfiano l'ego ma non pagano le bollette: un milione di download non serve a nulla se l' retention a 30 giorni è dell'1% a causa di una pessima esperienza d'uso."
            },
            {
                "question": "Perché nella ricerca qualitativa un campione di 5-8 partecipanti ben selezionati è metodologicamente valido per identificare i problemi di usabilità primari?",
                "options": [
                    "Perché l'obiettivo non è la significatività statistica su valori percentuali, ma la saturazione concettuale: scoprire la natura logica e percettiva degli ostacoli che si ripetono sistematicamente",
                    "Perché le leggi sulla privacy impediscono di intervistare più di otto persone al mese",
                    "Perché il cervello umano ha solo otto lobi cerebrali distinti",
                    "Perché la memoria dei registratori vocali si esaurisce dopo otto ore di audio"
                ],
                "correctIndex": 0,
                "explanation": "Se una porta ha la maniglia rotta, non servono 1000 persone per dimostrarlo statisticamente: basta vederne 5 che sbattono contro la porta chiusa per sapere che la maniglia va riparata subito."
            }
        ]
    }
}

with open("scripts/stull_part3.json", "w", encoding="utf-8") as f:
    json.dump(stull_c11_to_20, f, indent=2, ensure_ascii=False)

print(f"Salvata tranche capitoli 11-12 ({len(stull_c11_to_20)} capitoli)")
