# -*- coding: utf-8 -*-
"""
Genera quiz ed examQuiz accademici per Stull Capitoli 37 - 43.
- 5 quiz per capitolo con spiegazioni dettagliate.
- 3 examQuiz dedicati per capitolo su casi applicativi e scenari d'esame.
- Distrattori tecnici, realistici e universitari (nessuna opzione assurda o infantile).
"""

import json

data_p5 = {
    "stull-c37": {
        "quiz": [
            {
                "question": "Cosa definisce rigorosamente una 'Persona' nella metodologia UX ideata da Alan Cooper?",
                "options": [
                    "Un archetipo realistico e composito di un gruppo di utenti reali, fondato su dati empirici qualitativi e quantitativi, che ne descrive scopi, modelli mentali, comportamenti e punti di attrito",
                    "Un profilo utente generato casualmente da un algoritmo di intelligenza artificiale per popolare il database",
                    "Una scheda biografica romanzata con dettagli fittizi e pittoreschi per intrattenere i designer",
                    "La persona fisica del cliente aziendale che ha firmato il contratto economico di fornitura"
                ],
                "correctIndex": 0,
                "explanation": "Le personas non sono invenzioni di fantasia né fredde tabelle demografiche: sono modelli sintetici basati su ricerche reali che orientano le decisioni del team focalizzandole sui bisogni dell'utente."
            },
            {
                "question": "A quale grave distorsione metodologica allude Stull citando lo show televisivo 'The Dating Game' a proposito delle personas?",
                "options": [
                    "All'errore puerile di riempire le schede con hobby bizzarri, gusti musicali o dettagli privati futili che non hanno alcuna attinenza con il dominio o con gli scopi d'uso del prodotto",
                    "All'impiego di attori professionisti durante le sessioni di test con gli utenti",
                    "All'obbligo di selezionare partecipanti non sposati per i focus group sui servizi digitali",
                    "Alla trasmissione televisiva in diretta dei test di usabilità di un software"
                ],
                "correctIndex": 0,
                "explanation": "Sapere che una persona 'ama il sushi e i gatti persiani' è totalmente inutile se stiamo progettando un software per la fatturazione elettronica. Servono obiettivi di lavoro, ansie e contesti d'uso."
            },
            {
                "question": "Qual è la differenza fondamentale tra una 'Proto-Persona' e una 'Persona Data-Driven'?",
                "options": [
                    "La proto-persona si basa sulle supposizioni e sulle conoscenze preliminari degli stakeholder interni (da validare sul campo); la persona data-driven è interamente costruita e validata su ricerche ed evidenze empiriche dirette",
                    "La proto-persona è scritta in linguaggio XML, mentre la data-driven è redatta in formato JSON",
                    "La proto-persona riguarda solo i software open source, mentre la data-driven riguarda il software commerciale",
                    "Non sussiste differenza: sono denominazioni intercambiabili prive di distinzione operativa"
                ],
                "correctIndex": 0,
                "explanation": "Le proto-personas servono all'inizio per esplicitare i preconcetti del team; devono poi essere necessariamente confrontate con la ricerca sul campo per diventare personas autentiche e affidabili."
            },
            {
                "question": "Come si gestisce la priorità tra più personas quando si prendono decisioni di design contrastanti?",
                "options": [
                    "Identificando una singola 'Persona Primaria': il cui obiettivo deve essere soddisfatto pienamente senza compromessi, assicurandosi che le esigenze delle 'Personas Secondarie' non danneggino l'esperienza della primaria",
                    "Facendo la media aritmetica ponderata delle preferenze cromatiche di tutte le personas",
                    "Progettando un'interfaccia con impostazioni configurabili all'infinito per accontentare chiunque",
                    "Alternando l'interfaccia a giorni pari e dispari a seconda della persona target di turno"
                ],
                "correctIndex": 0,
                "explanation": "Progettare per tutti significa progettare per nessuno. Selezionare una Persona Primaria offre un faro chiaro che guida le scelte e dirime i contrasti durante lo sviluppo."
            },
            {
                "question": "Quale elemento centrale conferisce vero potere predittivo a una scheda Persona?",
                "options": [
                    "Gli 'Obiettivi' (Goals) e le 'Motivazioni sottostanti' (perché vuole compiere l'azione e cosa definisce il suo successo) anziché le mere caratteristiche demografiche (età, sesso, residenza)",
                    "La fotografia a figura intera ad altissima risoluzione con vestiti eleganti",
                    "Il segno zodiacale e il gruppo sanguigno del modello di riferimento",
                    "L'elenco dettagliato delle marche di automobili possedute nel corso della vita"
                ],
                "correctIndex": 0,
                "explanation": "Due uomini di 75 anni residenti a Londra con lo stesso reddito (es. Re Carlo e Ozzy Osbourne) hanno la stessa demografia ma modelli mentali e comportamenti agli antipodi: contano gli obiettivi e i comportamenti."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team progetta un portale per la donazione del sangue e crea la persona 'Marco, 32 anni, appassionato di immersioni subacquee, adora il rock anni '80 e possiede un cane di nome Birba'. Durante il design del form di prenotazione, il team si blocca. Quale lacuna metodologica presenta la persona?",
                "options": [
                    "Sindrome da Dating Game: mancano le informazioni critiche di dominio (frequenza delle donazioni, paure dell'ago, disponibilità di tempo lavorativo, ostacoli burocratici già incontrati)",
                    "Mancata indicazione del codice ISEE e del conto corrente bancario di Marco",
                    "Assenza del consenso informato firmato dal proprietario del cane Birba",
                    "Violazione delle linee guida di accessibilità sul contrasto cromatico della fotografia"
                ],
                "correctIndex": 0,
                "explanation": "I dettagli futili da show televisivo non aiutano a progettare: servono le ansie reali ('ha paura dello svenimento?', 'non sa dove parcheggiare all'ospedale?') per plasmare un servizio utile."
            },
            {
                "question": "Un'azienda SaaS decide di non condurre interviste sul campo e incarica il reparto marketing di redigere 15 personas basate unicamente sulle proprie impressioni interne. Come definisce Stull queste figure?",
                "options": [
                    "Personas immaginarie o speculative: pericolose perché cristallizzano i bias e le supposizioni interne del team sotto una parvenza di metodo, senza alcun contatto con la realtà",
                    "Personas altamente predittive conformi al framework quantitativo di Karl Pearson",
                    "Modelli cognitivi validati secondo le linee guida di usabilità ISO 9241",
                    "Una prassi raccomandata per risparmiare risorse durante la fase di Discovery"
                ],
                "correctIndex": 0,
                "explanation": "Inventare personas a tavolino senza dati sul campo è velenoso: dà l'illusione di essere user-centered mentre si stanno semplicemente disegnando le proprie fantasie interne."
            },
            {
                "question": "In che modo una buona Persona aiuta a risolvere un litigio interminabile tra uno sviluppatore e un designer durante una riunione?",
                "options": [
                    "Spostando il dibattito dai gusti soggettivi dei singoli ('A me piace il blu', 'Io preferisco il menu ad albero') a ciò che serve alla Persona ('Questo comando aiuta Chiara a validare la fattura in 2 minuti?')",
                    "Assegnando la vittoria della discussione a chi ha la voce più alta",
                    "Costringendo i contendenti a tirare a sorte con una moneta da un euro",
                    "Rinviando tutte le decisioni al consiglio di amministrazione dell'anno successivo"
                ],
                "correctIndex": 0,
                "explanation": "La persona spersonalizza il conflitto: non discutiamo di cosa piace a me o a te, ma di cosa serve a Chiara per completare il suo compito. Questo chiude le discussioni sterili."
            }
        ]
    },
    "stull-c38": {
        "quiz": [
            {
                "question": "A quale aneddoto geopolitico fa ricorso Stull per spiegare l'importanza vitale della cartografia dell'esperienza (Isole Spratly)?",
                "options": [
                    "Alla contesa territoriale nel Mar Cinese Meridionale: senza una mappa ufficiale condivisa e riconosciuta, ogni nazione interpreta i confini a proprio piacimento scontrandosi militarmente; nel team UX, senza una Journey Map condivisa, ognuno persegue una visione frammentata",
                    "Alla scoperta di rotte marittime commerciali per la tratta delle spezie verso le Indie orientali",
                    "Alla costruzione di canali artificiali per la navigazione interna dei fiumi europei",
                    "Al naufragio di navi mercantili causato da tempeste geomagnetiche impreviste"
                ],
                "correctIndex": 0,
                "explanation": "Senza una cartografia condivisa (Journey Map), i programmatori vedono solo il database, il marketing vede solo i click e il supporto vede solo i ticket. La mappa unifica la visione sistemica."
            },
            {
                "question": "Quali sono le quattro macro-fasi canoniche che compongono una 'Customer Journey Map' completa?",
                "options": [
                    "Consapevolezza (Awareness), Valutazione/Acquisizione (Consideration), Conversione/Azione (Conversion), Fidelizzazione/Supporto (Retention & Advocacy)",
                    "Compilazione del codice, Debugging, Rilascio sul server, Backup periodico",
                    "Progettazione grafica, Stampa su carta, Distribuzione postale, Archiviazione",
                    "Accesso al portale, Inserimento password, Cambio lingua, Disconnessione"
                ],
                "correctIndex": 0,
                "explanation": "La relazione con l'utente inizia molto prima del click sul sito (Consapevolezza) e continua a lungo dopo l'acquisto (Assistenza e fidelizzazione). La mappa copre l'intero arco temporale."
            },
            {
                "question": "Cosa si intende per 'Touchpoint' (Punto di contatto) all'interno di una mappa del percorso?",
                "options": [
                    "Qualsiasi momento e canale di interazione tra l'utente e l'organizzazione (sito web, email di notifica, cartello fisico, confezione, telefonata con il call center)",
                    "Il punto geometrico esatto in cui il dito tocca la superficie del display capacitivo",
                    "La presa di corrente fisica utilizzata per alimentare i router di rete",
                    "Il pixel centrale del logo aziendale visualizzato nell'header della pagina"
                ],
                "correctIndex": 0,
                "explanation": "Un touchpoint è ogni occasione in cui l'utente fa esperienza del brand: un SMS di conferma arrivato in ritardo è un touchpoint fallito che incrina l'intero viaggio."
            },
            {
                "question": "Cosa rappresenta la 'Curva Emotiva' (Emotional Journey) tracciata lungo le varie fasi della mappa?",
                "options": [
                    "La rappresentazione visiva dei picchi di gioia, soddisfazione, ansia, confusione o frustrazione vissuti dall'utente nel passaggio da un touchpoint all'altro",
                    "Il tracciato elettrocardiografico registrato durante i test medici sul personale",
                    "La variazione del tasso di interesse applicato dai circuiti di pagamento con carta",
                    "La curva di consumo della batteria dello smartphone durante lo scorrimento dei video"
                ],
                "correctIndex": 0,
                "explanation": "La curva emotiva fa balzare all'occhio i 'Pain Points' (i punti più bassi del grafico dove l'utente prova rabbia o ansia), indicando al team dove è più urgente intervenire."
            },
            {
                "question": "Quale differenza separa una 'Customer Journey Map' da un 'Service Blueprint'?",
                "options": [
                    "La Journey Map descrive l'esperienza visibile vissuta dall'utente (Frontstage); il Service Blueprint aggiunge i processi interni invisibili, i sistemi informatici e le azioni dei dipendenti che supportano ogni passaggio (Backstage)",
                    "La Journey Map è disegnata a colori, mentre il Service Blueprint è rigorosamente in bianco e nero",
                    "La Journey Map riguarda solo le automobili, mentre il Service Blueprint riguarda gli edifici",
                    "Non sussiste differenza: sono due denominazioni per indicare il medesimo diagramma di flusso"
                ],
                "correctIndex": 0,
                "explanation": "Il Service Blueprint mostra cosa avviene dietro le quinte: quando l'utente clicca 'Ordina' (Frontstage), il blueprint mappa il magazzino, le chiamate API bancarie e la notifica al corriere (Backstage)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda di noleggio auto ha un sito web splendido con prenotazione in 3 clic, ma all'arrivo in aeroporto i clienti fanno 2 ore di coda al bancone tra dipendenti scortesi e clausole opache, lasciando recensioni a 1 stella. Quale miopia di mapping è emersa?",
                "options": [
                    "Aver limitato la progettazione alla sola interfaccia digitale ignorando il touchpoint fisico critico del viaggio: la UX fallisce se l'esperienza sul campo distrugge le promesse fatte online",
                    "Mancata adozione di font tipografici personalizzati per la stampa del voucher",
                    "Violazione delle linee guida di sicurezza informatica sull'uso dei cookie di sessione",
                    "Utilizzo improprio di animazioni CSS nella schermata di conferma del noleggio"
                ],
                "correctIndex": 0,
                "explanation": "La Journey Map dimostra che il viaggio è continuo: un'ottima UI web non serve a nulla se l'interazione umana successiva trasforma l'esperienza in un incubo."
            },
            {
                "question": "Durante la mappatura del percorso di un servizio di rinnovo patente, il punto di minimo della curva emotiva (-5, rabbia profonda) si colloca tra l'invio della visita medica e la ricezione del documento (3 settimane di silenzio totale). Come si risolve questo pain point?",
                "options": [
                    "Introducendo un sistema di notifiche trasparenti di tracciamento di stato (SMS/Email con link di monitoraggio 'La tua patente è in stampa / affidata al corriere')",
                    "Raddoppiando il costo della marca da bollo per velocizzare i controlli burocratici",
                    "Eliminando la visita medica e rilasciando il documento a chiunque ne faccia richiesta",
                    "Nascondendo la data di scadenza della patente precedente per ridurre l'ansia dell'utente"
                ],
                "correctIndex": 0,
                "explanation": "L'ansia nasce dal vuoto informativo: quando l'utente non sa cosa sta succedendo, immagina il peggio. Un semplice messaggio di avanzamento trasforma l'angoscia in tranquillità."
            },
            {
                "question": "In quale fase del processo di design una Journey Map offre il massimo ritorno sull'investimento (ROI)?",
                "options": [
                    "Nella fase di Discovery e Sintesi della ricerca: per allineare l'intero team interdisciplinare sui punti critici e identificare le maggiori opportunità strategiche prima di disegnare soluzioni",
                    "La sera prima della conferenza stampa di presentazione del prodotto agli azionisti",
                    "Dopo il collaudo definitivo del codice per verificare l'assenza di errori di sintassi",
                    "Esclusivamente in caso di contenzioso legale con i fornitori di connettività internet"
                ],
                "correctIndex": 0,
                "explanation": "La mappa è uno strumento di diagnosi e strategia: serve all'inizio per capire dove fa male il sistema attuale e orientare gli sforzi del team su ciò che conta davvero."
            }
        ]
    },
    "stull-c39": {
        "quiz": [
            {
                "question": "A quale caso storico fa ricorso Stull citando l'Enciclopedia Britannica per illustrare la differenza tra accumulo di dati e Architettura dell'Informazione?",
                "options": [
                    "All'illusione che accumulare testi sterminati e nozioni isolate equivalga a produrre conoscenza fruibile: senza una struttura relazionale, ontologica e gerarchica chiara, la mole di dati diventa un labirinto impenetrabile",
                    "Al passaggio dai caratteri mobili di Gutenberg alla litografia industriale dell'Ottocento",
                    "Alla vendita ambulante porta a porta dei volumi enciclopedici nelle campagne inglesi",
                    "Alla traduzione del testo in lingua gaelica per proteggere le identità linguistiche locali"
                ],
                "correctIndex": 0,
                "explanation": "I contenuti da soli non fanno un buon servizio: se l'architettura dell'informazione è disastrosa, l'utente non troverà mai ciò che cerca, esattamente come in una biblioteca con libri gettati a terra."
            },
            {
                "question": "Nella triade cardine dell'Architettura dell'Informazione (Rosenfeld, Morville & Arango), cosa rappresentano rispettivamente Ontologia, Tassonomia e Coreografia?",
                "options": [
                    "Ontologia definisce il significato specifico dei concetti (cosa intendiamo con le parole); Tassonomia stabilisce la classificazione gerarchica delle categorie; Coreografia governa il movimento e le relazioni d'uso tra di esse",
                    "Ontologia è il database MySQL; Tassonomia è il foglio di stile CSS; Coreografia è l'animazione JavaScript",
                    "Ontologia è la licenza d'uso; Tassonomia è il prezzo di vendita; Coreografia è la campagna pubblicitaria",
                    "Sono tre tipologie di caratteri tipografici utilizzati per comporre titoli, paragrafi e note"
                ],
                "correctIndex": 0,
                "explanation": "La triade di Rosenfeld è fondamentale: prima chiariamo cosa significano i concetti (Ontologia), poi li raggruppiamo in categorie logiche (Tassonomia) e infine progettiamo come l'utente naviga tra essi (Coreografia)."
            },
            {
                "question": "Cos'è la tecnica del 'Card Sorting' (ordinamento delle carte) e a cosa serve?",
                "options": [
                    "Un metodo empirico di ricerca in cui i partecipanti raggruppano schede con i contenuti del sito in categorie logiche secondo il proprio modello mentale, per progettare menu e alberature intuitive",
                    "Un gioco d'azzardo utilizzato per determinare chi pagherà la cena del team di design",
                    "La procedura di ordinamento delle righe di codice prima della compilazione software",
                    "La catalogazione fisica delle ricevute di acquisto per fini di deduzione fiscale"
                ],
                "correctIndex": 0,
                "explanation": "Il card sorting fa parlare gli utenti: invece di inventare i menu alla scrivania, fai raggruppare i contenuti a 20 persone reali e scopri come organizzerebbero loro l'albero di navigazione."
            },
            {
                "question": "Quale differenza separa il 'Card Sorting Aperto' (Open) dal 'Card Sorting Chiuso' (Closed)?",
                "options": [
                    "Nel sorting aperto i partecipanti raggruppano le schede e creano liberamente i nomi delle categorie; nel sorting chiuso i partecipanti devono inserire le schede all'interno di categorie già prefissate dal team",
                    "Il sorting aperto si svolge all'aperto nei parchi pubblici; il sorting chiuso si svolge al chiuso di una stanza",
                    "Il sorting aperto riguarda solo i siti per adulti; il sorting chiuso riguarda i siti per bambini",
                    "Non sussiste differenza: sono denominazioni equivalenti prive di valore metodologico"
                ],
                "correctIndex": 0,
                "explanation": "Aperto (generativo): serve per scoprire quali categorie hanno in mente gli utenti. Chiuso (valutativo): serve per verificare se le categorie che abbiamo ideato noi sono chiare per il pubblico."
            },
            {
                "question": "Cos'è il 'Tree Testing' (test dell'albero informativo) nell'architettura dell'informazione?",
                "options": [
                    "Un metodo per valutare l'efficacia dell'alberatura dei menu privandola della grafica (interfaccia solo testo ad albero), verificando se gli utenti riescono a trovare i percorsi corretti per compiti specifici",
                    "Il collaudo della resistenza dei cavi di rete in fibra ottica esposti al vento",
                    "La verifica del risparmio di carta ottenuto eliminando la documentazione stampata",
                    "Un test di sicurezza informatica contro le infezioni da virus e malware trojan"
                ],
                "correctIndex": 0,
                "explanation": "Il tree testing è la radiografia dell'architettura: togli la grafica e guardi solo la gerarchia testuale dei menu; se gli utenti si perdono nel testo spoglio, nessuna grafica potrà salvarli."
            }
        ],
        "examQuiz": [
            {
                "question": "Sul sito di un ateneo universitario, la voce 'Richiesta duplicato badge smarrito' è inserita sotto 'Rettorato > Ufficio economato e patrimonio > Gestione inventario cespiti'. Gli studenti tempestano il centralino perché non la trovano. Quale errore di architettura dell'informazione è stato commesso?",
                "options": [
                    "L'alberatura riflette l'organigramma burocratico interno dell'ateneo anziché il modello mentale e i compiti dell'utente studente; la voce deve trovarsi sotto 'Servizi per gli studenti > Carriera e documenti'",
                    "Mancata adozione del protocollo di trasferimento file via FTP per i documenti di identità",
                    "Utilizzo di font con interlinea non conforme alle normative ISO per gli atti notarili",
                    "La parola 'badge' è un termine straniero non ammesso dai dizionari della lingua italiana"
                ],
                "correctIndex": 0,
                "explanation": "La legge d'oro dell'IA: MAI organizzare un sito secondo l'organigramma interno dell'azienda. All'utente non importa quale ufficio gestisca la pratica, vuole trovarla dove ha senso logico per lui."
            },
            {
                "question": "Un grande e-commerce di ferramenta deve classificare 50.000 articoli. Molti prodotti appartengono contemporaneamente a più concetti (es. un 'trapano a percussione con batteria al litio' è sia Elettroutensile, sia Strumento a Batteria, sia Articolo per Muratura). Quale modello tassonomico è indispensabile adottare?",
                "options": [
                    "Una classificazione sfaccettata (Faceted Classification) con filtri multidimensionali combinabili, anziché un'unica rigida gerarchia monofiletica",
                    "Una lista alfabetica statica di cinquantamila voci distribuite su un'unica schermata",
                    "Un ordinamento casuale degli articoli che muta ad ogni accesso alla home page",
                    "L'eliminazione di tutti i filtri per costringere gli acquirenti a contattare il negozio fisico"
                ],
                "correctIndex": 0,
                "explanation": "La tassonomia a faccette permette di cercare per molteplici attributi ortogonali (tipo, alimentazione, potenza, marca): l'utente trova il trapano da qualsiasi percorso logico provenga."
            },
            {
                "question": "Durante un Tree Testing su 50 partecipanti per un nuovo portale sanitario, l'82% degli utenti fallisce nel localizzare il comando 'Prenota visita specialistica' perché collocato all'interno della cartella 'Prestazioni ambulatoriali esterne'. Qual è l'intervento immediato?",
                "options": [
                    "Rinominare la cartella con un'etichetta accessibile e naturale (es. 'Visite ed Esami') e spostare il link al primo livello visibile di navigazione",
                    "Aggiungere un video di istruzioni di 15 minuti che spieghi il significato del termine ambulatoriale",
                    "Ignorare il test perché i partecipanti non hanno competenze mediche specialistiche",
                    "Chiudere il portale web e consentire le prenotazioni unicamente tramite fax cartaceo"
                ],
                "correctIndex": 0,
                "explanation": "L'82% di fallimento nel tree test è una condanna inappellabile: l'etichetta è gergale e nascosta. Rinominare con linguaggio naturale e portare in primo piano risolve il problema all'istante."
            }
        ]
    },
    "stull-c40": {
        "quiz": [
            {
                "question": "Cosa postula il fondamentale 'Modello di Kano' formulato dal professor Noriaki Kano sulla soddisfazione del cliente?",
                "options": [
                    "La soddisfazione del cliente non è lineare: diverse caratteristiche e funzionalità del prodotto impattano in modo qualitativamente asimmetrico sulla percezione di valore e sulla fedeltà dell'utente",
                    "Il livello di gradimento di un'applicazione è direttamente proporzionale al numero totale di linee di codice sorgente",
                    "Tutti i bisogni dell'utente possono essere soddisfatti unicamente riducendo il prezzo di vendita del cinquanta per cento",
                    "La fedeltà degli acquirenti decade matematicamente ogni novanta giorni indipendentemente dal servizio"
                ],
                "correctIndex": 0,
                "explanation": "Aggiungere funzioni a caso non aumenta la soddisfazione: alcune funzioni sono date per scontate e se mancano fanno infuriare, altre creano entusiasmo inaspettato con pochissimo sforzo."
            },
            {
                "question": "Come definisce Kano i requisiti 'Must-be' (o Indispensabili)?",
                "options": [
                    "Requisiti fondamentali dati assolutamente per scontati: la loro presenza non genera entusiasmo alcuno, ma la loro minima assenza o malfunzionamento provoca insoddisfazione e rabbia furiosa",
                    "Funzionalità di lusso accessibili solo a chi sottoscrive l'abbonamento più costoso",
                    "Elementi decorativi animati che abbelliscono la testata della home page",
                    "Funzionalità sperimentali rilasciate in versione beta per il collaudo degli sviluppatori"
                ],
                "correctIndex": 0,
                "explanation": "Se apri un'app bancaria e puoi fare il bonifico, non festeggi (è scontato). Ma se il bonifico fallisce o l'app non si apre, la cancelli infuriato. Questo è un requisito Must-be."
            },
            {
                "question": "Cosa caratterizza invece i requisiti 'Performance' (o Unidimensionali) nel Modello di Kano?",
                "options": [
                    "Requisiti in cui la soddisfazione è proporzionale al livello di efficienza fornito: più ce n'è (più veloce, più batteria, più capienza, minor costo), più l'utente è felice; meno ce n'è, meno è soddisfatto",
                    "Caratteristiche visibili solo se l'utente possiede una scheda grafica per videogiochi",
                    "Funzioni che provocano l'immediata chiusura della sessione per motivi di sicurezza",
                    "Test di velocità di digitazione somministrati ai candidati durante i colloqui"
                ],
                "correctIndex": 0,
                "explanation": "I requisiti Performance sono lineari: un'auto che consuma 4 litri/100 km è meglio di una che ne consuma 8; un'app che si carica in 1 secondo è due volte più gradita di una che ci mette 2 secondi."
            },
            {
                "question": "Cosa sono i requisiti 'Delighters' (o Attraenti) e quale ruolo ricoprono nella differenziazione del prodotto?",
                "options": [
                    "Funzionalità inattese e innovative non richieste esplicitamente dall'utente: se mancano non provocano alcun fastidio (l'utente non sa che esistono), ma se presenti generano stupore, gioia e passaparola spontaneo",
                    "I banner promozionali lampeggianti posizionati lungo i margini della pagina",
                    "I contratti di abbonamento con rinnovo automatico e clausole penali",
                    "Le notifiche di avviso sulla scadenza imminente della licenza software"
                ],
                "correctIndex": 0,
                "explanation": "Quando Uber ti ha mostrato per la prima volta l'auto che si muoveva in tempo reale sulla mappa, è stato un Delighter: nessuno lo aveva chiesto, ma ha lasciato tutti a bocca aperta."
            },
            {
                "question": "Quale fenomeno temporale descrive il decadimento dinamico delle categorie di Kano nel corso degli anni?",
                "options": [
                    "I requisiti migrano inesorabilmente verso il basso: ciò che oggi è un Delighter entusiasmante, domani diventa un requisito Performance atteso e dopodomani scade in un Must-be scontato e obbligatorio",
                    "Le funzionalità software diventano gradualmente più costose per legge",
                    "I prodotti tecnologici perdono la compatibilità con la rete elettrica domestica",
                    "Gli utenti sviluppano un'avversione cronica per qualsiasi forma di grafica vettoriale"
                ],
                "correctIndex": 0,
                "explanation": "La telecamera posteriore nelle auto o il Wi-Fi negli hotel erano Delighters straordinari dieci anni fa; oggi se entri in un hotel senza Wi-Fi o l'auto non ha i sensori, te ne vai scandalizzato (Must-be)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda di monopattini elettrici in sharing introduce una nuova funzione che riproduce melodie musicali personalizzate durante la corsa (Delighter teorico), ma il 25% dei monopattini ha freni usurati e l'app fallisce il rilascio della sosta (Must-be compromessi). Quale disastro di priorità evidenzia Kano?",
                "options": [
                    "Gravissimo errore di prioritizzazione: non si possono aggiungere Delighters superficiali quando i requisiti Must-be di base (sicurezza fisica e sosta funzionante) sono rotti; la priorità assoluta è sanare i fondamentali",
                    "Mancata adozione del protocollo audio Bluetooth 5.2 per la trasmissione del suono",
                    "Violazione delle norme sul copyright per la riproduzione pubblica di brani musicali",
                    "Una brillante strategia di fidelizzazione basata sull'emozione sonora dei pedoni"
                ],
                "correctIndex": 0,
                "explanation": "La regola aurea di Kano: prima sistema i Must-be al 100%. Nessuna musichetta simpatica potrà mai farti perdonare un freno rotto o un conto che continua a salire perché non riesci a chiudere la corsa."
            },
            {
                "question": "In un questionario di Kano somministrato ai clienti di un software di grafica, il 90% degli intervistati risponde 'Lo troverei inaccettabile' alla domanda 'Come ti sentiresti se NON ci fosse il salvataggio automatico continuo (Autosave)?'. In quale categoria si colloca l'Autosave?",
                "options": [
                    "Requisito Must-be: il mercato lo dà per scontato; la sua assenza è considerata intollerabile e provoca l'abbandono immediato del prodotto a favore dei concorrenti",
                    "Requisito Reverse: l'utente preferisce salvare manualmente ogni file con la tastiera",
                    "Requisito Indifferente: la funzionalità non produce alcun impatto sulla valutazione",
                    "Requisito Delighter: una sorpresa piacevole che giustifica un aumento del prezzo del 50%"
                ],
                "correctIndex": 0,
                "explanation": "L'analisi bivariata di Kano (domanda funzionale + disfunzionale) classifica subito l'Autosave come Must-be: nel 2026 perdere un'ora di lavoro per un crash è un difetto imperdonabile."
            },
            {
                "question": "Come si sfrutta il Modello di Kano nella gestione strategica del Backlog di prodotto?",
                "options": [
                    "Assicurando in ogni rilascio la tenuta perfetta di tutti i Must-be, allocando risorse per migliorare i fattori Performance chiave e inserendo 1 o 2 Delighters mirati a basso costo e alto impatto emotivo",
                    "Eliminando tutti i requisiti funzionali per sviluppare unicamente delighters decorativi",
                    "Assegnando le priorità in base all'ordine alfabetico dei titoli delle storie utente",
                    "Rifiutando qualsiasi richiesta proveniente dai clienti storici dell'applicazione"
                ],
                "correctIndex": 0,
                "explanation": "La formula vincente di una roadmap bilanciata: fondamenta solide come roccia (Must-be), motore potente e scattante (Performance) e una spolverata di magia inaspettata (Delighter)."
            }
        ]
    },
    "stull-c41": {
        "quiz": [
            {
                "question": "Cos'è rigorosamente una 'Valutazione Euristica' (Heuristic Evaluation) e da chi viene condotta?",
                "options": [
                    "Un metodo di ispezione dell'usabilità condotto da un piccolo gruppo di esperti (tipicamente 3-5 valutatori) che esaminano l'interfaccia confrontandola con principi di usabilità consolidati (euristiche)",
                    "Un test di gradimento somministrato a un campione di mille utenti finali tramite sondaggio telefonico",
                    "Una scansione automatica del codice sorgente eseguita da un software antivirus per rilevare bug",
                    "Un'ispezione fiscale condotta da funzionari dell'amministrazione tributaria sui bilanci societari"
                ],
                "correctIndex": 0,
                "explanation": "La valutazione euristica è un metodo ispettivo di esperti: NON coinvolge utenti finali. Gli esperti navigano l'interfaccia armati di checklist metodica (es. le 10 euristiche di Nielsen)."
            },
            {
                "question": "A quale metafora della vita quotidiana fa ricorso Stull per stigmatizzare l'improvvisazione nella revisione delle interfacce?",
                "options": [
                    "All'aneddoto delle cene disastrose: quando un cuoco cucina per amici basandosi sull'estro emotivo e dimentica ingredienti base o brucia il cibo; una checklist metodica avrebbe evitato errori banali e mortificanti",
                    "Alla costruzione di ponti sospesi senza l'impiego di tiranti in acciaio zincato",
                    "Al decollo di aerei commerciali in condizioni di nebbia fitta senza radar di bordo",
                    "Alla coltivazione di serre idroponiche prive di sistemi di illuminazione a LED"
                ],
                "correctIndex": 0,
                "explanation": "Affidarsi alla pura ispirazione porta a dimenticare le cose ovvie. Esattamente come i piloti d'aereo o i chirurghi, i valutatori UX usano checklist per non farsi sfuggire dettagli critici."
            },
            {
                "question": "Qual è il numero ottimale di valutatori raccomandato da Jakob Nielsen per una valutazione euristica efficace ed economicamente sostenibile?",
                "options": [
                    "Tra 3 e 5 esperti indipendenti, che permettono di scoprire circa il 75-85% dei problemi di usabilità complessivi con il miglior rapporto tra costi e benefici",
                    "Esattamente un solo esperto, per evitare opinioni discordanti e dibattiti interni",
                    "Almeno cinquanta valutatori professionisti residenti in nazioni diverse",
                    "Zero esperti, delegando l'intera verifica a script automatici di machine learning"
                ],
                "correctIndex": 0,
                "explanation": "La curva di Nielsen prova che un solo valutatore trova solo il 35% dei problemi; aggregando le revisioni indipendenti di 3-5 esperti si copre la stragrande maggioranza dei difetti."
            },
            {
                "question": "Qual è il limite metodologico strutturale della valutazione euristica rispetto ai test con utenti reali?",
                "options": [
                    "Può generare falsi allarmi (problemi teorici segnalati dagli esperti che gli utenti reali superano agevolmente) e non può mai sostituire l'osservazione diretta delle reazioni emotive e comportamentali reali",
                    "Richiede la compilazione di moduli notarili per ogni schermata esaminata",
                    "Non può essere applicata su schermi con risoluzione superiore a 1080p",
                    "È formalmente vietata dalle linee guida di sviluppo software dell'Unione Europea"
                ],
                "correctIndex": 0,
                "explanation": "Gli esperti non sono infallibili: possono trovare difetti formali che all'utente non danno fastidio, o mancare blocchi emotivi che solo un vero utente smarrito può palesare sul campo."
            },
            {
                "question": "Come si calcola la 'Gravità di un Problema di Usabilità' (Severity Rating) riscontrato durante una recensione euristica?",
                "options": [
                    "Combinando tre fattori: Frequenza (quanti utenti lo incontrano), Impatto (quanto è difficile superarlo o aggirarlo) e Persistenza (se si risolve da solo o blocca per sempre il compito)",
                    "Moltiplicando il numero di righe di codice CSS per la velocità di download del server",
                    "Calcolando l'età anagrafica del valutatore che ha scoperto il problema",
                    "Assegnando il punteggio massimo unicamente ai problemi legati al colore del logo"
                ],
                "correctIndex": 0,
                "explanation": "Nielsen: gravità da 0 (nessun problema) a 4 (catastrofe di usabilità che impedisce il completamento del compito e impone il blocco del rilascio prima di un fix urgente)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda ha 3 giorni di tempo e un budget di soli 1.500€ per valutare un nuovo e-commerce prima del black friday. Non c'è tempo né budget per reclutare 10 acquirenti reali. Quale metodo di ricerca garantisce la massima efficienza in queste condizioni?",
                "options": [
                    "Una Valutazione Euristica condotta da 3 specialisti UX indipendenti utilizzando le 10 euristiche di Nielsen, con report consolidato e prioritizzazione immediata dei fix critici",
                    "La cancellazione del sito internet per ripartire con lo sviluppo da zero l'anno successivo",
                    "Un focus group informale con i dipendenti della mensa aziendale durante il pranzo",
                    "L'invio di questionari cartacei per posta a un elenco telefonico di 500 famiglie"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il super-potere della valutazione euristica: 'discount usability'. Con pochi soldi e in 48 ore, 3 esperti ripuliscono l'interfaccia dai problemi più marchiani prima del debutto."
            },
            {
                "question": "Durante un'ispezione euristica, un esperto nota che il pulsante 'Cestino' cancella immediatamente i file senza conferme né possibilità di ripristino. Quale euristica di Nielsen viene violata con gravità massima (Severity 4)?",
                "options": [
                    "Euristica 5: Prevenzione dell'errore (Error Prevention) ed Euristica 3: Controllo e libertà dell'utente (User Control and Freedom / Undo)",
                    "Euristica 8: Design estetico e minimalista",
                    "Euristica 4: Coerenza e standard tipografici",
                    "Euristica 10: Documentazione cartacea e supporto telefonico"
                ],
                "correctIndex": 0,
                "explanation": "Distruggere dati senza avviso né Undo è un errore critico di Severity 4: viola la prevenzione dell'errore e toglie all'utente il controllo e la libertà fondamentale di annullare l'azione."
            },
            {
                "question": "Come deve essere condotta una sessione di revisione euristica tra 4 esperti per evitare la contaminazione reciproca dei giudizi?",
                "options": [
                    "Ciascun esperto deve ispezionare l'interfaccia in totale autonomia e isolamento redigendo il proprio elenco di violazioni; solo successivamente i valutatori si riuniscono per aggregare e pesare i dati",
                    "Tutti e 4 gli esperti devono guardare lo stesso monitor contemporaneamente esprimendo pareri a voce alta",
                    "Gli esperti devono votare a maggioranza su ogni singolo elemento grafico prima di annotarlo",
                    "I valutatori devono scambiarsi i computer ogni quindici minuti durante l'ispezione"
                ],
                "correctIndex": 0,
                "explanation": "L'indipendenza iniziale è categorica: se gli esperti discutono insieme durante l'ispezione, il più carismatico o anziano influenzerà gli altri annullando i benefici della pluralità di sguardi."
            }
        ]
    },
    "stull-c42": {
        "quiz": [
            {
                "question": "Qual è il presupposto etico e metodologico supremo di qualsiasi 'Test Utente' (Usability Testing)?",
                "options": [
                    "Si sta testando l'interfaccia e il sistema, MAI l'intelligenza o le capacità del partecipante: l'obiettivo è imparare dove il software fallisce per correggerlo, non esaminare la persona",
                    "Il partecipante deve dimostrare una perizia tecnica impeccabile per meritare il compenso pattuito",
                    "Il test ha lo scopo di convincere l'utente ad acquistare immediatamente il prodotto al termine della prova",
                    "La prova serve a individuare i dipendenti aziendali meritevoli di promozione o licenziamento"
                ],
                "correctIndex": 0,
                "explanation": "La prima cosa che il facilitatore dice all'utente: 'Noi stiamo testando il sito, non stiamo testando te. Se qualcosa non funziona o ti blocchi, la colpa è nostra e del sito, non tua'."
            },
            {
                "question": "In che cosa consiste il celebre 'Thinking Aloud Protocol' (Protocollo del pensiero ad alta voce) ideato da Clayton Lewis?",
                "options": [
                    "Chiedere al partecipante di verbalizzare continuamente ad alta voce pensieri, dubbi, impressioni, aspettative e motivazioni man mano che compie le azioni a schermo",
                    "Obbligare l'utente a cantare i testi presenti nei paragrafi dell'interfaccia",
                    "Registrare le onde cerebrali tramite elettrodi applicati sul cuoio capelluto",
                    "Far recitare all'utente una poesia a memoria prima di iniziare il test operativo"
                ],
                "correctIndex": 0,
                "explanation": "Il 'Think Aloud' è una finestra aperta sul cervello dell'utente: ti permette di sapere cosa sta cercando con gli occhi, cosa lo confonde e perché decide di cliccare quel pulsante."
            },
            {
                "question": "Come deve essere formulato un compito di test (Task) per non inquinare il comportamento del partecipante?",
                "options": [
                    "Fornendo uno scenario realistico con un obiettivo chiaro ('Devi comprare un regalo per il compleanno di tua sorella con budget di 30€'), senza mai suggerire i termini esatti dei menu o i passi operativi da compiere",
                    "Dicendo all'utente: 'Clicca sul pulsante blu in alto a destra, seleziona la voce tre del menu e premi invia'",
                    "Ordinando all'utente di memorizzare l'intero catalogo entro novanta secondi",
                    "Lasciando l'utente davanti allo schermo senza dargli alcuna istruzione o compito per 3 ore"
                ],
                "correctIndex": 0,
                "explanation": "Se nel compito scrivi 'Trova la voce Abbonamento Family', l'utente cercherà con gli occhi la parola 'Family' senza pensare. Lo scenario deve descrivere il bisogno, non la procedura."
            },
            {
                "question": "Quale deve essere il comportamento rigoroso del 'Facilitatore' quando l'utente si blocca e chiede: 'Devo cliccare qui?'?",
                "options": [
                    "Mantenere una neutralità assoluta e restituire la domanda con un rilancio esplorativo (es. 'Cosa ti aspetteresti che succeda se cliccassi lì?'), senza mai suggerire la soluzione né difendere il sito",
                    "Dire subito all'utente dove cliccare per velocizzare la conclusione della prova",
                    "Spiegare all'utente che il team ha impiegato 6 mesi per disegnare quel pulsante e che è chiarissimo",
                    "Interrompere il test ed espellere il partecipante per manifesta incapacità d'uso"
                ],
                "correctIndex": 0,
                "explanation": "Il facilitatore non deve mai aiutare l'utente: se lo aiuti rovini il test. Rilanciare la domanda permette di scoprire il modello mentale dell'utente senza condizionarlo."
            },
            {
                "question": "Perché Jakob Nielsen e Steve Krug concordano sul fatto che 'Testare con 5 utenti è sufficiente' per ciascun ciclo iterativo?",
                "options": [
                    "Perché dopo 5 partecipanti i problemi più gravi si ripetono costantemente (curva dei rendimenti decrescenti): è infinitamente più saggio testare con 5, correggere gli errori e testare di nuovo con altri 5",
                    "Perché i laboratori di test non possono contenere più di cinque sedie fisiche per motivi di sicurezza",
                    "Perché le normative vigenti sulla privacy impediscono di registrare più di cinque persone alla settimana",
                    "Perché la memoria dei computer si satura dopo aver salvato cinque file video di sessione"
                ],
                "correctIndex": 0,
                "explanation": "Meglio 3 test da 5 persone distribuiti nel tempo (iterazione) che 1 solo test mastodontico da 50 persone alla fine del progetto quando è troppo tardi per correggere gli errori."
            }
        ],
        "examQuiz": [
            {
                "question": "Durante un test di usabilità, il partecipante clicca per tre volte su un testo non cliccabile, poi scuote la testa e arrossisce dicendo: 'Scusatemi tanto, sono proprio stupido con la tecnologia'. Qual è l'intervento immediato e doveroso del facilitatore?",
                "options": [
                    "Rassicurarlo prontamente: 'Non chiederti scusa, non c'è nulla di sbagliato in te. Se hai cliccato lì significa che l'interfaccia ha fatto sembrare quel testo cliccabile, hai appena scoperto un nostro errore prezioso'",
                    "Confermare all'utente che in effetti quel testo non era un pulsante e che avrebbe dovuto fare più attenzione",
                    "Annotare sul report che il partecipante presenta lacune di apprendimento cognitivo",
                    "Spegnere il monitor del computer per proteggere la privacy aziendale"
                ],
                "correctIndex": 0,
                "explanation": "La de-colpevolizzazione è un dovere umano e professionale: l'utente che si sente in colpa si blocca e non produce più feedback autentico. Rassicurarlo restituisce serenità alla prova."
            },
            {
                "question": "Un designer assiste dietro lo specchio unidirezionale al test del carrello da lui disegnato. Vedendo l'utente esitare, il designer urla furioso: 'Ma è cieco? Non vede che il tasto checkout è verde?'. Quale patologia di bias emotivo si sta manifestando?",
                "options": [
                    "La maledizione della conoscenza e l'attaccamento egoico al proprio manufatto: il designer giudica l'utente dal punto di vista dell'esperto che sa già tutto, rifiutando l'evidenza empirica del fallimento del design",
                    "Un'applicazione rigorosa del principio di retroazione sensoriale di Donald Norman",
                    "La violazione delle linee guida di sicurezza informatica sull'osservazione remota",
                    "Un malfunzionamento dell'impianto di climatizzazione della sala di osservazione"
                ],
                "correctIndex": 0,
                "explanation": "Assistere a un test utente è una cura di umiltà per qualunque designer: vedere qualcuno faticare sul tuo lavoro distrugge l'ego e ti fa capire che se l'utente non lo vede, il design è sbagliato."
            },
            {
                "question": "Come si organizza la sessione di debriefing con il team di sviluppo subito dopo aver concluso 5 test utente?",
                "options": [
                    "Radunando team e stakeholder per stilare l'elenco dei 3 problemi più gravi osservati, concordando fix rapidi e minimalisti da implementare immediatamente nel ciclo di sviluppo successivo",
                    "Redigendo una memoria difensiva per dimostrare ai dirigenti che gli utenti intervistati erano incompetenti",
                    "Pianificando un progetto di riscrittura totale dell'intero sistema operativo per i successivi tre anni",
                    "Distruggendo le registrazioni video per non lasciare prove di difetti di programmazione"
                ],
                "correctIndex": 0,
                "explanation": "Come insegna Steve Krug: riunirsi subito dopo, scegliere i 'tre problemi più gravi che impediscono di completare il compito' e concordare la correzione più semplice e veloce da fare subito."
            }
        ]
    },
    "stull-c43": {
        "quiz": [
            {
                "question": "A quale metafora evolutiva fa ricorso Stull nel capitolo conclusivo citando la 'Regina Rossa' di Lewis Carroll (Attraverso lo specchio) e il biologo Leigh Van Valen?",
                "options": [
                    "All'imperativo biologico della coevoluzione continua: 'Qui per restare nello stesso posto devi correre più veloce che puoi'; i prodotti digitali non sono mai finiti e devono adattarsi incessantemente ai mutamenti di modelli mentali, tecnologie e concorrenza",
                    "Alla successione dinastica delle monarchie costituzionali europee nel corso dell'Ottocento",
                    "Al gioco degli scacchi come simulazione delle strategie di guerra medievale",
                    "All'obbligo di utilizzare colori regali come il porpora all'interno delle applicazioni di lusso"
                ],
                "correctIndex": 0,
                "explanation": "Un sito che non si aggiorna non rimane stabile: regredisce. Le abitudini degli utenti evolvono, i dispositivi cambiano, gli standard si alzano: fermarsi equivale a morire."
            },
            {
                "question": "Quali tre definizioni popolari ma riduttive di 'buona UX' vengono dialetticamente confutate da Edward Stull?",
                "options": [
                    "1. La buona UX è mera 'Efficienza' (velocità cronometrica); 2. La buona UX è mera 'Facilità' (assenza totale di sforzo); 3. La buona UX è pura 'Gioia' (delight decorativo forzato)",
                    "1. Il software deve essere gratuito; 2. Il codice deve essere Java; 3. Lo schermo deve essere 4K",
                    "1. Il sito deve contenere musica; 2. I font devono essere con grazie; 3. Il server deve essere Linux",
                    "1. Gli utenti devono avere meno di 30 anni; 2. Il logo deve essere tondo; 3. Il testo deve essere breve"
                ],
                "correctIndex": 0,
                "explanation": "Stull smonta i dogmi: non tutto deve essere efficiente (un videogioco efficiente finirebbe in 1 secondo); non tutto deve essere facile (imparare richiede sforzo); non tutto deve essere gioioso (un portale funebre o medico richiede sobrietà)."
            },
            {
                "question": "In quali contesti umani l''Inefficienza deliberata' rappresenta un valore esperienziale supremo superiore alla fretta e alla velocità?",
                "options": [
                    "In esperienze come una cena gastronomica, un rituale del tè, un videogioco d'avventura, la lettura di un romanzo o l'ascolto di un disco in vinile: dove il valore risiede nel tempo assaporato e nel viaggio stesso, non nel traguardo",
                    "Nelle operazioni di atterraggio d'emergenza degli aeroplani commerciali",
                    "Nel calcolo dell'indice dei prezzi al consumo dell'istituto nazionale di statistica",
                    "Nell'elaborazione delle transazioni dei mercati azionari ad alta frequenza"
                ],
                "correctIndex": 0,
                "explanation": "Se applichi l'efficienza cieca alla musica, suoni una sinfonia di Beethoven a quadrupla velocità per farla durare 5 minuti. Molte esperienze umane sublimi sono fatte di benefica lentezza."
            },
            {
                "question": "Qual è il test morale ed etico fondante con cui Stull sigilla l'intera opera sulla User Experience?",
                "options": [
                    "'Quanto meno, la nostra interfaccia e il nostro servizio preservano e tutelano la sicurezza, la tranquillità e la dignità dell'essere umano?'",
                    "'Quanto profitto netto siamo riusciti a estrarre dal cliente prima che cancellasse l'account?'",
                    "'Quante righe di codice sorgente sono state compilate senza generare avvisi di warning?'",
                    "'Quanti premi internazionali di graphic design siamo riusciti ad aggiudicarci nell'anno solare?'"
                ],
                "correctIndex": 0,
                "explanation": "L'etica del designer è proteggere la persona: prima ancora di stupire o arricchire l'azienda, abbiamo il dovere morale di non umiliare, non truffare e non angosciare l'essere umano che usa il nostro prodotto."
            },
            {
                "question": "In che cosa consiste il 'Ciclo di Miglioramento Continuo' post-rilascio nella maturità di un'organizzazione UX?",
                "options": [
                    "Nel monitoraggio costante di telemetria, feedback qualitativo, recensioni e test regolari, traducendo i problemi emergenti in un backlog di ottimizzazione incrementale senza fine",
                    "Nel licenziamento del team di sviluppo subito dopo il giorno del lancio per azzerare i costi",
                    "Nel rifiuto categorico di apportare modifiche all'interfaccia dopo la pubblicazione online",
                    "Nell'invio automatico di una copia di backup dell'intero sito al tribunale fallimentare"
                ],
                "correctIndex": 0,
                "explanation": "Il lancio non è la fine: è solo il primo giorno di vita del prodotto. Da quel momento inizia il vero lavoro: misurare, ascoltare, iterare e perfezionare senza sosta."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'applicazione per la compilazione del testamento biologico e delle donazioni post-mortem viene progettata con coriandoli animati, suoni di trombetta e popup con la scritta: 'Yuppi! Hai pianificato le tue esequie, sei un grande!'. Quale errore filosofico ed etico di design denuncia Stull?",
                "options": [
                    "Banalizzazione grottesca del momento: il dogma della 'gioia forzata' (delight a tutti i costi) applicato a un tema intimo e solenne offende la dignità dell'utente; in contesti gravi servono rispetto, silenzio e sobrietà",
                    "Mancata integrazione delle API di pagamento in criptovalute per le spese funebri",
                    "Violazione delle specifiche di rendering CSS sui dispositivi con schermi AMOLED",
                    "Mancanza di una colonna sonora stereofonica ad alta fedeltà di sottofondo"
                ],
                "correctIndex": 0,
                "explanation": "Il culto del 'delight' cieco è tossico. Ci sono momenti della vita umana (lutto, salute, separazioni, denunce) che richiedono sacralità, tatto e dignità assoluta, non fuochi d'artificio digitali."
            },
            {
                "question": "Nel design di un videogioco di esplorazione, gli sviluppatori introducono un pulsante 'Salta direttamente al livello finale e vinci in 1 secondo'. Tutti i giocatori che lo usano dichiarano che il gioco è noioso e privo di senso. Quale principio di Stull è confermato?",
                "options": [
                    "L'efficienza cieca distrugge il valore del viaggio: l'appagamento umano scaturisce dal superamento dell'ostacolo e dalla bellezza del percorso, non dall'azzeramento istantaneo dell'esperienza",
                    "La legge di Hick applicata ai controlli joystick fisici dei computer da gioco",
                    "L'incompatibilità delle schede video per videogiochi con i monitor a cristalli liquidi",
                    "La violazione delle normative antitrust sulla concorrenza tra case di sviluppo software"
                ],
                "correctIndex": 0,
                "explanation": "La vita non è solo efficienza da catena di montaggio. Il gioco, l'arte e la cultura traggono il loro valore dal tempo dedicato e dall'esperienza vissuta passo dopo passo."
            },
            {
                "question": "Un'azienda monopolista di software scolastico per il registro elettronico non aggiorna l'usabilità dell'interfaccia da 10 anni perché 'tanto gli insegnanti sono obbligati a usarlo'. Improvvisamente il ministero approva la concorrenza e in 3 mesi il 95% delle scuole migra su un'app moderna fluida. Quale legge biologica ha punito l'azienda?",
                "options": [
                    "L'ipotesi della Regina Rossa: credere che il software fosse finito e intoccabile ha condannato l'azienda all'estinzione evolutiva non appena il mercato ha ripristinato la libertà di scelta per gli utenti",
                    "La teoria dei quanti di luce applicata alla scansione dei documenti cartacei",
                    "La legge di conservazione della massa formulata da Antoine Lavoisier",
                    "Un guasto irreparabile dei server centrali causato dall'eccessivo calore estivo"
                ],
                "correctIndex": 0,
                "explanation": "Fermarsi mentre il resto del mondo corre è una sentenza di morte. L'obbligo forzato crea solo odio; non appena si apre una via di fuga, l'abbandono è immediato e totale."
            }
        ]
    }
}

with open("scripts/stull_clean_part5.json", "w", encoding="utf-8") as f:
    json.dump(data_p5, f, indent=2, ensure_ascii=False)

print(f"Salvata tranche capitoli 37-43 puliti con successo ({len(data_p5)} capitoli, {sum(len(v['quiz']) for v in data_p5.values())} quiz, {sum(len(v['examQuiz']) for v in data_p5.values())} examQuiz)")
