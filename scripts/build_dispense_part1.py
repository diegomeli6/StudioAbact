# build_full_dispense.py
# Generatore di data/dispense-data.js con 14 capitoli approfonditi e almeno 5 quiz complessi e bilanciati per capitolo
import json

chapters = [
    # 1. Introduzione
    {
        "id": "dispense-c1",
        "number": 1,
        "title": "Introduzione",
        "subtitle": "La trasmissione dell'informazione, la retorica visiva e il ruolo del designer",
        "readTime": "8 min",
        "summary": """### La trasmissione dell'informazione e il modello comunicativo
In ogni processo di comunicazione intervengono tre elementi imprescindibili:
1. **Mittente (Emittente)**: l'entità (azienda, istituzione, autore) che origina l'informazione e persegue un obiettivo comunicativo o funzionale.
2. **Messaggio**: il contenuto semantico, cognitivo e funzionale che deve essere trasmesso.
3. **Destinatario (Ricevente / Utente)**: il fruitore a cui il messaggio è destinato, caratterizzato da specifici modelli mentali, limiti cognitivi, bagaglio culturale e aspettative d'uso.

### Il ruolo del designer come mediatore e traduttore
Il designer non è un decoratore a valle del processo, ma si posiziona **esattamente all'intersezione tra mittente e destinatario**:
- **Costruzione di analogie visive**: traduce concetti astratti voluti dal mittente (*"affidabile"*, *"innovativo"*, *"giocoso"*, *"istituzionale"*, *"urgente"*) in forme visive tangibili (scelta tipografica, relazioni di layout, spaziatura, palette cromatica).
- **Relatività culturale del significato**: ciò che appare 'giocoso' o 'rassicurante' per un target giovane può risultare caotico o respingente per un utente anziano; per questo il designer deve conoscere a fondo il modello mentale del destinatario.
- **La retorica visiva**: le analogie visive sono figure retoriche a tutti gli effetti. Più il designer possiede cultura visiva, storica e progettuale, più sarà in grado di scegliere la metafora e la forma più efficace per abbattere il rumore comunicativo ed evitare ambiguità percettive.""",
        "keyPoints": [
            "Triade comunicativa: Mittente, Messaggio e Destinatario.",
            "Il designer come ponte mediatore che converte concetti astratti in analogie e codici visivi leggibili.",
            "I concetti astratti non hanno significato universale: dipendono strettamente dal contesto socio-culturale del destinatario.",
            "La cultura visiva del designer è lo strumento retorico fondamentale per ridurre il rumore comunicativo."
        ],
        "flashcards": [
            {
                "question": "Quali sono i tre elementi fondanti di qualsiasi processo di trasmissione dell'informazione?",
                "answer": "Mittente (chi emette il messaggio), Messaggio (il contenuto cognitivo/visivo) e Destinatario (chi riceve, interpreta e decodifica)."
            },
            {
                "question": "In che posizione si colloca il designer rispetto a mittente e destinatario?",
                "answer": "Si colloca come mediatore neutrale e costruttore di analogie visive tra le intenzioni del mittente e i modelli mentali del destinatario."
            },
            {
                "question": "Perché un attributo visivo come 'giocoso' o 'autorevole' non ha valore assoluto?",
                "answer": "Perché la percezione dipende dal patrimonio culturale, dall'età e dalle aspettative cognitive del pubblico di destinatari."
            }
        ],
        "quiz": [
            {
                "question": "Secondo il modello illustrato nelle dispense, qual è la funzione primaria del designer nella trasmissione del messaggio?",
                "options": [
                    "Imporre un proprio stile visivo soggettivo indipendentemente dagli obiettivi dell'emittente",
                    "Costruire analogie visive mirate che colleghino le intenzioni del mittente ai modelli del destinatario",
                    "Aggiungere ornamenti estetici a un messaggio già interamente codificato e immodificabile",
                    "Sostituirsi integralmente al destinatario anticipandone ogni decisione di acquisto"
                ],
                "correctIndex": 1,
                "explanation": "Il designer agisce come mediatore attivo: traduce gli obiettivi astratti del mittente in un linguaggio visivo comprensibile ed efficace per il destinatario."
            },
            {
                "question": "Per quale motivo la percezione di attributi come 'divertente' o 'serio' varia tra diversi utenti?",
                "options": [
                    "Perché la decodifica del messaggio visivo è filtrata dal background culturale e dalle attese del ricevente",
                    "A causa esclusivamente delle diverse impostazioni di calibrazione cromatica dei monitor digitali",
                    "Perché tali concetti dipendono unicamente dalla velocità di caricamento delle pagine web",
                    "In quanto le convenzioni tipografiche non possiedono alcun legame con la storia sociale"
                ],
                "correctIndex": 0,
                "explanation": "La semiotica del design insegna che il significato delle analogie visive non è innato ma scaturisce dalle convenzioni culturali del destinatario."
            },
            {
                "question": "Cosa si intende per 'rumore comunicativo' nel contesto della progettazione visiva?",
                "options": [
                    "Il segnale audio o sonoro riprodotto automaticamente durante la visita a una pagina web",
                    "Qualsiasi ambiguità, distrazione o incoerenza grafica che ostacola la corretta ricezione del messaggio",
                    "L'eccessiva quantità di codice CSS caricata dal browser durante il primo rendering visivo",
                    "Il volume delle conversazioni tra designer e stakeholder durante le riunioni di brief"
                ],
                "correctIndex": 1,
                "explanation": "Il rumore comunicativo è ogni elemento di disturbo percettivo, incoerenza stilistica o confusione strutturale che devia l'attenzione dal nucleo del messaggio."
            },
            {
                "question": "Quale ruolo svolge la cultura visiva pregressa del designer nella creazione di interfacce?",
                "options": [
                    "Consente di selezionare figure retoriche e analogie visive più accurate ed efficaci per il target",
                    "Permette di evitare del tutto l'esecuzione di test con utenti prima del lancio commerciale",
                    "Garantisce che ogni progetto grafico risulti gradito a qualsiasi fascia demografica di utenti",
                    "Serve esclusivamente a velocizzare la stesura del codice front-end in HTML e CSS"
                ],
                "correctIndex": 0,
                "explanation": "Un ricco bagaglio di riferimenti visivi permette al designer di utilizzare metafore ed espressioni formali calibrate sulle specifiche capacità interpretative del pubblico."
            },
            {
                "question": "In che termini il design si differenzia dalla pura decorazione artistica personale?",
                "options": [
                    "Il design impiega solo figure geometriche regolari mentre l'arte impiega forme libere",
                    "L'arte richiede software vettoriali avanzati mentre il design si affida a tecniche tradizionali",
                    "Il design persegue l'efficacia funzionale e comunicativa orientata a un utente, non la mera espressione",
                    "Non sussiste alcuna differenza reale, trattandosi di discipline formalmente coincidenti"
                ],
                "correctIndex": 2,
                "explanation": "A differenza dell'arte pura, il design è un'attività orientata a uno scopo (teleologica), progettata per risolvere problemi e comunicare con destinatari specifici."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega come il designer si colloca tra mittente e destinatario e perché la sua funzione non è puramente estetica.",
                "modelAnswer": "Il designer funge da traduttore e ponte cognitivo: analizza il messaggio e gli obiettivi del mittente e li adatta alle capacità percettive del destinatario. La funzione non è puramente estetica perché la grafica orienta l'attenzione, stabilisce gerarchie di importanza, facilita la scansione visiva e permette all'utente di compiere azioni corrette senza esitazioni o fraintendimenti."
            }
        ]
    },

    # 2. Quella cosa chiamata design
    {
        "id": "dispense-c2",
        "number": 2,
        "title": "Quella cosa chiamata design",
        "subtitle": "I tre livelli del digitale: Interfaccia, Comportamento, Flusso e User Experience",
        "readTime": "9 min",
        "summary": """### Il design come disciplina olistica del digitale
Nel contesto contemporaneo, ogni nostra interazione quotidiana — dallo sblocco dello smartphone alla prenotazione di un volo, fino all'utilizzo di un bancomat o di un gestionale aziendale — avviene tramite un'interfaccia plasmata da designer.

### I tre livelli strutturali del design digitale
Per analizzare criticamente qualsiasi manufatto o prodotto interattivo, le dispense individuano tre componenti inscindibili:
1. **L'Interfaccia (UI - User Interface)**:
   - Rappresenta il livello sensoriale visivo: la disposizione spaziale di campi d'immissione, pulsanti, elementi tipografici, palette cromatica, icone e gerarchia compositiva.
   - È il livello più direttamente connesso alla tradizione del graphic design e della tipografia.
2. **Il Comportamento (Interaction Design)**:
   - È la dimensione temporale e reattiva del sistema: descrive cosa accade quando l'utente compie un'azione (il feedback immediato al passaggio del mouse con `:hover`, lo stato attivo al tocco, le micro-animazioni di caricamento, la comparsa di modali o notifiche toast).
   - Un'interfaccia visivamente perfetta ma priva di feedback di stato genera smarrimento immediato.
3. **Il Flusso (User Flow)**:
   - È la concatenazione logica e sequenziale delle schermate e dei passaggi che collegano il punto di partenza dell'utente al raggiungimento del suo obiettivo finale (ad es. la sequenza da catalogo ➔ scheda prodotto ➔ carrello ➔ checkout ➔ conferma ordine).

**La formula fondamentale:**
$$\\text{Interfaccia} + \\text{Comportamento} + \\text{Flusso} = \\text{User Experience (UX)}$$

### Problem Framing e Problem Solving
Il design moderno non comincia disegnando schermate:
- **Problem Framing**: l'abilità di definire e mettere a fuoco il problema reale prima di cercare soluzioni. Spesso i committenti propongono soluzioni errate a problemi mal compresi; il compito del designer è risalire al bisogno sottostante.
- **Problem Solving**: l'elaborazione di risposte formali, strutturali e funzionali capaci di risolvere il problema identificato.
- **La Ricerca (User Research)**: osservare gli utenti reali nei loro contesti operativi per scardinare supposizioni non verificate.
- **La natura dinamica del digitale**: a differenza della stampa, un prodotto digitale non è mai una scultura marmorea immutabile; è un organismo vivo che evolve attraverso rilasci incrementali, misurazione dei dati e test continui.""",
        "keyPoints": [
            "La tripartizione essenziale: Interfaccia (visivo), Comportamento (reattività/feedback), Flusso (architettura dei passaggi).",
            "La UX è la risultante sinergica di interfaccia, comportamento e flusso: il cedimento di un solo livello invalida l'esperienza.",
            "Distinzione cruciale tra Problem Framing (inquadrare il vero problema) e Problem Solving (costruire la soluzione).",
            "Il prodotto digitale è intrinsecamente dinamico, iterativo e suscettibile di costante perfezionamento empirico."
        ],
        "flashcards": [
            {
                "question": "Quali sono i tre livelli che costituiscono l'architettura dell'esperienza digitale?",
                "answer": "1. Interfaccia (cosa appare a schermo), 2. Comportamento (come reagisce il sistema), 3. Flusso (i passaggi per completare il compito)."
            },
            {
                "question": "Cosa si intende per 'Comportamento' di un'interfaccia?",
                "answer": "La risposta visiva e dinamica del sistema agli stimoli dell'utente (microinterazioni, stati hover, feedback di errore, animazioni di caricamento)."
            },
            {
                "question": "Qual è la differenza sostanziale tra Problem Framing e Problem Solving?",
                "answer": "Il Framing indaga quale sia il reale problema degli utenti prima di progettare; il Solving definisce la specifica soluzione esecutiva per risolverlo."
            }
        ],
        "quiz": [
            {
                "question": "Secondo le dispense, in quale livello rientrano i feedback visivi al passaggio del mouse e le transizioni di caricamento?",
                "options": [
                    "Nel livello dell'Architettura Server",
                    "Nel livello del Comportamento (Interaction Design)",
                    "Nel livello dello Style Tile",
                    "Nel livello della Semantica Tipografica"
                ],
                "correctIndex": 1,
                "explanation": "Il Comportamento definisce la reattività dinamica del sistema e i feedback visivi innescati dalle azioni dell'utente sullo schermo."
            },
            {
                "question": "Cosa definisce il 'Flusso' (User Flow) all'interno di un'applicazione o sito web?",
                "options": [
                    "La velocità di trasmissione dati tra la scheda di rete e il server di hosting",
                    "La sequenza temporale e logica di schermate per consentire all'utente di compiere un task",
                    "Il numero totale di caratteri tipografici impiegati all'interno della pagina principale",
                    "L'alternanza dei colori complementari stabiliti all'interno della guida di stile"
                ],
                "correctIndex": 1,
                "explanation": "Il flusso rappresenta il percorso strutturato passo dopo passo che guida l'utente dall'inizio alla conclusione del suo obiettivo."
            },
            {
                "question": "Perché la fase di 'Problem Framing' è considerata prioritaria rispetto al 'Problem Solving'?",
                "options": [
                    "Perché scrivere codice HTML privo di CSS richiede l'approvazione preliminare del cliente",
                    "Perché risolvere con grande cura il problema sbagliato non genera alcun reale valore per l'utente",
                    "In quanto il problem framing riduce automaticamente i costi di hosting del server cloud",
                    "Perché consente di delegare l'intera progettazione grafica a librerie esterne prefabbricate"
                ],
                "correctIndex": 1,
                "explanation": "Inquadrare correttamente il problema (Framing) garantisce che gli sforzi progettuali siano indirizzati verso i veri bisogni e non su supposizioni sterili."
            },
            {
                "question": "Se un sito possiede una grafica elegante ma presenta passaggi contorti per concludere l'acquisto, cosa ne consegue?",
                "options": [
                    "L'interfaccia eccellente compensa integralmente qualsiasi difetto presente nel percorso",
                    "L'esperienza utente complessiva (UX) risulta gravemente compromessa dal fallimento del flusso",
                    "Il browser web corregge autonomamente il codice del flusso per agevolare la navigazione",
                    "Il comportamento dinamico del sistema viene disattivato automaticamente dal server"
                ],
                "correctIndex": 1,
                "explanation": "La UX nasce dall'equilibrio armonico di interfaccia, comportamento e flusso; se uno dei tre pilastri cede, l'esperienza globale fallisce."
            },
            {
                "question": "Quale peculiarità distingue un manufatto digitale rispetto a un'opera a stampa tradizionale?",
                "options": [
                    "Il prodotto digitale viene concepito una sola volta e non subisce mai aggiornamenti",
                    "Il supporto a stampa permette interazioni reattive mentre il web è puramente statico",
                    "Il prodotto digitale è dinamico, monitorabile nei dati e sottoposto a continue iterazioni",
                    "La stampa consente di modificare il layout istantaneamente dopo la pubblicazione"
                ],
                "correctIndex": 2,
                "explanation": "Il digitale ha una natura iterativa: viene costantemente misurato mediante analytics e test di usabilità, evolvendo nel corso del tempo."
            }
        ],
        "openQuestions": [
            {
                "question": "Definisci i concetti di Interfaccia, Comportamento e Flusso, spiegando come concorrono alla User Experience.",
                "modelAnswer": "L'interfaccia rappresenta il livello visivo e spaziale degli elementi con cui l'utente interagisce. Il comportamento riguarda la risposta dinamica del sistema agli stimoli dell'utente (feedback, cambi di stato, microinterazioni). Il flusso è l'architettura dei passaggi che collegano gli stati del sistema per consentire il completamento di un task. Dalla corretta sinergia di questi tre livelli nasce l'esperienza utente (UX): se uno di essi è difettoso (es. flusso contorto o assenza di feedback), l'intera UX ne risulta compromessa."
            }
        ]
    },

    # 3. Layout
    {
        "id": "dispense-c3",
        "number": 3,
        "title": "Layout",
        "subtitle": "La tavola apparecchiata, Tschichold, principi visivi e unità di misura responsive",
        "readTime": "11 min",
        "summary": """### Che cos'è un layout: la metafora della 'Tavola Apparecchiata'
Il termine *layout* indica la disposizione e la partizione ordinata di elementi (testi, immagini, comandi) nello spazio bidimensionale.
Per chiarire il concetto, Riccardo Falcinelli in *Critica portatile al Visual Design* ricorre all'efficace metafora dell'**apparecchiare una tavola**:
- La posizione di piatti, forchette, coltelli, bicchieri e tovaglioli non risponde a un vezzo decorativo casuale, ma a una rigorosa **logica d'uso e discorsiva**.
- Se vediamo una tavola ordinata, comprendiamo al primo sguardo che sta per iniziare un pasto formale e sappiamo istintivamente dove allungare la mano per afferrare ciò che ci serve.
- Se le posate fossero sparpagliate alla rinfusa sul tavolo, proveremmo disorientamento e fatica cognitiva.
- Allo stesso modo, in un layout web, l'occhio umano **non può fare a meno di interpretare le relazioni spaziali**: la vicinanza, la grandezza e la posizione comunicano prima ancora della lettura testuale.

### Jan Tschichold e la Nuova Tipografia
Uno dei padri fondatori dell'organizzazione razionale della pagina è Jan Tschichold (autore di *Die neue Typographie*, 1928):
- Nei suoi trattati dimostrò il potere della gabbia modulare accostando layout non progettati (frammentati, privi di asse centrale, confusi) a layout organizzati secondo gerarchia, ritmo visivo e allineamenti rigorosi.

### I quattro principi cardine della composizione

#### 1. Il Contrasto
- Ha lo scopo primario di stabilire **chiari rapporti gerarchici** tra gli elementi della pagina.
- Si realizza attraverso: contrasto di scala (grande vs piccolo), contrasto di peso (bold vs regular), contrasto cromatico (colore saturo vs neutro) o contrasto di forma.
- Regola fondamentale: *se due elementi hanno importanza diversa, la differenza visiva deve essere netta ed evidente*, mai timida o appena accennata (che risulterebbe come un refuso visivo).

#### 2. La Prossimità (Principio di Vicinanza della Gestalt)
- Gli elementi collocati vicini nello spazio vengono automaticamente raggruppati dalla nostra percezione come parte di una medesima unità logico-concettuale.
- Applicazione tipografica: il titolo di un paragrafo deve avere una distanza inferiore dal testo che introduce rispetto al blocco che lo precede, al fine di scongiurare ambiguità di afferenza.

#### 3. Lo Spazio Bianco (Negative Space)
- Lo spazio vuoto non è un'area 'sprecata' da riempire a ogni costo, ma un **elemento compositivo attivo di primo piano**.
- Permette al cervello di riposare tra un blocco informativo e l'altro, riduce il rumore visivo, dona eleganza e fa risaltare i punti focali con immediatezza.

#### 4. Gli Allineamenti
- Nessun elemento deve galleggiare arbitrariamente: ogni margine o bordo dovrebbe idealmente trovare un allineamento lungo un asse visivo condiviso con altri elementi della pagina.
- Gli allineamenti creano una griglia invisibile ma tangibile che stabilizza la scansione visiva e infonde senso di rigore e professionalità.

### Dimensioni del layout e unità di misura sul web
A differenza del supporto cartaceo (formati fissi A4 o libro), il web non possiede dimensioni prestabilite:
- **Pixel (px)**: unità assoluta vincolata alla risoluzione fisica; utile per definire bordi fini o dimensioni minime fisse.
- **Percentuali (%)**: unità relative alla larghezza o altezza del contenitore genitore; fondamento delle gabbie responsive fluide.
- **Em e Rem**:
  - `em`: unità scalabile relativa al `font-size` dell'elemento o del suo genitore immediato (può causare effetto cascata o compounding).
  - `rem` (*root em*): unità scalabile calcolata esclusivamente rispetto al `font-size` dell'elemento radice `<html>` (solitamente 16px di default); garantisce una scalabilità accessibile e perfettamente coerente in tutta l'interfaccia.""",
        "keyPoints": [
            "Metafora di Falcinelli: il layout come tavola apparecchiata (funzionalità, abitudini e chiarezza d'uso).",
            "Jan Tschichold e la gabbia grafica: razionalizzazione dello spazio tra testo, immagini e margini.",
            "I 4 principi: Contrasto (gerarchia netta), Prossimità (raggruppamento Gestalt), Spazio Bianco (respiro e focus), Allineamento (ordine invisibile).",
            "Unità di misura web: pixel per valori assoluti, percentuali per fluidità, rem/em per scalabilità accessibile."
        ],
        "flashcards": [
            {
                "question": "In che cosa consiste la metafora della 'tavola apparecchiata' di Riccardo Falcinelli?",
                "answer": "La disposizione delle posate e dei piatti segue regole d'uso funzionali immediate; allo stesso modo il layout organizza lo spazio per rendere intuitivo l'accesso ai contenuti."
            },
            {
                "question": "Qual è la regola aurea del Contrasto nella composizione grafica?",
                "answer": "Se due elementi hanno ruoli o pesi gerarchici differenti, la loro diversità visiva deve essere marcata e inequivocabile, mai quasi simile."
            },
            {
                "question": "Perché l'unità di misura 'rem' è preferibile a 'px' per la tipografia accessibile sul web?",
                "answer": "Perché il 'rem' si adatta dinamicamente alle preferenze di dimensione del testo impostate dall'utente nel browser, a differenza del valore rigido in pixel."
            }
        ],
        "quiz": [
            {
                "question": "Cosa dimostrò Jan Tschichold nei suoi trattati sulla 'Nuova Tipografia'?",
                "options": [
                    "Che le gabbie modulari e gli allineamenti razionali migliorano drasticamente leggibilità e ordine",
                    "Che ogni composizione grafica deve obbligatoriamente adottare caratteri gotici e simmetria rigida",
                    "Che l'impiego di immagini a colori rende del tutto superfluo l'uso di griglie compositive",
                    "Che il testo deve occupare il 100% dello spazio disponibile sulla pagina per non sprecare carta"
                ],
                "correctIndex": 0,
                "explanation": "Tschichold teorizzò l'uso della griglia, dell'asimmetria funzionale e della gerarchia visiva per trasformare la tipografia in uno strumento moderno e leggibile."
            },
            {
                "question": "In base al principio della Prossimità (Gestalt), cosa percepisce la mente umana?",
                "options": [
                    "Gli elementi colorati con tinte calde vengono interpretati come geograficamente più vicini",
                    "Gli oggetti collocati fisicamente vicini nello spazio vengono raggruppati nella medesima unità logica",
                    "I testi scritti in caratteri sans-serif vengono elaborati più rapidamente dei caratteri graziati",
                    "Tutti gli elementi dotati di bordo spesso vengono isolati come minacce visive per l'utente"
                ],
                "correctIndex": 1,
                "explanation": "La legge della prossimità stabilisce che la vicinanza spaziale è il primo fattore automatico di raggruppamento percettivo impiegato dal cervello."
            },
            {
                "question": "Quale funzione costruttiva svolge lo Spazio Bianco (Negative Space) all'interno di un'interfaccia?",
                "options": [
                    "Serve esclusivamente come area di scorta per inserire futuri annunci pubblicitari",
                    "Separa i blocchi di contenuto, riduce il carico visivo e orienta l'occhio verso i punti focali",
                    "Indica che il designer non ha completato la stesura dei testi della pagina web",
                    "Rallenta intenzionalmente la lettura dell'utente per aumentare il tempo medio di sessione"
                ],
                "correctIndex": 1,
                "explanation": "Lo spazio negativo è una componente attiva del design: dona respiro, definisce i confini dei gruppi e valorizza il contenuto primario."
            },
            {
                "question": "Qual è la differenza sostanziale tra l'unità di misura CSS 'em' e l'unità 'rem'?",
                "options": [
                    "Il valore 'em' si riferisce alla larghezza del monitor, mentre 'rem' si riferisce all'altezza",
                    "L'unità 'em' è scalabile sul font del genitore, mentre 'rem' fa riferimento unicamente alla radice html",
                    "Il valore 'rem' funziona solo con caratteri serif, mentre 'em' richiede font monospazio",
                    "Non sussiste alcuna differenza pratica, trattandosi di sinonimi intercambiabili nel codice"
                ],
                "correctIndex": 1,
                "explanation": "'rem' (root em) è ancorato alla dimensione del font dichiarata sul tag radice `html`, evitando i problemi di moltiplicazione cumulativa tipici di 'em'."
            },
            {
                "question": "Cosa accade se in un layout il contrasto tra il titolo primario e il testo del paragrafo è appena accennato?",
                "options": [
                    "La pagina risulta più elegante poiché priva di elementi graficamente invasivi",
                    "La gerarchia informativa diventa ambigua e l'utente fatica a scandire i blocchi di lettura",
                    "I motori di ricerca indicizzano automaticamente il titolo assegnandogli massima priorità",
                    "Il browser aumenta autonomamente il peso tipografico del titolo per correggere l'errore"
                ],
                "correctIndex": 1,
                "explanation": "Un contrasto debole o timido genera confusione gerarchica: l'occhio non comprende se si tratti di due elementi distinti o di una svista d'impaginazione."
            }
        ],
        "openQuestions": [
            {
                "question": "Spiega i 4 principi cardine del layout descritti nelle dispense e fornisci un esempio pratico di applicazione per ciascuno.",
                "modelAnswer": "I 4 principi sono: 1. Contrasto: differenziare in modo netto pesi e scale (es. titolo h1 a 32px bold scuro rispetto a testo body a 16px regular). 2. Prossimità: raggruppare visivamente elementi correlati (es. distanza minima tra etichetta input e relativo campo modulo). 3. Spazio Bianco: isolare i blocchi informativi con padding generoso per facilitare la scansione senza soffocare la pagina. 4. Allineamento: ancorare tutti i blocchi a una griglia invisibile (es. allineamento a sinistra comune tra logo, titoli e card di contenuto)."
            }
        ]
    }
]

with open('dispense_part1.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)
print("Part 1 built successfully")
