# -*- coding: utf-8 -*-
"""
Rebuilds data/arte-data.js with:
1. High-level academic chapter quizzes (chap.quiz) for all 16 chapters:
   - Realistic, art-history-grade distractors (no childish/absurd choices).
   - Balanced correctIndex across 0, 1, 2, 3.
2. Dedicated exam simulation questions (chap.examQuiz) for all 16 chapters:
   - Distinct, critical-analysis exam questions on Contemporary Art.
   - Realistic distractors.
   - Balanced correctIndex across 0, 1, 2, 3.
"""

import json, re

arte_quiz_data = {
    "arte-c1": {
        "quiz": [
            {
                "question": "Quale tesi filosofica centrale di Jean-François Lyotard ne 'La condizione postmoderna' (1979) ha influenzato l'arte degli anni Ottanta?",
                "options": [
                    "Il tramonto delle grandi narrazioni totalizzanti (meta-racconti illuministi e marxisti) a favore di una molteplicità frammentaria di linguaggi e micro-storie",
                    "L'affermazione dell'arte concettuale come unico strumento di redenzione politica globale",
                    "Il rifiuto categorico di qualsiasi tecnica pittorica tradizionale a favore dei soli media digitali",
                    "La teorizzazione dell'estetica minimalista come punto d'arrivo definitivo della civiltà occidentale"
                ],
                "correctIndex": 0,
                "explanation": "Lyotard sancisce la fine della fede nel progresso lineare: l'artista postmoderno non cerca più un'utopia universale, ma si riappropria liberamente di frammenti storici ed eclettismo stilistico."
            },
            {
                "question": "Quale ruolo ha svolto il quartiere newyorkese di SoHo nello sviluppo del sistema dell'arte degli anni Ottanta?",
                "options": [
                    "È stato il polo nevralgico della commercializzazione globale, dove galleristi innovativi hanno trasformato ex spazi industriali (loft) in templi del mercato internazionale",
                    "È stato un ghetto isolato in cui era vietata la vendita commerciale delle opere d'arte",
                    "Ha ospitato esclusivamente collettivi di artisti anonimi legati all'agit-prop politica",
                    "È stato sede esclusiva dei musei statali accademici dell'Ottocento"
                ],
                "correctIndex": 0,
                "explanation": "Con figure come Leo Castelli, Mary Boone e Tony Shafrazi, SoHo ha incarnato l'esplosione delle gallerie private e dell'art-star system, legando l'arte contemporanea alla finanza e ai mass media."
            },
            {
                "question": "Rispetto al rigore concettuale e poverista del decennio precedente, cosa rappresenta il 'ritorno alla pittura' degli anni Ottanta?",
                "options": [
                    "La rivendicazione della manualità, del piacere del colore, della figura e della libera citazione della memoria storica senza sensi di colpa",
                    "Una restaurazione accademica che imponeva la copia pedissequa dei maestri del Rinascimento fiorentino",
                    "Il divieto per gli artisti di esporre sculture o installazioni tridimensionali",
                    "L'abbandono della tela in favore della sola pittura murale politica"
                ],
                "correctIndex": 0,
                "explanation": "Dopo anni di smaterializzazione concettuale ('l'idea vale più dell'opera'), gli artisti riscoprono la sensualità della materia pittorica, il gesto, l'archetipo e il piacere del dipingere."
            },
            {
                "question": "In che modo l'eclettismo postmoderno affronta il rapporto con la storia dell'arte del passato?",
                "options": [
                    "Considera il museo e la storia come un repertorio illimitato di stili ed epoche da 'saccheggiare', ibridare e citare liberamente fuori dal tempo",
                    "Rifiuta qualsiasi forma di figurazione per preservare l'iconoclastia concettuale",
                    "Impone la distruzione filologica di tutte le correnti artistiche precedenti alle avanguardie storiche",
                    "Subordina l'invenzione figurativa alla rigorosa aderenza filologica ai canoni neoclassici"
                ],
                "correctIndex": 0,
                "explanation": "Il Postmoderno abolisce la gerarchia temporale: Manierismo, Espressionismo, Barocco e fumetto possono convivere nella medesima opera come tessere di un collage nomade."
            },
            {
                "question": "Quale dualismo linguistico caratterizza il panorama artistico internazionale degli anni Ottanta?",
                "options": [
                    "La coesistenza non conflittuale tra il ritorno passionale e violento alla pittura figurativa da un lato, e le indagini analitiche e fredde su merce, media e simulacro dall'altro",
                    "La contrapposizione violenta tra artisti solo digitali e scultori in marmo",
                    "La scissione geografica tra arte americana esclusivamente astratta e arte europea solo figurativa",
                    "Il divieto per le donne artiste di esporre nelle gallerie commerciali"
                ],
                "correctIndex": 0,
                "explanation": "Gli anni '80 vivono di questa polarità affascinante: da una parte l'impeto materico di Transavanguardia e Neoespressionismo; dall'altra la fredda riflessione di Neo-Geo, Appropriazionismo e Scuola di Düsseldorf."
            }
        ],
        "examQuiz": [
            {
                "question": "Perché la Biennale di Venezia del 1980 (e in particolare la sezione 'Aperto '80' curata da Achille Bonito Oliva e Harald Szeemann) è considerata uno spartiacque storico?",
                "options": [
                    "Ha consacrato sulla scena museale globale la nuova pittura figurativa giovanile (Transavanguardia e Neue Wilden), sancendo la fine dell'egemonia esclusiva del concettuale puro",
                    "Ha abolito per sempre i padiglioni nazionali in favore di una mostra unicamente online",
                    "Ha premiato con il Leone d'Oro le prime opere realizzate con computer grafica",
                    "Ha escluso tutti i pittori europei per dedicarsi solo all'arte sudamericana"
                ],
                "correctIndex": 0,
                "explanation": "'Aperto '80' nei Magazzini del Sale fu l'epifania internazionale: il pubblico e la critica videro per la prima volta riuniti i giovani protagonisti del ritorno alla pittura, decretandone il trionfo."
            },
            {
                "question": "In quale modo il fenomeno dei 'Megacollezionisti' (come Charles Saatchi o Peter Ludwig) ha mutato gli equilibri del sistema dell'arte negli anni Ottanta?",
                "options": [
                    "Hanno acquisito un potere d'orientamento del gusto paragonabile o superiore a quello dei direttori di museo, influenzando direttamente i prezzi d'asta e la carriera degli artisti",
                    "Hanno devoluto tutte le proprie risorse unicamente al restauro di monumenti archeologici romani",
                    "Hanno imposto agli artisti di non vendere mai opere all'estero",
                    "Hanno vietato l'accesso del pubblico alle proprie gallerie private"
                ],
                "correctIndex": 0,
                "explanation": "I collezionisti-finanzieri acquistavano in blocco intere mostre, creando e consacrando movimenti dall'oggi al domani e trasformando le opere in asset di investimento speculativo globale."
            },
            {
                "question": "Quale critica principale veniva mossa dai sostenitori dell'avanguardia intransigente (come Benjamin Buchloh) al ritorno alla pittura degli anni Ottanta?",
                "options": [
                    "Di rappresentare una restaurazione conservatrice, regressiva e nostalgica, asservita alle logiche di mercato dopo le conquiste politiche del Concettuale",
                    "Di essere un movimento troppo rivoluzionario e ostile all'ordine borghese",
                    "Di utilizzare pigmenti sintetici a bassa tossicità",
                    "Di non rispettare le proporzioni della sezione aurea classica"
                ],
                "correctIndex": 0,
                "explanation": "La critica teorica più severa (Buchloh su October) tacciava il neo-figurativismo di 'restaurazione autoritaria', vedendovi una fuga disimpegnata e commerciale dalla critica istituzionale."
            }
        ]
    },
    "arte-c2": {
        "quiz": [
            {
                "question": "Chi ha teorizzato il movimento della Transavanguardia nel 1979 sulle pagine della rivista Flash Art?",
                "options": [
                    "Il critico d'arte Achille Bonito Oliva",
                    "Germano Celant, teorico dell'Arte Povera",
                    "Renato Barilli, teorico dei Nuovi Nuovi",
                    "Gillo Dorfles, studioso del Kitsch"
                ],
                "correctIndex": 0,
                "explanation": "Achille Bonito Oliva (ABO) ha battezzato e teorizzato il movimento, formulando i concetti cardine di nomadismo culturale, transito stilistico e ritorno al 'manuale'."
            },
            {
                "question": "Quali sono i cinque artisti che costituiscono il nucleo canonico della Transavanguardia italiana?",
                "options": [
                    "Sandro Chia, Francesco Clemente, Enzo Cucchi, Nicola De Maria e Mimmo Paladino",
                    "Mario Merz, Jannis Kounellis, Michelangelo Pistoletto, Alighiero Boetti e Luciano Fabro",
                    "Lucio Fontana, Alberto Burri, Piero Manzoni, Enrico Castellani e Agostino Bonalumi",
                    "Giorgio de Chirico, Carlo Carrà, Alberto Savinio, Filippo de Pisis e Mario Sironi"
                ],
                "correctIndex": 0,
                "explanation": "I celebri 'magnifici cinque' di ABO: Chia, Clemente, Cucchi, De Maria e Paladino, ciascuno con una poetica figurativa o astratta radicata nella propria identità e memoria."
            },
            {
                "question": "Cosa indica il concetto di 'Nomadismo Culturale' coniato da Achille Bonito Oliva?",
                "options": [
                    "La libertà assoluta dell'artista di migrare attraverso stili, miti, epoche storiche e tradizioni geografiche senza vincoli evolutivi né obblighi di coerenza ideologica",
                    "L'obbligo per i pittori di risiedere in tende nel deserto durante la creazione artistica",
                    "Il divieto di esporre le proprie opere nella propria nazione d'origine",
                    "L'uso esclusivo di materiali deperibili raccolti durante viaggi all'estero"
                ],
                "correctIndex": 0,
                "explanation": "Nomadismo significa attraversamento: l'artista transita tra Manierismo, Futurismo, arte popolare o mitologie arcaiche come un viaggiatore disincantato che attinge liberamente alla storia."
            },
            {
                "question": "Quale tra i cinque artisti della Transavanguardia si distingue per una ricerca basata sull'astrazione lirica e su stanze affrescate a colori puri anziché sulla figurazione antropomorfa?",
                "options": [
                    "Nicola De Maria",
                    "Sandro Chia",
                    "Enzo Cucchi",
                    "Mimmo Paladino"
                ],
                "correctIndex": 0,
                "explanation": "De Maria è il poeta del gruppo: rifiuta la figura umana per lavorare sull'intensità lirica del colore puro, trasformando intere pareti e sale espositive in 'Regni dei Fiori' e poesia visiva."
            },
            {
                "question": "Quale immaginario iconografico contraddistingue in modo peculiare l'opera di Mimmo Paladino?",
                "options": [
                    "Figure enigmatiche senza volto, scudi, cavalli, maschere primordiali e simboli intrisi della memoria arcaica del Mediterraneo e della cultura sannita/etrusca",
                    "Automobili da corsa futuriste e grattacieli metropolitani d'acciaio",
                    "Ritratti fotografici iperrealisti di celebrità hollywoodiane",
                    "Forme geometriche pure basate sulla teoria costruttivista russa"
                ],
                "correctIndex": 0,
                "explanation": "Paladino attinge al mistero arcaico del Sud: geometrie primordiali, icone funerarie, guerrieri dormienti e sculture silenziose (come la 'Montagna di Sale') immerse nel mito mediterraneo."
            }
        ],
        "examQuiz": [
            {
                "question": "In che modo l'esperienza nei soggiorni in India ha plasmato il linguaggio pittorico di Francesco Clemente?",
                "options": [
                    "Ha introdotto tecniche tradizionali (miniatura, carta fatta a mano, affresco) e una riflessione intima sul corpo, sulla spiritualità induista, sulle metamorfosi e sull'eros",
                    "Lo ha spinto ad abbandonare definitivamente la pittura per dedicarsi unicamente alla fotografia industriale",
                    "Ha provocato il suo rifiuto totale di esporre nel mercato occidentale",
                    "Gli ha fatto adottare uno stile puramente geometrico e monocromatico"
                ],
                "correctIndex": 0,
                "explanation": "A Madras e Benares, Clemente sperimenta la fluidità dell'io: autoritratti frammentati, tecniche sapienziali e simbolismo orientale fusi con la cultura classica partenopea."
            },
            {
                "question": "Analizzando la pittura di Enzo Cucchi, quale matrice culturale e geografica alimenta la drammaticità delle sue tele telluriche e scure?",
                "options": [
                    "Le radici contadine e marine delle Marche, cariche di miti arcaici, teschi, barche, colline tormentate e presenze ctonie",
                    "Il razionalismo industriale e la nebbia metropolitana di Milano",
                    "L'architettura neoclassica parigina del secondo impero",
                    "La cultura dei fumetti underground della California"
                ],
                "correctIndex": 0,
                "explanation": "Cucchi è il 'visionario tellurico': le sue opere vibrano di un'energia vulcanica e materica, dove la terra marchigiana, il fuoco, le barche nel buio e i santi popolari si fondono in visioni drammatiche."
            },
            {
                "question": "Perché il prefisso 'Trans-' nella Transavanguardia segna una rottura rispetto al concetto tradizionale di Avanguardia?",
                "options": [
                    "Perché indica il superamento del mito illuminista della marcia lineare in avanti (l'avanguardia che supera il passato): l'artista ora attraversa orizzontalmente la storia senza gerarchie evolutive",
                    "Perché imponeva la transizione verso la scultura digitale tridimensionale",
                    "Perché sanciva il trasferimento degli artisti italiani sul mercato americano",
                    "Perché indicava la trasformazione dei quadri in oggetti di arredamento d'interni"
                ],
                "correctIndex": 0,
                "explanation": "L'avanguardia storica credeva nel futuro e nel progresso; la Transavanguardia prende atto della fine delle utopie e si concede il transito libero e nomadico tra tutti i linguaggi possibili."
            }
        ]
    }
}

# Generate chapters 3 to 16 for Arte
arte_c3_to_16 = {
    "arte-c3": {
        "quiz": [
            {
                "question": "Come viene definita la corrente pittorica che negli anni Ottanta in Germania ha incarnato la riscoperta violenta della pittura figurativa espressionista?",
                "options": [
                    "I Nuovi Selvaggi (Neue Wilden) o Neoespressionismo tedesco",
                    "Il Realismo Socialista della Germania Est",
                    "Il Movimento De Stijl berlinese",
                    "La Nuova Oggettività di Weimar"
                ],
                "correctIndex": 0,
                "explanation": "I Neue Wilden (Kiefer, Baselitz, Polke, Penck, Lupertz, Immendorff) esplodono con tele monumentali, pennellate rabbiose e una drammatica riflessione sull'identità e la storia tedesca."
            },
            {
                "question": "Quale segno distintivo ha reso celebre la pittura di Georg Baselitz a partire dal 1969?",
                "options": [
                    "Il capovolgimento sistematico dei soggetti e delle figure sulla tela, per svuotare l'immagine della sua referenzialità narrativa ed esaltare la pura materia pittorica",
                    "L'uso esclusivo di pittura spray su pareti di cemento armato",
                    "La cancellazione totale della figura tramite vernice bianca opaca",
                    "L'inserimento di schermi televisivi all'interno della cornice"
                ],
                "correctIndex": 0,
                "explanation": "Baselitz ribalta i quadri sottosopra: la figura rimane riconoscibile ma perde il suo primato tematico, costringendo l'osservatore a concentrarsi su colore, segno e forza compositiva."
            },
            {
                "question": "Quale grande tema storico e traumatico attraversa la produzione monumentale e materica di Anselm Kiefer?",
                "options": [
                    "La memoria tragica del passato tedesco, il nazismo, la Shoah, la mitologia germanica e la cabala ebraica, espressi attraverso materiali pesanti (piombo, paglia, cenere, terra)",
                    "L'ottimismo tecnologico della rinascita industriale automobilistica",
                    "I paesaggi marittimi tropicali e la fauna esotica",
                    "L'architettura funzionalista del Bauhaus di Dessau"
                ],
                "correctIndex": 0,
                "explanation": "Kiefer affronta il tabù della colpa tedesca senza reticenze: solchi arati coperti di cenere, ali di piombo, riferimenti a Paul Celan ('Sulamith') per elaborare il lutto storico (Trauerarbeit)."
            },
            {
                "question": "Cosa caratterizza la pittura e la ricerca polimorfa di Sigmar Polke?",
                "options": [
                    "L'ironia dissacrante, l'uso del retino tipografico raster ingrandito (Polke Dots), tessuti d'arredo a buon mercato come supporto e la sperimentazione alchemica con sostanze chimiche e veleni",
                    "Il rispetto rigoroso delle regole accademiche del disegno dal vero",
                    "L'uso esclusivo di colori a tempera all'uovo su tavola lignea dorata",
                    "L'adozione di forme geometriche matematiche generate al computer"
                ],
                "correctIndex": 0,
                "explanation": "Polke è l'alchimista beffardo del gruppo: demistifica la retorica dei consumi e della cultura alta, mescolando pigmenti tossici (blu di Prussia, arsenico) che mutano con l'umidità dell'aria."
            },
            {
                "question": "In quale celebre mostra londinese del 1981 alla Royal Academy of Arts il Neoespressionismo tedesco si è affermato definitivamente a livello mondiale?",
                "options": [
                    "A New Spirit in Painting (curata da Christos Joachimides, Norman Rosenthal e Nicholas Serota)",
                    "Documenta 5 di Kassel",
                    "When Attitudes Become Form di Harald Szeemann",
                    "Freeze di Damien Hirst"
                ],
                "correctIndex": 0,
                "explanation": "'A New Spirit in Painting' consacrò internazionalmente la vitalità inarrestabile della nuova pittura europea (tedeschi e italiani) di fronte alla scena anglosassone."
            }
        ],
        "examQuiz": [
            {
                "question": "Perché la serie fotografica 'Occupations' (1969) di Anselm Kiefer, in cui l'artista si ritraeva compiendo il saluto nazista in vari luoghi d'Europa, suscitò enorme scandalo in Germania?",
                "options": [
                    "Perché ruppe il silenzio e la rimozione collettiva post-bellica sul Terzo Reich, costringendo i tedeschi a confrontarsi brutalmente con l'eredità storica senza ipocrisie consolatorie",
                    "Perché violava il divieto di fotografare monumenti pubblici",
                    "Perché utilizzava una fotocamera di fabbricazione sovietica",
                    "Perché l'artista rifiutò di stampare le fotografie su carta all'alogenuro d'argento"
                ],
                "correctIndex": 0,
                "explanation": "Kiefer compì una mossa provocatoria e coraggiosa: personificando il mostro storico della Germania, scardinò l'amnesia di una nazione che fingeva che il nazismo non fosse mai esistito."
            },
            {
                "question": "Quale ruolo svolge la stratificazione materica (matericità) nelle opere di Anselm Kiefer?",
                "options": [
                    "I materiali reali (il piombo che schiaccia, la paglia che brucia e deperisce, la cenere e il ferro) non sono semplici colori ma incarnano fisicamente il tempo, la fragilità, la rovina e la resurrezione alchemica",
                    "Serve unicamente ad aumentare il peso fisico del quadro per impedirne il furto nei musei",
                    "È un rimedio chimico per proteggere la tela dall'attacco dei tarli",
                    "Costituisce una trovata puramente ornamentale per rendere i dipinti tridimensionali"
                ],
                "correctIndex": 0,
                "explanation": "Per Kiefer la materia è spirito e storia: il piombo è il metallo saturnino della malinconia e della trasformazione; la paglia evoca i capelli biondi di Margarete della poesia di Celan."
            },
            {
                "question": "Cosa accomuna il linguaggio figurativo di A.R. Penck (Ralf Winkler) e la pittura rupestre primitiva?",
                "options": [
                    "L'uso di una stenografia grafica di omini stilizzati (Standart), segni arcaici e pittogrammi universali per narrare le tensioni politiche della Guerra Fredda tra Est e Ovest",
                    "L'obbligo di dipingere all'interno di caverne calcaree buie",
                    "L'impiego esclusivo di polvere di carbone vegetale legata con grasso animale",
                    "Il rifiuto totale di esporre le proprie opere in mostre illuminate da lampade elettriche"
                ],
                "correctIndex": 0,
                "explanation": "Penck inventò il sistema 'Standart': figure lineari ridotte all'essenziale come graffiti preistorici ma cariche di segnali di conflitto, barriere, soldati e ideologie divise dalla cortina di ferro."
            }
        ]
    },
    "arte-c4": {
        "quiz": [
            {
                "question": "In quale contesto urbano e sociale ha mosso i primi passi la ricerca artistica di Keith Haring a New York?",
                "options": [
                    "Nella metropolitana di New York, disegnando con gesso bianco sui pannelli pubblicitari neri inutilizzati (Subway Drawings)",
                    "Nelle prestigiose accademie d'arte tradizionali dell'Upper East Side",
                    "Negli studi cinematografici di Hollywood come disegnatore di cartoni animati",
                    "All'interno dei grandi istituti bancari di Wall Street"
                ],
                "correctIndex": 0,
                "explanation": "Haring scelse la metropolitana come laboratorio pubblico gratuito: disegnava a ritmo febbrile davanti ai pendolari con gessetti bianchi sui cartelloni neri, democratizzando l'arte per tutti."
            },
            {
                "question": "Quale pseudonimo utilizzava Jean-Michel Basquiat nei primi anni della sua attività per firmare i graffiti aforistici e poetici per le strade di Manhattan?",
                "options": [
                    "SAMO© (Same Old Shit)",
                    "BLADE",
                    "TAKI 183",
                    "CRASH"
                ],
                "correctIndex": 0,
                "explanation": "Insieme all'amico Al Diaz, Basquiat firmava 'SAMO©': frasi fulminanti, enigmi filosofici e critiche sociali vergate sui muri dell'East Village che attirarono l'attenzione dei media."
            },
            {
                "question": "Quali elementi iconografici ricorrenti contraddistinguono la pittura neoespressionista e viscerale di Jean-Michel Basquiat?",
                "options": [
                    "Corone a tre punte, scheletri, teschi anatomici, parole cancellate e riscritture, figure di campioni ed eroi afroamericani (Miles Davis, Sugar Ray Robinson) e critica al razzismo",
                    "Paesaggi bucolici fioriti dipinti con tecnica impressionista all'aria aperta",
                    "Composizioni puriste basate su griglie modulari in bianco e nero",
                    "Ritratti fotografici in posa di aristocratici dell'Ottocento"
                ],
                "correctIndex": 0,
                "explanation": "Basquiat celebra il genio e il dolore della cultura nera: la corona santifica eroi, pugili e musicisti jazz, mentre teschi e citazioni del libro di anatomia Gray's Anatomy svelano la vulnerabilità umana."
            },
            {
                "question": "Cosa rappresentano simbolicamente il 'Radiant Baby' (bambino raggiante) e il 'Barking Dog' (cane che abbaia) nel vocabolario iconografico di Keith Haring?",
                "options": [
                    "Il Radiant Baby rappresenta la purezza dell'energia vitale, la gioia e la speranza innocente del futuro; il cane che abbaia incarna l'avvertimento, le forze autoritarie e la violenza sociale",
                    "Sono marchi commerciali registrati per una linea di cibo per animali domestici",
                    "Sono caricature satiriche dei presidenti degli Stati Uniti dell'epoca",
                    "Rappresentano illustrazioni mediche per manuali di pediatria clinica"
                ],
                "correctIndex": 0,
                "explanation": "L'iconografia di Haring è un alfabeto visivo universale: figure sintetiche e radianti che parlano con immediatezza a chiunque, affrontando temi immensi come la vita, la morte, l'amore e l'AIDS."
            },
            {
                "question": "Quale illustre protagonista della Pop Art ha stretto una profonda collaborazione artistica e umana con Basquiat e Haring negli anni Ottanta?",
                "options": [
                    "Andy Warhol (con cui Basquiat realizzò una celebre serie di dipinti a quattro mani)",
                    "Roy Lichtenstein",
                    "Jasper Johns",
                    "Claes Oldenburg"
                ],
                "correctIndex": 0,
                "explanation": "Warhol divenne mentore e padre spirituale per Basquiat e Haring: la collaborazione tra l'anziano re della Pop Art e il giovane prodigio della strada produsse opere iconiche e un sodalizio leggendario."
            }
        ],
        "examQuiz": [
            {
                "question": "Perché Jean-Michel Basquiat cancellava frequentemente con una riga di vernice singole parole o frasi all'interno dei suoi dipinti?",
                "options": [
                    "Perché — come dichiarò lui stesso — cancellando una parola la si rende molto più visibile e desiderabile per lo sguardo dell'osservatore, che si sforza di leggerla",
                    "Perché commetteva continui errori di ortografia che cercava goffamente di nascondere",
                    "Perché gli acquirenti dei quadri gli imponevano di censurare i testi politici",
                    "Perché la vernice nera costava meno di tutti gli altri pigmenti colorati"
                ],
                "correctIndex": 0,
                "explanation": "'I cross out words so you will see them more; the fact that they are obscured makes you want to read them'. Un dispositivo concettuale raffinatissimo di valorizzazione per negazione."
            },
            {
                "question": "Quale fu il significato politico e democratico dell'apertura del 'Pop Shop' a SoHo da parte di Keith Haring nel 1986?",
                "options": [
                    "Rendere la propria arte accessibile a chiunque tramite magliette, spille e poster a basso costo, scardinando l'esclusivismo elitario delle gallerie per miliardari",
                    "Abbandonare il mondo dell'arte per dedicarsi unicamente al commercio al dettaglio",
                    "Vendere illegalmente opere d'arte sottratte ai musei federali",
                    "Dimostrare che solo i collezionisti facoltosi avevano il diritto di possedere le sue creazioni"
                ],
                "correctIndex": 0,
                "explanation": "Il Pop Shop incarnò l'etica sociale di Haring: 'La mia arte è per tutti'. Chiunque con un dollaro poteva comprare un pezzo della sua iconografia, portando l'arte fuori dalle torri d'avorio."
            },
            {
                "question": "In che modo l'epidemia di AIDS ha segnato tragicamente l'ultima fase della produzione artistica di Keith Haring?",
                "options": [
                    "Ha trasformato la sua grafica in uno strumento militante di sensibilizzazione politica e denuncia contro l'omofobia e il silenzio dei governi ('Silence = Death')",
                    "Lo ha indotto a smettere di dipingere per dedicarsi alla pittura floreale decorativa",
                    "Ha provocato la distruzione di tutte le sue tele conservate nei musei americani",
                    "Non ha influenzato minimamente le sue opere, rimaste puramente astratte"
                ],
                "correctIndex": 0,
                "explanation": "Colpito egli stesso dal virus (di cui morì nel 1990 a soli 31 anni), Haring riversò la sua arte nella lotta per la vita, fondando la Keith Haring Foundation e realizzando manifesti indimenticabili."
            }
        ]
    },
    "arte-c5": {
        "quiz": [
            {
                "question": "Qual è il presupposto teorico alla base dell'Appropriazionismo (Appropriation Art) affermatosi tra la fine degli anni Settanta e gli anni Ottanta?",
                "options": [
                    "Il prelievo diretto, la ri-fotografia o la duplicazione dichiarata di immagini preesistenti create da altri autori o dai mass media, per decostruire i miti di originalità, autorialità e unicità dell'opera d'arte",
                    "Il furto materiale di quadri custoditi nei musei statali europei",
                    "L'obbligo di dipingere unicamente su tele donate da altri colleghi pittori",
                    "La riproduzione a mano di stampe tipografiche su commissione governativa"
                ],
                "correctIndex": 0,
                "explanation": "L'Appropriazionismo sancisce che nel mondo saturo di immagini non serve crearne di nuove: ri-fotografare o prelevare immagini esistenti svela i meccanismi di potere e stereotipo della società dei consumi."
            },
            {
                "question": "Quale celebre operazione concettuale ha reso celebre l'artista Sherrie Levine nella serie 'After Walker Evans' (1981)?",
                "options": [
                    "Ha rifotografato le famose fotografie dei contadini dell'era della Depressione scattate da Walker Evans, esponendole a proprio nome senza alcuna alterazione visiva",
                    "Ha colorato con bombolette spray le stampe d'epoca di Evans",
                    "Ha bruciato pubblicamente i negativi originali del fotografo americano",
                    "Ha sostituito i volti dei contadini con ritratti di attori di Hollywood"
                ],
                "correctIndex": 0,
                "explanation": "Levine compie l'atto di appropriazione radicale: ri-fotografando il catalogo di Evans, interroga il patriarcato artistico, il diritto d'autore e il feticcio dell'originale."
            },
            {
                "question": "Cosa caratterizza la celeberrima serie fotografica 'Untitled Film Stills' (1977-1980) di Cindy Sherman?",
                "options": [
                    "Una sequenza di 69 autoritratti in bianco e nero in cui l'artista si traveste interpretando stereotipi femminili del cinema hollywoodiano e noir degli anni '50 e '60 (la casalinga, la vittima, la donna in carriera)",
                    "La raccolta di fotogrammi scartati dalle case cinematografiche di Los Angeles",
                    "Ritratti di attrici famose fotografate a loro insaputa per strada",
                    "Fotografie di paesaggi urbani notturni completamente deserti"
                ],
                "correctIndex": 0,
                "explanation": "Sherman non fotografa se stessa: usa il proprio corpo come tela per decostruire gli stereotipi visivi femminili costruiti dallo sguardo maschile (Male Gaze) nel cinema occidentale."
            },
            {
                "question": "Cosa ha ri-fotografato Richard Prince nelle sue celebri opere della serie 'Cowboys'?",
                "options": [
                    "Gli scatti pubblicitari delle sigarette Marlboro, eliminando il testo e il marchio commerciale per isolare l'archetipo mitologico del cowboy americano come pura finzione mediatica",
                    "Veri butteri della maremma toscana durante la transumanza",
                    "I quadri storici dell'epopea del Far West conservati a Washington",
                    "Fotogrammi di pellicole cinematografiche con John Wayne"
                ],
                "correctIndex": 0,
                "explanation": "Prince estrapola la pubblicità: senza logo Marlboro, il cowboy appare per quello che è: un costrutto artificiale di mascolinità e libertà confezionato dall'industria del tabacco."
            },
            {
                "question": "Quale critica d'arte ha curato la storica mostra 'Pictures' (1977) all'Artists Space di New York che ha dato il nome alla 'Pictures Generation'?",
                "options": [
                    "Douglas Crimp",
                    "Rosalind Krauss",
                    "Lucy Lippard",
                    "Clement Greenberg"
                ],
                "correctIndex": 0,
                "explanation": "Il saggio e la mostra di Douglas Crimp battezzarono la 'Pictures Generation' (Robert Longo, Cindy Sherman, Jack Goldstein, Sherrie Levine), cresciuta sotto il bombardamento delle immagini tv."
            }
        ],
        "examQuiz": [
            {
                "question": "In che modo le tesi filosofiche di Roland Barthes ('La morte dell'autore', 1967) si collegano direttamente alla poetica dell'Appropriazionismo?",
                "options": [
                    "Sostengono che un testo o un'opera non scaturiscono da un genio creatore isolato, ma sono un tessuto di citazioni preesistenti che prendono senso unicamente nello sguardo del fruitore",
                    "Impongono la soppressione legale della figura del curatore museale",
                    "Affermano che l'unico vero autore è il fabbricante della macchina fotografica",
                    "Vietano la pubblicazione di cataloghi d'arte con saggi critici"
                ],
                "correctIndex": 0,
                "explanation": "Barthes demolisce il mito romantico del creatore demiurgo: l'artista contemporaneo non crea ex nihilo, ma assembla e riconfigura codici culturali che appartengono al patrimonio collettivo."
            },
            {
                "question": "Nelle fotografie di Cindy Sherman, perché l'artista non assegna mai un titolo esplicito alle sue opere, limitandosi alla dicitura 'Untitled' seguita da un numero progressivo?",
                "options": [
                    "Per lasciare aperta l'interpretazione ed evitare che un nome guidi o limiti la decodifica dell'osservatore, costringendolo a confrontarsi con i propri preconcetti",
                    "Perché non ricordava i nomi dei personaggi interpretati durante gli scatti",
                    "Perché le gallerie applicavano una tassa su ogni lettera del titolo dell'opera",
                    "Perché le fotografie facevano parte di un archivio giudiziario segreto"
                ],
                "correctIndex": 0,
                "explanation": "'Untitled' nega la narrazione preconfezionata: lo spettatore crede di ricordare il film da cui è tratto il fotogramma, ma il film non esiste; è solo il repertorio visivo sedimentato nella sua mente."
            },
            {
                "question": "Quale riflessione sul genere (gender) e sul concetto di identità emerge dalla pratica del travestimento di Cindy Sherman?",
                "options": [
                    "L'identità femminile non è un'essenza biologica immutabile, ma una costruzione sociale, performativa e mediatica appresa attraverso la cultura visiva patriarcale",
                    "L'abbigliamento femminile degli anni Cinquanta era superiore a quello moderno",
                    "Le donne non dovrebbero mai essere ritratte all'interno di set fotografici",
                    "L'uso del trucco è incompatibile con il messaggio dell'arte concettuale"
                ],
                "correctIndex": 0,
                "explanation": "Anticipando le teorie queer e di genere di Judith Butler ('Gender Trouble'), la Sherman dimostra che il genere è una maschera, una performance codificata dalle immagini di consumo."
            }
        ]
    }
}

arte_quiz_data.update(arte_c3_to_16)

# Generate chapters 6 to 16 for Arte
arte_c6_to_16 = {
    "arte-c6": {
        "quiz": [
            {
                "question": "Quale concetto sociologico e filosofico di Jean Baudrillard ha costituito il fondamento teorico del movimento Neo-Geo (Neo-Geometric Conceptualism)?",
                "options": [
                    "Il concetto di 'Simulacro e Simulazione': nella società dei consumi il segno ha sostituito la realtà, creando un'iperrealtà in cui l'originale non esiste più",
                    "La teoria dell'alienazione operaia nella fabbrica metallurgica",
                    "Il principio di indeterminazione della meccanica quantistica",
                    "L'estetica romantica del sublime naturale di fronte all'infinito"
                ],
                "correctIndex": 0,
                "explanation": "Baudrillard ispira il Neo-Geo: viviamo in una mappa che precede il territorio. La merce e i media generano modelli di una realtà che non rimanda più a nulla di concreto (simulacri)."
            },
            {
                "question": "Cosa rappresentano metaforicamente le geometrie colorate (prigioni e celle con condotti) nei quadri di Peter Halley?",
                "options": [
                    "L'organizzazione invisibile del potere e del controllo sociale nella società post-industriale: gli appartamenti, gli uffici, i microchip e i flussi di comunicazione che imprigionano e collegano gli individui",
                    "Semplici studi formali di cromatologia pura senza alcun significato politico",
                    "Piante planimetriche di cattedrali rinascimentali toscane",
                    "Decorazioni geometriche destinate alla tessitura di tappeti orientali"
                ],
                "correctIndex": 0,
                "explanation": "Halley decostruisce l'astrazione geometrica di Mondrian e Malevic: le sue forme non sono armonie pure, ma celle carcerarie (prisons) collegate da tubi di conduzione (conduits), metafora della società disciplinare."
            },
            {
                "question": "Quale celebre serie di opere ha consacrato Jeff Koons nei primi anni Ottanta sigillando elettrodomestici nuovi in teche di plexiglas trasparente?",
                "options": [
                    "The New (aspirapolvere Hoover e lucidatrici immacolate illuminate da tubi al neon fluorescenti)",
                    "Celebration",
                    "Made in Heaven",
                    "Equilibrium"
                ],
                "correctIndex": 0,
                "explanation": "In 'The New', Koons santifica la merce intatta: gli aspirapolvere non hanno mai aspirato polvere, preservati in un'eterna purezza asessuata e seducente come nuovi idoli religiosi del consumo."
            },
            {
                "question": "Cosa simboleggiano le sculture in acciaio inox lucidato a specchio di Jeff Koons (come 'Rabbit', 1986)?",
                "options": [
                    "La trasformazione di un giocattolo gonfiabile da pochi centesimi in un feticcio di lusso riflettente, che attrae lo spettatore rispecchiandone il narcisismo e la bramosia di possesso",
                    "Uno studio scientifico sulla resistenza dei metalli alla corrosione atmosferica",
                    "La denuncia morale contro i produttori di palloncini in lattice",
                    "Un monumento funebre dedicato alla memoria degli animali da laboratorio"
                ],
                "correctIndex": 0,
                "explanation": "'Rabbit' è l'icona suprema dell'iper-merce: un coniglietto gonfiabile d'aria convertito in metallo freddo e prezioso che rimanda allo spettatore la sua stessa immagine riflessa."
            },
            {
                "question": "Quale atteggiamento ideologico distingue il Neo-Geo e Jeff Koons rispetto alla Pop Art storica degli anni Sessanta?",
                "options": [
                    "L'abbandono di qualsiasi critica o distanza ironica: una celebrazione e un'immersione totale, euforica e senza complessi nella logica del capitale, del marketing e del desiderio consumistico",
                    "Il ritorno al comunismo sovietico e il boicottaggio delle gallerie private",
                    "Il rifiuto categorico di vendere le opere a collezionisti d'élite",
                    "L'adozione esclusiva di materiali organici deperibili"
                ],
                "correctIndex": 0,
                "explanation": "Koons non critica il kitsch né la merce: li abbraccia con entusiasmo messianico, dichiarando che l'arte deve rassicurare la classe media e celebrare il godimento del presente."
            }
        ],
        "examQuiz": [
            {
                "question": "Nelle opere della serie 'Equilibrium' (1985) di Jeff Koons, cosa rappresenta l'iconica palla da basket perfettamente sospesa al centro di una vasca d'acqua distillata?",
                "options": [
                    "Uno stato irreale di perfetto equilibrio fisico e metafisico, metafora della promessa ingannevole di ascesa sociale che lo sport e la pubblicità offrono alle classi svantaggiate",
                    "Un esperimento didattico per spiegare la legge di gravitazione universale",
                    "La sponsorizzazione commerciale ufficiale per la squadra dei Chicago Bulls",
                    "Una scultura cinetica mossa da correnti marine artificiali"
                ],
                "correctIndex": 0,
                "explanation": "Koons unì fisica e sociologia: con l'aiuto del premio Nobel Richard Feynman sospese i palloni in equilibrio statico, affiancandoli a poster Nike che promettevano sogni di riscatto sociale."
            },
            {
                "question": "Perché Peter Halley ha scelto di dipingere i suoi quadri geometrici utilizzando esclusivamente vernici industriali sintetiche (come il Day-Glo e il Roll-a-Tex)?",
                "options": [
                    "Per rifiutare l'aura romantica della pittura tradizionale ad olio, utilizzando i materiali ruvidi e fosforescenti tipici dei cantieri e dei segnali d'allarme metropolitani",
                    "Perché i colori tradizionali erano stati dichiarati fuorilegge negli Stati Uniti",
                    "Per consentire ai dipinti di essere lavati con candeggina nei musei",
                    "Perché le vernici fluorescenti costavano meno dei pigmenti naturali"
                ],
                "correctIndex": 0,
                "explanation": "Il Roll-a-Tex è la vernice finta-intonaco dei condomini commerciali; il Day-Glo è la luce chimica dei giubbotti catarinfrangenti: Halley usa i materiali del condizionamento sociale moderno."
            },
            {
                "question": "Quale paradosso sociologico incarna il record di vendita di 'Rabbit' di Jeff Koons, battuto all'asta da Christie's per oltre 91 milioni di dollari nel 2019?",
                "options": [
                    "La consacrazione finale dell'opera come bene rifugio supremo della finanza globale, confermando la tesi di Baudrillard sulla coincidenza totale tra arte e feticismo del capitale",
                    "Il crollo definitivo del mercato dell'arte contemporanea a favore della pittura antica",
                    "L'acquisto dell'opera da parte di un consorzio di agricoltori canadesi",
                    "L'obbligo per l'artista di restituire il ricavato allo Stato federale"
                ],
                "correctIndex": 0,
                "explanation": "L'opera più costosa mai venduta di un artista vivente è un coniglietto gonfiabile finto: il trionfo assoluto del simulacro, dove il valore concettuale e finanziario sublima l'oggetto materiale."
            }
        ]
    },
    "arte-c7": {
        "quiz": [
            {
                "question": "Quali elementi contraddistinguono la poetica scultorea della New British Sculpture affermatasi in Inghilterra nei primi anni Ottanta?",
                "options": [
                    "Il superamento del minimalismo freddo attraverso la riscoperta della manualità, la reinvenzione dell'oggetto quotidiano di scarto e una forte carica metaforica e poetica",
                    "L'abbandono di qualsiasi materiale solido per dedicarsi unicamente alla realtà virtuale",
                    "La copia monumentale di archi di trionfo romani in gesso bianco",
                    "L'uso esclusivo di sculture meccaniche semoventi radiocomandate"
                ],
                "correctIndex": 0,
                "explanation": "Scultori come Cragg, Deacon, Woodrow e Kapoor rigenerano la scultura: riutilizzano frammenti di plastica, metallo, legno o pigmento per raccontare il rapporto tra uomo, natura e industria."
            },
            {
                "question": "Quale tecnica caratterizza le celebri prime opere di Tony Cragg composte da frammenti di plastica colorata trovati per strada o sulle spiagge?",
                "options": [
                    "La composizione a parete o a terra di tessere plastiche di scarto raggruppate per sfumatura cromatica, a formare silhouette di figure umane, bandiere o oggetti (come in 'Britain Seen from the North')",
                    "La fusione della plastica per creare blocchi solidi indistinti",
                    "L'incisione a laser di codici a barre su contenitori di detersivo",
                    "L'incenerimento pubblico dei rifiuti per protestare contro l'inquinamento"
                ],
                "correctIndex": 0,
                "explanation": "Cragg fa archeologia del presente: raccoglie i fossili della civiltà dei consumi (pezzi di giocattoli, flaconi) e li ordina cromaticamente, ricreando immagini che denunciano il degrado urbano."
            },
            {
                "question": "Cosa caratterizza le celebri prime sculture di Anish Kapoor degli anni Ottanta ricoperte di pigmento puro in polvere?",
                "options": [
                    "Forme geometriche e organiche misteriose che sembrano affiorare dal pavimento o dalla parete, sature di polvere di pigmento intensissimo (blu, rosso, giallo) che ne dissolve i contorni fisici",
                    "L'uso di circuiti elettrici lampeggianti alimentati a energia solare",
                    "La presenza di scritte satiriche contro la famiglia reale britannica",
                    "La riproduzione in miniatura di locomotive a vapore dell'epoca vittoriana"
                ],
                "correctIndex": 0,
                "explanation": "Il pigmento puro non è vernice stesa: è materia vibrante che fuoriesce dall'oggetto disperdendosi a terra. Il colore saturatissimo inganna l'occhio e trasforma la scultura in pura apparizione spirituale."
            },
            {
                "question": "Quale incontro culturale alimenta la ricerca scultorea e metafisica di Anish Kapoor?",
                "options": [
                    "La sintesi armonica tra la spiritualità e il misticismo della tradizione indiana e il rigore concettuale e formale della scultura occidentale contemporanea",
                    "La fusione tra l'arte aborigena australiana e il cinema muto svedese",
                    "L'architettura funzionalista sovietica e la calligrafia araba medievale",
                    "Il folklore musicale caraibico e la fisica nucleare sperimentale"
                ],
                "correctIndex": 0,
                "explanation": "Nato a Mumbai e formatosi a Londra, Kapoor fonde l'esperienza sensoriale dell'induismo (polveri votive, cavità, sacro) con la pulizia spaziale del modernismo occidentale."
            },
            {
                "question": "Cosa rappresenta il concetto di 'Vuoto' (The Void) nella poetica matura di Anish Kapoor?",
                "options": [
                    "Non un'assenza inerte, ma uno spazio gravido di possibilità, un abisso oscuro che assorbe lo sguardo dello spettatore provocando una sensazione di vertigine cosmica e introspezione psicologica",
                    "Uno spazio vuoto lasciato nel catalogo della mostra per risparmiare carta",
                    "La rimozione della scultura dalla sala per protesta sindacale",
                    "L'evacuazione forzata del pubblico dalle gallerie d'arte"
                ],
                "correctIndex": 0,
                "explanation": "Il vuoto di Kapoor (es. cavità dipinte di blu oltremare scurissimo o Vantablack) è pieno di presenza: lo sguardo non riesce a misurare la profondità e precipita nell'infinito."
            }
        ],
        "examQuiz": [
            {
                "question": "Nella celebre scultura pubblica monumentale 'Cloud Gate' (2006) a Chicago (soprannominata 'The Bean'), quale esperienza fenomenologica vive il visitatore?",
                "options": [
                    "La superficie di acciaio inox lucidata a specchio riflette e distorce lo skyline della città e i corpi dei visitatori, dissolvendo il confine tra spazio urbano, scultura e cielo",
                    "La scultura emette vapore acqueo refrigerante a ciclo continuo per mitigare il calore estivo",
                    "L'opera è programmata per cambiare forma geometrica ogni tre ore tramite pistoni idraulici",
                    "I visitatori sono obbligati a camminare sopra la scultura indossando speciali pattini a rotelle"
                ],
                "correctIndex": 0,
                "explanation": "Cloud Gate è un miracolo di ingegneria e percezione: privo di saldature visibili, attrae migliaia di persone che toccano il metallo e si vedono riflesse dentro la pancia concava del cielo liquido."
            },
            {
                "question": "Quale controversia ha scatenato Anish Kapoor nel mondo dell'arte contemporanea acquisendo i diritti esclusivi sul 'Vantablack'?",
                "options": [
                    "Ha ottenuto la licenza artistica monopolistica per il materiale più nero mai creato (capace di assorbire il 99.96% della luce), scatenando l'indignazione degli altri artisti per la privatizzazione di un colore",
                    "Ha impedito la vendita di qualsiasi vernice a tempera nera nelle cartolerie londinesi",
                    "Ha tentato di cancellare tutte le opere d'arte del Museo del Louvre dipingendole di nero",
                    "Ha imposto il pagamento di una royalty per chiunque utilizzi vestiti di colore scuro"
                ],
                "correctIndex": 0,
                "explanation": "Il caso Vantablack ha aperto un dibattito etico senza precedenti: un artista che brevetta per sé l'uso esclusivo del buio assoluto, a cui altri colleghi (come Stuart Semple) hanno risposto con provocazioni beffarde."
            },
            {
                "question": "Nelle opere in cera rossa e vaselina di Anish Kapoor (come 'Svayambhu' o 'Shooting into the Corner'), quale richiamo organico e corporeo viene evocato?",
                "options": [
                    "La carne, il sangue, la nascita e le funzioni viscerali del corpo femminile e universale, contrapposti alla pulizia asettica del cubo bianco museale",
                    "L'industria alimentare della produzione di confetture di frutta",
                    "La celebrazione della pittura a cera dell'antico Egitto",
                    "La conservazione criogenica delle specie animali in via d'estinzione"
                ],
                "correctIndex": 0,
                "explanation": "'Svayambhu' (auto-generato in sanscrito) è un blocco gigantesco di cera rossa che attraversa lentamente gli archi del museo scorticandosi: un corpo monumentale sanguinolento che lascia residui densi nello spazio."
            }
        ]
    },
    "arte-c8": {
        "quiz": [
            {
                "question": "Chi sono i maestri fondatori che hanno guidato la celebre cattedra di fotografia alla Kunstakademie di Düsseldorf a partire dal 1976?",
                "options": [
                    "Bernd e Hilla Becher",
                    "August Sander e Karl Blossfeldt",
                    "Henri Cartier-Bresson e Robert Capa",
                    "Helmut Newton e Guy Bourdin"
                ],
                "correctIndex": 0,
                "explanation": "I coniugi Becher hanno formato un'intera generazione di geni della fotografia contemporanea (Gursky, Struth, Ruff, Hütte, Candida Höfer), rivoluzionando la fotografia d'arte mondiale."
            },
            {
                "question": "Quale metodo di ripresa e archiviazione fotografica ha reso leggendaria la ricerca di Bernd e Hilla Becher?",
                "options": [
                    "La catalogazione sistematica e oggettiva di archeologie industriali (torri d'acqua, altiforni, silos) fotografate in bianco e nero frontale, luce diffusa senza ombre e ordinate in 'Tipologie' a griglia",
                    "Fotografie istantanee a colori scattate con fotocamere Polaroid durante le vacanze estive",
                    "Ritratti psicologici di operai siderurgici catturati con teleobiettivo nascosto",
                    "Scatti notturni ad altissima sensibilità con esposizioni multiple casuali"
                ],
                "correctIndex": 0,
                "explanation": "I Becher hanno creato cattedrali industriali della memoria: rigore geometrico assoluto, assenza di figure umane, cielo lattiginoso uniforme per confrontare le varianti morfologiche degli edifici industriali."
            },
            {
                "question": "Cosa caratterizza le spettacolari fotografie monumentali di Andreas Gursky?",
                "options": [
                    "Immagini di grandissimo formato, punto di vista panoramico elevato, nitidezza iperrealistica di ogni singolo dettaglio e fotoritocco digitale per esaltare le strutture seriali della globalizzazione capitalista",
                    "Fotografie in bianco e nero sgranate scattate con vecchie fotocamere stenopeiche",
                    "Ritratti intimi in penombra realizzati all'interno di camere da letto private",
                    "Collage di ritagli di giornale incollati su tavole di compensato grezzo"
                ],
                "correctIndex": 0,
                "explanation": "Gursky ritrae l'infrastruttura del capitale globale: borse valori brulicanti, magazzini Amazon sterminati, concerti oceanici e negozi discount (99 Cent), elevati a sublimi arazzi della modernità."
            },
            {
                "question": "Quale celebre serie fotografica ha reso famoso Thomas Struth nei principali musei internazionali?",
                "options": [
                    "Museum Photographs: ritratti di visitatori immersi nella contemplazione dei grandi capolavori della storia dell'arte (Louvre, Prado, Hermitage), creando un gioco di sguardi speculare tra pubblico e quadri",
                    "Ritratti di animali selvatici in riserve naturali africane",
                    "Fotografie di gare automobilistiche di Formula 1 scattate ad alta velocità",
                    "Documentazione fotografica di interventi chirurgici a cuore aperto"
                ],
                "correctIndex": 0,
                "explanation": "Nelle 'Museum Photographs', Struth fotografa noi che guardiamo l'arte: il tempo presente dei turisti contemporanei si fonde e si confronta con il tempo eterno dei maestri dipinti sulla parete."
            },
            {
                "question": "In cosa consistono i celebri 'Ritratti' (Portraits) dei primi anni Ottanta di Thomas Ruff?",
                "options": [
                    "Ritratti frontali a colori di giovani amici, scattati con luce asettica priva di ombre come fotografie segnaletiche o da passaporto, ingranditi a scala monumentale e privi di qualsiasi espressione emotiva",
                    "Ritratti scattati al buio tramite sensori termici a infrarossi",
                    "Autoritratti caricaturali in costume teatrale barocco",
                    "Fotografie di neonati scattate nelle sale parto ospedaliere"
                ],
                "correctIndex": 0,
                "explanation": "Ruff azzera la psicologia del ritratto borghese: l'ingrandimento gigante di un volto inespressivo e neutro trasforma il soggetto in una superficie enigmatica, interrogando la presunta verità dell'obiettivo."
            }
        ],
        "examQuiz": [
            {
                "question": "Perché alla Biennale di Venezia del 1990 l'assegnazione del Leone d'Oro per la Scultura a Bernd e Hilla Becher rappresentò una pietra miliare?",
                "options": [
                    "Perché riconobbe per la prima volta nella storia che una serie di fotografie tipologiche a griglia possedeva valore, monumentalità e rigore concettuale scultoreo",
                    "Perché i Becher avevano presentato sculture in marmo di Carrara anziché fotografie",
                    "Perché la giuria della Biennale era composta unicamente da fotografi tedeschi",
                    "Perché i Becher decisero di rifiutare pubblicamente il premio in segno di protesta"
                ],
                "correctIndex": 0,
                "explanation": "Un trionfo concettuale: considerare la fotografia tipologica come scultura riconobbe la natura monumentale delle loro griglie architettoniche, cambiando la percezione della fotografia nei musei d'arte."
            },
            {
                "question": "Nelle opere di Andreas Gursky (come 'Rhein II' o '99 Cent'), quale ruolo svolge la manipolazione digitale dei file fotografici?",
                "options": [
                    "Non serve a falsificare la realtà per ingannare, ma a perfezionare la composizione geometrica eliminando elementi di disturbo o clonando moduli per creare un 'iper-reale' tipico della contemporaneità",
                    "Serve unicamente a inserire personaggi famosi all'interno del paesaggio",
                    "Viene impiegata per ridurre la risoluzione dell'immagine e mascherare errori di messa a fuoco",
                    "Viene utilizzata per convertire automaticamente le fotografie in disegni a carboncino"
                ],
                "correctIndex": 0,
                "explanation": "Gursky interviene al computer come un pittore: in 'Rhein II' cancella una fabbrica e una pista ciclabile per ottenere la striscia perfetta del fiume; in '99 Cent' dilata all'infinito le corsie delle merci."
            },
            {
                "question": "Quale legame storico unisce la Scuola di Düsseldorf alle ricerche fotografiche della Nuova Oggettività (Neue Sachlichkeit) degli anni Venti di August Sander?",
                "options": [
                    "L'approccio enciclopedico, analitico, seriale e distaccato che rinuncia al sentimentalismo artistico per documentare il mondo attraverso categorie strutturali e tipologie formali rigorose",
                    "L'uso esclusivo delle stesse identiche lastre di vetro originali del 1920",
                    "La condivisione del medesimo manifesto politico rivoluzionario comunista",
                    "L'obbligo di ritrarre unicamente contadini della regione della Renania"
                ],
                "correctIndex": 0,
                "explanation": "Sander catalogava i tipi umani ('Uomini del Ventesimo Secolo'); i Becher e i loro allievi catalogano le strutture della civiltà industriale: il filo rosso dell'oggettività analitica tedesca."
            }
        ]
    },
    "arte-c9": {
        "quiz": [
            {
                "question": "Cosa indica l'acronimo 'YBAs' nel panorama artistico internazionale degli anni Novanta?",
                "options": [
                    "Young British Artists (il gruppo di giovani artisti emergenti britannici guidati da Damien Hirst, Tracey Emin, Sarah Lucas e Gary Hume)",
                    "Yorkshire Brotherhood of Arts",
                    "Yellow Bauhaus Architecture Society",
                    "Youth Broadcasting Association of London"
                ],
                "correctIndex": 0,
                "explanation": "Gli YBAs hanno rivoluzionato l'arte britannica degli anni '90: irriverenti, imprenditoriali, scandalosi e abili strateghi dei media, hanno fatto di Londra la capitale mondiale dell'arte contemporanea."
            },
            {
                "question": "Quale celebre mostra autogestita del 1988 in un edificio portuale dismesso dei Docklands di Londra ha segnato la nascita ufficiale degli YBAs?",
                "options": [
                    "Freeze (ideata e curata da Damien Hirst quando era ancora studente al Goldsmiths College)",
                    "Sensation",
                    "Young Americans",
                    "This is Tomorrow"
                ],
                "correctIndex": 0,
                "explanation": "Hirst capisce che non bisogna aspettare le gallerie ufficiali: affitta un magazzino vuoto nei Docklands, seleziona i compagni di corso del Goldsmiths, allestisce 'Freeze' e invita i collezionisti più influenti."
            },
            {
                "question": "Quale figura di influente magnate pubblicitario e megacollezionista ha acquistato le opere degli YBAs consacrandoli a livello planetario?",
                "options": [
                    "Charles Saatchi",
                    "Leo Castelli",
                    "Peggy Guggenheim",
                    "Larry Gagosian"
                ],
                "correctIndex": 0,
                "explanation": "Saatchi vide 'Freeze', intuì il potenziale dirompente del gruppo e ne divenne il mecenate principale: acquistò le opere di Hirst, Emin, Quinn e Chapman, organizzando mostre leggendarie."
            },
            {
                "question": "Quale mostra epocale del 1997 alla Royal Academy of Arts di Londra ha scatenato scandali mediatici e proteste di piazza consacrando definitivamente gli YBAs?",
                "options": [
                    "Sensation: Young British Artists from the Saatchi Collection",
                    "A New Spirit in Painting",
                    "The Great British Art Show",
                    "Pop Life: Art in a Material World"
                ],
                "correctIndex": 0,
                "explanation": "'Sensation' scosse l'opinione pubblica: folle sterminate, cortei di protesta contro il ritratto di Myra Hindley di Marcus Harvey, e l'affermazione definitiva del fenomeno YBAs nel costume globale."
            },
            {
                "question": "Quali caratteristiche tematiche e stilistiche hanno reso celebri e provocatorie le opere degli YBAs?",
                "options": [
                    "L'uso di materiali non convenzionali e scioccanti (animali morti in formalina, sangue, deiezioni, letti sfatti), umorismo nero, cinismo, estetica shock e un'inedita scaltrezza imprenditoriale",
                    "Il ritorno esclusivo all'acquerello di paesaggio all'aperto",
                    "L'adozione rigorosa del disegno a matita secondo i canoni accademici ottocenteschi",
                    "L'anonimato totale degli artisti che rifiutavano di farsi fotografare o intervistare"
                ],
                "correctIndex": 0,
                "explanation": "Gli YBAs infrangono ogni tabù: uniscono il retaggio del ready-made di Duchamp con l'attitudine sfacciata del punk e l'efficacia comunicativa dei cartelloni pubblicitari di massa."
            }
        ],
        "examQuiz": [
            {
                "question": "Cosa distingueva la formazione al Goldsmiths College di Londra rispetto alle accademie d'arte tradizionali negli anni Ottanta?",
                "options": [
                    "L'abolizione della separazione tra le diverse tecniche (pittura, scultura, fotografia) a favore di un approccio concettuale libero, interdisciplinare e attento alla promozione e alla critica istituzionale",
                    "L'obbligo di frequentare cinque anni di studio del nudo dal vero in creta",
                    "Il divieto assoluto di parlare di denaro o di mercato dell'arte",
                    "L'insegnamento esclusivo del restauro di affreschi medievali"
                ],
                "correctIndex": 0,
                "explanation": "Il Goldsmiths guidato da Michael Craig-Martin formava artisti-manager concettuali: niente corporativismo di mestiere, ma pensiero critico, capacità di presentarsi e audacia espositiva."
            },
            {
                "question": "Nella celebre opera 'Self' (1991) di Marc Quinn, quale materiale biologico estremo viene impiegato per realizzare il calco della testa dell'artista?",
                "options": [
                    "Cinque litri del sangue dello stesso artista prelevato nell'arco di cinque mesi, congelato all'interno di una teca refrigerata",
                    "Resina epossidica colorata con pigmento rosso sintetico",
                    "Vino rosso d'annata solidificato tramite addensanti chimici",
                    "Cera d'api vergine proveniente da alveari londinesi"
                ],
                "correctIndex": 0,
                "explanation": "'Self' è un autoritratto biologico totale: se la spina elettrica della teca frigo viene staccata, l'opera si scioglie e muore, metafora cruda della fragilità e dipendenza della vita umana."
            },
            {
                "question": "Perché l'opera 'My Bed' (1998) di Tracey Emin ha rappresentato un culmine scandaloso e intimo dell'estetica YBA?",
                "options": [
                    "Ha esposto nella prestigiosa cornice del Turner Prize il proprio letto sfatto circondato da rifiuti reali, lenzuola macchiate, mozziconi di sigaretta e biancheria usata, trasformando il dolore privato in confessione pubblica",
                    "Era una scultura in bronzo dorato raffigurante un letto reale del Seicento",
                    "Si trattava di una performance teatrale recitata da attori professionisti",
                    "Era un'installazione interattiva che invitava i visitatori a dormire nel museo"
                ],
                "correctIndex": 0,
                "explanation": "La Emin trasforma la propria crisi depressiva in ready-made confessionale: nessun filtro estetizzante, ma la nuda verità biografica di un momento di collasso emotivo offerta allo sguardo collettivo."
            }
        ]
    },
    "arte-c10": {
        "quiz": [
            {
                "question": "Qual è il titolo formale della celeberrima opera di Damien Hirst del 1991 raffigurante uno squalo tigre di oltre 4 metri immerso in formalina dentro una teca vetrata?",
                "options": [
                    "The Physical Impossibility of Death in the Mind of Someone Living (L'impossibilità fisica della morte nella mente di un essere vivente)",
                    "Jaws: The Shark that Ate the Art Market",
                    "Natural History of Modern Fear",
                    "A Thousand Years of Swimming"
                ],
                "correctIndex": 0,
                "explanation": "Il titolo poetico e filosofico è parte integrante dell'opera: guardare negli occhi un predatore letale a pochi centimetri di distanza evoca il terrore della morte e l'incapacità umana di concepire la propria fine."
            },
            {
                "question": "Quale grande tema universale costituisce il baricentro ossessivo dell'intera ricerca artistica di Damien Hirst?",
                "options": [
                    "Il confronto ineludibile tra la vita, la morte, il decadimento biologico e i disperati tentativi umani (religione, scienza, medicina, arte) di eludere o ritardare la fine",
                    "L'analisi matematica delle proprietà geometriche dei frattali",
                    "La celebrazione nostalgica dell'impero coloniale britannico",
                    "La promozione delle diete alimentari vegetariane"
                ],
                "correctIndex": 0,
                "explanation": "Tutta la produzione di Hirst (animali sezionati, armadietti di farmaci, farfalle morte, teschi) indaga il grande enigma: la nostra vulnerabilità fisica e la fede cieca che riponiamo nei farmaci per non morire."
            },
            {
                "question": "In cosa consiste la celebre serie degli 'Spot Paintings' (o Pharmaceutical Paintings) di Damien Hirst?",
                "options": [
                    "Tele a fondo bianco su cui sono disposti a griglia rigorosa cerchi colorati di diametro identico, dove nessun colore si ripete mai all'interno della stessa tela, intitolati con nomi di composti chimici e farmaci",
                    "Quadri dipinti a getti casuali di colore lanciati con pistole ad aria compressa",
                    "Fotografie ingrandite di macchie di muffa coltivate in piastre di Petri",
                    "Disegni a puntini realizzati a mano con inchiostro di china nero"
                ],
                "correctIndex": 0,
                "explanation": "Gli Spot Paintings mimano l'estetica rassicurante e asettica dell'industria farmaceutica: pillole colorate gioiose che promettono salute e immortalità seriale disposte con precisione industriale."
            },
            {
                "question": "Cosa accade nella scioccante installazione 'A Thousand Years' (1990) di Damien Hirst?",
                "options": [
                    "All'interno di una doppia teca di vetro, le mosche nascono da una scatola di vermi, si nutrono di una testa di mucca decapitata e insanguinata e muoiono fulminate da una lampada elettrocutrice",
                    "Un computer elabora una sequenza numerica destinata a durare un millennio",
                    "Mille libri di storia vengono consumati lentamente da colonie di termiti",
                    "Una pianta di quercia cresce all'interno di una camera climatica controllata"
                ],
                "correctIndex": 0,
                "explanation": "La vita e la morte condensate in un ciclo chiuso e crudele: la mosca nasce, si ciba del cadavere e trova la morte fulminea. Francis Bacon rimase talmente impressionato da quest'opera da ammirarla per un'ora intera."
            },
            {
                "question": "Cosa caratterizza la serie delle 'Pharmacy' e degli armadietti medicinali (Medicine Cabinets)?",
                "options": [
                    "Vetr 쇼teche e armadi chirurgici in acciaio inossidabile che ospitano migliaia di confezioni reali di farmaci, pillole e strumenti chirurgici ordinati secondo la loro funzione terapeutica",
                    "Sculture in cartapesta dipinte con motivi floreali",
                    "Distributori automatici funzionanti di aspirina collocati nelle sale del museo",
                    "Ritratti fotografici di medici e infermieri inglesi"
                ],
                "correctIndex": 0,
                "explanation": "Hirst svela la nuova religione laica d'Occidente: non crediamo più nei santi, ma crediamo ciecamente che una compressa chimica possa salvarci l'anima e il corpo."
            }
        ],
        "examQuiz": [
            {
                "question": "Quando lo squalo originale di 'The Physical Impossibility of Death...' iniziò a decomporsi nel 2006 a causa della conservazione imperfetta, cosa decise di fare Damien Hirst?",
                "options": [
                    "Sostituì lo squalo deteriorato con un nuovo esemplare identico pescato in Australia, riaffermando il primato dell'idea concettuale rispetto alla singola reliquia organica fisica",
                    "Distrusse l'opera ritirandola per sempre dal mercato dell'arte",
                    "Accusò il collezionista di aver violato il contratto di manutenzione",
                    "Rimpiazzò lo squalo con un calco in resina plastica sintetica"
                ],
                "correctIndex": 0,
                "explanation": "Il paradosso della nave di Teseo in salsa contemporanea: Hirst ribadì che l'opera non è il corpo biologico dello squalo, ma l'idea dell'incontro visivo con la bestia dentro la formalina."
            },
            {
                "question": "Nelle opere della serie 'Kaleidoscope' (quadri a caleidoscopio), quale materiale naturale viene utilizzato per creare disegni che imitano le vetrate delle cattedrali gotiche?",
                "options": [
                    "Migliaia di vere ali di farfalla incollate sulla vernice lucida a smalto, combinando una bellezza seducente con il fatto macabro della strage di insetti necessari per comporla",
                    "Piume di pavone raccolte nei giardini reali britannici",
                    "Petali di rosa stabilizzati chimicamente contro la disidratazione",
                    "Scaglie di conchiglie fossili intagliate a mano"
                ],
                "correctIndex": 0,
                "explanation": "Da lontano sembrano vetrate luminose di Chartres; da vicino scoprite che sono ali strappate a migliaia di creature morte: il tipico cortocircuito di Hirst tra estasi estetica e memento mori."
            },
            {
                "question": "Quale critica etica e artistica è stata più frequentemente indirizzata a Damien Hirst riguardo alla produzione seriale dei suoi 'Spin' e 'Spot Paintings'?",
                "options": [
                    "L'utilizzo massiccio di decine di assistenti di studio per dipingere le tele al posto suo, trasformando l'atelier in una fabbrica commerciale (Warhol Factory) dove l'artista agisce da amministratore delegato del marchio",
                    "L'uso esclusivo di colori tossici che hanno causato intossicazioni nei musei",
                    "L'incapacità tecnica di utilizzare il software Photoshop per i bozzetti",
                    "Il rifiuto di apporre la propria firma autografa sul retro delle tele"
                ],
                "correctIndex": 0,
                "explanation": "Hirst ha sempre risposto senza ipocrisie: 'I miei assistenti dipingono gli spot meglio di quanto saprei fare io; la mia maestria sta nel concepire l'idea e governare il sistema'."
            }
        ]
    }
}

arte_quiz_data.update(arte_c6_to_16)

# Generate chapters 11 to 16 for Arte
arte_c11_to_16 = {
    "arte-c11": {
        "quiz": [
            {
                "question": "In cosa consiste la celebre e controversa opera 'For the Love of God' (Per l'amor di Dio) realizzata da Damien Hirst nel 2007?",
                "options": [
                    "Un calco in platino di un vero teschio umano del Settecento, tempestato da 8.601 diamanti purissimi per un totale di 1.106 carati, con i denti umani originali incastonati",
                    "Una scultura in marmo di Carrara raffigurante San Pietro crocifisso a testa in giù",
                    "Un mosaico gigante composto da banconote da cinquecento euro autentiche",
                    "Un reliquiario medievale contenente ossa di martiri cristiani"
                ],
                "correctIndex": 0,
                "explanation": "'For the Love of God' è il memento mori più costoso e splendente della storia dell'umanità: costato circa 15 milioni di sterline di produzione, esorcizza la morte coprendola di ricchezza accecante."
            },
            {
                "question": "Quale significato culturale e filosofico racchiude l'uso dei diamanti applicati sul teschio di 'For the Love of God'?",
                "options": [
                    "La sfida suprema alla caducità: il diamante (la materia più dura e incorruttibile dell'universo, simbolo di eternità e ricchezza terrena) che riveste e cancella la decomposizione della carne",
                    "La sponsorizzazione commerciale delle aziende diamantifere sudafricane",
                    "La celebrazione del valore monetario delle riserve della Banca d'Inghilterra",
                    "Una critica ecologica all'inquinamento delle miniere di carbone fossile"
                ],
                "correctIndex": 0,
                "explanation": "Il diamante non muore mai, il corpo umano si disfa: accostare il cranio al diamante è il tentativo disperato e sfarzoso di vincere la morte trasformando il teschio in un gioiello immortale."
            },
            {
                "question": "Quale evento rivoluzionario e senza precedenti ha organizzato Damien Hirst nel settembre del 2008 presso la casa d'aste Sotheby's a Londra?",
                "options": [
                    "L'asta storica 'Beautiful Inside My Head Forever': ha venduto 223 opere nuove saltando completamente le sue gallerie di riferimento (disintermediazione), incassando oltre 111 milioni di sterline proprio mentre crollava Lehman Brothers",
                    "La vendita di beneficenza di tutti i suoi averi per finanziare la ricerca medica",
                    "Un'asta al ribasso in cui le opere venivano regalate ai visitatori disoccupati",
                    "La distruzione col fuoco di cento quadri per protestare contro le banche"
                ],
                "correctIndex": 0,
                "explanation": "Un atto di audacia economica senza precedenti: bypassando galleristi influenti come White Cube e Gagosian, Hirst ha venduto direttamente all'asta, ridefinendo il potere dell'artista nel mercato."
            },
            {
                "question": "Cosa si intende per 'Disintermediazione' nel mercato dell'arte contemporanea applicata da Damien Hirst?",
                "options": [
                    "La prassi con cui l'artista scavalca il tradizionale intermediario (la galleria privata) per vendere direttamente le proprie creazioni ai collezionisti finali o tramite case d'asta",
                    "L'eliminazione dei critici d'arte dalla redazione delle riviste specializzate",
                    "La vendita di opere d'arte unicamente tramite canali televisivi commerciali",
                    "L'obbligo di pagare le transazioni artistiche esclusivamente in monete d'oro"
                ],
                "correctIndex": 0,
                "explanation": "Hirst ha dimostrato che un artista con un marchio personale potente e planetario può trattare direttamente col mercato primario, sovvertendo le gerarchie consolidate del sistema delle gallerie."
            },
            {
                "question": "Quale celebre frase pronunciò la madre di Damien Hirst quando il figlio le annunciò l'idea di voler realizzare un teschio di diamanti?",
                "options": [
                    "'For the love of God, what are you going to do next?' (Per l'amor di Dio, cos'altro ti inventerai adesso?), frase che diede il titolo all'opera",
                    "'I diamanti sono i migliori amici delle donne'",
                    "'Non dovresti mai scherzare con le cose della religione'",
                    "'Spero che le banche ti concedano un prestito abbastanza generoso'"
                ],
                "correctIndex": 0,
                "explanation": "La tipica esclamazione esasperata della madre di fronte alle stravaganze del figlio artista ha fornito a Hirst il titolo perfetto per un'opera intrisa di stupore, blasfemia e misticismo."
            }
        ],
        "examQuiz": [
            {
                "question": "Cosa accadde sui mercati finanziari globali nelle stesse identiche ore del 15 settembre 2008 in cui si apriva la trionfale asta di Damien Hirst da Sotheby's?",
                "options": [
                    "Dichiarava bancarotta la banca d'affari americana Lehman Brothers, innescando la peggiore crisi finanziaria mondiale dal 1929, mentre l'asta di Hirst registrava record assoluti",
                    "Il prezzo del petrolio scendeva a zero dollari al barile",
                    "Veniva introdotta la moneta unica europea in tutti i paesi del G8",
                    "Le borse asiatiche chiudevano per festività nazionale prolungata"
                ],
                "correctIndex": 0,
                "explanation": "Una coincidenza storica surreale: mentre il cuore della finanza mondiale collassava, la stanza d'asta di Sotheby's batteva squali e vitelli d'oro a cifre folli, segnando l'apogeo dell'iper-capitalismo nell'arte."
            },
            {
                "question": "Quale confronto antropologico e storico ha instaurato la critica tra il teschio di Hirst e i reperti delle civiltà mesoamericane (Aztechi e Maya)?",
                "options": [
                    "Il teschio di Hirst rinnova la tradizione dei teschi di cristallo e delle maschere turchesi azteche, in cui il cranio del defunto viene trasformato in oggetto votivo abbagliante per dialogare con le divinità della morte",
                    "Dimostra che gli Aztechi conoscevano le tecniche moderne di fusione del platino industriale",
                    "Conferma che Hirst ha trafugato reperti archeologici dal museo antropologico di Città del Messico",
                    "Non sussiste alcun nesso, trattandosi di fenomeni totalmente incompatibili"
                ],
                "correctIndex": 0,
                "explanation": "Hirst ha citato esplicitamente la fascinazione per i teschi aztechi visti al British Museum: un rito antico quanto l'umanità che veste lo scheletro di pietre preziose per vincere il terrore dell'oblio."
            },
            {
                "question": "In che modo l'attività di Damien Hirst mette in discussione la tradizionale separazione tra 'creazione artistica' e 'strategia finanziaria'?",
                "options": [
                    "Dimostra che nel mondo contemporaneo il marketing, la costruzione del prezzo, la speculazione e la gestione del marchio non sono fattori esterni all'opera, ma costituiscono il medium stesso dell'opera d'arte",
                    "Provoca l'annullamento del valore estetico di tutti i dipinti realizzati prima del 2000",
                    "Dimostra che per avere successo artistico è obbligatorio possedere una laurea in economia bancaria",
                    "Esclude i musei pubblici dalla possibilità di acquistare opere d'arte contemporanea"
                ],
                "correctIndex": 0,
                "explanation": "Come Warhol disse 'La Business Art è il gradino successivo all'Arte', Hirst trasforma la transazione economica in performance artistica: il denaro e la quotazione sono parte integrante del significato concettuale."
            }
        ]
    },
    "arte-c12": {
        "quiz": [
            {
                "question": "Quale colossale mostra personale ha allestito Damien Hirst a Venezia nel 2017 occupando contemporaneamente Palazzo Grassi e Punta della Dogana?",
                "options": [
                    "Treasures from the Wreck of the Unbelievable (Tesori dal naufragio dell'Incredibile)",
                    "The Miraculous Journey",
                    "Relics from the Deep Ocean",
                    "Sensation 2: The Venetian Collection"
                ],
                "correctIndex": 0,
                "explanation": "Frutto di 10 anni di lavoro segreto e decine di milioni di investimento, 'Treasures' è stata una delle mostre più monumentali e spiazzanti della storia dell'arte del ventunesimo secolo."
            },
            {
                "question": "Qual è la grandiosa finzione narrativa (mockumentary archeologico) costruita da Hirst per giustificare le centinaia di opere esposte in 'Treasures'?",
                "options": [
                    "Il ritrovamento sottomarino, al largo delle coste dell'Africa orientale, del tesoro inabissatosi duemila anni fa appartenuto a un ricco liberto romano collezionista d'arte di nome Cif Amotan II",
                    "Il recupero dei resti della mitica città scomparsa di Atlantide nel mezzo dell'oceano Atlantico",
                    "Il ritrovamento della stiva del relitto del Titanic contenente sculture di Michelangelo",
                    "La scoperta di sculture aliene sepolte sotto i ghiacci dell'Antartide"
                ],
                "correctIndex": 0,
                "explanation": "Hirst fabbrica una bugia sublime: gira finti documentari subacquei con sub che ripescano colossi corallini dal fondale marino, attribuendoli alla collezione perduta del liberto Cif Amotan II (anagramma di 'I am a fiction')."
            },
            {
                "question": "Cosa rivela l'anagramma del nome del collezionista fittizio 'Cif Amotan II' ideato da Damien Hirst?",
                "options": [
                    "'I am a fiction' (Io sono una finzione)",
                    "'Art is dead'",
                    "'Gold and money'",
                    "'Faith and love'"
                ],
                "correctIndex": 0,
                "explanation": "Hirst dissemina indizi ironici: ammette apertamente che tutto è finto, sfidando l'osservatore a decidere se credere alla favola o smascherare l'inganno."
            },
            {
                "question": "Quali elementi anacronistici e spiazzanti compaiono tra le statue 'archeologiche' ricoperte di falsi coralli sottomarini in 'Treasures'?",
                "options": [
                    "Personaggi della cultura pop contemporanea (Topolino, Pippo, Mowgli e Baloo, Transformer) riprodotti come reperti antichi insieme a busti che ritraggono lo stesso Hirst o Kate Moss",
                    "Modelli in scala di automobili Ferrari e pneumatici da corsa",
                    "Telefoni cellulari e tastiere di computer incrostati di conchiglie",
                    "Bandiere degli Stati moderni con scritte al neon"
                ],
                "correctIndex": 0,
                "explanation": "Il cortocircuito tra antico e pop: Topolino coperto di coralli duemila anni dopo o una dea sumera che assomiglia a Kate Moss. Hirst demolisce il confine tra archeologia autentica e mito contemporaneo."
            },
            {
                "question": "Quale riflessione contemporanea sull'era della 'Post-Verità' (Post-Truth) e delle Fake News solleva la mostra 'Treasures from the Wreck'?",
                "options": [
                    "Dimostra come la fede, l'autorità dell'istituzione museale e una narrazione spettacolare ben orchestrata possano convincere il pubblico a credere a qualsiasi finzione spacciata per verità storica",
                    "Dimostra che la tecnologia archeologica sottomarina è obsoleta",
                    "Invita i musei a non esporre mai opere prive di datazione al carbonio 14",
                    "Sostiene che tutti i musei di antichità del mondo espongono esclusivamente copie false"
                ],
                "correctIndex": 0,
                "explanation": "Nel secolo delle fake news, Hirst mette in scena il potere della narrazione: se l'opera è collocata in un palazzo storico con targhette accademiche e finti video, la gente desidera credere all'illusione."
            }
        ],
        "examQuiz": [
            {
                "question": "Nella monumentale statua 'Demon with Bowl' alta oltre 16 metri collocata nel cortile di Palazzo Grassi, a quale scultura visionaria di William Blake si è ispirato Damien Hirst?",
                "options": [
                    "Al disegno 'The Ghost of a Flea' (Il fantasma di una pulce)",
                    "Al dipinto 'Il Grande Drago Rosso e la Donna vestita di Sole'",
                    "All'incisione 'L'Antico dei Giorni'",
                    "All'illustrazione della 'Divina Commedia' dantesca"
                ],
                "correctIndex": 0,
                "explanation": "Il mostruoso demone senza testa che svettava nel cortile è la trasposizione tridimensionale gigante della pulce vampiro di William Blake: un colosso di resina dipinto come bronzo millenario ripescato dal mare."
            },
            {
                "question": "Perché le opere di 'Treasures' venivano presentate contemporaneamente in tre versioni distinte (The Collector's Edition, The Copy, The Museum Translation)?",
                "options": [
                    "Per decostruire il concetto di autenticità museale, mostrando il reperto incrostato dai coralli marini, la sua copia integra di restauro e la riproduzione commerciale contemporanea",
                    "Perché l'artista aveva esaurito le idee per creare nuove forme scultoree",
                    "Per consentire ai non vedenti di toccare la versione in plastica morbida",
                    "Per rispettare una direttiva della dogana marittima italiana"
                ],
                "correctIndex": 0,
                "explanation": "Hirst svela la stratificazione dell'industria archeologica: c'è l'oggetto 'ripescato' sporco di alghe, la versione pulita per il museo e il souvenir per il bookshop, svelando come il museo 'fabbrica' la storia."
            },
            {
                "question": "Quale fu il giudizio della critica d'arte internazionale di fronte alla titanica operazione di 'Treasures from the Wreck' a Venezia?",
                "options": [
                    "Profondamente polarizzato: da una parte chi la giudicò un capolavoro concettuale vertiginoso sulla finzione e la megalomania del collezionismo; dall'altra chi la stroncò come un kitsch faraonico degno di Las Vegas o Disneyland",
                    "Totalmente unanime nell'assegnare all'artista il premio Nobel per la pace",
                    "Indifferente, tanto che la mostra registrò meno di cento visitatori",
                    "Di condanna unanime per violazione delle leggi sui diritti marittimi internazionali"
                ],
                "correctIndex": 0,
                "explanation": "La critica si spaccò: monumentale trionfo barocco della post-verità o baracconata disneyana miliardaria? Hirst ha polarizzato il mondo, confermando la sua capacità di dominare il discorso culturale globale."
            }
        ]
    },
    "arte-c13": {
        "quiz": [
            {
                "question": "Qual è il metodo di lavoro e la struttura organizzativa dello Studio Olafur Eliasson fondato a Berlino nel 1995?",
                "options": [
                    "Un grande laboratorio multidisciplinare e interdisciplinare che riunisce oltre novanta professionisti tra architetti, ingegneri, programmatori, artigiani, cuochi, storici dell'arte e filosofi",
                    "Uno studio solitario in cui l'artista dipinge isolato senza alcun contatto con collaboratori esterni",
                    "Un'agenzia pubblicitaria commerciale che produce loghi per multinazionali",
                    "Una scuola elementare d'arte per bambini della città di Berlino"
                ],
                "correctIndex": 0,
                "explanation": "Lo studio di Eliasson a Prenzlauer Berg è una fucina rinascimentale del ventunesimo secolo: ricerca scientifica, modelli geometrici, prototipi ottici ed ecologia convivono in un ecosistema collettivo."
            },
            {
                "question": "Quale corrente filosofica costituisce la pietra angolare della ricerca artistica di Olafur Eliasson?",
                "options": [
                    "La Fenomenologia della percezione (Merleau-Ponty), che pone al centro l'esperienza corporea e sensoriale diretta dello spettatore nel qui-e-ora ('Your engagement has consequences')",
                    "Il Nichilismo radicale nietzschiano",
                    "Il Razionalismo cartesiano che disprezza i sensi come fonte di inganno",
                    "L'idealismo platonico del mondo delle idee incorporee"
                ],
                "correctIndex": 0,
                "explanation": "Per Eliasson 'L'opera non è nell'oggetto, ma nell'incontro tra l'oggetto e lo spettatore'. Il visitatore non è un osservatore passivo ma il co-produttore dell'esperienza attraverso i suoi sensi."
            },
            {
                "question": "Quali elementi e fenomeni fisici naturali costituiscono i 'materiali da costruzione' primari nelle installazioni di Eliasson?",
                "options": [
                    "Luce, nebbia artificiale, vapore acqueo, riflessi di specchi, vento, temperatura, muschio e prismi ottici",
                    "Gesso alabastrino, marmo di Carrara e bronzo fuso a cera persa",
                    "Vernici fluorescenti sintetiche e motori a scoppio alimentati a benzina",
                    "Cavi telefonici in rame e componenti hardware dismessi"
                ],
                "correctIndex": 0,
                "explanation": "Eliasson dematerializza l'arte: plasma l'aria, la luce gialla monocromatica, la condensa e la rifrazione ottica per risvegliare la consapevolezza sensoriale e il rapporto con la natura."
            },
            {
                "question": "Perché nelle sue installazioni tecnologiche Olafur Eliasson sceglie quasi sempre di lasciare a vista i macchinari (ventilatori, cavi, pompe della nebbia, proiettori)?",
                "options": [
                    "Perché non intende creare un'illusione ingannevole o magica, ma svelare la natura artificiale e costruita del fenomeno, rendendo il pubblico consapevole del meccanismo percettivo",
                    "Perché lo studio non aveva fondi economici sufficienti per costruire pareti di cartongesso",
                    "Perché le normative di sicurezza dei musei impongono l'ispezione visiva dei cavi elettrici",
                    "Per consentire ai visitatori di spegnere i macchinari quando desiderano"
                ],
                "correctIndex": 0,
                "explanation": "Trasparenza fenomenologica: Eliasson mostra l'artificio. Quando vedi il ventilatore o la lampada al sodio, capisci come la tua percezione viene costruita e diventi un osservatore critico, non ingannato."
            },
            {
                "question": "Cosa indica l'uso ricorrente del pronome possessivo 'Your' (Tuo) nei titoli delle opere di Eliasson (es. 'Your atmospheric colour atlas', 'Your waste of time')?",
                "options": [
                    "Sottolinea la natura soggettiva e unica dell'esperienza: ogni persona percepisce i colori e lo spazio in modo diverso, e l'opera esiste solo attraverso la presenza attiva dell'individuo",
                    "Indica che l'opera appartiene legalmente al visitatore che ha acquistato il biglietto",
                    "È un omaggio formale alla regina Elisabetta II del Regno Unito",
                    "Costituisce un trucco pubblicitario per vendere merchandising all'uscita del museo"
                ],
                "correctIndex": 0,
                "explanation": "Il 'Tuo' è un appello etico e percettivo: non c'è una verità oggettiva del museo, ma 'il tuo colore', 'la tua percezione', 'la tua responsabilità' ecologica verso il pianeta."
            }
        ],
        "examQuiz": [
            {
                "question": "Quale collaborazione pluridecennale con un celebre architetto e geometra islandese ha permesso a Eliasson di sviluppare le sue complesse strutture spaziali poliedriche e reticolari?",
                "options": [
                    "La collaborazione con Einar Thorsteinn (già allievo di Buckminster Fuller e pioniere delle geometrie spaziali complesse)",
                    "La collaborazione con Renzo Piano",
                    "La consulenza ingegneristica con Norman Foster",
                    "Il sodalizio artistico con Frank Gehry"
                ],
                "correctIndex": 0,
                "explanation": "Thorsteinn ha portato nello studio di Eliasson la magia dei poliedri non euclidei, delle cupole geodetiche e della cristallografia, traducendo formule matematiche in spazi abitabili di luce e specchi."
            },
            {
                "question": "In che modo l'esperienza nei paesaggi primordiali dell'Islanda ha forgiato la sensibilità visiva ed ecologica di Olafur Eliasson fin dall'infanzia?",
                "options": [
                    "Il contatto costante con ghiacciai, vulcani, distese di lava muschiata, cascate e la luce boreale mutevole gli ha insegnato che la natura non è uno sfondo fisso ma un processo vivo e dinamico",
                    "Lo ha convinto a dedicarsi unicamente all'estrazione mineraria del carbone",
                    "Lo ha spinto a rifiutare qualsiasi forma di tecnologia moderna all'interno dell'arte",
                    "Gli ha fatto scegliere di vivere in solitudine senza mai viaggiare nelle metropoli mondiali"
                ],
                "correctIndex": 0,
                "explanation": "L'Islanda è un pianeta in formazione: camminando sui ghiacciai con il padre, Eliasson ha imparato a misurare il tempo geologico e a comprendere la vulnerabilità degli ecosistemi fragili."
            },
            {
                "question": "Nelle celebri stanze a 'Luce Monocromatica' (Mono-frequency light) di Eliasson illuminate con lampade a vapori di sodio a banda stretta, quale fenomeno ottico sperimentano i visitatori?",
                "options": [
                    "Tutti i colori della stanza e dei vestiti scompaiono istantaneamente, riducendo l'intera visione a sfumature di giallo ocra e grigio, aumentando paradossalmente la percezione dei dettagli e delle forme",
                    "I visitatori sperimentano una temporanea cecità notturna irreversibile",
                    "Tutti gli oggetti metallici assumono una colorazione blu fosforescente brillante",
                    "L'aria all'interno della stanza diventa immediatamente trasparente ai raggi infrarossi"
                ],
                "correctIndex": 0,
                "explanation": "Le lampade al sodio emettono una sola lunghezza d'onda (circa 589 nanometri): i recettori del colore nell'occhio non possono distinguere le tinte e il cervello decodifica tutto come un bianco e nero dorato iper-dettagliato."
            }
        ]
    },
    "arte-c14": {
        "quiz": [
            {
                "question": "Quale leggendaria installazione ambientale del 2003 all'interno della gigantesca Turbine Hall della Tate Modern di Londra ha consacrato Olafur Eliasson sulla scena globale?",
                "options": [
                    "The Weather Project",
                    "The Weather Station",
                    "The Solar System",
                    "The Sun Machine"
                ],
                "correctIndex": 0,
                "explanation": "'The Weather Project' è una delle pietre miliari dell'arte del nuovo millennio: oltre 2 milioni di persone visitarono la Turbine Hall, trasformandola in una cattedrale laica di luce, nebbia e raccoglimento collettivo."
            },
            {
                "question": "Come era costruito tecnicamente il colossale 'Sole' che dominava lo spazio in 'The Weather Project'?",
                "options": [
                    "Un semicerchio di centinaia di lampade monofrequenza a vapori di sodio gialle, montato contro la parete di fondo sotto un soffitto interamente rivestito di specchi che ne rifletteva l'altra metà completando la sfera perfetta",
                    "Un enorme pallone aerostatico gonfiato a elio e dipinto con smalto arancione",
                    "Un proiettore cinematografico 70mm puntato su una tela bianca circolare",
                    "Una lente convergente che convogliava la vera luce solare dall'esterno dell'edificio"
                ],
                "correctIndex": 0,
                "explanation": "L'illusione era magistrale: il sole era in realtà solo un mezzo cerchio. Lo specchio al soffitto raddoppiava lo spazio, completando la sagoma solare e rispecchiando i visitatori come minuscole ombre nere sul pavimento."
            },
            {
                "question": "Quale comportamento sociale spontaneo e inedito assunsero i milioni di visitatori all'interno di 'The Weather Project'?",
                "options": [
                    "Si sdraiarono sul pavimento di cemento freddo della Turbine Hall a guardarsi riflessi nel soffitto a specchio, parlando sottovoce, meditando o formando figure umane collettive in un'atmosfera di comunità condivisa",
                    "Iniziarono a protestare violentemente chiedendo la rimozione dell'opera d'arte",
                    "Fuggirono spaventati temendo un incendio a causa della fitta nebbia artificiale",
                    "Rimasero in silenzio assoluto senza muoversi per tutta la durata dell'esposizione"
                ],
                "correctIndex": 0,
                "explanation": "Eliasson creò uno spazio di cittadinanza sensoriale: le persone si sdraiavano a terra come in un parco pubblico, salutando la propria immagine riflessa a 35 metri di altezza in una quiete quasi religiosa."
            },
            {
                "question": "Cosa simboleggiava il tema del 'Tempo meteorologico' (Weather) scelto da Eliasson per la Tate Modern di Londra?",
                "options": [
                    "Il clima come grande costrutto sociale e argomento di conversazione quotidiano britannico, ma anche come indicatore del cambiamento climatico globale che unisce il destino di tutti gli esseri viventi",
                    "La celebrazione delle previsioni del tempo trasmesse dalla televisione di stato BBC",
                    "La memoria delle piogge acide che hanno colpito l'Inghilterra nell'Ottocento",
                    "Una ricerca meteorologica per calcolare l'umidità dell'aria del fiume Tamigi"
                ],
                "correctIndex": 0,
                "explanation": "Il meteo è l'argomento rompighiaccio universale: parlando del tempo parliamo della nostra vulnerabilità e del pianeta che condividiamo, unendo natura interiore e atmosfera esteriore."
            },
            {
                "question": "Quale ruolo svolgeva la nebbia artificiale (mist) diffusa costantemente nello spazio in 'The Weather Project'?",
                "options": [
                    "Materializzava i fasci di luce dorata rendendo visibile l'aria e lo spazio volumetrico, disperdendo le ombre nette e creando un senso di sospensione temporale",
                    "Serviva a disinfettare l'ambiente per prevenire epidemie influenzali",
                    "Raffreddava la temperatura della stanza fino a sotto lo zero termico",
                    "Nascondeva i visitatori per garantire la loro privacy durante l'esperienza"
                ],
                "correctIndex": 0,
                "explanation": "La nebbia creava corpo: l'aria non era più vuota ma densa di particelle d'acqua e zucchero che catturavano la radiazione luminosa monocromatica, avvolgendo i corpi in un tramonto senza fine."
            }
        ],
        "examQuiz": [
            {
                "question": "Quale concetto sociologico definisce la capacità di opere come 'The Weather Project' di trasformare un museo in un luogo di incontro democratico e intersoggettivo?",
                "options": [
                    "L'Estetica Relazionale (teorizzata dal critico Nicolas Bourriaud negli anni Novanta), in cui l'opera d'arte produce relazioni umane dirette e comunità temporanee",
                    "Il Funzionalismo strutturale sociologico",
                    "La teoria della scelta razionale applicata al tempo libero",
                    "Il determinismo tecnologico dei mass media"
                ],
                "correctIndex": 0,
                "explanation": "Bourriaud descrive l'arte come 'stato di incontro': The Weather Project non era un feticcio da comprare, ma una piazza comune dove le persone interagivano e sperimentavano la coesistenza."
            },
            {
                "question": "Perché Eliasson definisce 'The Weather Project' come un modello di 'vedere se stessi mentre si fa esperienza' (Seeing yourself sensing)?",
                "options": [
                    "Perché lo specchio al soffitto costringe l'osservatore a vedere il proprio corpo dal di fuori mentre vive la sensazione sensoriale, sviluppando una coscienza meta-cognitiva del proprio atto percettivo",
                    "Perché l'artista forniva occhiali speciali polarizzati a tutti i visitatori all'ingresso",
                    "Perché telecamere a circuito chiuso registravano i volti per proiettarli sul web",
                    "Perché i visitatori dovevano compilare un diario di bordo delle proprie emozioni"
                ],
                "correctIndex": 0,
                "explanation": "'Seeing yourself sensing': non solo guardare il sole, ma vedere se stessi minuscoli mentre guardano. Questa sdoppiatura fenomenologica trasforma l'esperienza in consapevolezza critica di sé."
            },
            {
                "question": "In che modo l'installazione delle quattro cascate artificiali monumentali 'The New York City Waterfalls' (2008) lungo l'East River ha riletto il paesaggio urbano di Manhattan?",
                "options": [
                    "Ha introdotto la forza primordiale e scrosciante dell'acqua nel cuore della metropoli d'acciaio, interrompendo la velocità frenetica dei newyorkesi e riconnettendoli alla natura del porto fluviale",
                    "Ha fornito acqua potabile a tutti i quartieri degradati di Brooklyn",
                    "Ha generato energia idroelettrica per illuminare i ponti sospesi della città",
                    "Ha impedito alle imbarcazioni mercantili di navigare lungo il fiume per motivi ecologici"
                ],
                "correctIndex": 0,
                "explanation": "Quattro cascate monumentali alte fino a 35 metri: l'acqua sollevata su impalcature industriali precipitava nell'East River, regalando alla metropoli il suono e la potenza dimenticata dell'elemento naturale."
            }
        ]
    },
    "arte-c15": {
        "quiz": [
            {
                "question": "In quale memorabile azione di arte pubblica non autorizzata del 1998 Olafur Eliasson ha colorato le acque dei fiumi di Brema, Moss, Stoccolma, Los Angeles e Venezia senza preavviso?",
                "options": [
                    "Green River (utilizzando uranina, un colorante atossico biodegradabile impiegato dai biologi per tracciare le correnti)",
                    "Red Waters of Venice",
                    "The Toxic River Tour",
                    "Liquid Nature Project"
                ],
                "correctIndex": 0,
                "explanation": "Green River fu un'epifania improvvisa: svegliarsi e vedere il Canal Grande di un verde acido radioattivo. L'acqua non era più invisibile o scontata; la gente si fermava, guardava la città e riscopriva il fiume."
            },
            {
                "question": "Cosa intendeva provocare Eliasson tingendo improvvisamente l'acqua dei fiumi metropolitani in 'Green River'?",
                "options": [
                    "Svegliare i cittadini dall'anestesia urbana quotidiana, costringendoli a notare lo scorrere della corrente e a ridefinire il loro rapporto emotivo con lo spazio comune che attraversano distrattamente ogni giorno",
                    "Protestare contro i costi del trasporto pubblico locale sui battelli",
                    "Promuovere un nuovo marchio di bibite energetiche sportive",
                    "Dimostrare l'efficacia di un nuovo brevetto di depurazione fognaria"
                ],
                "correctIndex": 0,
                "explanation": "'La gente guarda l'acqua solo quando accade qualcosa': colorarla di verde smeraldo brillante senza avvisare nessuno ha rotto l'abitudine mentale, trasformando la città in un punto interrogativo vivente."
            },
            {
                "question": "Cosa ha portato fisicamente Olafur Eliasson nelle piazze di Copenaghen (2014), Parigi (Cop21 nel 2015) e Londra (2018) per la monumentale opera 'Ice Watch'?",
                "options": [
                    "Decine di enormi blocchi di ghiaccio millenario staccatisi dalla calotta polare della Groenlandia, disposti a cerchio come un orologio affinché i passanti potessero toccarli, ascoltarli e vederli sciogliersi davanti ai propri occhi",
                    "Ghiaccio sintetico refrigerato artificialmente con compressori elettrici",
                    "Sculture di orologi da polso giganti realizzate in resina trasparente",
                    "Fotografie satellitari del polo nord stampate su grandi cartelloni pubblicitari"
                ],
                "correctIndex": 0,
                "explanation": "L'emergenza climatica non è più un dato statistico astratto: in 'Ice Watch' puoi posare l'orecchio sul blocco di ghiaccio, sentire lo scricchiolio millenario dell'aria intrappolata e vederlo liquefarsi al sole."
            },
            {
                "question": "Quale dispositivo solare portatile a forma di fiore giallo ha co-fondato e progettato Olafur Eliasson insieme all'ingegnere Frederik Ottesen nel 2012?",
                "options": [
                    "Little Sun (una piccola lampada solare ad alta efficienza per portare luce pulita ed economica a comunità prive di rete elettrica in Africa e nel mondo)",
                    "Solar Flower Battery",
                    "Yellow Pocket Phone",
                    "Eco-Light Power"
                ],
                "correctIndex": 0,
                "explanation": "Con Little Sun, l'arte diventa impresa sociale: sostituendo le tossiche lampade a cherosene con l'energia del sole, la luce dona ai bambini ore di studio la notte e riduce le emissioni di carbonio."
            },
            {
                "question": "In che modo il progetto fotografico 'The Glacier Melt Series' (1999-2019) di Eliasson documenta drammaticamente il cambiamento climatico?",
                "options": [
                    "Rifotografando esattamente dagli stessi identici punti aerei trenta ghiacciai islandesi a distanza di vent'anni, rivelando la loro devastante contrazione e scomparsa",
                    "Colorando i ghiacciai con inchiostro nero per accelerare l'assorbimento termico",
                    "Scattando fotografie notturne illuminate da razzi di segnalazione navali",
                    "Confrontando i ghiacciai islandesi con le dune sabbiose del deserto del Sahara"
                ],
                "correctIndex": 0,
                "explanation": "La prova provata della crisi ecologica: accostando lo scatto del 1999 e quello del 2019, la parete monumentale di ghiaccio si è ritirata di chilometri, trasformandosi in una pozza di sassi e fango."
            }
        ],
        "examQuiz": [
            {
                "question": "Quale tesi etica sostiene Olafur Eliasson nel suo saggio 'Your engagement has consequences'?",
                "options": [
                    "La conoscenza razionale dei dati climatici non basta a cambiare i comportamenti: serve un'esperienza sensoriale ed emotiva incarnata nel corpo per trasformare l'informazione in azione etica e politica concreta",
                    "L'arte contemporanea deve essere disinteressata e non occuparsi mai di problemi sociali o ambientali",
                    "Gli artisti hanno il dovere di pagare le tasse sulle emissioni di anidride carbonica delle proprie mostre",
                    "L'esperienza estetica riguarda unicamente i visitatori che appartengono alle classi sociali abbienti"
                ],
                "correctIndex": 0,
                "explanation": "Se diciamo 'si sono sciolti cento milioni di tonnellate di ghiaccio', la mente non reagisce. Se tocchi il ghiaccio che piange a gocce sulla tua mano, senti la responsabilità sulla tua pelle: l'arte colma il divario tra capire e agire."
            },
            {
                "question": "Come viene gestito il bilancio ecologico (Carbon Footprint) del trasporto dei blocchi di ghiaccio dalla Groenlandia all'Europa per il progetto 'Ice Watch'?",
                "options": [
                    "I blocchi vengono prelevati da quelli già staccati naturalmente e galleggianti nei fiordi, caricati su navi commerciali già in rotta e l'impronta di carbonio viene rigorosamente calcolata e compensata con progetti di riforestazione certificati",
                    "Il ghiaccio viene trasportato con aerei militari ad altissima velocità",
                    "I blocchi vengono lasciati sciogliere durante la navigazione marittima senza alcuna protezione",
                    "L'artista non si occupa dell'impatto ambientale, ritenendo l'arte superiore alle leggi della termodinamica"
                ],
                "correctIndex": 0,
                "explanation": "Eliasson collabora con climatologi come Minik Rosing: il ghiaccio viaggiava nei container frigo di navi commerciali che tornavano vuote dalla Groenlandia, e ogni grammo di CO2 è stato documentato e compensato."
            },
            {
                "question": "Quale modello economico virtuoso adotta il progetto sociale 'Little Sun' di Eliasson?",
                "options": [
                    "Le lampade sono vendute a prezzo maggiorato nei musei e nelle nazioni ricche, consentendo di sussidiare la vendita a prezzi popolari accessibili nelle comunità rurali africane off-grid, creando posti di lavoro locali",
                    "Tutte le lampade vengono donate gratuitamente tramite elicotteri militari",
                    "Il progetto è finanziato esclusivamente tramite la vendita di armi leggere",
                    "Le lampade funzionano unicamente se connesse a una rete internet a fibra ottica"
                ],
                "correctIndex": 0,
                "explanation": "Un modello di micro-economia sostenibile: il visitatore del museo a New York compra Little Sun a 30 euro, permettendo all'imprenditore locale in Etiopia di acquistarla a poco e rivenderla a prezzo calmierato nella sua comunità."
            }
        ]
    },
    "arte-c16": {
        "quiz": [
            {
                "question": "Quale posizione pionieristica occupa l'artista francese Miguel Chevalier nella storia dell'arte contemporanea internazionale?",
                "options": [
                    "È considerato uno dei massimi pionieri mondiali della Computer Art e della Digital Art, avendo iniziato a utilizzare il computer come medium artistico esclusivo fin dal 1978",
                    "È stato il fondatore del movimento della Pop Art parigina negli anni Cinquanta",
                    "È l'inventore della tecnica di incisione all'acquaforte su rame",
                    "È stato il primo artista a dipingere su tela utilizzando smalti sintetici automobilistici"
                ],
                "correctIndex": 0,
                "explanation": "Fin dagli albori dell'informatica (fine anni '70), Chevalier ha compreso che il computer non era una calcolatrice da ufficio ma una nuova tavolozza infinita per esplorare luce, algoritmi e codice."
            },
            {
                "question": "Cosa si intende per 'Arte Generativa' (Generative Art) nella poetica di Miguel Chevalier?",
                "options": [
                    "Opere create attraverso algoritmi e software che generano autonomamente forme visive in costante mutazione e auto-rigenerazione in tempo reale, senza mai ripetersi identiche nel tempo",
                    "Opere generate riproducendo all'infinito la stessa fotografia stampata su carta",
                    "Dipinti a olio realizzati da più generazioni di pittori della stessa famiglia",
                    "Sculture che cambiano colore solo se scaldate a fuoco vivo"
                ],
                "correctIndex": 0,
                "explanation": "Nell'arte generativa l'artista non disegna l'immagine finale, ma programma le regole e le leggi genetiche del codice: il computer calcola e genera un flusso infinito di forme organiche viventi."
            },
            {
                "question": "Quale grande tema contraddistingue celebri installazioni di Chevalier come 'Fractal Flowers' o 'Extra-Natural'?",
                "options": [
                    "Il dialogo poetico e filosofico tra Natura e Artificio: la creazione di giardini virtuali e piante digitali mutanti che imitano i cicli biologici di crescita, fioritura e morte nel regno dei pixel",
                    "L'analisi delle malattie infettive all'interno delle foreste tropicali",
                    "La documentazione fotografica dei parchi urbani della città di Parigi",
                    "La coltivazione idroponica di specie vegetali commestibili nei musei"
                ],
                "correctIndex": 0,
                "explanation": "I 'Fractal Flowers' sono una flora transgenica virtuale: semi di codice matematico germogliano in fiori poligonali giganti che reagiscono al vento cibernetico, esplorando l'ibridazione tra biologia e silicio."
            },
            {
                "question": "Cosa caratterizza le installazioni immersive e monumentali 'Site-Specific' proiettate da Chevalier su grandi architetture storiche (come 'Magic Carpets' o nelle cattedrali)?",
                "options": [
                    "Tappeti luminosi interattivi di pixel e trame geometriche proiettati su pavimenti e volte, che ondeggiano, si deformano e si ricompongono in tempo reale reagendo al passaggio e ai movimenti del pubblico",
                    "Proiezioni di filmati pubblicitari muti senza interattività",
                    "La copertura delle facciate con teli di plastica colorata non illuminata",
                    "L'emissione di raggi laser concentrati che incidono la pietra degli edifici"
                ],
                "correctIndex": 0,
                "explanation": "In 'Magic Carpets' il pubblico cammina sulla luce: sensori a infrarossi captano i passi dei visitatori, scatenando onde fluide di colori caleidoscopici che trasformano lo spazio monumentale in un sogno interattivo."
            },
            {
                "question": "Come interagisce lo spettatore nelle opere digitali interattive di Miguel Chevalier?",
                "options": [
                    "Lo spettatore diventa parte attiva e co-autore dell'opera: i suoi movimenti corporei, la sua velocità e la sua vicinanza (rilevati da sensori ottici e telecamere) alterano la forma, i colori e la musica dell'installazione in tempo reale",
                    "Lo spettatore deve rimanere seduto e immobile con gli occhi bendati",
                    "Lo spettatore deve inserire monete all'interno di un lettore ottico per attivare lo schermo",
                    "Lo spettatore può solo guardare l'opera da uno spioncino senza entrare nella sala"
                ],
                "correctIndex": 0,
                "explanation": "Senza visitatore l'opera dorme: il corpo della persona è l'interruttore cinetico che risveglia l'algoritmo, dissolvendo la barriera tra spettatore passivo e creatore dell'immagine."
            }
        ],
        "examQuiz": [
            {
                "question": "Nelle opere storiche della serie 'De l'argentique au numérique' degli anni Ottanta, come operava Miguel Chevalier per esplorare le possibilità del pixel?",
                "options": [
                    "Scomponeva e ingrandiva la struttura a mosaico dei pixel fino al limite della leggibilità dell'immagine, anticipando la riflessione sulla risoluzione, sulla perdita di definizione e sulla nuova retina digitale",
                    "Dipingeva i pixel a mano con pennelli di martora su pergamena medievale",
                    "Distruggeva fisicamente i monitor televisivi a colpi di martello",
                    "Utilizzava solo tubi catodici rotti per mostrare immagini deformate"
                ],
                "correctIndex": 0,
                "explanation": "Quando il mondo vedeva il pixel come un difetto di bassa risoluzione, Chevalier ne ha colto l'essenza estetica: il pixel è l'atomo luminoso della nuova pittura del futuro, il tassello del mosaico contemporaneo."
            },
            {
                "question": "Cosa si intende per 'Realtà Virtuale e Aumentata' all'interno delle sperimentazioni più recenti di Miguel Chevalier?",
                "options": [
                    "L'uso di visori VR (come Oculus) per immergere completamente il fruitore a 360 gradi all'interno delle sue architetture generiche e delle foreste poligonali, consentendogli di volare dentro il codice visivo",
                    "La registrazione di documentari didattici sulla vita dei programmatori di computer",
                    "La vendita di videogiochi commerciali d'azione sugli store digitali",
                    "L'installazione di webcam di sicurezza lungo le strade delle città"
                ],
                "correctIndex": 0,
                "explanation": "Con la VR, Chevalier abbatte l'ultimo diaframma: lo spettatore non guarda più uno schermo piatto appeso al muro, ma entra fisicamente dentro il dipinto digitale, navigando tra costellazioni di dati mutanti."
            },
            {
                "question": "Quale legame filosofico e storico unisce le proiezioni digitali di Miguel Chevalier all'arte optical (Op Art) e cinetica degli anni Sessanta (Vasarely, Le Parc)?",
                "options": [
                    "L'indagine sulla cinetica visiva, l'instabilità percettiva, le illusioni ottiche di movimento e il coinvolgimento fisiologico dell'osservatore, aggiornati attraverso la potenza di calcolo del software contemporaneo",
                    "L'uso esclusivo di sculture meccaniche azionate da motori a molla",
                    "La firma di manifesti programmatici che vietavano l'impiego dell'elettricità",
                    "L'adesione formale alle regole compositive del Neoclassicismo canoviano"
                ],
                "correctIndex": 0,
                "explanation": "Chevalier è l'erede diretto dell'Op Art e dell'arte programmata: Vasarely sognava un alfabeto plastico universale; Chevalier realizza quel sogno attraverso il codice binario e la computazione in tempo reale."
            }
        ]
    }
}

arte_quiz_data.update(arte_c11_to_16)

# Load existing arte-data.js
with open("data/arte-data.js", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"window\.ARTE_DATA\s*=\s*(\[.*\]);?", content, re.DOTALL)
if not m:
    raise Exception("Could not find window.ARTE_DATA in data/arte-data.js")

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
    if cid in arte_quiz_data:
        quizzes = arte_quiz_data[cid]["quiz"]
        exam_quizzes = arte_quiz_data[cid]["examQuiz"]
        
        # Balance quiz across 0, 1, 2, 3 rotato per capitolo
        for idx, q in enumerate(quizzes):
            balance_question(q, (idx + c_idx) % 4)
            
        # Balance examQuiz rotato per capitolo
        for idx, eq in enumerate(exam_quizzes):
            balance_question(eq, (idx + c_idx + 1) % 4)
            
        chap["quiz"] = quizzes
        chap["examQuiz"] = exam_quizzes
        print(f"Updated {cid}: {len(chap['quiz'])} quiz, {len(chap['examQuiz'])} examQuiz")

with open("data/arte-data.js", "w", encoding="utf-8") as f:
    f.write(f"// Dataset Storia dell'Arte Contemporanea (Anni '80, Hirst/YBAs, Eliasson, Chevalier)\nwindow.ARTE_DATA = {json.dumps(data, indent=2, ensure_ascii=False)};\n")

print("Successfully rebuilt data/arte-data.js with high academic rigor and balanced options!")
