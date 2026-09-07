# -*- coding: utf-8 -*-
"""
Rebuilds data/progetto-cards-data.js with:
1. High-level academic chapter quizzes (chap.quiz) with realistic, technical distractors and balanced correctIndex.
2. Distinct exam simulation questions (chap.examQuiz) testing code comprehension, layout debugging, and CSS/HTML specifications.
"""

import json, re

cards_modules_quiz = {
    "cards-m1": {
        "quiz": [
            {
                "question": "Nel codice di index.html, quale tag semantico HTML5 è specificamente deputato a racchiudere i link di navigazione principale del sito?",
                "options": [
                    "Il tag strutturale <aside>, riservato a contenuti tangenziali",
                    "Il tag generico <section id='nav'> privo di semantica di navigazione",
                    "Il tag <nav>, che funge da landmark accessibile per browser e screen reader",
                    "Il tag <menu>, deprecato nelle specifiche HTML moderne"
                ],
                "correctIndex": 2,
                "explanation": "Il tag HTML5 standard deputato a racchiudere i collegamenti primari è <nav>. Esso definisce un landmark di navigazione che consente alle tecnologie assistive di saltare direttamente al menu senza scorrere l'intera pagina."
            },
            {
                "question": "Qual è la funzione tecnica fondamentale dell'istruzione <meta name='viewport' content='width=device-width, initial-scale=1.0'> inserita nell'<head>?",
                "options": [
                    "Forza la larghezza del viewport a coincidere con i pixel fisici del dispositivo impedendo il rendering desktop rimpicciolito",
                    "Disabilita permanentemente lo zoom tattile per impedire rotture del layout grafico",
                    "Adatta automaticamente la densità di pixel delle immagini bitmap alla risoluzione dello schermo",
                    "Imposta la risoluzione di rendering a un valore fisso di 980px con scrolling orizzontale automatico"
                ],
                "correctIndex": 0,
                "explanation": "Nei dispositivi mobili senza meta viewport, il browser assume una larghezza virtuale di circa 980px scalando la pagina e rendendo i testi minuscoli. L'istruzione impone un rapporto 1:1 tra pixel CSS e viewport del dispositivo."
            },
            {
                "question": "Per quale ragione l'attributo lang='it' all'interno dell'elemento <html> è considerato un requisito critico di accessibilità WCAG?",
                "options": [
                    "Permette ai motori di ricerca di indicizzare il sito escludendolo dai risultati internazionali",
                    "Indica al software di sintesi vocale (screen reader) quale motore fonetico e di pronuncia applicare",
                    "Attiva automaticamente i caratteri tipografici con glifi e accenti specifici della lingua italiana",
                    "Garantisce che la codifica dei caratteri venga forzata a ISO-8859-1 anziché UTF-8"
                ],
                "correctIndex": 1,
                "explanation": "I sintetizzatori vocali utilizzano l'attributo 'lang' per caricare le corrette regole di pronuncia fonetica e accentazione. Senza di esso, un lettore vocale configurato in inglese leggerebbe il testo italiano con fonetica anglosassone."
            },
            {
                "question": "Cosa comporterebbe l'omissione della dichiarazione <!doctype html> nella prima riga del file HTML?",
                "options": [
                    "La mancata esecuzione di tutti gli script JavaScript esterni collegati al documento",
                    "L'attivazione della modalità Quirks da parte del browser, con calcolo errato del Box Model e delle dimensioni",
                    "Il rifiuto da parte del server web di trasmettere il documento con codice di stato HTTP 200",
                    "L'impossibilità di applicare classi e ID tramite selettori nei fogli di stile CSS esterni"
                ],
                "correctIndex": 1,
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
                    "Associare esplicitamente un elemento <label for='id_campo'> all'input con id corrispondente",
                    "Inserire il testo della label in uno <span> adiacente formattato con CSS",
                    "Affidarsi unicamente all'attributo title sull'elemento input"
                ],
                "correctIndex": 1,
                "explanation": "L'associazione esplicita tramite for/id permette alle tecnologie assistive di annunciare l'etichetta al focus e consente agli utenti su mobile o desktop di cliccare sulla label per attivare il campo."
            },
            {
                "question": "Quale differenza intercorre tra l'utilizzo dell'elemento <section> e dell'elemento <div> secondo le specifiche W3C?",
                "options": [
                    "I <div> possono contenere classi CSS mentre i <section> supportano unicamente attributi inline",
                    "Non esiste differenza tecnica, l'uso di <section> è puramente convenzionale",
                    "La <section> definisce una porzione tematica del documento tipicamente introdotta da un'intestazione (h2-h6), mentre il <div> è un mero contenitore stilistico neutro",
                    "La <section> impone automaticamente un display: flex mentre il <div> ha display: block"
                ],
                "correctIndex": 2,
                "explanation": "La <section> è un elemento di sezione semantica con valore strutturale che raggruppa contenuti omogenei dotati di una propria intestazione. Il <div> è un contenitore generico privo di qualsiasi significato semantico, impiegato per fini stilistici."
            }
        ]
    },
    "cards-m2": {
        "quiz": [
            {
                "question": "Se a un elemento con width: 300px e box-sizing: content-box vengono applicati padding: 20px su tutti i lati e border: 2px solid, quale sarà la larghezza totale occupata nel layout?",
                "options": [
                    "300 pixel, poiché il padding si espande verso l'interno senza alterare i bordi",
                    "320 pixel, sommando solo il padding orizzontale e ignorando lo spessore del bordo",
                    "344 pixel, risultante da 300px + 40px di padding totale + 4px di bordi totali",
                    "256 pixel, poiché lo spazio di padding e bordo viene sottratto dalla larghezza dichiarata"
                ],
                "correctIndex": 2,
                "explanation": "Nel box-sizing standard (content-box), la larghezza finale corrisponde a: width + padding-left + padding-right + border-left + border-right = 300 + 20 + 20 + 2 + 2 = 344px."
            },
            {
                "question": "Qual è il beneficio fondamentale della regola di reset globale '* , *::before, *::after { box-sizing: border-box; }'?",
                "options": [
                    "Elimina qualsiasi margine tra gli elementi della pagina rendendo superfluo Flexbox",
                    "Include padding e bordi all'interno della larghezza e altezza dichiarate, rendendo i calcoli percentuali esatti e stabili",
                    "Forza tutti gli elementi della pagina ad avere proporzioni rettangolari auree",
                    "Impedisce agli elementi inline di superare la larghezza del genitore contenitore"
                ],
                "correctIndex": 1,
                "explanation": "Con border-box, impostare width: 50% garantisce che l'elemento occuperà esattamente la metà dello spazio disponibile anche aggiungendo padding interni o bordi decorativi, senza generare overflow indesiderati."
            },
            {
                "question": "Cosa accade nel fenomeno del 'collasso dei margini verticali' (margin collapse) tra due elementi a blocco adiacenti?",
                "options": [
                    "I due margini verticali si sommano algebricamente raddoppiando la spaziatura finale",
                    "I due margini collassano fondendosi nel valore del margine più grande tra i due",
                    "Il browser annulla entrambi i margini impostando la spaziatura verticale a zero pixel",
                    "Il margine dell'elemento inferiore sovrascrive quello superiore soltanto se è espresso in percentuali"
                ],
                "correctIndex": 1,
                "explanation": "Nel normale flusso di blocco, i margini verticali adiacenti si sovrappongono: se il primo blocco ha margin-bottom: 30px e il secondo margin-top: 20px, la distanza effettiva tra essi sarà 30px, non 50px."
            },
            {
                "question": "In quale tra i seguenti contesti di formattazione NON si verifica il collasso dei margini verticali?",
                "options": [
                    "Tra paragrafi <p> consecutivi nel normale flusso del documento",
                    "Tra il primo elemento figlio e il contenitore genitore privo di padding e bordo",
                    "All'interno di elementi con contesto di formattazione Flexbox o CSS Grid",
                    "Tra titoli <h2> e paragrafi successivi formattati con display: block"
                ],
                "correctIndex": 2,
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
        "examQuiz": [
            {
                "question": "Due elementi a blocco hanno rispettivamente margin-bottom: 24px e margin-top: 16px. Se entrambi sono inseriti all'interno di un contenitore con display: flex e flex-direction: column, quale sarà la loro distanza verticale?",
                "options": [
                    "24 pixel, a causa del classico collasso dei margini verticali",
                    "40 pixel, poiché all'interno di un flex container i margini verticali non collassano",
                    "16 pixel, prevalendo sempre il margine dell'elemento successivo",
                    "8 pixel, calcolando la differenza assoluta tra i due valori"
                ],
                "correctIndex": 1,
                "explanation": "All'interno di un flex container (anche con direzione column), gli elementi figli stabiliscono contesti indipendenti e i margini non collassano: 24px + 16px = 40px."
            },
            {
                "question": "Un elemento div ha width: 100%, padding: 16px e margin: 0, ma genera una barra di scorrimento orizzontale imprevista. Qual è la diagnosi più probabile del bug?",
                "options": [
                    "L'elemento genitore ha impostato display: inline-block",
                    "L'elemento sta calcolando le dimensioni con box-sizing: content-box anziché border-box",
                    "I browser moderni non supportano valori percentuali per la proprietà width sui tag div",
                    "L'elemento contiene testo privo di proprietà text-overflow: ellipsis"
                ],
                "correctIndex": 1,
                "explanation": "Con content-box, width: 100% occupa l'intero spazio del genitore; aggiungendo i 16px di padding su entrambi i lati, la larghezza totale diventa 100% + 32px, causando overflow orizzontale."
            },
            {
                "question": "Perché nel reset moderno universale si applica 'box-sizing: border-box' anche agli pseudo-elementi *::before e *::after?",
                "options": [
                    "Perché gli pseudo-elementi altrimenti non verrebbero renderizzati dal motore del browser",
                    "Per evitare che icone, badge decorativi o sagome generate via CSS causino overflow imprevisti sommando padding e bordi",
                    "Per forzare gli pseudo-elementi ad assumere un posizionamento assoluto di default",
                    "Per consentire l'inserimento di codice HTML all'interno della proprietà content"
                ],
                "correctIndex": 1,
                "explanation": "Gli pseudo-elementi ::before e ::after sono ampiamente impiegati per decorazioni grafiche, badge o clearing; includerli nel reset assicura che qualsiasi padding o bordo applicato rispetti il medesimo calcolo geometrico del resto dell'interfaccia."
            }
        ]
    },
    "cards-m3": {
        "quiz": [
            {
                "question": "Cosa rappresenta l'unità di misura 'fr' (frazione) introdotta nelle specifiche CSS Grid?",
                "options": [
                    "Una percentuale fissa calcolata esclusivamente rispetto all'altezza dello schermo",
                    "Una frazione dello spazio libero rimanente all'interno del contenitore griglia dopo l'assegnazione degli spazi fissi",
                    "La frequenza di refresh del rendering applicata alla griglia vettoriale",
                    "Un valore relativo all'ampiezza tipografica del glifo 'F' del font genitore"
                ],
                "correctIndex": 1,
                "explanation": "L'unità 'fr' (fractional unit) distribuisce lo spazio libero non allocato. Ad esempio, '1fr 2fr' divide lo spazio residuo in 3 parti uguali, assegnandone 1 alla prima colonna e 2 alla seconda."
            },
            {
                "question": "Quale comportamento produce la dichiarazione 'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));'?",
                "options": [
                    "Crea una griglia con un numero fisso di 4 colonne a larghezza fissa di 280px",
                    "Genera un layout responsive dinamico che inserisce quante più colonne da almeno 280px possibile, espandendole proporzionalmente per riempire la riga",
                    "Comprime tutte le card a 280px forzando lo scroll orizzontale sui dispositivi con schermo inferiore",
                    "Richiede obbligatoriamente l'aggiunta di media queries specifiche per ogni singolo breakpoint"
                ],
                "correctIndex": 1,
                "explanation": "Questa formula è il cardine del responsive design con Grid: crea automaticamente nuove colonne se lo spazio lo consente (almeno 280px ciascuna) ed espande le colonne esistenti fino a 1fr per non lasciare spazi vuoti."
            },
            {
                "question": "Qual è la differenza fondamentale tra 'auto-fill' e 'auto-fit' nella definizione delle colonne di una griglia CSS?",
                "options": [
                    "auto-fill funziona solo sui dispositivi mobili, mentre auto-fit è destinato agli schermi desktop",
                    "auto-fill mantiene le colonne vuote create nello spazio residuo, mentre auto-fit le collassa a zero permettendo alle colonne occupate di espandersi",
                    "Non sussiste alcuna differenza reale, sono sinonimi introdotti per retrocompatibilità",
                    "auto-fill calcola le righe mentre auto-fit calcola unicamente le colonne verticali"
                ],
                "correctIndex": 1,
                "explanation": "Quando gli elementi non riempiono l'intera larghezza, 'auto-fill' preserva lo spazio delle colonne vuote rimanenti; 'auto-fit' collassa le colonne vuote permettendo agli elementi presenti di dilatarsi per colmare tutta la riga."
            },
            {
                "question": "Quale proprietà CSS sostituisce in modo pulito l'uso di margini per distanziare celle e righe in un contenitore CSS Grid?",
                "options": [
                    "La proprietà 'gap' (oppure row-gap e column-gap)",
                    "La proprietà 'cell-spacing' ereditata dalle tabelle HTML",
                    "La proprietà 'grid-padding-between'",
                    "La proprietà 'margin-collapse: separate'"
                ],
                "correctIndex": 0,
                "explanation": "La proprietà standard 'gap' definisce la spaziatura esatta tra righe e colonne senza applicare margini ai bordi esterni del contenitore, eliminando la necessità di hack come :last-child."
            },
            {
                "question": "Se in un layout a griglia una card deve estendersi per occupare l'intera larghezza di una griglia a 3 colonne, quale istruzione è corretta?",
                "options": [
                    "grid-column: span 3; (oppure grid-column: 1 / -1;)",
                    "width: 300%;",
                    "grid-row: full-width;",
                    "display: inline-grid; colspan: 3;"
                ],
                "correctIndex": 0,
                "explanation": "'grid-column: span 3' ordina all'elemento di espandersi su 3 tracce colonna. La notazione '1 / -1' estende l'elemento dalla prima linea di traccia all'ultima linea esplicita."
            }
        ],
        "examQuiz": [
            {
                "question": "In una griglia CSS con 'grid-template-columns: repeat(3, 1fr)' e gap: 20px, come viene calcolata l'effettiva larghezza di ciascuna delle 3 colonne su una larghezza totale di 940px?",
                "options": [
                    "940px diviso 3 = 313.33px, e il gap viene aggiunto esternamente debordando dal contenitore",
                    "Si sottraggono prima i due gap (20px * 2 = 40px) ottenendo 900px, quindi si divide per 3, assegnando 300px a ciascuna colonna",
                    "Ciascuna colonna occupa 940px / 3 meno 20px = 293.33px, lasciando 60px non allocati",
                    "Il browser assegna 33.33% a ogni colonna e annulla la proprietà gap in presenza di 1fr"
                ],
                "correctIndex": 1,
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
    "cards-m4": {
        "quiz": [
            {
                "question": "All'interno di un contenitore flessibile con flex-direction: row, quale proprietà allinea gli elementi lungo l'asse principale (orizzontale)?",
                "options": [
                    "align-items",
                    "justify-content",
                    "flex-wrap",
                    "align-content"
                ],
                "correctIndex": 1,
                "explanation": "L'asse principale (main axis) è governato da 'justify-content' (es. flex-start, center, space-between, flex-end). L'asse trasversale (cross axis) è invece governato da 'align-items'."
            },
            {
                "question": "Cosa accade quando su un contenitore flessibile viene impostata la proprietà 'flex-wrap: wrap'?",
                "options": [
                    "Gli elementi figli vengono forzati a comprimersi sulla stessa riga rimpicciolendosi all'infinito",
                    "Gli elementi che superano la larghezza disponibile vanno a capo creando una nuova riga anziché debordare",
                    "Il contenitore converte automaticamente il suo modello di rendering in una tabella HTML",
                    "Tutti gli elementi figli assumono una larghezza fissa del 50%"
                ],
                "correctIndex": 1,
                "explanation": "Di default i flex items tentano di stare su una sola riga ('nowrap'). Impostando 'flex-wrap: wrap', quando la somma delle dimensioni eccede lo spazio del genitore, gli elementi scorrono ordinatamente su una nuova riga."
            },
            {
                "question": "Per centrare perfettamente un elemento sia in orizzontale che in verticale all'interno di un contenitore, quale combinazione CSS è più sintetica ed efficace?",
                "options": [
                    "display: flex; justify-content: center; align-items: center;",
                    "position: absolute; margin: auto; float: left;",
                    "display: inline-block; vertical-align: middle; text-align: center;",
                    "display: flex; flex-direction: column; align-self: baseline;"
                ],
                "correctIndex": 0,
                "explanation": "Impostando il contenitore come 'display: flex', la coppia 'justify-content: center' (asse principale) e 'align-items: center' (asse trasversale) garantisce il perfetto centraggio bidimensionale."
            },
            {
                "question": "Cosa indica la notazione sintetica 'flex: 1' applicata a un elemento figlio in un flex container?",
                "options": [
                    "Che l'elemento deve avere una larghezza minima rigida di 1px",
                    "Equivale a 'flex: 1 1 0%', permettendo all'elemento di espandersi e ridursi proporzionalmente assorbendo lo spazio libero",
                    "Che l'elemento sarà l'unico elemento renderizzato nel contenitore",
                    "Che l'elemento possiede una priorità di stacking z-index pari a 1"
                ],
                "correctIndex": 1,
                "explanation": "'flex: 1' espande la proprietà 'flex-grow: 1', 'flex-shrink: 1' e 'flex-basis: 0%'. Consente al componente di riempire elasticamente lo spazio disponibile equamente tra fratelli con il medesimo valore."
            },
            {
                "question": "A cosa serve la proprietà 'align-self' in Flexbox?",
                "options": [
                    "Permette a un singolo elemento figlio di sovrascrivere l'allineamento sull'asse trasversale stabilito da 'align-items' sul genitore",
                    "Permette di riordinare sequenzialmente gli elementi all'interno del flusso DOM",
                    "Centra il testo tipografico all'interno del proprio box di contenuto",
                    "Allinea l'intero flex container rispetto al centro della finestra del browser"
                ],
                "correctIndex": 0,
                "explanation": "'align-self' accetta i medesimi valori di 'align-items' (es. flex-start, center, flex-end, stretch) ma viene applicata al singolo elemento figlio per personalizzarne la posizione sull'asse trasversale."
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
                    "Genera una discordanza tra l'ordine visivo a schermo e l'ordine nel DOM, disorientando gli utenti che navigano con tastiera (Tab) o screen reader",
                    "Provoca il blocco del rendering grafico sui dispositivi basati su processori ARM",
                    "Invalida la validazione del codice HTML secondo gli standard del W3C",
                    "Disabilita automaticamente gli eventi JavaScript di ascolto del clic"
                ],
                "correctIndex": 0,
                "explanation": "La proprietà 'order' modifica solo il rendering visivo ma NON altera il Document Object Model (DOM). Chi naviga con tastiera (tasto Tab) o ascolta lo screen reader seguirà la sequenza HTML originale, generando grave disorientamento."
            }
        ]
    },
    "cards-m5": {
        "quiz": [
            {
                "question": "Nel pattern architetturale del 'Checkbox Hack' per menu mobile CSS-only, quale elemento HTML funge da pulsante cliccabile visibile dall'utente?",
                "options": [
                    "Un elemento <input type='checkbox'> visualizzato a tutto schermo",
                    "Un elemento <label> associato al checkbox tramite l'attributo 'for' che rispecchia l'id dell'input",
                    "Un bottone <button onclick='toggle()'> gestito da JavaScript",
                    "Un elemento <a> con ancoraggio href='#menu-toggle'"
                ],
                "correctIndex": 1,
                "explanation": "L'input checkbox viene reso invisibile (es. con display: none o clip). L'utente clicca sull'elemento <label for='menu-toggle'>; il browser cambia lo stato del checkbox permettendo al CSS di intercettare :checked."
            },
            {
                "question": "Quale selettore e combinatore CSS permette di mostrare il menu di navigazione quando il checkbox nascosto viene attivato?",
                "options": [
                    ".menu-toggle:checked ~ nav (oppure .menu-toggle:checked + nav)",
                    ".menu-toggle:hover > nav",
                    "nav:active .menu-toggle",
                    "checkbox[status='open'] nav"
                ],
                "correctIndex": 0,
                "explanation": "Lo pseudo-selettore ':checked' rileva lo stato attivo dell'input. Il combinatore fratello adiacente (+) o fratello generale (~) seleziona il menu <nav> situato allo stesso livello gerarchico nel codice."
            },
            {
                "question": "Come viene tipicamente creata l'icona 'hamburger' (le 3 righe orizzontali) senza utilizzare immagini esterne?",
                "options": [
                    "Inserendo tre elementi <span> (o uno span combinato con gli pseudo-elementi ::before e ::after) stilizzati con altezza, larghezza e colore di sfondo",
                    "Scaricando un font raster non compresso da 4 Megabyte",
                    "Disegnando una tabella HTML con 3 righe e 1 colonna a bordi neri spessi",
                    "Utilizzando l'emoji standard di un hamburger alimentare 🍔"
                ],
                "correctIndex": 0,
                "explanation": "L'approccio CSS standard ed elegante impiega elementi <span> o pseudo-elementi con background-color, border-radius e transizioni CSS, che possono anche animarsi a 'X' quando aperti."
            },
            {
                "question": "Quale attributo ARIA è opportuno associare al controllo del menu per informare le tecnologie assistive sul fatto che il menu sia aperto o chiuso?",
                "options": [
                    "aria-expanded='true'/'false'",
                    "aria-checked='hidden'",
                    "aria-menu-visible='1'",
                    "role='dialog-alert'"
                ],
                "correctIndex": 0,
                "explanation": "'aria-expanded' è l'attributo standard W3C che comunica allo screen reader se il sottomenu o la sezione collassabile associata è attualmente espansa o compressa."
            },
            {
                "question": "Cosa consente la proprietà CSS 'transition: transform 0.3s ease-in-out' applicata al pannello del menu mobile?",
                "options": [
                    "Modifica il colore di sfondo del testo al passaggio del mouse",
                    "Rende l'apertura e chiusura del pannello un'animazione fluida anziché uno scatto istantaneo a comparsa secca",
                    "Costringe il browser a ricaricare la pagina web durante l'animazione",
                    "Applica una sfocatura prospettica al logo principale del sito"
                ],
                "correctIndex": 1,
                "explanation": "La proprietà 'transition' interpola dolcemente i valori tra lo stato di riposo (es. transform: translateX(-100%)) e lo stato aperto (:checked ~ nav { transform: translateX(0); }), creando un'esperienza fluida a 60fps."
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
                    "L'uso della classe visivamente nascosta (visually-hidden/sr-only) con clip-path: inset(50%) e width: 1px",
                    "Impostare color: transparent e font-size: 0px",
                    "Posizionare l'input a top: -99999px causando problemi di scrolling imprevisto",
                    "Impostare visibility: hidden che rimuove l'elemento dall'albero di accessibilità"
                ],
                "correctIndex": 0,
                "explanation": "'display: none' e 'visibility: hidden' rimuovono l'elemento anche dall'albero di accessibilità degli screen reader. La classe 'sr-only' (visually-hidden) riduce le dimensioni a 1px e ritaglia il box, preservando la navigabilità da tastiera."
            },
            {
                "question": "In quale modo è consigliabile disabilitare il menu mobile su schermi desktop (es. oltre i 768px)?",
                "options": [
                    "Utilizzare una Media Query '@media (min-width: 768px)' in cui la label hamburger riceve display: none e il tag <nav> torna a display: flex o block statico",
                    "Ricaricare il documento via JavaScript caricando un foglio di stile differente",
                    "Impostare opacity: 0 sul checkbox rendendolo invisibile ma cliccabile",
                    "Cancellare il tag nav tramite selettore di pseudo-classe :not(:mobile)"
                ],
                "correctIndex": 0,
                "explanation": "Attraverso la media query desktop min-width, si nasconde il bottone/label di toggle (display: none) e si ripristina la visualizzazione orizzontale permanente dei link di navigazione nel flusso della testata."
            }
        ]
    },
    "cards-m6": {
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
                    "@media screen and (min-width: 768px) { ... }",
                    "@viewport-width >= 768px { ... }",
                    "@media (device-resolution: 768px) { ... }",
                    "@media screen and (max-width: 767px) { ... }"
                ],
                "correctIndex": 0,
                "explanation": "La direttiva '@media (min-width: 768px)' attiva il blocco di regole CSS per tutte le finestre con ampiezza pari o superiore a 768 pixel, tipica soglia per layout tablet e desktop."
            },
            {
                "question": "Cosa assicura la proprietà CSS 'object-fit: cover' applicata alle immagini all'interno delle card?",
                "options": [
                    "Comprime l'immagine riducendo il peso in byte del file scaricato",
                    "Scala l'immagine mantenendo le proporzioni e ritagliando le parti eccedenti per riempire completamente il box senza deformazioni",
                    "Applica una maschera circolare a tutti i quattro angoli del contenitore",
                    "Stira forzatamente l'immagine in altezza e larghezza fino a riempire il riquadro anche se viene deformata"
                ],
                "correctIndex": 1,
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
                    "I punti tipografici di stampa (pt)",
                    "L'unità relativa 'rem' (root em)",
                    "I millimetri (mm)"
                ],
                "correctIndex": 2,
                "explanation": "L'unità 'rem' è relativa alla dimensione base del font definita nell'elemento radice <html> (solitamente 16px di default). Se un utente ipovedente aumenta la dimensione caratteri nelle preferenze di sistema del browser, i testi in 'rem' scalano correttamente, cosa che i pixel fissi ostacolano."
            }
        ],
        "examQuiz": [
            {
                "question": "Un designer propone di utilizzare breakpoint basati sulle dimensioni esatte dell'iPhone 15 e dell'iPad Pro. Perché questo approccio è sconsigliato nelle best practice del Responsive Web Design?",
                "options": [
                    "Perché i moderni motori browser ignorano le media query che corrispondono a marchi commerciali registrati",
                    "Perché i breakpoint non dovrebbero essere fissati sui singoli dispositivi ma sui 'punti di rottura' naturali in cui il contenuto e il layout iniziano a degradare",
                    "Perché Apple impedisce l'uso del CSS responsive sui propri dispositivi mobili",
                    "Perché i dispositivi tablet non supportano display con orientamento orizzontale (landscape)"
                ],
                "correctIndex": 1,
                "explanation": "Il parco dispositivi è infinito e in continua mutazione. I breakpoint devono essere guidati dal contenuto (Content-out), ovvero collocati dove la leggibilità o la gerarchia visiva richiedono una riorganizzazione (es. quando le colonne diventano troppo strette o le righe troppo lunghe)."
            },
            {
                "question": "Qual è la differenza pratica tra l'utilizzo della media query '@media (prefers-reduced-motion: reduce)' e le animazioni standard?",
                "options": [
                    "Consente di disabilitare o semplificare animazioni, scorrimenti veloci e transizioni per utenti che soffrono di disturbi vestibolari o cinetosi",
                    "Aumenta la frequenza dei fotogrammi (FPS) della GPU sui telefoni da gaming",
                    "Sostituisce i video HTML5 con file audio WAV",
                    "Disabilita automaticamente il touch screen forzando l'uso del mouse"
                ],
                "correctIndex": 0,
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
}

# Update data/progetto-cards-data.js
with open("data/progetto-cards-data.js", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"window\.CARDS_DATA\s*=\s*(\[.*\]);?", content, re.DOTALL)
if not m:
    raise Exception("Could not find window.CARDS_DATA in data/progetto-cards-data.js")

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
    if cid in cards_modules_quiz:
        quizzes = cards_modules_quiz[cid]["quiz"]
        exam_quizzes = cards_modules_quiz[cid]["examQuiz"]
        for idx, q in enumerate(quizzes):
            balance_question(q, (idx + c_idx) % 4)
        for idx, eq in enumerate(exam_quizzes):
            balance_question(eq, (idx + c_idx + 1) % 4)
        chap["quiz"] = quizzes
        chap["examQuiz"] = exam_quizzes
        print(f"Updated {cid}: {len(chap['quiz'])} quiz, {len(chap['examQuiz'])} examQuiz")

with open("data/progetto-cards-data.js", "w", encoding="utf-8") as f:
    f.write(f"// Moduli didattici basati sul codice reale di Progetto_Esame_Cards\nwindow.CARDS_DATA = {json.dumps(data, indent=2, ensure_ascii=False)};\n")

print("Successfully rebuilt data/progetto-cards-data.js!")
