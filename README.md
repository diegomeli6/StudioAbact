# Studio ABA Catania — Piattaforma di Studio Interattiva

Piattaforma web client-side per lo studio accademico all'**Accademia di Belle Arti di Catania**.  
Nessun server, nessun account: tutto funziona direttamente nel browser con salvataggio automatico e persistente in `localStorage`.

---

## Funzionalità principali

### Studio guidato e contenuti didattici
- **Sintesi accademiche approfondite** per ogni capitolo, strutturate fedelmente sui testi d'esame.
- **Storie-àncora mnemoniche**: narrativa visiva che facilita la memorizzazione dei concetti complessi.
- **Punti chiave d'esame**: liste mirate di concetti imprescindibili per il colloquio d'esame.
- **Formattazione ricca**: tabelle di confronto, blocchi di codice con syntax highlighting, blockquote, gallerie opere d'arte.

### Lettore Vocale Intelligente (TTS)
- **Voce naturale Google Italiano**: sintesi vocale ad alta fedeltà integrata direttamente nella pagina.
- **Moltiplicatori di velocità**: selettore rapido a pillola (`1x`, `1.25x`) con aggiornamento dinamico immediato durante l'ascolto.
- **Player audio completo**: controlli di ascolto, pausa, stop, visualizzatore a onde sonore e indicazione del capitolo in riproduzione.
- **Chunking sequenziale**: suddivisione automatica del testo per garantire fluidità di lettura senza blocchi del browser.

### Flashcard interattive
- Domanda → Risposta (clic per girare con animazione 3D).
- Classificazione rapida dello stato: "Lo so bene" / "Da rivedere".
- Conteggio e percentuali di padronanza aggiornate in tempo reale.

### Quiz con feedback immediato
- Domande a scelta multipla con 4 alternative plausibili.
- Feedback visivo istantaneo con spiegazione didattica dettagliata e citazione del testo originale.
- Tracciamento delle risposte corrette ed errate per capitolo.

### Simulatore d'esame
- Generazione dinamica di prove d'esame con estrazione casuale dal pool delle domande.
- Rimescolamento delle opzioni per evitare risposte a memoria posizionale.
- Scelta dell'ambito: singolo testo/modulo oppure esame misto completo.
- Riepilogo finale con punteggio in trentesimi e revisione puntuale degli errori.

### Tema Scuro / Chiaro e Sincronizzazione Cross-Page
- Tema scuro su tonalità di nero profondo (`#0d0f12`) ad alto contrasto, per studiare a lungo senza affaticamento visivo.
- Preservazione dei colori istituzionali del corso (es. giallo `#feb940` per Nuove Tecnologie dell'Arte).
- **Sincronizzazione istantanea**: il cambio tema si propaga in tempo reale su tutte le schede e pagine aperte.

### Navigazione Intelligente e Privacy
- Passaggio fluido tra dispense con posizionamento automatico sul primo capitolo non completato.
- **100% Privacy**: nessun dato viene inviato a server esterni; tutti i progressi risiedono nel browser.
- Esportazione e importazione rapida di backup completi in formato JSON.

---

## Stack tecnologico

- **HTML5** semantico
- **CSS3 Vanilla** (design system responsive con custom properties, senza librerie esterne)
- **JavaScript ES6+** modulare (`StudyCore` condiviso tra le pagine di studio)
- **Web Speech API** per la sintesi vocale
- **Web Storage API** (`localStorage`) per la persistenza
- **Google Fonts** (famiglia tipografica Inter)

---

## Come avviare

Non richiede installazione di pacchetti o dipendenze:

1. Apri direttamente `index.html` con qualsiasi browser moderno (Chrome, Edge, Safari, Firefox).
2. Seleziona il tuo corso di laurea (es. *Nuove Tecnologie dell'Arte*).
3. Seleziona l'anno e accedi alla materia desiderata (*Web Design*, *Storia dell'Arte Contemporanea 2*, ecc.).

### Con server locale (opzionale)

```bash
# Con Python
python3 -m http.server 8080

# Con Node.js
npx serve .
```

---

## Struttura del repository

```
Studio/
├── index.html              ← Home e hub di navigazione Corsi → Anni → Materie
├── styles.css              ← Design system, componenti UI e variabili chiaro/scuro
├── README.md               ← Questo file (presentazione del progetto)
├── ARCHITECTURE.md         ← Architettura tecnica, standard e convenzioni di sviluppo
│
├── js/
│   ├── core.js             ← Modulo StudyCore: motore TTS, stato, rendering, quiz ed esame
│   ├── app-ux.js           ← Logica specifica per Web Design
│   └── app-arte.js         ← Logica specifica per Storia dell'Arte Contemporanea 2
│
├── pages/
│   ├── ux-webdesign.html   ← Materia: Web Design (ABPR 19)
│   └── storia-arte.html    ← Materia: Storia dell'Arte Contemporanea 2 (ABST 47)
│
├── data/                   ← Dataset capitoli, sintesi, flashcard e quiz
│   ├── dispense-data.js
│   ├── krug-data.js
│   ├── stull-data.js
│   ├── maeda-data.js
│   ├── glossary-data.js
│   └── arte-data.js
│
└── assets/                 ← Loghi SVG, icone e immagini opere d'arte
    ├── logo.svg
    ├── logo-icon.svg
    └── arte/
```
