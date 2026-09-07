# build_dispense_10to14.py
import json

chapters = [
    # 10. Progettare pagine web
    {
        "id": "dispense-c10",
        "number": 10,
        "title": "Progettare pagine web",
        "subtitle": "Principi di Krug, scansione visiva, satisficing, gerarchie e navigazione persistente",
        "readTime": "10 min",
        "summary": """### Come gli utenti usano davvero il Web
Le dispense riprendono integralmente i cardini metodologici del classico dell'usabilità di Steve Krug (*Don't Make Me Think*).
La maggior parte dei progettisti neofiti immagina l'utente come un lettore attento e riflessivo che esamina ogni riga della pagina con calma metodica. La realtà empirica dimostra l'esatto opposto:
1. **Non leggiamo le pagine: le scansioniamo**:
   - L'occhio dell'utente salta rapidamente sulla superficie dello schermo cercando parole chiave, titoli in grassetto o elementi grafici salienti che emanano un 'odore di informazione' (*scent of information*).
2. **Non scegliamo l'opzione migliore: facciamo 'Satisficing'**:
   - Teorizzato dal premio Nobel Herbert Simon, il *satisficing* (da *satisfying* + *sufficing*) descrive la tendenza a scegliere la **prima opzione ragionevole** che appare sufficientemente promettente, piuttosto che sprecare tempo ed energia a valutare tutte le alternative possibili.
3. **Non capiamo come funzionano le cose: ci arrangiamo (*Muddling through*)**:
   - Gli utenti non leggono le istruzioni: cliccano finché non ottengono ciò che desiderano, creandosi modelli mentali empirici imperfetti ma funzionali.

### La Prima Legge di Krug: 'Non farmi pensare!'
Ogni pagina web dovrebbe idealmente risultare **autoevidente** (*self-evident*) o almeno **autoesplicativa**:
- Qualsiasi punto interrogativo inutile che sorge nella mente dell'utente (*'È un bottone o solo un testo?'*, *'Dove mi trovo?'*, *'Posso cliccare qui?'*) consuma la preziosa riserva di energia cognitiva.

### Regole auree per progettare pagine che funzionano
- **Stabilire una gerarchia visiva chiara**: le cose più importanti devono essere visivamente più evidenti; gli elementi correlati devono essere raggruppati; le relazioni di parentela devono essere esplicitate dall'annidamento.
- **Sfruttare le convenzioni consolidate**: non reinventare la ruota; posizionare il logo in alto a sinistra cliccabile verso la home, il carrello in alto a destra e il campo di ricerca evidente rassicura l'utente.
- **Definire chiaramente le aree dello schermo**: una pagina suddivisa in zone funzionali distinte permette all'occhio di scartare subito le porzioni irrilevanti.
- **Rendere evidente cosa è cliccabile**: l'affordance dei collegamenti e dei bottoni deve essere palese (contrasto di colore, rilievo, sottolineatura, cursore `pointer`).
- **Eliminare il rumore visivo**: rimuovere elementi ridondanti, testi di benvenuto vuoti (*happy talk*) e animazioni superflue che distraggono dal compito primario.

### La navigazione persistente (Persistent Navigation)
L'insieme di elementi presenti identicamente in ogni pagina del sito per orientare l'utente:
- **Site ID (Logo)**: il punto fermo identitario, sempre cliccabile per tornare alla Home.
- **Sezioni primarie**: i livelli più alti della gerarchia del sito.
- **Utilities**: scorciatoie per funzioni trasversali (Accedi, Contatti, Lingua, Carrello).
- **Ricerca (Search Box)**: casella di input con bottone esplicito 'Cerca'.
- **Indicatore 'Tu sei qui'**: evidenziazione visiva inequivocabile della sezione attualmente attiva.
- **Briciole di pane (Breadcrumbs)**: percorso a ritroso per mostrare dove si colloca la pagina corrente nella gerarchia complessiva.""",
        "keyPoints": [
            "Gli utenti non leggono: scansionano a salti e adottano la prima opzione plausibile (Satisficing).",
            "Prima Legge di Krug: 'Non farmi pensare!'. L'interfaccia deve essere autoevidente.",
            "Importanza cruciale delle convenzioni del web: logo in alto a sinistra, carrello a destra, affordance palesi.",
            "Navigazione persistente e indicatore 'Tu sei qui' per scongiurare il disorientamento dell'utente."
        ],
        "flashcards": [
            {
                "question": "Cosa indica il termine 'Satisficing' nel comportamento degli utenti web?",
                "answer": "La tendenza naturale a scegliere la prima opzione ragionevole e sufficiente invece di analizzare tutte le alternative per trovare la migliore."
            },
            {
                "question": "Quali elementi compongono la 'Navigazione Persistente' descritta nelle dispense?",
                "answer": "Site ID (logo cliccabile), sezioni primarie, utilities, casella di ricerca, indicatore 'Tu sei qui' e breadcrumbs."
            },
            {
                "question": "Cosa afferma la Prima Legge dell'usabilità di Steve Krug?",
                "answer": "'Non farmi pensare!': ogni schermata deve risultare autoevidente senza costringere l'utente a decifrare l'interfaccia."
            }
        ],
        "quiz": [
            {
                "question": "In base al concetto di 'Satisficing' di Herbert Simon ripreso da Krug, come agisce l'utente medio su una pagina web?",
                "options": [
                    "Esamina metodicamente tutti i link della pagina prima di selezionare il più autorevole",
                    "Clicca sulla prima opzione che sembra plausibile per raggiungere l'obiettivo con il minimo sforzo cognitivo",
                    "Memorizza la mappa del sito prima di iniziare la navigazione nei contenuti interni",
                    "Attende il caricamento completo di tutti gli script analitici prima di compiere qualsiasi azione"
                ],
                "correctIndex": 1,
                "explanation": "L'utente web non ottimizza alla perfezione, ma adotta la prima scelta ragionevole per risparmiare tempo ed energia mentale."
            },
            {
                "question": "Quale funzione svolgono le 'briciole di pane' (breadcrumbs) all'interno dell'architettura di navigazione?",
                "options": [
                    "Mostrano il percorso gerarchico dalla Home fino alla pagina corrente e offrono una via di risalita rapida",
                    "Memorizzano i cookie di tracciamento pubblicitario per le campagne di remarketing",
                    "Riducono il consumo di banda internet cancellando le immagini già visualizzate dall'utente",
                    "Indicano il numero di volte che l'utente ha inserito una password errata durante il login"
                ],
                "correctIndex": 0,
                "explanation": "I breadcrumbs mostrano la gerarchia strutturale della pagina all'interno del sito e consentono con un clic di risalire ai livelli superiori."
            },
            {
                "question": "Perché le convenzioni di design consolidate (es. logo in alto a sinistra, carrello in alto a destra) NON andrebbero stravolte?",
                "options": [
                    "Perché violare le convenzioni comporta sanzioni pecuniarie da parte del consorzio W3C",
                    "Perché sfruttano i modelli mentali già acquisiti dagli utenti, rendendo la navigazione istintiva e immediata",
                    "Perché i moderni browser web rifiutano di compilare fogli di stile con posizionamenti insoliti",
                    "Perché impediscono al server di eseguire la compressione gzip del codice sorgente HTML"
                ],
                "correctIndex": 1,
                "explanation": "Le convenzioni abbattono lo sforzo di apprendimento: l'utente sa già dove cercare i comandi senza dover decifrare l'interfaccia."
            },
            {
                "question": "In un'interfaccia web usabile, quale compito assolve l'indicatore 'Tu sei qui'?",
                "options": [
                    "Mostra le coordinate geografiche GPS dell'utente per scopi di geolocalizzazione",
                    "Evidenzia in modo evidente nella barra di navigazione la sezione o pagina in cui ci si trova",
                    "Segnala l'indirizzo IP del computer dell'utente per prevenire attacchi informatici",
                    "Attiva un suono acustico ogni volta che l'utente passa con il mouse sul menu principale"
                ],
                "correctIndex": 1,
                "explanation": "L'indicatore visivo 'Tu sei qui' fornisce orientamento spaziale immediato, prevenendo il disorientamento durante la navigazione."
            },
            {
                "question": "Cosa intende Krug con l'espressione 'Happy Talk' da eliminare sistematicamente dai siti web?",
                "options": [
                    "I messaggi di ringraziamento inviati via email al termine dell'acquisto di un prodotto",
                    "I testi introduttivi autocelebrativi e privi di informazioni utili (es. 'Benvenuti nel nostro sito')",
                    "I pulsanti grafici dedicati alla condivisione dei contenuti sui social network",
                    "I sistemi di chat automatica per il supporto clienti basati su intelligenza artificiale"
                ],
                "correctIndex": 1,
                "explanation": "L'happy talk è testo promozionale vuoto che gli utenti scavalcano sistematicamente e che aggiunge solo rumore visivo inutile."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega perché gli utenti scansionano invece di leggere e illustra come applicare la Prima Legge di Krug alla navigazione persistente.",
                "modelAnswer": "Gli utenti scansionano perché vanno di fretta, sanno che non serve leggere tutto per raggiungere il loro scopo e adottano il satisficing (scelta della prima opzione plausibile). La Prima Legge di Krug ('Non farmi pensare!') si applica alla navigazione persistente rendendo ogni elemento ovvio e convenzionale: il logo in alto a sinistra rimanda sempre alla Home, i link principali sono chiaramente cliccabili, la barra di ricerca è visibile con bottone esplicito e l'indicatore visivo 'Tu sei qui' segnala inequivocabilmente dove l'utente si trova nella gerarchia."
            }
        ]
    },

    # 11. Style tile
    {
        "id": "dispense-c11",
        "number": 11,
        "title": "Style tile",
        "subtitle": "La metodologia di Samantha Warren, il ponte tra moodboard astratte e mockup definitivi",
        "readTime": "8 min",
        "summary": """### L'origine e lo scopo dello Style Tile
Lo **Style Tile** è un artefatto visivo ideato dalla designer Samantha Warren per risolvere un problema storico della progettazione web: il divario comunicativo tra designer e committente.
- Da un lato, le **Moodboard** tradizionali (collage di foto, texture e ispirazioni artistiche) risultano spesso **troppo astratte**: il cliente fatica a immaginare come quelle sensazioni si tradurranno in un sito reale.
- Dall'altro, i **Mockup ad alta fedeltà completi** richiedono decine di ore di lavoro minuzioso: se il cliente rifiuta lo stile visivo o la direzione cromatica, gran parte del lavoro di impaginazione viene cestinato con enormi costi e frustrazione.

### Che cos'è uno Style Tile
Lo Style Tile si colloca esattamente a metà strada:
- È un **foglio di campioni visivi digitali** che presenta l'identità del brand applicata ai veri elementi dell'interfaccia, ma **completamente decontestualizzata dalla struttura rigida del layout**.
- Raccoglie in un unico foglio conciso:
  1. **Palette cromatica**: campioni dei colori primari, secondari, sfondi e neutri.
  2. **Coppie tipografiche reali**: campioni di titoli (`H1`, `H2`), sottotitoli e paragrafi composti con i font effettivi del progetto.
  3. **Componenti interattivi chiave**: bottoni nello stato normale e hover, campi form, selettori.
  4. **Iconografia e pattern visivi**: stile dei tratti iconici, trattamenti fotografici o illustrativi, texture e bordi.

### I grandi vantaggi operativi
1. **Velocità di iterazione**: produrre tre Style Tile con direzioni visive radicalmente diverse (es. uno 'Minimalista ed Elegante', uno 'Audace e Tecnologico', uno 'Caldo e Umano') richiede una frazione del tempo di tre mockup interi.
2. **Coinvolgimento del cliente**: permette di concordare il 'tono di voce' visivo e la palette con gli stakeholder prima di affrontare l'impaginazione dei contenuti.
3. **Ponte verso il Design System**: gli elementi validati nello Style Tile costituiscono il nucleo originario dei futuri Design Tokens e componenti del Design System.""",
        "keyPoints": [
            "Metodologia di Samantha Warren: ponte tra l'astrattezza della moodboard e la rigidità del mockup.",
            "Raccoglie font reali, palette di colori, bottoni, trattamenti di immagini e icone slegati dalla struttura della pagina.",
            "Consente di testare e concordare rapidamente diverse direzioni visive con i committenti.",
            "Costituisce il seme genetico da cui si sviluppano i token del Design System."
        ],
        "flashcards": [
            {
                "question": "Chi ha ideato la metodologia dello Style Tile e a quale scopo?",
                "answer": "La designer Samantha Warren, per creare un terreno d'intesa visivo rapido con i clienti a metà strada tra moodboard e mockup finito."
            },
            {
                "question": "Quali elementi fondamentali sono contenuti in uno Style Tile?",
                "answer": "Palette cromatica, gerarchia tipografica reale (titoli e testo), stili di bottoni con stati hover, icone e campioni di texture."
            },
            {
                "question": "In che modo lo Style Tile fa risparmiare tempo al team di progettazione?",
                "answer": "Evita di disegnare decine di schermate definitive prima di sapere se il cliente approva lo stile grafico, i font e i colori scelti."
            }
        ],
        "quiz": [
            {
                "question": "Cosa differenzia uno Style Tile rispetto a una tradizionale Moodboard artistica?",
                "options": [
                    "La moodboard è scritta in codice HTML mentre lo Style Tile si disegna unicamente su tela ad olio",
                    "Lo Style Tile usa i reali elementi di interfaccia (font veri, bottoni, colori) invece di foto astratte di suggestione",
                    "La moodboard definisce la struttura del database mentre lo Style Tile gestisce le API esterne",
                    "Non sussiste alcuna differenza reale, trattandosi esattamente dello stesso documento di lavoro"
                ],
                "correctIndex": 1,
                "explanation": "Mentre la moodboard raccoglie ispirazioni generiche, lo Style Tile mostra già i veri mattoni dell'interfaccia (font, colori, pulsanti)."
            },
            {
                "question": "Per quale motivo presentare direttamente mockup completi ad alta fedeltà può rivelarsi rischioso?",
                "options": [
                    "Perché se il cliente rifiuta la direzione stilistica, decine di ore di impaginazione dettagliata vanno sprecate",
                    "Perché i mockup ad alta fedeltà non possono essere visualizzati su computer moderni",
                    "Perché la legge vieta di mostrare schermate complete prima della registrazione del marchio",
                    "Perché i mockup impediscono al programmatore di scegliere la versione di JavaScript preferita"
                ],
                "correctIndex": 0,
                "explanation": "Disegnare subito tutte le pagine è inefficiente: lo Style Tile consente di convalidare prima il tono visivo in poche ore."
            },
            {
                "question": "Quale tra i seguenti elementi NON appartiene tipicamente alla composizione di uno Style Tile?",
                "options": [
                    "I campioni delle tonalità cromatiche primarie e secondarie del brand",
                    "Il codice sorgente del database relazionale SQL per l'autenticazione degli utenti",
                    "Esempi di titoli H1 e paragrafi formattati con i font tipografici selezionati",
                    "Pulsanti interattivi di test con i relativi stati visivi di riposo e passaggio mouse"
                ],
                "correctIndex": 1,
                "explanation": "Lo Style Tile è un artefatto puramente visivo e linguistico; non contiene architettura di server né codice di backend."
            },
            {
                "question": "In che misura lo Style Tile agevola il dialogo tra designer e committente?",
                "options": [
                    "Consente di discutere e concordare l'atmosfera estetica prima di affrontare la complessità del layout",
                    "Costringe il committente ad accettare qualsiasi scelta grafica senza possibilità di critica",
                    "Elimina la necessità di definire il budget economico preventivo per la realizzazione del sito",
                    "Permette di calcolare in automatico il numero di visitatori che frequenteranno il portale"
                ],
                "correctIndex": 0,
                "explanation": "Focalizza la conversazione sulle qualità percettive (elegante, amichevole, autorevole) senza confonderle con la disposizione degli elementi."
            },
            {
                "question": "Quale legame sussiste tra gli elementi di uno Style Tile approvato e il successivo Design System?",
                "options": [
                    "Gli elementi visivi dello Style Tile diventano i valori base (Design Tokens) dei fogli di stile CSS",
                    "Tutti gli elementi dello Style Tile vengono distrutti e ricreati da capo in fase di programmazione",
                    "Lo Style Tile serve solo per la stampa e non ha alcuna relazione con il codice CSS del web",
                    "Il browser estrae le password di sistema a partire dai codici esadecimali dello Style Tile"
                ],
                "correctIndex": 0,
                "explanation": "I font, i codici esadecimali e i raggi di curvatura dello Style Tile diventano le variabili CSS (`:root`) del design system."
            }
        ],
        "openQuestions": [
            {
                "question": "Definisci il concetto di Style Tile ideato da Samantha Warren, illustrandone la struttura e spiegando perché ottimizza il processo di approvazione visiva.",
                "modelAnswer": "Lo Style Tile è un artefatto visivo concepito da Samantha Warren che colma il divario tra la vaghezza concettuale delle moodboard e l'eccessiva rigidità temporale dei mockup definitivi. Si compone di una scheda che raccoglie palette cromatica, coppie tipografiche reali (titoli e corpo del testo), stili dei bottoni con stati hover, icone e pattern visivi, slegati dalla struttura della pagina. Consente di produrre rapidamente alternative di stile diverse da concordare con il committente, evitando sprechi di lavoro prima dell'impaginazione completa."
            }
        ]
    },

    # 12. HTML e CSS
    {
        "id": "dispense-c12",
        "number": 12,
        "title": "HTML e CSS",
        "subtitle": "Tag, elementi inline vs block, attributi, semantica HTML5, Box Model e cascata CSS",
        "readTime": "11 min",
        "summary": """### I due linguaggi cardine del Front-End
Ogni pagina web si fonda sulla separazione tra **struttura/significato (HTML)** e **presentazione/stile (CSS)**:
- **HTML (HyperText Markup Language)**: definisce cosa sono gli elementi (un titolo, un paragrafo, un'immagine, un link). Non dovrebbe mai essere usato per decidere l'aspetto visivo.
- **CSS (Cascading Style Sheets)**: definisce come quegli elementi appaiono a schermo (colori, dimensioni, allineamenti, animazioni).

### Anatomia dei tag e degli attributi HTML
I tag delimitano il contenuto con apertura `<tag>` e chiusura `</tag>` (o sono auto-chiudenti come `<img>` e `<input>`).
Gli attributi forniscono informazioni supplementari inserite nel tag di apertura:
- `id`: identificatore univoco e irripetibile all'interno del documento (es. `id="header-principale"`).
- `class`: classificatore riutilizzabile su elementi multipli (es. `class="card-articolo"`).
- `href`: destinazione del link nel tag `<a>`.
- `src` e `alt`: sorgente del file e testo alternativo accessibile nel tag `<img>`.

### Elementi a Blocco (Block) vs Elementi in Linea (Inline)
- **Elementi Block** (`<div>`, `<p>`, `<h1>`-`<h6>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<ul>`, `<li>`):
  - Iniziano sempre su una nuova riga autonoma.
  - Occupano di default tutta la larghezza disponibile del genitore (100%).
  - Accettano proprietà `width`, `height`, `margin` e `padding` su tutti e quattro i lati.
- **Elementi Inline** (`<span>`, `<a>`, `<strong>`, `<em>`, `<code>`):
  - Rimangono all'interno del flusso del testo senza andare a capo.
  - Occupano solo lo spazio strettamente necessario al loro contenuto.
  - Ignorano `width` e `height`; i margini verticali non spostano le righe adiacenti.

### La Semantica di HTML5
HTML5 ha introdotto tag specifici per superare la proliferazione indistinta di `<div class="...">`:
- `<header>`: testata di pagina o di singola sezione.
- `<nav>`: blocco con i link primari di navigazione (riconosciuto come landmark dagli screen reader).
- `<main>`: il contenuto principale unico del documento (esclude testate e piè di pagina ripetuti).
- `<article>`: blocco di contenuto autonomo, autoconsistente e riutilizzabile (es. post di un blog o card).
- `<section>`: raggruppamento tematico all'interno di una pagina con un proprio titolo.
- `<aside>`: contenuto secondario correlato (barra laterale, note a margine).
- `<footer>`: chiusura di pagina con note legali, crediti e navigazione secondaria.

### Il Box Model e la cascata CSS
- **Box Model**: Content ➔ Padding ➔ Border ➔ Margin. La regola `box-sizing: border-box` include padding e bordo nella larghezza dichiarata.
- **La Cascata e Specificità**: quando più regole CSS competono per lo stesso elemento, prevale la regola con specificità più alta (Stili in linea > ID > Classi/Pseudo-classi > Tag) o, a parità di peso, l'ultima dichiarata nel foglio di stile.""",
        "keyPoints": [
            "Separazione netta: HTML per la semantica e struttura, CSS per stile, layout e interazioni visive.",
            "Differenza radicale tra elementi Block (a capo, 100% larghezza) ed elementi Inline (nel testo, no width/height).",
            "Tag semantici HTML5: header, nav, main, article, section, aside, footer per l'accessibilità.",
            "Il Box Model CSS e il calcolo delle specificità delle regole a cascata."
        ],
        "flashcards": [
            {
                "question": "Qual è la differenza fondamentale di comportamento tra un elemento Block e uno Inline?",
                "answer": "L'elemento Block va a capo occupando il 100% della larghezza e accetta width/height; l'elemento Inline fluisce nel testo e occupa solo lo spazio dei suoi caratteri."
            },
            {
                "question": "Qual è la differenza tra l'attributo 'id' e l'attributo 'class' in HTML?",
                "answer": "L'id è un identificatore univoco che può comparire una sola volta nella pagina; la classe è riutilizzabile su quanti elementi si desidera."
            },
            {
                "question": "A cosa serve il tag semantico HTML5 <main>?",
                "answer": "Identifica il contenuto centrale e predominante della pagina, escludendo parti ripetute su tutto il sito come header, menu e footer."
            }
        ],
        "quiz": [
            {
                "question": "Quale tra i seguenti tag HTML appartiene alla categoria degli elementi nativi di tipo 'Block'?",
                "options": [
                    "Il tag <span> impiegato per colorare singole parole all'interno di una frase",
                    "Il tag <p> utilizzato per strutturare interi paragrafi di testo autonomi",
                    "Il tag <strong> impiegato per evidenziare visivamente una parola in grassetto",
                    "Il tag <a> utilizzato per definire un collegamento ipertestuale in linea"
                ],
                "correctIndex": 1,
                "explanation": "Il tag `<p>` è un elemento di blocco: inizia su una nuova riga e occupa l'intera larghezza orizzontale a disposizione."
            },
            {
                "question": "Perché è considerata una cattiva pratica di sviluppo usare tag HTML con stili visivi obsoleti come <font> o <center>?",
                "options": [
                    "Perché vìola il principio cardine di separazione tra struttura semantica (HTML) e presentazione grafica (CSS)",
                    "Perché i moderni processori per smartphone non supportano più la lettura dei tag HTML",
                    "Perché tali tag richiedono la sottoscrizione di un abbonamento a pagamento con il W3C",
                    "Perché aumentano il rischio che il sito web venga infettato da virus informatici durante il rendering"
                ],
                "correctIndex": 0,
                "explanation": "HTML deve descrivere unicamente il significato logico dei dati; tutto l'aspetto estetico e visivo spetta al foglio di stile CSS."
            },
            {
                "question": "Quale elemento semantico introdotto da HTML5 è specificamente designato per racchiudere un contenuto autonomo e riutilizzabile (come una card di un articolo)?",
                "options": [
                    "Il tag <nav>",
                    "Il tag <article>",
                    "Il tag <aside>",
                    "Il tag <footer>"
                ],
                "correctIndex": 1,
                "explanation": "<article> rappresenta un blocco di contenuto autosufficiente che avrebbe senso compiuto anche se distribuito separatamente (es. post o card)."
            },
            {
                "question": "Quale selettore CSS possiede la specificità (peso gerarchico) maggiore nella risoluzione dei conflitti di stile a cascata?",
                "options": [
                    "Il selettore di tag generico (es. p)",
                    "Il selettore di classe (es. .card)",
                    "Il selettore di ID (es. #bottone-principale)",
                    "Il selettore universale asterisco (*)"
                ],
                "correctIndex": 2,
                "explanation": "Nella scala di specificità CSS standard, un ID ha un peso nettamente superiore rispetto a classi, pseudo-classi o selettori di tag."
            },
            {
                "question": "Quale attributo obbligatorio deve essere sempre fornito sul tag <img> per garantire l'accessibilità visiva?",
                "options": [
                    "L'attributo alt che fornisce una descrizione testuale per gli screen reader dei non vedenti",
                    "L'attributo style contenente istruzioni di animazione tridimensionale",
                    "L'attributo target che impone l'apertura dell'immagine in una nuova scheda",
                    "L'attributo download per forzare il salvataggio del file sul disco rigido dell'utente"
                ],
                "correctIndex": 0,
                "explanation": "L'attributo `alt` (alternative text) è il requisito cardine per descrivere l'immagine a chi non può vederla o se l'immagine non si carica."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega la separazione delle responsabilità tra HTML e CSS, illustrando la differenza tra elementi block e inline e il valore della semantica HTML5.",
                "modelAnswer": "HTML definisce la struttura semantica dei contenuti, mentre CSS governa l'aspetto visivo e il layout. Gli elementi block (div, p, article, header) vanno a capo e occupano il 100% della larghezza, accettando dimensioni su tutti i lati; gli elementi inline (span, a, strong) scorrono nel flusso del testo senza andare a capo e non accettano width o height. I tag semantici HTML5 (header, nav, main, article, section, footer) sono fondamentali perché attribuiscono significato strutturale al codice, consentendo ai motori di ricerca di indicizzare i contenuti e agli screen reader di fornire navigazione autonoma tramite landmarks."
            }
        ]
    },

    # 13. Responsive web design
    {
        "id": "dispense-c13",
        "number": 13,
        "title": "Responsive web design",
        "subtitle": "I tre pilastri di Ethan Marcotte, Media Queries, Mobile First e Viewport",
        "readTime": "10 min",
        "summary": """### L'era della frammentazione dei dispositivi
Prima del 2010, i siti web venivano progettati su tele a larghezza fissa (es. 960 o 1024 pixel).
Con l'esplosione di smartphone, tablet, laptop, schermi widescreen 4K e display pieghevoli, l'idea di un layout fisso è diventata insostenibile.
Nel 2010, il designer Ethan Marcotte ha formalizzato la teoria del **Responsive Web Design (RWD)**: il web non deve costringere gli utenti ad adattarsi allo schermo, ma è l'interfaccia che deve flettersi e adattarsi al contesto di visualizzazione.

### I tre pilastri tecnici di Ethan Marcotte
Il Responsive Web Design non è una tecnologia singola, ma la sinergia di tre elementi tecnici:
1. **Griglie Fluide (Fluid Grids)**:
   - Abbandono delle dimensioni rigide in pixel per contenitori e colonne a favore di proporzioni percentuali (`%`), unità frazionarie (`fr`) o funzioni fluide (`minmax()`, `clamp()`).
   - La formula classica di Marcotte:
     $$\\text{Target} \\div \\text{Context} = \\text{Result (\\%)}$$
2. **Immagini Flessibili (Flexible Images / Media)**:
   - Le immagini e i video non devono mai eccedere la larghezza del loro contenitore.
   - La regola d'oro universale in CSS:
     ```css
     img, video {
       max-width: 100%;
       height: auto;
     }
     ```
   - L'immagine scala rimpicciolendosi quando il contenitore si stringe, preservando sempre il proprio rapporto d'aspetto (aspect-ratio).
3. **Media Queries (CSS3)**:
   - Istruzioni condizionali che consentono di applicare specifici blocchi di regole CSS solo al verificarsi di determinate condizioni del dispositivo (larghezza, orientamento, risoluzione, preferenza tema scuro).

### La filosofia 'Mobile First' (Luke Wroblewski)
- Tradizionalmente si progettava per il desktop per poi 'tagliare' o nascondere elementi su mobile (approccio a ritroso o *Desktop First* con media query `max-width`).
- La metodologia **Mobile First** inverte radicalmente la prospettiva:
  - Si progetta e sviluppa prima di tutto per il vincolo più severo: lo schermo piccolo del cellulare (single column, gerarchia essenziale, nessun hover).
  - Si scrive il CSS base per il mobile senza alcuna media query.
  - Si arricchisce progressivamente il layout per tablet e desktop tramite media queries basate su larghezza minima (`min-width`):
    ```css
    /* Stile base: Mobile (1 colonna) */
    .card-grid { display: grid; grid-template-columns: 1fr; }

    /* Breakpoint Tablet */
    @media (min-width: 768px) {
      .card-grid { grid-template-columns: repeat(2, 1fr); }
    }

    /* Breakpoint Desktop */
    @media (min-width: 1024px) {
      .card-grid { grid-template-columns: repeat(3, 1fr); }
    }
    ```
- **Vantaggi del Mobile First**: codice CSS più snello ed elegante, tempi di caricamento più veloci per gli smartphone e chiarezza gerarchica garantita.""",
        "keyPoints": [
            "I 3 pilastri di Ethan Marcotte: Griglie Fluide, Immagini Flessibili e Media Queries.",
            "Regola universale per immagini responsive: max-width: 100% e height: auto.",
            "Strategia Mobile First: partire dal vincolo più stringente arricchendo il layout con media queries min-width.",
            "I breakpoint devono essere stabiliti dove il contenuto 'si rompe', non rincorrendo specifici modelli di smartphone."
        ],
        "flashcards": [
            {
                "question": "Quali sono i tre pilastri tecnici del Responsive Web Design teorizzati da Ethan Marcotte?",
                "answer": "1. Griglie fluide (fluid grids), 2. Immagini flessibili (flexible images), 3. Media queries CSS3."
            },
            {
                "question": "Quale regola CSS assicura che un'immagine non trabocchi dal suo contenitore mantenendo le proporzioni?",
                "answer": "img { max-width: 100%; height: auto; }"
            },
            {
                "question": "Perché l'approccio Mobile First impiega media queries basate su 'min-width' invece di 'max-width'?",
                "answer": "Perché il codice base definisce l'interfaccia mobile semplice; le regole min-width aggiungono progressivamente complessità man mano che lo schermo si allarga."
            }
        ],
        "quiz": [
            {
                "question": "Chi ha teorizzato e formalizzato per la prima volta nel 2010 i principi del Responsive Web Design?",
                "options": [
                    "Steve Jobs",
                    "Ethan Marcotte",
                    "Jakob Nielsen",
                    "Tim Berners-Lee"
                ],
                "correctIndex": 1,
                "explanation": "Ethan Marcotte pubblicò il fondamentale articolo 'Responsive Web Design' nel maggio 2010 su A List Apart, coniando la disciplina."
            },
            {
                "question": "Cosa accade se a un'immagine web non viene applicata la proprietà 'max-width: 100%' all'interno di una colonna fluida?",
                "options": [
                    "L'immagine conserva i suoi pixel fissi e se è più grande del contenitore genera uno sgradevole scroll orizzontale",
                    "Il browser rimpicciolisce automaticamente tutti i caratteri tipografici della pagina per compensare",
                    "L'immagine viene cancellata dalla memoria del browser per motivi di sicurezza informatica",
                    "Il server di hosting converte automaticamente il file da JPEG a vettoriale SVG"
                ],
                "correctIndex": 0,
                "explanation": "Senza max-width: 100%, l'immagine mantiene la sua dimensione nativa e travalica i bordi del contenitore quando questo si restringe."
            },
            {
                "question": "Nel paradigma 'Mobile First', dove e come viene definito il layout per gli schermi degli smartphone?",
                "options": [
                    "All'interno di una complessa media query impostata su max-width: 320px",
                    "Nel codice CSS principale all'inizio del file, senza alcuna media query protettiva",
                    "In un secondo file CSS separato caricato tramite script dinamico JavaScript",
                    "Esclusivamente attraverso attributi di stile inline all'interno dei tag HTML"
                ],
                "correctIndex": 1,
                "explanation": "Mobile First impone che lo stile base naturale sia proprio quello per smartphone; le media queries min-width intervengono solo per allargare."
            },
            {
                "question": "In base a quale criterio dovrebbero essere scelti i punti di interruzione (breakpoint) in un foglio di stile responsivo?",
                "options": [
                    "Rincorrendo esattamente i pixel dei modelli di iPhone appena usciti sul mercato commerciale",
                    "Nel punto esatto in cui il contenuto e il layout iniziano a 'rompersi' o risultare scomposti",
                    "A intervalli rigorosamente identici e costanti di cento pixel a partire da zero",
                    "Unicamente su raccomandazione scritta formulata dai motori di ricerca nelle console web"
                ],
                "correctIndex": 1,
                "explanation": "I breakpoint efficaci non inseguono la miriade di schermi sul mercato, ma si posizionano dove il contenuto necessita di una riorganizzazione strutturale."
            },
            {
                "question": "Quale unità di misura moderna in CSS consente di creare dimensioni tipografiche che scalano fluidamente tra un minimo e un massimo?",
                "options": [
                    "La funzione clamp(minimo, ideale, massimo)",
                    "L'unità fissa in millimetri tipografici pt",
                    "La pseudo-classe :nth-child",
                    "La proprietà z-index a incremento automatico"
                ],
                "correctIndex": 0,
                "explanation": "La funzione CSS `clamp()` definisce un valore ideale fluido (es. con unità di viewport vw) racchiuso tra una soglia minima e una massima."
            }
        ],
        "openQuestions": [
            {
                "question": "Descrivi i tre pilastri del Responsive Web Design formulati da Ethan Marcotte e spiega la logica metodologica dell'approccio Mobile First.",
                "modelAnswer": "I tre pilastri sono: 1. Griglie Fluide (layout proporzionali basati su percentuali o unità fr anziché pixel fissi); 2. Immagini Flessibili (immagini vincolate da max-width: 100% e height: auto per scalare senza deformarsi né debordare); 3. Media Queries (regole condizionali CSS per adattare il layout alle dimensioni dello schermo). L'approccio Mobile First progetta preliminarmente per lo schermo mobile (il vincolo più rigoroso) scrivendo il CSS base senza media queries, e utilizza successivamente media queries min-width per arricchire progressivamente il layout su tablet e desktop, ottimizzando velocità e pulizia del codice."
            }
        ]
    },

    # 14. Javascript e Client vs Server
    {
        "id": "dispense-c14",
        "number": 14,
        "title": "Javascript",
        "subtitle": "Linguaggio client-side, manipolazione del DOM, eventi e differenze strutturali tra Client e Server",
        "readTime": "11 min",
        "summary": """### Il terzo pilastro del Web: JavaScript
Se l'HTML rappresenta la struttura portante della casa e il CSS ne definisce l'aspetto estetico e le finiture, **JavaScript** costituisce l'impianto elettrico e domotico: conferisce intelligenza, reattività e comportamento dinamico.
Nato nel 1995 ad opera di Brendan Eich in Netscape, JavaScript è l'unico linguaggio di programmazione eseguito **nativamente all'interno di tutti i browser web del mondo**.

### Il Document Object Model (DOM) e la gestione degli eventi
- **Il DOM**: quando il browser scarica il file HTML, costruisce una rappresentazione ad albero in memoria chiamata DOM (Document Object Model).
- JavaScript interagisce con il DOM per:
  - Selezionare elementi (`document.querySelector('.bottone')`).
  - Modificare contenuti o attributi in tempo reale (`el.textContent = 'Nuovo Testo'`).
  - Aggiungere o togliere classi CSS dinamiche (`el.classList.toggle('attivo')`).
- **Gli Eventi (Event Listeners)**:
  - JavaScript rimane in ascolto delle azioni dell'utente sullo schermo: click del mouse, digitazione da tastiera, scroll della pagina, submit di un form o caricamento completato.
  - Al verificarsi dell'evento, esegue una funzione di risposta (**callback**).

### Differenze architetturali tra Client e Server
La comprensione dei ruoli di Client e Server è un passaggio fondamentale per qualsiasi designer o sviluppatore web:

#### 1. Il Client (Front-End)
- È il dispositivo dell'utente (lo smartphone, il tablet, il personal computer) e l'applicazione browser che esegue il codice (Chrome, Safari, Firefox).
- **Cosa fa**:
  - Renderizza l'interfaccia grafica calcolando il CSS.
  - Esegue JavaScript localmente per gestire l'interattività immediata, le animazioni, la validazione preliminare dei moduli e il cambio di stato senza ricaricare la pagina.
- **Limiti e insidie**:
  - L'ambiente client è **intrinsecamente insicuro**: l'utente può ispezionare, modificare o disabilitare qualsiasi riga di codice JavaScript tramite i DevTools. Non si possono mai memorizzare chiavi segrete o convalidare pagamenti solo sul client!

#### 2. Il Server (Back-End)
- È un computer remoto (o cluster cloud) permanentemente connesso alla rete che risponde alle richieste del client via protocollo HTTP/HTTPS.
- **Cosa fa**:
  - Esegue codice back-end sicuro (Node.js, Python, PHP, Java, Go).
  - Interroga e aggiorna i database persistenti (SQL o NoSQL).
  - Gestisce l'autenticazione sicura degli utenti, la crittografia delle password, le transazioni bancarie e l'invio di email.
  - Invia al browser le pagine web o i dati strutturati in formato **JSON** tramite API REST o GraphQL.

### La sinergia moderna: le Single Page Application (SPA)
Nelle applicazioni moderne (come la piattaforma di studio che stai utilizzando), JavaScript sul client riceve dati strutturati (array JSON) e genera dinamicamente le card, i quiz e i punteggi all'interno del browser, consentendo una velocità e fluidità di navigazione istantanea senza mai ricaricare la pagina.""",
        "keyPoints": [
            "JavaScript conferisce comportamento e dinamismo interagendo con l'albero del DOM.",
            "Meccanismo degli eventi: ascolto di azioni utente (click, input, scroll) ed esecuzione di callback.",
            "Il Client (browser) gestisce interfaccia e interattività immediata ma è manipolabile dall'utente.",
            "Il Server (back-end) gestisce database, sicurezza, autenticazione crittografica e logiche di business protette."
        ],
        "flashcards": [
            {
                "question": "Che cos'è il Document Object Model (DOM) manipolato da JavaScript?",
                "answer": "È la rappresentazione ad albero in memoria che il browser crea a partire dal codice HTML, permettendo a JavaScript di modificare testi, stili e classi in tempo reale."
            },
            {
                "question": "Perché la convalida dei dati di un form non può essere affidata esclusivamente a JavaScript sul client?",
                "answer": "Perché un utente malintenzionato può facilmente disabilitare o manomettere il codice JavaScript nel browser; il server deve sempre eseguire la convalida finale sicura."
            },
            {
                "question": "Qual è il ruolo primario del Server rispetto al Client in un'applicazione web?",
                "answer": "Il Server gestisce in modo protetto i database, l'autenticazione degli account e le transazioni economiche, inviando al Client i dati necessari."
            }
        ],
        "quiz": [
            {
                "question": "Cosa accade nel browser quando JavaScript esegue il metodo 'classList.toggle('active')' su un elemento?",
                "options": [
                    "Aggiunge la classe se non presente, oppure la rimuove se è già presente, aggiornando lo stile CSS",
                    "Elimina permanentemente l'elemento dal codice sorgente salvato sul server",
                    "Invia una notifica di avvenuta violazione di copyright al consorzio internazionale W3C",
                    "Forza il riavvio del sistema operativo dell'utente per applicare la modifica"
                ],
                "correctIndex": 0,
                "explanation": "`classList.toggle()` alterna la presenza di una classe CSS: se c'è la toglie, se manca la aggiunge, permettendo cambi di stato dinamici."
            },
            {
                "question": "Quale tra le seguenti attività NON può essere delegata in sicurezza al solo ambiente Client (browser)?",
                "options": [
                    "Il cambio di colore di un bottone durante il passaggio del mouse con la pseudo-classe :hover",
                    "L'autenticazione della password di un utente e l'addebito su carta di credito di un acquisto",
                    "L'apertura di un menu hamburger a tendina su dispositivo mobile",
                    "Il controllo preliminare che una casella di testo non sia stata lasciata vuota"
                ],
                "correctIndex": 1,
                "explanation": "Il client è controllato dall'utente e può essere manomesso; operazioni critiche come autenticazione e pagamenti devono risiedere sul server."
            },
            {
                "question": "Cosa si intende per 'Event Listener' in linguaggio JavaScript?",
                "options": [
                    "Un componente hardware che registra l'audio ambientale nella stanza del programmatore",
                    "Una funzione in attesa di un'azione specifica dell'utente (come un click o un tasto premuto) per eseguire codice",
                    "Un virus informatico che rallenta la velocità di navigazione sul World Wide Web",
                    "Un tag HTML speciale deputato unicamente alla riproduzione di file musicali"
                ],
                "correctIndex": 1,
                "explanation": "Un listener (es. `addEventListener('click', fn)`) intercetta gli eventi innescati dall'utente ed esegue la logica associata."
            },
            {
                "question": "In quale formato strutturato viaggiano tipicamente i dati scambiati tra Server e Client nelle moderne API web?",
                "options": [
                    "Nel formato JSON (JavaScript Object Notation), leggero e facilmente interpretabile",
                    "In file eseguibili compressi in formato binario proprietario .exe",
                    "In documenti fotografici raster non compressi a risoluzione cinematografica",
                    "In nastri magnetici digitalizzati privi di qualsiasi indice di ricerca"
                ],
                "correctIndex": 0,
                "explanation": "JSON è lo standard universale per trasmettere dati strutturati (array e oggetti) tra server e applicazioni web."
            },
            {
                "question": "Quale vantaggio offrono le Single Page Application (SPA) basate su JavaScript rispetto ai siti web tradizionali?",
                "options": [
                    "Aggiornano dinamicamente porzioni della schermata senza dover ricaricare l'intera pagina a ogni clic",
                    "Funzionano anche su monitor spenti grazie alla trasmissione delle onde radio a bassa frequenza",
                    "Eliminano del tutto la necessità di avere un server per conservare le informazioni del database",
                    "Consentono di visualizzare siti internet anche in assenza di un collegamento elettrico"
                ],
                "correctIndex": 0,
                "explanation": "Le SPA aggiornano il DOM localmente in modo reattivo, offrendo un'esperienza d'uso fluida e istantanea simile a un'app nativa."
            }
        ],
        "openQuestions": [
            {
                "question": "Illustra il ruolo di JavaScript nel front-end web (DOM ed eventi) e analizza le differenze funzionali e di sicurezza tra Client e Server.",
                "modelAnswer": "JavaScript governa il comportamento dinamico del front-end: interagisce con il DOM (l'albero degli elementi in memoria) per manipolare stili, classi e contenuti in tempo reale e risponde alle interazioni dell'utente tramite Event Listeners. Il Client (il browser) è deputato al rendering grafico e alla reattività immediata, ma è un ambiente insicuro poiché accessibile e modificabile dall'utente. Il Server (back-end) opera in ambiente protetto: gestisce la persistenza sui database, la sicurezza crittografica, le transazioni e le logiche di business, dialogando con il client tramite API che scambiano dati strutturati in formato JSON."
            }
        ]
    }
]

print("Saving part 3 of dispense (10 to 14)...")
with open('dispense_part3_10to14.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)
