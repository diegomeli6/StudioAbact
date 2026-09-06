# build_full_database.py
import re, json

print("Inizio costruzione database completo di studio approfondito...")

# 1. GENERAZIONE GLOSSARIO UNIFICATO
with open('extracted_stull.txt', 'r', encoding='utf-8') as f:
    stull_raw = f.read()

with open('extracted_krug.txt', 'r', encoding='utf-8') as f:
    krug_raw = f.read()

# Estrarre glossario Stull (Section A)
pos_g_stull = stull_raw.rfind('A. Glossario ragionato')
pos_g_end = stull_raw.rfind('B. Leggi, modelli')
gloss_stull_chunk = stull_raw[pos_g_stull:pos_g_end] if (pos_g_stull != -1 and pos_g_end != -1) else ""

# Estrarre glossario Krug (Appendice B)
pos_g_krug = krug_raw.find('Appendice\tB')
pos_g_krug_end = krug_raw.find('Appendice\tC')
gloss_krug_chunk = krug_raw[pos_g_krug:pos_g_krug_end] if (pos_g_krug != -1 and pos_g_krug_end != -1) else ""

unified_glossary = [
    # Krug
    {"term": "Satisficing", "source": "Krug / Stull", "def": "Scegliere la prima opzione ragionevole anziché la migliore in assoluto (concetto di Herbert Simon). È il comportamento tipico e naturale degli utenti web che cercano un buon risultato con il minimo sforzo cognitivo."},
    {"term": "Muddling through (Arrangiarsi)", "source": "Krug", "def": "Usare interfacce, software e siti web senza comprendere come funzionano internamente, costruendosi modelli empirici e spiegazioni plausibili purché consentano di raggiungere l'obiettivo."},
    {"term": "Scent of information (Odore dell'informazione)", "source": "Krug / Stull", "def": "Indizio visivo o testuale (etichetta di un link, icona) che segnala in modo chiaro dove conduce e quanto è promettente il contenuto della pagina di destinazione (teoria del foraging di Pirolli e Card)."},
    {"term": "Trunk Test (Test del bagagliaio)", "source": "Krug", "def": "Protocollo di valutazione rapido per verificare se un utente 'catapultato' su una pagina interna casuale riesce a rispondere in 5 secondi a: Di che sito si tratta? Che pagina è? Quali sono le sezioni primarie? Quali sono le opzioni qui? Dove sono rispetto al tutto? Come cerco?"},
    {"term": "Thinking Aloud (Pensare ad alta voce)", "source": "Krug / Stull", "def": "Metodo cardine del test di usabilità qualitativo: chiedere al partecipante di verbalizzare spontaneamente ogni pensiero, dubbio, esitazione o aspettativa durante lo svolgimento dei compiti assegnati."},
    {"term": "Reservoir of Goodwill (Serbatoio della buona volontà)", "source": "Krug", "def": "Metafora della riserva limitata di pazienza e benevolenza che l'utente porta con sé. Si svuota con ostacoli, formati rigidi e popup; si riempie con trasparenza, scorciatoie e messaggi di errore costruttivi."},
    {"term": "Happy talk", "source": "Krug", "def": "Testi introduttivi autocelebrativi e privi di informazioni concrete (es. 'Benvenuti nel nostro sito...'). Rallentano la scansione e vanno sistematicamente eliminati."},
    {"term": "Navigazione persistente", "source": "Krug", "def": "Insieme di elementi di navigazione presenti in ogni pagina del sito: Site ID (logo cliccabile), sezioni primarie, utility, casella di ricerca e indicatore 'Tu sei qui'."},
    {"term": "Banner blindness (Cecità ai banner)", "source": "Krug", "def": "Tendenza inconscia degli utenti a ignorare del tutto le porzioni dello schermo che per posizione o grafica assomigliano a messaggi pubblicitari."},
    {"term": "Prima Legge di Krug", "source": "Krug", "def": "'Non farmi pensare!'. Ogni pagina dovrebbe risultare autoevidente o almeno autoesplicativa senza richiedere sforzo conscio di decifrazione."},
    {"term": "Seconda Legge di Krug", "source": "Krug", "def": "Non conta quante volte devo cliccare, purché ogni clic sia una scelta ovvia e priva di ambiguità (3 clic senza pensiero equivalgono o battono 1 clic difficile)."},
    {"term": "Terza Legge di Krug", "source": "Krug", "def": "Elimina metà delle parole di ogni pagina, poi elimina metà di ciò che resta. Riduce il rumore visivo ed esalta i contenuti di reale valore."},
    
    # Dispense Professore
    {"term": "Layout (metafora di Falcinelli)", "source": "Dispense", "def": "Disposizione e organizzazione nello spazio di elementi e oggetti. Falcinelli lo paragona all'apparecchiare una tavola: una disposizione ordinata e funzionale che comunica subito senso e modalità d'uso."},
    {"term": "Contrasto", "source": "Dispense", "def": "Principio di composizione grafica: se due elementi svolgono ruoli diversi o hanno pesi gerarchici differenti, devono essere resi visivamente molto diversi per dimensione, peso, colore o forma."},
    {"term": "Prossimità (Gestalt)", "source": "Dispense / Stull", "def": "Gli elementi spazialmente vicini vengono percepiti automaticamente dal cervello come appartenenti alla stessa unità logico-concettuale."},
    {"term": "Spazio bianco (Negative Space)", "source": "Dispense", "def": "L'area vuota attorno e tra gli elementi di design. Non è spazio perso ma un elemento attivo che dona respiro, riduce l'affaticamento e guida l'occhio sui punti focali."},
    {"term": "Allineamento", "source": "Dispense", "def": "Disposizione degli elementi lungo assi orizzontali e verticali condivisi; genera coerenza, pulizia e ritmo visivo."},
    {"term": "Typeface vs Font", "source": "Dispense", "def": "Typeface è il disegno della famiglia di caratteri (es. Helvetica); Font è l'istanza o file digitale specifico a un determinato corpo e peso (es. Helvetica Bold a 16px)."},
    {"term": "x-height (Altezza delle x)", "source": "Dispense", "def": "Altezza delle lettere minuscole prive di aste ascendenti e discendenti. Un'ampia x-height favorisce notevolmente la leggibilità sui display digitali."},
    {"term": "Design System", "source": "Dispense", "def": "Insieme organizzato di standard, linee guida visive e componenti riutilizzabili codificati (UI token, bottoni, card, form) condiviso tra designer e sviluppatori per garantire coerenza."},
    {"term": "Style Tile", "source": "Dispense", "def": "Artefatto visivo ideato da Samantha Warren: via di mezzo tra moodboard e mockup finito, raccoglie palette, font reali, bottoni e texture per concordare lo stile grafico con il committente."},
    {"term": "Box Model (CSS)", "source": "Dispense", "def": "Modello di calcolo dello spazio degli elementi HTML: Content (contenuto) racchiuso da Padding (spazio interno), Border (bordo) e Margin (spazio esterno)."},
    {"term": "Mobile First", "source": "Dispense", "def": "Strategia progettuale e di sviluppo che parte dai vincoli dello schermo mobile, arricchendo progressivamente il layout per desktop tramite media queries min-width."},
    {"term": "Client vs Server", "source": "Dispense", "def": "Il Client (browser) esegue JavaScript per l'interfaccia e l'interattività immediata; il Server elabora dati protetti, database, autenticazione e sicurezza persistente."},
    
    # Stull UX Design
    {"term": "Affordance e Signifier", "source": "Stull / Krug", "def": "L'affordance è la proprietà reale o percepita di un oggetto che ne indica l'uso possibile (Gibson/Norman); il signifier (segnalatore) è l'indizio visivo esplicito (es. forma a bottone in rilievo) che rende palese l'azione."},
    {"term": "Legge di Hick-Hyman (1952)", "source": "Stull", "def": "Il tempo necessario per prendere una decisione logaritmica cresce all'aumentare del numero di opzioni disponibili: T = b * log2(n + 1). Limitare le scelte riduce l'affaticamento decisionale."},
    {"term": "Legge di Fitts (1954)", "source": "Stull", "def": "Il tempo per raggiungere un bersaglio dipende dalla distanza e dalla dimensione del bersaglio. Bersagli più grandi e più vicini sono più facili e veloci da cliccare o toccare."},
    {"term": "Modello di Kano (Noriaki Kano, 1984)", "source": "Stull", "def": "Modello di soddisfazione cliente che distingue tre categorie di attributi: Di base (must-be, scontati ma critici se assenti), Prestazionali (lineari, più ce n'è meglio è), Deliziatori (inattesi, generano entusiasmo ma subiscono l'erosione del piacere nel tempo)."},
    {"term": "ELM (Elaboration Likelihood Model - Petty e Cacioppo, 1986)", "source": "Stull", "def": "Modello di persuasione a due percorsi: Percorso Centrale (analisi logica e razionale degli argomenti, richiede alta motivazione) e Percorso Periferico (euristiche rapide, appeal estetico, testimonial e indizi superficiali)."},
    {"term": "Sistema 1 e Sistema 2 (Daniel Kahneman)", "source": "Stull", "def": "Sistema 1: veloce, automatico, impulsivo, a basso consumo energetico (il pilota automatico che usiamo sul web). Sistema 2: lento, riflessivo, calcolatore ed energivoro. La pigrizia cognitiva dell'utente protegge il Sistema 2."},
    {"term": "Just Noticeable Difference (JND - Ernst Weber)", "source": "Stull", "def": "La differenza minima percettibile tra due stimoli sensoriali. Nel redesign si usa una JND bassa per aggiornare l'interfaccia senza disorientare gli utenti storici."},
    {"term": "Curva di adozione di Rogers (1962)", "source": "Stull", "def": "Modello di diffusione delle innovazioni: Innovatori (2.5%), Primi Adottanti (13.5%), Maggioranza Precoce (34%), Maggioranza Tardiva (34%), Ritardatari (16%)."},
    {"term": "Il Chasm di Moore (Crossing the Chasm, 1991)", "source": "Stull", "def": "Il baratro o abisso che separa i Primi Adottanti (visionari amanti della novità tecnologica) dalla Maggioranza Precoce (pragmatici che pretendono soluzioni stabili, referenziate e facili da usare)."},
    {"term": "Maledizione della conoscenza (Curse of Knowledge)", "source": "Stull", "def": "Bias cognitivo per cui un esperto che padroneggia perfettamente un sistema non riesce più a immaginare quanto quel sistema risulti incomprensibile e difficile per un neofita."},
    {"term": "Wicked Problems (Problemi complessi / intrattabili)", "source": "Stull", "def": "Problemi mal definiti, interconnessi e privi di una soluzione finale assoluta (Rittel e Webber, 1973). Si affrontano non con soluzioni definitive ma con l'incrementalismo e la conciliazione continua."},
    {"term": "Effetto Kuleshov (1918)", "source": "Stull", "def": "Fenomeno psicologico per cui la percezione e il significato di un'immagine sono radicalmente influenzati da ciò che viene mostrato immediatamente prima o dopo. Nell'UX, l'ordine sequenziale modifica l'interpretazione dello stimolo."},
    {"term": "Effetto alone (Halo Effect - Edward Thorndike, 1920)", "source": "Stull", "def": "Tendenza cognitiva a generalizzare un singolo tratto positivo (es. una grafica elegante o una schermata pulita) all'intero prodotto, giudicandolo intuitivo e sicuro anche quando ha difetti funzionali."},
    {"term": "MVP (Minimum Viable Product)", "source": "Stull", "def": "La versione minima di un prodotto sufficiente a raccogliere il massimo apprendimento validato dagli utenti reali con il minimo sforzo. Il suo limite è che se è troppo rozzo non offre una reale utilità né soddisfazione."}
]

with open('data/glossary-data.js', 'w', encoding='utf-8') as f:
    f.write(f"// Glossario ragionato unificato dei 3 testi di studio\nwindow.GLOSSARY_DATA = {json.dumps(unified_glossary, indent=2, ensure_ascii=False)};\n")

print(f"data/glossary-data.js generato con {len(unified_glossary)} termini unificati.")
