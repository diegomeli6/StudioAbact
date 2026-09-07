// Dati di studio approfonditi sul codice del Progetto Esame Cards
window.CARDS_DATA = [
  {
    "id": "cards-m1",
    "number": 1,
    "title": "Struttura HTML Semantica & Metadati",
    "subtitle": "Architettura di index.html, tag semantici, metadati viewport e accessibilità WCAG",
    "readTime": "9 min",
    "summary": "### Architettura del documento `index.html`\nIl progetto didattico d'esame *MagicTheArchive* è strutturato su una rigorosa impalcatura HTML5 conforme alle direttive W3C e WCAG.\n\n```html\n<!doctype html>\n<html lang=\"it\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>MagicTheArchive | Home</title>\n    <link rel=\"icon\" type=\"image/x-icon\" href=\"IMG/Icon.ico\" />\n    <link rel=\"stylesheet\" href=\"style.css\" />\n  </head>\n```\n\n### Analisi approfondita dei metadati nel `<head>`\n1. `<!doctype html>`: istruzione preambolare che forza il browser ad attivare la **modalità standard** (evitando la modalità *quirks* retrocompatibile che altererebbe il calcolo delle dimensioni del Box Model).\n2. `<html lang=\"it\">`: dichiara formalmente la lingua naturale del documento; è fondamentale per le tecnologie assistive (sintesi vocale degli screen reader che adotta la corretta fonetica) e per i motori di ricerca.\n3. `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />`: la direttiva imprescindibile del Responsive Web Design. Impone al viewport virtuale del dispositivo mobile di coincidere con la larghezza fisica dello schermo (`width=device-width`) con un fattore di scala iniziale pari a 1:1, prevenendo il ridimensionamento a 980px con conseguente testo microscopico.\n4. `<link rel=\"stylesheet\" href=\"style.css\" />`: inclusione del foglio di stile esterno senza attributi obsoleti come `type=\"text/css\"`.\n\n### Gerarchia e partizione semantica del `<body>`\nIl layout abbandona la vecchia prassi dei `<div>` generici a favore di tag semantici che descrivono il ruolo del contenuto:\n- `<header>`: testata del sito contenente il marchio (`.logo`), il selettore del menu mobile e il contenitore di navigazione `<nav>`.\n- `<nav>`: racchiude l'elenco non ordinato `<ul>` con i collegamenti ipertestuali alle sezioni principali (*Gioco*, *Espansioni*, *Formati*, *Chi Siamo*).\n- `<section class=\"hero\">`: area a forte impatto visivo (hero banner) che introduce il portale con titolo e call to action.\n- `<section class=\"categorie\">`: griglia di navigazione tassonomica verso le tre macro-aree di approfondimento.\n- `<section class=\"banner-lo-hobbit\">`: sezione promozionale tematica.\n- `<section class=\"lista-argomenti\">`: aggregatore editoriale delle card informative degli articoli.\n- `<footer>`: chiusura del documento con link secondari, copyright e riferimenti degli autori.",
    "keyPoints": [
      "Doctype HTML5 per garantire il rendering standard del Box Model.",
      "Meta viewport essenziale per sincronizzare la scala logica e fisica sui display mobili.",
      "Attributo lang='it' per l'accessibilità e la pronuncia corretta da parte degli screen reader.",
      "Struttura semantica rigorosa: header, nav, section, article e footer."
    ],
    "flashcards": [
      {
        "question": "Cosa accadrebbe su smartphone se si omettesse il meta tag viewport?",
        "answer": "Il browser mobile simulerebbe un monitor desktop largo circa 980px, rimpicciolendo drasticamente testi e card e forzando l'utente allo zoom manuale."
      },
      {
        "question": "Qual è il beneficio di utilizzare <nav> al posto di un generico <div class='menu'>?",
        "answer": "I browser e gli screen reader riconoscono il tag <nav> come punto di riferimento (landmark), consentendo agli utenti non vedenti di saltare direttamente alla navigazione."
      },
      {
        "question": "A cosa serve l'attributo aria-label='Menu' applicato alla label del menu mobile?",
        "answer": "Dato che l'etichetta contiene solo linee grafiche (span) prive di testo, l'aria-label fornisce una descrizione testuale accessibile alle tecnologie assistive."
      }
    ],
    "quiz": [
      {
        "question": "Nel codice di index.html, quale tag semantico è stato impiegato per raggruppare i link di navigazione primaria?",
        "options": [
          "Il tag semantico <nav> per identificare il blocco di collegamenti",
          "Il tag generico <div class='navigatore'> privo di semantica nativa",
          "Il tag accessorio <aside> riservato ai contenuti correlati secondari",
          "Il tag strutturale <section class='menu'> privo di valore landmark"
        ],
        "correctIndex": 0,
        "explanation": "Il tag HTML5 standard deputato a racchiudere i link di navigazione principale è <nav>, che funge da landmark accessibile."
      },
      {
        "question": "Qual è l'effetto tecnico dell'istruzione <meta name='viewport' content='width=device-width, initial-scale=1.0'>?",
        "options": [
          "Impedisce all'utente di effettuare qualsiasi ridimensionamento della pagina web",
          "Allinea la larghezza della finestra del browser alla larghezza fisica dello schermo",
          "Attiva automaticamente la modalità scura quando il dispositivo è a batteria bassa",
          "Comprime le immagini del sito web per risparmiare traffico dati sulla rete mobile"
        ],
        "correctIndex": 1,
        "explanation": "L'attributo width=device-width istruisce il browser del dispositivo mobile ad adattare la griglia di layout alla risoluzione effettiva dello schermo."
      },
      {
        "question": "Perché l'attributo lang='it' all'interno del tag <html> è critico per l'accessibilità?",
        "options": [
          "Consente ai sintetizzatori vocali per non vedenti di applicare le regole fonetiche italiane",
          "Obbliga il motore di ricerca a visualizzare il sito unicamente agli utenti con indirizzo IP italiano",
          "Modifica automaticamente i caratteri tipografici sostituendoli con font disegnati in Italia",
          "Traduce in tempo reale tutti i termini stranieri inseriti dagli autori all'interno del codice sorgente"
        ],
        "correctIndex": 0,
        "explanation": "Gli screen reader utilizzano la dichiarazione lang per selezionare il motore di sintesi vocale appropriato, evitando pronunce errate."
      },
      {
        "question": "Quale conseguenza provocherebbe la rimozione del preambolo <!doctype html> dalla prima riga del file?",
        "options": [
          "Il browser caricherebbe il file in modalità quirks alterando il calcolo delle dimensioni del Box Model",
          "Il server rifiuterebbe la connessione HTTP restituendo all'utente una schermata di errore 404",
          "Tutti i file CSS collegati verrebbero ignorati bloccando completamente il caricamento della pagina",
          "I comandi JavaScript perderebbero la capacità di selezionare gli elementi del DOM tramite querySelector"
        ],
        "correctIndex": 0,
        "explanation": "Senza doctype moderno, i browser attivano la Quirks Mode retrocompatibile, compromettendo il box model e il posizionamento CSS."
      },
      {
        "question": "All'interno di index.html, quale elemento racchiude ciascuna singola card di articolo nella sezione argomenti?",
        "options": [
          "Un blocco autonomo strutturato con tag semantico o classe specifica che ne delimita il contenuto",
          "Un tag <pre> pensato per visualizzare porzioni di codice sorgente non formattato",
          "Un semplice tag <span> in linea che non consente l'assegnazione di margini verticali",
          "Una tabella <table> a celle multiple utilizzata secondo i vecchi standard del web anni Novanta"
        ],
        "correctIndex": 0,
        "explanation": "Le card sono componenti modulari a blocco che raggruppano immagine, titolo, tassonomia e descrizione in una struttura semantica coerente."
      }
    ],
    "openQuestions": [
      {
        "question": "Descrivi i componenti essenziali del tag <head> in index.html e spiega perché la semantica HTML5 è superiore ai semplici tag <div> generici.",
        "modelAnswer": "Il tag <head> definisce la codifica caratteri UTF-8, il meta viewport per la corretta scalatura mobile, il titolo del documento per SEO e browser tab, la favicon e il collegamento al foglio di stile CSS. L'uso dei tag semantici HTML5 (header, nav, section, article, footer) è superiore ai semplici div perché fornisce significato alla struttura (landmarks), consentendo ai motori di ricerca di indicizzare correttamente la gerarchia e agli screen reader di consentire la navigazione facilitata per utenti con disabilità."
      }
    ]
  },
  {
    "id": "cards-m2",
    "number": 2,
    "title": "Il Box Model CSS & Azzeramento Globale",
    "subtitle": "Calcolo dello spazio, box-sizing: border-box, margini, padding e reset universale",
    "readTime": "10 min",
    "summary": "### Il Box Model nel World Wide Web\nNel linguaggio CSS, ogni elemento renderizzato sulla pagina viene calcolato come una scatola rettangolare (Box).\nIl Box Model si compone di quattro aree concentriche (dall'interno verso l'esterno):\n1. **Content**: l'area dove risiedono testo, immagini o elementi figli.\n2. **Padding (Spaziatura interna)**: lo spazio di respiro trasparente attorno al contenuto, ma all'interno dell'eventuale sfondo o bordo.\n3. **Border (Bordo)**: la linea perimetrale visibile che delimita il box.\n4. **Margin (Margine esterno)**: lo spazio trasparente che separa il box dagli elementi circostanti.\n\n### La rivoluzione di `box-sizing: border-box`\nNel modello tradizionale W3C (`content-box`):\n$$\\text{Larghezza totale} = \\text{width} + \\text{padding-left} + \\text{padding-right} + \\text{border-left} + \\text{border-right}$$\nQuesto rendeva il calcolo dei layout matematicamente instabile: assegnando `width: 50%` e `padding: 20px` a due colonne affiancate, la somma superava il 100%, spingendo la seconda colonna a capo.\n\nNel file `style.css` del progetto esame viene adottato il reset moderno universale:\n```css\n*,\n*::before,\n*::after {\n  box-sizing: border-box;\n  margin: 0;\n  padding: 0;\n}\n```\nCon `box-sizing: border-box`, la proprietà `width` include già al suo interno il padding e il bordo:\n$$\\text{Content effettivo} = \\text{width dichiarata} - (\\text{padding} + \\text{border})$$\nQuesto garantisce che un elemento impostato a `width: 33.333%` occuperà esattamente un terzo dello spazio disponibile, a prescindere dal padding interno assegnato.\n\n### Il collasso dei margini verticali (Margin Collapse)\nUn fenomeno cruciale del Box Model: quando due margini verticali adiacenti si toccano nel normale flusso di blocco, non si sommano, ma collassano nel margine più grande tra i due. Non accade invece sui margini orizzontali o all'interno di contenitori Flexbox e CSS Grid.",
    "keyPoints": [
      "I 4 livelli del Box Model: Content, Padding, Border e Margin.",
      "box-sizing: border-box include padding e bordo nella larghezza totale dichiarata.",
      "Il reset universale con selettore asterisco previene divergenze di layout cross-browser.",
      "Il margin collapsing agisce solo sui margini verticali nel normale flusso a blocchi."
    ],
    "flashcards": [
      {
        "question": "Qual è la formula di calcolo della larghezza totale di un elemento con box-sizing: border-box?",
        "answer": "La larghezza totale corrisponde esattamente alla proprietà width dichiarata (il padding e il bordo vengono sottratti dallo spazio del contenuto)."
      },
      {
        "question": "Perché nel reset globale di style.css vengono inclusi anche *::before e *::after?",
        "answer": "Per garantire che anche gli pseudo-elementi generati tramite CSS ereditino il medesimo modello border-box, prevenendo anomalie dimensionali."
      },
      {
        "question": "Cosa si intende per 'collasso dei margini' (margin collapse)?",
        "answer": "È il comportamento per cui due margini verticali adiacenti non si sommano, ma si fondono assumendo la dimensione del margine di valore maggiore."
      }
    ],
    "quiz": [
      {
        "question": "Se a un elemento con larghezza 300px e box-sizing: content-box aggiungiamo padding: 20px su tutti i lati, quale sarà la larghezza totale?",
        "options": [
          "300 pixel, poiché il padding si distribuisce internamente senza espandere la scatola",
          "340 pixel, poiché si sommano i 20px del padding sinistro e i 20px del padding destro",
          "320 pixel, poiché il browser applica il padding unicamente sulla coordinata sinistra",
          "260 pixel, poiché la misura del padding viene detratta dalla larghezza del contenuto"
        ],
        "correctIndex": 1,
        "explanation": "Con content-box, la larghezza finale è width (300px) + padding sinistro (20px) + padding destro (20px) = 340px."
      },
      {
        "question": "Quale vantaggio primario offre la regola globale 'box-sizing: border-box' applicata a tutti gli elementi?",
        "options": [
          "Rende il calcolo delle griglie intuitivo poiché padding e bordi non eccedono la larghezza impostata",
          "Elimina completamente la necessità di scrivere codice CSS specifico per i dispositivi mobili",
          "Aumenta la risoluzione grafica dei file immagine vettoriali inseriti nel documento HTML",
          "Consente di ignorare le regole di contrasto cromatico stabilite dalle linee guida WCAG"
        ],
        "correctIndex": 0,
        "explanation": "Con border-box, la larghezza impostata non viene mai superata dall'aggiunta di padding o bordi, facilitando la creazione di layout complessi."
      },
      {
        "question": "Quale tra le seguenti aree del Box Model CSS si trova immediatamente all'esterno del bordo?",
        "options": [
          "L'area del Padding, che circonda internamente la cornice visibile",
          "L'area del Margine (Margin), che distanzia l'elemento dai blocchi circostanti",
          "L'area del Content, che ospita direttamente la stringa di testo o immagine",
          "L'area dello Stroke vettoriale, generata solo durante le animazioni"
        ],
        "correctIndex": 1,
        "explanation": "Il Margin è lo strato più esterno del Box Model e si colloca esternamente rispetto al Border."
      },
      {
        "question": "Cosa caratterizza il fenomeno del 'Margin Collapsing' (collasso dei margini) in CSS?",
        "options": [
          "Si verifica unicamente tra elementi disposti in linea all'interno dello stesso paragrafo",
          "Due margini verticali contigui nel normale flusso si sovrappongono assumendo la misura del più grande",
          "I margini orizzontali di due card contigue si azzerano quando lo schermo supera i 1200px",
          "Il browser converte i valori dichiarati in pixel in percentuali relative al contenitore padre"
        ],
        "correctIndex": 1,
        "explanation": "Nel flusso normale di blocco, i margini verticali contigui collassano nel valore più elevato tra i due invece di sommarsi."
      },
      {
        "question": "Per quale motivo il reset universale in style.css azzera preliminarmente margin e padding con il selettore asterisco?",
        "options": [
          "Per rimuovere le spaziature predefinite dei browser che variano da un programma all'altro",
          "Per impedire all'utente di selezionare il testo della pagina web con il cursore del mouse",
          "Per disabilitare la barra di scorrimento verticale su monitor ad altissima definizione",
          "Per accelerare la velocità di download dei file multimediali dal server web remoto"
        ],
        "correctIndex": 0,
        "explanation": "Ogni browser applica margini e padding predefiniti differenti (es. su body, h1, p, ul); il reset garantisce un punto di partenza uniforme e prevedibile."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega dettagliatamente la differenza pratica tra box-sizing: content-box e box-sizing: border-box, indicando perché quest'ultimo è lo standard moderno.",
        "modelAnswer": "In content-box (default storico del browser), width e height si applicano solo al contenuto; padding e bordi si sommano all'esterno, rendendo difficoltoso il calcolo delle percentuali (es. due elementi al 50% con padding andranno a capo). In border-box, width e height rappresentano la misura finita della scatola: padding e bordi vengono assorbiti all'interno, riducendo lo spazio a disposizione del testo ma mantenendo invariate le dimensioni totali del blocco, rendendo i layout modulari stabili e calcolabili."
      }
    ]
  },
  {
    "id": "cards-m3",
    "number": 3,
    "title": "CSS Grid, Griglie Fluide & Layout Cards",
    "subtitle": "display: grid, repeat(3, 1fr), gap, allineamento e media queries responsive",
    "readTime": "11 min",
    "summary": "### La griglia bidimensionale: CSS Grid Layout\nA differenza di Flexbox (orientato prevalentemente a layout monodimensionali su riga o colonna), **CSS Grid** è stato progettato per governare simultaneamente righe e colonne bidimensionali.\n\nNel file `style.css` del progetto esame, la sezione `.lista-argomenti` e le categorie sono gestite con griglie avanzate:\n```css\n.lista-argomenti {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 30px;\n  max-width: 1200px;\n  margin: 0 auto;\n}\n```\n\n### Decostruzione delle istruzioni di griglia\n1. `display: grid`: attiva il contesto di formattazione a griglia sul contenitore genitore; tutti i figli diretti diventano istantaneamente *grid items*.\n2. `grid-template-columns: repeat(3, 1fr)`:\n   - La funzione `repeat(3, ...)` definisce 3 colonne ripetute con lo stesso schema.\n   - L'unità frazionaria `fr` (*fraction unit*) rappresenta una quota dello spazio libero disponibile nel contenitore. Tre colonne `1fr` si dividono lo spazio in tre parti identiche (33.333% ciascuna al netto dei gap).\n3. `gap: 30px`: definisce lo spazio di separazione (*gutters*) tra righe e colonne. Rispetto ai vecchi margini negativi di float, il `gap` non viene applicato sui bordi esterni del contenitore, garantendo un allineamento perfetto con i margini della pagina.\n4. `max-width: 1200px; margin: 0 auto;`: schema standard di contenimento per monitor widescreen: impedisce alle card di allargarsi all'infinito e centra il blocco orizzontalmente.\n\n### Strategia di adattamento responsive con Media Queries\nSu dispositivi mobili con schermo ridotto, una griglia a 3 colonne risulterebbe illeggibile. Nel progetto viene impiegata una media query con approccio progressivo:\n```css\n@media (max-width: 900px) {\n  .lista-argomenti {\n    grid-template-columns: repeat(2, 1fr);\n    gap: 20px;\n  }\n}\n\n@media (max-width: 600px) {\n  .lista-argomenti {\n    grid-template-columns: 1fr;\n    gap: 15px;\n  }\n}\n```\nIn questo modo il layout passa fluidamente da 3 colonne su desktop, a 2 colonne su tablet, fino a 1 colonna singola a tutta larghezza su smartphone.",
    "keyPoints": [
      "CSS Grid gestisce layout bidimensionali completi (righe e colonne contemporaneamente).",
      "L'unità fr divide lo spazio residuo in modo flessibile ed elastico.",
      "La proprietà gap gestisce gli spazi tra le celle senza intaccare i margini esterni del contenitore.",
      "Riorganizzazione responsive a breakpoint: 3 colonne (desktop) ➔ 2 colonne (tablet) ➔ 1 colonna (mobile)."
    ],
    "flashcards": [
      {
        "question": "Cosa rappresenta l'unità di misura 'fr' in CSS Grid?",
        "answer": "Rappresenta una frazione (fraction) dello spazio disponibile non occupato all'interno del contenitore di griglia."
      },
      {
        "question": "Qual è il vantaggio di usare la proprietà 'gap' rispetto ai margini tradizionali sui singoli elementi?",
        "answer": "La proprietà gap crea spaziatura solo tra gli elementi interni, senza aggiungere spazio indesiderato sui bordi esterni della griglia."
      },
      {
        "question": "Cosa indica la sintassi grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))?",
        "answer": "Crea una griglia intrinsecamente responsive che genera automaticamente quante più colonne da almeno 280px possibili, senza bisogno di media queries."
      }
    ],
    "quiz": [
      {
        "question": "Cosa indica l'istruzione CSS 'grid-template-columns: repeat(3, 1fr)'?",
        "options": [
          "Crea tre colonne identiche che dividono equamente lo spazio orizzontale libero disponibile",
          "Definisce una griglia con tre righe sovrapposte ciascuna alta esattamente un frame al secondo",
          "Ripete per tre volte la stessa immagine di sfondo all'interno del contenitore principale",
          "Limita il caricamento degli elementi a un massimo di tre articoli per sessione di navigazione"
        ],
        "correctIndex": 0,
        "explanation": "repeat(3, 1fr) dichiara tre colonne di ampiezza uniforme, ciascuna pari a 1 frazione dello spazio libero."
      },
      {
        "question": "Qual è la differenza concettuale fondamentale tra CSS Grid e Flexbox?",
        "options": [
          "Flexbox è bidimensionale mentre CSS Grid lavora esclusivamente lungo un singolo asse",
          "CSS Grid governa contemporaneamente righe e colonne, mentre Flexbox è monodimensionale",
          "Flexbox richiede l'esecuzione di codice JavaScript mentre CSS Grid è nativo per i browser",
          "CSS Grid funziona unicamente con immagini mentre Flexbox è riservato ai testi tipografici"
        ],
        "correctIndex": 1,
        "explanation": "Grid è un sistema bidimensionale (righe e colonne insieme), mentre Flexbox gestisce il flusso lungo un asse principale alla volta."
      },
      {
        "question": "A cosa serve la dichiarazione 'margin: 0 auto;' combinata con una 'max-width: 1200px'?",
        "options": [
          "A impedire al testo della pagina di essere evidenziato o copiato dagli utenti",
          "A centrare orizzontalmente il blocco dei contenuti impedendone l'espansione eccessiva su monitor grandi",
          "A forzare il download del font istituzionale dai server cloud di Google Fonts",
          "A bloccare lo scorrimento della pagina web fino al completamento del caricamento"
        ],
        "correctIndex": 1,
        "explanation": "max-width stabilisce il tetto massimo di larghezza, mentre margin: 0 auto calcola margini orizzontali uguali centrando il contenitore."
      },
      {
        "question": "Cosa accade alla proprietà 'gap: 30px' quando lo schermo scende sotto il breakpoint stabilito per smartphone?",
        "options": [
          "Viene solitamente ridotta (es. a 15px o 20px) per massimizzare l'area utile di lettura sui display piccoli",
          "Viene moltiplicata per due per evitare che i pollici dell'utente premano per errore i tasti vicini",
          "Viene disattivata del tutto trasformando la pagina in un unico blocco di testo continuo",
          "Provoca un errore di sintassi CSS che blocca il funzionamento dell'intero foglio di stile"
        ],
        "correctIndex": 0,
        "explanation": "Sui dispositivi mobili si riducono i gap tra le card per non sprecare lo spazio ristretto dello schermo."
      },
      {
        "question": "In un layout responsive, cosa accade alla griglia a 3 colonne quando viene visualizzata su uno schermo largo 400px?",
        "options": [
          "La media query riorganizza la griglia impostando una colonna singola a tutta larghezza (1fr)",
          "Le tre colonne si sovrappongono in trasparenza rendendo il testo illeggibile per l'utente",
          "Il browser disattiva la connessione di rete mobile per prevenire il surriscaldamento del dispositivo",
          "Le colonne vengono ritagliate sui lati nascondendo i due terzi dei contenuti della pagina"
        ],
        "correctIndex": 0,
        "explanation": "Sui monitor compatti da smartphone la media query commuta la griglia su un'unica colonna incolonnando verticalmente le card."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega la sintassi di CSS Grid utilizzata per la sezione lista-argomenti e descrivi come viene gestita la transizione da desktop a mobile.",
        "modelAnswer": "La sezione adotta display: grid con grid-template-columns: repeat(3, 1fr) e gap: 30px all'interno di un contenitore con max-width: 1200px e margin: 0 auto. Su desktop questo genera tre colonne perfette di larghezza identica con 30px di spazio tra loro. Tramite media queries a max-width: 900px e 600px, le colonne vengono progressivamente ridotte a 2 e infine a 1 singola colonna per gli smartphone, garantendo leggibilità ottimale senza scroll orizzontale."
      }
    ]
  },
  {
    "id": "cards-m4",
    "number": 4,
    "title": "Custom Properties CSS (:root) & Design System Cromatico",
    "subtitle": "Variabili native CSS, pseudo-classe :root, palette di progetto e consistenza del design system",
    "readTime": "8 min",
    "summary": "### Variabili CSS native (Custom Properties)\nPrima dell'introduzione delle Custom Properties, modificare una tonalità di colore o un valore di margine in un file CSS complesso richiedeva un'operazione rischiosa di 'Trova e Sostituisci'.\nLe Custom Properties CSS permettono di memorizzare valori riutilizzabili con supporto nativo nel browser (e senza necessità di precompilatori come Sass o Less).\n\nNel file `style.css` del progetto esame, la palette cromatica è centralizzata all'inizio del file tramite la pseudo-classe `:root`:\n```css\n:root {\n  --rosso: #ce3021;\n  --blu: #0c436b;\n  --giallo: #f7a827;\n  --nero: #1a1a1a;\n  --bianco: #ffffff;\n  --grigio-chiaro: #f4f4f4;\n  --grigio-scuro: #333333;\n  --font-principale: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n  --transizione-veloce: 0.3s ease;\n}\n```\n\n### La pseudo-classe `:root` e l'ereditarietà\n- `:root` seleziona l'elemento radice del documento (che in HTML coincide con il tag `<html>`), ma possiede una specificità superiore.\n- Definire le variabili in `:root` le rende disponibili in **modalità globale** a qualsiasi selettore della pagina attraverso la funzione `var(--nome-variabile)`.\n- Esempio pratico nel progetto:\n```css\n.card-titolo {\n  color: var(--blu);\n  font-family: var(--font-principale);\n  transition: color var(--transizione-veloce);\n}\n\n.card-titolo:hover {\n  color: var(--rosso);\n}\n```\n\n### Vantaggi sistemici nel Design System\n1. **Consistenza cromatica**: impedisce la proliferazione accidentale di codici esadecimali leggermente diversi (es. `#ce3021` vs `#cd2f20`).\n2. **Manutenibilità immediata**: la modifica del valore in un unico punto (`:root`) aggiorna all'istante bottoni, bordi, testi e hover in centinaia di regole CSS.\n3. **Predisposizione al Dark Mode**: ridefinendo i valori delle variabili all'interno di una classe `.dark-theme` o di una media query `@media (prefers-color-scheme: dark)`, l'intero sito cambia tema senza duplicare le dichiarazioni di stile.",
    "keyPoints": [
      "Le Custom Properties si dichiarano con il prefisso doppio trattino (--nome).",
      "La pseudo-classe :root garantisce visibilità globale delle variabili in tutto il documento.",
      "I valori si richiamano tramite la funzione nativa var(--nome-variabile).",
      "Garantiscono consistenza visiva, rapida manutenibilità e facilità di tematizzazione (es. Dark Mode)."
    ],
    "flashcards": [
      {
        "question": "Con quale prefisso sintattico devono iniziare le variabili CSS native?",
        "answer": "Devono obbligatoriamente iniziare con due trattini consecutivi (es. --colore-primario)."
      },
      {
        "question": "A quale elemento del DOM corrisponde la pseudo-classe :root in un documento HTML?",
        "answer": "Corrisponde all'elemento radice <html>, ma con un peso di specificità superiore rispetto a un semplice selettore di tag."
      },
      {
        "question": "Come si richiama il valore di una variabile CSS all'interno di una proprietà?",
        "answer": "Utilizzando la funzione nativa var(), ad esempio: color: var(--rosso);"
      }
    ],
    "quiz": [
      {
        "question": "Quale vantaggio offrono le Custom Properties CSS rispetto all'inserimento diretto di codici colore esadecimali?",
        "options": [
          "Centralizzano i valori cromatici permettendo modifiche globali immediate e garantendo consistenza visiva",
          "Riducono il consumo energetico della scheda video del visitatore durante la navigazione sul web",
          "Eliminano la necessità di inserire immagini all'interno delle card e delle sezioni del sito",
          "Consentono di convertire automaticamente il testo in caratteri tridimensionali animati"
        ],
        "correctIndex": 0,
        "explanation": "Le Custom Properties fungono da token di design: centralizzano valori e colori, assicurando coerenza ed estrema manutenibilità."
      },
      {
        "question": "Perché le variabili globali del foglio di stile vengono dichiarate all'interno del selettore ':root'?",
        "options": [
          "Perché :root rappresenta l'elemento radice del documento rendendo le proprietà ereditabili ovunque",
          "Perché i browser web bloccano qualsiasi variabile dichiarata all'interno di selettori di classe",
          "Perché :root è un'istruzione riservata unicamente al caricamento dei file di script esterni",
          "Perché impedisce agli utenti di ispezionare il codice sorgente tramite i DevTools del browser"
        ],
        "correctIndex": 0,
        "explanation": "Dichiarando le custom properties su :root (elemento radice <html>), esse vengono ereditate a cascata da tutti gli elementi del DOM."
      },
      {
        "question": "Qual è la sintassi corretta per applicare il colore definito nella variabile '--blu' al bordo di un elemento?",
        "options": [
          "border: 2px solid get(--blu);",
          "border: 2px solid var(--blu);",
          "border: 2px solid $--blu;",
          "border: 2px solid #--blu;"
        ],
        "correctIndex": 1,
        "explanation": "La funzione standard CSS per estrarre il valore di una custom property è var(--nome-variabile)."
      },
      {
        "question": "Come si definisce un valore di riserva (fallback) nella funzione var() qualora la variabile non fosse definita?",
        "options": [
          "Inserendo il valore alternativo come secondo argomento separato da virgola: var(--colore, #000);",
          "Scrivendo due volte il comando var in sequenza: var(--colore) or var(#000);",
          "Utilizzando il punto esclamativo prima del nome: var(!(--colore));",
          "I browser moderni non supportano valori di riserva nelle Custom Properties"
        ],
        "correctIndex": 0,
        "explanation": "La sintassi var(--variabile, valoreFallback) consente di specificare un valore di riserva qualora la variabile non sia dichiarata."
      },
      {
        "question": "In che modo le Custom Properties facilitano l'implementazione di un tema scuro (Dark Mode)?",
        "options": [
          "Basta sovrascrivere i valori delle variabili colore all'interno della media query prefers-color-scheme",
          "Richiedono di duplicare l'intera struttura dei file HTML creando una seconda cartella separata",
          "Invertono automaticamente i pixel delle immagini fotografiche caricate sul server",
          "Costringono il browser a ricaricare l'intera pagina da zero a ogni variazione di luce"
        ],
        "correctIndex": 0,
        "explanation": "È sufficiente riassegnare i valori esadecimali delle variabili dentro la classe o media query del dark theme, senza toccare i selettori dei componenti."
      }
    ],
    "openQuestions": [
      {
        "question": "Mostra come vengono definite e utilizzate le Custom Properties in style.css e spiega il loro ruolo nella costruzione di un Design System.",
        "modelAnswer": "In style.css le variabili vengono definite all'interno di :root con il prefisso doppio trattino (es. --rosso: #ce3021; --transizione-veloce: 0.3s ease;). Vengono richiamate nelle regole CSS con la funzione var(--rosso). In un Design System, queste variabili fungono da 'Design Tokens': standardizzano palette cromatiche, spaziature, tipografia e velocità di transizione, garantendo che l'intera squadra rispetti le linee guida del brand e consentendo modifiche globali istantanee."
      }
    ]
  },
  {
    "id": "cards-m5",
    "number": 5,
    "title": "Il Checkbox Hack per Menu Mobile Responsive CSS-only",
    "subtitle": "Interattività senza JavaScript: input checkbox, label for, :checked e combinatore fratello ~",
    "readTime": "10 min",
    "summary": "### Cos'è il 'Checkbox Hack'\nIl **Checkbox Hack** è una celebre tecnica di front-end che consente di creare componenti interattivi (come menu a scomparsa, fisarmoniche o toggle modali) **esclusivamente tramite HTML e CSS**, senza scrivere una singola riga di codice JavaScript.\n\n### I componenti della tecnica in `index.html`\n```html\n<!-- Checkbox reale nascosto -->\n<input type=\"checkbox\" id=\"menu-toggle\" class=\"menu-toggle\" />\n\n<!-- Pulsante grafico (Hamburger) associato al checkbox -->\n<label for=\"menu-toggle\" class=\"hamburger\" aria-label=\"Menu\">\n  <span></span>\n  <span></span>\n  <span></span>\n</label>\n\n<!-- Menu di navigazione che compare/scompare -->\n<nav class=\"nav-menu\">\n  <ul>\n    <li><a href=\"#\">Gioco</a></li>\n    <li><a href=\"#\">Espansioni</a></li>\n    <li><a href=\"#\">Formati</a></li>\n    <li><a href=\"#\">Chi Siamo</a></li>\n  </ul>\n</nav>\n```\n\n### Meccanica e selettori in `style.css`\n1. **Il collegamento tra label e input**:\n   - L'attributo `for=\"menu-toggle\"` sulla `<label>` punta all'attributo `id=\"menu-toggle\"` dell'input.\n   - Ogni volta che l'utente clicca sulla label (o sull'icona hamburger), il browser inverte lo stato del checkbox da spuntato (`checked`) a non spuntato (`unchecked`).\n2. **Occultamento visivo del checkbox nativo**:\n   - `display: none;` rende invisibile il quadrato del checkbox di sistema, lasciando a schermo solo la label stilizzata a tre barre.\n3. **La pseudo-classe `:checked` e il Combinatore Fratello Generale (`~`)**:\n```css\n/* Su desktop il menu è visibile, la label hamburger è nascosta */\n.menu-toggle, .hamburger { display: none; }\n\n/* Su mobile (max-width: 768px) */\n@media (max-width: 768px) {\n  .hamburger { display: flex; }\n  \n  .nav-menu {\n    display: none; /* Nascosto di default */\n    position: absolute;\n    top: 70px;\n    left: 0;\n    width: 100%;\n  }\n\n  /* Quando il checkbox è selezionato, mostra il nav fratello */\n  .menu-toggle:checked ~ .nav-menu {\n    display: block;\n  }\n}\n```\n\n### Perché il combinatore `~` è fondamentale?\nIl combinatore `A ~ B` seleziona qualsiasi elemento `B` che sia un **fratello successivo** di `A` all'interno dello stesso contenitore padre. Poiché `<nav>` si trova dopo `<input id=\"menu-toggle\">`, lo pseudo-stato `:checked` può pilotare l'apertura e chiusura del menu in modo dichiarativo e ultra-performante.",
    "keyPoints": [
      "Il Checkbox Hack consente l'interattività senza JavaScript sfruttando il comportamento nativo dei form HTML.",
      "La label con for='id' commuta lo stato del checkbox nascosto con display: none.",
      "Lo pseudo-selettore :checked rileva lo stato attivo dell'input.",
      "Il combinatore fratello generale (~) seleziona il menu adiacente attivandone la visibilità."
    ],
    "flashcards": [
      {
        "question": "Come fa la label a commutare lo stato del checkbox senza codice JavaScript?",
        "answer": "Grazie all'attributo for='menu-toggle' che associa nativamente l'interazione della label all'id del checkbox."
      },
      {
        "question": "Cosa seleziona in CSS la regola .menu-toggle:checked ~ .nav-menu?",
        "answer": "Seleziona l'elemento con classe .nav-menu che si trova come fratello successivo rispetto all'input .menu-toggle quando questo è spuntato."
      },
      {
        "question": "Qual è il limite principale del Checkbox Hack rispetto a un menu controllato da JavaScript?",
        "answer": "La gestione dell'accessibilità da tastiera e la chiusura automatica al click esterno (click-outside) risultano più complesse da gestire."
      }
    ],
    "quiz": [
      {
        "question": "Quale attributo HTML collega l'interazione di una <label> al rispettivo campo <input>?",
        "options": [
          "L'attributo for che deve contenere lo stesso valore dell'id dell'input",
          "L'attributo class che deve corrispondere al nome del file CSS",
          "L'attributo href che punta all'indirizzo della pagina di navigazione",
          "L'attributo name che viene letto unicamente dai motori di ricerca"
        ],
        "correctIndex": 0,
        "explanation": "L'attributo for della label associa il tocco o clic all'elemento input identificato dallo stesso id."
      },
      {
        "question": "Nel selettore '.menu-toggle:checked ~ .nav-menu', cosa rappresenta il simbolo tilde (~)?",
        "options": [
          "Il combinatore fratello generale che intercetta elementi fratelli successivi nello stesso genitore",
          "Il combinatore figlio diretto che seleziona solo elementi annidati immediatamente all'interno",
          "L'operatore logico di negazione che esclude tutti gli elementi privi di classe menu",
          "Il moltiplicatore di specificità che rende la regola prioritaria rispetto a !important"
        ],
        "correctIndex": 0,
        "explanation": "Il simbolo tilde (~) è il selettore fratello successivo: seleziona gli elementi fratelli che condividono lo stesso padre e seguono l'elemento."
      },
      {
        "question": "Quale pseudo-classe CSS permette di verificare se una casella di spunta è stata selezionata dall'utente?",
        "options": [
          "La pseudo-classe :hover",
          "La pseudo-classe :active",
          "La pseudo-classe :checked",
          "La pseudo-classe :focus"
        ],
        "correctIndex": 2,
        "explanation": ":checked è la pseudo-classe nativa di stato per radio button e checkbox selezionati."
      },
      {
        "question": "Perché nel foglio di stile la label hamburger viene impostata con 'display: none' sui monitor desktop?",
        "options": [
          "Perché su monitor grandi c'è spazio sufficiente per mostrare tutti i link estesi senza menu a tendina",
          "Perché i browser desktop non sono tecnicamente in grado di interpretare il combinatore fratello",
          "Perché la normativa sull'accessibilità vieta l'uso di icone grafiche su schermi superiori a 1024px",
          "Per velocizzare il caricamento della pagina riducendo il numero di nodi del Document Object Model"
        ],
        "correctIndex": 0,
        "explanation": "Sul desktop la barra di navigazione ha spazio orizzontale abbondante; l'hamburger menu ha senso solo sui display ristretti."
      },
      {
        "question": "Cosa accadrebbe se nel codice HTML l'elemento <nav class='nav-menu'> venisse posizionato PRIMA del tag <input>?",
        "options": [
          "Il combinatore fratello generale (~) non funzionerebbe poiché CSS seleziona solo elementi successivi",
          "Il browser scambierebbe automaticamente l'ordine dei tag nel DOM per garantire il funzionamento",
          "Il menu rimarrebbe perennemente visibile a schermo senza possibilità di essere nascosto",
          "Il foglio di stile verrebbe bloccato dal parser HTML impedendo l'applicazione dei font"
        ],
        "correctIndex": 0,
        "explanation": "In CSS non esiste un selettore di fratello precedente; il combinatore ~ funziona solo se il target si trova dopo l'elemento selezionato."
      }
    ],
    "openQuestions": [
      {
        "question": "Descrivi il funzionamento del Checkbox Hack implementato per il menu mobile, spiegando il ruolo di label, input, :checked e del combinatore ~.",
        "modelAnswer": "Il Checkbox Hack si basa su un input checkbox nascosto (id='menu-toggle') associato a una label con for='menu-toggle' stilizzata a hamburger. Al click sulla label, il browser commuta lo stato del checkbox. Nel CSS, tramite la regola .menu-toggle:checked ~ .nav-menu { display: block; }, quando il checkbox è spuntato, il combinatore fratello generale (~) seleziona il menu <nav> che segue nello stesso genitore e ne mostra i contenuti. Questo permette di gestire l'apertura e chiusura del menu in puro CSS senza dipendere da JavaScript."
      }
    ]
  },
  {
    "id": "cards-m6",
    "number": 6,
    "title": "Rendering Immagini, Aspect-Ratio & Microinterazioni Hover",
    "subtitle": "object-fit: cover, position: sticky, transizioni fluide e sollevamento card con translateY",
    "readTime": "9 min",
    "summary": "### Gestione e proporzioni delle immagini nelle card\nUno dei problemi classici nella progettazione delle card informative riguarda le immagini di anteprima caricate da fonti diverse: immagini con proporzioni eterogenee (orizzontali, quadrate, verticali) rischiano di deformarsi o di rompere l'allineamento della griglia.\n\nNel progetto esame, le immagini delle card sono regolate tramite:\n```css\n.card-img {\n  width: 100%;\n  height: 200px;\n  object-fit: cover;\n  display: block;\n}\n```\n- `width: 100%`: l'immagine occupa l'intera larghezza della card.\n- `height: 200px`: impone un'altezza fissa e uniforme per tutte le immagini della griglia.\n- `object-fit: cover`: l'istruzione chiave. Scala l'immagine mantenendone inalterate le proporzioni originali (aspect-ratio), ritagliando le parti eccedenti per riempire interamente il box di 200px senza alcuna distorsione anamorfica o stiramento visivo.\n\n### Posizionamento fluttuante: `position: sticky`\nPer la testata (`<header>`) viene impiegato il posizionamento ibrido sticky:\n```css\nheader {\n  position: sticky;\n  top: 0;\n  z-index: 1000;\n  background-color: var(--bianco);\n  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);\n}\n```\n- `position: sticky`: l'elemento si comporta come `relative` durante il normale scorrimento, ma non appena raggiunge la coordinata definita (`top: 0`), si 'ancora' al bordo superiore dello schermo rimanendo visibile durante tutta la navigazione.\n- `z-index: 1000`: garantisce che l'header passi sopra a tutti i contenuti e alle card durante lo scorrimento.\n\n### Microinterazioni e profondità visiva sulle Card\nPer conferire dinamismo e tangibilità fisica ai contenuti, ogni card risponde al passaggio del cursore con una microinterazione tridimensionale:\n```css\n.card {\n  background: var(--bianco);\n  border-radius: 8px;\n  overflow: hidden;\n  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);\n  transition: transform var(--transizione-veloce), box-shadow var(--transizione-veloce);\n}\n\n.card:hover {\n  transform: translateY(-8px);\n  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);\n}\n```\n- `transform: translateY(-8px)`: solleva la card di 8 pixel verso l'alto lungo l'asse verticale (l'asse Y cresce verso il basso nel browser, quindi un valore negativo sposta l'oggetto verso l'alto).\n- `transition`: interpola gradualmente nel tempo (0.3s) il movimento e l'intensità dell'ombra, comunicando all'utente l'affordance di cliccabilità in modo fluido e naturale.",
    "keyPoints": [
      "object-fit: cover ritaglia l'immagine preservando le proporzioni ed evitando qualsiasi stiramento.",
      "position: sticky ancora la barra di navigazione in cima allo schermo senza uscire dal flusso del documento.",
      "transform: translateY(-8px) simula un sollevamento fisico della card stimolando l'interazione.",
      "L'uso combinato di ombre dinamiche (box-shadow) e transizioni morbide rafforza la gerarchia visiva."
    ],
    "flashcards": [
      {
        "question": "Quale distorsione previene l'istruzione CSS 'object-fit: cover' su un tag <img>?",
        "answer": "Previene lo stiramento e la deformazione visiva dell'immagine, ritagliando le parti eccedenti per riempire il contenitore mantenendo il rapporto d'aspetto."
      },
      {
        "question": "In che modo position: sticky si differenzia da position: fixed?",
        "answer": "Sticky rimane nel normale flusso del documento finché non raggiunge la coordinata di ancoraggio (es. top: 0), mentre fixed è perennemente ancorato allo schermo e rimosso dal flusso."
      },
      {
        "question": "Perché nelle coordinate del browser il valore transform: translateY(-8px) sposta l'elemento verso l'alto?",
        "answer": "Perché nel sistema di riferimento cartesiano del web l'origine (0,0) si trova nell'angolo in alto a sinistra e l'asse Y aumenta verso il basso."
      }
    ],
    "quiz": [
      {
        "question": "Quale proprietà CSS garantisce che un'immagine riempia un box di altezza fissa senza deformare le sue proporzioni native?",
        "options": [
          "object-fit: cover",
          "display: inline-block",
          "image-rendering: pixelated",
          "text-align: center"
        ],
        "correctIndex": 0,
        "explanation": "object-fit: cover scala l'immagine mantenendo inalterato l'aspect-ratio e ritaglia le parti in eccesso rispetto alle dimensioni del box."
      },
      {
        "question": "Come si comporta un elemento impostato con 'position: sticky; top: 0;'?",
        "options": [
          "Scorre normalmente con la pagina finché non tocca il margine superiore dello schermo, dove si aggancia",
          "Rimane permanentemente sovrapposto al centro dello schermo impedendo la visualizzazione dei contenuti",
          "Viene nascosto automaticamente non appena l'utente avvia l'operazione di scorrimento verso il basso",
          "Modifica le proprie dimensioni occupando il cento per cento dell'altezza del monitor del computer"
        ],
        "correctIndex": 0,
        "explanation": "position: sticky è un ibrido tra relative e fixed: si muove col flusso fino alla soglia (top: 0) e poi rimane fisso."
      },
      {
        "question": "Nel codice delle card, quale effetto visivo produce l'istruzione 'transform: translateY(-8px)' al passaggio del mouse?",
        "options": [
          "Provoca un sollevamento visivo della card di 8 pixel verso l'alto simulando un feedback tridimensionale",
          "Ruota la card in senso orario di otto gradi attorno al proprio asse baricentrico",
          "Aumenta la larghezza orizzontale della card di otto pixel spingendo le card adiacenti a capo",
          "Riduce l'opacità dello sfondo rendendo il testo sottostante parzialmente trasparente"
        ],
        "correctIndex": 0,
        "explanation": "Un valore negativo sull'asse Y sposta l'elemento verso l'alto, creando l'effetto di galleggiamento o sollevamento."
      },
      {
        "question": "A cosa serve impostare la proprietà 'z-index: 1000' sull'header della pagina?",
        "options": [
          "A garantire che l'header rimanga visivamente posizionato sopra tutti gli altri contenuti durante lo scroll",
          "A velocizzare di mille millisecondi l'avvio della riproduzione dei video multimediali del sito",
          "A limitare a mille il numero massimo di caratteri tipografici consentiti all'interno della barra",
          "A definire la larghezza dell'header pari a mille pixel indipendentemente dalla grandezza del display"
        ],
        "correctIndex": 0,
        "explanation": "z-index gestisce l'ordine di impilamento lungo l'asse Z perpendicolare allo schermo: valori più alti sovrappongono l'elemento a quelli inferiori."
      },
      {
        "question": "Perché è fondamentale dichiarare la proprietà 'transition' prima di applicare effetti all'evento :hover?",
        "options": [
          "Perché interpola gradualmente gli stati intermedi evitando scatti bruschi e donando naturalezza all'interazione",
          "Perché senza transition i browser disabilitano completamente il supporto ai cursori del mouse",
          "Perché transition costringe il server a inviare una notifica di avvenuta interazione ai server analitici",
          "Perché converte automaticamente le ombre sfumate in vettori geometrici a bassissima risoluzione"
        ],
        "correctIndex": 0,
        "explanation": "transition calcola l'animazione graduale tra lo stato di riposo e lo stato hover, rendendo la microinterazione fluida e piacevole."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega il funzionamento di object-fit: cover e descrivi le tecniche CSS usate per rendere le card interattive e responsive.",
        "modelAnswer": "object-fit: cover permette a un'immagine con width: 100% e height: 200px di riempire esattamente il contenitore senza deformare le proporzioni native, ritagliando le parti eccedenti. Per l'interattività, la card utilizza box-shadow e transform: translateY(-8px) con transition: 0.3s ease per simulare un sollevamento tridimensionale fluido al passaggio del cursore (:hover). Per la responsività, le card sono inserite in una griglia CSS (repeat(3, 1fr)) che scala a 2 e poi a 1 colonna sui dispositivi mobili tramite media queries."
      }
    ]
  }
];
