// Moduli didattici basati sul codice reale di Progetto_Esame_Cards
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
        "question": "Nel codice di index.html, quale tag semantico HTML5 è specificamente deputato a racchiudere i link di navigazione principale del sito?",
        "options": [
          "Il tag <nav>, che funge da landmark accessibile per browser e screen reader",
          "Il tag generico <section id='nav'> privo di semantica di navigazione",
          "Il tag strutturale <aside>, riservato a contenuti tangenziali",
          "Il tag <menu>, deprecato nelle specifiche HTML moderne"
        ],
        "correctIndex": 0,
        "explanation": "Il tag HTML5 standard deputato a racchiudere i collegamenti primari è <nav>. Esso definisce un landmark di navigazione che consente alle tecnologie assistive di saltare direttamente al menu senza scorrere l'intera pagina."
      },
      {
        "question": "Qual è la funzione tecnica fondamentale dell'istruzione <meta name='viewport' content='width=device-width, initial-scale=1.0'> inserita nell'<head>?",
        "options": [
          "Disabilita permanentemente lo zoom tattile per impedire rotture del layout grafico",
          "Forza la larghezza del viewport a coincidere con i pixel fisici del dispositivo impedendo il rendering desktop rimpicciolito",
          "Adatta automaticamente la densità di pixel delle immagini bitmap alla risoluzione dello schermo",
          "Imposta la risoluzione di rendering a un valore fisso di 980px con scrolling orizzontale automatico"
        ],
        "correctIndex": 1,
        "explanation": "Nei dispositivi mobili senza meta viewport, il browser assume una larghezza virtuale di circa 980px scalando la pagina e rendendo i testi minuscoli. L'istruzione impone un rapporto 1:1 tra pixel CSS e viewport del dispositivo."
      },
      {
        "question": "Per quale ragione l'attributo lang='it' all'interno dell'elemento <html> è considerato un requisito critico di accessibilità WCAG?",
        "options": [
          "Permette ai motori di ricerca di indicizzare il sito escludendolo dai risultati internazionali",
          "Attiva automaticamente i caratteri tipografici con glifi e accenti specifici della lingua italiana",
          "Indica al software di sintesi vocale (screen reader) quale motore fonetico e di pronuncia applicare",
          "Garantisce che la codifica dei caratteri venga forzata a ISO-8859-1 anziché UTF-8"
        ],
        "correctIndex": 2,
        "explanation": "I sintetizzatori vocali utilizzano l'attributo 'lang' per caricare le corrette regole di pronuncia fonetica e accentazione. Senza di esso, un lettore vocale configurato in inglese leggerebbe il testo italiano con fonetica anglosassone."
      },
      {
        "question": "Cosa comporterebbe l'omissione della dichiarazione <!doctype html> nella prima riga del file HTML?",
        "options": [
          "La mancata esecuzione di tutti gli script JavaScript esterni collegati al documento",
          "L'impossibilità di applicare classi e ID tramite selettori nei fogli di stile CSS esterni",
          "Il rifiuto da parte del server web di trasmettere il documento con codice di stato HTTP 200",
          "L'attivazione della modalità Quirks da parte del browser, con calcolo errato del Box Model e delle dimensioni"
        ],
        "correctIndex": 3,
        "explanation": "Senza <!doctype html>, i browser moderni attivano la retrocompatibilità Quirks Mode (simulando i vecchi browser anni '90), alterando la gestione delle altezze percentuali, dei margini e del box model standard."
      },
      {
        "question": "In una tipica architettura a schede informative (card list), quale elemento semantico HTML5 è più idoneo a racchiudere ciascuna singola card con contenuto autonomo e riutilizzabile?",
        "options": [
          "L'elemento <article>, che rappresenta un'unità di contenuto autonoma e sindacabile",
          "L'elemento <div> generico, poiché i tag semantici non possono contenere link",
          "L'elemento <details>, che richiede obbligatoriamente l'interazione per essere visualizzato",
          "L'elemento <figure>, che può ospitare unicamente immagini senza paragrafi di testo"
        ],
        "correctIndex": 0,
        "explanation": "L'elemento <article> è specificamente pensato per contenuti autosufficienti che avrebbero senso anche estrapolati dal contesto generale della pagina, come card di prodotti, post o schede tematiche."
      }
    ],
    "openQuestions": [
      {
        "question": "Descrivi i componenti essenziali del tag <head> in index.html e spiega perché la semantica HTML5 è superiore ai semplici tag <div> generici.",
        "modelAnswer": "Il tag <head> definisce la codifica caratteri UTF-8, il meta viewport per la corretta scalatura mobile, il titolo del documento per SEO e browser tab, la favicon e il collegamento al foglio di stile CSS. L'uso dei tag semantici HTML5 (header, nav, section, article, footer) è superiore ai semplici div perché fornisce significato alla struttura (landmarks), consentendo ai motori di ricerca di indicizzare correttamente la gerarchia e agli screen reader di consentire la navigazione facilitata per utenti con disabilità."
      }
    ],
    "examQuiz": [
      {
        "question": "Un auditor di accessibilità rileva che il logo nella testata del progetto MagicTheArchive contiene un'immagine con attributo alt=''. In quale circostanza questa scelta è conforme alle WCAG?",
        "options": [
          "In nessun caso: qualsiasi elemento <img> deve sempre descrivere dettagliatamente il marchio",
          "Soltanto se l'immagine è puramente decorativa o se il nome dell'azienda è già presente come testo accessibile nel medesimo link",
          "Esclusivamente se l'immagine ha estensione SVG vettoriale e non formato PNG o WebP",
          "Solo se il tag <img> è posizionato all'interno di un tag <aside> anziché nell'<header>"
        ],
        "correctIndex": 1,
        "explanation": "Un attributo alt='' (alt vuoto) segnala allo screen reader di ignorare l'immagine. È conforme solo se l'immagine ha funzione puramente estetica o se il testo del link circostante fornisce già l'indicazione completa, evitando doppie letture ridondanti."
      },
      {
        "question": "Analizzando la struttura di un form HTML5, quale associazione garantisce la massima usabilità e accessibilità per un campo di input?",
        "options": [
          "Utilizzare un semplice attributo placeholder senza alcun elemento <label>",
          "Inserire il testo della label in uno <span> adiacente formattato con CSS",
          "Associare esplicitamente un elemento <label for='id_campo'> all'input con id corrispondente",
          "Affidarsi unicamente all'attributo title sull'elemento input"
        ],
        "correctIndex": 2,
        "explanation": "L'associazione esplicita tramite for/id permette alle tecnologie assistive di annunciare l'etichetta al focus e consente agli utenti su mobile o desktop di cliccare sulla label per attivare il campo."
      },
      {
        "question": "Quale differenza intercorre tra l'utilizzo dell'elemento <section> e dell'elemento <div> secondo le specifiche W3C?",
        "options": [
          "I <div> possono contenere classi CSS mentre i <section> supportano unicamente attributi inline",
          "Non esiste differenza tecnica, l'uso di <section> è puramente convenzionale",
          "La <section> impone automaticamente un display: flex mentre il <div> ha display: block",
          "La <section> definisce una porzione tematica del documento tipicamente introdotta da un'intestazione (h2-h6), mentre il <div> è un mero contenitore stilistico neutro"
        ],
        "correctIndex": 3,
        "explanation": "La <section> è un elemento di sezione semantica con valore strutturale che raggruppa contenuti omogenei dotati di una propria intestazione. Il <div> è un contenitore generico privo di qualsiasi significato semantico, impiegato per fini stilistici."
      }
    ]
  },
  {
    "id": "cards-m2",
    "number": 2,
    "title": "Il Box Model CSS & Azzeramento Globale",
    "subtitle": "Calcolo dello spazio, box-sizing: border-box, margini, padding e reset universale",
    "readTime": "10 min",
    "summary": "### Il Box Model nel World Wide Web\nNel linguaggio CSS, ogni elemento renderizzato sulla pagina viene calcolato come una scatola rettangolare (Box).\nIl Box Model si compone di quattro aree concentriche (dall'interno verso l'esterno):\n1. **Content**: l'area dove risiedono testo, immagini o elementi figli.\n2. **Padding (Spaziatura interna)**: lo spazio di respiro trasparente attorno al contenuto, ma all'interno dell'eventuale sfondo o bordo.\n3. **Border (Bordo)**: la linea perimetrale visibile che delimita il box.\n4. **Margin (Margine esterno)**: lo spazio trasparente che separa il box dagli elementi circostanti.\n\n### La rivoluzione di `box-sizing: border-box`\nNel modello tradizionale W3C (`content-box`):\n> **Box Model Tradizionale (`content-box`)**:\n> **Larghezza totale** = width + padding-left + padding-right + border-left + border-right\nQuesto rendeva il calcolo dei layout matematicamente instabile: assegnando `width: 50%` e `padding: 20px` a due colonne affiancate, la somma superava il 100%, spingendo la seconda colonna a capo.\n\nNel file `style.css` del progetto esame viene adottato il reset moderno universale:\n```css\n*,\n*::before,\n*::after {\n  box-sizing: border-box;\n  margin: 0;\n  padding: 0;\n}\n```\nCon `box-sizing: border-box`, la proprietà `width` include già al suo interno il padding e il bordo:\n> **Box Model Moderno (`border-box`)**:\n> **Larghezza totale a schermo** = width dichiarata *(padding e bordi sono incorporati internamente)*\nQuesto garantisce che un elemento impostato a `width: 33.333%` occuperà esattamente un terzo dello spazio disponibile, a prescindere dal padding interno assegnato.\n\n### Il collasso dei margini verticali (Margin Collapse)\nUn fenomeno cruciale del Box Model: quando due margini verticali adiacenti si toccano nel normale flusso di blocco, non si sommano, ma collassano nel margine più grande tra i due. Non accade invece sui margini orizzontali o all'interno di contenitori Flexbox e CSS Grid.",
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
        "question": "Se a un elemento con width: 300px e box-sizing: content-box vengono applicati padding: 20px su tutti i lati e border: 2px solid, quale sarà la larghezza totale occupata nel layout?",
        "options": [
          "300 pixel, poiché il padding si espande verso l'interno senza alterare i bordi",
          "344 pixel, risultante da 300px + 40px di padding totale + 4px di bordi totali",
          "320 pixel, sommando solo il padding orizzontale e ignorando lo spessore del bordo",
          "256 pixel, poiché lo spazio di padding e bordo viene sottratto dalla larghezza dichiarata"
        ],
        "correctIndex": 1,
        "explanation": "Nel box-sizing standard (content-box), la larghezza finale corrisponde a: width + padding-left + padding-right + border-left + border-right = 300 + 20 + 20 + 2 + 2 = 344px."
      },
      {
        "question": "Qual è il beneficio fondamentale della regola di reset globale '* , *::before, *::after { box-sizing: border-box; }'?",
        "options": [
          "Elimina qualsiasi margine tra gli elementi della pagina rendendo superfluo Flexbox",
          "Forza tutti gli elementi della pagina ad avere proporzioni rettangolari auree",
          "Include padding e bordi all'interno della larghezza e altezza dichiarate, rendendo i calcoli percentuali esatti e stabili",
          "Impedisce agli elementi inline di superare la larghezza del genitore contenitore"
        ],
        "correctIndex": 2,
        "explanation": "Con border-box, impostare width: 50% garantisce che l'elemento occuperà esattamente la metà dello spazio disponibile anche aggiungendo padding interni o bordi decorativi, senza generare overflow indesiderati."
      },
      {
        "question": "Cosa accade nel fenomeno del 'collasso dei margini verticali' (margin collapse) tra due elementi a blocco adiacenti?",
        "options": [
          "I due margini verticali si sommano algebricamente raddoppiando la spaziatura finale",
          "Il margine dell'elemento inferiore sovrascrive quello superiore soltanto se è espresso in percentuali",
          "Il browser annulla entrambi i margini impostando la spaziatura verticale a zero pixel",
          "I due margini collassano fondendosi nel valore del margine più grande tra i due"
        ],
        "correctIndex": 3,
        "explanation": "Nel normale flusso di blocco, i margini verticali adiacenti si sovrappongono: se il primo blocco ha margin-bottom: 30px e il secondo margin-top: 20px, la distanza effettiva tra essi sarà 30px, non 50px."
      },
      {
        "question": "In quale tra i seguenti contesti di formattazione NON si verifica il collasso dei margini verticali?",
        "options": [
          "All'interno di elementi con contesto di formattazione Flexbox o CSS Grid",
          "Tra il primo elemento figlio e il contenitore genitore privo di padding e bordo",
          "Tra paragrafi <p> consecutivi nel normale flusso del documento",
          "Tra titoli <h2> e paragrafi successivi formattati con display: block"
        ],
        "correctIndex": 0,
        "explanation": "Nei contesti flessibili o a griglia (display: flex e display: grid), i margini degli elementi figli non collassano mai, garantendo un controllo rigoroso e prevedibile delle distanze tramite la proprietà 'gap'."
      },
      {
        "question": "Quale proprietà CSS consente di creare un margine interno negativo su un box?",
        "options": [
          "padding: -10px, supportato da tutte le specifiche W3C",
          "Nessuna: i valori negativi per il padding non sono ammessi dalle specifiche CSS e vengono ignorati",
          "box-padding-trim: negative, introdotto nei moduli CSS recenti",
          "inner-margin: -10px, utilizzato per arretrare il contenuto di blocco"
        ],
        "correctIndex": 1,
        "explanation": "A differenza dei margini esterni ('margin'), che possono accettare valori negativi per avvicinare o sovrapporre elementi, i valori di 'padding' devono essere necessariamente non negativi (>= 0)."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega dettagliatamente la differenza pratica tra box-sizing: content-box e box-sizing: border-box, indicando perché quest'ultimo è lo standard moderno.",
        "modelAnswer": "In content-box (default storico del browser), width e height si applicano solo al contenuto; padding e bordi si sommano all'esterno, rendendo difficoltoso il calcolo delle percentuali (es. due elementi al 50% con padding andranno a capo). In border-box, width e height rappresentano la misura finita della scatola: padding e bordi vengono assorbiti all'interno, riducendo lo spazio a disposizione del testo ma mantenendo invariate le dimensioni totali del blocco, rendendo i layout modulari stabili e calcolabili."
      }
    ],
    "examQuiz": [
      {
        "question": "Due elementi a blocco hanno rispettivamente margin-bottom: 24px e margin-top: 16px. Se entrambi sono inseriti all'interno di un contenitore con display: flex e flex-direction: column, quale sarà la loro distanza verticale?",
        "options": [
          "24 pixel, a causa del classico collasso dei margini verticali",
          "16 pixel, prevalendo sempre il margine dell'elemento successivo",
          "40 pixel, poiché all'interno di un flex container i margini verticali non collassano",
          "8 pixel, calcolando la differenza assoluta tra i due valori"
        ],
        "correctIndex": 2,
        "explanation": "All'interno di un flex container (anche con direzione column), gli elementi figli stabiliscono contesti indipendenti e i margini non collassano: 24px + 16px = 40px."
      },
      {
        "question": "Un elemento div ha width: 100%, padding: 16px e margin: 0, ma genera una barra di scorrimento orizzontale imprevista. Qual è la diagnosi più probabile del bug?",
        "options": [
          "L'elemento genitore ha impostato display: inline-block",
          "L'elemento contiene testo privo di proprietà text-overflow: ellipsis",
          "I browser moderni non supportano valori percentuali per la proprietà width sui tag div",
          "L'elemento sta calcolando le dimensioni con box-sizing: content-box anziché border-box"
        ],
        "correctIndex": 3,
        "explanation": "Con content-box, width: 100% occupa l'intero spazio del genitore; aggiungendo i 16px di padding su entrambi i lati, la larghezza totale diventa 100% + 32px, causando overflow orizzontale."
      },
      {
        "question": "Perché nel reset moderno universale si applica 'box-sizing: border-box' anche agli pseudo-elementi *::before e *::after?",
        "options": [
          "Per evitare che icone, badge decorativi o sagome generate via CSS causino overflow imprevisti sommando padding e bordi",
          "Perché gli pseudo-elementi altrimenti non verrebbero renderizzati dal motore del browser",
          "Per forzare gli pseudo-elementi ad assumere un posizionamento assoluto di default",
          "Per consentire l'inserimento di codice HTML all'interno della proprietà content"
        ],
        "correctIndex": 0,
        "explanation": "Gli pseudo-elementi ::before e ::after sono ampiamente impiegati per decorazioni grafiche, badge o clearing; includerli nel reset assicura che qualsiasi padding o bordo applicato rispetti il medesimo calcolo geometrico del resto dell'interfaccia."
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
        "question": "Cosa rappresenta l'unità di misura 'fr' (frazione) introdotta nelle specifiche CSS Grid?",
        "options": [
          "Una percentuale fissa calcolata esclusivamente rispetto all'altezza dello schermo",
          "La frequenza di refresh del rendering applicata alla griglia vettoriale",
          "Una frazione dello spazio libero rimanente all'interno del contenitore griglia dopo l'assegnazione degli spazi fissi",
          "Un valore relativo all'ampiezza tipografica del glifo 'F' del font genitore"
        ],
        "correctIndex": 2,
        "explanation": "L'unità 'fr' (fractional unit) distribuisce lo spazio libero non allocato. Ad esempio, '1fr 2fr' divide lo spazio residuo in 3 parti uguali, assegnandone 1 alla prima colonna e 2 alla seconda."
      },
      {
        "question": "Quale comportamento produce la dichiarazione 'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));'?",
        "options": [
          "Crea una griglia con un numero fisso di 4 colonne a larghezza fissa di 280px",
          "Richiede obbligatoriamente l'aggiunta di media queries specifiche per ogni singolo breakpoint",
          "Comprime tutte le card a 280px forzando lo scroll orizzontale sui dispositivi con schermo inferiore",
          "Genera un layout responsive dinamico che inserisce quante più colonne da almeno 280px possibile, espandendole proporzionalmente per riempire la riga"
        ],
        "correctIndex": 3,
        "explanation": "Questa formula è il cardine del responsive design con Grid: crea automaticamente nuove colonne se lo spazio lo consente (almeno 280px ciascuna) ed espande le colonne esistenti fino a 1fr per non lasciare spazi vuoti."
      },
      {
        "question": "Qual è la differenza fondamentale tra 'auto-fill' e 'auto-fit' nella definizione delle colonne di una griglia CSS?",
        "options": [
          "auto-fill mantiene le colonne vuote create nello spazio residuo, mentre auto-fit le collassa a zero permettendo alle colonne occupate di espandersi",
          "auto-fill funziona solo sui dispositivi mobili, mentre auto-fit è destinato agli schermi desktop",
          "Non sussiste alcuna differenza reale, sono sinonimi introdotti per retrocompatibilità",
          "auto-fill calcola le righe mentre auto-fit calcola unicamente le colonne verticali"
        ],
        "correctIndex": 0,
        "explanation": "Quando gli elementi non riempiono l'intera larghezza, 'auto-fill' preserva lo spazio delle colonne vuote rimanenti; 'auto-fit' collassa le colonne vuote permettendo agli elementi presenti di dilatarsi per colmare tutta la riga."
      },
      {
        "question": "Quale proprietà CSS sostituisce in modo pulito l'uso di margini per distanziare celle e righe in un contenitore CSS Grid?",
        "options": [
          "La proprietà 'cell-spacing' ereditata dalle tabelle HTML",
          "La proprietà 'gap' (oppure row-gap e column-gap)",
          "La proprietà 'grid-padding-between'",
          "La proprietà 'margin-collapse: separate'"
        ],
        "correctIndex": 1,
        "explanation": "La proprietà standard 'gap' definisce la spaziatura esatta tra righe e colonne senza applicare margini ai bordi esterni del contenitore, eliminando la necessità di hack come :last-child."
      },
      {
        "question": "Se in un layout a griglia una card deve estendersi per occupare l'intera larghezza di una griglia a 3 colonne, quale istruzione è corretta?",
        "options": [
          "grid-row: full-width;",
          "width: 300%;",
          "grid-column: span 3; (oppure grid-column: 1 / -1;)",
          "display: inline-grid; colspan: 3;"
        ],
        "correctIndex": 2,
        "explanation": "'grid-column: span 3' ordina all'elemento di espandersi su 3 tracce colonna. La notazione '1 / -1' estende l'elemento dalla prima linea di traccia all'ultima linea esplicita."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega la sintassi di CSS Grid utilizzata per la sezione lista-argomenti e descrivi come viene gestita la transizione da desktop a mobile.",
        "modelAnswer": "La sezione adotta display: grid con grid-template-columns: repeat(3, 1fr) e gap: 30px all'interno di un contenitore con max-width: 1200px e margin: 0 auto. Su desktop questo genera tre colonne perfette di larghezza identica con 30px di spazio tra loro. Tramite media queries a max-width: 900px e 600px, le colonne vengono progressivamente ridotte a 2 e infine a 1 singola colonna per gli smartphone, garantendo leggibilità ottimale senza scroll orizzontale."
      }
    ],
    "examQuiz": [
      {
        "question": "In una griglia CSS con 'grid-template-columns: repeat(3, 1fr)' e gap: 20px, come viene calcolata l'effettiva larghezza di ciascuna delle 3 colonne su una larghezza totale di 940px?",
        "options": [
          "940px diviso 3 = 313.33px, e il gap viene aggiunto esternamente debordando dal contenitore",
          "Il browser assegna 33.33% a ogni colonna e annulla la proprietà gap in presenza di 1fr",
          "Ciascuna colonna occupa 940px / 3 meno 20px = 293.33px, lasciando 60px non allocati",
          "Si sottraggono prima i due gap (20px * 2 = 40px) ottenendo 900px, quindi si divide per 3, assegnando 300px a ciascuna colonna"
        ],
        "correctIndex": 3,
        "explanation": "Il calcolo di 1fr tiene conto del gap: lo spazio libero è pari a Larghezza Totale (940px) - somma dei gap interni (2 gap da 20px = 40px) = 900px. Le 3 frazioni si ripartiscono 900px in parti uguali: 300px ciascuna."
      },
      {
        "question": "Quale combinazione di proprietà su un elemento griglia garantisce che tutte le card di una riga abbiano visivamente la medesima altezza indipendentemente dalla quantità di testo?",
        "options": [
          "align-items: stretch sul contenitore griglia (comportamento predefinito) con card ad altezza height: auto",
          "height: 100vh su ciascuna singola card con overflow: hidden",
          "grid-auto-rows: min-content con text-truncate",
          "justify-content: space-between applicato alle colonne"
        ],
        "correctIndex": 0,
        "explanation": "Il valore predefinito di align-items in CSS Grid è 'stretch'. Se le card non hanno altezze fisse forzate, esse si estendono automaticamente per eguagliare l'altezza della card più alta nella medesima riga."
      },
      {
        "question": "In un progetto web moderno, quale criterio architetturale orienta la scelta tra CSS Grid e Flexbox?",
        "options": [
          "Grid è riservato ai dispositivi mobili, mentre Flexbox va impiegato per schermi desktop",
          "Grid è bidimensionale (controlla contemporaneamente righe e colonne dell'intero layout), mentre Flexbox è monodimensionale (orientato alla distribuzione su un singolo asse, come navbar o bottoni)",
          "Flexbox è una specifica obsoleta destinata a essere soppressa in favore di CSS Grid",
          "Grid funziona solo con elementi con dimensioni espresse in pixel assoluti"
        ],
        "correctIndex": 1,
        "explanation": "La regola aurea del design CSS moderno: CSS Grid gestisce la macro-struttura a due dimensioni (layout di pagina, matrici di card), mentre Flexbox gestisce micro-layout a un solo asse (allineamento di link in una barra, icone e testi dentro un bottone)."
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
        "question": "All'interno di un contenitore flessibile con flex-direction: row, quale proprietà allinea gli elementi lungo l'asse principale (orizzontale)?",
        "options": [
          "align-items",
          "align-content",
          "flex-wrap",
          "justify-content"
        ],
        "correctIndex": 3,
        "explanation": "L'asse principale (main axis) è governato da 'justify-content' (es. flex-start, center, space-between, flex-end). L'asse trasversale (cross axis) è invece governato da 'align-items'."
      },
      {
        "question": "Cosa accade quando su un contenitore flessibile viene impostata la proprietà 'flex-wrap: wrap'?",
        "options": [
          "Gli elementi che superano la larghezza disponibile vanno a capo creando una nuova riga anziché debordare",
          "Gli elementi figli vengono forzati a comprimersi sulla stessa riga rimpicciolendosi all'infinito",
          "Il contenitore converte automaticamente il suo modello di rendering in una tabella HTML",
          "Tutti gli elementi figli assumono una larghezza fissa del 50%"
        ],
        "correctIndex": 0,
        "explanation": "Di default i flex items tentano di stare su una sola riga ('nowrap'). Impostando 'flex-wrap: wrap', quando la somma delle dimensioni eccede lo spazio del genitore, gli elementi scorrono ordinatamente su una nuova riga."
      },
      {
        "question": "Per centrare perfettamente un elemento sia in orizzontale che in verticale all'interno di un contenitore, quale combinazione CSS è più sintetica ed efficace?",
        "options": [
          "position: absolute; margin: auto; float: left;",
          "display: flex; justify-content: center; align-items: center;",
          "display: inline-block; vertical-align: middle; text-align: center;",
          "display: flex; flex-direction: column; align-self: baseline;"
        ],
        "correctIndex": 1,
        "explanation": "Impostando il contenitore come 'display: flex', la coppia 'justify-content: center' (asse principale) e 'align-items: center' (asse trasversale) garantisce il perfetto centraggio bidimensionale."
      },
      {
        "question": "Cosa indica la notazione sintetica 'flex: 1' applicata a un elemento figlio in un flex container?",
        "options": [
          "Che l'elemento deve avere una larghezza minima rigida di 1px",
          "Che l'elemento sarà l'unico elemento renderizzato nel contenitore",
          "Equivale a 'flex: 1 1 0%', permettendo all'elemento di espandersi e ridursi proporzionalmente assorbendo lo spazio libero",
          "Che l'elemento possiede una priorità di stacking z-index pari a 1"
        ],
        "correctIndex": 2,
        "explanation": "'flex: 1' espande la proprietà 'flex-grow: 1', 'flex-shrink: 1' e 'flex-basis: 0%'. Consente al componente di riempire elasticamente lo spazio disponibile equamente tra fratelli con il medesimo valore."
      },
      {
        "question": "A cosa serve la proprietà 'align-self' in Flexbox?",
        "options": [
          "Allinea l'intero flex container rispetto al centro della finestra del browser",
          "Permette di riordinare sequenzialmente gli elementi all'interno del flusso DOM",
          "Centra il testo tipografico all'interno del proprio box di contenuto",
          "Permette a un singolo elemento figlio di sovrascrivere l'allineamento sull'asse trasversale stabilito da 'align-items' sul genitore"
        ],
        "correctIndex": 3,
        "explanation": "'align-self' accetta i medesimi valori di 'align-items' (es. flex-start, center, flex-end, stretch) ma viene applicata al singolo elemento figlio per personalizzarne la posizione sull'asse trasversale."
      }
    ],
    "openQuestions": [
      {
        "question": "Mostra come vengono definite e utilizzate le Custom Properties in style.css e spiega il loro ruolo nella costruzione di un Design System.",
        "modelAnswer": "In style.css le variabili vengono definite all'interno di :root con il prefisso doppio trattino (es. --rosso: #ce3021; --transizione-veloce: 0.3s ease;). Vengono richiamate nelle regole CSS con la funzione var(--rosso). In un Design System, queste variabili fungono da 'Design Tokens': standardizzano palette cromatiche, spaziature, tipografia e velocità di transizione, garantendo che l'intera squadra rispetti le linee guida del brand e consentendo modifiche globali istantanee."
      }
    ],
    "examQuiz": [
      {
        "question": "In una navbar con logo a sinistra e link di navigazione a destra, quale tecnica Flexbox evita l'uso di float o posizionamenti assoluti?",
        "options": [
          "Applicare 'margin-left: auto' al contenitore dei link (o usare justify-content: space-between sul flex container)",
          "Impostare float: right sul contenitore dei link e clear: both sul logo",
          "Applicare text-align: right al contenitore genitore",
          "Usare position: relative con left: 100% sui link"
        ],
        "correctIndex": 0,
        "explanation": "In Flexbox, applicare 'margin-left: auto' a un elemento spinge quell'elemento (e tutti i successivi) all'estrema destra dell'asse principale, assorbendo tutto lo spazio vuoto disponibile in modo pulito e responsive."
      },
      {
        "question": "In un layout a card verticale con immagine, titolo, paragrafo descrittivo variabile e un bottone 'Acquista' sul fondo, come si assicura che il bottone sia sempre allineato alla base della card?",
        "options": [
          "Impostando position: absolute; bottom: 0 sul bottone e position: relative sulla card",
          "Impostando sulla card display: flex; flex-direction: column e applicando 'margin-top: auto' al bottone",
          "Aggiungendo un numero fisso di tag <br> per uniformare le altezze dei paragrafi",
          "Impostando height: 100px sul paragrafo descrittivo con overflow: scroll"
        ],
        "correctIndex": 1,
        "explanation": "Impostando la card in Flexbox a colonna, 'margin-top: auto' applicato al bottone spinge il margine superiore ad assorbire tutto lo spazio residuo creato dai testi brevi, posizionando il pulsante perfettamente allineato sul fondo."
      },
      {
        "question": "Qual è il rischio nell'utilizzare la proprietà CSS 'order' di Flexbox per alterare la sequenza visiva degli elementi a schermo?",
        "options": [
          "Invalida la validazione del codice HTML secondo gli standard del W3C",
          "Provoca il blocco del rendering grafico sui dispositivi basati su processori ARM",
          "Genera una discordanza tra l'ordine visivo a schermo e l'ordine nel DOM, disorientando gli utenti che navigano con tastiera (Tab) o screen reader",
          "Disabilita automaticamente gli eventi JavaScript di ascolto del clic"
        ],
        "correctIndex": 2,
        "explanation": "La proprietà 'order' modifica solo il rendering visivo ma NON altera il Document Object Model (DOM). Chi naviga con tastiera (tasto Tab) o ascolta lo screen reader seguirà la sequenza HTML originale, generando grave disorientamento."
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
        "question": "Nel pattern architetturale del 'Checkbox Hack' per menu mobile CSS-only, quale elemento HTML funge da pulsante cliccabile visibile dall'utente?",
        "options": [
          "Un elemento <label> associato al checkbox tramite l'attributo 'for' che rispecchia l'id dell'input",
          "Un elemento <input type='checkbox'> visualizzato a tutto schermo",
          "Un bottone <button onclick='toggle()'> gestito da JavaScript",
          "Un elemento <a> con ancoraggio href='#menu-toggle'"
        ],
        "correctIndex": 0,
        "explanation": "L'input checkbox viene reso invisibile (es. con display: none o clip). L'utente clicca sull'elemento <label for='menu-toggle'>; il browser cambia lo stato del checkbox permettendo al CSS di intercettare :checked."
      },
      {
        "question": "Quale selettore e combinatore CSS permette di mostrare il menu di navigazione quando il checkbox nascosto viene attivato?",
        "options": [
          ".menu-toggle:hover > nav",
          ".menu-toggle:checked ~ nav (oppure .menu-toggle:checked + nav)",
          "nav:active .menu-toggle",
          "checkbox[status='open'] nav"
        ],
        "correctIndex": 1,
        "explanation": "Lo pseudo-selettore ':checked' rileva lo stato attivo dell'input. Il combinatore fratello adiacente (+) o fratello generale (~) seleziona il menu <nav> situato allo stesso livello gerarchico nel codice."
      },
      {
        "question": "Come viene tipicamente creata l'icona 'hamburger' (le 3 righe orizzontali) senza utilizzare immagini esterne?",
        "options": [
          "Disegnando una tabella HTML con 3 righe e 1 colonna a bordi neri spessi",
          "Scaricando un font raster non compresso da 4 Megabyte",
          "Inserendo tre elementi <span> (o uno span combinato con gli pseudo-elementi ::before e ::after) stilizzati con altezza, larghezza e colore di sfondo",
          "Utilizzando l'emoji standard di un hamburger alimentare 🍔"
        ],
        "correctIndex": 2,
        "explanation": "L'approccio CSS standard ed elegante impiega elementi <span> o pseudo-elementi con background-color, border-radius e transizioni CSS, che possono anche animarsi a 'X' quando aperti."
      },
      {
        "question": "Quale attributo ARIA è opportuno associare al controllo del menu per informare le tecnologie assistive sul fatto che il menu sia aperto o chiuso?",
        "options": [
          "role='dialog-alert'",
          "aria-checked='hidden'",
          "aria-menu-visible='1'",
          "aria-expanded='true'/'false'"
        ],
        "correctIndex": 3,
        "explanation": "'aria-expanded' è l'attributo standard W3C che comunica allo screen reader se il sottomenu o la sezione collassabile associata è attualmente espansa o compressa."
      },
      {
        "question": "Cosa consente la proprietà CSS 'transition: transform 0.3s ease-in-out' applicata al pannello del menu mobile?",
        "options": [
          "Rende l'apertura e chiusura del pannello un'animazione fluida anziché uno scatto istantaneo a comparsa secca",
          "Modifica il colore di sfondo del testo al passaggio del mouse",
          "Costringe il browser a ricaricare la pagina web durante l'animazione",
          "Applica una sfocatura prospettica al logo principale del sito"
        ],
        "correctIndex": 0,
        "explanation": "La proprietà 'transition' interpola dolcemente i valori tra lo stato di riposo (es. transform: translateX(-100%)) e lo stato aperto (:checked ~ nav { transform: translateX(0); }), creando un'esperienza fluida a 60fps."
      }
    ],
    "openQuestions": [
      {
        "question": "Descrivi il funzionamento del Checkbox Hack implementato per il menu mobile, spiegando il ruolo di label, input, :checked e del combinatore ~.",
        "modelAnswer": "Il Checkbox Hack si basa su un input checkbox nascosto (id='menu-toggle') associato a una label con for='menu-toggle' stilizzata a hamburger. Al click sulla label, il browser commuta lo stato del checkbox. Nel CSS, tramite la regola .menu-toggle:checked ~ .nav-menu { display: block; }, quando il checkbox è spuntato, il combinatore fratello generale (~) seleziona il menu <nav> che segue nello stesso genitore e ne mostra i contenuti. Questo permette di gestire l'apertura e chiusura del menu in puro CSS senza dipendere da JavaScript."
      }
    ],
    "examQuiz": [
      {
        "question": "Qual è il limite principale dal punto di vista dell'accessibilità di un menu responsive basato puramente sul 'Checkbox Hack' privo di JavaScript?",
        "options": [
          "I motori di ricerca considerano il sito malevolo e penalizzano il punteggio SEO",
          "L'utente che naviga da tastiera non riceve la gestione del tasto 'Esc' per chiudere il menu né il 'focus trap' che impedisce di navigare sotto il pannello aperto",
          "I browser mobili non supportano lo pseudo-selettore :checked",
          "Il codice CSS richiede più memoria RAM rispetto a uno script JavaScript"
        ],
        "correctIndex": 1,
        "explanation": "Sebbene elegante perché CSS-only, il Checkbox Hack non può gestire pattern complessi come la chiusura con tasto 'Escape' o il confinare il focus da tastiera (focus trapping) all'interno del menu modale, requisiti essenziali per WCAG AAA."
      },
      {
        "question": "Per nascondere il checkbox accessorio dallo schermo mantenendolo accessibile alle tecnologie assistive, quale tecnica è considerata una best practice rispetto a 'display: none'?",
        "options": [
          "Posizionare l'input a top: -99999px causando problemi di scrolling imprevisto",
          "Impostare color: transparent e font-size: 0px",
          "L'uso della classe visivamente nascosta (visually-hidden/sr-only) con clip-path: inset(50%) e width: 1px",
          "Impostare visibility: hidden che rimuove l'elemento dall'albero di accessibilità"
        ],
        "correctIndex": 2,
        "explanation": "'display: none' e 'visibility: hidden' rimuovono l'elemento anche dall'albero di accessibilità degli screen reader. La classe 'sr-only' (visually-hidden) riduce le dimensioni a 1px e ritaglia il box, preservando la navigabilità da tastiera."
      },
      {
        "question": "In quale modo è consigliabile disabilitare il menu mobile su schermi desktop (es. oltre i 768px)?",
        "options": [
          "Cancellare il tag nav tramite selettore di pseudo-classe :not(:mobile)",
          "Ricaricare il documento via JavaScript caricando un foglio di stile differente",
          "Impostare opacity: 0 sul checkbox rendendolo invisibile ma cliccabile",
          "Utilizzare una Media Query '@media (min-width: 768px)' in cui la label hamburger riceve display: none e il tag <nav> torna a display: flex o block statico"
        ],
        "correctIndex": 3,
        "explanation": "Attraverso la media query desktop min-width, si nasconde il bottone/label di toggle (display: none) e si ripristina la visualizzazione orizzontale permanente dei link di navigazione nel flusso della testata."
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
        "question": "Quale filosofia di sviluppo raccomanda di progettare e scrivere le regole CSS partendo dai dispositivi mobili per poi arricchire il layout sugli schermi ampi?",
        "options": [
          "Desktop-Only Degradation",
          "Mobile First (Progressive Enhancement)",
          "Graceful Degradation for Big Screens",
          "Client-Side Adaptive Overwriting"
        ],
        "correctIndex": 1,
        "explanation": "La metodologia 'Mobile First' impone di impostare le regole base per schermi piccoli (semplici, leggere, a colonna singola) e aggiungere complessità su schermi più grandi tramite media queries con 'min-width'."
      },
      {
        "question": "Qual è la sintassi corretta di una Media Query che applica determinati stili unicamente a partire da una larghezza schermo minima di 768px?",
        "options": [
          "@media (device-resolution: 768px) { ... }",
          "@viewport-width >= 768px { ... }",
          "@media screen and (min-width: 768px) { ... }",
          "@media screen and (max-width: 767px) { ... }"
        ],
        "correctIndex": 2,
        "explanation": "La direttiva '@media (min-width: 768px)' attiva il blocco di regole CSS per tutte le finestre con ampiezza pari o superiore a 768 pixel, tipica soglia per layout tablet e desktop."
      },
      {
        "question": "Cosa assicura la proprietà CSS 'object-fit: cover' applicata alle immagini all'interno delle card?",
        "options": [
          "Comprime l'immagine riducendo il peso in byte del file scaricato",
          "Stira forzatamente l'immagine in altezza e larghezza fino a riempire il riquadro anche se viene deformata",
          "Applica una maschera circolare a tutti i quattro angoli del contenitore",
          "Scala l'immagine mantenendo le proporzioni e ritagliando le parti eccedenti per riempire completamente il box senza deformazioni"
        ],
        "correctIndex": 3,
        "explanation": "'object-fit: cover' è analoga a 'background-size: cover': preserva l'aspect ratio naturale della fotografia o illustrazione, ritagliando le parti esterne in modo che non appaia mai schiacciata o allungata."
      },
      {
        "question": "Cosa permette di realizzare la funzione CSS moderna 'clamp(1rem, 2.5vw, 2rem)' per la dimensione dei testi tipografici?",
        "options": [
          "Imposta una dimensione fluida che scala con la larghezza del viewport (2.5vw), vincolata tra una soglia minima (1rem) e una massima (2rem)",
          "Arrotonda la misura del carattere al valore intero di pixel più vicino",
          "Forza il testo a rimanere esattamente fisso a 2.5 centimetri su qualsiasi dispositivo",
          "Converte automaticamente i caratteri minuscoli in maiuscoletto sopra i 2rem"
        ],
        "correctIndex": 0,
        "explanation": "La funzione 'clamp(min, preferred, max)' crea la tipografia fluida ideale: il testo cresce proporzionalmente alla larghezza dello schermo (2.5vw), garantendo che non diventi mai né troppo piccolo né eccessivamente grande."
      },
      {
        "question": "Quale unità di misura per i font è preferibile rispetto ai pixel (px) per rispettare le impostazioni di accessibilità dell'utente nel browser?",
        "options": [
          "I centimetri (cm)",
          "L'unità relativa 'rem' (root em)",
          "I punti tipografici di stampa (pt)",
          "I millimetri (mm)"
        ],
        "correctIndex": 1,
        "explanation": "L'unità 'rem' è relativa alla dimensione base del font definita nell'elemento radice <html> (solitamente 16px di default). Se un utente ipovedente aumenta la dimensione caratteri nelle preferenze di sistema del browser, i testi in 'rem' scalano correttamente, cosa che i pixel fissi ostacolano."
      }
    ],
    "openQuestions": [
      {
        "question": "Spiega il funzionamento di object-fit: cover e descrivi le tecniche CSS usate per rendere le card interattive e responsive.",
        "modelAnswer": "object-fit: cover permette a un'immagine con width: 100% e height: 200px di riempire esattamente il contenitore senza deformare le proporzioni native, ritagliando le parti eccedenti. Per l'interattività, la card utilizza box-shadow e transform: translateY(-8px) con transition: 0.3s ease per simulare un sollevamento tridimensionale fluido al passaggio del cursore (:hover). Per la responsività, le card sono inserite in una griglia CSS (repeat(3, 1fr)) che scala a 2 e poi a 1 colonna sui dispositivi mobili tramite media queries."
      }
    ],
    "examQuiz": [
      {
        "question": "Un designer propone di utilizzare breakpoint basati sulle dimensioni esatte dell'iPhone 15 e dell'iPad Pro. Perché questo approccio è sconsigliato nelle best practice del Responsive Web Design?",
        "options": [
          "Perché i moderni motori browser ignorano le media query che corrispondono a marchi commerciali registrati",
          "Perché Apple impedisce l'uso del CSS responsive sui propri dispositivi mobili",
          "Perché i breakpoint non dovrebbero essere fissati sui singoli dispositivi ma sui 'punti di rottura' naturali in cui il contenuto e il layout iniziano a degradare",
          "Perché i dispositivi tablet non supportano display con orientamento orizzontale (landscape)"
        ],
        "correctIndex": 2,
        "explanation": "Il parco dispositivi è infinito e in continua mutazione. I breakpoint devono essere guidati dal contenuto (Content-out), ovvero collocati dove la leggibilità o la gerarchia visiva richiedono una riorganizzazione (es. quando le colonne diventano troppo strette o le righe troppo lunghe)."
      },
      {
        "question": "Qual è la differenza pratica tra l'utilizzo della media query '@media (prefers-reduced-motion: reduce)' e le animazioni standard?",
        "options": [
          "Disabilita automaticamente il touch screen forzando l'uso del mouse",
          "Aumenta la frequenza dei fotogrammi (FPS) della GPU sui telefoni da gaming",
          "Sostituisce i video HTML5 con file audio WAV",
          "Consente di disabilitare o semplificare animazioni, scorrimenti veloci e transizioni per utenti che soffrono di disturbi vestibolari o cinetosi"
        ],
        "correctIndex": 3,
        "explanation": "'prefers-reduced-motion' è una media feature di accessibilità fondamentale: intercetta l'impostazione di sistema dell'utente che richiede di minimizzare il movimento non essenziale per evitare vertigini, nausea o distrazione cognitiva."
      },
      {
        "question": "Se un'immagine ha 'max-width: 100%; height: auto;', quale comportamento garantisce all'interno di un layout responsive?",
        "options": [
          "L'immagine non supererà mai la larghezza del proprio contenitore genitore e manterrà inalterate le proprie proporzioni scalando verso il basso",
          "L'immagine si espanderà per occupare sempre il 100% dell'altezza dell'intero schermo",
          "L'immagine verrà caricata in formato SVG vettoriale a qualsiasi risoluzione",
          "L'immagine forzerà il genitore ad allargarsi fino alla risoluzione nativa del file bitmap"
        ],
        "correctIndex": 0,
        "explanation": "'max-width: 100%' impedisce all'immagine di debordare dal genitore nei display piccoli, mentre 'height: auto' permette al browser di calcolare l'altezza in base al rapporto di forma nativo, evitando qualsiasi distorsione visiva."
      }
    ]
  }
];
