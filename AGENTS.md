# REGOLE ASSOLUTE DEL PROGETTO

## 1. DIVIETO ASSOLUTO DI EMOJI
### NON INSERIRE MAI EMOJI IN NESSUN POSTO, NÉ NEL CODICE, NÉ NELL'INTERFACCIA, NÉ NEI TESTI.

1. È SEVERAMENTE VIETATO USARE QUALSIASI EMOJI UNICODE (faccine, nuvole, simboli, icone grafiche unicode come faccine, dischetti, razzi, libri, ecc.).
2. NESSUNA EMOJI nei messaggi toast, nelle notifiche, nei titoli, nei bottoni, nei placeholder, nei commenti di codice o nelle descrizioni.
3. Se serve un'icona, usare ESCLUSIVAMENTE icone vettoriali SVG inline (`<svg>`).
4. Se serve enfasi grafica, usare stili CSS (colori di accento, badge testuali, bordi, contrasti tipografici).

---

## 2. PARITÀ GRAFICA E STRUTTURA DELLE PAGINE DI STUDIO (`pages/*.html`)
### TUTTE LE PAGINE DI STUDIO DEVONO RISPETTARE LO SCHEMA STANDARD MASTER (es. `storia-arte.html`)

Ogni pagina materia (`storia-arte.html`, `storia-arte-1.html`, `fotografia.html`, `archetipi.html`, `interaction.html`, `taw.html`, `ux-webdesign.html`) deve contenere tutti e i soli elementi dell'architettura condivisa:

1. **Sticky Header Unificato**:
   - Tasto indietro `#btn-hub-nav.btn-back-nav` con SVG freccia e attributo esatto `data-href="../index.html?view=materie&course={CORSO}&anno={ANNO}"`.
   - Titolo brand `#brand-main-title` e badge docente `.brand-docente-badge` (`Docente: Prof...`).
   - Selettore moduli `.pdf-selector#pdf-selector-nav` con bottoni `.pdf-tab` contenenti `.tab-indicator`, `.tab-title` e `.tab-progress-mini`.
   - Switch modalità studio/test `.view-mode-pills#header-view-pills`: `#pill-study` (Studio) e `#pill-exam` (Test).
   - Tasto tema `#btn-theme-toggle.icon-btn`.
2. **Session Bar**:
   - `#session-bar`: `.session-dot`, `#active-pdf-name`, divisori, `.session-docente` con prefisso obbligatorio `Docente: `, `#active-pdf-progress-text`.
3. **Sidebar e Twitch Expander**:
   - Sidebar `#sidebar` con titolo, `#sidebar-stats-count`, tasto collasso Twitch `#btn-sidebar-collapse.sidebar-toggle-twitch` e chiusura mobile `#btn-sidebar-close`.
   - Barra progresso `#sidebar-progress-fill` e lista capitoli `#chapter-list`.
   - Tasto espansione Twitch laterale `#btn-sidebar-expand.sidebar-expand-twitch`.
4. **Navigazione Capitoli e Subtabs**:
   - Doppia barra di navigazione `.chapter-nav-bar` (sia `.chapter-nav-top` che `.chapter-nav-bottom`): pulsante `.btn-prev-chap`, pulsante `.btn-complete.btn-toggle-complete`, pulsante `.btn-next-chap`.
   - Subtabs `.chapter-subtabs`: 3 tab standard:
     - `[data-subtab="summary"]`: icona documento SVG + testo `Sintesi & Concetti` / `Sintesi`.
     - `[data-subtab="flashcards"]`: icona flashcard SVG + testo `Flashcard (<span id="count-fc">0</span>)`.
     - `[data-subtab="quiz"]`: icona quiz SVG + testo `Quiz con Spiegazione` / `Quiz`.
   - Tre pannelli corrispondenti: `#subtab-panel-summary`, `#subtab-panel-flashcards`, `#subtab-panel-quiz`.
5. **Simulatore d'Esame (`#view-exam`)**:
   - Setup completo con `#exam-setup-box`, select `#exam-scope-select`, pillole numeriche `.num-pills .num-btn`, `#btn-start-exam`, `#exam-active-box`, `#exam-result-box`.
6. **Mobile Bottom Bar & Overlay**:
   - `#mobile-bottom-bar`, `#mobile-dispense-overlay`, `#sidebar-backdrop`.

---

## 3. CONTRATTO DEL LETTORE VOCALE SINTESI (TTS)
### GLI ID E LE CLASSI DEL LETTORE VOCALE SONO TASSATIVI PER IL FUNZIONAMENTO IN `js/core.js`

Non rinominare MAI gli ID del lettore vocale (vietati `#btn-audio-play`, `.audio-play-btn`, ecc.). La barra della sintesi deve avere SEMPRE:
- Contenitore: `#summary-audio-bar.summary-audio-bar`.
- Tasto Play/Pausa: `#btn-audio-listen.btn-audio-player` contenente `#audio-icon-play`, `#audio-icon-pause` e `#audio-btn-label` (*Ascolta Sintesi*).
- Tasto Stop: `#btn-audio-stop.btn-audio-stop` (con `style="display: none;"` iniziale).
- Velocità: `#audio-speed-pills.audio-speed-pills` con bottoni `.speed-pill` (`data-speed="1"` e `data-speed="1.25"`).
- Equalizzatore: `#audio-visualizer.audio-visualizer` (con 3 barre `.visualizer-bar`).
- Stato: `#audio-status-label.audio-status-label` (*Lettore vocale pronto*).

---

## 4. REGOLE SULLE IMMAGINI E OPERE D'ARTE
### DIVIETO DI AI PER LE OPERE D'ARTE — SOLO FOTO AUTENTICHE MUSEALI / ARCHIVISTICHE

1. **Opere d'Arte Storiche o Contemporanee**:
   - Per tutte le opere d'arte (quadri, sculture, fotografie d'autore di Cattelan, Hirst, Banksy, Magritte, Man Ray, Warhol, Bresson, Giacomelli, ecc.) è SEVERAMENTE VIETATO usare immagini generate da intelligenza artificiale.
   - Usare ESCLUSIVAMENTE immagini fotografiche autentiche reperite online da musei, archivi o Wikimedia Commons.
2. **Immagini Generate (AI / Nano Banana)**:
   - Consentite ESCLUSIVAMENTE per schemi concettuali, infografiche tecniche o diagrammi astratti.
   - **Meno scritte possibili**: gli schemi generati NON devono contenere paragrafi o descrizioni fitte (che l'AI allucina o sovrappone), ma soltanto i **nomi principali essenziali** e una grafica pulita, distanziata e leggibile.

---

## 5. SCHEMI VETTORIALI SVG E MODALE LIGHTBOX
### DIMENSIONI FISSE PER GLI SVG E TASTO CHIUSURA FISSO NON TAGLIATO

1. **Dimensioni Schemi SVG**:
   - Negli schemi SVG inseriti nelle dispense, dichiarare sempre dimensioni fisiche fisse e viewBox (es. `width="1000" height="600" viewBox="0 0 1000 600"`), e MAI `width="100%" height="100%"`. Se si usano percentuali, i browser le collassano a 300x150px aprendole nella modale.
   - I testi all'interno degli SVG non devono MAI sovrapporsi tra loro né sovrapporsi ai tracciati geometrici.
2. **Modale Lightbox Ingrandimento**:
   - La modale (`.artwork-lightbox-overlay`) deve aprirsi ad alta risoluzione (`max-width: min(1200px, 94vw)`), occupando lo spazio adeguato per una visione chiara e dettagliata.
   - Il tasto di chiusura X (`.artwork-lightbox-close`) deve essere a posizione fissa nel viewport in alto a destra (`position: fixed; top: 20px; right: 24px; z-index: 10002;`). NON posizionarlo in negativo rispetto all'immagine (`top: -46px`), altrimenti con immagini grandi esce dallo schermo e viene tagliato a metà.

---

## 6. COLORI E TEMA DEI CORSI (PALETTE DAPL08)
### OGNI MATERIA DEVE AVERE IL COLORE DEL PROPRIO CORSO DI LAUREA

1. Per tutte le materie del corso **DAPL08 (Nuove Tecnologie dell'Arte)**, i colori ufficiali nel `<head>` devono essere:
   ```css
   :root {
     --course-accent: #feb940;
     --accent-primary: #d97706;
     --accent-primary-light: #fef3c7;
   }
   body.theme-dark {
     --accent-primary: #feb940;
     --accent-primary-light: rgba(254, 185, 64, 0.15);
   }
   ```
2. Non colorare arbitrariamente di blu le pagine di DAPL08. I colori dei corsi sono centralizzati in `data/corsi-data.js` (`ABA.COURSE_COLORS`).

---

## 7. ICONE DELLE MATERIE E NAVIGAZIONE INDICE
1. Tutte le icone associate alle materie in `data/corsi-data.js` e renderizzate in `index.html` devono attingere ESCLUSIVAMENTE al dizionario centrale `ICONS`:
   - `palette` (Storia dell'arte)
   - `camera` (Fotografia)
   - `video` (Audiovisivi, Cinema, Regia)
   - `layout` (Interaction Design, Grafica, Interfacce)
   - `code` (Informatica, Web Design, Programmazione)
   - `book` (Archetipi, Sociologia, Teoria)
   - `cpu` (Computer Graphic, 2D/3D, Tecnologie digitali)
2. Il calcolo del progresso in `index.html` (`getSubjectProgress`) deve sempre riflettere l'esatto numero totale di capitoli presenti nel rispettivo file dati.
