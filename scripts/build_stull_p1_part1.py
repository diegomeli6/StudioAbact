# build_stull_p1.py
# Capitoli 1-11 di Edward Stull - UX Design (Parte I: I Principi della UX)
import json

chapters = [
    # Cap 1
    {
        "id": "stull-c1",
        "number": 1,
        "partNum": 1,
        "partTitle": "Parte I — I Principi della UX",
        "title": "La UX è inevitabile",
        "anchorTitle": "MADGE LA MANICURE (PALMOLIVE, 1981)",
        "anchorText": "Negli spot Palmolive una casalinga immerge la mano in una sostanza verde e Madge le rivela: «Ci sei dentro fino al collo!». La campagna andò in onda per circa 30 anni e dimostra una verità: spesso non ci rendiamo conto della situazione in cui ci troviamo finché qualcun altro non ce lo fa notare. La sostanza verde in cui siamo costantemente immersi è la user experience: la UX non è opzionale, scaturisce inevitabilmente dall'uso di un qualunque prodotto o servizio.",
        "summary": """### La natura inevitabile della User Experience
La User Experience (UX) non è una funzionalità accessoria che si può scegliere di inserire o omettere a piacimento: **la UX esiste sempre**, scaturendo in modo automatico da qualunque contatto che una persona ha con un manufatto, un servizio, uno sportello o un software.
La sola vera distinzione progettuale ed economica è tra:
- **UX Intenzionale**: il risultato di ricerca attiva, ascolto empatico e progettazione deliberata dei bisogni dell'utente.
- **UX Accidentale**: l'esperienza lasciata al caso o alla sola comodità del codice interno, che si traduce in frizione, frustrazione, perdita di clienti e fallimento del prodotto.

### Etimologia e fondamenti storici
- **«User» (Utente)**: dal latino *uti* (utilizzare, praticare, trarre beneficio operativo).
- **«Experience» (Esperienza)**: dal latino *experientia* (conoscenza acquisita attraverso ripetuti tentativi sul campo).
- Il termine *User Experience* è stato coniato e formalizzato decenni fa da **Don Norman** (co-fondatore con Jakob Nielsen del Nielsen Norman Group), all'epoca vicepresidente dell'Advanced Technology Group di Apple, per comprendere non solo l'interfaccia a schermo, ma l'intera relazione della persona con il prodotto (dall'apertura della confezione all'assistenza clienti).

### I due grandi rami della disciplina
1. **UXD (User Experience Design)**: l'attività progettuale esecutiva che plasma l'architettura, le interfacce, i flussi e i comportamenti del prodotto.
2. **UXR (User Experience Research)**: l'attività scientifica e investigativa di raccolta dati:
   - *Ricerca primaria*: dati grezzi originali raccolti direttamente (interviste, osservazioni contestuali, test di usabilità).
   - *Ricerca secondaria*: analisi di dati già aggregati da terzi (report di settore, statistiche demografiche, studi di benchmark).
Ciò che accomuna ogni ruolo della UX è un unico principio cardine: **la centralità assoluta degli utenti reali**.""",
        "keyPoints": [
            "La UX non è opzionale: esiste in ogni prodotto e può essere solo intenzionale o accidentale.",
            "Etimologia: uti (utilizzare) + experientia (conoscenza tramite tentativi).",
            "Don Norman ha coniato il termine per abbracciare tutti gli aspetti del contatto tra persona e sistema.",
            "La disciplina si articola in UX Design (progettazione) e UX Research (ricerca primaria e secondaria)."
        ],
        "flashcards": [
            {
                "question": "Cosa dimostra la metafora di Madge la Manicure applicata alla UX?",
                "answer": "Che siamo costantemente immersi nell'esperienza utente senza rendercene conto, e che la UX scaturisce inevitabilmente da ogni interazione con un prodotto."
            },
            {
                "question": "Qual è la differenza fondamentale tra UX intenzionale e UX accidentale?",
                "answer": "L'UX intenzionale è frutto di ricerca deliberata e ascolto dei bisogni dell'utente; l'accidentale è il risultato casuale di scelte non coordinate che porta al fallimento."
            },
            {
                "question": "Chi ha coniato il termine 'User Experience' e quale era il suo scopo?",
                "answer": "Don Norman in Apple negli anni Novanta, per abbracciare l'intero ciclo di vita della relazione tra utente e prodotto, superando la sola interfaccia."
            }
        ],
        "quiz": [
            {
                "question": "Secondo Edward Stull, quale affermazione descrive la reale natura della User Experience (UX)?",
                "options": [
                    "È un servizio a pagamento che le aziende decidono facoltativamente di installare",
                    "È una proprietà inevitabile che scaturisce dall'uso di qualunque prodotto o servizio",
                    "È un algoritmo software per velocizzare la sincronizzazione dei dati sui server cloud",
                    "È una tecnica pubblicitaria ideata per aumentare i follower sui social network"
                ],
                "correctIndex": 1,
                "explanation": "La UX non si può evitare: ogni volta che una persona interagisce con un oggetto o software vive un'esperienza, positiva o frustrante."
            },
            {
                "question": "Qual è la distinzione decisiva tra 'UX intenzionale' e 'UX accidentale' illustrata nel testo?",
                "options": [
                    "L'UX intenzionale riguarda solo hardware Apple mentre l'accidentale riguarda sistemi Windows",
                    "L'intenzionale scaturisce da ricerca e progettazione deliberate; l'accidentale produce frustrazione e abbandono",
                    "L'intenzionale non richiede budget economico mentre l'accidentale comporta investimenti milionari",
                    "L'intenzionale è riservata ad accademici universitari mentre l'accidentale è adatta alle startup"
                ],
                "correctIndex": 1,
                "explanation": "Se non si progetta intenzionalmente per l'utente, l'esperienza finale sarà accidentale, caotica e fonte di perdita di clienti."
            },
            {
                "question": "Qual è il significato etimologico del termine latino 'experientia' da cui deriva 'esperienza'?",
                "options": [
                    "Capacità innata di dipingere paesaggi e ritratti ad olio",
                    "Conoscenza acquisita attraverso ripetuti tentativi pratici sul campo",
                    "Misurazione scientifica della velocità della luce nello spazio vuoto",
                    "Obbedienza incondizionata agli ordini dell'autorità costituita"
                ],
                "correctIndex": 1,
                "explanation": "Experientia deriva dalla radice di periculum/esperire, ovvero apprendere e acquisire conoscenza facendo cose e provando."
            },
            {
                "question": "Chi ha formalizzato storicamente il termine 'User Experience' e per quale motivo?",
                "options": [
                    "Tim Berners-Lee per descrivere il funzionamento dei protocolli ipertestuali HTTP",
                    "Don Norman per abbracciare tutti gli aspetti dell'interazione dell'individuo con il sistema",
                    "Bill Gates per spiegare l'architettura grafica delle finestre di Microsoft Windows",
                    "Steve Krug per descrivere i comportamenti di scansione visiva durante la navigazione"
                ],
                "correctIndex": 1,
                "explanation": "Don Norman coniò il termine in Apple per andare oltre la sola 'interfaccia' e includere packaging, ergonomia e supporto."
            },
            {
                "question": "Cosa differenzia la 'ricerca primaria' dalla 'ricerca secondaria' nel campo della UX Research (UXR)?",
                "options": [
                    "La primaria raccoglie dati originali direttamente dagli utenti, la secondaria analizza dati già esistenti",
                    "La primaria si svolge solo su campioni di bambini mentre la secondaria coinvolge gli adulti",
                    "La primaria utilizza software open source mentre la secondaria impiega brevetti industriali",
                    "Non sussiste alcuna reale distinzione metodologica tra le due tipologie di ricerca"
                ],
                "correctIndex": 0,
                "explanation": "La ricerca primaria produce nuovi dati sul campo (interviste, test); la secondaria sintetizza fonti e studi già pubblicati da terzi."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega perché la UX è inevitabile secondo Stull, illustra la metafora di Madge e definisci gli ambiti UXD e UXR.",
                "modelAnswer": "La UX è inevitabile perché ogni interazione con un artefatto genera percezioni e reazioni nell'utente; come nello spot di Madge Palmolive («ci sei dentro fino al collo»), l'esperienza esiste sempre, che ne siamo consapevoli o meno. Il compito dell'azienda è trasformare la UX da accidentale (lasciata al caso e foriera di fallimento) in intenzionale (guidata dai bisogni reali). La disciplina unisce UXD (User Experience Design, la progettazione esecutiva dell'interfaccia e dei flussi) e UXR (User Experience Research, l'indagine empirica tramite ricerca primaria con utenti e secondaria sui dati di settore)."
            }
        ]
    },

    # Cap 2
    {
        "id": "stull-c2",
        "number": 2,
        "partNum": 1,
        "partTitle": "Parte I — I Principi della UX",
        "title": "Voi non siete l'utente",
        "anchorTitle": "IL TORAFUGU DELLO YANGTZE",
        "anchorText": "Il pesce palla giapponese produce il sashimi considerato più delizioso in assoluto e, insieme, la tetrodotossina — una neurotossina letale senza antidoto. Solo alcune parti sono velenose. I team di progettazione sono come gli chef di sushi: con cura e precisione creano un'esperienza sublime; con superficialità avvelenano gli utenti. Il veleno, nella metafora di Stull, è il preconcetto che introduciamo nel progetto: opinioni radicate, scorciatoie cognitive e la presunzione di sapere cosa desiderano gli altri.",
        "summary": """### L'assioma fondante della comunità UX
L'antidoto al veleno del preconcetto è la massima più celebre e rigorosa della disciplina:
> **«Voi non siete l'utente» (You are not the user).**

### La trappola dell'auto-referenzialità
I progettisti e gli sviluppatori cadono continuamente nella trappola di credere che le proprie preferenze corrispondano a quelle dell'utente finale:
- Se il designer ama l'iPhone, tende a ignorare i comportamenti degli utenti Android.
- Se ha una vista perfetta, tende a sottovalutare i contrasti deboli per chi è ipovedente.
- Se conosce intimamente l'architettura del software, non comprende lo smarrimento di chi lo apre per la prima volta (*Maledizione della conoscenza*).

### Il caso studio di 'Fishes'R'Us'
Stull smonta l'illusione anche quando il progettista appartiene demograficamente al target.
Immaginiamo un'applicazione commissionata da una catena ittica (*Fishes'R'Us*) per insegnare a cucinare il pesce:
- Il designer pensa: *'Io amo il pesce, cucino il pesce tre volte a settimana, quindi io sono l'utente!'*.
- **Errore madornale**: chi progetta l'applicazione conosce la logica del database, sa cosa succederà al clic successivo e non ha l'ansia di bruciare la cena.
- **Definizione essenziale**: *«L'utente è una persona che ha un'esperienza»*. È necessario un utente perché ci sia un'esperienza, ed è necessaria un'esperienza perché ci sia un utente: i due concetti sono inscindibili. Non possiamo mai davvero essere utenti di qualcosa che abbiamo disegnato noi stessi.

### L'intersezione magica: Bisogni dell'Utente vs Obiettivi di Business
Il valore del design non consiste nel compiacere i gusti del designer:
- Da un lato vi sono i **Bisogni dell'Utente** (risolvere un problema, risparmiare tempo, non sentirsi frustrati).
- Dall'altro vi sono gli **Obiettivi dell'Azienda** (vendere prodotti, acquisire lead, ridurre i costi di supporto).
- Il compito esclusivo della UX è **costruire esperienze significative nell'area di sovrapposizione** tra queste due sfere.""",
        "keyPoints": [
            "Assioma cardinale: 'Voi non siete l'utente'; il designer non può mai vivere l'esperienza con gli occhi vergini di un estraneo.",
            "La metafora del Torafugu: i preconcetti non testati sono veleno letale per il successo del prodotto.",
            "L'esempio Fishes'R'Us dimostra che appartenere al target demografico non equivale a essere l'utente del proprio sistema.",
            "La UX vincente si colloca esattamente all'intersezione tra bisogni reali dell'utente e obiettivi dell'azienda."
        ],
        "flashcards": [
            {
                "question": "Cosa rappresenta il veleno del pesce palla Torafugu nella metafora di Stull?",
                "answer": "I preconcetti, i bias cognitivi e le supposizioni non verificate che il team riversa nel progetto avvelenando l'esperienza utente."
            },
            {
                "question": "Perché anche un designer che ama cucinare il pesce non è l'utente dell'app Fishes'R'Us?",
                "answer": "Perché possiede la 'maledizione della conoscenza': sa già come funziona il sistema e non può avere l'esperienza ingenua di chi lo usa per la prima volta."
            },
            {
                "question": "Dove deve collocarsi la progettazione UX di successo?",
                "answer": "Nell'area di intersezione armonica tra i bisogni concreti dell'utente e gli obiettivi economici dell'azienda."
            }
        ],
        "quiz": [
            {
                "question": "Cosa stabilisce l'assioma universale della comunità UX «Voi non siete l'utente»?",
                "options": [
                    "I progettisti non possono mai valutare l'interfaccia con gli occhi neutrali di chi non l'ha costruita",
                    "Gli sviluppatori di software non hanno il diritto di navigare sul web durante l'orario di ufficio",
                    "Gli utenti registrati non devono mai entrare in contatto diretto con il team di sviluppo",
                    "Un sito internet deve essere progettato unicamente per consumatori residenti all'estero"
                ],
                "correctIndex": 0,
                "explanation": "Chi progetta un sistema ne conosce i meccanismi interni e non può simulare l'esperienza ingenua di un utente reale."
            },
            {
                "question": "Nella metafora del pesce Torafugu descritta nel Capitolo 2, a cosa corrisponde la letale tetrodotossina?",
                "options": [
                    "Agli attacchi hacker mirati a sottrarre i dati di pagamento delle carte di credito",
                    "Ai preconcetti, supposizioni e bias personali che il team inserisce senza verificarli con la ricerca",
                    "Ai linguaggi di programmazione obsoleti che rallentano il caricamento delle pagine web",
                    "Alla mancata conformità dei server rispetto alle normative europee sulla privacy"
                ],
                "correctIndex": 1,
                "explanation": "Il veleno è il pregiudizio non testato: credere che ciò che piace a noi piaccia a tutti avvelena l'esperienza dell'utente."
            },
            {
                "question": "Perché l'esempio di 'Fishes'R'Us' smonta la convinzione di molti designer di 'essere il target'?",
                "options": [
                    "Perché il pesce crudo giapponese non può essere venduto tramite piattaforme di commercio elettronico",
                    "Perché anche se il designer cucina pesce, la conoscenza dell'app gli impedisce di provarne l'esperienza reale",
                    "Perché le ricette culinarie devono essere scritte unicamente da chef professionisti stellati",
                    "Perché l'utente dell'applicazione utilizza esclusivamente schermi touch screen da smartphone"
                ],
                "correctIndex": 1,
                "explanation": "Conoscere il funzionamento del sistema impedisce al designer di provare lo smarrimento, i dubbi e il contesto reale dell'utente."
            },
            {
                "question": "Secondo Edward Stull, da quale incontro scaturisce la definizione essenziale di 'utente'?",
                "options": [
                    "Dall'acquisto formale di un abbonamento mensile tramite carta di credito",
                    "Dalla relazione inscindibile per cui serve un utente per avere un'esperienza e un'esperienza per avere un utente",
                    "Dalla compilazione di un questionario cartaceo di gradimento inviato per posta",
                    "Dalla memorizzazione del codice fiscale all'interno del database centrale dell'azienda"
                ],
                "correctIndex": 1,
                "explanation": "Stull definisce l'utente come 'una persona che ha un'esperienza': i due termini sono co-dipendenti e inseparabili."
            },
            {
                "question": "Quale rischio si corre privilegiando unicamente gli obiettivi dell'azienda a discapito dei bisogni dell'utente?",
                "options": [
                    "Il sito subisce una perdita di clienti per via di un'esperienza ostile e frustrante",
                    "I server web aumentano automaticamente la memoria RAM a disposizione dei visitatori",
                    "I motori di ricerca bloccano l'indicizzazione dei video multimediali del portale",
                    "L'azienda riceve una sanzione amministrativa da parte della camera di commercio"
                ],
                "correctIndex": 0,
                "explanation": "Se l'azienda impone solo i suoi scopi (es. popup aggressivi o ostacoli), l'utente si sente sfruttato e fugge verso i concorrenti."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega il principio 'Voi non siete l'utente', illustra la metafora del Torafugu e analizza il caso Fishes'R'Us.",
                "modelAnswer": "L'assioma 'Voi non siete l'utente' ricorda che nessun designer può guardare una propria creazione con l'ingenuità e i modelli mentali di un utente estraneo. La metafora del Torafugu (pesce palla) evidenzia che come lo chef deve isolare il veleno della tetrodotossina per creare un piatto sublime, così il team UX deve isolare il veleno dei propri preconcetti e bias personali per non avvelenare il prodotto. Il caso Fishes'R'Us dimostra che anche appartenere al target (amare e cucinare il pesce) non fa del designer un utente: chi progetta conosce l'architettura software, non ha dubbi su dove cliccare e non vive la pressione operativa del vero fruitore."
            }
        ]
    },

    # Cap 3
    {
        "id": "stull-c3",
        "number": 3,
        "partNum": 1,
        "partTitle": "Parte I — I Principi della UX",
        "title": "Siete in competizione con tutto",
        "anchorTitle": "I GIOCHI OLIMPICI",
        "anchorText": "Dal 1896 più di 100 discipline sono state escluse dai Giochi Olimpici: il duello con pistole, il salto in alto da fermo, il tiro al piccione vivo (Parigi 1900), le gare di barche a motore. Combinando le preferenze di 200 comitati nazionali, miliardi di spettatori e spazi televisivi limitati, il Comitato Olimpico deve tagliare senza pietà ciò che non compete ai massimi livelli. Nello stesso identico modo, il vostro prodotto non compete solo con i rivali diretti, ma con ogni stimolo che reclama l'attenzione dell'utente.",
        "summary": """### La vera natura della competizione: l'economia dell'attenzione
L'errore più ingenuo nel business digitale è definire i concorrenti in modo miope:
- Se create un'app di meditazione, non siete in competizione solo con le altre app di meditazione.
- Siete in competizione con **Netflix, TikTok, un messaggio WhatsApp, una tazza di caffè, il sonno, la pigrizia o una passeggiata all'aria aperta**.
Nel mondo contemporaneo, la risorsa più scarsa e contesa dell'essere umano non è il denaro, ma **l'attenzione e il tempo cognitivo**.

### Il Costo Opportunità e il Trade-Off dell'Utente
Ogni volta che un utente decide di dedicare un minuto al vostro sito o alla vostra applicazione, compie una rinuncia: rinuncia a fare qualsiasi altra cosa in quel medesimo istante (*Opportunity Cost*).
Se l'interfaccia si dimostra faticosa, lenta o respingente, l'utente non passa al concorrente diretto: **fa semplicemente qualcos'altro**.

### Appassionarsi vs Adeguarsi a una soluzione
Stull introduce una distinzione psicologica fondamentale per il design d'esperienza:
1. **Adeguarsi a una soluzione**:
   - L'utente usa il prodotto solo perché obbligato (es. il software gestionale contabile imposto dall'azienda o il portale fiscale statale).
   - L'utente sopporta la cattiva UX per necessità, ma al primo spiraglio di alternativa lo abbandonerà con risentimento accumulato.
2. **Appassionarsi a una soluzione**:
   - L'utente sperimenta piacere, facilità e risonanza emotiva.
   - Il prodotto non si limita a svolgere il compito, ma elimina l'ansia e fa sentire la persona competente ed efficace.
L'obiettivo della vera UX non è costringere le persone ad adeguarsi al sistema, ma concepire sistemi a cui le persone desiderino appassionarsi spontaneamente.""",
        "keyPoints": [
            "La competizione sul digitale è totale: non solo rivali diretti, ma qualsiasi stimolo che contende il tempo dell'utente.",
            "L'attenzione e il tempo cognitivo sono le risorse umane più scarse nell'economia contemporanea.",
            "Il costo opportunità: usare il vostro prodotto significa rinunciare a fare qualsiasi altra cosa.",
            "Differenza tra adeguarsi (subire una cattiva UX per obbligo) e appassionarsi (adottare con entusiasmo un'esperienza fluida)."
        ],
        "flashcards": [
            {
                "question": "Cosa dimostra l'esempio delle discipline escluse dai Giochi Olimpici?",
                "answer": "Che l'attenzione e il tempo del pubblico sono finiti: per far spazio a ciò che vale davvero, tutto ciò che non regge la competizione globale viene scartato."
            },
            {
                "question": "Qual è la risorsa più scarsa per cui combattono i prodotti digitali moderni?",
                "answer": "L'attenzione e il tempo cognitivo dell'essere umano, costantemente conteso da mille distrazioni."
            },
            {
                "question": "Che differenza c'è fra 'adeguarsi' e 'appassionarsi' a una soluzione software?",
                "answer": "Adeguarsi significa tollerare un sistema ostile per obbligo lavorativo; appassionarsi significa usarlo con piacere e naturalezza grazie a un'eccellente UX."
            }
        ],
        "quiz": [
            {
                "question": "Secondo Edward Stull nel Capitolo 3, con chi è davvero in competizione un prodotto digitale?",
                "options": [
                    "Esclusivamente con le tre aziende leader che vendono esattamente lo stesso identico servizio",
                    "Con qualsiasi stimolo o attività che contende l'attenzione e il tempo limitato dell'utente",
                    "Unicamente con i motori di ricerca e i provider di connettività internet",
                    "Con i produttori di componenti hardware e schede grafiche per personal computer"
                ],
                "correctIndex": 1,
                "explanation": "La competizione nell'economia dell'attenzione è globale: un'app contende il tempo a social, email, hobby e vita quotidiana."
            },
            {
                "question": "Cosa indica il concetto economico di 'Costo Opportunità' applicato alla User Experience?",
                "options": [
                    "Il costo monetario per acquistare una licenza software commerciale",
                    "Il valore delle attività alternative a cui l'utente rinuncia decidendo di usare il nostro prodotto",
                    "La percentuale di sconto offerta durante le campagne promozionali del Black Friday",
                    "Il costo energetico per alimentare i server durante il caricamento del database"
                ],
                "correctIndex": 1,
                "explanation": "Usare il nostro sito costa tempo che l'utente potrebbe dedicare ad altro: se la UX è faticosa, il costo opportunità diventa insostenibile."
            },
            {
                "question": "Cosa caratterizza un utente che 'si adegua' a un software anziché 'appassionarsi'?",
                "options": [
                    "Utilizza il software con entusiasmo consigliandolo spontaneamente a tutti i suoi colleghi",
                    "Sopporta l'interfaccia contorta solo perché obbligato dall'azienda, pronto ad abbandonarla appena possibile",
                    "Partecipa attivamente ai test di usabilità per aiutare i programmatori a riscrivere il codice",
                    "Disabilita volontariamente gli aggiornamenti di sicurezza del sistema operativo"
                ],
                "correctIndex": 1,
                "explanation": "Chi si adegua è un utente prigioniero: sopporta la cattiva UX per costrizione, accumulando frustrazione."
            },
            {
                "question": "Perché le discipline olimpiche insolite (come il tiro al piccione) sono state progressivamente eliminate dai Giochi?",
                "options": [
                    "Perché il tempo e l'attenzione di atleti, spettatori e televisioni sono risorse finite e preziose",
                    "A causa del divieto universale di praticare sport all'aperto introdotto all'inizio del Novecento",
                    "Perché gli atleti si rifiutavano di gareggiare senza retribuzioni economiche preventive",
                    "Perché i moderni cronometri digitali non consentono di misurare gare acquatiche"
                ],
                "correctIndex": 0,
                "explanation": "La scarsità di tempo e attenzione impone una selezione spietata: solo ciò che genera reale valore e coinvolgimento resiste."
            },
            {
                "question": "Quale obiettivo prioritario deve porsi la UX per vincere la competizione nell'economia dell'attenzione?",
                "options": [
                    "Aumentare il numero di notifiche push giornaliere per interrompere continuamente l'utente",
                    "Ridurre al minimo l'attrito cognitivo e far sentire l'utente competente, efficace e soddisfatto",
                    "Obbligare l'utente a condividere l'applicazione sui propri canali social prima di accedere",
                    "Allungare artificialmente i percorsi di navigazione per incrementare le visualizzazioni pubblicitarie"
                ],
                "correctIndex": 1,
                "explanation": "Rispettare il tempo dell'utente offrendo un'esperienza fluida e gratificante è l'unico modo per farsi scegliere spontaneamente."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega il concetto 'Siete in competizione con tutto' collegandolo all'economia dell'attenzione e alla differenza tra adeguarsi e appassionarsi a una soluzione.",
                "modelAnswer": "Stull dimostra che un prodotto digitale non compete solo con i rivali di categoria, ma con ogni stimolo che reclama l'attenzione finita dell'utente (social, messaggi, svago, sonno). Il costo opportunità misura ciò a cui l'utente rinuncia dedicandoci del tempo: se l'esperienza è lenta o frustrante, il costo supera il beneficio. La distinzione è tra 'adeguarsi' (l'utente sopporta un software ostile perché imposto dal datore di lavoro, accumulando risentimento) e 'appassionarsi' (l'utente sperimenta piacere, fluidità e si sente competente, adottando spontaneamente la soluzione)."
            }
        ]
    }
]

print("Saving Stull Part 1 (Chapters 1 to 3)...")
with open('stull_p1_part_1to3.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)
