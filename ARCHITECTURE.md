# ARCHITECTURE.md — Guida Tecnica e Operativa per Chat AI

> [!IMPORTANT]
> ### REGOLA FONDAMENTALE DEL PROGETTO
> **Dopo qualsiasi modifica importante, aggiunta di dispense, nuove materie o refactoring, questo file deve essere tassativamente mantenuto aggiornato.**
> Tutte le istruzioni e le convenzioni operative risiedono in questo documento. Il file `README.md` e riservato alla sola descrizione pubblica per gli studenti e GitHub.
> 
> ### DIVIETO ASSOLUTO DI EMOJI
> **NON INSERIRE MAI EMOJI IN NESSUN POSTO, NE NEL CODICE, NE NELL'INTERFACCIA, NE NEI TESTI O NEI FILE MARKDOWN.**
> E severamente vietato qualsiasi carattere emoji unicode (es. faccine, simboli grafici, razzi, nuvole, lampadine, libri grafici unicode). Usare unicamente icone vettoriali SVG inline (`<svg>`) con `fill="currentColor"` o `stroke="currentColor"` oppure stili CSS.

---

## 1. Mappa e Struttura del Progetto

```
Studio/
|-- index.html              <-- Home: selezione Corso -> Anno -> Materia con card geometricamente identiche
|-- styles.css              <-- Design system unificato: token CSS, temi chiaro/scuro, layout desktop e mobile
|-- README.md               <-- Presentazione per gli studenti e documentazione pubblica GitHub
|-- ARCHITECTURE.md         <-- QUESTO FILE: Specifiche tecniche e procedura aggiunta materie
|-- AGENTS.md               <-- Regola assoluta del divieto emoji per agenti AI
|-- GEMINI.md               <-- Regola assoluta del divieto emoji per modelli Gemini
|-- GUIDA_AUTENTICAZIONE.md <-- Documentazione integrazione Supabase Auth e Freemium
|
|-- js/
|   |-- core.js             <-- Modulo condiviso StudyCore: stato globale, persistenza, navigazione capitoli,
|   |                           TTS audio reader sincrono per iOS/Android, markdown parser, quiz, flashcard
|   |-- auth.js             <-- Client Supabase: gestione sessione, modale login/registrazione, sync cloud
|   |-- app-ux.js           <-- Logica specifica Web Design (dispense, calcolo pool esame, stats)
|   `-- app-arte.js         <-- Logica specifica Storia dell'Arte Contemporanea 2
|
|-- pages/
|   |-- ux-webdesign.html   <-- Pagina studio Web Design (template standard di riferimento)
|   `-- storia-arte.html    <-- Pagina studio Storia dell'Arte Contemporanea 2
|
|-- data/
|   |-- dispense-data.js    <-- Dispense Professore Web Design (14 capitoli)
|   |-- krug-data.js        <-- Steve Krug - Don't Make Me Think (14 capitoli)
|   |-- stull-data.js       <-- Edward Stull - UX Design con storie-ancora (43 capitoli)
|   |-- maeda-data.js       <-- John Maeda - Le leggi della semplicita (13 capitoli)
|   |-- glossary-data.js    <-- Glossario termini tecnici UX
|   `-- arte-data.js        <-- Storia dell'Arte: Anni '80, Anni '90, Duemila, Monografie
|
`-- assets/
    |-- favicon.svg         <-- Favicon SVG adattiva al tema del browser (nero su chiaro, bianco su scuro)
    |-- logo.svg            <-- Logo orizzontale ABA Catania
    |-- logo-white.svg      <-- Logo orizzontale ABA Catania in bianco per footer
    |-- logo-icon.svg       <-- Pittogramma stella vettoriale isolato
    `-- arte/               <-- Immagini delle opere d'arte citate nei moduli di studio
```

---

## 2. Standard Grafici e Componenti UI Consolidati

Tutte le pagine di studio e la home devono rispettare rigorosamente gli standard definiti:

### 2.1. Favicon SVG Dinamica (`assets/favicon.svg`)
- Mostra esclusivamente il **pittogramma stella geometrico** dell'Accademia (senza loghi estesi o scritte).
- Include la regola nativa `@media (prefers-color-scheme: dark)`:
  - Browser con tema chiaro: riempimento nero (`fill: #000000;`).
  - Browser con tema scuro: riempimento bianco (`fill: #ffffff;`).

### 2.2. Barra Superiore di Navigazione (Navbar Stile Twitch)
- **Rimosso il burger menu**: la navigazione laterale e gestita direttamente dalla sidebar.
- **Pulsante Indietro (`#btn-hub-nav`)**: posizionato a sinistra su desktop/tablet, rimanda a `index.html?view=materie&course={ID}&anno={NUM}`. Su smartphone e nascosto (`display: none !important;`) poiche sostituito dal tasto "Materie" nella barra inferiore.
- **Titolo Materia e Docente (`.header-brand`)**: visualizza il titolo ufficiale del corso e il badge con il nome del docente colorato con l'accento della materia.
- **Selettore Documenti (`.pdf-selector`)**: tab a scorrimento orizzontale senza alcuna maschera sfumata trasparente (`mask-image: none !important;`).
- **Pannello Azioni a Destra (`.header-actions`)**:
  - Pulsanti segmentati **Studio** e **Test** (`.view-mode-pills`).
  - Tasto cambio tema chiaro/scuro (`#btn-theme-toggle`).
  - Pulsante **Accedi** (`#btn-auth-user`) posizionato all'estrema destra con spaziatura dedicata (`gap: 14px`). In tema scuro, il testo del pulsante e sempre bianco (`#ffffff !important`).

### 2.3. Sidebar Collassabile Stile Twitch
- **Pulsante di Chiusura (`#btn-sidebar-collapse`)**: posizionato nell'intestazione della sidebar (`.sidebar-header`) a fianco del contatore capitoli, con icona SVG a freccia verso sinistra con barra di battuta (`<-|`).
- **Aletta di Espansione (`#btn-sidebar-expand`)**: quando la sidebar ha la classe `.collapsed`, un'aletta dedicata con icona (`|->`) appare agganciata al bordo sinistro dello schermo (`position: fixed; left: 0; top: 96px; z-index: 35;`) per riaprire l'indice al click.

### 2.4. Layout Responsive per Smartphone (< 860px)
- **Testata su 3 Righe Distinte**:
  1. **Riga 1 (`.header-brand`)**: occupa il 100% della larghezza. Il titolo della materia e visualizzato a dimensione confortevole (`18px`, `white-space: normal;`) con sotto il badge del docente, senza troncamenti ne sovrapposizioni.
  2. **Riga 2 (`.header-actions`)**: occupa il 100% della larghezza (`justify-content: space-between;`). I pulsanti Studio e Test si espandono a coprire la porzione sinistra (`flex: 1;`), mentre Tema e Accedi rimangono allineati a destra.
  3. **Riga 3 (`.pdf-selector`)**: barra delle dispense a scorrimento orizzontale a tutta larghezza, priva di gradienti.
- **Subtabs di Capitolo (Sintesi, Flashcard, Quiz)**:
  - Controllo segmentato a tutta larghezza con griglia a 3 colonne uguali (`grid-template-columns: repeat(3, 1fr);`).
  - Testi ottimizzati ("Sintesi", "Flashcard (N)", "Quiz") a 14px senza wrapping, icone nascoste su smartphone per massima leggibilita.
- **Barra Fissa Inferiore (`.mobile-bottom-nav`)**:
  - Pulsanti: Materie (torna alla home), Capitoli (apre il drawer laterale dell'indice), Indice PDF (apre il foglio modale dispense), Tema.

### 2.5. Lettore Vocale / Text-To-Speech (`#summary-audio-bar`)
- **Avvio Audio Sincrono su Mobile**: `speakNextChunk()` viene invocato in modo rigorosamente sincrono nel gestore dell'evento click per rispettare le policy di autoplay audio di iOS Safari e Android (evitando ritardi in `setTimeout` o attese asincrone).
- **Compatibilita Voci**: fallback progressivo da Google Italiano alle voci neurali di sistema e a qualsiasi voce italiana (es. Alice, Federica, Luca, Paola su iOS).
- **Ottimizzazione Mobile**: su smartphone, il blocco con la frase letta (`.audio-status-wrap`) e nascosto (`display: none !important;`). La barra audio mantiene altezza e larghezza costanti (nessun ballooning ne sfasamento di margini) e rimane sempre ancorata a inizio lettura con `position: sticky; top: 0; z-index: 85;`.
- **Desktop**: include pulsante Play/Pausa, Stop, selettori di velocita (1x e 1.25x) ed equalizzatore grafico con etichetta del testo in corso di lettura.

### 2.6. Spaziatura Footer nelle Pagine di Studio
- Per garantire respiro visivo nei capitoli lunghi, il container dei pulsanti di completamento (`.chapter-footer`) ha `margin-bottom: 64px;` e `padding-top: 24px;`.
- Il footer del sito (`.study-site-footer`) ha `margin-top: 64px;` su desktop e `margin-top: 48px;` su mobile.

### 2.7. Card Materie nella Home (`index.html`)
Tutte le schede delle materie devono essere rigorosamente identiche e speculari:
- **Titolo su Riga Singola**: `white-space: nowrap; overflow: hidden; text-overflow: ellipsis; height: 24px; font-size: clamp(15.5px, 1.35vw, 17.5px);`.
- **Badge Docente Allineati**: posizionati alla stessa identica quota verticale su tutte le card.
- **Descrizioni Bilanciate**: lunghezza contenuta e uniforme (~140-150 caratteri, esattamente 3 righe).
- **Footer e Statistiche Ancorate in Basso**: `.materia-card-footer` con `margin-top: auto; border-top: 1px solid var(--border-color); padding-top: 18px;`.
- **Statistiche Allineate**: elementi capitoli, quiz e fonti distribuiti con `justify-content: space-between;` senza andare a capo.
- **Altezza Totale Identica**: tutte le card condividono la medesima altezza complessiva.
- **Accento Cromatico del Corso**: tutte le materie appartenenti allo stesso corso condividono il medesimo colore d'accento (es. `#feb940` per Nuove Tecnologie dell'Arte).

### 2.8. Protezione Accesso Freemium
- Il Capitolo 1 di ogni dispensa/modulo e liberamente consultabile per tutti (inclusi i relativi quiz e flashcard).
- Dal Capitolo 2 in avanti, e per tutte le simulazioni d'esame (`#view-exam`), l'accesso e riservato agli utenti registrati: compare il banner freemium con pulsante che apre la modale di autenticazione Supabase.
- Al login/logout, la pagina si sblocca/aggiorna in tempo reale via evento custom `auth:change`.

---

## 3. PROCEDURA STANDARD: Come Aggiungere una Nuova Materia da PDF

Quando l'utente carica dei nuovi PDF e richiede di aggiungere una materia, l'assistente AI deve eseguire i seguenti 5 passaggi senza alterare gli stili globali esistenti:

### Passo 1: Estrazione e Creazione del File Dati (`data/{id-materia}-data.js`)
1. Analizzare il PDF ed estrarre il testo completo dei capitoli/moduli.
2. Creare il file `data/{id-materia}-data.js` esponendo una variabile globale `window.{NOME_VARIABILE}_DATA`.
3. Ogni oggetto capitolo deve contenere:
   - `id`: identificativo univoco (es. `fotografia-c1`, `storia-design-c2`).
   - `number`: numero progressivo del capitolo (intero).
   - `title`: titolo del capitolo o argomento (breve e conciso).
   - `subtitle`: eventuale sottotitolo esplicativo.
   - `readTime`: tempo stimato (es. `"8 min"`).
   - `module`: ID stringa del modulo di appartenenza (se il programma ha piu libri/dispense).
   - `summary`: testo della sintesi in **Markdown pulito** (sezioni con `###`, elenchi puntati, grassetti, tabelle, citazioni). **NESSUNA EMOJI**.
   - `keyPoints`: array di stringhe con i punti chiave per l'esame.
   - `flashcards`: array di 3-8 oggetti `{ question: "...", answer: "..." }`.
   - `quiz`: array di 3-8 quiz a scelta multipla con spiegazione:
     ```javascript
     {
       question: "Domanda concettuale chiara",
       options: ["Opzione corretta", "Distrattore 1", "Distrattore 2", "Distrattore 3"],
       correctIndex: 0,
       explanation: "Spiegazione didattica puntuale dell'argomento."
     }
     ```

### Passo 2: Creazione del File Logica Materia (`js/app-{id-materia}.js`)
Duplicare la struttura consolidata di `js/app-ux.js` o `js/app-arte.js`:
1. Definire `getCurrentPdfChapters()` per restituire i capitoli in base al modulo selezionato in `state.activePdf`.
2. Definire `getPdfDisplayName(key)` con le etichette formattate dei documenti (es. `"1. Dispense"`, `"2. Manuale Tecnico"`).
3. Definire `getExamPool(scope)` per aggregare i quiz nel simulatore d'esame generale o per modulo.
4. Definire `updateProgressIndicators()` per aggiornare i badge numerici delle tab.
5. Inizializzare `StudyCore.init({...})`.

### Passo 3: Creazione della Pagina HTML (`pages/{id-materia}.html`)
Duplicare `pages/ux-webdesign.html` (che costituisce il template standard perfetto):
1. Aggiornare `<title>` e `<meta name="description">`.
2. Nel blocco `.header-brand`, impostare:
   - `#btn-hub-nav` con link corretto al corso e anno (`index.html?view=materie&course={CODE}&anno={ANNO}`).
   - `#brand-main-title`: nome ufficiale esatto della materia.
   - `.brand-docente-badge`: nome del docente ufficiale.
3. Nella barra `<nav class="pdf-selector">`, configurare i pulsanti `.pdf-tab` per i moduli/libri d'esame.
4. Mantenere intatta tutta l'infrastruttura standard:
   - Navbar con pulsanti Twitch (`#btn-sidebar-collapse` e `#btn-sidebar-expand`).
   - Sezione comandi con `#header-view-pills` (Studio/Test), `#btn-theme-toggle` e container login Supabase.
   - Barra di sessione `#session-bar`.
   - Barra audio TTS `#summary-audio-bar`.
   - Subtabs a 3 colonne con testi compatti.
   - Drawer e barra inferiore mobile (`.mobile-bottom-nav`).
   - Modale di autenticazione e script di chiusura.
5. Nei tag `<script>` in fondo alla pagina, includere:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
   <script src="../js/auth.js"></script>
   <script src="../data/{id-materia}-data.js"></script>
   <script src="../js/core.js"></script>
   <script src="../js/app-{id-materia}.js"></script>
   ```

### Passo 4: Registrazione della Materia in `index.html`
Nell'array del corso corrispondente in `index.html` (es. `ANNI_NTA` o array del nuovo corso):
1. Inserire l'oggetto della materia:
   ```javascript
   { 
     id: '{id-materia}',
     name: '{Nome Ufficiale Materia}',
     code: '{Codice Ministeriale, es. ABPR 19}',
     credits: '{N} CFA',
     docente: '{Titolo e Nome Docente}',
     desc: 'Insegnamento ufficiale {Codice} ({N} CFA). {Descrizione bilanciata su ~140 caratteri con indicazione dei testi e modalita di studio}.',
     icon: '{chiave_icona_ICONS}',
     stats: { capitoli: {TOT_CAPITOLI}, quiz: {TOT_QUIZ}, fonti: {TOT_FONTI} },
     page: 'pages/{id-materia}.html'
   }
   ```
2. Assicurarsi che `desc` abbia lunghezza coerente (~140-150 caratteri) affinche la card risulti perfettamente speculare e allineata con le altre.

### Passo 5: Verifica di Conformita
1. Verificare l'assenza totale di emoji in ogni riga aggiunta.
2. Aprire la home e verificare che tutte le card siano alte uguali, con titoli su riga singola, badge docenti allineati e statistiche in basso.
3. Aprire la nuova pagina sia in visualizzazione desktop sia mobile (390px):
   - Verificare che la testata mobile sia su 3 righe ordinate.
   - Verificare che il tasto "Ascolta Sintesi" avvii la voce e che la barra rimanga sticky.
   - Verificare che i test e i capitoli dal 2 in poi mostrino il blocco freemium se non loggati.

---

## 4. Note sulle Tecnologie e Dipendenze

- **Vanilla JavaScript & CSS Moderno**: Nessun framework pesante (React, Vue, Vite, Next.js). Nessun build step a runtime. Il sito e immediatamente eseguibile aprendo i file HTML nel browser o tramite GitHub Pages.
- **Supabase JS**: Unica libreria esterna, caricata via CDN (`@supabase/supabase-js@2`), impiegata per l'autenticazione cloud degli studenti e il salvataggio remoto dei progressi.
- **Compatibilita Percorsi Relativi**: Tutti gli asset (`assets/`), fogli di stile (`styles.css`), script (`js/`) e dati (`data/`) utilizzano rigorosamente percorsi relativi (`./` o `../`) per funzionare sia su `file:///` locale sia su hosting remoto con sottocartella GitHub Pages.
