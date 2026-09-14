const fs = require('fs');
const path = require('path');

const dataFilePath = path.join(__dirname, '..', 'data', 'arte-data.js');
let fileContent = fs.readFileSync(dataFilePath, 'utf8');

const sandbox = { window: {} };
eval(fileContent.replace('window.ARTE_DATA', 'sandbox.window.ARTE_DATA'));
const allData = sandbox.window.ARTE_DATA;

// Capitolo 34: Il Secolo a Uncinetto (indice 33)
allData[33].subtitle = "Francesco Bonami, la fine delle rotture d'avanguardia, l'11 settembre, le fiere e i musei delle archistar";
allData[33].summary = `### 1. La metafora dell'uncinetto: Fine dei manifesti rigidi e nascita della rete globale

![Il Secolo a Uncinetto (a cura di Francesco Bonami, 50ª Biennale di Venezia 2003) - La trama iperconnessa dell'arte globale](assets/corsi/dapl08/anno-2/storia-arte-2/images/secolo_uncinetto_bonami.jpg)

All'aprirsi del terzo millennio, il critico e curatore d'arte **Francesco Bonami** introduce una delle definizioni più felici per spiegare il cambiamento dell'arte contemporanea: **«Il secolo a uncinetto»**.
Se il Novecento è stato il secolo delle avanguardie storiche — caratterizzato da rotture violente, manifesti categorici, scontri ideologici e una continua corsa in avanti verso il futuro — gli anni Duemila si aprono all'insegna di una **trama fitta, orizzontale e senza un centro unico**, paragonabile proprio al lavoro continuo dell'uncinetto:
* **Una trama ricca di collegamenti:** l'arte non procede più cancellando ciò che è venuto prima, ma riannoda fili diversi. Moda, architettura d'autore, design, mercati del lusso, geopolitica e finanza si intrecciano in un unico grande tessuto.
* **Assenza di movimenti unici:** non esistono più grandi correnti dominanti con un'etichetta fissa (come l'Informale, la Pop Art o la Transavanguardia). Esistono invece **singoli artisti celebri e di grande visibilità**, capaci di lavorare a livello mondiale attraverso una fitta rete di grandi gallerie internazionali (Gagosian, Hauser & Wirth, David Zwirner, Pace).

---

### 2. Lo spartiacque dell'11 settembre 2001 e il mondo policentrico

L'attacco terroristico alle Torri Gemelle di New York l'**11 settembre 2001** distrugge per sempre l'illusione di una pace sicura e l'invulnerabilità del modello occidentale:
* **La tragedia vissuta in diretta tv:** per la prima volta un evento drammatico di distruzione globale viene visto in tempo reale da miliardi di persone attraverso gli schermi televisivi. Le immagini del crollo spingono gli artisti a riflettere sul trauma, sulla fragilità delle costruzioni umane e sull'impatto mediatico delle immagini della violenza.
* **Spostamento del baricentro mondiale:** il mondo dell'arte non gravita più solo sull'asse storico New York-Londra-Parigi-Berlino, ma si apre all'ascesa straordinaria dei paesi emergenti (Brasile, Russia, India, Cina, Sudafrica) e delle capitali del Medio Oriente (Dubai, Abu Dhabi, Doha).
* **Il ruolo centrale dei curatori internazionali:** si moltiplicano le grandi mostre periodiche in ogni continente (Istanbul, Sharjah, San Paolo, Gwangju), trasformando i grandi curatori (come Okwui Enwezor, Hans Ulrich Obrist o Francesco Bonami con la Biennale di Venezia del 2003, *Sogni e Conflitti*) in figure chiave che mettono a confronto culture, migrazioni e memorie diverse.

---

### 3. Fiere d'arte, musei spettacolari e rivoluzione digitale

Negli anni Duemila cambiano i luoghi e i modi in cui l'arte viene vissuta e acquistata:

| Ambito di Cambiamento | Caratteristica degli Anni Duemila | Impatto sull'Arte |
| :--- | :--- | :--- |
| **Le Grandi Fiere Internazionali** | *Art Basel*, *Art Basel Miami Beach*, *Frieze London*, *Armory Show* | La fiera non è più un semplice mercato per mercanti, ma diventa un grande evento culturale e mondano che orienta i gusti e stabilisce le quotazioni internazionali. |
| **I Musei-Cattedrale (Archistar)** | *Guggenheim Bilbao* (Gehry), *Tate Modern* (Herzog & de Meuron, 2000), *MAXXI* (Hadid) | Il museo diventa un monumento spettacolare; l'architettura esterna e le sale gigantesche (come la *Turbine Hall*) attirano milioni di turisti. |
| **Internet e i Social Network** | Nascita di YouTube, Facebook, blog e smartphone | Le immagini delle opere circolano all'istante in rete, favorendo un'esperienza dell'arte sempre più visiva e condivisibile. |

---

### 4. I temi principali degli anni Duemila

1. **La memoria delle vittime e il corpo politico:** artisti come Doris Salcedo e Adrian Paci danno voce alle sofferenze degli oppressi, alle migrazioni umane e alle ferite aperte della storia recente.
2. **L'ironia sul sistema e la satira del potere:** Maurizio Cattelan e Francesco Vezzoli mostrano con amara ironia i meccanismi della celebrità, della religione e dello spettacolo.
3. **L'attenzione al clima e l'esperienza della luce:** Olafur Eliasson porta elementi della natura all'interno degli spazi museali, stimolando la consapevolezza ecologica del pubblico.
4. **La ribellione urbana:** Banksy usa lo stencil e l'arte di strada come un mezzo immediato e virale per denunciare le guerre, le ingiustizie e il mercato.
5. **L'attivismo per la libertà e il controllo della rete:** Ai Weiwei unisce la maestria artigianale cinese alla comunicazione su internet per sfidare l'autoritarismo politico.`;

allData[33].keyPoints = [
  "Francesco Bonami conia la definizione 'Il secolo a uncinetto' (Biennale 2003) per descrivere l'arte contemporanea come una rete priva di centro unico.",
  "L'11 settembre 2001 rompe la certezza della sicurezza occidentale e apre a un mondo dell'arte multipolare e globale.",
  "Le grandi fiere (Art Basel) e i musei progettati da grandi archistar (Guggenheim Bilbao, Tate Modern) ridefiniscono gli spazi dell'arte.",
  "I temi cardine sono: memoria storica, migrazioni umane, ironia sul potere, emergenza ecologica e attivismo politico in rete."
];

// Capitolo 35: Adrian Paci (indice 34)
allData[34].subtitle = "L'emigrazione dall'Albania, la poesia degli incontri a distanza, la scaletta nel vuoto e la memoria";
allData[34].summary = `### 1. Dati biografici e contesto: La fuga dall'Albania e l'arrivo in Italia

Nato a Shkodra (Scutari, Albania) nel 1969, **Adrian Paci** si forma all'Accademia di Belle Arti di Tirana in un paese segnato dal rigido isolamento del regime comunista. Nel 1997, a seguito del crollo delle piramidi finanziarie che getta l'Albania nella guerra civile e nel caos, Paci fugge via mare verso l'Italia con la moglie e le figlie piccole, stabilendosi a Milano. 

Questa esperienza vissuta in prima persona trasforma la sua arte: l'emigrazione, il senso di sradicamento, la perdita delle certezze e la ricerca faticosa di un nuovo inizio diventano il cuore palpitante della sua poesia visiva.

---

### 2. Poetica: La dignità dell'emigrante e la delicatezza del racconto

L'opera di Paci unisce video, pittura su tela, scultura e mosaico con un tono poetico, intimo e mai retorico:
* **La memoria della terra d'origine**: Paci racconta la vita del suo popolo senza pietismo, mostrando la fierezza, la ricchezza culturale e la forza d'animo degli albanesi.
* **Il corpo umano sospeso nel viaggio**: gli emigranti nelle sue opere non sono visti come numeri statistici o emergenze di cronaca, ma come persone vive, colte nell'attesa e nella sospensione tra la patria lasciata alle spalle e un futuro incerto da costruire.

---

### 3. Analisi delle opere cardine

#### Apparizione (2001)
![Adrian Paci, Apparizione, 2001 - Installazione video a due canali, Collezione privata](assets/corsi/dapl08/anno-2/storia-arte-2/images/paci_apparizione.jpg)

* **Descrizione dell'opera**: Un'installazione video a due schermi contrapposti. Su uno schermo appare la figlia piccola dell'artista a Milano, che canta con voce pura e infantile una tradizionale canzoncina albanese. Quando la bambina si ferma per riprendere fiato o dimentica una parola, sullo schermo opposto i parenti rimasti in Albania (nonni, zii e cugini seduti in cerchio a Scutari) cantano il verso successivo per aiutarla.
* **Significato poetico**: Il video commuove per la sua grazia: la voce della bambina e il coro della famiglia annullano la distanza geografica dell'esilio attraverso il filo invisibile ma indissolubile della lingua, dell'affetto e della memoria familiare.

#### Centro di permanenza temporanea (2007)
![Adrian Paci, Centro di permanenza temporanea, 2007 - Video e fotografia, Tate Modern, Londra](assets/corsi/dapl08/anno-2/storia-arte-2/images/paci_centro_permanenza.jpg)

* **Descrizione della scena**: Sulla pista desolata di un aeroporto della California, un gruppo di uomini e donne vestiti con abiti quotidiani sale con ordine e pazienza lungo una tipica scaletta metallica mobile usata per salire a bordo degli aerei.
* **L'immagine potente della sospensione**: Arrivati in cima, si scopre che **l'aereo non c'è**: la scaletta si interrompe nel vuoto. Le persone rimangono stipate insieme sui gradini e sulla piattaforma sospesa nell'aria, guardando verso un orizzonte vuoto.
* **Significato concettuale**: L'opera è un monumento visivo indimenticabile alla condizione dell'emigrante contemporaneo: bloccato a metà del cammino, privo di documenti, escluso dall'arrivo e impossibilitato a tornare indietro, sospeso in un'attesa senza fine.

#### Vajtojca (Colei che piange, 2002)
* Paci torna a Scutari e mette in scena il proprio finto funerale: assume una tradizionale prefica albanese (la donna pagata per recitare i lamenti funebri rituali) affinché pianga sulla sua finta bara mentre lui è ancora vivo. Alla fine del lamento funebre, l'artista si alza, abbraccia la donna e le bacia la mano, celebrando la vittoria della vita e dell'arte sulla morte.`;

allData[34].keyPoints = [
  "Adrian Paci trasforma la propria esperienza di emigrato dall'Albania in Italia in una toccante riflessione universale sullo sradicamento.",
  "In 'Apparizione' (2001) una canzoncina cantata tra Milano e Scutari unisce la famiglia separata dall'emigrazione.",
  "Il capolavoro 'Centro di permanenza temporanea' (2007) mostra emigranti stipati su una scaletta d'aereo che finisce nel vuoto.",
  "Il suo lavoro unisce video, pittura classica e rispetto profondo per la dignità delle tradizioni popolari."
];

// Capitolo 36: Francesco Vezzoli (indice 35)
allData[35].subtitle = "Il ricamo a piccolo punto, le lacrime metalliche sulle dive del cinema e la parodia dello spettacolo";
allData[35].summary = `### 1. Dati biografici e formazione: Da Brescia a Londra

Nato a Brescia nel 1971, **Francesco Vezzoli** studia all'autorevole Central Saint Martins College of Art di Londra nei primi anni Novanta. In terra inglese scopre il valore rivoluzionario del kitsch, del cinema d'autore e della cultura camp, decidendo di unire l'amore per il cinema classico a un'attività tradizionalmente considerata umile e femminile: **il ricamo manuale a piccolo punto**.

---

### 2. Poetica: Il ricamo delle dive e la parodia del mondo dello spettacolo

La ricerca di Vezzoli è una sottile e affascinante **decostruzione dei miti dello spettacolo e della celebrità**:
* **Il ricamo a piccolo punto come lavoro intimo**: Vezzoli passa mesi e mesi a ricamare a mano con fili di seta, cotone e fili metallici. Applica questo lavoro paziente sui volti stampati su tela di grandi dive del cinema e del teatro (Silvana Mangano, Maria Callas, Catherine Deneuve, Franca Valeri).
* **Le lacrime metalliche (*Tears*)**: sui volti delle attrici, l'artista ricama vistose gocce metalliche di lacrime che scendono dagli occhi. La lacrima ricamata simboleggia il dolore segreto, la solitudine e il prezzo umano pagato dalle celebrità per vivere sotto i riflettori del successo.
* **La parodia dei media di massa**: Vezzoli non si limita ai quadri da galleria: crea veri e propri progetti spettacolari che utilizzano gli stessi linguaggi del marketing globale (finti trailer cinematografici, finti spot pubblicitari, finte campagne elettorali).

![Francesco Vezzoli, Trailer for a Remake of Gore Vidal's Caligula, 2005 - 51ª Biennale di Venezia](assets/corsi/dapl08/anno-2/storia-arte-2/images/vezzoli_caligula.jpg)

---

### 3. Analisi delle opere cardine

#### Trailer for a Remake of Gore Vidal's Caligula (2005)
* Presentato con enorme risonanza alla Biennale di Venezia del 2005, è un sontuoso **finto trailer cinematografico** per un ipotetico rifacimento del celebre film scandaloso *Caligola*.
* Vezzoli riesce a coinvolgere un cast eccezionale di attori e celebrità mondiali (tra cui Courtney Love, Benicio Del Toro, Helen Mirren e lo stilista Donatella Versace). Il finto trailer unisce costumi sfarzosi d'epoca romana, scarpe gioiello create appositamente e decadenza visiva, svelando come il potere contemporaneo viva di gossip e provocazioni mediatiche.

#### Greed (A New Fragrance by Francesco Vezzoli, 2009)
* L'artista inventa un profumo di lusso che in realtà non esiste (chiamato *Greed*, cioè Avidità), creando una boccetta con la propria immagine e affidando la regia del finto spot televisivo al celebre regista premio Oscar **Roman Polanski**. Lo spot vede protagoniste le star Natalie Portman e Michelle Williams che si azzuffano furiosamente per possedere la boccetta: una riflessione tagliente sull'ossessione per il lusso e sul potere di seduzione della pubblicità.`;

allData[35].keyPoints = [
  "Francesco Vezzoli fonde la pazienza artigianale del ricamo a piccolo punto con la parodia brillante dello star system hollywoodiano.",
  "Le sue caratteristiche 'lacrime metalliche' ricamate sui volti delle dive del cinema simboleggiano la solitudine della celebrità.",
  "Con il finto trailer di 'Caligula' (Biennale 2005) coinvolge attori e celebrità mondiali in una riflessione sulla spettacolarizzazione del potere.",
  "In 'Greed' (2009) crea la campagna pubblicitaria diretta da Roman Polanski per un profumo di lusso che in realtà non esiste."
];

// Capitolo 37: Doris Salcedo (indice 36)
allData[36].subtitle = "Mobili in legno pieni di cemento, la grande crepa Shibboleth alla Tate Modern e il silenzio per le vittime";
allData[36].summary = `### 1. Dati biografici e contesto: La Colombia e il dolore per i desaparecidos

Nata a Bogotá nel 1958, **Doris Salcedo** compie i suoi studi d'arte in Colombia prima di perfezionarsi a New York. Rientrata in patria, vive da vicino la tragedia delle guerre civili colombiane, segnate da decenni di violenze tra narcotrafficanti, gruppi paramilitari e forze statali, con migliaia di rapimenti e persone scomparse nel nulla (*desaparecidos*).

La sua scultura nasce dall'ascolto diretto e prolungato dei testimoni e delle famiglie delle vittime: Salcedo si mette al servizio del loro dolore per dare forma a una **scultura della memoria e del rispetto civile**.

---

### 2. Poetica: La materia silenziosa e gli oggetti della memoria

Salcedo rifiuta qualsiasi forma di monumento trionfale:
* **I mobili di casa sigillati nel cemento (*Atrabiliarios*, *La Casa Viuda*)**: raccoglie vecchi mobili in legno appartenuti alle famiglie delle vittime (armadi, comodini, tavoli, sedie) e **ne riempie i cassetti e le cavità con colate di cemento armato grigio**, inserendo all'interno vestiti usati, scarpe consumate o frammenti di ossa. Il mobile perde la sua apertura verso la vita e diventa una lapide muta, pesante e invalicabile.
* **Il valore del vuoto e dell'assenza**: nelle sue opere la persona scomparsa non viene mai ritratta fisicamente. È la pesantezza del cemento e l'inutilizzabilità dell'oggetto che rendono palpabile l'assenza improvvisa e dolorosa di chi non è più tornato a casa.

![Doris Salcedo, Shibboleth, 2007 - Spaccatura monumentale nel pavimento della Turbine Hall, Tate Modern, Londra](assets/corsi/dapl08/anno-2/storia-arte-2/images/salcedo_shibboleth.jpg)

---

### 3. Analisi delle opere cardine

#### Shibboleth (2007, Tate Modern, Londra)
* **Descrizione dell'opera monumentale**: Invitata a realizzare un'opera per la monumentale *Turbine Hall* della Tate Modern di Londra, Salcedo compie un gesto di straordinaria potenza: **apre una crepa profonda e frastagliata lunga 167 metri nel pavimento di cemento dell'edificio**.
* **Il significato della spaccatura**: Il termine biblico *Shibboleth* indica una parola d'ordine usata anticamente per riconoscere gli stranieri e gli intrusi. La crepa nel pavimento simboleggia la frattura invisibile ma profonda che divide il mondo ricco occidentale dai popoli poveri del Sud del mondo, denunciando il razzismo, la separazione sociale e il rifiuto dei migranti.
* **La cicatrice rimasta per sempre**: Al termine della mostra la crepa è stata riempita con una colata di cemento, lasciando sul pavimento una cicatrice visibile per sempre: a testimoniare che le ferite della storia non si cancellano facilmente.

#### Sedie al Palazzo di Giustizia di Bogotá (2002)
* Nel diciassettesimo anniversario del violento assalto al Palazzo di Giustizia di Bogotá, Salcedo cala lentamente centinaia di sedie di legno vuote lungo le pareti esterne dell'edificio per circa 53 ore consecutive, una per ogni persona uccisa nella tragedia, riempiendo il silenzio della piazza di commossa memoria civile.`;

allData[36].keyPoints = [
  "Doris Salcedo dà voce al dolore e alla memoria delle vittime della violenza civile e dei desaparecidos in Colombia.",
  "Raccoglie mobili domestici di legno usati e li sigilla con colate di cemento grigio inglobando abiti e ricordi.",
  "Con 'Shibboleth' (2007) apre una spaccatura lunga 167 metri nel pavimento della Tate Modern per denunciare il razzismo verso i migranti.",
  "La sua scultura rifiuta la retorica del monumento per trasformarsi in una silenziosa e partecipe presenza di rispetto."
];

// Capitolo 38: Thomas Hirschhorn (indice 37)
allData[37].subtitle = "Cartone, nastro adesivo marrone, fogli d'alluminio e monumenti temporanei nei quartieri popolari";
allData[37].summary = `### 1. Dati biografici e formazione: Dalla grafica all'energia dell'arte pubblica

Nato a Berna (Svizzera) nel 1957, **Thomas Hirschhorn** studia grafica pubblicitaria a Zurigo negli anni Settanta prima di trasferirsi a Parigi, dove lavora inizialmente all'interno di un collettivo di grafici comunisti. Questa esperienza lo porta a rifiutare l'arte come bene di lusso per ricchi collezionisti, scegliendo di creare installazioni ad altissima intensità usando **materiali poveri, precari e reperibili ovunque**.

---

### 2. Poetica: L'estetica del precario e i materiali quotidiani

Hirschhorn adotta una regola ferrea e rigorosa sui materiali:
* **Materiali comuni e non nobili**: usa solo materiali che chiunque può comprare a poco prezzo in una ferramenta o in un supermercato: **cartone ondulato, fogli di alluminio da cucina, compensato, plastica trasparente, fotocopie in bianco e nero e chilometri di nastro adesivo marrone da pacchi (*tape*)**.
* **Energia invece di qualità estetica formale**: Hirschhorn dichiara di non voler fare opere «belle» secondo le regole del museo, ma di voler generare **energia, dibattito e confronto critico**. Le sue opere sembrano barricate urbane o chioschi di fortuna fitti di testi filosofici, articoli di giornale e fotografie di guerra.

![Thomas Hirschhorn, Gramsci Monument, 2013 - Struttura in legno e nastro adesivo nel quartiere Bronx di New York](assets/corsi/dapl08/anno-2/storia-arte-2/images/hirschhorn_gramsci.jpg)

---

### 3. I Monumenti dedicati ai grandi filosofi nei quartieri popolari

La serie più celebre di Hirschhorn è costituita dai monumenti dedicati a grandi pensatori non collocati nei ricchi centri storici, ma costruiti **insieme agli abitanti delle periferie e delle case popolari**:
* **I quattro monumenti cardine**:
  1. *Spinoza Monument* (Amsterdam, 1999)
  2. *Deleuze Monument* (Avignone, 2000, in un quartiere a forte presenza operaia)
  3. *Bataille Monument* (Documenta 11 a Kassel, 2002, nel quartiere turco di Nordstadt)
  4. *Gramsci Monument* (New York, 2013, nel quartiere Forest Houses del Bronx)
* **Il Gramsci Monument nel Bronx (2013)**: dedicato al pensatore e politico antifascista italiano **Antonio Gramsci**. Costruito interamente in legno grezzo e nastro adesivo con l'aiuto dei residenti del quartiere, comprendeva una biblioteca con i libri di Gramsci, una radio web locale, un bar, una sala computer con internet gratuito e laboratori d'arte per i bambini.
* Al termine dei mesi di attività, la struttura è stata interamente smontata e i materiali riciclati o donati agli abitanti del quartiere: l'opera non è il monumento fisico fisso, ma l'incontro umano, la cultura condivisa e l'energia sociale nata durante la sua costruzione.`;

allData[37].keyPoints = [
  "Thomas Hirschhorn rifiuta i materiali nobili e crea opere usando solo cartone, alluminio, fotocopie e nastro adesivo da imballaggio.",
  "Dichiara di cercare l'energia e l'impegno critico del pubblico anziché la bellezza formale o decorativa.",
  "I suoi celebri monumenti ai filosofi (Spinoza, Deleuze, Bataille, Gramsci) sono costruiti nei quartieri popolari ed emarginati.",
  "Il 'Gramsci Monument' (2013 nel Bronx) era un centro sociale vivo con biblioteca, laboratori e radio gestiti insieme agli abitanti."
];

// Capitolo 39: Cao Fei (indice 38)
allData[38].subtitle = "Il boom industriale cinese, i giovani tra anime e cosplay, le fabbriche e la città virtuale RMB City";
allData[38].summary = `### 1. Dati biografici e contesto: La Cina del boom economico e della rete

Nata a Canton (Guangzhou) nel 1978, figlia di un illustre scultore accademico di regime, **Cao Fei** appartiene alla prima generazione di giovani cinesi cresciuta dopo le riforme economiche, testimone del vertiginoso passaggio della Cina da paese agricolo a fabbrica del mondo e superpotenza tecnologica.

La sua opera unisce video d'avanguardia, documentario, cinema, cultura dei giovani appassionati di cartoni animati (*cosplay*) e mondi virtuali digitali, raccontando con sensibilità e ironia le contraddizioni della società cinese contemporanea.

---

### 2. Le opere cardine: Tra fabbrica reale e sogni digitali

#### Rabid Dogs (Cani rabbiosi, 2002)
* Un video surreale e divertente in cui giovani impiegati di un'azienda moderna, elegantemente vestiti con completi a quadri del prestigioso marchio di moda Burberry, camminano a quattro zampe negli uffici abbaiando e comportandosi come cani feroci. L'opera ironizza sulla frenesia capitalista e sulla sottomissione al profitto aziendale.

#### Whose Utopia? (Di chi è l'utopia?, 2006)
![Cao Fei, Whose Utopia?, 2006 - Video a colori nella fabbrica Osram a Foshan](assets/corsi/dapl08/anno-2/storia-arte-2/images/cao_fei_utopia.jpg)

* **Descrizione del progetto**: Realizzato all'interno di una gigantesca fabbrica di lampadine (la Osram a Foshan), con migliaia di giovani operai emigrati dalle campagne cinesi. Cao Fei passa mesi nella fabbrica, parlando con i lavoratori e chiedendo loro quali siano i loro veri sogni e desideri.
* **La messa in scena dei sogni**: Nel video, improvvisamente, tra i rumori assordanti dei macchinari e i nastri trasportatori della catena di montaggio, alcuni operai iniziano a mettere in scena le proprie passioni personali: una ragazza balla in tutù sulle punte come una ballerina classica, un giovane suona la chitarra elettrica, un altro esegue mosse di kung-fu. L'opera restituisce dignità, poesia e umanità a persone altrimenti ridotte a semplici ingranaggi della produzione mondiale.

---

### 3. RMB City (2007-2011): La metropoli virtuale su Second Life

* **La fondazione della città digitale**: Quando la piattaforma virtuale online *Second Life* raggiunge il successo mondiale, Cao Fei crea il proprio alter-ego virtuale (chiamato *China Tracy*) e fonda una vera e propria città digitale chiamata **RMB City** (dal nome della moneta cinese, il Renminbi).
* **L'architettura fantastica**: RMB City galleggia sull'acqua come un immenso collage tridimensionale di tutti i simboli della nuova Cina: lo stadio «Nido d'uccello» di Pechino, una statua arrugginita di Mao che spunta dal mare, grattacieli futuristi, ciminiere e cantieri edili sempre aperti.
* **Un'anticipazione del Metaverso**: Per anni RMB City ha ospitato mostre d'arte virtuali, dibattiti, eventi e visite guidate con curatori e collezionisti da tutto il mondo, anticipando di quindici anni i temi contemporanei della vita nel mondo digitale e nel Metaverso.`;

allData[38].keyPoints = [
  "Cao Fei racconta la vertiginosa trasformazione della Cina contemporanea unendo video, cultura giovanile dei cosplay e internet.",
  "In 'Whose Utopia?' (2006) mostra i sogni artistici (danza classica, musica) dei giovani operai all'interno di una grande fabbrica di lampadine.",
  "In 'Rabid Dogs' ironizza sulla frenesia degli uffici moderni mostrando impiegati in abiti eleganti che si comportano come cani.",
  "Con la città virtuale 'RMB City' (2007-2011) su Second Life anticipa di molti anni il dibattito contemporaneo sul Metaverso."
];

// Capitolo 40: Gregor Schneider e Piotr Uklański (indice 39)
allData[39].subtitle = "Le stanze labirintiche di Gregor Schneider e le 164 fotografie di attori in uniforme nazista di Uklański";
allData[39].summary = `### 1. Due percorsi a confronto alle Biennali del nuovo millennio

All'inizio degli anni Duemila due artisti europei scuotono il dibattito internazionale affrontando lo spazio fisico e i fantasmi della storia recente: il tedesco **Gregor Schneider** (Leone d'Oro alla Biennale di Venezia del 2001) e il polacco **Piotr Uklański**, maestro delle provocazioni visive tra arte concettuale e cinema.

---

### 2. Gregor Schneider e l'ossessione di Haus u r: L'inquietudine dello spazio di casa

A partire dal 1985, ad appena sedici anni, Gregor Schneider compie un'opera ossessiva e impressionante all'interno della casa di famiglia ereditata a **Rheydt** (in Germania, abbreviata con la sigla *u r*):
* **Costruire stanze dentro le stanze preesistenti**: l'artista non si limita a ridipingere la casa, ma comincia a **costruire nuove stanze all'interno di quelle già esistenti**. Inserisce doppie pareti in cartongesso e piombo a pochi centimetri da quelle vecchie, abbassa i soffitti, monta doppie finestre illuminate con lampade elettriche che imitano la luce del giorno e crea stanze completamente insonorizzate dove non si sente alcun rumore.
* **Le stanze rotanti**: alcuni ambienti vengono montati su perni meccanici che ruotano lentissimamente senza farsi notare, facendo perdere completamente l'orientamento a chi vi entra.

![Gregor Schneider, Totes Haus u r, 2001, Padiglione Germania, 49ª Biennale di Venezia (Leone d'Oro)](assets/corsi/dapl08/anno-2/storia-arte-2/images/schneider_totes_haus.jpg)

* **Il trionfo alla Biennale di Venezia (2001)**: invitato a rappresentare la Germania, Schneider smonta 24 stanze della sua casa di Rheydt (pesanti decine di tonnellate), le trasporta a Venezia su grandi barche e le rimonta dentro il severo e monumentale **Padiglione Germania** ai Giardini (un padiglione fatto ristrutturare da Adolf Hitler nel 1938). I visitatori entravano da una normale porta di casa e si perdevano in un labirinto soffocante di corridoi ciechi, porte che davano su muri e pavimenti scricchiolanti, vivendo in prima persona il concetto del **perturbante** (la casa che da rifugio sicuro diventa una trappola misteriosa).

---

### 3. Piotr Uklański: La seduzione del fascismo al cinema e la pista da ballo

Piotr Uklański indaga con coraggio e ironia come i mass media e il cinema trattino i temi della colpa storica e del divertimento:

#### The Nazis (I nazisti, 1998)
![Piotr Uklański, The Nazis, 1998, 164 fotografie di attori in uniformi naziste](assets/corsi/dapl08/anno-2/storia-arte-2/images/uklanski_the_nazis.jpg)

* **Descrizione dell'opera**: Uklański raccoglie ed espone in una lunga fila sulle pareti 164 fotografie a colori di **celebri attori del cinema occidentale** (come Marlon Brando, Clint Eastwood, Michael Caine) mentre interpretano ufficiali o soldati delle SS in famosi film di guerra europei e americani. Tutti appaiono virili, eleganti, affascinanti e carismatici nelle loro perfette uniformi nere.
* **Il significato concettuale**: L'opera suscitò grandi polemiche e scandali (a Varsavia un famoso attore entrò nella galleria con una sciabola e tagliò il proprio ritratto). Lo scopo di Uklański non era affatto esaltare il nazismo, ma compiere una severa denuncia: mostrare come il cinema di Hollywood e la cultura dello spettacolo abbiano reso affascinante e seducente l'immagine della peggiore tirannia della storia per vendere biglietti al cinema.

#### Untitled (Dance Floor) (1996)
* Uklański costruisce una vera e propria pista da ballo da discoteca perfettamente funzionante, con pannelli di vetro trasparenti illuminati dal basso da luci colorate che pulsano a ritmo di musica. L'opera unisce ironicamente il rigore geometrico del Minimalismo storico alla voglia di divertimento e ballo della musica disco, trasformando il silenzio del museo in una festa vivace.`;

allData[39].keyPoints = [
  "Gregor Schneider vince il Leone d'Oro a Venezia nel 2001 ricostruendo 24 stanze della sua casa natale ('Totes Haus u r') dentro il Padiglione Germania.",
  "La sua opera esplora il Perturbante (Unheimliche) attraverso doppie pareti, stanze cieche e corridoi insonorizzati che disorientano chi vi entra.",
  "Piotr Uklański con 'The Nazis' (1998) espone 164 ritratti di star del cinema in uniforme delle SS per denunciare come i film abbiano reso affascinante il male.",
  "Con 'Dance Floor' (1996) trasforma la griglia geometrica della scultura moderna in una vera pista da ballo luminosa da discoteca."
];

// Salva i dati aggiornati
const output = 'window.ARTE_DATA = ' + JSON.stringify(allData, null, 2) + ';\n';
fs.writeFileSync(dataFilePath, output, 'utf8');
console.log('Module 3 (Capitoli 34-40) aggiornato e semplificato con successo!');
