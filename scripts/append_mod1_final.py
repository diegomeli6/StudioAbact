import json
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "scripts")
import append_mod1_part6
chaps = append_mod1_part6.chaps
partNum = 1
partTitle = "1. Arte Contemporanea Anni '50: Informale, Espressionismo Astratto e Spazialismo"
module = "anni50"

# C15: Enrico Baj
chaps.append({
    "id": "arte1-c15",
    "number": 15,
    "partNum": partNum,
    "partTitle": partTitle,
    "module": module,
    "title": "Enrico Baj e l'Arte Nucleare: L'Ironia Grottesca dei Generali",
    "subtitle": "La fondazione del Movimento Arte Nucleare (1951), l'incubo di Hiroshima e la satira feroce del potere militare",
    "summary": """### 1. Dati biografici e la fondazione del Movimento Arte Nucleare (Milano, 1951)\n\nNato a Milano nel 1924 da una colta famiglia borghese, **Enrico Baj** si laurea in giurisprudenza all'Università degli Studi di Milano e contemporaneamente si diploma all'Accademia di Belle Arti di Brera. Nel clima di angoscia collettiva suscitato dalla Guerra Fredda e dalla proliferazione degli arsenali termonucleari, nel 1951 fonda a Milano insieme a **Sergio Dangelo** il **Movimento Arte Nucleare** (a cui aderiranno successivamente anche Gianni Dova, Roberto Crippa e Joe Colombo):\n* **Il Manifesto della Pittura Nucleare (1952)**: I firmatari proclamano che, dopo l'avvento dell'era atomica, la pittura non può più imitare la realtà statica né indulgere in accademismi. Le forme devono disintegrarsi ed esplodere come l'atomo: *«I Nucleari vogliono abbattere tutti gli 'ismi' di una pittura che cade inevitabilmente nel manierismo. Vogliamo e possiamo reinventare la pittura: la materia non deve essere sottomessa a regole, ma sprigionare la propria energia termonucleare»*.\n* **Le prime sperimentazioni**: Negli anni Cinquanta Baj sperimenta colature fluide di smalti sintetici lucidi, polveri di metallo, polverizzazioni pesanti e impasti di sabbia, evocando paesaggi devastati dal fungo atomico e popolati da mostruose creature mutanti (*Uccelli atomici*, *Paesaggi nucleari*).\n\n---\\n\n### 2. La satira del potere: La serie monumentale dei Generali\n\nVerso la fine degli anni Cinquanta, Baj compie un passaggio decisivo: dall'astrazione materica dell'esplosione atomica approda a una **feroce, ironica e grottesca satira del potere politico, militare e autoritario**, inventando la celeberrima serie dei **Generali**:\n* **Il collage polimaterico provocatorio**: Invece della tela tradizionale, Baj utilizza vecchi scampoli di stoffe per materassi, tessuti damascati, broccati ottocenteschi, arazzi logori o carte da parati fiorite comprate nei mercatini delle pulci.\n* **Gli elementi militari feticistici**: Su questi sfondi borghesi e polverosi incolla elementi eterogenei del decoro bellico: vere medaglie d'onore arrugginite, passamanerie dorate, spalline cerimoniali, cordoni da parata, bottoni d'ottone, specchietti, orologi rotti e maniglie di cassetto.\n* **L'antropomorfismo mostruoso**: I volti dei generali sono sagome goffe, panciute e deformi, con occhi spalancati ricavati da bottoni cuciti e bocche ghignanti. Il generale bajano è un mostro infantile e ridicolo: incarna l'ottusità fanatica del potere marziale, la violenza burocratica e la vanità senile dei guerrafondai che trascinano l'umanità verso la catastrofe atomica.\n\n---\\n\n### 3. Analisi delle opere cardine\n\n#### I Generali (1959-1961)\n![Enrico Baj, I Generali / Movimento Arte Nucleare, 1959 - Collage di medaglie e passamanerie su stoffa](assets/corsi/dapl08/anno-1/storia-arte-1/images/baj_arte_nucleare.jpg)\n\n* **Descrizione e composizione**: Un alto graduato militare colossale si erge con torso monumentale coperto da decine di nastrini e medaglie luccicanti. La figura è priva di collo: la testa è un cerchio grezzo sormontato da un pennacchio piumato che ricorda un elmo cerimoniale borbonico o prussiano.\n* **Significato dissacrante**: L'accumulo ossessivo delle medaglie d'onore e dei galloni militari svela l'artificio ridicolo della parata militare. Dietro la pompa dell'uniforme si cela il vuoto morale, l'imbecillità omicida e la mostruosità del comando autoritario.\n\n#### I Funerali dell'anarchico Pinelli (1972)\n* Monumentale polittico lungo dodici metri composto da diciotto figure sagomate in legno dipinto e collage, ispirato a *Guernica* di Picasso e al celebre capolavoro futurista di Carrà. L'opera denuncia la tragica morte dell'anarchico Giuseppe Pinelli, precipitato dalla questura di Milano nel 1969. La mostra a Palazzo Reale fu annullata il giorno stesso dell'inaugurazione (17 maggio 1972) a causa dell'assassinio del commissario Luigi Calabresi, rimanendo una delle opere civili più potenti del Novecento italiano.""",
    "keyPoints": [
        "Enrico Baj fonda a Milano nel 1951 il Movimento Arte Nucleare con Sergio Dangelo, in risposta al terrore della bomba atomica.",
        "Nelle prime opere esplora colature pesanti, polveri e smalti che evocano paesaggi radioattivi e mostri post-nucleari.",
        "Nella serie dei 'Generali' (dal 1959) inventa una satira feroce del potere marziale assemblando medaglie, broccati e passamanerie.",
        "Il capolavoro civile 'I Funerali dell'anarchico Pinelli' (1972) unisce collage e pittura nella memoria tragica della strategia della tensione."
    ],
    "flashcards": [
        {"question": "Quale movimento artistico fondò Enrico Baj a Milano nel 1951 insieme a Sergio Dangelo?", "answer": "Il Movimento Arte Nucleare.", "front": "Quale movimento artistico fondò Enrico Baj a Milano nel 1951 insieme a Sergio Dangelo?", "back": "Il Movimento Arte Nucleare."},
        {"question": "Cosa proclamava il Manifesto della Pittura Nucleare del 1952?", "answer": "La disgregazione della forma artistica in sintonia con l'era atomica e la liberazione dell'energia materica.", "front": "Cosa proclamava il Manifesto della Pittura Nucleare del 1952?", "back": "La disgregazione della forma artistica in sintonia con l'era atomica e la liberazione dell'energia materica."},
        {"question": "Quale serie celebre di dipinti-collage dissacrò il potere militare a partire dal 1959?", "answer": "La serie dei 'Generali'.", "front": "Quale serie celebre di dipinti-collage dissacrò il potere militare a partire dal 1959?", "back": "La serie dei 'Generali'."},
        {"question": "Quali oggetti reali e scarti tessili incollava Baj nei suoi Generali?", "answer": "Medaglie militari autentiche, passamanerie dorate, cordoni, bottoni, broccati e stoffe per materassi.", "front": "Quali oggetti reali e scarti tessili incollava Baj nei suoi Generali?", "back": "Medaglie militari autentiche, passamanerie dorate, cordoni, bottoni, broccati e stoffe per materassi."},
        {"question": "Quale monumentale opera civile di Enrico Baj del 1972 fu censurata a Palazzo Reale a Milano?", "answer": "I Funerali dell'anarchico Pinelli.", "front": "Quale monumentale opera civile di Enrico Baj del 1972 fu censurata a Palazzo Reale a Milano?", "back": "I Funerali dell'anarchico Pinelli."}
    ],
    "openQuestions": [
        "Analizzate come Enrico Baj utilizzi il collage polimaterico e il kitsch tessile come strumenti di feroce satira politica e antimilitarista nella serie dei Generali.",
        "Descrivete il contesto storico della Guerra Fredda che portò alla nascita del Movimento Arte Nucleare a Milano nel 1951."
    ],
    "quiz": [
        {"question": "In quale città fu fondato il Movimento Arte Nucleare nel 1951?", "options": ["Milano", "Roma", "Torino", "Napoli"], "correctIndex": 0, "explanation": "Milano fu la culla del movimento nucleare, promosso da Baj e Dangelo al bar Giamaica di Brera."},
        {"question": "Quale caratteristica accomuna i 'Generali' di Enrico Baj?", "options": ["Figure grottesche coperte da medaglie, passamanerie e bottoni su stoffe da materasso o parati", "Ritratti realistici dei generali dell'armata napoleonica", "Sculture astratte in marmo bianco privo di ornamenti", "Fotografie in posa scattate nelle caserme militari"], "correctIndex": 0, "explanation": "Baj deforma il generale in mostro borioso arricchito di medaglie e nastrini dorati."},
        {"question": "A quale celebre movimento d'avanguardia storico era profondamente legato lo spirito ironico e patafisico di Baj?", "options": ["Al Dadaismo e alla Patafisica di Alfred Jarry", "Al Futurismo marinettiano bellicista", "Al Neoclassicismo canoviano", "Al Realismo magico"], "correctIndex": 0, "explanation": "Baj fu nominato Trascendente Satrapo del Collegio di Patafisica, celebrando l'ironia dadaista."},
        {"question": "Quale evento tragico causò l'annullamento della mostra dei Funerali dell'anarchico Pinelli nel 1972?", "options": ["L'assassinio del commissario Luigi Calabresi poche ore prima dell'inaugurazione", "Un allagamento delle sale di Palazzo Reale", "Il furto dell'opera durante la notte", "La rottura delle cornici lignee"], "correctIndex": 0, "explanation": "L'omicidio Calabresi il 17 maggio 1972 rese la mostra politicamente esplosiva, portando alla sua chiusura preventiva."},
        {"question": "In quale città della provincia di Varese visse e operò a lungo Enrico Baj fino alla morte nel 2003?", "options": ["Leggiuno", "Busto Arsizio", "Gallarate", "Saronno"], "correctIndex": 0, "explanation": "A Leggiuno sul Lago Maggiore Baj aveva la sua celebre dimora-studio e archivio."}
    ],
    "examQuiz": [
        {"question": "In che termini la parodia dell'uniforme nei Generali di Baj smaschera il feticismo dell'autoritarismo militare?",
        "options": [
            "Riduce i simboli del potere (galloni, medaglie, cordoni) a banale chincaglieria da mercatino delle pulci cucita su tessuti da materasso, privando il guerrafondaio di ogni aura eroica e rivelandone l'essenza farsesca",
            "Celebra la superiorità tecnologica delle forze armate italiane nel dopoguerra",
            "Propone una riforma sartoriale per gli ufficiali dell'esercito della NATO",
            "Dimostra che le medaglie d'oro aumentano il valore finanziario della pittura ad olio"
        ],
        "correctIndex": 0,
        "explanation": "La brillante operazione di Baj svuota dall'interno l'estetica marziale mostrandone la ridicola vanità senile."},
        {"question": "Quale celebre quadro futurista del 1911 costituì il modello iconografico diretto per 'I Funerali dell'anarchico Pinelli'?",
        "options": [
            "I Funerali dell'anarchico Galli di Carlo Carrà",
            "La città che sale di Umberto Boccioni",
            "Dinamismo di un cane al guinzaglio di Giacomo Balla",
            "Elasticità di Boccioni"
        ],
        "correctIndex": 0,
        "explanation": "Baj rielabora esplicitamente il capolavoro di Carrà del 1911, sostituendo Galli con Pinelli in un drammatico confronto storico."},
        {"question": "Quale rapporto intrattiene il Movimento Arte Nucleare con lo Spazialismo di Lucio Fontana?",
        "options": [
            "Vi fu una stretta vicinanza intellettuale e ammirazione reciproca (Fontana firmò manifesti nucleari e Baj firmò manifesti spaziali), condividendo la consapevolezza che la fisica moderna imponeva il superamento dell'arte tradizionale",
            "Vi fu una guerra giudiziaria per l'uso del colore rosso",
            "Fontana querelò Baj vietandogli di esporre quadri a Milano",
            "Non ebbero mai contatti vivendo in continenti differenti"
        ],
        "correctIndex": 0,
        "explanation": "Spazialismo e Arte Nucleare furono i due pilastri della Milano d'avanguardia dei primi anni Cinquanta."},
        {"question": "Cosa caratterizza la serie delle 'Modificazioni' realizzata da Baj negli anni Cinquanta?",
        "options": [
            "Baj acquistava vecchi quadri a olio accademici o kitsch di paesaggi montani ottocenteschi nei mercatini e vi dipingeva sopra mostri atomici e funghi radioattivi, profanando il buon gusto borghese",
            "Modificava le cornici tagliandole a fette con la sega circolare",
            "Cancellava le firme degli autori per apporvi la firma di Picasso",
            "Dipingeva numeri telefonici sopra i ritratti di famiglia"
        ],
        "correctIndex": 0,
        "explanation": "Le Modificazioni anticipano le pratiche situazioniste del détournement (Détournements di Asger Jorn)."},
        {"question": "Quale filosofo della scienza e teorico del linguaggio influenzò la polemica antitecnocratica di Enrico Baj?",
        "options": [
            "Alfred Jarry (fondatore della Patafisica, la scienza delle soluzioni immaginarie)",
            "Auguste Comte",
            "Cartesio",
            "Isaac Newton"
        ],
        "correctIndex": 0,
        "explanation": "La Patafisica fu l'arma concettuale con cui Baj combatteva la cieca fede positivista nella bomba e nel progresso."}
    ]
})

# C16: Francis Bacon
chaps.append({
    "id": "arte1-c16",
    "number": 16,
    "partNum": partNum,
    "partTitle": partTitle,
    "module": module,
    "title": "Francis Bacon: La Carne Reclusa e il Grido Biologico",
    "subtitle": "Dal Ritratto di Papa Innocenzo X ai trittici della crocifissione: la gabbia prospettica e l'urlo muto dell'animale uomo",
    "summary": """### 1. Dati biografici e la solitudine londinese\n\nNato a Dublino nel 1909 da genitori inglesi (il padre era un rigido addestratore di cavalli da corsa discendente del filosofo Francis Bacon), **Francis Bacon** vive un'infanzia segnata da gravi crisi d'asma, dal ripudio familiare a causa della propria omosessualità e dal vagabondaggio giovanile tra Berlino, Parigi e Londra. Privo di qualsiasi formazione accademica tradizionale, Bacon inizia come decoratore d'interni prima di consacrarsi alla pittura in uno studio leggendario, caotico e polveroso al numero 7 di Reece Mews a South Kensington (Londra).\n\nNel 1944 presenta alla Lefevre Gallery di Londra il monumentale trittico *Tre studi per figure alla base di una crocifissione*: l'impatto sul pubblico britannico stremato dalla guerra è sismico. Bacon rifiuta categoricamente l'astrazione, considerandola un'evasione decorativa sterile: per lui la grande sfida dell'arte contemporanea è **reinventare la figura umana dopo la catastrofe**, registrandone la vulnerabilità organica, la solitudine claustrofobica e il terrore carnale.\n\n---\\n\n### 2. Dispositivi spaziali e procedimenti pittorici di Bacon\n\nBacon mette a punto una serie di dispositivi compositivi inconfondibili:\n* **La gabbia spaziale (*Space frame*)**: La figura umana non siede in una stanza rassicurante, ma è rinchiusa all'interno di una gabbia cubica trasparente, un prisma di linee sottili che fluttua nel vuoto. La gabbia simboleggia l'isolamento solipsistico e claustrofobico dell'individuo moderno, ma agisce anche come lente di ingrandimento chirurgica che impedisce alla figura di fuggire dallo sguardo dello spettatore.\n* **La distorsione della carne e l'incidente controllato**: Bacon stende fondi compatti e impeccabili di colori acidi e uniformi (aranci accesi, viola, ocra, neri). Sulla figura, invece, aggredisce la pittura a olio con stracci imbevuti di trementina, spugne abrasive, pennelli da barba e le proprie dita, provocando sbavature, torsioni violente e cancellature accidentali che de-figurano l'anatomia senza mai distruggerne il riconoscimento biologico.\n* **La bocca spalancata e il grido muto**: Ispirato dal fermo-immagine della nutrice urlante nel film *La corazzata Potëmkin* di Ejzenštejn e da un manuale illustrato di malattie della bocca comprato a Parigi, Bacon trasforma la bocca aperta non in un simbolo metafisico, ma nel **condotto biologico primordiale attraverso cui l'animale uomo emette il grido della propria caducità**.\n\n---\\n\n### 3. Analisi delle opere cardine\n\n#### Studio dal ritratto di papa Innocenzo X di Velázquez (1953)\n![Francis Bacon, Studio dal ritratto di papa Innocenzo X di Velázquez, 1953](assets/corsi/dapl08/anno-1/storia-arte-1/images/bacon_innocenzo_x.jpg)\n\n* **Descrizione e composizione**: Ispirato ossessivamente dal capolavoro dipinto da Diego Velázquez nel 1650 (conservato a Roma a Palazzo Doria Pamphilj), Bacon rielabora la figura del pontefice. Il papa non siede più sul trono papale maestoso e sicuro di sé: è un uomo solo, intrappolato in una gabbia di barre verticali traslucide simili a una sedia elettrica. La mozzetta purpurea è scossa da colature violente e il volto è sfigurato da un urlo primordiale che dilacera i lineamenti.\n* **Significato iconologico**: Il Vicario di Cristo in terra perde ogni attributo di sacralità e potere temporale: diventa la bestia urlante nel mattatoio della storia moderna, l'uomo straziato dalla paura della fine. Come dichiarò Bacon: *«Quando vedo un quarto di bue al macello, penso sempre che lì avrei potuto esserci io... siamo tutti carne da macello»*.\n\n#### I Trittici monumentali e l'ombra di George Dyer\n* Dagli anni Sessanta Bacon adotta il formato monumentale del trittico (*Tre studi di figura*, *In memoria di George Dyer*, 1971), dove il dramma dell'amante suicidatosi a Parigi nel 1971 viene sezionato attraverso una spietata lucidità anatomica ed esistenziale.""",
    "keyPoints": [
        "Francis Bacon rifiuta l'astrazione difendendo la necessità di reinventare la figura umana e la carne dopo la Seconda Guerra Mondiale.",
        "Il trittico del 1944 'Tre studi per figure alla base di una crocifissione' sancisce l'irruzione della sua pittura traumatica a Londra.",
        "Utilizza la 'gabbia spaziale' cubica per isolare il soggetto e procedimenti accidentali (stracci, spugne) per torcere la carne.",
        "Negli Studi su Innocenzo X (1953) demolisce il ritratto di Velázquez trasformando il papa in un essere urlante su una sedia elettrica."
    ],
    "flashcards": [
        {"question": "Quale celebre capolavoro di Diego Velázquez del 1650 ossessionò Bacon per oltre un decennio?", "answer": "Il Ritratto di papa Innocenzo X (conservato alla Galleria Doria Pamphilj a Roma).", "front": "Quale celebre capolavoro di Diego Velázquez del 1650 ossessionò Bacon per oltre un decennio?", "back": "Il Ritratto di papa Innocenzo X (conservato alla Galleria Doria Pamphilj a Roma)."},
        {"question": "Quale dispositivo compositivo geometrico usava Bacon per isolare le sue figure umane nel vuoto?", "answer": "La gabbia spaziale (space frame), una struttura prismatica cubica trasparente.", "front": "Quale dispositivo compositivo geometrico usava Bacon per isolare le sue figure umane nel vuoto?", "back": "La gabbia spaziale (space frame), una struttura prismatica cubica trasparente."},
        {"question": "Da quale celebre fotogramma cinematografico di Ejzenštejn trasse ispirazione per la bocca urlante?", "answer": "Dalla scena della scalinata di Odessa nel film 'La corazzata Potëmkin' (la nutrice ferita all'occhio).", "front": "Da quale celebre fotogramma cinematografico di Ejzenštejn trasse ispirazione per la bocca urlante?", "back": "Dalla scena della scalinata di Odessa nel film 'La corazzata Potëmkin' (la nutrice ferita all'occhio)."},
        {"question": "Cosa dichiarò Bacon riguardo alla carne animale nei macelli?", "answer": "'Siamo tutti carne da macello... se entro in una macelleria mi stupisce sempre non essere appeso io al posto dell'animale'.", "front": "Cosa dichiarò Bacon riguardo alla carne animale nei macelli?", "back": "'Siamo tutti carne da macello... se entro in una macelleria mi stupisce sempre non essere appeso io al posto dell'animale'."},
        {"question": "Quale tragico evento autobiografico del 1971 a Parigi segnò i monumentali 'Trittici Neri' di Bacon?", "answer": "Il suicidio del compagno George Dyer per overdose alla vigilia della retrospettiva di Bacon al Grand Palais.", "front": "Quale tragico evento autobiografico del 1971 a Parigi segnò i monumentali 'Trittici Neri' di Bacon?", "back": "Il suicidio del compagno George Dyer per overdose alla vigilia della retrospettiva di Bacon al Grand Palais."}
    ],
    "openQuestions": [
        "Analizzate il significato formale e simbolico della 'gabbia spaziale' e della distorsione anatomica nell'opera di Francis Bacon.",
        "Confrontate lo Studio da papa Innocenzo X di Bacon (1953) con il modello originale di Velázquez del 1650, evidenziando il ribaltamento di senso e di potere."
    ],
    "quiz": [
        {"question": "Dove nacque Francis Bacon nel 1909?", "options": ["Dublino (Irlanda)", "Londra (Inghilterra)", "Edimburgo (Scozia)", "Belfast (Irlanda del Nord)"], "correctIndex": 0, "explanation": "Bacon nacque a Dublino da genitori inglesi, crescendo in un clima familiare conflittuale."},
        {"question": "Quale formato espositivo prediligeva Bacon per le sue opere più ambiziose a partire dagli anni Sessanta?", "options": ["Il Trittico monumentale con tre grandi tele incorniciate sotto vetro", "Il dittico orizzontale in legno dorato", "Il rotolo di pergamena continua da srotolare", "Il tondo rinascimentale a monocromo"], "correctIndex": 0, "explanation": "Il trittico permetteva a Bacon di isolare sequenze temporali del corpo senza narrazione aneddotica."},
        {"question": "Cosa pretendeva categoricamente Bacon per l'esposizione di tutti i suoi quadri nei musei?", "options": ["Che fossero tutti rigorosamente protetti da pesanti vetri riflettenti", "Che fossero toccati con le mani dal pubblico", "Che fossero illuminati da candele a cera", "Che non avessero alcuna cornice"], "correctIndex": 0, "explanation": "Il vetro creava una distanza protettiva e rifletteva la sagoma dello spettatore all'interno della gabbia spaziale."},
        {"question": "In quale celebre studio londinese lavorò Bacon fino alla fine della sua vita?", "options": ["7 Reece Mews a South Kensington", "Abbey Road", "Baker Street", "Trafalgar Square"], "correctIndex": 0, "explanation": "Lo studio caotico di Reece Mews fu donato alla Hugh Lane Gallery di Dublino che lo ricostruì fedelmente."},
        {"question": "In quale città morì Francis Bacon nel 1992 durante un soggiorno?", "options": ["Madrid", "Londra", "Parigi", "New York"], "correctIndex": 0, "explanation": "Bacon morì a Madrid il 28 aprile 1992 all'età di 82 anni."},
    ],
    "examQuiz": [
        {"question": "Nel celebre saggio filosofico 'Francis Bacon: Logica della sensazione' (1981), quale tesi magistrale formula Gilles Deleuze sulla pittura di Bacon?",
        "options": [
            "Deleuze dimostra che Bacon non dipinge il mostro o l'orrore fantastico, ma strappa la Figura dal racconto figurativo per farne un puro aggregato di forze invisibili (pressione, caduta, isolamento) che agiscono direttamente sul sistema nervoso del fruitore",
            "Deleuze definisce Bacon un semplice illustratore gotico di storie di fantasmi vittoriane",
            "Deleuze accusa Bacon di aver copiato i manifesti della propaganda stalinista",
            "Deleuze dimostra che la pittura di Bacon è solo un'operazione finanziaria di borsa"
        ],
        "correctIndex": 0,
        "explanation": "Deleuze teorizza che Bacon dipinge non la forma, ma le 'forze' (il grido, il collasso carnale) che deformano il corpo."},
        {"question": "Quale ruolo svolgono le fotografie cronofotografiche di Eadweard Muybridge nella pittura di Bacon?",
        "options": [
            "Costituirono l'archivio iconografico primario da cui Bacon estrapolava corpi maschili nudi in movimento, lottatori atletici e animali in corsa per studiarne la muscolatura e le contorsioni biologiche",
            "Servivano per proiettare film educativi nelle scuole d'arte",
            "Erano cataloghi di vendita per abiti sartoriali maschili",
            "Venivano incollate direttamente sulle tele come fotomontaggi pop"
        ],
        "correctIndex": 0,
        "explanation": "I libri di Muybridge erano costantemente aperti e calpestati sul pavimento dello studio di Bacon."},
        {"question": "Per quale motivo Bacon rifiutava sempre di vedere dal vero il ritratto originale di Innocenzo X di Velázquez a Roma?",
        "options": [
            "Temeva che la perfezione del dipinto reale infrangesse l'ossessione visiva e la potenza fantasmica che la riproduzione fotografica stampata aveva creato nella sua mente",
            "Perché il Vaticano gli aveva interdetto l'ingresso nei musei ecclesiastici",
            "Perché non amava viaggiare in treno o in aereo",
            "Perché considerava Velázquez un pittore mediocre privo di tecnica"
        ],
        "correctIndex": 0,
        "explanation": "Pur essendo stato a Roma, non volle mai vedere l'originale per non compromettere la propria rielaborazione mentale."},
        {"question": "In che termini la presenza di quarti di carne da macello nei quadri di Bacon dialoga con la storia dell'arte?",
        "options": [
            "Rinnova la tradizione della carne macellata inaugurata dal 'Bue squartato' di Rembrandt e ripresa da Chaïm Soutine, facendone la metafora definitiva dell'animale uomo crocifisso nella materia",
            "Rappresenta una campagna vegetariana animalista dell'Inghilterra laburista",
            "Era una ricetta culinaria illustrata per la cucina tradizionale irlandese",
            "Costituiva una protesta sindacale dei lavoratori dei mattatoi londinesi"
        ],
        "correctIndex": 0,
        "explanation": "Da Rembrandt a Soutine, la carne squartata per Bacon è la prova biologica dell'uguaglianza tra uomo e animale di fronte alla morte."},
        {"question": "Cosa indica la nozione baconiana di 'incidente' (*accident*) nel processo pittorico?",
        "options": [
            "Una macchia improvvisa, un colpo di spugna o una sbavatura involontaria che l'artista introduce deliberatamente per distruggere il disegno illustrativo e aprire la via alla verità della sensazione",
            "La rottura involontaria dei tubetti di colore caduti per terra",
            "Un litigio fisico tra l'artista e i modelli in studio",
            "Un errore tipografico nella stampa del catalogo d'asta"
        ],
        "correctIndex": 0,
        "explanation": "L'incidente per Bacon è il dispositivo con cui la pittura sfugge al controllo razionale aprendosi alla vita inconscia."}
    ]
})

# C17: Alberto Giacometti
chaps.append({
    "id": "arte1-c17",
    "number": 17,
    "partNum": partNum,
    "partTitle": partTitle,
    "module": module,
    "title": "Alberto Giacometti: La Fragilità Filiforme e l'Uomo che Cammina",
    "subtitle": "Dalla stagione surrealista alla scarnificazione della materia nel leggendario atelier di Rue Hippolyte-Maindron",
    "summary": """### 1. Dati biografici e la solitudine dell'atelier parigino\n\nNato a Borgonovo di Stampa nella svizzera Val Bregaglia nel 1901, figlio del celebre pittore post-impressionista Giovanni Giacometti, **Alberto Giacometti** compie la sua formazione artistica a Ginevra e Roma prima di trasferirsi a Parigi nel 1922 per studiare scultura sotto la guida di Antoine Bourdelle. Negli anni Venti e Trenta aderisce attivamente al movimento surrealista di André Breton, realizzando sculture-oggetto memorabili cariche di erotismo e violenza psicologica (*La pallina sospesa*, 1930; *Il palazzo alle 4 del mattino*, 1932).\n\nNel 1935 compie una clamorosa rottura con i surrealisti: decide di **ritornare a lavorare dal vero**, ponendosi davanti al modello umano per indagare la realtà dell'apparato visivo. Si stabilisce nel leggendario, minuscolo e polveroso atelier di soli ventitré metri quadrati al numero 46 di Rue Hippolyte-Maindron a Montparnasse, dove lavorerà per quarant'anni fino alla morte insieme al fedele fratello Diego e alla moglie Annette.\n\n---\\n\n### 2. La poetica dello sguardo e la scarnificazione della figura\n\nTra il 1940 e il 1947 Giacometti attraversa una crisi creativa drammatica, riducendo le sue sculture in gesso a dimensioni minuscole di pochi millimetri (*«più cercavo di rendere ciò che vedevo, più la statua si rimpiccioliva, fino a sparire nella polvere»*). All'indomani del 1945 approda alla sua invenzione definitiva:\n* **La figura filiforme e scarnificata**: Giacometti modella figure umane in gesso e bronzo **altissime, sottilissime, erose fino all'osso**, prive di carne e di massa volumetrica muscolare. Il corpo si trasforma in una linea verticale rugosa e scabra, segnata da un'ossessiva manipolazione delle dita.\n* **I piedi monumentali ancorati al suolo**: In netto contrasto con la fragilità quasi trasparente del torso filiforme, i piedi della figura sono enormi, pesanti, zavorrati e saldati a una zolla di bronzo o a un basamento spesso. Questo contrasto esprime la condizione tragica dell'essere umano: schiacciato dalla gravità della terra, ma proteso con lo spirito verso l'infinito dello spazio circostante.\n* **La nozione di distanza e lo spazio vivente**: Giacometti non modella il corpo anatomico oggettivo; modella **la figura umana così come essa appare a distanza nello spazio reale**. Quando guardiamo una persona da lontano nella strada, non vediamo i pori della pelle o i dettagli anatomici, ma una presenza verticale e vibrante circondata da un immenso vuoto atmosferico che la assedia e tenta di cancellarla.\n\n---\\n\n### 3. Analisi delle opere cardine\n\n#### L'Homme qui marche I (L'uomo che cammina I, 1960)\n![Alberto Giacometti, L'Homme qui marche I (L'uomo che cammina I), 1960 - Bronzo](assets/corsi/dapl08/anno-1/storia-arte-1/images/giacometti_uomo_cammina.jpg)\n\n* **Descrizione e impianto plastico**: Una scultura in bronzo alta oltre un metro e ottanta. Una figura maschile scheletrica ed essenziale, con la gamba sinistra proiettata in avanti nell'atto di compiere un passo risoluto, le braccia tese lungo i fianchi e lo sguardo fermo puntato verso l'orizzonte. La superficie bronzea è tormentata, piena di asperità, rugosità e solchi che catturano la luce vibrando nello spazio.\n* **Significato iconologico e filosofico**: L'opera è universalmente considerata il manifesto visivo supremo dell'**Esistenzialismo** moderno. Nel celebre saggio *La ricerca dell'assoluto* (1948), Jean-Paul Sartre riconobbe in Giacometti l'artista che aveva saputo incarnare la condizione dell'uomo contemporaneo: un essere fragile, solitario, scarnificato dalle guerre e minacciato dal nulla, ma che **nonostante tutto continua ostinatamente ad avanzare, a camminare e ad affermare la propria dignità nel mondo**.\n* **Fortuna critica e record d'asta**: Nel 1962 Giacometti trionfa alla 31ª Biennale di Venezia vincendo il Gran Premio per la Scultura. Morì a Coira nel gennaio 1966 a sessantaquattro anni, consacrato come uno dei massimi scultori di ogni tempo.""",
    "keyPoints": [
        "Alberto Giacometti rompe con il Surrealismo nel 1935 per tornare allo studio ossessivo del modello dal vero a Montparnasse.",
        "Le sue sculture della maturità sono figure filiformi scarnificate, erose fino all'osso, circondate da un vuoto atmosferico assediante.",
        "I piedi enormi zavorrati a terra contrastano con l'estrema leggerezza della silhouette, simboleggiando la gravità dell'esistere.",
        "Nel capolavoro 'L'Homme qui marche I' (1960), celebrato da Jean-Paul Sartre, visualizza l'emblema dell'eroismo esistenziale moderno."
    ],
    "flashcards": [
        {"question": "In quale leggendario atelier parigino di soli 23 metri quadrati lavorò Giacometti per quarant'anni?", "answer": "Al 46 di Rue Hippolyte-Maindron nel quartiere di Montparnasse.", "front": "In quale leggendario atelier parigino di soli 23 metri quadrati lavorò Giacometti per quarant'anni?", "back": "Al 46 di Rue Hippolyte-Maindron nel quartiere di Montparnasse."},
        {"question": "Quale movimento d'avanguardia storico frequentò attivamente Giacometti negli anni Trenta prima della rottura?", "answer": "Il Surrealismo di André Breton.", "front": "Quale movimento d'avanguardia storico frequentò attivamente Giacometti negli anni Trenta prima della rottura?", "back": "Il Surrealismo di André Breton."},
        {"question": "Come si presentano le sculture della maturità di Alberto Giacometti?", "answer": "Figure umane filiformi, sottilissime, scarnificate e rugose, con grandi piedi ancorati al basamento.", "front": "Come si presentano le sculture della maturità di Alberto Giacometti?", "back": "Figure umane filiformi, sottilissime, scarnificate e rugose, con grandi piedi ancorati al basamento."},
        {"question": "Quale illustre filosofo esistenzialista scrisse il saggio 'La ricerca dell'assoluto' dedicato a Giacometti nel 1948?", "answer": "Jean-Paul Sartre.", "front": "Quale illustre filosofo esistenzialista scrisse il saggio 'La ricerca dell'assoluto' dedicato a Giacometti nel 1948?", "back": "Jean-Paul Sartre."},
        {"question": "Quale celebre scultura in bronzo del 1960 raffigura una figura scarnificata che avanza decisa nel vuoto?", "answer": "L'Homme qui marche I (L'uomo che cammina I).", "front": "Quale celebre scultura in bronzo del 1960 raffigura una figura scarnificata che avanza decisa nel vuoto?", "back": "L'Homme qui marche I (L'uomo che cammina I)."}
    ],
    "openQuestions": [
        "Analizzate il significato filosofico ed esistenziale del contrasto tra la silhouette filiforme scarnificata e i piedi pesantemente zavorrati nelle sculture di Giacometti.",
        "Descrivete l'evoluzione artistica di Giacometti dalla fase surrealista degli oggetti a funzionamento simbolico fino alla riduzione spaziale della figura umana nel dopoguerra."
    ],
    "quiz": [
        {"question": "In quale cantone della Svizzera nacque Alberto Giacometti nel 1901?", "options": ["Cantone dei Grigioni (Borgonovo di Stampa)", "Canton Ticino", "Canton Zurigo", "Canton Ginevra"], "correctIndex": 0, "explanation": "Giacometti nacque in Val Bregaglia nei Grigioni da una celebre famiglia di artisti svizzeri."},
        {"question": "Chi fu il fedele fratello di Alberto che collaborò per decenni come scultore e designer nel suo studio?", "options": ["Diego Giacometti", "Bruno Giacometti", "Giovanni Giacometti", "Augusto Giacometti"], "correctIndex": 0, "explanation": "Diego Giacometti fu il modello, assistente e bronzista inseparabile di Alberto, nonché celebre designer di arredi."},
        {"question": "Cosa cercava di rappresentare Giacometti nelle sue figure umane scarnificate?", "options": ["La presenza viva della figura umana percepita a distanza reale nello spazio, assediata dal vuoto", "La ricostruzione scientifica dei muscoli per studenti di medicina", "Ideali di bellezza atletica per le olimpiadi", "Fantasmi incorporei privi di peso"], "correctIndex": 0, "explanation": "Giacometti voleva restituire l'apparizione ottica e la solitudine della persona umana nello spazio circostante."},
        {"question": "Quale prestigioso riconoscimento internazionale ottenne Giacometti nel 1962?", "options": ["Il Gran Premio per la Scultura alla 31ª Biennale di Venezia", "Il Premio Nobel per la Pace", "La Palma d'Oro al Festival di Cannes", "Il Leone d'Oro alla Mostra del Cinema"], "correctIndex": 0, "explanation": "Nel 1962 la Biennale di Venezia consacrò Giacometti come il massimo scultore vivente."},
        {"question": "Oltre alla scultura in gesso e bronzo, quale altra disciplina praticò instancabilmente Giacometti per tutta la vita?", "options": ["La pittura a olio su tela e il disegno a grafite frenetico", "La tessitura di arazzi fiamminghi", "La regia di film di fantascienza", "L'incisione di medaglie numismatiche statali"], "correctIndex": 0, "explanation": "I dipinti di Giacometti, solcati da ragnatele di segni grigi e bianchi, indagano con la stessa ossessione lo sguardo del modello."}
    ],
    "examQuiz": [
        {"question": "In che termini Jean-Paul Sartre interpreta la materia assottigliata delle sculture di Giacometti nel saggio 'La ricerca dell'assoluto'?",
        "options": [
            "Come la vittoria dell'uomo sul nulla: la figura è erosa dal vuoto cosmico ma resiste come nucleo indistruttibile di libertà e coscienza morale, rifiutando la pienezza compiuta della scultura classica",
            "Come un tentativo fallito di imitare la scultura funeraria egizia",
            "Come una dimostrazione della malnutrizione infantile durante la guerra",
            "Come un bozzetto incompleto destinato a essere ricoperto di marmo"
        ],
        "correctIndex": 0,
        "explanation": "Sartre scrisse che Giacometti seppe dare forma al nulla che circonda l'uomo, restituendo l'eroismo dell'esistere."},
        {"question": "Quale fenomeno ottico e psicologico costrinse Giacometti a rimpicciolire le sue figure scultoree tra il 1940 e il 1945?",
        "options": [
            "La consapevolezza che una testa umana vista a venti metri di distanza non misura le sue reali dimensioni metriche, ma occupa uno spazio microscopico nel campo ottico, inducendolo a inseguire la percezione fenomenologica reale",
            "La carenza di gesso a Parigi causata dal razionamento di guerra",
            "Il divieto delle autorità di scolpire statue più alte di cinque centimetri",
            "Una malattia alla vista che gli impediva di vedere oggetti grandi"
        ],
        "correctIndex": 0,
        "explanation": "Giacometti rifiutava la scultura concettuale: voleva scolpire esattamente ciò che l'occhio vede a distanza reale."},
        {"question": "Quale celebre scultura surrealista del 1930 di Giacometti fu definita da Breton il prototipo dell'oggetto a funzionamento simbolico?",
        "options": [
            "La sfera sospesa (Boule suspendue)",
            "L'oggetto invisibile",
            "La donna sgozzata",
            "Il palazzo alle 4 del mattino"
        ],
        "correctIndex": 0,
        "explanation": "La pallina intagliata oscillante sopra una mezzaluna generava una carica di sensualità e frustrazione erotica pura."},
        {"question": "Sul piano della morfologia visiva, quale ruolo svolgono i ritratti dipinti da Giacometti della moglie Annette e del fratello Diego?",
        "options": [
            "Il volto è costantemente incorniciato da una gabbia di linee e rettangoli concentrici dipinti sulla tela, con occhi ipnotici che fissano lo spettatore penetrando la densità dello spazio",
            "Sono ritratti umoristici destinati alle riviste satiriche parigine",
            "Raffigurano i modelli travestiti da personaggi mitologici romani",
            "Sono miniature su avorio secondo la tecnica settecentesca"
        ],
        "correctIndex": 0,
        "explanation": "Nei dipinti il modello è intrappolato in un reticolo spaziale da cui lo sguardo emana con intensità perforante."},
        {"question": "In che modo l'opera di Giacometti influenzò il drammaturgo Samuel Beckett nella stesura di 'Aspettando Godot'?",
        "options": [
            "Giacometti e Beckett furono intimi amici nelle notti parigine, condividendo il senso dell'assurdo e della solitudine umana; per la messinscena di Godot all'Odéon nel 1961 Giacometti realizzò la celebre scultura dell'albero spoglio solitario",
            "Beckett scrisse la commedia all'interno dell'atelier di Giacometti mentre posava come modello nudo",
            "Giacometti finanziò la pubblicazione dei romanzi di Beckett in America",
            "Non ebbero mai alcun contatto intellettuale o personale"
        ],
        "correctIndex": 0,
        "explanation": "L'albero scheletrico e solitario realizzato da Giacometti per Godot è la perfetta sintesi dell'esistenzialismo condiviso dai due maestri."}
    ]
})

print("Writing completed mod1_data.py with all 17 chapters...")

with open("scripts/mod1_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("# Modulo 1 Completo: Anni Cinquanta (Capitoli 1 - 17)\n\n")
    f.write(f"partNum = 1\n")
    f.write(f"partTitle = \"1. Arte Contemporanea Anni '50: Informale, Espressionismo Astratto e Spazialismo\"\n")
    f.write(f"module = \"anni50\"\n\n")
    f.write("def get_mod1_chapters():\n")
    f.write("    return " + json.dumps(chaps, ensure_ascii=False, indent=4) + "\n")

print("Successfully wrote scripts/mod1_data.py with", len(chaps), "chapters!")
