// Dati di studio e quiz approfonditi sul codice di 'Progetto_Esame_Cards' (HTML & CSS)
window.CARDS_DATA = [
  {
    "id": "cards-m1",
    "number": 1,
    "title": "Struttura HTML Semantica & Metadati",
    "subtitle": "Analisi dell'architettura di index.html, tag semantici e accessibilità",
    "readTime": "8 min",
    "summary": "### Analisi della struttura di `index.html`\nIl progetto *MagicTheArchive* è costruito su una solida struttura semantica HTML5 conforme agli standard W3C.\n\n```html\n<!doctype html>\n<html lang=\"it\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>MagicTheArchive | Home</title>\n    <link rel=\"icon\" type=\"image/x-icon\" href=\"IMG/Icon.ico\" />\n    <link rel=\"stylesheet\" href=\"style.css\" />\n  </head>\n```\n\n### Elementi chiave del `<head>`\n1. `<!doctype html>`: dichiara la modalità standard HTML5 al motore di rendering del browser.\n2. `<html lang=\"it\">`: dichiara la lingua del documento (fondamentale per screen reader e pronuncia corretta, oltre che per i motori di ricerca).\n3. `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />`: istruzione cardine del Responsive Web Design. Senza questo tag, i dispositivi mobili simulerebbero una pagina desktop a 980px rendendo il testo microscopico.\n4. `<link rel=\"icon\" type=\"image/x-icon\" href=\"IMG/Icon.ico\" />`: visualizza la favicon nella scheda del browser.\n\n### Architettura Semantica del `<body>`\nIl layout è suddiviso in macro-sezioni semantiche ben distinte:\n- `<header>`: racchiude il logo del sito, il checkbox per il menu mobile e il tag `<nav>` con l'elenco `<ul>` dei link.\n- `<section class=\"hero\">`: area di impatto visivo principale (Hero Header) con immagine di sfondo, logo e testo descrittivo.\n- `<section class=\"categorie\">`: blocco di navigazione verso i tre macro-rami del sito (*Gioco*, *Espansioni*, *Formati*).\n- `<section class=\"banner-lo-hobbit\">`: sezione promozionale dedicata alle ultime uscite.\n- `<section class=\"lista-argomenti\">`: carrellata editoriale con le card degli articoli in evidenza.\n- `<footer>`: chiusura del documento con link rapidi, texture grafica e crediti formali del team di lavoro.",
    "keyPoints": [
      "Uso rigoroso dei tag semantici HTML5: header, nav, section, footer.",
      "Meta viewport indispensabile per adattare la scala sui dispositivi mobili.",
      "L'attributo lang='it' garantisce l'accessibilità per le tecnologie assistive.",
      "Nesting logico: header contiene nav e ul per i link di navigazione persistente."
    ],
    "flashcards": [
      {
        "question": "Cosa accadrebbe su smartphone se rimuovessimo il tag <meta name='viewport' content='width=device-width, initial-scale=1.0'> da index.html?",
        "answer": "Lo smartphone visualizzerebbe la pagina come se fosse su un monitor desktop da circa 980px, rimpicciolendo tutti i testi e costringendo l'utente a fare 'pinch-to-zoom'."
      },
      {
        "question": "Quali tag semantici principali compongono la struttura verticale del body in index.html?",
        "answer": "<header> (con logo e <nav>), quattro <section> specializzate (hero, categorie, banner, lista-argomenti) e il <footer> finale."
      },
      {
        "question": "Perché nel form di navigazione del menu mobile è stato aggiunto l'attributo aria-label='Menu' al tag <label>?",
        "answer": "Perché la label contiene solo tre tag <span> grafici senza testo; l'aria-label comunica agli screen reader per non vedenti che quel pulsante serve ad aprire il menu."
      }
    ],
    "quiz": [
      {
        "question": "Nel codice di index.html, quale tag semantico racchiude i collegamenti a 'Gioco', 'Espansioni', 'Formati' e 'Chi Siamo'?",
        "options": [
          "<div class='navigatore'>",
          "<nav>",
          "<aside>",
          "<section class='menu'>"
        ],
        "correctIndex": 1,
        "explanation": "Il tag standard HTML5 dedicato ai blocchi di navigazione principale è <nav>."
      },
      {
        "question": "A cosa serve l'attributo lang='it' sul tag <html> di index.html?",
        "options": [
          "A impedire l'accesso agli utenti che si collegano dall'estero",
          "A comunicare a browser, motori di ricerca e screen reader che il testo della pagina è in lingua italiana",
          "A impostare automaticamente i colori della bandiera italiana",
          "A caricare il dizionario di correzione ortografica nel database"
        ],
        "correctIndex": 1,
        "explanation": "L'attributo lang informa le tecnologie assistive (screen reader) e i motori di ricerca sulla lingua da utilizzare per la lettura."
      }
    ],
    "openQuestions": [
      {
        "question": "Illustra come è strutturata la gerarchia dei titoli (h1, h2, h3, h5) all'interno di index.html e spiega se rispetta la gerarchia logica dei contenuti.",
        "modelAnswer": "In index.html la gerarchia visiva ed editoriale è articolata: nella hero delle categorie compare l'h1 per il titolo principale della pagina; nelle card categorie si utilizza l'h3 per identificare le sezioni ('Il Gioco', 'Le Espansioni', 'I Formati'); nella sezione articoli compare un h2 per il titolo di sezione ('Leggi anche') e h2 per i singoli articoli ('La Storia', 'Modern'), accompagnati da h5 per indicare la categoria di appartenenza. Questa gerarchia permette ai motori di ricerca e agli screen reader di distinguere i macro-temi dagli argomenti specifici."
      }
    ]
  },
  {
    "id": "cards-m2",
    "number": 2,
    "title": "Fondamenti CSS, Reset & Variabili :root",
    "subtitle": "Custom properties, box-sizing: border-box e gestione globale delle immagini",
    "readTime": "8 min",
    "summary": "### Il blocco iniziale di `style.css`\nLe prime righe del foglio di stile stabiliscono i token visivi e le regole base di calcolo geometrico:\n\n```css\n:root {\n  --rosso: #ce3021;\n  --grigio: #f7f7f7;\n}\n\n* {\n  margin: 0;\n  padding: 0;\n  box-sizing: border-box;\n  font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;\n}\n\nbody {\n  color: #000;\n  background-color: var(--grigio);\n  line-height: 1.4;\n  -webkit-font-smoothing: antialiased;\n}\n\nimg {\n  display: block;\n  max-width: 100%;\n}\n```\n\n### Concetti chiave da sapere all'esame\n\n#### 1. Le Variabili CSS (`:root`)\n- La pseudo-classe `:root` fa riferimento alla radice del documento (l'elemento `<html>`), rendendo le variabili accessibili ovunque.\n- `--rosso: #ce3021;` è il colore primario del brand (usato per hover, accenti e icone).\n- `--grigio: #f7f7f7;` è il colore neutro di sfondo della pagina.\n- Vengono richiamate con la funzione `var(--rosso)`, facilitando la manutenzione centralizzata.\n\n#### 2. Il CSS Reset con `box-sizing: border-box`\n- Per impostazione predefinita del browser (`box-sizing: content-box`), se a un elemento largo 300px si aggiungono 20px di padding e 2px di bordo, la larghezza totale diventa `300 + 40 + 4 = 344px`, sballando i layout.\n- Con `box-sizing: border-box`, la proprietà `width` include già padding e bordi all'interno dei 300px, rendendo il calcolo del layout matematicamente perfetto e prevedibile.\n\n#### 3. Gestione Responsive delle Immagini\n- `img { display: block; max-width: 100%; }`:\n  - `display: block` elimina il fastidioso spazio vuoto di 3-4px sotto le immagini (dovuto al fatto che di default le immagini sono elementi inline posizionati sulla baseline del testo).\n  - `max-width: 100%` garantisce che le immagini non fuoriescano mai dal contenitore genitore su schermi piccoli.",
    "keyPoints": [
      "Variabili CSS in :root per centralizzare i colori di brand (--rosso, --grigio).",
      "box-sizing: border-box: calcola padding e bordi all'interno della larghezza definita.",
      "display: block su img per azzerare lo spazio fantasma sulla baseline.",
      "max-width: 100% per rendere tutte le immagini fluide e responsive."
    ],
    "flashcards": [
      {
        "question": "Qual è la differenza tra box-sizing: content-box (default) e box-sizing: border-box applicato nel progetto?",
        "answer": "In content-box padding e bordi si sommano all'esterno della width; in border-box padding e bordi sono compresi dentro la larghezza dichiarata, semplificando la gestione del layout."
      },
      {
        "question": "Perché nel file style.css è impostato 'img { display: block; }'?",
        "answer": "Perché i tag <img> sono nativamente elementi inline; renderli block elimina lo spazio vuoto indesiderato di default che si crea sotto le immagini allineate alla baseline tipografica."
      },
      {
        "question": "Come si definisce e come si richiama una custom property (variabile) in CSS?",
        "answer": "Si definisce con il prefisso '--' (es. --rosso: #ce3021;) e si richiama usando la funzione var() (es. color: var(--rosso);)."
      }
    ],
    "quiz": [
      {
        "question": "Nel selettore '*' di style.css, perché viene specificato 'box-sizing: border-box;' per tutti gli elementi?",
        "options": [
          "Per disegnare un bordo nero attorno a ogni blocco del sito",
          "Per fare in modo che padding e border non aumentino le dimensioni totali stabilite con width ed height",
          "Per disabilitare la barra di scorrimento laterale",
          "Per centrare automaticamente tutti i testi della pagina"
        ],
        "correctIndex": 1,
        "explanation": "border-box include padding e bordi all'interno delle dimensioni assegnate, evitando che gli elementi sbordino dalle griglie."
      },
      {
        "question": "In style.css, a quale elemento fa riferimento la pseudo-classe ':root'?",
        "options": [
          "Al tag <body>",
          "Alla radice del documento (l'elemento <html>)",
          "Al primo tag <div> del codice",
          "Alla cartella principale del server"
        ],
        "correctIndex": 1,
        "explanation": ":root ha specificità identica a una classe e punta all'elemento radice del documento HTML, cioè <html>."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega il significato e l'utilità del font-stack di sistema dichiarato nel selettore universale '*' di style.css.",
        "modelAnswer": "Il font-stack '-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif' adotta i caratteri tipografici nativi del sistema operativo dell'utente (San Francisco su macOS/iOS, Segoe UI su Windows, Roboto su Android). I vantaggi sono: 1. Prestazioni eccezionali: tempo di caricamento nullo poiché non serve scaricare file font esterni via web (zero ritardo FOIT/FOUT). 2. Familiarità visiva: l'interfaccia si integra armoniosamente con l'aspetto delle app native del dispositivo."
      }
    ]
  },
  {
    "id": "cards-m3",
    "number": 3,
    "title": "Posizionamento Avanzato & Hero Section",
    "subtitle": "Position sticky, relative/absolute, layering z-index e object-fit: cover",
    "readTime": "9 min",
    "summary": "### Header Sticky e Posizionamento\n```css\nheader {\n  height: 70px;\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  padding: 0 50px;\n  background-color: #fff;\n  position: sticky;\n  top: 0;\n  z-index: 1000;\n  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);\n}\n```\n- `position: sticky; top: 0;`: l'header si comporta come un elemento normale finché l'utente scorre la pagina; non appena tocca la cima dello schermo (`top: 0`), rimane ancorato visibile.\n- `z-index: 1000;`: assicura che l'header e il menu passino sempre sopra a tutti gli altri elementi durante lo scroll.\n\n### Lo schema Relative / Absolute della Hero\n```css\n.hero {\n  position: relative;\n  width: 100%;\n  height: 95vh;\n  min-height: 600px;\n  display: flex;\n  align-items: flex-end;\n  padding: 80px 10%;\n  overflow: hidden;\n}\n\n.sfondo-hero {\n  position: absolute;\n  top: 0;\n  left: 0;\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  z-index: -1;\n}\n\n.contenuto-hero {\n  position: relative;\n  max-width: 40vw;\n  z-index: 2;\n}\n```\n\n### Perché questa combinazione è fondamentale\n1. `.hero` ha `position: relative`: funge da **sistema di coordinate (containing block)** per i figli assoluti.\n2. `.sfondo-hero` ha `position: absolute; top: 0; left: 0; width: 100%; height: 100%;`: riempie esattamente tutta la superficie della hero.\n3. `object-fit: cover`: evita che l'immagine si deformi o si allunghi, ritagliandola elegantemente al centro per coprire l'intera area indipendentemente dalle proporzioni dello schermo.\n4. `z-index: -1` per lo sfondo e `z-index: 2` per il testo: garantisce che il testo stia sopra l'immagine.\n5. Unità di misura moderne: `height: 95vh` (occupa il 95% dell'altezza della finestra visibile) e `max-width: 40vw` (il testo occupa al massimo il 40% della larghezza dello schermo).",
    "keyPoints": [
      "position: sticky sull'header per mantenerlo sempre accessibile durante lo scorrimento.",
      "Schema classico Hero: contenitore relative + immagine absolute con object-fit: cover.",
      "object-fit: cover adatta e ritaglia la foto senza deformare le proporzioni native.",
      "Gestione dei piani con z-index: sfondo a -1, testo a 2, header a 1000.",
      "Unità viewport vh e vw per dimensionamenti armonici rispetto allo schermo dell'utente."
    ],
    "flashcards": [
      {
        "question": "Come funziona la proprietà 'position: sticky' impostata sull'header?",
        "answer": "Si comporta come static fino al raggiungimento della soglia dichiarata (top: 0); superata tale soglia, rimane 'incollato' in testa alla finestra durante lo scroll."
      },
      {
        "question": "Perché è necessario impostare 'position: relative' sul contenitore .hero se lo sfondo è 'position: absolute'?",
        "answer": "Perché un elemento absolute si posiziona rispetto al primo antenato che non sia 'static'. Senza relative su .hero, lo sfondo si posizionerebbe rispetto all'intera pagina HTML."
      },
      {
        "question": "Cosa fa la proprietà 'object-fit: cover' sull'immagine di sfondo della Hero?",
        "answer": "Scala l'immagine mantenendone le proporzioni per riempire l'intero riquadro (100% width e height), ritagliando le parti eccedenti senza mai deformarla."
      }
    ],
    "quiz": [
      {
        "question": "Se eliminiamo 'object-fit: cover;' dall'immagine '.sfondo-hero' avente width: 100% e height: 100%, cosa succede?",
        "options": [
          "L'immagine scompare totalmente dallo schermo",
          "L'immagine viene deformata e schiacciata/allungata per forzarla nelle proporzioni del contenitore",
          "L'immagine diventa automaticamente in bianco e nero",
          "Il browser mostra un errore nella console"
        ],
        "correctIndex": 1,
        "explanation": "Senza object-fit, assegnare sia larghezza che altezza al 100% forza l'immagine a perdere le proprie proporzioni native provocando distorsione visiva."
      },
      {
        "question": "Qual è lo scopo del valore 'z-index: 1000;' assegnato al tag <header> in style.css?",
        "options": [
          "Impostare il peso del font dell'header a 1000",
          "Posizionare l'header 1000 pixel sotto la cima della pagina",
          "Garantire che durante lo scorrimento l'header rimanga sopra alle immagini e al testo che hanno z-index inferiori",
          "Ritardare il caricamento dell'header di un secondo"
        ],
        "correctIndex": 2,
        "explanation": "z-index controlla l'ordine di sovrapposizione lungo l'asse Z: un valore alto come 1000 evita che altri elementi scorrano 'sopra' l'header."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega come è stato risolto il problema della leggibilità del testo bianco posizionato sopra l'immagine di sfondo della hero section in style.css.",
        "modelAnswer": "Nel CSS, oltre al contrasto cromatico tra testo bianco (#fff) e immagine di sfondo scura, è stata applicata la proprietà 'text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);' sui paragrafi e 'text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);' sui titoli h1. Quest'ombra scura morbida crea un contrasto locale immediato dietro ai caratteri, garantendo che il testo sia sempre perfettamente leggibile anche nelle porzioni dell'immagine fotografica che presentano riflessi chiari."
      }
    ]
  },
  {
    "id": "cards-m4",
    "number": 4,
    "title": "Flexbox & CSS Grid nel Layout del Progetto",
    "subtitle": "Confronto tra Flexbox (1D) e CSS Grid (2D): Header, Categorie e Pagina Chi Siamo",
    "readTime": "9 min",
    "summary": "### L'uso combinato di Flexbox e Grid nel progetto\nNel progetto di Web Design, Flexbox e CSS Grid vengono usati in base alla loro vocazione:\n- **Flexbox**: per distribuzioni e allineamenti unidimensionali (lungo una riga o colonna).\n- **CSS Grid**: per gabbie modulari bidimensionali con colonne fisse o frazionate.\n\n### 1. Flexbox nell'Header e nella Navigazione\n```css\nheader {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n\nnav ul {\n  display: flex;\n  list-style: none;\n  gap: 35px;\n}\n```\n- `display: flex`: trasforma i figli diretti in flex-item.\n- `justify-content: space-between`: spinge il logo all'estrema sinistra e la navigazione all'estrema destra.\n- `align-items: center`: allinea perfettamente i centri verticali del logo e del testo del menu.\n- `gap: 35px`: spaziatura costante tra le voci del menu senza dover ricorrere a complessi `margin-right`.\n\n### 2. Flexbox nelle Card Categorie e Card Argomenti\n```css\n.categorie {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  gap: 50px;\n}\n\n.card-argomento {\n  display: flex;\n  flex-direction: row;\n  width: 100%;\n  max-width: 900px;\n}\n```\n- Nelle categorie le tre card sono affiancate al centro dello schermo con `gap: 50px`.\n- Nelle card argomento, `flex-direction: row` affianca l'immagine a sinistra e il blocco di testo a destra su desktop.\n\n### 3. CSS Grid nella Sezione 'Chi Siamo'\n```css\n.card_chisiamo {\n  width: 100%;\n  max-width: 850px;\n  margin: 60px auto 50px;\n  padding: 0 20px;\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  justify-content: center;\n  align-items: center;\n  gap: 25px;\n}\n```\n- `display: grid`: dichiara una griglia CSS bidimensionale.\n- `grid-template-columns: repeat(3, 1fr);`: crea 3 colonne di identica larghezza che occupano ciascuna una frazione (`1fr`) dello spazio disponibile.\n- `gap: 25px`: imposta la grondaia (*gutter*) tra le colonne in modo pulito e nativo.",
    "keyPoints": [
      "Flexbox: allineamento monodimensionale lungo asse principale (main axis) e incrociato (cross axis).",
      "justify-content: space-between per distanziare logo e menu agli estremi.",
      "CSS Grid: layout bidimensionale con righe e colonne sincronizzate.",
      "grid-template-columns: repeat(3, 1fr) per creare 3 colonne fluide identiche per il team.",
      "gap: sostituisce margin e padding esterni per gestire le spaziature tra elementi."
    ],
    "flashcards": [
      {
        "question": "Qual è la differenza fondamentale di utilizzo tra Flexbox e CSS Grid nel progetto?",
        "answer": "Flexbox è usato per elementi disposti lungo un unico asse (header, riga orizzontale categorie); CSS Grid è usato per strutture a griglia modulare (card del team in repeat(3, 1fr))."
      },
      {
        "question": "Cosa significa 'grid-template-columns: repeat(3, 1fr);' nella classe .card_chisiamo?",
        "answer": "Significa definire 3 colonne di larghezza uguale, ciascuna delle quali riceve 1 quota frazionaria (1fr) dello spazio orizzontale disponibile nella griglia."
      },
      {
        "question": "Quale proprietà Flexbox viene usata nell'header per spingere il logo a sinistra e i link a destra?",
        "answer": "justify-content: space-between;"
      }
    ],
    "quiz": [
      {
        "question": "Nella classe .card_chisiamo, cosa rappresenta l'unità di misura 'fr' in CSS Grid?",
        "options": [
          "Frame rate (frequenza dei fotogrammi al secondo)",
          "Fractional unit (una frazione proporzionale dello spazio libero disponibile nel contenitore)",
          "Front radius (il raggio di curvatura del bordo frontale)",
          "Fixed resolution (pixel a risoluzione fissa)"
        ],
        "correctIndex": 1,
        "explanation": "L'unità 'fr' distribuisce lo spazio residuo in parti proporzionali tra le colonne della griglia."
      },
      {
        "question": "Come viene gestita la spaziatura interna tra i link del tag <nav> in style.css?",
        "options": [
          "Inserendo caratteri di spazio vuoto non interrompibile (&nbsp;) nell'HTML",
          "Tramite la proprietà 'gap: 35px;' sul flex container 'nav ul'",
          "Impostando float: left con margin negativo",
          "Usando la proprietà word-spacing sul tag <body>"
        ],
        "correctIndex": 1,
        "explanation": "La proprietà gap su flex container e grid definisce la distanza esatta tra gli elementi figli senza margini laterali indesiderati."
      }
    ],
    "openQuestions": [
      {
        "question": "Descrivi i vantaggi della proprietà 'gap' in Flexbox e Grid rispetto all'uso tradizionale di 'margin-right' con selettori ':last-child'.",
        "modelAnswer": "Con la tecnica tradizionale dei margini, bisognava applicare 'margin-right' a ciascun figlio e poi rimuoverlo dall'ultimo elemento con ':last-child' o ':not(:last-child)' per evitare disallineamenti con i bordi del contenitore. Inoltre, in caso di a capo (flex-wrap), i margini verticali richiedevano ulteriore codice. La proprietà 'gap' (supportata nativamente in Flexbox e Grid) applica lo spazio esclusivamente tra gli elementi adiacenti, azzerando le eccezioni CSS e gestendo in automatico sia righe che colonne con una sola riga di codice pulita."
      }
    ]
  },
  {
    "id": "cards-m5",
    "number": 5,
    "title": "Il Menu Hamburger CSS-Only (Senza JavaScript)",
    "subtitle": "La tecnica della checkbox nascosta, il selettore fratello ~ e l'animazione nella 'X'",
    "readTime": "10 min",
    "summary": "### Il meccanismo del Menu Hamburger senza JavaScript\nUno dei punti tecnicamente più raffinati del progetto *MagicTheArchive* è la creazione del menu responsive mobile **completamente privo di codice JavaScript**: funziona al 100% tramite puro HTML e CSS!\n\n### Il codice HTML\n```html\n<input type=\"checkbox\" id=\"menu-toggle\" class=\"menu-toggle\" />\n<label for=\"menu-toggle\" class=\"burger-btn\" aria-label=\"Menu\">\n  <span></span>\n  <span></span>\n  <span></span>\n</label>\n<nav>\n  <ul>...</ul>\n</nav>\n```\n\n### Il codice CSS in Desktop vs Mobile\nSu desktop:\n```css\n.menu-toggle { display: none; }\n.burger-btn { display: none; }\n```\nSu schermi mobile (`@media (max-width: 900px)`):\n```css\n.burger-btn {\n  display: flex;\n  flex-direction: column;\n  justify-content: space-around;\n  width: 28px;\n  height: 22px;\n  cursor: pointer;\n  z-index: 1002;\n}\n\n.burger-btn span {\n  display: block;\n  width: 100%;\n  height: 3px;\n  background-color: #000;\n  border-radius: 3px;\n  transition: all 0.3s ease;\n}\n```\n\n### La 'Magia' dello pseudo-selettore `:checked` e del combinatore `~`\nQuando l'utente clicca sulla `<label>`, per via dell'attributo `for=\"menu-toggle\"`, la checkbox nascosta passa allo stato `:checked`.\nGrazie al **combinatore fratello generale (`~`)**, il CSS applica stili condizionali a label e nav:\n\n```css\n/* Il primo span scende e ruota di 45 gradi */\n.menu-toggle:checked ~ .burger-btn span:nth-child(1) {\n  transform: translateY(7.5px) rotate(45deg);\n  background-color: var(--rosso);\n}\n\n/* Il secondo span centrale scompare */\n.menu-toggle:checked ~ .burger-btn span:nth-child(2) {\n  opacity: 0;\n}\n\n/* Il terzo span sale e ruota di -45 gradi */\n.menu-toggle:checked ~ .burger-btn span:nth-child(3) {\n  transform: translateY(-7.5px) rotate(-45deg);\n  background-color: var(--rosso);\n}\n\n/* Il tag nav si espande aprendo il menu */\n.menu-toggle:checked ~ nav {\n  max-height: 240px;\n  border-top: 1px solid rgba(0, 0, 0, 0.08);\n}\n```\nI tre segmenti neri si fondono fluidamente in una **'X' rossa di chiusura**, e il menu scorre verso il basso.",
    "keyPoints": [
      "Menu responsive 100% CSS-only senza dipendenze JS (zero ritardi di esecuzione).",
      "La checkbox memorizza lo stato booleano (spuntato = aperto, deselezionato = chiuso).",
      "L'attributo for='menu-toggle' sul tag label permette il toggle al tocco delle dita.",
      "Il combinatore ~ (general sibling) intercetta gli elementi successivi alla checkbox spuntata.",
      "Animazione della 'X': translateY + rotate(45deg / -45deg) con secondo span a opacity: 0."
    ],
    "flashcards": [
      {
        "question": "Come fa la checkbox a cambiare stato quando l'utente tocca il pulsante con le 3 linee?",
        "answer": "Perché il pulsante è un tag <label for='menu-toggle'>: per specifica HTML, cliccare su una label attiva o disattiva l'input che possiede l'id corrispondente."
      },
      {
        "question": "Qual è il ruolo del selettore tilde (~) nella regola '.menu-toggle:checked ~ nav'?",
        "answer": "È il combinatore fratello generale: seleziona l'elemento <nav> che si trova allo stesso livello gerarchico (fratello) dopo l'input quando questo è spuntato (:checked)."
      },
      {
        "question": "Come viene realizzata l'animazione di trasformazione delle tre linee in una 'X'?",
        "answer": "Il primo span trasla verso il basso e ruota di +45°; il secondo scompare con opacity: 0; il terzo trasla verso l'alto e ruota di -45°, colorandosi entrambi di rosso."
      }
    ],
    "quiz": [
      {
        "question": "Quale combinatore CSS viene impiegato per selezionare il tag <nav> quando l'input checkbox è attivo?",
        "options": [
          "Il combinatore discendente (spazio)",
          "Il combinatore fratello generale (~)",
          "Il combinatore figlio diretto (>)",
          "Il selettore universale (*)"
        ],
        "correctIndex": 1,
        "explanation": "Il combinatore '~' seleziona i fratelli che seguono nello stesso genitore, permettendo alla checkbox di controllare stile di label e nav."
      },
      {
        "question": "Cosa accade al secondo <span> (quello centrale) del pulsante burger quando la checkbox è in stato :checked?",
        "options": [
          "Viene ruotato di 90 gradi",
          "Diventa trasparente grazie alla proprietà 'opacity: 0;'",
          "Aumenta la larghezza del 200%",
          "Cambia colore in verde"
        ],
        "correctIndex": 1,
        "explanation": "opacity: 0 fa scomparire la linea centrale, lasciando che la prima e la terza linea si incrocino formando la lettera 'X'."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega i vantaggi e le possibili limitazioni dell'implementazione di un menu hamburger con la tecnica CSS-only (checkbox hack) rispetto a una soluzione con JavaScript.",
        "modelAnswer": "I vantaggi del metodo CSS-only sono molteplici: 1. Funziona istantaneamente all'avvio della pagina senza attendere il caricamento o l'esecuzione di script JS. 2. È leggerissimo ed esente da bug di runtime o conflitti di librerie. 3. Le animazioni grafiche (la X e l'apertura) sono accelerate dall'hardware della GPU del browser. Le limitazioni riguardano l'accessibilità avanzata: senza JS è più difficile gestire la chiusura automatica del menu premendo il tasto 'Esc' della tastiera o al clic su un punto qualsiasi esterno alla pagina (click outside), e richiede attenzione nell'inserire attributi ARIA (come aria-label) per consentire agli screen reader di comprenderne lo stato."
      }
    ]
  },
  {
    "id": "cards-m6",
    "number": 6,
    "title": "Media Queries, Responsive Web Design & Microinterazioni",
    "subtitle": "Breakpoints (900px e 1450px), transizioni fluide, ombre e animazioni hover",
    "readTime": "9 min",
    "summary": "### La strategia Responsive di `style.css`\nIl progetto adotta un approccio Responsive modulare basato su due breakpoint principali:\n\n```css\n/* Per schermi intermedi (Tablet / Laptop compatti) */\n@media (min-width: 900px) and (max-width: 1450px) { ... }\n\n/* Per smartphone e schermi sotto i 900px */\n@media (max-width: 900px) { ... }\n```\n\n### Cosa cambia sotto i 900px\n1. **L'Header e la Navigazione**:\n   - I link del menu scompaiono dalla riga orizzontale e si compattano nel menu a tendina attivato dal burger button.\n   - Il padding dell'header si riduce da `0 50px` a `0 20px`.\n2. **La Sezione Hero**:\n   - Da `height: 95vh` con testo allineato a sinistra passa ad `height: auto`, `min-height: 380px`, con testo centrato al 100% di larghezza (`max-width: 100%; text-align: center;`).\n3. **Le Card Categorie**:\n   - Le tre card non sono più affiancate con larghezza fissa a 320px, ma si riducono o si incolonnano con padding adeguato.\n4. **Le Card Argomenti**:\n   - Da disposizione orizzontale (`flex-direction: row`), su mobile diventano verticali (`flex-direction: column`), con l'immagine in alto a tutta larghezza e il testo in basso.\n\n### Microinterazioni ed Effetti Hover\nPer dare un senso di tridimensionalità e reattività al tocco o al puntatore del mouse:\n```css\n.card-categorie {\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n}\n\n.card-categorie:hover {\n  transform: translateY(-10px);\n  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9);\n}\n\n.card-categorie:hover .immagine-card {\n  transform: scale(1.05);\n}\n```\n- `transform: translateY(-10px)`: la card si solleva verso l'alto di 10 pixel.\n- `box-shadow`: l'ombra diventa più scura, profonda e diffusa, simulando un allontanamento dal piano di fondo (*elevazione*).\n- `transform: scale(1.05)`: l'immagine interna si ingrandisce del 5% con un piacevole effetto zoom cinematografico all'interno della maschera (`overflow: hidden`).",
    "keyPoints": [
      "Breakpoint a 900px: soglia principale per il passaggio da layout desktop a layout mobile.",
      "Flessibilità del layout: le card argomento passano da flex-direction: row a column.",
      "Microinterazioni con transform: translateY(-10px) e potenziamento dell'ombra box-shadow.",
      "Zoom interno: scale(1.05) sull'immagine con overflow: hidden sulla card.",
      "Transizioni morbide: transition: transform 0.3s ease per evitare scatti visivi bruschi."
    ],
    "flashcards": [
      {
        "question": "Cosa succede alla disposizione delle '.card-argomento' quando lo schermo scende sotto i 900px?",
        "answer": "Passano da 'flex-direction: row' (immagine a sinistra, testo a destra) a 'flex-direction: column' (immagine in alto a tutta larghezza, testo subito sotto)."
      },
      {
        "question": "Come viene ottenuto l'effetto di sollevamento e zoom al passaggio del mouse sulle card delle categorie?",
        "answer": "La card riceve 'transform: translateY(-10px)' e un'ombra 'box-shadow' più marcata; l'immagine interna subisce 'transform: scale(1.05)', contenuta da 'overflow: hidden'."
      },
      {
        "question": "Perché è fondamentale definire 'transition: transform 0.3s ease;' sulla card e non solo sullo stato :hover?",
        "answer": "Perché definendola sulla classe base la transizione è fluida sia all'ingresso del mouse sia all'uscita; mettendola solo su :hover l'uscita risulterebbe a scatto istantaneo."
      }
    ],
    "quiz": [
      {
        "question": "Nello stato hover della card categoria, quale trasformazione geometrica simula il sollevamento verso l'alto?",
        "options": [
          "transform: rotate(180deg);",
          "transform: translateY(-10px);",
          "transform: skewX(10deg);",
          "transform: matrix(1, 0, 0, 1, 0, 0);"
        ],
        "correctIndex": 1,
        "explanation": "translateY con valore negativo sposta l'elemento verso l'alto lungo l'asse Y cartesiano del viewport."
      },
      {
        "question": "A cosa serve la proprietà 'overflow: hidden;' impostata sulle card con angoli arrotondati (border-radius: 16px)?",
        "options": [
          "A nascondere la barra di caricamento del browser",
          "A impedire che l'immagine figlia zoomata fuoriesca dai bordi arrotondati della card",
          "A rimuovere le sottolineature dei link",
          "A bloccare lo zoom da parte degli utenti touch"
        ],
        "correctIndex": 1,
        "explanation": "overflow: hidden maschera qualsiasi contenuto figlio (come l'immagine durante lo scale 1.05) che ecceda il raggio arrotondato della card."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega come le media queries e le microinterazioni CSS di style.css rispettano i principi di usabilità (affordance e feedback) descritti nelle dispense e da Steve Krug.",
        "modelAnswer": "Le microinterazioni su pulsanti e card (il sollevamento con translateY, il cambio colore in rosso con transition, e l'ampliamento dell'ombra) forniscono all'utente un feedback visivo immediato (affordance dinamica), confermando che l'elemento è cliccabile senza richiedere riflessione (prima legge di Krug: Don't Make Me Think). Le media queries a 900px riorganizzano i flussi per lo spazio ridotto dello smartphone: ampliano i touch target, evitano lo scroll orizzontale e raggruppano i menu, preservando il Serbatoio della Buona Volontà dell'utente."
      }
    ]
  }
];
