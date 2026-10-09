# AGENTS.md — Istruzioni per gli assistenti AI (Studio ABA Catania)

Questo è l'**unico** file di istruzioni del progetto. `CLAUDE.md` e `GEMINI.md` sono collegamenti a questo file.
Va aggiornato **ogni volta** che si cambia la struttura, si aggiunge una materia o si introduce una nuova convenzione.
`README.md` è invece la presentazione pubblica per gli studenti: non contiene istruzioni tecniche.

---

## 1. Regole assolute

1. **Nessuna emoji, mai.** Né nel codice, né nell'interfaccia, né nei testi, nei commenti, nei toast, nei placeholder, nei titoli o nei file Markdown. Vietati anche i simboli Unicode usati come icone (stelle, spunte, frecce decorative, dischetti, ecc.).
   - Se serve un'icona: SVG inline con `stroke="currentColor"` o `fill="currentColor"`.
   - Se serve enfasi: CSS (colore d'accento, badge testuali, bordi, peso del font).
2. **Italiano corretto con gli accenti** in tutti i contenuti visibili: `è`, `perché`, `qualità`, `più`, `città`. Mai `e'`, `perche`, `qualita`.
3. **Opere d'arte: solo immagini autentiche** (musei, archivi, Wikimedia Commons). Vietato generare con AI quadri, sculture, fotografie d'autore o qualsiasi opera reale.
   Le immagini generate sono ammesse **solo** per schemi concettuali e diagrammi astratti, con pochissimo testo (solo i nomi essenziali, niente paragrafi).
4. **Nessun framework e nessun build step.** HTML, CSS e JavaScript vanilla, percorsi relativi (`./`, `../`), il sito deve funzionare su GitHub Pages così com'è.
5. **Non rinominare gli ID e le classi del contratto** (sezione 5): `core.js` e `auth.js` dipendono da essi.
6. Dopo ogni modifica eseguire `node tools/check-data.js` e correggere tutti gli **ERRORI** (sezione 9).

---

## 2. Mappa del progetto

```
index.html            Home: presentazione, "Riprendi lo studio", materie disponibili (dal registro), funzioni
corsi.html            Tutti i corsi: Corso -> Anno -> Materia (logica inline nel <script> in fondo)
home.css              Stili di index.html e corsi.html
styles.css            Design system condiviso: token, temi, colori dei corsi, layout desktop/mobile
README.md             Presentazione pubblica per gli studenti
AGENTS.md             Questo file (CLAUDE.md e GEMINI.md sono link simbolici)

js/
  theme-boot.js       Applica il tema salvato prima del caricamento (primo elemento del <body>)
  subjects.js         REGISTRO DELLE MATERIE: titolo, docente, corso/anno, moduli, file dati
  layout.js           Genera tutto il markup della pagina di studio a partire dal registro
  core.js             Motore: stato, salvataggio, capitoli, flashcard (ripasso a intervalli), quiz, esame, glossario, lettore vocale, Markdown
  practice.js         Vista "Allenati": ripasso flashcard, simulazione dell'orale, progressi
  subject-app.js      Avvio generico della pagina di studio (legge il registro)
  auth.js             Supabase: login, registrazione, sincronizzazione progressi
  supabase.min.js     Libreria Supabase (copia locale)

data/
  corsi-data.js       Offerta formativa ABA: corsi, colori, piani di studio, card della home
  {materia}-data.js   Contenuti di studio (capitoli, sintesi, flashcard, quiz)
  glossary-data.js    Glossario Web Design (caricato da pages/ux-webdesign.html, vedi 5.4)

pages/{materia}.html  Guscio della pagina di studio (circa 25 righe, nessun markup di layout)
tools/check-data.js   Verifica di qualità (da eseguire dopo ogni modifica)
tools/supabase-user-state.sql  SQL della tabella user_state (da eseguire una volta nella dashboard Supabase)
assets/
  favicon.svg         Favicon: logo semplificato, inchiostro nero/bianco secondo il tema del browser
  logo.svg            Logo del sito (evidenziatore), inchiostro nero: README, anteprime, materiali esterni
  logo-white.svg      Lo stesso logo con inchiostro bianco, per fondi scuri (spot, social)
  media/              Output dello spot Remotion: hero-loop.webm/.mp4 + hero-poster.jpg (clip nella home),
                      studioabact-promo.mp4 (16:9) e studioabact-vertical.mp4 (9:16) per la finestra "Guarda lo spot",
                      studioabact-promo-poster.jpg, og-image.jpg (anteprima dei link, 1200x630)
  app-icon-180.png    Icona per la schermata home (apple-touch-icon); app-icon-512.png per site.webmanifest
  corsi/{CORSO}/anno-{N}/{materia}/images/    Immagini e schemi SVG delle sintesi
  corsi/{CORSO}/anno-{N}/{materia}/dispense/  PDF sorgente (ignorati da git, solo in locale)
```

Materie con contenuti (tutte del corso DAPL08):

| ID registro | Pagina | File dati | Prefisso ID capitoli | Anno |
|---|---|---|---|---|
| `storia-arte-1` | `pages/storia-arte-1.html` | `arte1-data.js` (`ARTE1_DATA`) | `arte1-` | 1 |
| `fotografia` | `pages/fotografia.html` | `fotografia-data.js` (`FOTOGRAFIA_DATA`) | `foto-` | 1 |
| `taw` | `pages/taw.html` | `taw-data.js` (`TAW_DATA`) | `taw-` | 1 |
| `interaction` | `pages/interaction.html` | `interaction-data.js` (`INTERACTION_DATA`) | `ixd-` | 1 |
| `storia-arte` | `pages/storia-arte.html` | `arte-data.js` (`ARTE_DATA`) | `arte-` | 2 |
| `archetipi` | `pages/archetipi.html` | `archetipi-data.js` (`ARCHETIPI_DATA`) | `archetipi-` | 2 |
| `ux-webdesign` | `pages/ux-webdesign.html` | `dispense`, `krug`, `stull`, `maeda` `-data.js` | `dispense-`, `krug-`, `stull-`, `maeda-` | 2 |

---

## 3. Come funziona una pagina di studio

Le pagine in `pages/` sono **gusci**: contengono solo `<head>` e la lista degli script. Tutta l'interfaccia viene generata da `js/layout.js`, quindi una modifica grafica o strutturale si fa **una volta sola** e vale per tutte le materie.

Ordine obbligatorio degli script nel `<body>`:

```html
<body class="theme-light" data-subject="{id-registro}" data-course="{CODICE_CORSO}">
  <script src="../js/theme-boot.js?v=AAAAMMGG"></script>
  <script src="../js/supabase.min.js"></script>
  <script src="../js/auth.js?v=AAAAMMGG"></script>
  <script src="../data/{materia}-data.js?v=AAAAMMGG"></script>   <!-- uno o più file dati -->
  <script src="../js/subjects.js?v=AAAAMMGG"></script>
  <script src="../js/layout.js?v=AAAAMMGG"></script>
  <script src="../js/core.js?v=AAAAMMGG"></script>
  <script src="../js/practice.js?v=AAAAMMGG"></script>
  <script src="../js/subject-app.js?v=AAAAMMGG"></script>
</body>
```

- `data-subject` è la chiave in `window.SUBJECTS` e **deve coincidere con il nome del file** della pagina (la home usa il nome del file per collegare la card al registro).
- `data-course` attiva i colori del corso (sezione 6).
- `?v=AAAAMMGG`: aggiornare la data su tutti i file modificati per forzare il refresh della cache di GitHub Pages.

Struttura generata da `layout.js` (uguale per tutte le materie):

1. **Header sticky**: tasto indietro `#btn-hub-nav` (porta a `corsi.html?view=materie&course={CORSO}&anno={ANNO}`), titolo `#brand-main-title`, badge `.brand-docente-badge` ("Docente: ..."), selettore moduli `.pdf-selector#pdf-selector-nav` con `.pdf-tab` (`.tab-indicator`, `.tab-title`, `.tab-progress-mini`), pillole `#pill-study` ("Studio") / `#pill-exam` ("Allenati"), tasto tema `#btn-theme-toggle`. Il pulsante Accedi viene aggiunto da `auth.js` dentro `.utility-btns`.
2. **Session bar** `#session-bar` (solo desktop): nome esteso del modulo `#active-pdf-name`, `#active-pdf-progress-text` e barra `#session-progress-fill`. Il docente è già nella testata: non ripeterlo.
3. **Sidebar** `#sidebar` con `#sidebar-stats-count`, `#sidebar-progress-fill`, `#chapter-list`, tasti `#btn-sidebar-collapse`, `#btn-sidebar-close`, e tasto esterno `#btn-sidebar-expand`.
4. **Studio** `#view-study`: due barre `.chapter-nav-bar` (`.chapter-nav-top` e `.chapter-nav-bottom`) con `.btn-prev-chap`, `.btn-toggle-complete`, `.btn-next-chap`; subtab `[data-subtab="summary|flashcards|quiz"]` e pannelli `#subtab-panel-summary|flashcards|quiz`.
   Nel pannello sintesi: lettore vocale, storia-ancora (se presente), sintesi, punti chiave, **domande da orale** (se presenti).
5. **Allenati** `#view-exam`: schede `.practice-tab[data-practice="test|review|oral|stats"]` e pannelli `#practice-panel-{nome}`.
   - Test a quiz (core.js): `#exam-setup-box`, `#exam-scope-select`, `.num-pills .num-btn`, `#btn-start-exam`, `#exam-active-box`, `#exam-progress-fill`, `#exam-result-box`.
   - Ripasso, Orale, Progressi (practice.js): contenuto generato in `#review-root`, `#oral-root`, `#stats-root`. Il tasto `#btn-oral-chapter` nella sintesi avvia l'orale sul capitolo aperto.
6. **Mobile**: `#mobile-bottom-bar` (Materie, Capitoli, Moduli), `#mobile-dispense-overlay`, `#sidebar-backdrop`. Sotto 860px il selettore moduli in alto è nascosto e si usa il tasto "Moduli" (gli ID restano `*-dispense` per compatibilità).

---

## 4. Formato dei file dati

Ogni file espone una variabile globale: un array di capitoli (`window.ARTE_DATA = [...]`) oppure un oggetto con `chapters` (`window.TAW_DATA = { ..., chapters: [...] }`). Entrambi sono supportati.

```javascript
{
  id: "foto-c12",                 // univoco, con il prefisso della materia
  number: 12,                     // numero mostrato nell'indice
  module: "foto-autori",          // deve coincidere con modules[].module nel registro (se usato)
  partNum: 3, partTitle: "...",   // opzionali: intestazioni di gruppo nella sidebar
  title: "...",
  subtitle: "...",
  readTime: "12 min",
  summary: "Markdown...",         // sintesi (vedi regole sotto)
  keyPoints: ["...", "..."],      // 4-8 punti chiave d'esame
  flashcards: [{ question: "...", answer: "..." }],
  quiz: [{ question: "...", options: ["", "", "", ""], correctIndex: 2, explanation: "..." }],
  examQuiz: [ ... ],              // opzionale: se presente, il simulatore usa questi invece di quiz
  openQuestions: [                // opzionale: "Domande da orale"
    "Testo della domanda",                              // solo domanda
    { question: "...", modelAnswer: "Markdown..." }     // domanda con traccia di risposta
  ],
  anchorTitle: "...", anchorText: "..."  // opzionali: storia-ancora mnemonica
}
```

Il campo della risposta corretta si chiama **sempre** `correctIndex` (il vecchio `correct` è supportato solo per compatibilità e non va più usato).

Markdown supportato da `core.js`: `##`, `###`, `####`, `**grassetto**`, `*corsivo*`, elenchi `-` e `1.`, citazioni `>`, tabelle `| a | b |`, separatore `---`, codice, immagini `![didascalia](assets/corsi/...)`. Le immagini si scrivono con percorso dalla radice del sito (`assets/...`): il motore aggiunge `../` nelle pagine.

### 4.1 Regole per le sintesi (livello universitario)

- Le sintesi sono il materiale principale di studio: devono essere **complete rispetto alla dispensa**, non un riassunto di copertina. Obiettivo: **almeno 700-1000 parole per capitolo** (sotto 500 il validatore segnala un avviso).
- Ogni capitolo deve coprire: contesto storico/teorico, definizioni precise, autori e opere con **date**, concetti chiave e il loro rapporto con gli altri capitoli, esempi.
- Struttura: sezioni `###`, paragrafi brevi, elenchi solo dove servono, tabelle per confronti, citazioni per le definizioni degli autori.
- Tutto deve essere verificabile nella dispensa PDF in `assets/corsi/.../dispense/`. Non inventare date, nomi, citazioni o opere. Se un'informazione non è nella fonte e non è certa, non inserirla.
- Se la fonte è breve (un libro sintetico come Krug o Maeda), la sintesi può restare sotto le 500 parole: meglio breve e fedele che allungata con contenuti inventati. L'avviso del validatore in quel caso è accettabile.
- Se la dispensa contiene un errore evidente, non correggerlo in silenzio: riportare la versione della dispensa e segnalare la discrepanza in una nota (es. "Nota sulla fonte: ...").
- Alcune dispense (Storia dell'Arte 1: volumi anni cinquanta, sessanta, settanta e Man Ray) sono scansioni senza testo: per verificarle serve l'OCR. Fotografia non ha ancora le dispense dei moduli Tecnica e Maestri nella cartella.
- Le storie-ancora e le analogie sono ammesse come aiuto mnemonico, mai al posto del contenuto.

### 4.2 Regole per i quiz (devono far ragionare)

Ogni capitolo ha **almeno 5 quiz** a 4 opzioni (se se ne aggiungono, aggiornare `stats.quiz` in `corsi-data.js`). Regole obbligatorie:

1. **Distrattori plausibili**: le opzioni sbagliate devono essere errori che uno studente preparato a metà potrebbe commettere. Usare concetti, autori, date e termini **dello stesso corso** (spesso di un capitolo vicino), mai opzioni assurde o comiche ("cambia il gruppo sanguigno", "cancella la cronologia").
2. **Lunghezza e struttura omogenee**: tutte e 4 le opzioni con lunghezza simile (la corretta non deve superare la più lunga delle altre di oltre il 30%), stessa forma grammaticale, stesso livello di dettaglio. La risposta corretta non deve essere l'unica "completa" o l'unica con termini tecnici.
3. **Posizione**: il motore mescola le opzioni in visualizzazione, ma nel file `correctIndex` va comunque variato (0-3) e non sempre 0.
4. **Niente indizi linguistici**: evitare che la domanda ripeta parole presenti solo nella risposta giusta; evitare "sempre", "mai", "unicamente", "esclusivamente" solo nei distrattori.
5. **Varietà cognitiva** nei 5 quiz del capitolo: almeno 1 di definizione, 1 di attribuzione (autore/opera/data), 2 di comprensione o applicazione (caso pratico, confronto tra due concetti, causa-effetto), 1 di collegamento con un altro capitolo.
6. **Spiegazione**: dice perché la risposta è corretta **e** perché il distrattore più insidioso è sbagliato. Non deve **mai** citare la posizione delle opzioni ("la prima", "la risposta B"): il motore le mescola.
7. Evitare domande "Quale di queste NON..." se non strettamente utili, e mai opzioni "Tutte le precedenti" / "Nessuna delle precedenti".

Le **flashcard** (5 per capitolo) chiedono di richiamare un concetto, non di riconoscerlo: risposta in 1-3 frasi.
Le **domande da orale** (2-4 per capitolo) imitano l'esame orale dell'Accademia: "Illustrate...", "Confrontate...", con una `modelAnswer` di 80-150 parole quando possibile.

---

## 5. Contratti tecnici da non rompere

### 5.1 Lettore vocale (TTS) — ID e classi tassativi
- Contenitore `#summary-audio-bar.summary-audio-bar`
- Play/Pausa `#btn-audio-listen.btn-audio-player` con `#audio-icon-play`, `#audio-icon-pause`, `#audio-btn-label` ("Ascolta Sintesi")
- Stop `#btn-audio-stop.btn-audio-stop` (inizialmente `display: none`)
- Velocità `#audio-speed-pills.audio-speed-pills` con `.speed-pill` `data-speed="1"` e `data-speed="1.25"`
- Equalizzatore `#audio-visualizer.audio-visualizer` con 3 `.visualizer-bar`
- Stato `#audio-status-label.audio-status-label` ("Lettore vocale pronto")
- `speakNextChunk()` va chiamato in modo **sincrono** dentro il click (requisito di iOS Safari e Android).

### 5.2 Salvataggio e sincronizzazione
- `localStorage['ux_web_study_state_v1']` (nome storico, **non cambiarlo**: contiene i progressi degli studenti): `completed`, `quizAnswers`, `flashcardStatus` (formato precedente, ancora letto), `srs` (ripasso: `{ [cardId]: { box, due, reviews } }`), `activity` (azioni per giorno), `examHistory`, `oralLog`, `positions` (posizione di lettura per materia), `lastSubject`, `activeView`, `theme`.
- ID derivati (non cambiarli, sono le chiavi dei progressi): flashcard `{capitolo}-fc-{indice}`, quiz `{capitolo}-quiz-{indice}`, domande da orale `{capitolo}-oq-{indice}`. Aggiungere elementi **in coda** agli array, mai in mezzo.
- `localStorage['aba_studio_theme']`: tema globale (`light` / `dark`). `localStorage['aba_tts_speed']`: velocità del lettore.
- Le risposte ai quiz sono salvate con l'indice **originale** dell'opzione: il mescolamento in visualizzazione non le invalida.
- Supabase (`js/auth.js`) usa due tabelle:
  - `user_progress` (`user_id`, `subject`, `chapter_id`, `completed`): i capitoli completati, con Realtime. Il campo `subject` vale `arte` per gli ID `arte-*` e `ux` per tutti gli altri: non cambiarlo, altrimenti l'upsert su `user_id,subject,chapter_id` crea righe duplicate.
  - `user_state` (`user_id` chiave primaria, `data` jsonb, `updated_at`, RLS "solo il proprietario"): il resto dei progressi, cioè `srs`, `quizAnswers`, `activity`, `examHistory`, `oralLog`, `lastSubject` (elenco in `SYNCED_STATE_KEYS`). SQL di creazione in `tools/supabase-user-state.sql`.
- All'accesso e quando la pagina torna in primo piano lo stato remoto viene fuso con quello locale da `mergeStudyState()` (nessun dato si perde): `srs` vince la scheda con più `reviews`, a parità la `due` più lontana; `quizAnswers` e `oralLog` unione delle chiavi; `activity` massimo per giorno; `examHistory` unione deduplicata, ultime 30; `lastSubject` vince il locale. Ogni salvataggio invia lo stato con un debounce di 4 secondi, sempre fuso con il remoto prima dell'upsert. Se la tabella `user_state` non esiste il sito continua a sincronizzare solo i capitoli.
- Se si aggiunge un nuovo campo ai progressi, aggiungerlo a `SYNCED_STATE_KEYS` e definirne la regola di fusione in `mergeStudyState()`.

### 5.3 Accesso
- Tutti i contenuti e tutte le funzioni sono liberi, senza registrazione. L'accesso è facoltativo e serve solo a sincronizzare i progressi tra dispositivi.
- Non reintrodurre blocchi lato interfaccia: i dati sono comunque pubblici nei file `data/`.

### 5.4 Glossario
- Se una pagina carica un file che definisce `window.GLOSSARY_DATA` (`[{ term, source, def }]`), `core.js` trasforma la prima occorrenza di ogni termine nella sintesi in un pulsante `.glossary-term` con la definizione. Oggi è attivo solo in Web Design (`data/glossary-data.js`).
- Chiave del termine: il testo prima della parentesi; un alias tra parentesi vale solo se ha almeno due parole e nessuna cifra. I termini di una sola parola valgono solo con la maiuscola.

### 5.5 Animazioni
- Solo CSS, brevi (150-400 ms), su opacità e trasformazioni: classi `.anim-enter`, `.anim-pop`, `.just-answered` e i keyframe `fadeUp`, `popIn`, `shakeX`, `slideDown` in `styles.css`.
- Rispettare sempre `prefers-reduced-motion` (già gestito globalmente). Niente librerie di animazione.

### 5.6 Schemi SVG e lightbox
- Gli SVG nelle sintesi hanno sempre dimensioni fisse e `viewBox` (es. `width="1000" height="600" viewBox="0 0 1000 600"`), mai `width="100%"`.
- I testi negli SVG non si sovrappongono mai tra loro né ai tracciati.
- La lightbox `.artwork-lightbox-overlay` apre l'immagine fino a `min(1200px, 94vw)`; il tasto `.artwork-lightbox-close` è `position: fixed; top: 20px; right: 24px; z-index: 10002` (mai in negativo rispetto all'immagine).

---

## 6. Colori dei corsi di laurea

Fonte unica: `ABA_DATA.COURSE_COLORS` in `data/corsi-data.js` (home e card). Nelle pagine di studio i colori si applicano con `body[data-course]` in `styles.css`: quando un nuovo corso riceve contenuti, aggiungere lì il suo blocco (accento chiaro più scuro per il contrasto, accento pieno in tema scuro).

| Codice | Corso | Colore |
|---|---|---|
| DAPL01 / DASL01 | Pittura | `#4365a5` |
| DASL01-PLC | Pittura e linguaggi del contemporaneo | `#538ac3` |
| DAPL02 / DASL02 | Scultura | `#c6ac8b` |
| DAPL03 / DASL03 | Decorazione | `#3f8759` |
| DAPL04 / DASL04 | Grafica, illustrazione (e fumetto) | `#645085` |
| DAPL05 / DASL05 | Scenografia | `#94a9bc` |
| DAPL06-DCV / DASL06-DE | Design della comunicazione visiva / per l'editoria | `#d13528` |
| DAPL06-FD / DASL06-FD | Fashion design | `#d74f75` |
| DASL06-PID | Product e interior design | `#4ea9aa` |
| **DAPL08 / DASL08** | **Nuove Tecnologie dell'Arte / Arti e Tecnologie Digitali** | **`#feb940`** |
| DAPL09 / DASL09 | Patrimonio artistico contemporaneo / Didattica dell'arte | `#731f2e` |
| DAPL11-F / DASL11-F | Fotografia | `#51535f` |
| DAPL11-C / DASL11-C | Cinema | `#d15434` |

DAPL08 nelle pagine di studio (già in `styles.css`):

```css
body[data-course="DAPL08"]            { --course-accent: #feb940; --accent-primary: #d97706; --accent-primary-light: #fef3c7; }
body.theme-dark[data-course="DAPL08"] { --accent-primary: #feb940; --accent-primary-light: rgba(254, 185, 64, 0.15); }
```

Non colorare mai di blu una pagina DAPL08. Il blu `#2563eb` è solo l'accento generico della home.

Altri token (`styles.css`): sfondi `--bg-main`, `--bg-surface`, `--bg-sidebar`; testo `--text-main`, `--text-muted`; stati `--accent-success`, `--accent-warning`, `--accent-danger`. Font: Inter (Google Fonts) con fallback di sistema. Tema scuro neutro (`#141414`), senza viraggi blu.

---

## 7. Icone

- Solo SVG inline in stile "line" (viewBox 24, `stroke-width` 2, `stroke-linecap="round"`).
- Icone delle materie (campo `icon` in `corsi-data.js`, dizionario `ICONS` in `corsi.html`), esclusivamente:
  `palette` (storia dell'arte), `camera` (fotografia), `video` (audiovisivi, cinema, regia), `layout` (interaction, grafica, interfacce), `code` (informatica, web, programmazione), `book` (teoria, sociologia, archetipi), `cpu` (computer graphic, 2D/3D, tecnologie digitali).
- Icone della pagina di studio: oggetto `I` in `js/layout.js`. Icone generate dal motore (lucchetto, spunte, stato capitoli): `ICONS` in `js/core.js`. Non duplicarle altrove.

---

### 7.0 Video e anteprime

- Lo spot si rigenera nel progetto Remotion (fuori da questo repository) e gli output si copiano in `assets/media/` **con gli stessi nomi**: nessun file HTML va modificato.
- Nella home la clip `hero-loop` parte da sola senza audio (ferma con `prefers-reduced-motion`); lo spot completo si scarica solo quando si apre la finestra, in versione verticale sugli schermi in verticale.
- Ogni pagina ha i meta Open Graph con URL assoluti su `https://diegomeli6.github.io/StudioAbact/` (immagine `assets/media/og-image.jpg`), l'icona `apple-touch-icon` e `site.webmanifest`. Una pagina nuova va creata copiando questi meta da un guscio esistente.

### 7.1 Logo

- Il logo è l'evidenziatore: pittogramma a stella disegnato a mano, tocco accademico, passata gialla `#FEB940` (lo stesso tono dell'arancio DAPL08). Non usare più il pittogramma o il logotipo ufficiale dell'Accademia: il sito non è un canale ufficiale.
- Nel sito è **inline** (`SITE_LOGO` in `js/layout.js`, testata e piè di pagina di `index.html` e `corsi.html`), con classe `.site-logo`: l'inchiostro è `currentColor` e si adatta al tema, il riempimento del tocco usa `--logo-paper` (colore di sfondo).
- La versione inline ha i tratti ingrossati per restare leggibile a 36-64 px; la favicon è una versione semplificata (senza i raggi interni). I file di partenza si rigenerano in proporzione da `assets/logo.svg`.

## 8. Aggiungere una materia

1. **Dati**: creare `data/{materia}-data.js` dalla dispensa PDF (in `assets/corsi/{CORSO}/anno-{N}/{materia}/dispense/`), rispettando la sezione 4. ID con prefisso nuovo e univoco.
2. **Immagini**: in `assets/corsi/{CORSO}/anno-{N}/{materia}/images/` (regole della sezione 1.3 e 5.6).
3. **Registro**: aggiungere la voce in `js/subjects.js` (titolo, docente, `course`, `anno`, `examLabel`, `idPrefixes`, `modules`).
4. **Pagina**: copiare un guscio esistente in `pages/{id-registro}.html`, cambiare `<title>`, `<meta name="description">`, `data-subject`, `data-course` e gli script dei dati.
5. **Home**: nella materia corrispondente di `data/corsi-data.js` (dentro `PIANI_STUDIO[CORSO][anno].materie`) impostare `isClickable: true`, `hasContent: true`, `page: "pages/{id-registro}.html"`, `stats: { capitoli, quiz, fonti }` e una `desc` di circa 140-150 caratteri.
6. **Colori**: se il corso non ha ancora un blocco `body[data-course]` in `styles.css`, aggiungerlo.
7. **Verifica**: `node tools/check-data.js` (0 errori), poi aprire la home, la pagina dei corsi e la pagina della materia in desktop e a 390px di larghezza: testata, lettore vocale, flashcard, quiz, le quattro schede di "Allenati".

Materie laboratoriali senza dispense (es. Estetica delle Interfacce): `isClickable: false`, `hasContent: false` e in `desc` il testo `<span class="materia-notice-highlight">Questa materia non prevede lo studio di dispense orali.</span>`.

---

## 9. Verifica di qualità

```bash
node tools/check-data.js
```

- **ERRORI** (bloccanti): conteggi diversi da `stats` in `corsi-data.js`, ID duplicati o senza prefisso, quiz senza 4 opzioni o con `correctIndex` non valido, spiegazioni mancanti, immagini mancanti, emoji in qualunque file.
- **AVVISI** (qualità): risposta corretta nettamente più lunga delle altre, sintesi sotto le 500 parole. Quando si lavora su una materia, l'obiettivo è portare a zero gli avvisi di quella materia.

Per provare il sito in locale: `python3 -m http.server 8765` nella cartella del progetto, poi `http://localhost:8765`.
