# -*- coding: utf-8 -*-
"""
High-level academic quiz and exam questions for Stull UX Design - Chapters 29 to 34.
29: Principi della Gestalt applicati all'UI
30: Copywriting e Microcopy
31: Accessibilità e Design Inclusivo
32: Design System e scalabilità
33: Test di usabilità qualitativi
34: Test non moderati e da remoto
"""

import json

stull_c29_to_34 = {
    "stull-c29": {
        "quiz": [
            {
                "question": "Cosa postula l'assioma fondante della psicologia della Gestalt (Wertheimer, Koffka, Köhler, 1912) applicato al design delle interfacce?",
                "options": [
                    "'Il tutto è diverso dalla somma delle sue singole parti': il cervello umano non percepisce elementi visivi isolati, ma li organizza istantaneamente in configurazioni globali e insiemi dotati di senso",
                    "Gli schermi dei computer devono essere costruiti con proporzioni quadrate perfette",
                    "I colori primari sono superiori a tutte le altre combinazioni cromatiche",
                    "La percezione visiva umana funziona esattamente come una fotocamera a pellicola chimica"
                ],
                "correctIndex": 0,
                "explanation": "La mente cerca ordine ed economia: quando guardiamo una schermata, il cervello raggruppa elementi vicini o simili creando automaticamente gruppi, gerarchie e significati d'insieme prima ancora di leggere i testi."
            },
            {
                "question": "In base al 'Principio di Somiglianza' (Similarity) della Gestalt, quale comportamento percettivo si manifesta nell'utente?",
                "options": [
                    "Elementi che condividono caratteristiche visive simili (stesso colore, forma, dimensione o stile) vengono percepiti automaticamente come appartenenti alla stessa funzione o categoria logica",
                    "Tutti gli utenti con lo stesso nome hanno gli stessi gusti grafici",
                    "I pulsanti quadrati richiedono più tempo per essere cliccati rispetto a quelli rotondi",
                    "Gli elementi con testo in corsivo vengono ignorati dal motore di rendering del browser"
                ],
                "correctIndex": 0,
                "explanation": "Se tutti i link di navigazione sono blu e in grassetto, l'utente sa che qualsiasi testo blu e in grassetto sulla pagina è un link. Usare lo stesso stile per testo statico crea confusione distruggendo il principio."
            },
            {
                "question": "Cosa descrive la 'Legge di Chiusura' (Closure) della Gestalt?",
                "options": [
                    "La tendenza della mente a completare visivamente figure o contorni parzialmente interrotti o frammentati, percependo un oggetto intero anche dove mancano delle parti",
                    "La chiusura definitiva della finestra del browser al termine dell'acquisto",
                    "L'obbligo di inserire un punto fermo alla fine di ogni frase scritta sul web",
                    "La rimozione delle immagini non scaricate entro cinque secondi"
                ],
                "correctIndex": 0,
                "explanation": "Esempio magistrale: il logo del WWF (il panda) o un carosello su mobile dove l'ultima card sbuca tagliata a metà dal bordo dello schermo; il cervello 'completa' la forma e capisce subito che si può scorrere."
            },
            {
                "question": "Quale fenomeno visivo è governato dalla relazione 'Figura-Sfondo' (Figure-Ground)?",
                "options": [
                    "La capacità del sistema percettivo di distinguere chiaramente l'oggetto di interesse focale prioritario (la figura) dal piano di riferimento neutro sottostante (lo sfondo)",
                    "Il calcolo della profondità di campo nei file video ad alta definizione",
                    "La regolazione automatica del volume audio negli altoparlanti del computer",
                    "La scelta di una fotografia panoramica per la testata del sito aziendale"
                ],
                "correctIndex": 0,
                "explanation": "Fondamentale nei modali (popup): quando si apre una finestra modale, lo sfondo sotto viene scurito o sfocato (backdrop). Questo stacca la figura dallo sfondo, concentrando l'attenzione senza ambiguità."
            },
            {
                "question": "Cosa stabilisce la 'Legge della Regione Comune' (Common Region) introdotta da Stephen Palmer nel 1992?",
                "options": [
                    "Elementi collocati all'interno di un confine visivo chiuso condiviso (come una card con bordo, un riquadro con sfondo colorato o una linea perimetrale) vengono percepiti come un gruppo fortemente unito",
                    "I residenti della stessa nazione devono visualizzare la stessa versione del sito",
                    "Tutti i dati devono essere archiviati in server situati nella medesima regione geografica",
                    "Le immagini devono essere raggruppate unicamente per data di scatto"
                ],
                "correctIndex": 0,
                "explanation": "È il principio alla base del card design: racchiudere titolo, immagine e bottone dentro una scatola con sfondo bianco e ombra leggera fa percepire quel blocco come un'unità autonoma indissolubile."
            }
        ],
        "examQuiz": [
            {
                "question": "In un'applicazione mobile, un carosello orizzontale mostra 3 card perfette che occupano esattamente la larghezza dello schermo senza lasciare intravedere nulla ai lati. Gli utenti non scorrono mai il carosello. Come si risolve applicando la Gestalt?",
                "options": [
                    "Applicando la Legge di Chiusura: far sporgere parzialmente (peek) la quarta card tagliata a metà dal bordo destro dello schermo, stimolando il cervello a completare la forma e suggerendo lo swipe naturale",
                    "Inserendo un testo lampeggiante di 50 parole che ordina di fare scorrere il dito",
                    "Raddoppiando l'altezza del carosello fino a coprire l'intera pagina",
                    "Sostituendo tutte le card con file audio ad avvio automatico"
                ],
                "correctIndex": 0,
                "explanation": "Se la card finisce esattamente sul bordo dello schermo, il cervello chiude la forma e crede che la lista sia finita (falsa fine/illusion of completeness). Tagliare a metà la card fa capire all'istante che c'è altro da vedere."
            },
            {
                "question": "In un modulo di login, il testo di errore in rosso 'Password non valida' è posizionato a 40px dal campo password e a soli 4px dal pulsante 'Invia'. Quale legge della Gestalt è violata e quale disservizio provoca?",
                "options": [
                    "La Legge di Prossimità: l'errore appare visivamente agganciato al pulsante sottostante anziché al campo a cui si riferisce, disorientando l'utente sulla natura del problema",
                    "La Legge di Buona Continuazione geometrica",
                    "Il principio di sovranità digitale del consumatore",
                    "La compatibilità del foglio di stile con i vecchi monitor a tubo catodico"
                ],
                "correctIndex": 0,
                "explanation": "Prossimità invertita: gli elementi correlati devono stare vicini. L'avviso di errore deve trovarsi subito sotto il campo incriminato (4-8px), non galleggiare vicino ad altri comandi estranei."
            },
            {
                "question": "Cosa si intende per 'Legge del Destino Comune' (Common Fate) nelle interfacce animate moderne?",
                "options": [
                    "Elementi visivi che si muovono simultaneamente nella stessa direzione e alla stessa velocità vengono percepiti automaticamente dal cervello come parte della medesima entità logica",
                    "Il destino condiviso di tutte le aziende che non investono in usabilità",
                    "La cancellazione programmata di tutti i file temporanei a fine giornata",
                    "La sincronizzazione dell'orologio di sistema con il fuso orario di Greenwich"
                ],
                "correctIndex": 0,
                "explanation": "Fondamentale nell'animazione UI: se aprendo un cassetto laterale (drawer) l'icona, il testo e lo sfondo scorrono insieme verso destra con la stessa velocità, il cervello li decodifica come un unico oggetto solido."
            }
        ]
    },
    "stull-c30": {
        "quiz": [
            {
                "question": "Cosa si intende per 'UX Writing' (e Microcopy) nella progettazione dei prodotti digitali?",
                "options": [
                    "La disciplina che progetta i testi brevi, mirati e contestuali dell'interfaccia (etichette, bottoni, messaggi di errore, istruzioni, notifiche) per guidare l'utente con chiarezza, empatia ed efficacia",
                    "La redazione di articoli di giornale lunghi per i blog aziendali",
                    "La scrittura di poesie commemorative in occasione dei lanci di prodotto",
                    "La stesura di contratti legali in linguaggio burocratico formale"
                ],
                "correctIndex": 0,
                "explanation": "L'UX Writing non decora l'interfaccia a posteriori: progetta l'interazione attraverso le parole. Un microcopy brillante su un bottone o in un messaggio di errore può raddoppiare le conversioni e azzerare l'ansia."
            },
            {
                "question": "Quali sono le tre qualità imprescindibili che ogni testo di Microcopy deve possedere?",
                "options": [
                    "Chiaro (privo di gergo e inequivocabile), Conciso (senza parole inutili) e Utile (orientato ad aiutare l'utente a compiere il prossimo passo)",
                    "Lungo, Poetico e Accademico",
                    "Economico, Commerciale e Promozionale",
                    "Misterioso, Reticente e Astratto"
                ],
                "correctIndex": 0,
                "explanation": "Le tre 'C' di Google per l'UX Writing: Clear, Concise, Useful. Nessuna parola di troppo, nessun termine gergale per addetti ai lavori, solo la guida limpida per andare avanti."
            },
            {
                "question": "Come si formula un messaggio di errore ideale (Error Message) secondo le buone pratiche di UX Writing?",
                "options": [
                    "Spiegando con garbo cosa è successo in parole semplici, indicando dove risiede l'intoppo e fornendo una soluzione costruttiva immediata per risolverlo, senza mai incolpare l'utente",
                    "Mostrando un codice alfanumerico esadecimale come 'Err 0x847B' senza spiegazioni",
                    "Scrivendo 'Operazione non valida!' in caratteri maiuscoli lampeggianti",
                    "Chiudendo l'applicazione senza mostrare alcun tipo di testo a schermo"
                ],
                "correctIndex": 0,
                "explanation": "Un buon errore non dice 'Hai sbagliato!', ma 'Ops, la data di nascita inserita è nel futuro. Controlla l'anno e riprova'. Trasparenza, gentilezza e via d'uscita immediata."
            },
            {
                "question": "Cosa si intende per 'Tone of Voice' (Tono di Voce) di un'applicazione digitale?",
                "options": [
                    "L'espressione della personalità del marchio attraverso il linguaggio, che deve adattarsi con intelligenza al contesto emotivo dell'utente (es. empatico e rassicurante in caso di errore, brillante ed energico in un traguardo)",
                    "Il volume in decibel con cui l'assistente vocale pronuncia le parole",
                    "L'accento regionale utilizzato dagli attori negli spot radiofonici",
                    "La frequenza di campionamento dei file musicali di sottofondo"
                ],
                "correctIndex": 0,
                "explanation": "La voce è l'identità stabile (chi sei); il tono è l'abito contestuale (come parli). Se un'app bancaria fa battute spiritose mentre l'utente scopre che la carta è bloccata, il tono è gravemente stonato."
            },
            {
                "question": "Quale testo su un pulsante Call to Action (CTA) è nettamente superiore per l'usabilità rispetto al generico 'Invia'?",
                "options": [
                    "Un testo che descrive esplicitamente il valore o l'azione finale (es. 'Crea il mio account gratuito' o 'Conferma e paga 25€')",
                    "La parola 'Clicca qui per proseguire'",
                    "Un'espressione poetica in lingua latina",
                    "Un semplice punto esclamativo privo di lettere"
                ],
                "correctIndex": 0,
                "explanation": "Il bottone deve promettere il risultato: 'Invia' è pigro e impersonale; 'Prenota il tuo tavolo' o 'Scarica la guida gratuita' chiarisce esattamente cosa riceverà l'utente al tocco."
            }
        ],
        "examQuiz": [
            {
                "question": "Un modulo di cancellazione dell'account presenta un pulsante rosso con scritto: 'Annulla'. Un utente vuole cancellare l'account ma non sa se cliccando 'Annulla' cancellerà l'account o annullerà la procedura. Quale grave difetto di microcopy è presente?",
                "options": [
                    "Ambiguità lessicale fatale: 'Annulla' può significare sia 'Cancella account' sia 'Abortisci operazione'; la soluzione corretta è usare etichette esplicite: 'Elimina definitivamente account' e 'Torna indietro'",
                    "Un errore di compatibilità con i sistemi operativi Windows",
                    "La violazione delle normative sul commercio marittimo internazionale",
                    "Una richiesta esplicita imposta dalle direttive antitrust europee"
                ],
                "correctIndex": 0,
                "explanation": "L'ambiguità nei momenti critici è letale. Mai usare verbi doppi come 'Annulla' in contesti distruttivi: usate verbi di stato inequivocabili che non lascino ombra di dubbio sull'esito."
            },
            {
                "question": "In un esperimento celebre su Google Hotel Search, il team cambiò il testo del bottone da 'Prenota una stanza' a 'Verifica disponibilità'. Quale impatto produsse e perché?",
                "options": [
                    "Un aumento del 17% dell'engagement, perché 'Prenota' suonava come un impegno economico e contrattuale prematuro e vincolante, mentre 'Verifica disponibilità' invitava all'esplorazione a zero rischio",
                    "Un crollo del 90% delle prenotazioni a causa dell'uso di parole troppo lunghe",
                    "La cancellazione automatica di tutti i database alberghieri collegati",
                    "Nessun cambiamento misurabile trattandosi di sinonimi esatti"
                ],
                "correctIndex": 0,
                "explanation": "Il potere delle parole: nelle fasi esplorative l'utente ha paura di vincolarsi. Dire 'Verifica disponibilità' toglie la frizione dell'impegno economico e spalanca le porte del funnel."
            },
            {
                "question": "Cosa sono i 'Dark Patterns' nel copywriting (es. il Confusopoly o il Confirmshaming)?",
                "options": [
                    "Testi manipolatori e disonesti progettati per far sentire in colpa o confondere l'utente spingendolo a fare ciò che vuole l'azienda (es. 'No grazie, non mi piace risparmiare denaro' per rifiutare una newsletter)",
                    "Caratteri tipografici stampati con inchiostro nero invisibile",
                    "Algoritmi di intelligenza artificiale per il furto di dati personali",
                    "Moduli di contatto visualizzati unicamente durante la notte"
                ],
                "correctIndex": 0,
                "explanation": "Il Confirmshaming è una vergogna etica: far leva sul senso di colpa per forzare un'iscrizione. Distrugge la stima dell'utente verso il brand e genera risentimento duraturo."
            }
        ]
    },
    "stull-c31": {
        "quiz": [
            {
                "question": "Cosa stabilisce il concetto di 'Design Inclusivo' (Inclusive Design) rispetto all'accessibilità tradizionale?",
                "options": [
                    "Progettare fin dall'inizio considerando la vasta gamma della diversità umana (disabilità permanenti, temporanee e situazionali), creando soluzioni che migliorano l'esperienza per chiunque",
                    "Progettare unicamente per le persone con disabilità visiva trascurando tutti gli altri",
                    "Tradurre tutti i siti web in cento lingue straniere contemporaneamente",
                    "Costruire siti web identici per qualsiasi azienda commerciale"
                ],
                "correctIndex": 0,
                "explanation": "Il design inclusivo non è una checklist medica: è una filosofia. Riconosce che la disabilità non è un difetto della persona, ma la discrepanza tra le capacità umane e un ambiente mal progettato."
            },
            {
                "question": "Quali sono i tre livelli temporali di disabilità identificati nel Microsoft Inclusive Design Toolkit?",
                "options": [
                    "Disabilità Permanente (es. un braccio amputato), Temporanea (es. un braccio ingessato per una frattura) e Situazionale (es. un genitore con un neonato in braccio)",
                    "Infantile, Giovanile e Senile",
                    "Fisica, Chimica e Meccanica",
                    "Hardware, Software e Network"
                ],
                "correctIndex": 0,
                "explanation": "La geniale matrice di Microsoft: progettare per chi ha un solo braccio (permanente) aiuta chi si è rotto il polso (temporaneo) e chi guida tenendo la spesa (situazionale). L'inclusione serve a tutti."
            },
            {
                "question": "Cosa descrive il celebre 'Curb Cut Effect' (Effetto Scivolo del Marciapiede)?",
                "options": [
                    "Il fenomeno per cui una caratteristica o innovazione progettata inizialmente per persone con disabilità finisce per avvantaggiare enormemente l'intera popolazione (es. sottotitoli dei video o scivoli stradali)",
                    "Il degrado del cemento armato lungo le strade ad alto traffico",
                    "La riduzione della velocità delle automobili nei pressi dei semafori",
                    "Il consumo energetico dei lampioni dell'illuminazione pubblica"
                ],
                "correctIndex": 0,
                "explanation": "Gli scivoli sui marciapiedi furono creati per le sedie a rotelle; oggi li usano mamme con passeggini, corrieri con carrelli, viaggiatori con trolley e ciclisti. L'accessibilità arricchisce la società intera."
            },
            {
                "question": "Quali sono i 4 principi cardine (POUR) delle linee guida internazionali WCAG 2.1?",
                "options": [
                    "Percepibile (Perceivable), Utilizzabile (Operable), Comprensibile (Understandable) e Robusto (Robust)",
                    "Perfetto, Ottimo, Utile e Rapido",
                    "Progettato, Organizzato, Unificato e Reattivo",
                    "Pubblico, Originale, Universale e Resistente"
                ],
                "correctIndex": 0,
                "explanation": "L'acronimo POUR è la bibbia dell'accessibilità: le informazioni devono potersi percepire coi sensi, l'interfaccia deve potersi comandare, i testi devono essere chiari e il codice deve reggere su ogni browser."
            },
            {
                "question": "Perché un video web deve sempre contenere sottotitoli sincronizzati (Closed Captions) oltre alla traccia audio?",
                "options": [
                    "Per garantire l'accesso alle persone non udenti o ipoudenti, ma anche per consentire la visione a milioni di persone in ambienti rumorosi, sui mezzi pubblici o in ufficio con audio disattivato",
                    "Perché i motori di ricerca non supportano i file multimediali video",
                    "Per aumentare il peso in megabyte del file caricato sul server",
                    "Perché la legge impone di tradurre tutti i video in lingua esperanto"
                ],
                "correctIndex": 0,
                "explanation": "Altra prova del Curb Cut Effect: oltre l'80% dei video sui social media viene guardato a volume zero; i sottotitoli creati per i non udenti sono diventati indispensabili per tutti."
            }
        ],
        "examQuiz": [
            {
                "question": "Un designer rimuove l'anello di focus da tastiera in CSS con la regola 'outline: none' perché 'era un brutto contorno blu che rovinava l'estetica'. Quale disastro di accessibilità provoca?",
                "options": [
                    "Rende il sito completamente inusabile per milioni di persone con disabilità motorie che navigano con il tasto Tab, che non sanno più dove si trovi il cursore sullo schermo",
                    "Provoca l'immediata disinstallazione del browser dal computer dell'utente",
                    "Invalida la validazione del codice HTML secondo le direttive del W3C",
                    "Aumenta la frequenza di aggiornamento della scheda grafica a 240Hz"
                ],
                "correctIndex": 0,
                "explanation": "Togliere l'outline senza sostituirlo con un indicatore di focus personalizzato visibile è come togliere il volante a chi non usa il mouse: l'utente preme Tab e naviga alla cieca nel buio."
            },
            {
                "question": "In un audit di accessibilità, un portale ottiene un contrasto cromatico di 3.2:1 per il testo del corpo a 14px su sfondo grigio. È conforme alle WCAG AA?",
                "options": [
                    "No: per il testo standard (sotto i 18pt o 14pt grassetto) il rapporto di contrasto minimo deve essere di almeno 4.5:1; un valore di 3.2:1 è non conforme e rende la lettura faticosa o impossibile",
                    "Sì: qualsiasi contrasto superiore a 2.0:1 è considerato conforme alle normative",
                    "Sì: purché il font utilizzato appartenga alla famiglia dei caratteri sans-serif",
                    "È conforme unicamente se il portale viene visitato durante le ore diurne"
                ],
                "correctIndex": 0,
                "explanation": "Le soglie matematiche WCAG sono tassative: 4.5:1 per testo normale; 3.0:1 per testo grande. Un contrasto di 3.2:1 per testo minuto condanna persone con ipovisione o anziani all'illeggibilità."
            },
            {
                "question": "Quale impatto legale e commerciale ha l'entrata in vigore dell'European Accessibility Act (EAA 2025) per le aziende digitali che operano nell'Unione Europea?",
                "options": [
                    "Rende l'accessibilità un obbligo di legge inderogabile per tutti i servizi digitali privati (e-commerce, banche, trasporti, media), con pesanti sanzioni economiche per le aziende non conformi",
                    "Impone la chiusura di tutti i siti web creati prima del 2020",
                    "Obbliga le aziende a fornire smartphone gratuiti a tutti i cittadini europei",
                    "Vieta la vendita di prodotti digitali a persone residenti fuori dall'Europa"
                ],
                "correctIndex": 0,
                "explanation": "L'EAA segna la svolta epocale: l'accessibilità non è più un 'optional etico', ma un requisito normativo stringente con multe salatissime per chi esclude i cittadini dai servizi digitali."
            }
        ]
    },
    "stull-c32": {
        "quiz": [
            {
                "question": "Cos'è un 'Design System' nella moderna produzione digitale e in cosa differisce da una semplice guida di stile (Style Guide)?",
                "options": [
                    "È un ecosistema completo, vivo e integrato di principi, pattern, linee guida, token e componenti codificati riutilizzabili condivisi tra design e sviluppo, corredato da regole di governance",
                    "È un file PDF statico di cinquanta pagine stampato e conservato in archivio",
                    "È un software antivirus per proteggere i computer dei designer",
                    "È l'elenco dei fornitori di cancelleria e carta per gli uffici aziendali"
                ],
                "correctIndex": 0,
                "explanation": "Una Style Guide statica muore in tre mesi. Un Design System è un'infrastruttura viva: codice, design e documentazione allineati in tempo reale come singola fonte di verità per tutta l'azienda."
            },
            {
                "question": "Quale metafora gerarchica propone la metodologia 'Atomic Design' di Brad Frost per strutturare i componenti di un Design System?",
                "options": [
                    "Una scala chimica a 5 stadi: Atomi (particelle base), Molecole (gruppi di atomi), Organismi (sezioni complesse), Template (strutture di pagina) e Pagine (istanze con contenuti reali)",
                    "Una piramide militare: Soldati, Sergenti, Capitani, Generali e Presidenti",
                    "Un albero genealogico biologico: Radici, Tronco, Rami, Foglie e Frutti",
                    "Un sistema solare: Sole, Pianeti, Satelliti, Asteroidi e Comete"
                ],
                "correctIndex": 0,
                "explanation": "L'Atomic Design insegna la modularità: un'etichetta, un input e un bottone (atomi) si uniscono per formare la barra di ricerca (molecola), che inserita nella testata forma l'organismo."
            },
            {
                "question": "Cosa si intende per 'Governance' di un Design System?",
                "options": [
                    "L'insieme di processi, regole, ruoli e flussi decisionali che stabiliscono come i componenti vengono proposti, creati, revisionati, aggiornati o ritirati nel tempo per evitarne il degrado",
                    "Il consiglio di amministrazione politico del comune in cui ha sede l'impresa",
                    "Il pagamento delle imposte governative sui marchi di fabbrica registrati",
                    "Il controllo di polizia giudiziaria sui contenuti pubblicati sul sito web"
                ],
                "correctIndex": 0,
                "explanation": "Un Design System senza governance diventa un cimitero caotico: chi decide se serve un nuovo bottone? Come si approva una modifica? La governance mantiene il sistema sano e coerente."
            },
            {
                "question": "Quale straordinario beneficio di efficienza aziendale produce l'adozione matura di un Design System?",
                "options": [
                    "Abbassa drasticamente il Time-to-Market delle nuove funzionalità, elimina la duplicazione di lavoro tra team, garantisce coerenza e libera tempo per concentrarsi sui veri problemi degli utenti",
                    "Rende superfluo l'impiego di una connessione internet negli uffici aziendali",
                    "Consente di raddoppiare il prezzo di vendita dei prodotti ogni tre mesi",
                    "Elimina automaticamente la necessità di fare manutenzione sui server fisici"
                ],
                "correctIndex": 0,
                "explanation": "Senza Design System, ogni team passa settimane a ridisegnare e ricodificare la propria card o il proprio form. Con esso, i blocchi sono pronti e testati: le schermate si assemblano in ore anziché mesi."
            },
            {
                "question": "Cos'è una 'Living Style Guide' (o documentazione interattiva come Storybook)?",
                "options": [
                    "Una piattaforma web interattiva che esegue e renderizza i componenti direttamente dal codice sorgente reale usato in produzione, mostrando stati, proprietà e codice aggiornato in tempo reale",
                    "Un libro di design con copertina in pelle naturale non trattata",
                    "Una trasmissione televisiva settimanale dedicata all'arredamento d'interni",
                    "Un diario personale compilato quotidianamente dal capo dei programmatori"
                ],
                "correctIndex": 0,
                "explanation": "Storybook è lo specchio vivo del codice: designer e ingegneri vedono e testano il componente vero nel browser, con tutti i suoi stati e varianti, garantendo trasparenza assoluta."
            }
        ],
        "examQuiz": [
            {
                "question": "In un'azienda con 8 team di prodotto indipendenti, ciascun team ha creato la propria versione del pulsante 'Paga ora', generando 8 stili, colori e comportamenti diversi. Quale diagnosi organizzativa ne scaturisce?",
                "options": [
                    "Frammentazione dell'esperienza e gravissimo debito tecnico: l'assenza di un Design System centralizzato provoca incoerenza per l'utente e moltiplica per 8 i costi di manutenzione e correzione bug",
                    "Un'eccellente applicazione del principio della biodiversità digitale",
                    "Una strategia virtuosa per confondere i concorrenti industriali",
                    "Un requisito tecnico indispensabile per i sistemi di pagamento con carta di credito"
                ],
                "correctIndex": 0,
                "explanation": "L'anarchia da silos: 8 team che riscrivono la stessa cosa sprecano centinaia di migliaia di euro e disorientano il cliente che vede l'app cambiare faccia a ogni schermata. Un Design System cura questa piaga."
            },
            {
                "question": "Quale modello di team di governance è considerato più sostenibile per la crescita di un Design System (Modello Centralizzato vs Federato)?",
                "options": [
                    "Il Modello Federato (o Ibrido): un team centrale nucleare supportato da 'ambasciatori' distribuiti all'interno dei singoli team di prodotto che raccolgono bisogni reali e contribuiscono all'evoluzione",
                    "Il Modello Dittatoriale: un solo designer anziano che decide tutto senza consultare nessuno",
                    "Il Modello Anarchico: chiunque può modificare il codice centrale senza alcuna revisione",
                    "Il Modello Esterno: delegare la gestione a un'agenzia che non conosce i prodotti aziendali"
                ],
                "correctIndex": 0,
                "explanation": "Il modello federato evita la torre d'avorio: se il team del Design System si isola, crea componenti che nessuno usa. Con gli ambasciatori nei team di prodotto, il sistema evolve sulle reali esigenze sul campo."
            },
            {
                "question": "In che modo l'accessibilità (a11y) viene scalata in tutta l'azienda grazie al Design System?",
                "options": [
                    "Rendendo accessibili alla radice i componenti base (atomi e molecole): ogni volta che uno sviluppatore usa il bottone o il form del Design System, eredita gratuitamente contrasti WCAG, focus e ruoli ARIA già testati",
                    "Obbligando tutti i dipendenti a seguire un corso di laurea in oculistica",
                    "Cancellando tutti i componenti che contengono immagini fotografiche",
                    "Disabilitando l'uso della tastiera per tutti i programmatori del team"
                ],
                "correctIndex": 0,
                "explanation": "L'accessibilità sistemica: invece di formare 50 programmatori su complessi ruoli ARIA per ogni singolo task, si collaudano i componenti del Design System una volta per tutte, e chiunque li usa produce codice accessibile per default."
            }
        ]
    },
    "stull-c33": {
        "quiz": [
            {
                "question": "Qual è il protocollo metodologico cardine di un 'Test di Usabilità Moderato' qualitativo?",
                "options": [
                    "Un partecipante viene invitato a completare scenari di compiti realistici sul prototipo, verbalizzando pensieri e impressioni ad alta voce (Thinking Aloud), mentre un facilitatore osserva e guida senza suggerire",
                    "Un esame universitario a risposte multiple con penalità per ogni errore commesso",
                    "Un colloquio di lavoro per verificare le competenze tecniche informatiche del candidato",
                    "Una seduta di psicoanalisi freudiana per indagare i traumi infantili dell'utente"
                ],
                "correctIndex": 0,
                "explanation": "Il test moderato è il microscopio della UX: mettete la persona davanti al prodotto, le date un compito ('Prenota un hotel a Roma per due notti') e ascoltate i suoi pensieri mentre cerca di farlo."
            },
            {
                "question": "Come deve formulare i 'Compiti' (Task Scenarios) il ricercatore affinché il test produca dati autentici?",
                "options": [
                    "In forma di scenari realistici orientati all'obiettivo finale, senza mai rivelare le parole esatte scritte sui bottoni o guidare i passaggi (es. 'Vuoi fare un regalo a tua sorella', non 'Clicca sulla voce Regali')",
                    "Fornendo l'elenco esatto delle dieci schermate da visitare in ordine numerico",
                    "Spiegando passo dopo passo dove cliccare per non far sbagliare il partecipante",
                    "Formulandoli in lingua straniera per verificare la pronuncia dell'utente"
                ],
                "correctIndex": 0,
                "explanation": "Se nel testo del compito usate la parola esatta del bottone ('Cerca regali'), l'utente farà solo matching visivo di parole. Lo scenario deve descrivere il bisogno nella vita reale ('Trova un pensiero per il compleanno')."
            },
            {
                "question": "Cosa deve fare il facilitatore quando un utente durante il test chiede: 'Cosa devo fare adesso? È giusto questo pulsante?'",
                "options": [
                    "Rilanciare con una domanda a specchio (Mirroring / Boomerang): 'Cosa ti aspetteresti che accada cliccando lì?', incoraggiando l'esplorazione autonoma senza fornire aiuti né conferme",
                    "Rispondere subito dicendo dove cliccare per non fargli perdere tempo",
                    "Rimproverare l'utente per non aver letto attentamente le istruzioni della pagina",
                    "Spegnere il monitor del computer e dichiarare conclusa la sessione"
                ],
                "correctIndex": 0,
                "explanation": "La regola di ferro del moderatore: mai spiegare, mai giustificare, mai aiutare. Se aiutate l'utente, avete distrutto il dato del test. La domanda a specchio rimette in moto il suo modello mentale spontaneo."
            },
            {
                "question": "Quale ruolo svolge la registrazione video e dello schermo durante una sessione di test di usabilità?",
                "options": [
                    "Fornisce prove inconfutabili (clip di evidenza) per mostrare a stakeholder e dirigenti scettici le reali difficoltà incontrate dagli utenti, superando qualsiasi contestazione soggettiva",
                    "Serve per pubblicare i volti degli utenti su canali di intrattenimento comico",
                    "Viene utilizzata per monitorare la produttività oraria dei dipendenti dell'ufficio",
                    "Costituisce un archivio giudiziario segreto per le forze dell'ordine"
                ],
                "correctIndex": 0,
                "explanation": "Il video batte cento slide: montare una clip di 2 minuti in cui 4 utenti consecutivi non riescono a trovare il pulsante 'Paga' convince il manager più ostinato molto più di qualsiasi relazione scritta."
            },
            {
                "question": "Cosa si intende per 'Debriefing' collegiale al termine della giornata di test di usabilità?",
                "options": [
                    "Una riunione immediata del team di prodotto per confrontare le note osservate, stilare l'elenco dei 3 problemi di usabilità più gravi e concordare le soluzioni da implementare subito",
                    "La consegna dei premi in denaro ai partecipanti che non hanno commesso errori",
                    "La pulizia e sanificazione dei locali del laboratorio con detergenti industriali",
                    "La cancellazione di tutte le registrazioni audio e video dai server aziendali"
                ],
                "correctIndex": 0,
                "explanation": "A caldo, prima che i ricordi svaniscano: ci si riunisce attorno a una lavagna, si raggruppano gli ostacoli visti e si decide il piano d'azione per risolverli prima della sessione del mese successivo."
            }
        ],
        "examQuiz": [
            {
                "question": "Un osservatore interno all'azienda (es. lo sviluppatore capo) siede dietro al partecipante durante il test e sbotta: 'Ma no, è ovvio che devi cliccare in alto a destra!'. Quale errore letale ha commesso e come si previene?",
                "options": [
                    "Ha violato la neutralità e invalidato il test umiliando l'utente; si previene isolando gli osservatori in una stanza separata con specchio unidirezionale o collegamento video in streaming silenzioso",
                    "Ha fatto bene perché l'utente stava sprecando il tempo del team di sviluppo",
                    "Lo sviluppatore deve essere nominato facilitatore unico di tutte le sessioni future",
                    "L'utente deve essere multato per aver provocato la rabbia del personale tecnico"
                ],
                "correctIndex": 0,
                "explanation": "Regola aurea: chi ha creato il software soffre fisicamente nel vedere un estraneo che non capisce. Gli osservatori devono stare muti, preferibilmente dietro uno schermo remoto, con microfono disattivato."
            },
            {
                "question": "Qual è la differenza fondamentale tra 'Fallimento del Task' (Task Failure) e 'Difficoltà Temporanea' (Struggle)?",
                "options": [
                    "Nel fallimento l'utente si arrende definitivamente, dichiara concluso il compito avendo sbagliato o abbandona; nella difficoltà l'utente incontra intoppi o esitazioni ma riesce infine a raggiungere l'obiettivo autonomamente",
                    "Il fallimento riguarda solo i siti web e la difficoltà solo le applicazioni mobili",
                    "La difficoltà comporta una riduzione dello stipendio del ricercatore",
                    "Non sussiste alcuna distinzione metodologica, essendo considerati eventi identici"
                ],
                "correctIndex": 0,
                "explanation": "Entrambi sono preziosi: il fallimento è un blocco critico letale (Showstopper); lo struggle segnala frizione cognitiva e consumo di pazienza che, se accumulati, portano all'abbandono futuro."
            },
            {
                "question": "Perché quando si reclutano i partecipanti per un test di usabilità è preferibile selezionare persone che rappresentino i comportamenti d'uso reali anziché amici o colleghi d'ufficio?",
                "options": [
                    "Perché amici e colleghi conoscono già l'azienda, hanno un bias di cortesia enorme e condividono lo stesso gergo interno, fornendo un quadro falsato e illusorio della reale facilità d'uso",
                    "Perché la legge vieta di far testare i software a persone con cui si hanno rapporti di parentela",
                    "Perché i colleghi d'ufficio chiedono compensi economici doppi rispetto agli estranei",
                    "Perché gli amici non sanno utilizzare il mouse del computer con sufficiente precisione"
                ],
                "correctIndex": 0,
                "explanation": "Mai testare con la mamma o il collega della porta accanto: non vorranno ferirvi e conoscono già il contesto. Servono perfetti sconosciuti che rappresentino il target e non abbiano alcuna pietà nel dire cosa non funziona."
            }
        ]
    },
    "stull-c34": {
        "quiz": [
            {
                "question": "Cosa caratterizza un 'Test di Usabilità Non Moderato e da Remoto' (Unmoderated Remote Usability Test)?",
                "options": [
                    "I partecipanti svolgono i compiti assegnati autonomamente dal proprio computer o telefono, guidati da una piattaforma software che registra schermo, voce e webcam senza la presenza di un ricercatore in tempo reale",
                    "Un test condotto unicamente tramite onde radio da stazioni spaziali orbitanti",
                    "Un questionario cartaceo inviato per posta ordinaria senza busta di ritorno",
                    "Un colloquio telefonico condotto da un operatore commerciale di telemarketing"
                ],
                "correctIndex": 0,
                "explanation": "Piattaforme come UserTesting o Maze: caricate il prototipo e le domande; 50 persone in tutto il mondo svolgono la prova a casa loro e in poche ore avete registrazioni video e metriche pronte."
            },
            {
                "question": "Qual è il principale VANTAGGIO dei test di usabilità non moderati da remoto?",
                "options": [
                    "Rapidità estrema di raccolta dati, costi scalabili inferiori, campioni ampi e diversificati geograficamente, e svolgimento nel reale contesto d'uso domestico/lavorativo dell'utente",
                    "L'impossibilità totale per gli utenti di incontrare bug o rallentamenti",
                    "La certezza matematica che nessun partecipante mentirà mai durante le risposte",
                    "La possibilità di controllare a distanza il mouse del computer dell'utente"
                ],
                "correctIndex": 0,
                "explanation": "Scalabilità e realismo: testare contemporaneamente su 100 utenti in 5 fusi orari diversi mentre usano il proprio computer reale, con la propria connessione di casa, in meno di 24 ore."
            },
            {
                "question": "Qual è invece il principale LIMITE o svantaggio dei test non moderati rispetto a quelli moderati?",
                "options": [
                    "L'impossibilità per il ricercatore di fare domande di approfondimento su comportamenti imprevisti, di chiarire fraintendimenti del compito o di confortare l'utente se si blocca in un vicolo cieco",
                    "L'obbligo di pagare tasse doganali su tutti i video registrati all'estero",
                    "Il divieto legale di utilizzare la connessione Wi-Fi per la trasmissione dei dati",
                    "Il consumo eccessivo di carta per stampare i report automatici"
                ],
                "correctIndex": 0,
                "explanation": "Manca l'interazione umana: se l'utente capisce male il testo del compito o si blocca su un punto stupido, non potete intervenire con una domanda chiarificatrice, e l'intera sessione rischia di andare perduta."
            },
            {
                "question": "Come devono essere formulati i compiti in un test non moderato per evitare che i partecipanti si blocchino o fraintendano?",
                "options": [
                    "Devono essere chiarissimi, atomici, autoesplicativi, lineari e collaudati con un test pilota preliminare (Pilot Test) prima del lancio sul campione completo",
                    "Devono essere formulati con enigmi filosofici per stimolare la concentrazione",
                    "Devono contenere almeno quaranta righe di istruzioni per ciascuna schermata",
                    "Devono essere scritti interamente in lettere maiuscole con caratteri gotici"
                ],
                "correctIndex": 0,
                "explanation": "Nessuno potrà chiarire i dubbi: se la consegna è ambigua, 50 persone faranno la cosa sbagliata. Il 'Pilot Test' su un solo utente è obbligatorio per verificare che la consegna sia a prova di bomba."
            },
            {
                "question": "Quale tipologia di indagine è particolarmente idonea per i test non moderati da remoto?",
                "options": [
                    "Task specifici, flussi chiusi e quantificabili (es. completare un acquisto, trovare un'informazione specifica), test di primo clic (First Click Testing) e alberi di navigazione (Tree Testing)",
                    "Interviste esplorative intime sulle paure e i traumi esistenziali dell'utente",
                    "Sessioni di brainstorming creativo di gruppo della durata di otto ore",
                    "La stipula di contratti di fusione societaria tra grandi banche"
                ],
                "correctIndex": 0,
                "explanation": "Perfetti per compiti circoscritti e misurabili: misurare tempi sul task, tassi di successo e percorsi di clic su flussi definiti senza bisogno di una guida umana costante."
            }
        ],
        "examQuiz": [
            {
                "question": "In un test non moderato su un prototipo Figma complesso, il 60% degli utenti abbandona al secondo step perché il prototipo non supporta lo scorrimento orizzontale su Safari mobile. Quale lezione metodologica ne deriva?",
                "options": [
                    "Nei test non moderati i prototipi devono essere collaudati tecnicamente su tutti i browser e dispositivi target prima del lancio, e i percorsi interattivi devono essere blindati contro i vicoli ciechi",
                    "Gli utenti di Safari mobile devono essere esclusi da tutte le ricerche future",
                    "I prototipi Figma non possono essere utilizzati per test da remoto",
                    "Il team deve abbandonare la metodologia UX per tornare allo sviluppo a cascata"
                ],
                "correctIndex": 0,
                "explanation": "Un intoppo tecnico invisibile in laboratorio distrugge i test non moderati: senza un facilitatore che dica 'È un limite del prototipo, clicca qui', l'utente pensa che sia rotto e chiude la sessione."
            },
            {
                "question": "Cosa si intende per 'Tester Professionisti' (Professional Panelists) nelle piattaforme di test non moderati e quale rischio comportano?",
                "options": [
                    "Utenti che partecipano a decine di test alla settimana per guadagnare compensi economici, sviluppando una familiarità artificiale con i gerghi e i pattern UX che non rispecchia l'ingenuità del pubblico reale",
                    "Ingegneri informatici stipendiati dal ministero delle telecomunicazioni",
                    "Artisti digitali che creano video musicali durante le prove di usabilità",
                    "Hacker internazionali che tentano di rubare i dati delle aziende committenti"
                ],
                "correctIndex": 0,
                "explanation": "Il bias dei 'panelisti seriali': sanno già come parlare al microfono, sanno cos'è un hamburger menu e sanno cosa il ricercatore vuole sentirsi dire. Serve uno screening accurato per reclutare utenti autentici."
            },
            {
                "question": "Come si combinano virtuosamente test moderati e test non moderati in un processo di ricerca solido?",
                "options": [
                    "Si conducono prima 5 test moderati per comprendere a fondo le dinamiche qualitative e rifinire il flusso, e poi si lanciano 50-100 test non moderati per quantificare e validare la soluzione su larga scala",
                    "Si alternano i due metodi a giorni pari e giorni dispari della settimana",
                    "Si utilizzano i test moderati solo per le donne e i non moderati solo per gli uomini",
                    "Si utilizzano i test non moderati solo quando il budget aziendale è pari a zero"
                ],
                "correctIndex": 0,
                "explanation": "La combinazione perfetta: il moderato dà profondità umana ed empatia (scopri gli ostacoli); il non moderato dà numeri e scala statistica (confermi che la correzione funziona per il 90% degli utenti)."
            }
        ]
    }
}

with open("scripts/stull_part7.json", "w", encoding="utf-8") as f:
    json.dump(stull_c29_to_34, f, indent=2, ensure_ascii=False)

print(f"Salvata tranche capitoli 29-34 ({len(stull_c29_to_34)} capitoli)")
