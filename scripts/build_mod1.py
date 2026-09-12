# -*- coding: utf-8 -*-
import json

partNum = 1
partTitle = "1. Arte Contemporanea Anni '50: Informale, Espressionismo Astratto e Spazialismo"
module = "anni50"

# We will read C1, C2, C3 from scripts/mod1_data.py
import sys
sys.path.insert(0, "scripts")
import mod1_data
chaps = mod1_data.get_mod1_chapters() # has c1, c2, c3

# C4: Wols
chaps.append({
    "id": "arte1-c4",
    "number": 4,
    "partNum": partNum,
    "partTitle": partTitle,
    "module": module,
    "title": "Wols e l'Informale Segnico: Il Dolore Esistenziale e il Tachisme",
    "subtitle": "La parabola tragica di Alfred Otto Wolfgang Schulze: il segno febbrile, la macchia organica e l'angoscia della reclusione",
    "summary": """### 1. Dati biografici e la parabola tragica di Alfred Otto Wolfgang Schulze\n\nNato a Berlino nel 1913 da una colta famiglia alto-borghese, Alfred Otto Wolfgang Schulze assume lo pseudonimo contratto di **Wols** nel 1937 a Parigi, dove si era rifugiato per fuggire dall'oppressione del regime nazista. Spirito inquieto, fotografo visionario, musicista e poeta maledetto, allo scoppio della Seconda Guerra Mondiale viene arrestato dalle autorità francesi in quanto cittadino tedesco e internato in vari campi di concentramento (tra cui il celebre campo di Les Milles vicino ad Aix-en-Provence), vivendo anni di stenti fisici, freddo e disperazione psichica.\n\nLiberato dopo l'armistizio, vive da rifugiato clandestino a Dieulefit e poi a Parigi, sprofondando nell'alcolismo cronico e nella miseria materiale. Nel 1945 e nel 1947 espone alla Galerie René Drouin i suoi piccoli acquerelli e dipinti: la mostra sconvolge la scena intellettuale parigina, venendo salutata con devozione da Jean-Paul Sartre, Simone de Beauvoir e Henri Michaux. Wols muore tragicamente a Parigi nel 1951 a soli trentotto anni per avvelenamento da cibo avariato combinato a cirrosi epatica, incarnando la figura archetipica del martire esistenziale del dopoguerra.\n\n---\\n\n### 2. Il Tachisme, il microcosmo e la pulsione segnica\n\nWols è considerato il padre fondatore del **Tachisme** (dal francese *tache*, macchia):\n* **Il rifiuto del grande formato**: A differenza dell'enfasi eroica dei maestri americani, Wols lavora inizialmente su fogli microscopici di carta, spesso consumati dall'umidità o intrisi di vino e tabacco.\n* **La macchia germinale**: Versa l'acquerello liquido o l'inchiostro sul supporto, lasciando che il pigmento si espanda per capillarità e si asciughi in pozze concentriche, aloni biologici e grumi casuali che evocano cellule al microscopio, ferite infette o formazioni batteriche.\n* **La ragnatela grafica febbrile**: Sopra e dentro la macchia umida, con un pennino acuminato intinto nell'inchiostro nero, traccia un reticolo fittissimo di segni vibranti, graffi, filamenti nervosi, peli, uncini e cicatrici.\n* **L'automatismo della sofferenza**: Il gesto di Wols non è un gioco formale; è una sismografia interiore dell'angoscia, una registrazione compulsiva del panico di fronte alla minaccia del nulla cosmico.\n\n---\\n\n### 3. Analisi delle opere cardine\n\n#### Composizione / La Farfalla Spuntata (*Composition*, 1946-1947)\n* **Descrizione e impianto ottico**: Un nucleo cromatico centrale denso e viscerale (rosso cupo, ocra putrido, grigio plumbeo) da cui si diramano filamenti neri aggrovigliati come vasi capillari o ragnatele lacerate. La materia pittorica è raschiata, spruzzata, colata.\n* **Significato iconologico**: L'opera non illustra un oggetto del mondo esterno; è un autoritratto ontologico dell'anima scorticata. La tela si presenta come un occhio malato, un utero ferito o un'esplosione stellare in miniatura: il microcosmo interiore dell'artista coincide drammaticamente con il macrocosmo di un'Europa dilaniata dal conflitto.\n* **Ricezione critica**: Sartre dedicò a Wols saggi memorabili, ravvisando nei suoi intrichi grafici la visualizzazione suprema della 'nausea' e dell'essere-per-la-morte.""",
    "keyPoints": [
        "Wols (Alfred Otto Wolfgang Schulze) è il padre fondatore del Tachisme e figura cardine dell'Informale segnico europeo.",
        "La sua vita è segnata dalla fuga dal nazismo, dall'internamento nei campi di concentramento e da una tragica fine a 38 anni.",
        "La sua tecnica unisce la macchia liquida casuale (tache) a una trama fittissima di segni febbrili incisi a pennino.",
        "Le sue opere di piccolo formato evocano microcosmi biologici, cellule lacerate e la sismografia dell'angoscia esistenziale."
    ],
    "flashcards": [
        {"question": "Quale artista è universalmente considerato il padre fondatore del 'Tachisme'?", "answer": "Wols (pseudonimo di Alfred Otto Wolfgang Schulze).", "front": "Quale artista è universalmente considerato il padre fondatore del 'Tachisme'?", "back": "Wols (pseudonimo di Alfred Otto Wolfgang Schulze)."},
        {"question": "Cosa significa letteralmente il termine 'Tachisme'?", "answer": "Pittura a macchie (dal francese 'tache', macchia), caratterizzata da stesure liquide spontanee ed esplosioni segniche.", "front": "Cosa significa letteralmente il termine 'Tachisme'?", "back": "Pittura a macchie (dal francese 'tache', macchia), caratterizzata da stesure liquide spontanee ed esplosioni segniche."},
        {"question": "Quale tragica esperienza biografica segnò la produzione di Wols durante la Seconda Guerra Mondiale?", "answer": "L'arresto e l'internamento nei campi di concentramento francesi (come Les Milles) in quanto profugo tedesco.", "front": "Quale tragica esperienza biografica segnò la produzione di Wols durante la Seconda Guerra Mondiale?", "back": "L'arresto e l'internamento nei campi di concentramento francesi (come Les Milles) in quanto profugo tedesco."},
        {"question": "Quale grande filosofo esistenzialista scrisse saggi fondamentali sull'opera di Wols?", "answer": "Jean-Paul Sartre.", "front": "Quale grande filosofo esistenzialista scrisse saggi fondamentali sull'opera di Wols?", "back": "Jean-Paul Sartre."},
        {"question": "Quali elementi grafici caratterizzano il linguaggio visivo degli acquerelli di Wols?", "answer": "Macchie concentriche di colore liquido solcate da ragnatele di segni febbrili, graffi e filamenti tracciati a pennino.", "front": "Quali elementi grafici caratterizzano il linguaggio visivo degli acquerelli di Wols?", "back": "Macchie concentriche di colore liquido solcate da ragnatele di segni febbrili, graffi e filamenti tracciati a pennino."}
    ],
    "openQuestions": [
        "Analizzate il rapporto tra la dimensione microcosmica del segno di Wols e la filosofia della 'nausea' di Sartre.",
        "Descrivete l'evoluzione tecnica che conduce Wols dalla fotografia visionaria degli anni Trenta all'invenzione del Tachisme."
    ],
    "quiz": [
        {"question": "Qual era il vero nome di Wols?", "options": ["Alfred Otto Wolfgang Schulze", "Hans Hartung", "Georges Mathieu", "Jean Fautrier"], "correctIndex": 0, "explanation": "Wols nacque a Berlino come Alfred Otto Wolfgang Schulze, abbreviando il nome a Parigi nel 1937."},
        {"question": "In quale celebre galleria parigina Wols espose nel 1945 e nel 1947?", "options": ["Galerie René Drouin", "Galerie Denise René", "Leo Castelli Gallery", "Galerie Maeght"], "correctIndex": 0, "explanation": "René Drouin fu il mecenate che espose sia Fautrier, sia Dubuffet, sia Wols negli anni quaranta."},
        {"question": "Cosa evocano visivamente le strutture al centro dei quadri di Wols?", "options": ["Cellule biologiche, forme organiche microscopiche, ragnatele e ferite aperte", "Grattacieli newyorkesi e ponti industriali", "Composizioni geometriche ortogonali a colori primari", "Ritratti realistici di gerarchi militari"], "correctIndex": 0, "explanation": "I nuclei di Wols appaiono come visioni biologiche al microscopio intrise di pulsione e dolore."},
        {"question": "Quale formato prediligeva Wols per i suoi lavori più celebri?", "options": ["Piccole carte, acquerelli e formati intimi e ridotti", "Tele lunghe oltre venti metri per pareti museali", "Sculture colossali in marmo di Carrara", "Cartelloni pubblicitari urbani per Times Square"], "correctIndex": 0, "explanation": "La ricerca di Wols è intimista e concentrata in fogli minuti solcati da tratti fittissimi."},
        {"question": "A quale età morì tragicamente Wols a Parigi nel 1951?", "options": ["38 anni", "75 anni", "21 anni", "55 anni"], "correctIndex": 0, "explanation": "Wols morì a soli trentotto anni, consumato dagli stenti, dall'alcol e da un'intossicazione alimentare."}
    ],
    "examQuiz": [
        {"question": "Quale differenza concettuale sussiste tra l'automatismo psichico surrealista di André Masson e il segno tachiste di Wols?",
        "options": [
            "Il Surrealismo cercava la liberazione gioiosa o onirica dell'inconscio freudiano; Wols registra l'angoscia esistenziale, il panico e l'isolamento claustrofobico dell'individuo senza illusioni redentive",
            "Wols utilizzava esclusivamente il computer per tracciare linee algebriche",
            "Masson rifiutava l'uso dell'inchiostro privilegiando la pittura a cera",
            "Non vi è alcuna differenza, essendo Wols il segretario ufficiale del movimento surrealista"
        ],
        "correctIndex": 0,
        "explanation": "In Wols l'automatismo si spoglia dell'ottimismo rivoluzionario surrealista per farsi traccia disperata dell'angoscia post-bellica."},
        {"question": "In che termini la critica ha collegato la fotografia d'anteguerra di Wols alla sua successiva pittura informale?",
        "options": [
            "Nelle fotografie parigine Wols isolava dettagli macroscopici e frammenti marginali (vetrine, carcasse, ciottoli), anticipando l'attenzione per la micro-materia organica della pittura",
            "Le fotografie erano copie perfette delle statue di Canova",
            "Wols dipingeva solo ingrandendo i ritratti fotografici di famiglia",
            "La fotografia fu una parentesi commerciale del tutto slegata dalla pittura"
        ],
        "correctIndex": 0,
        "explanation": "L'occhio fotografico di Wols indagava l'usura, i riflessi liquidi e gli scarti, fondando la sua sensibilità materica."},
        {"question": "Quale ruolo attribuisce Sartre al 'vuoto' che circonda il nucleo centrale nelle tele di Wols?",
        "options": [
            "Rappresenta il nulla minaccioso dell'esistenza che assedia la fragilità della materia viva",
            "Uno spazio lasciato libero per appunti manoscritti degli acquirenti",
            "Una mancata finitura dovuta alla pigrizia dell'artista",
            "L'imitazione delle cornici dei codici miniati medioevali"
        ],
        "correctIndex": 0,
        "explanation": "Il margine vuoto e sgranato isola il groviglio centrale nel nulla circostante, visualizzando l'esistenzialismo."},
        {"question": "Come si colloca la pittura di Wols rispetto all'Action Painting americana di Pollock?",
        "options": [
            "Mentre Pollock esprime l'energia fisica espansiva e il gigantismo dello spazio americano (all-over), Wols esprime l'introversione tragica, la compressione e la ferita dell'Europa devastata",
            "Wols fu l'allievo diretto di Pollock a New York",
            "Entrambi usavano barattoli forati stesi a terra su tele monumentali",
            "Pollock imitava gli acquerelli microscopici di Wols senza variarne le dimensioni"
        ],
        "correctIndex": 0,
        "explanation": "Pollock è scala monumentale e dinamismo cosmico; Wols è concentrazione introspettiva e sofferenza claustrofobica."},
        {"question": "Quale saggio critico consacrò Wols tra i massimi esponenti dell'Informale europeo?",
        "options": [
            "Il capitolo dedicatogli da Michel Tapié in 'Un art autre' (1952)",
            "Il primo manifesto del Futurismo su Le Figaro",
            "Il saggio The American Action Painters di Harold Rosenberg",
            "La recensione della mostra dei Fauves al Salon d'Automne del 1905"
        ],
        "correctIndex": 0,
        "explanation": "Tapié lo definì la figura più folgorante e pura dell'Informale europeo del dopoguerra."}
    ]
})

print("Added C4: Wols. Total chapters:", len(chaps))
