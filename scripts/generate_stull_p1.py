# -*- coding: utf-8 -*-
"""
High-level academic quiz and exam questions for Stull UX Design - Part 1 & Part 2 (Chapters 1 to 5).
"""
import json

stull_p1_p2 = {
    "stull-c1": {
        "quiz": [
            {
                "question": "Qual è l'etimologia e il significato originario della locuzione 'User Experience' secondo la ricostruzione di Stull?",
                "options": [
                    "Deriva dal latino 'uti' (utilizzare, trarre utilità) ed 'experientia' (conoscenza acquisita attraverso tentativi ed errori pratici): insieme significano 'conoscenza maturata facendo qualcosa'",
                    "Deriva dal greco antico 'techne' e indica la bellezza geometrica degli schermi catodici",
                    "È un neologismo coniato dagli uffici brevetti della Silicon Valley per tutelare i marchi software",
                    "Indica il protocollo di collaudo hardware delle prime schede madri IBM"
                ],
                "correctIndex": 0,
                "explanation": "L'etimologia rivela la natura attiva della UX: l'esperienza non è passiva contemplazione, ma conoscenza pragmatica che l'utente accumula interagendo con il sistema."
            },
            {
                "question": "Perché l'autore afferma categoricamente che 'La User Experience è inevitabile'?",
                "options": [
                    "Perché ogni volta che un essere umano interagisce con un prodotto, servizio o ambiente, un'esperienza si genera comunque: se non la progettate consapevolmente, state progettando per omissione un'esperienza casuale o pessima",
                    "Perché i sistemi operativi moderni impediscono l'avvio di applicazioni prive di certificato UX",
                    "Perché le leggi sulla concorrenza impongono a tutte le aziende di assumere un ricercatore UX",
                    "Perché gli utenti rifiutano di acquistare prodotti privi di packaging biodegradabile"
                ],
                "correctIndex": 0,
                "explanation": "Non si può scegliere di 'non avere' una UX: anche un'interfaccia caotica o un modulo illeggibile producono un'esperienza (frustrazione, rabbia). Progettare significa governare questo esito."
            },
            {
                "question": "Quali due grandi macro-aree compongono la disciplina della User Experience?",
                "options": [
                    "UXD (User Experience Design, la progettazione esecutiva della soluzione) e UXR (User Experience Research, la comprensione analitica dei bisogni e dei comportamenti)",
                    "Frontend Development e Backend Engineering",
                    "Marketing pubblicitario e Gestione del personale",
                    "Grafica 3D e Montaggio sonoro"
                ],
                "correctIndex": 0,
                "explanation": "La UX poggia su due gambe inscindibili: la Research (scoprire i bisogni reali degli utenti) e il Design (costruire la risposta formale e interattiva a quei bisogni)."
            },
            {
                "question": "In cosa differisce l'approccio olistico della UX rispetto alla tradizionale User Interface (UI)?",
                "options": [
                    "La UI si concentra sugli elementi visivi e sensoriali a schermo (bottoni, colori, tipografia); la UX abbraccia l'intero ecosistema dell'esperienza, dal primo contatto all'assistenza post-vendita",
                    "La UI riguarda solo i programmatori e la UX riguarda solo i dirigenti aziendali",
                    "La UI si occupa dei siti web e la UX solo dei prodotti fisici tangibili",
                    "Non sussiste alcuna distinzione tecnica, essendo sinonimi commerciali"
                ],
                "correctIndex": 0,
                "explanation": "La UI è solo la pelle visibile del sistema; la UX è il viaggio completo: comprende usabilità, utilità percepita, velocità, affidabilità del servizio e sensazioni emotive provate."
            },
            {
                "question": "Qual è il ruolo dell'empatia nel processo di progettazione human-centered?",
                "options": [
                    "Capacità di sospendere i propri giudizi personali per comprendere a fondo le frustrazioni, i modelli mentali e il contesto operativo delle persone a cui il prodotto è destinato",
                    "Accettare qualsiasi lamentela del cliente concedendo rimborsi economici immediati",
                    "Disegnare interfacce con colori pastello per trasmettere serenità emotiva",
                    "Imporre agli utenti le scelte estetiche ritenute migliori dal designer"
                ],
                "correctIndex": 0,
                "explanation": "L'empatia è lo strumento cognitivo essenziale della UX: permette di uscire dalla propria mente di esperto per indossare i panni dell'utente profano e cogliere dove il sistema fallisce."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda lancia un'app innovativa con una grafica premiata e animazioni spettacolari, ma il servizio clienti riceve centinaia di chiamate perché gli utenti non riescono a recuperare la password. Come si valuta questo prodotto secondo Stull?",
                "options": [
                    "Un fallimento di UX sistemica: una UI visivamente splendida non può compensare un cedimento funzionale che blocca l'accesso e distrugge la fiducia dell'utente",
                    "Un successo straordinario poiché l'estetica è l'unico parametro di valutazione dell'esperienza",
                    "Un problema imputabile esclusivamente alla scarsa preparazione informatica dei consumatori",
                    "Un'opportunità commerciale per far pagare l'assistenza tecnica telefonica"
                ],
                "correctIndex": 0,
                "explanation": "La UX è la catena completa: se un anello fondamentale si spezza (il recupero credenziali), l'intera esperienza crolla, indipendentemente dalla bellezza grafica delle schermate."
            },
            {
                "question": "Quale differenza separa la 'Ricerca Primaria' dalla 'Ricerca Secondaria' in un processo di UX Research?",
                "options": [
                    "La primaria raccoglie dati originali direttamente dagli utenti finali (interviste, test); la secondaria analizza dati e studi già pubblicati da terzi (benchmark, report di settore)",
                    "La primaria viene svolta prima del 2000 e la secondaria dopo il 2010",
                    "La primaria è facoltativa e la secondaria è imposta dalla legge",
                    "La primaria utilizza solo carta e penna e la secondaria software di analytics"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca secondaria (desk research) fa il punto su ciò che già si sa sul mercato; la primaria (field research) scende sul campo per scoprire le verità non documentate del nostro target specifico."
            },
            {
                "question": "Cosa si intende per 'ROI (Return on Investment) della UX' nei contesti aziendali?",
                "options": [
                    "Il ritorno economico misurabile generato dal buon design: aumento delle conversioni, riduzione dei costi di supporto e assistenza, e abbattimento dei tempi di sviluppo evitando rifacimenti",
                    "Il tasso di interesse sui prestiti bancari concessi alle agenzie di grafica",
                    "Il costo delle licenze software per i programmi di prototipazione",
                    "La percentuale di sconto applicata agli abbonamenti annuali"
                ],
                "correctIndex": 0,
                "explanation": "La UX non è una spesa cosmetica: prevenire un errore di architettura in fase di ricerca costa un decimo rispetto a correggerlo dopo il rilascio in produzione (Regola dell'1:10:100 di Pressman)."
            }
        ]
    },
    "stull-c2": {
        "quiz": [
            {
                "question": "Cosa stabilisce l'assioma cardinale della comunità UX: 'Voi non siete l'utente' (You are not the user)?",
                "options": [
                    "I progettisti non possono mai vivere l'interfaccia con lo sguardo vergine e ingenuo di chi la usa per la prima volta, poiché ne conoscono intimamente i meccanismi interni",
                    "Gli sviluppatori non hanno il permesso di utilizzare i computer personali in orario di lavoro",
                    "Un'applicazione web deve essere venduta solo a consumatori residenti all'estero",
                    "Gli utenti registrati non devono mai comunicare direttamente con i grafici"
                ],
                "correctIndex": 0,
                "explanation": "Chi disegna un sistema soffre inevitabilmente della 'Maledizione della Conoscenza': sa dove cliccare e cosa accadrà dopo. Presumere che l'utente ragioni come noi è l'errore più letale del design."
            },
            {
                "question": "Nella metafora del pesce palla giapponese (Torafugu) descritta da Stull, a cosa corrisponde il veleno mortale nel processo di design?",
                "options": [
                    "Ai preconcetti, ai bias cognitivi e alle supposizioni non verificate che il team riversa nel progetto presumendo di sapere già cosa desiderano gli utenti",
                    "All'utilizzo di font tipografici privi di licenza commerciale",
                    "All'eccessiva velocità di caricamento delle pagine web sul server",
                    "Alla scelta di linguaggi di programmazione open-source"
                ],
                "correctIndex": 0,
                "explanation": "Come lo chef di sushi deve eliminare con precisione chirurgica la tetrodotossina per non avvelenare il commensale, il team UX deve spurgare il progetto dai propri pregiudizi tramite la ricerca empirica."
            },
            {
                "question": "Nel caso studio dell'app 'Fishes'R'Us' per amanti del pesce, perché anche un designer che ama cucinare il pesce non è 'l'utente' del sistema?",
                "options": [
                    "Perché chi progetta conosce la logica del database, non ha l'ansia di bruciare la cena e non può cancellare la propria competenza tecnologica sull'interfaccia",
                    "Perché per essere utenti bisogna possedere un ristorante professionale di pesce",
                    "Perché la normativa sulla privacy vieta ai dipendenti di utilizzare le app aziendali",
                    "Perché il designer cucina usando ricette cartacee tradizionali"
                ],
                "correctIndex": 0,
                "explanation": "Condividere il dato demografico (amare il pesce) non basta: chi progetta non vive l'esperienza autentica del principiante che apre l'app con le mani bagnate e i fornelli accesi."
            },
            {
                "question": "Cos'è il bias cognitivo noto come 'Maledizione della Conoscenza' (Curse of Knowledge)?",
                "options": [
                    "L'incapacità psicologica, una volta appreso un concetto o padroneggiato un sistema complesso, di re-immaginare lo stato mentale di chi quel concetto non lo conosce affatto",
                    "L'amnesia temporanea causata da un sovraccarico di studio universitario",
                    "Il timore di condividere segreti industriali con le aziende concorrenti",
                    "La perdita di dati su disco fisso a causa di un crash di sistema"
                ],
                "correctIndex": 0,
                "explanation": "La conoscenza è una strada a senso unico: una volta che sappiamo come funziona un'interfaccia, ci sembra 'ovvia', e consideriamo erroneamente stupido o distratto chiunque incontri difficoltà."
            },
            {
                "question": "Dove deve collocarsi la progettazione UX di successo secondo il modello a due sfere di Stull?",
                "options": [
                    "Esattamente nell'area di intersezione armonica tra i bisogni concreti dell'utente e gli obiettivi economici e strategici dell'azienda",
                    "Unicamente all'interno della sfera degli obiettivi di profitto dell'azienda",
                    "Esclusivamente all'interno dei desideri dell'utente anche se portano al fallimento del business",
                    "Al di fuori di entrambe le sfere per preservare la neutralità artistica"
                ],
                "correctIndex": 0,
                "explanation": "La UX non è filantropia né avidità: è l'intersezione magica. Un'app fantastica per l'utente che non genera entrate muore; un'app che massimizza il profitto a spese dell'utente viene disinstallata."
            }
        ],
        "examQuiz": [
            {
                "question": "Uno sviluppatore esperto di Linux afferma: 'Questo form per la configurazione dei server DNS è intuitivo, io l'ho compilato in 10 secondi'. Quale fallacia metodologica sta commettendo?",
                "options": [
                    "Il bias del falso consenso e la violazione dell'assioma 'Voi non siete l'utente': confonde la propria competenza da super-esperto con l'intuitività universale dell'interfaccia",
                    "Una violazione del codice deontologico dei programmatori di sistema",
                    "Un errore di sintassi nella gestione delle chiamate asincrone",
                    "La mancata conformità alle direttive antitrust internazionali"
                ],
                "correctIndex": 0,
                "explanation": "Niente è intuitivo per definizione, tranne ciò che già sappiamo fare. Confondere la propria familiarità professionale con la facilità per gli altri è la causa primaria di software ostili e incomprensibili."
            },
            {
                "question": "Come si contrasta efficacemente la 'Maledizione della Conoscenza' all'interno di un team di prodotto?",
                "options": [
                    "Conducendo test di usabilità continui con persone realmente esterne al progetto che non abbiano mai visto il software prima",
                    "Facendo testare il software ai colleghi della scrivania accanto",
                    "Scrivendo manuali d'uso di 500 pagine da allegare all'applicazione",
                    "Assumendo unicamente programmatori junior privi di esperienza"
                ],
                "correctIndex": 0,
                "explanation": "L'unico specchio della realtà sono gli occhi ingenui dei neofiti: solo osservare uno sconosciuto che prova a usare il software svela le trappole mentali invisibili al team di sviluppo."
            },
            {
                "question": "Cosa accade a un prodotto digitale quando il team di design si concentra unicamente sugli 'Obiettivi di Business' ignorando i 'Bisogni dell'Utente'?",
                "options": [
                    "Il prodotto adotta dark pattern, inganni visivi e barriere all'uscita, ottenendo metriche effimere a breve termine ma distruggendo la fidelizzazione e provocando fuga di massa",
                    "Il prodotto conquista immediatamente la leadership del mercato mondiale",
                    "L'applicazione riduce automaticamente il consumo energetico sui server",
                    "I browser bloccano l'accesso al sito tramite firewall governativi"
                ],
                "correctIndex": 0,
                "explanation": "Ottimizzare solo il business genera prodotti predatori (abbonamenti difficili da disdire, costi nascosti): l'utente si sente truffato e si rifugia presso concorrenti più etici e trasparenti."
            }
        ]
    },
    "stull-c3": {
        "quiz": [
            {
                "question": "Cosa intende Stull con il principio: 'Siete in competizione con tutto' (You are competing with everything)?",
                "options": [
                    "Gli utenti non confrontano la vostra app solo con i concorrenti diretti dello stesso settore, ma con le migliori esperienze digitali quotidiane che usano (Amazon, Uber, Netflix, Apple)",
                    "Ogni sito web deve vendere qualsiasi tipologia di merce per sopravvivere sul mercato",
                    "Le aziende tecnologiche sono in guerra legale permanente tra loro",
                    "I computer desktop sono destinati a essere distrutti dagli smartphone"
                ],
                "correctIndex": 0,
                "explanation": "Questo è il fenomeno delle 'Aspettative Liquide': se con Uber ordino un'auto con un tocco e con Amazon pago in un secondo, pretendo la stessa immediatezza e semplicità anche dalla banca o dalla pubblica amministrazione."
            },
            {
                "question": "Cosa si intende per 'Aspettative Liquide' (Liquid Expectations) nel comportamento dei consumatori digitali?",
                "options": [
                    "Le aspettative di semplicità, velocità e fluidità maturate su un servizio eccellente 'trasbordano' e si riversano su qualsiasi altro settore merceologico",
                    "La tendenza dei display a diventare flessibili e pieghevoli",
                    "L'incertezza sui prezzi dei carburanti per autotrazione",
                    "La volatilità dei mercati delle criptovalute"
                ],
                "correctIndex": 0,
                "explanation": "Le aspettative non sono più stagne per settore: l'utente non pensa 'per essere un'assicurazione questo sito è decente', ma 'perché per fare un preventivo devo faticare mentre su Spotify cambio brano all'istante?'."
            },
            {
                "question": "Quale conseguenza comporta il principio delle aspettative liquide per la fase di benchmarking competitivo?",
                "options": [
                    "È necessario analizzare non solo i concorrenti diretti, ma anche i benchmark indiretti e analogici per trarre ispirazione dalle migliori pratiche di interazione al mondo",
                    "Bisogna copiare pixel per pixel il codice HTML del leader di mercato",
                    "È vietato consultare i siti web delle altre aziende dello stesso comparto",
                    "L'analisi della concorrenza deve essere affidata a società di spionaggio industriale"
                ],
                "correctIndex": 0,
                "explanation": "Se progettate un portale medico, non guardate solo gli altri ospedali: guardate come Airbnb gestisce le prenotazioni o come Duolingo incentiva la costanza. Le soluzioni migliori arrivano spesso da settori affini."
            },
            {
                "question": "Perché un'interfaccia 'media' o 'sufficiente' non basta più per garantire la sopravvivenza commerciale di un servizio online?",
                "options": [
                    "Perché il costo di cambio (switching cost) sul web è quasi azzerato: basta un clic per passare a un concorrente che offre un'esperienza più scorrevole e meno frustrante",
                    "Perché i motori di ricerca cancellano i siti che non ottengono cinque stelle di recensioni",
                    "Perché gli utenti cambiano smartphone ogni mese rendendo obsolete le app",
                    "Perché la legge vieta la coesistenza di più di due fornitori per tipologia di servizio"
                ],
                "correctIndex": 0,
                "explanation": "Nel mondo fisico cambiare banca o supermercato costa fatica; nel digitale basta chiudere una scheda e aprirne un'altra. L'attrito (friction) è il killer numero uno delle conversioni."
            },
            {
                "question": "Qual è il rischio nell'effettuare un benchmark limitato unicamente ai concorrenti diretti del proprio mercato di nicchia?",
                "options": [
                    "Si rischia di copiare e perpetuare errori e mediocrità consolidate nel settore, perdendo l'opportunità di compiere un salto innovativo che ridefinisca gli standard",
                    "Si incorre in sanzioni penali per plagio artistico",
                    "Si perde l'accesso ai finanziamenti statali per la ricerca scientifica",
                    "I server cloud rifiutano di ospitare il database dei clienti"
                ],
                "correctIndex": 0,
                "explanation": "Se tutti i siti di noleggio auto fanno schifo e voi vi limitate a imitarli per sembrare 'del settore', create un altro sito mediocre. Chi rompe lo schema mutuando pattern da altri mondi sbaraglia il mercato."
            }
        ],
        "examQuiz": [
            {
                "question": "Un'azienda di fornitura energetica richiede 18 schermate e l'invio di documenti PDF via fax per sottoscrivere un contratto luce online, giustificandosi con: 'Tutti i fornitori di energia fanno così'. Quale errore strategico evidenzia la teoria di Stull?",
                "options": [
                    "Cecità settoriale: ignorano che l'utente confronta la loro procedura con l'onboarding in due minuti di Revolut o Apple, percependo il servizio come arcaico e ostile",
                    "Una corretta applicazione delle norme di sicurezza bancaria europea",
                    "Una strategia virtuosa per scoraggiare i clienti a basso reddito",
                    "Un problema tecnico legato alla larghezza di banda della rete internet"
                ],
                "correctIndex": 0,
                "explanation": "La mediocrità condivisa non è un alibi: il cliente confronta la fatica totale. Chi per primo semplifica radicalmente il processo (come fece Satispay o NeN) conquista gli utenti esasperati dalla burocrazia."
            },
            {
                "question": "In un'analisi di UX Benchmark, cosa distingue un 'Concorrente Diretto' da un 'Concorrente Analogico'?",
                "options": [
                    "Il concorrente diretto risolve lo stesso problema con la stessa offerta allo stesso target; il concorrente analogico affronta una sfida interattiva simile ma in un settore completamente differente",
                    "Il concorrente diretto usa il web e l'analogico usa solo manifesti cartacei",
                    "Il concorrente diretto ha sede nella stessa città e l'analogico all'estero",
                    "Non sussiste alcuna distinzione metodologica"
                ],
                "correctIndex": 0,
                "explanation": "Esempio brillante: se progettate la donazione del sangue, il concorrente diretto è un'altra associazione umanitaria; il concorrente analogico è un'app di delivery che vi mostra la mappa dell'autista in arrivo per placare l'ansia dell'attesa."
            },
            {
                "question": "Perché le interfacce con 'micro-attriti' invisibili subiscono una perdita di utenti lenta ma inesorabile (Silent Churn)?",
                "options": [
                    "Perché gli utenti raramente protestano: semplicemente si stancano, completano l'azione con fatica e alla prima alternativa migliore migrano altrove senza lasciare feedback",
                    "Perché il browser cancella i profili utente inattivi da più di una settimana",
                    "Perché le banche bloccano i pagamenti ricorrenti sui siti con poco traffico",
                    "Perché i motori di ricerca declassano automaticamente i siti con form lunghi"
                ],
                "correctIndex": 0,
                "explanation": "L'utente insoddisfatto quasi mai compila il modulo reclami: vota con i piedi (o con le dita). Il Silent Churn erode il fatturato all'insaputa del management finché non è troppo tardi."
            }
        ]
    },
    "stull-c4": {
        "quiz": [
            {
                "question": "Nel celebre modello cognitivo di Daniel Kahneman ('Pensieri lenti e veloci', 2011), quali sono le caratteristiche del 'Sistema 1'?",
                "options": [
                    "È veloce, automatico, impulsivo, emotivo, associativo e opera a bassissimo consumo energetico, fungendo da pilota automatico nella maggior parte delle azioni quotidiane",
                    "È lento, riflessivo, logico, calcolatore ed estremamente energivoro",
                    "È la parte del cervello che si attiva solo durante il sonno profondo",
                    "È un software di intelligenza artificiale installato sui computer quantistici"
                ],
                "correctIndex": 0,
                "explanation": "Il Sistema 1 è l'istinto biologico di sopravvivenza: non richiede concentrazione, riconosce sagome al volo e guida l'utente sul web attraverso euristiche immediate a sforzo zero."
            },
            {
                "question": "Quali sono invece le caratteristiche del 'Sistema 2' secondo Kahneman?",
                "options": [
                    "È lento, analitico, razionale, deliberato e faticoso: richiede concentrazione conscia e consuma rapidamente le riserve metaboliche di glucosio del cervello",
                    "È istintivo, emotivo e non richiede alcuna attenzione conscia",
                    "Opera a una velocità di elaborazione di un nanosecondo per operazione",
                    "Si occupa unicamente del controllo del battito cardiaco e della digestione"
                ],
                "correctIndex": 0,
                "explanation": "Il Sistema 2 è il pensatore cosciente: calcola 17x24, compila dichiarazioni dei redditi o analizza tabelle complesse. Poiché è pigro ed energivoro, il cervello cerca sempre di delegare tutto al Sistema 1."
            },
            {
                "question": "Perché si dice che 'Gli utenti navigano e decidono sul web con il Sistema 1'?",
                "options": [
                    "Perché la 'pigrizia cognitiva' naturale dell'essere umano spinge a risparmiare energia mentale: le persone scansionano con il pilota automatico e si irritano se costrette ad attivare il Sistema 2 per capire l'interfaccia",
                    "Perché il Sistema 2 è stato disattivato nei giovani dall'uso dei telefoni cellulari",
                    "Perché le leggi di internet vietano l'uso del ragionamento razionale durante lo shopping",
                    "Perché i computer non sono in grado di elaborare le richieste del Sistema 2"
                ],
                "correctIndex": 0,
                "explanation": "Nessuno vuole 'faticare' per comprare un paio di calzini. Se un sito richiede sforzo di decifrazione razionale (attivando il Sistema 2), la frizione cognitiva aumenta e l'utente desiste."
            },
            {
                "question": "Cosa si intende per 'Pigrizia Cognitiva' (Cognitive Miser) nella psicologia delle decisioni?",
                "options": [
                    "La tendenza biologica ed evolutiva della mente umana a preferire scorciatoie di pensiero (euristiche) e soluzioni rapide per preservare le limitate risorse di attenzione e concentrazione",
                    "Una malattia neurologica causata dall'eccessivo uso di videogiochi",
                    "L'incapacità degli studenti di memorizzare formule algebriche",
                    "Il rifiuto dei programmatori di commentare il proprio codice sorgente"
                ],
                "correctIndex": 0,
                "explanation": "Siamo 'avari cognitivi' per ragioni evolutive: il cervello pesa il 2% del corpo ma consuma il 20% delle calorie. Risparmiare pensiero su compiti banali era essenziale per sopravvivere nella savana."
            },
            {
                "question": "Come deve progettare un designer consapevole del funzionamento del Sistema 1?",
                "options": [
                    "Creando interfacce fluide e autoevidenti che comunichino attraverso convenzioni visive immediate, colori chiari e schemi noti, riducendo al minimo i bivi complessi",
                    "Inserendo problemi matematici prima di consentire l'accesso al carrello",
                    "Utilizzando testi scritti al contrario per stimolare l'attenzione del Sistema 2",
                    "Nascondendo i prezzi fino al momento del pagamento finale"
                ],
                "correctIndex": 0,
                "explanation": "Il design ideale parla direttamente al Sistema 1: pulsanti che sembrano pulsanti, percorsi ovvi e rassicuranti. Il Sistema 2 viene chiamato in causa solo quando serve una decisione ponderata cruciale."
            }
        ],
        "examQuiz": [
            {
                "question": "Un modulo di richiesta preventivo contiene 45 campi distribuiti su un'unica schermata con etichette scritte in gergo assicurativo ambiguo. Cosa accade nella mente del visitatore?",
                "options": [
                    "Il Sistema 1 si arrende immediatamente di fronte al sovraccarico cognitivo; il Sistema 2 valuta l'enorme dispendio energetico richiesto e decide razionalmente di abbandonare la pagina",
                    "Il Sistema 2 entra in estasi intellettuale e compila il modulo con entusiasmo",
                    "Il browser raddoppia la velocità di elaborazione della scheda video",
                    "L'utente richiede telefonicamente di raddoppiare il numero dei campi"
                ],
                "correctIndex": 0,
                "explanation": "Questa è la dinamica del rimbalzo (Bounce): il pilota automatico si schianta contro il muro di complessità e il decisore razionale sentenzia 'Non ne vale la pena', spingendo l'utente a chiudere la scheda."
            },
            {
                "question": "In quale specifica circostanza di progettazione è invece virtuoso forzare un rallentamento consapevole attivando il 'Sistema 2' dell'utente?",
                "options": [
                    "Nelle azioni critiche, irreversibili o ad alto rischio (es. 'Elimina definitivamente l'account', 'Trasferisci 10.000 euro'), richiedendo conferme esplicite o digitazione di codici per evitare errori impulsivi",
                    "Nella selezione del colore di una t-shirt durante lo shopping online",
                    "Al momento dell'accesso alla pagina iniziale del sito web",
                    "Durante la lettura di un articolo informativo di cronaca sportiva"
                ],
                "correctIndex": 0,
                "explanation": "È l'uso nobile dell'attrito (Friction deliberata): le azioni distruttive non devono essere troppo facili o il Sistema 1 le compirà per sbaglio. Una modale che fa riflettere salva l'utente dal disastro."
            },
            {
                "question": "Quale ruolo svolgono le euristiche visive (come l'Aesthetic-Usability Effect) nei processi decisionali del Sistema 1?",
                "options": [
                    "Forniscono indizi periferici rapidi: un'interfaccia visivamente pulita e armoniosa predispone positivamente il Sistema 1, inducendolo ad attendersi facilità d'uso e affidabilità complessiva",
                    "Inibiscono il funzionamento della memoria a lungo termine",
                    "Costringono l'utente ad acquistare prodotti non necessari",
                    "Modificano la risoluzione ottica della cornea dell'osservatore"
                ],
                "correctIndex": 0,
                "explanation": "L'abito fa il monaco per il Sistema 1: se la schermata è elegante, pulita e rassicurante, il cervello abbassa le difese e affronta l'interazione con fiducia e serenità."
            }
        ]
    },
    "stull-c5": {
        "quiz": [
            {
                "question": "Cosa descrive il celebre 'Modello di Kano' formulato da Noriaki Kano nel 1984?",
                "options": [
                    "Una teoria di sviluppo prodotto che classifica le caratteristiche e le funzionalità in categorie distinte in base a come influenzano la soddisfazione e la fedeltà del cliente",
                    "Un modello matematico per prevedere la velocità di obsolescenza dei computer portatili",
                    "Un algoritmo per calcolare la percentuale di sconto ottimale nei periodi di saldi",
                    "Un sistema di certificazione per le linee aeree internazionali"
                ],
                "correctIndex": 0,
                "explanation": "Il modello di Kano è una pietra miliare: dimostra che non tutte le funzionalità pesano allo stesso modo nella mente dell'utente, superando l'idea ingenua che 'più funzioni = più soddisfazione'."
            },
            {
                "question": "Quali sono le tre categorie fondamentali di attributi identificate dal Modello di Kano?",
                "options": [
                    "Attributi di Base (Must-be), Attributi Prestazionali (One-dimensional/Performance) e Attributi Deliziatori (Delighters/Attractive)",
                    "Economici, Medi e Costosi",
                    "Hardware, Software e Firmware",
                    "Iniziali, Intermedi e Avanzati"
                ],
                "correctIndex": 0,
                "explanation": "La tripartizione aurea: 1) Must-be (dati per scontati, generano rabbia se mancano), 2) Performance (più ce n'è meglio è, proporzionali), 3) Delighters (inattesi, generano entusiasmo)."
            },
            {
                "question": "Come si comportano gli 'Attributi di Base' (Must-be) nella psicologia del consumatore?",
                "options": [
                    "Sono requisiti minimi dati per scontati: la loro presenza non aumenta l'entusiasmo dell'utente, ma la loro assenza o malfunzionamento genera immediata insoddisfazione e rabbia furibonda",
                    "Sono funzioni futuristiche che lasciano il cliente a bocca aperta",
                    "Aumentano linearmente il prezzo di vendita del bene",
                    "Possono essere omessi senza che nessuno se ne accorga"
                ],
                "correctIndex": 0,
                "explanation": "Esempio classico: i freni in un'auto o la pulizia in una stanza d'albergo. Nessuno dice 'Che meraviglia, l'auto frena!'; ma se i freni non funzionano, l'esperienza è distrutta."
            },
            {
                "question": "Cosa caratterizza gli 'Attributi Prestazionali' (Performance) nel modello di Kano?",
                "options": [
                    "Hanno un impatto lineare e proporzionale sulla soddisfazione: più sono veloci, capienti o efficienti, maggiore è il gradimento dell'utente (e viceversa)",
                    "Generano sempre insoddisfazione a prescindere dal loro funzionamento",
                    "Vengono utilizzati unicamente nei primi tre giorni di vita del prodotto",
                    "Sono riservati esclusivamente ai mercati di lusso"
                ],
                "correctIndex": 0,
                "explanation": "Esempio: la durata della batteria dello smartphone o la velocità della connessione Wi-Fi. Più dura la batteria, più sono contento; meno dura, meno sono soddisfatto (relazione 1 a 1)."
            },
            {
                "question": "Cosa accade nel tempo a una funzionalità che oggi è considerata un 'Deliziatore' (Erosione del piacere)?",
                "options": [
                    "Subisce un inesorabile decadimento qualitativo: con il tempo e l'imitazione della concorrenza, la novità diventa un'aspettativa standard (prestazionale) e infine un requisito di base dato per scontato",
                    "Aumenta il suo valore economico all'infinito senza mai degradare",
                    "Viene dichiarata illegale dalle autorità di regolamentazione del mercato",
                    "Scompare spontaneamente dal codice sorgente dell'applicazione"
                ],
                "correctIndex": 0,
                "explanation": "L'adattamento edonico: quando uscì il Wi-Fi gratuito negli hotel o lo sblocco col volto negli smartphone, era un deliziatore magico. Oggi, se un hotel non ha il Wi-Fi, il cliente si infuria (è diventato un Must-be)."
            }
        ],
        "examQuiz": [
            {
                "question": "Un team di sviluppo per un'app bancaria decide di dedicare due mesi a creare animazioni 3D e avatar personalizzabili (Delighters), mentre la funzione di invio bonifico fallisce nel 20% dei casi. Quale errore di Kano ha commesso il management?",
                "options": [
                    "Hanno investito in deliziatori superficiali senza aver prima garantito la solidità ferrea degli attributi di base (Must-be), condannando il prodotto a un'insoddisfazione disastrosa",
                    "Una strategia corretta perché le animazioni distolgono l'attenzione dagli errori bancari",
                    "Una violazione delle norme contabili sulla tassazione dei servizi digitali",
                    "Un problema risolvibile raddoppiando il prezzo dell'abbonamento mensile"
                ],
                "correctIndex": 0,
                "explanation": "La gerarchia di Kano è inflessibile: non potete deliziare un utente a cui avete appena perso un bonifico. Prima si consolidano i Must-be al 100%, poi si ottimizzano le performance, e solo allora si delizia."
            },
            {
                "question": "Come si progetta un questionario secondo la metodologia di Noriaki Kano per classificare una determinata funzionalità?",
                "options": [
                    "Ponendo per ogni funzione due domande accoppiate: una funzionale ('Come ti sentiresti se ci fosse questa funzione?') e una disfunzionale ('Come ti sentiresti se NON ci fosse?'), incrociando le risposte in una matrice",
                    "Chiedendo unicamente agli utenti se desiderano pagare per la funzione",
                    "Facendo votare il consiglio di amministrazione dell'azienda a porte chiuse",
                    "Inviando un messaggio di testo con una valutazione da uno a dieci"
                ],
                "correctIndex": 0,
                "explanation": "La forza di Kano sta nella doppia domanda incrociata: se l'utente risponde 'Mi piacerebbe se ci fosse' e 'Non mi importerebbe se non ci fosse', la funzione è un Deliziatore; se dice 'Normale se c'è' e 'Non la tollererei se manca', è un Must-be."
            },
            {
                "question": "Quale fenomeno competitivo spiega perché le aziende tecnologiche sono costrette a innovare continuamente per mantenere la fedeltà dei clienti?",
                "options": [
                    "L'erosione temporale delle aspettative: ciò che ieri stupiva l'utente oggi è il minimo sindacale indispensabile, rendendo i deliziatori di ieri i must-be di oggi",
                    "La saturazione dello spazio di archiviazione sui server aziendali",
                    "L'obbligo contrattuale imposto dai produttori di microprocessori",
                    "La scadenza annuale dei brevetti sul software"
                ],
                "correctIndex": 0,
                "explanation": "La corsa della Regina Rossa: nel digitale bisogna correre solo per restare nello stesso posto. I competitor copiano le vostre idee geniali e il cliente si abitua, pretendendo sempre nuovi standard di eccellenza."
            }
        ]
    }
}

with open("scripts/stull_part1.json", "w", encoding="utf-8") as f:
    json.dump(stull_p1_p2, f, indent=2, ensure_ascii=False)

print(f"Salvata Parte 1 ({len(stull_p1_p2)} capitoli)")
