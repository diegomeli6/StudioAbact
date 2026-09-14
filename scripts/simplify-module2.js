const fs = require('fs');
const path = require('path');

const dataFilePath = path.join(__dirname, '..', 'data', 'arte-data.js');
let fileContent = fs.readFileSync(dataFilePath, 'utf8');

const sandbox = { window: {} };
eval(fileContent.replace('window.ARTE_DATA', 'sandbox.window.ARTE_DATA'));
const allData = sandbox.window.ARTE_DATA;

// Capitolo 20: Il Mondo Post-1989 e la Svolta Globale (indice 19)
allData[19].subtitle = "Il crollo del Muro di Berlino, la fine della Guerra Fredda, la nascita delle biennali nel mondo e la globalizzazione";
allData[19].summary = `### 1. Il 1989 come svolta storica: Dalla Guerra Fredda al mondo globale

![Panorama storico-artistico degli Anni Novanta: la caduta del Muro di Berlino, la globalizzazione e la nascita delle biennali periferiche](assets/corsi/dapl08/anno-2/storia-arte-2/images/svolta_post1989_globale.jpg)

Nel suo saggio introduttivo, il critico **Francesco Bernardelli** individua nel **1989** l'anno di svolta fondamentale che segna il passaggio definitivo dal Novecento al mondo contemporaneo di oggi:
* Il **9 novembre 1989 crolla il Muro di Berlino**: si dissolve l'Unione Sovietica e finisce la divisione del mondo in due blocchi contrapposti (la Guerra Fredda) che aveva segnato la politica internazionale per quasi mezzo secolo.
* La fine di questa contrapposizione accelera la **globalizzazione economica, tecnologica e della comunicazione**: nasce e si diffonde la rete Internet (World Wide Web), aumentano i viaggi e gli scambi internazionali di persone e capitali, e si aprono al mercato globale l'Europa dell'Est, l'Asia e l'America Latina.
* Nel mondo dell'arte cade per sempre il monopolio esclusivo delle sole capitali occidentali tradizionali (Parigi, Londra, New York): **si conclude l'epoca dell'eurocentrismo** e si apre uno scenario globale con molti centri culturali diversi in tutto il pianeta.

---

### 2. Dalle metropoli occidentali alla rete delle 'Biennali nel mondo'

Negli anni Novanta la geografia del sistema dell'arte si trasforma profondamente:
* Se prima Parigi e New York erano state le uniche capitali indiscusse dell'arte moderna, gli anni Novanta vedono l'esplosione delle **grandi Biennali d'arte nei paesi emergenti e nel Sud del mondo**: la Biennale dell'Avana (Cuba), la Biennale di Johannesburg in Sudafrica (curata da Okwui Enwezor nel 1997), la Biennale di Gwangju in Corea del Sud, la Biennale di Istanbul in Turchia e la Biennale di San Paolo in Brasile.
* Queste grandi rassegne non celebrano più i vecchi padiglioni divisi per nazioni in stile ottocentesco, ma diventano luoghi di incontro internazionale aperti al **dialogo e al superamento del colonialismo culturale**, dando finalmente voce ad artisti africani, asiatici, mediorientali e latinoamericani che raccontano la propria storia e la propria identità.

---

### 3. I grandi temi della ricerca artistica degli anni Novanta

I filoni fondamentali che hanno trasformato l'arte degli anni Novanta comprendono:
1. **Multiculturalismo e studi post-coloniali**: riscrittura della storia e della cultura da parte dei popoli che erano stati colonizzati, per superare i pregiudizi occidentali.
2. **Identità, corpo e la tragedia dell'AIDS**: il corpo umano vissuto come luogo di diritti civili, fragilità fisica e memoria delle vittime dell'epidemia.
3. **Il fenomeno del Post Human (1992)**: la riflessione curata da Jeffrey Deitch su come chirurgia estetica, genetica, farmaci e protesi tecnologiche stiano modificando il corpo umano.
4. **L'Estetica Relazionale (1998)**: la teoria di Nicolas Bourriaud secondo cui l'opera non è più un semplice oggetto da ammirare da lontano, ma un'occasione concreta per far incontrare, dialogare e convivere le persone.
5. **Nuovi media e videoinstallazioni immersive**: l'immagine in movimento su grandi schermi invade i musei, offrendo al pubblico esperienze visive e sensoriali avvolgenti.`;

allData[19].keyPoints = [
  "Il 1989 (caduta del Muro di Berlino e fine della Guerra Fredda) segna l'inizio dell'arte contemporanea globale.",
  "Finisce il dominio esclusivo dell'Occidente e si apre una geografia dell'arte con molti centri in tutto il mondo.",
  "Le Biennali internazionali nel Sud del mondo (Johannesburg, L'Avana, Istanbul, Gwangju) danno voce a culture a lungo trascurate.",
  "I temi cardine del decennio sono: multiculturalismo, studi post-coloniali, lotta all'AIDS, Post Human ed Estetica Relazionale."
];

// Capitolo 21: Multiculturalismo e Decolonizzazione (indice 20)
allData[20].subtitle = "I manichini vestiti di tessuti africani di Shonibare e i disegni a carboncino cancellati di Kentridge";
allData[20].summary = `### 1. Il contesto: Riscrivere la storia oltre il colonialismo

Negli anni Novanta il dibattito culturale internazionale mette al centro la critica del colonialismo europeo. Artisti provenienti dall'Africa, dall'Asia e dalle comunità della diaspora usano l'arte per svelare le contraddizioni della dominazione occidentale, mescolando ironia, storia e memoria dolorosa.

---

### 2. Yinka Shonibare: I tessuti wax e la parodia del potere aristocratico

Nato a Londra nel 1962 da genitori nigeriani e cresciuto tra Lagos e la capitale britannica, **Yinka Shonibare** crea installazioni spettacolari e ironiche che mettono in discussione i concetti di razza, classe sociale e identità:
* **I tessuti 'olandesi' africani (*Dutch Wax Fabrics*)**: Shonibare veste i suoi personaggi con stoffe dai colori vivaci e fantasie geometriche, comunemente considerate il simbolo tipico dell'identità africana. In realtà questi tessuti hanno una storia complessa e globale: inventati in Indonesia, furono prodotti industrialmente dagli olandesi e dagli inglesi nel corso dell'Ottocento e venduti nei mercati dell'Africa occidentale. Il tessuto stesso dimostra che l'identità pura non esiste, ma è sempre il frutto di scambi e incroci storici.
* **I manichini aristocratici decapitati**: Shonibare ricrea scene tipiche della nobiltà europea settecentesca e vittoriana (battute di caccia, balli di corte, incontri galanti) usando manichini vestiti con sfarzosi abiti d'epoca realizzati in tessuto wax africano. I manichini sono sistematicamente **senza testa**: un riferimento alla ghigliottina della Rivoluzione Francese e al tempo stesso un modo per cancellare qualsiasi tratto somatico razziale, rendendo universale la critica all'arroganza del potere.

![Yinka Shonibare, The Swing (after Fragonard), 2001 - Manichino senza testa, tessuto wax africano, Tate Modern](assets/corsi/dapl08/anno-2/storia-arte-2/images/shonibare_the_swing.jpg)

* **Descrizione dell'opera cardine**: Ispirata al celebre dipinto rococò *L'altalena* di Jean-Honoré Fragonard, l'installazione mostra una fanciulla aristocratica senza testa che dondola su un'altalena tra rami fioriti, vestita con un sontuoso abito confezionato in tessuto wax. L'opera unisce l'eleganza frivola della corte francese allo sfruttamento delle colonie su cui quella ricchezza era fondata.

---

### 3. William Kentridge: La memoria dell'Apartheid e il disegno cancellato

Nato a Johannesburg nel 1955 in una famiglia di illustri avvocati ebrei impegnati nella difesa dei diritti dei neri sudafricani (il padre difese Nelson Mandela), **William Kentridge** è uno dei più grandi artisti e registi del nostro tempo:
* **L'animazione a carboncino cancellato (*Drawings for Projection*)**: Kentridge inventa una tecnica di animazione poetica e personalissima. Realizza un grande disegno a carboncino e pastello su carta, ne filma un fotogramma con la cinepresa, poi cancella parzialmente il disegno con una gomma, lo modifica leggermente e ne filma un altro fotogramma.
* **La memoria delle cancellature**: sulla carta rimangono sempre le ombre e gli aloni delle figure precedenti (come in una lavagna cancellata male). Questo processo visivo diventa la metafora perfetta della memoria storica: la storia e le ingiustizie dell'**Apartheid** in Sudafrica non possono essere cancellate con un colpo di spugna, ma lasciano sempre una cicatrice visibile sul corpo della società.
* **I personaggi simbolo**: attraverso i personaggi di Soho Eckstein (l'imprenditore senza scrupoli della finanza mineraria) e Felix Teitlebaum (il poeta sensibile e sognatore), Kentridge racconta il senso di colpa, la violenza e la speranza di riconciliazione del popolo sudafricano.`;

allData[20].keyPoints = [
  "Yinka Shonibare usa i tessuti africani di produzione olandese (Dutch Wax) per dimostrare che le identità culturali sono frutti di contaminazioni storiche.",
  "I suoi manichini senza testa vestiti con abiti vittoriani criticano con ironia il potere coloniale e l'aristocrazia europea.",
  "William Kentridge crea celebri film d'animazione modificando e cancellando a mano grandi disegni a carboncino.",
  "Le tracce e gli aloni lasciati dalle cancellature di Kentridge simboleggiano le cicatrici indelebili dell'Apartheid in Sudafrica."
];

// Capitolo 22: Gabriel Orozco e Mona Hatoum (indice 21)
allData[21].subtitle = "La poesia degli oggetti trovati di Orozco e gli utensili domestici minacciosi di Mona Hatoum";
allData[21].summary = `### 1. Due sguardi sulla realtà quotidiana

Negli anni Novanta due artisti di fama internazionale rinnovano profondamente la scultura contemporanea partendo da oggetti comuni: il messicano **Gabriel Orozco** con interventi minimi e poetici durante i suoi viaggi, e la palestinese-britannica **Mona Hatoum** trasformando gli arredi della casa in oggetti inquietanti e carichi di tensione.

---

### 2. Gabriel Orozco: Il viaggiatore nomade e l'arte degli scarti quotidiani

Nato in Messico nel 1962, **Gabriel Orozco** rifiuta di avere uno studio fisso: lavora viaggiando per il mondo, usando la strada, i mercati e gli spazi pubblici come suo laboratorio continuo:
* **Interventi minimi e poetici**: Orozco non crea monumenti pesanti, ma compie azioni leggere e temporanee con oggetti trovati per caso: lascia un'arancia sul tavolo di un mercato vuoto in Brasile, raccoglie sabbia bagnata su una spiaggia, o fa rotolare per le strade di New York una grande palla di plastilina grigia (*Piedra que cede*, 1992) che raccoglie polvere, cicche e detriti della metropoli.
* **La DS (1993)**: la sua scultura più famosa nasce tagliando una classica automobile Citroën DS in tre parti longitudinali, eliminando la sezione centrale di 60 centimetri e incollando di nuovo insieme le due parti laterali. L'automobile diventa una scultura stretta e aerodinamica a un solo posto, che conserva l'eleganza della forma ma perde del tutto la sua funzione pratica di veicolo per famiglie.

![Mona Hatoum, In Divan / Homebound - Oggetti domestici elettrificati e gabbie di metallo](assets/corsi/dapl08/anno-2/storia-arte-2/images/hatoum_homebound.jpg)

---

### 3. Mona Hatoum: La casa come luogo di pericolo e minaccia

Nata a Beirut nel 1952 da genitori palestinesi in esilio, rifugiatasi a Londra nel 1975 allo scoppio della guerra civile libanese, **Mona Hatoum** porta nella scultura il senso di sradicamento e di pericolo che segna la vita dei rifugiati:
* **La casa non più come rifugio, ma come minaccia**: per Hatoum la casa non è il nido sicuro della famiglia, ma un luogo di prigionia e ansia. L'artista utilizza il concetto psicologico del **'perturbante'** (quella sensazione di profonda inquietudine che proviamo quando un oggetto consueto e familiare si rivela improvvisamente minaccioso ed estraneo).
* **Utensili da cucina giganti e pericolosi**: ingrandisce a dismisura colapasta, grattugie da parmigiano e tritacarne, trasformandoli in barriere metalliche taglienti che ricordano strumenti di tortura o gabbie carcerarie.
* **Homebound (2000)**: un'intera stanza di casa arredata con sedie, tavoli, culle per bambini e utensili da cucina collegati tra loro da fili elettrici in cui scorre **corrente elettrica ad alto voltaggio**. I fili e le lampadine si accendono e ronzano a intermittenza: il visitatore è separato dall'ambiente da una barriera di filo spinato, avvertendo il pericolo mortale che si nasconde nella vita domestica.`;

allData[21].keyPoints = [
  "Gabriel Orozco lavora come un viaggiatore senza studio fisso, creando sculture poetiche con materiali trovati e azioni minime.",
  "La sua celebre 'DS' (1993) taglia e restringe una Citroën DS trasformando un'auto famosa in una scultura futuribile ma inservibile.",
  "Mona Hatoum trasforma gli oggetti di casa in sculture inquietanti, riflettendo sull'esilio e sul senso di pericolo.",
  "In 'Homebound' elettrifica mobili e utensili da cucina con corrente ad alto voltaggio, trasformando il rifugio domestico in una gabbia rischiosa."
];

// Capitolo 23: Felix Gonzalez-Torres (indice 22)
allData[22].subtitle = "Il dono al pubblico, i mucchi di caramelle, gli orologi sincronizzati e il lutto per l'AIDS";
allData[22].summary = `### 1. Dati biografici e contesto: L'amore e la perdita nell'era dell'AIDS

Nato a Cuba nel 1957, trasferitosi prima a Porto Rico e poi a New York nel 1979, **Felix Gonzalez-Torres** è una delle figure più commoventi e rivoluzionarie dell'arte contemporanea. La sua opera nasce nel pieno della drammatica epidemia di AIDS degli anni Ottanta e Novanta, che colpisce a morte la comunità omosessuale e porta via nel 1991 il suo amatissimo compagno Ross Laycock, prima che lo stesso artista muoia per le complicazioni del virus nel 1996 a soli trentotto anni.

Rifiutando i toni urlati della semplice protesta politica, Gonzalez-Torres inventa una forma d'arte delicatissima, capace di fondere il rigore geometrico del Minimalismo con la tenerezza dell'amore, del dono e della perdita.

---

### 2. Poetica: La scultura come dono che si consuma

La grande rivoluzione di Gonzalez-Torres è la trasformazione della scultura in un **gesto di generosità e partecipazione attiva**:
* **I mucchi di caramelle (*Candy Spills*)**: grandi accumuli di caramelle avvolte in carta colorata luccicante adagiate negli angoli dei musei o distese come tappeti sul pavimento.
  * In *«Untitled» (Portrait of Ross in L.A.)* del 1991, il mucchio di caramelle pesa esattamente **79 chili**, pari al peso ideale del corpo del suo compagno Ross prima che la malattia lo consumasse.
  * **Il pubblico è invitato a prendere una caramella e mangiarla**: man mano che i visitatori portano via le caramelle, il mucchio si riduce di peso e svanisce lentamente, riproducendo sotto gli occhi di tutti il dimagrimento e la perdita del corpo dell'amato. Tuttavia il museo ha l'obbligo di rifornire continuamente le caramelle, trasformando l'opera in un ciclo eterno di morte e risurrezione attraverso il dono.
* **Le pile di poster di carta (*Paper Stacks*)**: alte cataste di fogli stampati con scritte poetiche o fotografie di cieli con uccelli in volo. Chiunque può staccare un foglio e portarlo gratuitamente a casa con sé, diffondendo l'opera d'arte nel mondo reale.

![Felix Gonzalez-Torres, «Untitled» (Perfect Lovers), 1991 - Due orologi sincronizzati a parete](assets/corsi/dapl08/anno-2/storia-arte-2/images/gonzalez_torres_lovers.jpg)

---

### 3. I due orologi e i fili di lampadine

* **«Untitled» (Perfect Lovers, Amanti perfetti, 1991)**: due orologi commerciali a batteria identici sono appesi l'uno accanto all'altro sulla parete, perfettamente allineati e sincronizzati all'inizio sullo stesso identico secondo. Con il passare dei giorni e dei mesi, inevitabilmente uno dei due orologi comincerà a perdere qualche frazione di secondo fino a fermarsi per primo, mentre l'altro continuerà a battere il tempo da solo: una metafora limpida e straziante del legame d'amore, del tempo condiviso e della separazione che la morte impone.
* **I fili di lampadine luminose**: lunghe catene di lampadine accese appese al soffitto che cadono sul pavimento come cascate di luce, accogliendo il pubblico in un abbraccio caloroso e intimo.`;

allData[22].keyPoints = [
  "Felix Gonzalez-Torres affronta il tema dell'amore, della malattia e del lutto per l'AIDS con sculture poetiche e partecipative.",
  "Nei suoi mucchi di caramelle il pubblico è invitato a prendere e consumare una caramella, vivendo fisicamente l'idea della perdita e del dono.",
  "Il peso ideale di 79 kg delle caramelle in 'Portrait of Ross in L.A.' corrisponde al corpo sano dell'amato prima della malattia.",
  "In 'Perfect Lovers' due orologi sincronizzati battono il tempo insieme fino a quando uno si ferma, toccante simbolo dell'amore e della morte."
];

// Capitolo 24: Identità, Genere e Conflitto (indice 23)
allData[23].subtitle = "Le donne armate con testi poetici di Shirin Neshat e le silhouette di carta nera di Kara Walker";
allData[23].summary = `### 1. Il corpo femminile tra religione, razzismo e memoria storica

Negli anni Novanta la riflessione sulla condizione delle donne assume una forza straordinaria grazie a due grandi artiste che affrontano temi storici cruciali: l'iraniana **Shirin Neshat**, con lo sguardo sulla rivoluzione islamica e il ruolo della donna in Medio Oriente, e l'afroamericana **Kara Walker**, con la memoria della schiavitù e delle piantagioni del Sud degli Stati Uniti.

---

### 2. Shirin Neshat: Il velo, la poesia persiana e il fuoco delle armi

Nata in Iran nel 1957 in una famiglia benestante e trasferitasi giovanissima negli Stati Uniti nel 1974 per studiare arte, **Shirin Neshat** fa ritorno nel suo paese d'origine solo nel 1990, dopo la Rivoluzione Islamica del 1979 e la sanguinosa guerra tra Iran e Iraq. Trova una società completamente cambiata, dove le donne sono obbligate a indossare il velo nero integrale (*chador*) e sottomesse a rigide leggi religiose.

* **La serie fotografica Women of Allah (1993-1997)**: autoritratti e ritratti fotografici in bianco e nero nitidissimo, costruiti attraverso la combinazione di quattro elementi fondamentali:
  1. **Il Chador**: il velo nero che copre interamente la testa e il corpo, lasciando visibili solo il viso, gli occhi, le mani e i piedi nudi.
  2. **La Calligrafia in lingua farsi**: Neshat scrive a mano con inchiostro direttamente sulla superficie delle fotografie poesie di celebri poetesse iraniane contemporanee (come Forugh Farrokhzad), che parlano di fede, desiderio, coraggio e amore.
  3. **L'Arma da fuoco**: canne di fucili o pistole che spuntano dal velo, dividendo il viso a metà o impugnate con fierezza.
  4. **Lo Sguardo diretto**: gli occhi delle donne guardano dritto nell'obiettivo senza alcuna paura o sottomissione.
* **Significato profondo**: l'opera non è una semplice condanna occidentale del velo né una glorificazione del fondamentalismo: mostra la complessità dolorosa delle donne divise tra fede religiosa, patriarcato e desiderio di libertà. Dalla fine degli anni Novanta passa al video (*Turbulent*, 1998, Leone d'Oro a Venezia; *Rapture*) e al cinema (*Donne senza uomini*, Leone d'Argento a Venezia 2009).

![Kara Walker, Camptown Ladies / Insurrection - Silhouette di carta nera su parete](assets/corsi/dapl08/anno-2/storia-arte-2/images/kara_walker_silhouette.jpg)

---

### 3. Kara Walker: Le silhouette nere e gli orrori della schiavitù americana

Nata in California nel 1969 e trasferitasi da adolescente in Georgia, nel profondo Sud degli Stati Uniti, **Kara Walker** esplora le radici mai rimarginate del razzismo americano:
* **La tecnica delle sagome nere ritagliate (*Cut-paper Silhouettes*)**: Walker riprende una tipica tecnica decorativa e borghese dell'Ottocento, il ritaglio di sagome di carta nera incollate su pareti bianche.
* **La violenza dietro l'eleganza fiabesca**: a un primo sguardo da lontano le pareti sembrano raffigurare scene fiabesche di dame in abiti ampi, bambini e paesaggi con salici piangenti. Avvicinandosi, lo spettatore scopre con orrore scene esplicite di violenza brutale, stupri, linciaggi, mutilazioni e torture perpetrate dai padroni bianchi contro gli schiavi neri nelle piantagioni di cotone.
* **Significato critico**: Walker usa uno stile apparentemente grazioso e d'epoca per costringere il pubblico contemporaneo a guardare in faccia i fantasmi della storia americana e la violenza del razzismo che ancora persiste oggi.`;

allData[23].keyPoints = [
  "Shirin Neshat indaga la condizione femminile nell'Islam post-rivoluzionario con la celebre serie fotografica 'Women of Allah'.",
  "Nelle sue immagini combina quattro simboli chiave: il velo (chador), la calligrafia poetica persiana, le armi e lo sguardo fiero.",
  "Kara Walker utilizza la raffinata tecnica ottocentesca delle sagome di carta nera ritagliate su sfondo bianco.",
  "Dietro la grazia visiva delle sagome, la Walker mette a nudo l'orrore, le torture e gli abusi della schiavitù nel Sud americano."
];

// Capitolo 25: Kiki Smith e Robert Gober (indice 24)
allData[24].subtitle = "La cera d'api, i fluidi del corpo umano, i lavandini ciechi e le gambe che spuntano dai muri";
allData[24].summary = `### 1. Kiki Smith: La fragilità anatomica, la cera d'api e i fluidi vitali

![Kiki Smith, Senza Titolo, 1987-1990 - Cera d'api, pigmenti e garza su supporto modellato](assets/corsi/dapl08/anno-2/storia-arte-2/images/kiki_smith_scultura.jpg)

![Robert Gober, Untitled (Sink), 1985 - Gesso, legno, acciaio e pittura semi-lucida, 1990 - Cera d'api, capelli e pigmenti](assets/corsi/dapl08/anno-2/storia-arte-2/images/gober_sink_torso.jpg)

Nata a Norimberga nel 1954 da padre scultore minimalista (Tony Smith) e cresciuta negli Stati Uniti, **Kiki Smith** compie una ricerca che ribalta del tutto la fredda perfezione geometrica della scultura moderna:
* **La riscoperta della fragilità del corpo**: formatasi anche come soccorritrice paramedica per studiare da vicino l'anatomia umana, Smith mette al centro del suo lavoro il **corpo umano fragile, mortale, malato e vulnerabile**.
* **I fluidi corporei e la rottura dei tabù**: alla fine degli anni Ottanta, nel pieno della tragedia dell'AIDS, porta alla luce ciò che la società tende a nascondere: sangue, latte materno, lacrime, urina e liquidi organici. Crea vasi da farmacia in vetro trasparente incisi con i nomi dei fluidi vitali (*Game of Loss*, 1991).
* **Materiali delicati e artigianali**: modella figure umane a grandezza naturale usando **cera d'api vergine, fogli di carta giapponese stratificati, bronzo grezzo, porcellana e tessuti**.
* In capolavori come *Tale* (1992), una donna di cera nuda cammina a quattro zampe trascinando dietro di sé una traccia visibile delle sue ferite; non c'è volgarità, ma la celebrazione toccante della sacralità della vita umana e della nostra comune natura biologica.

---

### 2. Robert Gober: I lavandini senza scarico e l'inquietudine della memoria

Nato nel Connecticut nel 1954 da famiglia di origini italo-americane e cresciuto in una severa educazione cattolica, **Robert Gober** crea sculture cariche di mistero, colpa e tensione emotiva:

* **I lavandini modellati a mano (*Sinks*)**: a metà degli anni Ottanta realizza grandi lavandini bianchi in gesso, legno, rete metallica e vernice. A prima vista sembrano comuni sanitari industriali già pronti, ma sono in realtà **modellati a mano con cura infinita**:
  * I lavandini sono sistematicamente **senza rubinetti e senza fori di scarico**: l'acqua (simbolo del battesimo, della pulizia e del perdono dei peccati) non può scorrere né lavare nulla. Diventano simboli muti di colpa, sterilità e purificazione impossibile.
* **Le gambe umane di cera che spuntano dalle pareti**: dagli anni Novanta modella realistiche gambe maschili in cera d'api, complete di scarpe di cuoio, calzini e veri peli umani impiantati a mano uno ad uno, che **sbucano misteriosamente dal battiscopa delle pareti del museo**.
* Gober affronta il senso di colpa, la paura dell'AIDS e la discriminazione dell'omosessualità unendo l'inquietudine surreale di Magritte al rigore formale delle forme pure.`;

allData[24].keyPoints = [
  "Kiki Smith studia la fragilità anatomica del corpo umano, lavorando con materiali sensibili come cera d'api, carta e bronzo.",
  "Supera i tabù sociali mostrando la realtà dei fluidi corporei (sangue, lacrime, latte) nel contesto drammatico dell'AIDS.",
  "Robert Gober realizza a mano finti lavandini in gesso privi di fori e rubinetti, simboli di colpa e impossibile purificazione.",
  "Le sue realistiche gambe di cera che spuntano dalle pareti fondono mistero surreale, memoria cattolica e identità personale."
];

// Capitolo 26: Il Fenomeno 'Post Human' di Jeffrey Deitch (1992) (indice 25)
allData[25].subtitle = "Il corpo modificabile tra biotecnologie, interventi chirurgici, protesi e figura del cyborg";
allData[25].summary = `### 1. La mostra manifesto: FAE Musée d'Art Contemporain di Losanna (1992)

![Mostra Post Human (1992, a cura di Jeffrey Deitch) - La ridefinizione del corpo umano tra biotecnologie e mutazione estetica](assets/corsi/dapl08/anno-2/storia-arte-2/images/post_human_deitch.jpg)

Nel 1992 il critico e curatore d'arte americano **Jeffrey Deitch** organizza a Losanna (mostra poi ospitata in Italia al Castello di Rivoli a Torino, ad Atene e ad Amburgo) un'esposizione fondamentale destinata a dare il nome a un'intera epoca: **Post Human** (Oltre l'umano).

La tesi centrale di Deitch è chiarissima:
* L'evoluzione naturale dell'uomo secondo le leggi tradizionali è giunta al capolinea: stiamo entrando in una **fase post-biologica**, in cui il corpo umano non è più un dato di natura immutabile, ma una **materia artificiale che può essere riprogrammata e modificata** attraverso la scienza e la tecnologia.
* Tre grandi forze guidano questo cambiamento epocale:
  1. **La chirurgia estetica di massa**: la modifica programmata del viso e del corpo per assomigliare a modelli visivi ideali e virtuali.
  2. **L'ingegneria genetica e le biotecnologie**: lo studio del DNA, la clonazione (la pecora Dolly sarà clonata nel 1996) e i farmaci moderni per il controllo dell'umore (come il Prozac).
  3. **Il cyborg e le protesi digitali**: l'integrazione sempre più stretta tra corpo vivente e computer, organi artificiali e protesi tecnologiche.

---

### 2. Gli artisti protagonisti della mutazione

La mostra *Post Human* riunisce 36 artisti internazionali che raccontano la nascita di questo «nuovo corpo» artificiale:
* **Matthew Barney**: esplora il corpo degli atleti, i muscoli potenziati e materiali sintetici come silicone, teflon e vaselina.
* **Cindy Sherman**: presenta le *Sex Pictures*, con manichini da laboratorio anatomico smembrati che svelano come la pornografia riduca il corpo a un semplice meccanismo privo di anima.
* **Charles Ray**: realizza manichini realistici ma sconcertanti, come *Family Romance* (1993), dove padre, madre, figlio e figlia hanno tutti esattamente la stessa altezza di 135 centimetri, o manichini maschili con i genitali completamente cancellati.
* **Paul McCarthy e Mike Kelley**: svelano i traumi e le paure nascoste della cultura americana usando peluche usati, manichini animati e performance estreme.
* **ORLAN**: artista francese pioniera della *Body Art chirurgica*, che trasforma la sala operatoria nel proprio studio d'arte, facendosi innestare protesi di silicone sotto la pelle per rimodellare il volto secondo le figure della pittura classica.

---

### 3. Tra promessa e incubo: Il doppio volto del Post Human

Questa trasformazione del corpo genera sentimenti opposti:
* Da un lato, la **speranza**: vincere le malattie genetiche, ritardare l'invecchiamento, potenziare le capacità umane e superare le barriere rigide tra i generi.
* Dall'altro, il **rischio inquietante**: la perdita dell'empatia umana, l'omologazione a canoni di bellezza artificiali dettati dalla televisione e la trasformazione del corpo umano in un prodotto commerciale brevettato dalle grandi multinazionali.`;

allData[25].keyPoints = [
  "La storica mostra 'Post Human' (curata da Jeffrey Deitch nel 1992 a Losanna e al Castello di Rivoli) annuncia l'era del corpo modificabile.",
  "L'evoluzione naturale viene affiancata da biotecnologie, chirurgia plastica, genetica e protesi informatiche (cyborg).",
  "Tra gli artisti chiave spiccano Matthew Barney, Cindy Sherman, Charles Ray, Paul McCarthy, Mike Kelley e ORLAN.",
  "Il corpo umano cessa di essere immutabile e diventa una materia sintetica plasmabile dalla tecnologia e dal mercato."
];

// Capitolo 27: Matthew Barney: L'Epica del Cremaster Cycle (indice 26)
allData[26].subtitle = "I cinque film epici, il muscolo cremastere, la vaselina e la grande mitologia contemporanea";
allData[26].summary = `### 1. Dati biografici e formazione: Dall'atletismo all'arte totale

Nato a San Francisco nel 1967 e cresciuto nell'Idaho, **Matthew Barney** unisce da giovane la passione per lo sport agonistico (giocatore di football americano) allo studio dell'arte e della medicina a Yale. Questa formazione insolita lo porta a concepire la scultura e l'arte come un **allenamento estremo del corpo umano**: la massa muscolare cresce solo se sottoposta a resistenza e sforzo, e allo stesso modo la forma artistica nasce dalla tensione fisica e dal superamento dei limiti.

---

### 2. Il Cremaster Cycle (1994-2002): Un'epopea visiva in cinque capitoli

Tra il 1994 e il 2002 Barney realizza la sua opera monumentale, il **Cremaster Cycle**, un ciclo di cinque lungometraggi filmici (numerati non in ordine cronologico ma biologico: *Cremaster 4, 1, 5, 2, 3*) che compongono una colossale mitologia contemporanea:
* **L'origine biologica del titolo**: il termine deriva dal muscolo *cremastere*, il muscolo involontario che regola la salita o la discesa dei testicoli in risposta alla temperatura o alle emozioni. Nelle prime settimane di vita del feto umano, prima che il sesso maschile o femminile si sia definito, il cremastere rappresenta la condizione potenziale in cui tutto è ancora aperto.
* **L'esplorazione della metamorfosi**: il ciclo filmico racconta il passaggio dallo stato biologico indifferenziato alla definizione della forma, popolato da fate, atleti, maghi, creature mitologiche e personaggi storici (come il mago Harry Houdini).
* **Materiali sintetici e industriali unici**: per le sue sculture e scenografie Barney rifiuta il marmo o il bronzo tradizionale e utilizza sostanze chimiche innovative: **vaselina solida, cera d'api, teflon, gomma siliconica e termoplastica**. Questi materiali possono sciogliersi con il calore o indurirsi con il freddo, incarnando concretamente l'idea della materia vivente in perenne trasformazione.

![Matthew Barney, Cremaster 3 al Guggenheim Museum di New York, 2002](assets/corsi/dapl08/anno-2/storia-arte-2/images/barney_cremaster3.jpg)

---

### 3. Cremaster 3 e la mostra al Guggenheim di New York (2002-2003)

* **Il vertice del ciclo (*Cremaster 3*, 2002)**: ambientato all'interno del celebre grattacielo Chrysler Building di New York e lungo la rampa a spirale del Museo Guggenheim. Barney impersona l'Apprendista massone che scala la spirale del museo affrontando cinque prove simboliche (inclusa la sfida con la modella e atleta paralimpica Aimee Mullins con protesi di cristallo trasparente).
* **L'opera d'arte totale**: Barney unisce cinema d'avanguardia, grande scultura in teflon, costumi di scena e fotografia, creando la più grandiosa e complessa epopea visiva della fine del Novecento.`;

allData[26].keyPoints = [
  "Matthew Barney concepisce l'arte come sforzo fisico e trasformazione della materia, unendo sport, medicina e scultura.",
  "Il 'Cremaster Cycle' (1994-2002) è un ciclo di cinque grandi film che esplora la differenziazione biologica e la metamorfosi.",
  "Usa materiali sintetici capaci di mutare stato con la temperatura: vaselina solida, teflon, silicone e plastica.",
  "In 'Cremaster 3' trasforma il Museo Guggenheim di New York in un monumentale teatro di sfide simboliche e riti iniziatici."
];

// Capitolo 28: Jake & Dinos Chapman e Charles Ray (indice 27)
allData[27].subtitle = "Manichini mutanti, rilettura dissacrante di Goya, manichini di famiglia omologati e il perturbante";
allData[27].summary = `### 1. La scultura tra grottesco e inquietudine

Negli anni Novanta la figura umana nella scultura viene messa radicalmente in discussione: i fratelli britannici **Jake e Dinos Chapman** creano visioni provocatorie e grottesche per denunciare l'orrore della storia, mentre l'americano **Charles Ray** altera impercettibilmente la realtà quotidiana per creare un senso di profonda inquietudine.

---

### 2. Jake & Dinos Chapman: I manichini mutanti e l'inferno della storia

Protagonisti di punta della corrente dei *Young British Artists* (YBA) a Londra, i fratelli **Jake** (1966) e **Dinos** (1962) **Chapman** utilizzano la provocazione estrema e lo humour nero:
* **I manichini infantili mutanti (*Tragic Anatomies*, 1996)**: fondono insieme manichini di bambini con scarpe da ginnastica, i cui organi sessuali (genitali maschili e femminili) sono impiantati mostruosamente al posto di nasi, bocche o orecchie. L'opera suscita scandalo, ma intende denunciare l'iper-sessualizzazione dei minori e la violenza della società dei consumi.
* **La riscrittura delle incisioni di Francisco Goya**: acquistano una serie originale di preziose stampe storiche dei *Disastri della guerra* di Goya e vi dipingono sopra a mano volti grotteschi di pagliacci e mostri (*Insult to Injury*, 2003). Non per distruggere il maestro spagnolo, ma per dimostrare che la crudeltà umana e le atrocità delle guerre contemporanee hanno superato perfino l'incubo di Goya.
* **Hell (Inferno, 1999-2000)**: una serie di grandi teche di vetro disposte a forma di croce uncinata, contenenti oltre trentamila soldatini e figure in miniatura modellati e dipinti a mano, impegnati in un massacro apocalittico tra soldati nazisti ed esseri mostruosi. L'opera ricorda che l'Olocausto non è una fiaba lontana, ma una tragica realtà della storia moderna.

![Charles Ray, Family Romance, 1993 - Manichini in fibra di vetro a grandezza uniforme, MoMA New York](assets/corsi/dapl08/anno-2/storia-arte-2/images/charles_ray_family.jpg)

---

### 3. Charles Ray: La normalità che diventa sconcertante

Nato a Chicago nel 1953, **Charles Ray** lavora su impercettibili variazioni della realtà che creano un forte effetto di spaesamento:
* **Family Romance (1993)**: la sua scultura più celebre mostra quattro manichini nudi che si tengono per mano: un padre, una madre, un figlio maschio e una figlia femmina. L'elemento sconcertante è che **tutti e quattro i personaggi hanno la stessa identica altezza di 135 centimetri**: i genitori sono rimpiccioliti e i bambini sono ingranditi. Questa perfetta uniformità toglie ogni naturalezza alla famiglia, facendola apparire come una strana mutazione biologica prefabbricata.
* **Manichini da vetrina modificati**: Ray modella figure umane vestite da impiegati o manichini maschili con i genitali cancellati, dimostrando come basti una minima alterazione della proporzione per rendere inquietante l'oggetto più comune.`;

allData[27].keyPoints = [
  "I fratelli Chapman usano provocazione e umorismo nero per mostrare gli orrori della violenza storica e dell'omologazione.",
  "Con i loro manichini mutanti e l'intervento sulle stampe di Goya denunciano la brutalità e la disumanizzazione del nostro tempo.",
  "Charles Ray lavora sulle alterazioni minime della realtà quotidiana per generare una profonda sensazione di inquietudine.",
  "In 'Family Romance' (1993) padre, madre e figli hanno tutti la medesima statura (135 cm), svelando una conformità artificiale e mostruosa."
];

// Capitolo 29: L'Arte Relazionale di Nicolas Bourriaud (1998) (indice 28)
allData[28].subtitle = "Nicolas Bourriaud, l'opera come momento di incontro, la convivialità e la partecipazione del pubblico";
allData[28].summary = `### 1. La svolta teorica: Il saggio Esthétique relationnelle (1998)

Nel 1998 il critico d'arte e curatore francese **Nicolas Bourriaud** pubblica a Parigi un saggio destinato a diventare il punto di riferimento teorico di tutti gli anni Novanta: **Estetica Relazionale** (*Esthétique relationnelle*).

La tesi di fondo trasforma radicalmente il modo di intendere l'arte:
* **Dall'oggetto alla relazione umana**: per secoli l'arte occidentale ha prodotto oggetti materiali finiti (quadri da appendere, sculture da ammirare). Negli anni Novanta gli artisti non sono più interessati a fabbricare semplici merci per collezionisti, ma mirano a creare **occasioni concrete di incontro, dialogo e convivenza tra le persone**.
* **L'opera come 'dispositivo di incontro'**: la galleria o il museo non sono più sale silenziose dove contemplare capolavori distanti, ma si trasformano in piazze accoglienti, cucine, bar o salotti dove il pubblico è invitato a sedersi, parlare, mangiare o collaborare.
* **Costruire comunità reali contro l'isolamento digitale**: in un'epoca in cui la televisione e i primi computer cominciano a isolare gli individui davanti agli schermi, l'arte relazionale rivendica il valore del contatto umano in presenza, delle relazioni dal vivo e del tempo condiviso insieme senza fretta.

---

### 2. Le caratteristiche della pratica relazionale

Gli artisti di questo movimento condividono tratti operativi ben precisi:
* **Rifiuto dell'opera d'arte intoccabile**: non c'è più un piedistallo sacro né un cartello «vietato toccare». L'opera esiste e ha senso solo se il visitatore partecipa, la usa o la consuma.
* **La convivialità e l'ospitalità**: cucinare per gli altri, offrire un caffè, prestare oggetti, organizzare giochi di società o feste collettive diventano veri e propri atti scultorei.
* **Il ruolo aperto dello spettatore**: chi visita la mostra non è più un semplice consumatore passivo di immagini, ma diventa parte integrante e attiva dell'opera stessa.

---

### 3. I protagonisti del movimento

Bourriaud individua un gruppo compatto di artisti internazionali:
* **Rirkrit Tiravanija**: che cucina e serve cibo thailandese caldo gratuitamente ai visitatori nelle gallerie;
* **Carsten Höller**: che costruisce scivoli giganti, occhiali che capovolgono la visione e giostre rallentate per far sperimentare dubbi percettivi al pubblico;
* **Liam Gillick**: che progetta architetture modulari e pannelli di plexiglas colorato per favorire la discussione e il lavoro condiviso;
* **Philippe Parreno e Pierre Huyghe**: che esplorano il tempo libero, le fiabe, il cinema e la proprietà collettiva delle immagini.

![Estetica Relazionale - La galleria trasformata in spazio di convivenza e incontro umano](assets/corsi/dapl08/anno-2/storia-arte-2/images/arte_relazionale_generale.jpg)`;

allData[28].keyPoints = [
  "Nicolas Bourriaud teorizza nel 1998 l'Estetica Relazionale: l'arte crea momenti di incontro umano anziché semplici oggetti.",
  "La mostra diventa uno spazio conviviale (cucina, salotto, bar) dove le persone si incontrano e comunicano tra loro.",
  "L'opera d'arte non è più intoccabile, ma vive della partecipazione attiva e della presenza del pubblico.",
  "Tra i principali esponenti figurano Rirkrit Tiravanija, Carsten Höller, Liam Gillick, Philippe Parreno e Pierre Huyghe."
];

// Capitolo 30: Rirkrit Tiravanija e Carsten Höller (indice 29)
allData[29].subtitle = "Cucinare cibo thailandese per il pubblico, gli scivoli giganti e gli esperimenti sul dubbio";
allData[29].summary = `### 1. Rirkrit Tiravanija: L'ospitalità come arte e il profumo del cibo condiviso

Nato a Buenos Aires nel 1961 da diplomatici thailandesi, cresciuto tra Bangkok, l'Etiopia e il Canada e attivo tra New York e Berlino, **Rirkrit Tiravanija** è il simbolo assoluto dell'Estetica Relazionale:
* **Pad Thai (1990) alla Paula Allen Gallery di New York**: la sua prima celebre azione pubblica. Tiravanija svuota completamente la galleria, porta via i quadri e trasforma lo spazio in una cucina improvvisata con fornelli da campeggio, tavoli pieghevoli e scorte di ingredienti freschi. Si mette ai fornelli e **cucina piatti caldi della tradizione thailandese (*Pad Thai*) offrendoli gratuitamente a tutti i visitatori**.
* **Il significato del pasto in comune**: l'opera non è il piatto di cibo in sé, e non ci sono oggetti da comprare. L'opera è **l'esperienza umana di sedersi insieme a sconosciuti, parlare, mangiare e condividere del tempo**. Il museo smette di essere un tempio d'affari elitario e diventa un luogo di autentica generosità.
* **Le repliche e le architetture comunitarie**: negli anni successivi ricostruisce in scala 1:1 il suo intero appartamento all'interno delle gallerie lasciandolo aperto giorno e notte a chiunque voglia dormire, farsi una doccia o ascoltare musica.

![Rirkrit Tiravanija, Pad Thai, 1990 - Cucina thailandese e condivisione conviviale in galleria](assets/corsi/dapl08/anno-2/storia-arte-2/images/tiravanija_pad_thai.jpg)

---

### 2. Carsten Höller: Lo scienziato che fa nascere il dubbio e gli scivoli monumentali

Nato a Bruxelles nel 1961 da genitori tedeschi, **Carsten Höller** compie un percorso scientifico prima di dedicarsi all'arte, conseguendo un dottorato in scienze agrarie ed entomologia (lo studio degli insetti). Questa formazione lo spinge a concepire la mostra come un **laboratorio scientifico di sperimentazione umana**:
* **L'arte che mette in crisi le certezze**: Höller non vuole dare risposte preconfezionate, ma desidera stimolare nel visitatore uno stato di **dubbio benefico e disorientamento**:
  * **Gli Scivoli monumentali (*Test Site*, 2006)**: installa enormi scivoli tubolari d'acciaio nella celebre *Turbine Hall* della Tate Modern di Londra. I visitatori salgono ai piani alti e scivolano a tutta velocità fino al piano terra: la discesa rapida regala un misto di paura incontrollata e gioia infantile, cambiando radicalmente il modo consueto di vivere un museo.
  * **Gli Occhiali rovesciati (*Upside-Down Goggles*)**: occhiali speciali con prismi che capovolgono totalmente la vista del mondo a testa in giù; chi li indossa fatica a camminare e a toccare gli oggetti, scoprendo quanto la nostra percezione dipenda da abitudini mentali.
  * **I Funghi giganti rotanti (*Giant Triple Mushrooms*)**: sculture di funghi enormi (alcuni dei quali allucinogeni come l'Amanita muscaria) che ruotano sospesi, alludendo all'alterazione della coscienza e al mistero della natura.`;

allData[29].keyPoints = [
  "Rirkrit Tiravanija trasforma la galleria d'arte in una cucina comunitaria, cucinando e offrendo piatti thailandesi ai visitatori.",
  "Per Tiravanija l'opera d'arte risiede nell'incontro, nella conversazione e nel tempo trascorso piacevolmente insieme.",
  "Carsten Höller applica il rigore scientifico all'arte per far nascere il dubbio e la sperimentazione sensoriale nel pubblico.",
  "I suoi celebri scivoli giganti alla Tate Modern uniscono divertimento, velocità e spaesamento percettivo."
];

// Capitolo 31: Vanessa Beecroft: Il Tableau Vivant e la Politica dello Sguardo (indice 30)
allData[30].subtitle = "Gruppi di modelle immobili in spazi museali, l'eleganza della moda e la critica dello sguardo maschile";
allData[30].summary = `### 1. Dati biografici e formazione

Nata a Genova nel 1969 da madre italiana e padre britannico, **Vanessa Beecroft** studia all'Accademia di Belle Arti di Brera a Milano, diplomandosi in scenografia. Durante gli anni degli studi affronta da vicino il problema personale dei disturbi alimentari: annota meticolosamente su un quaderno intimo ogni cibo ingerito giorno per giorno, dando vita al *Libro del cibo* (1993), prima testimonianza del suo interesse per il rapporto complesso tra corpo, controllo e apparenza esteriore.

Nel 1993 compie la sua prima performance ufficiale a Milano, facendosi notare subito per l'originalità e la forza visiva delle sue composizioni.

---

### 2. Poetica: La reinvenzione del Quadro Vivente (*Tableau Vivant*)

La Beecroft inventa una formula scenica inconfondibile che unisce la pittura classica al mondo contemporaneo della moda:
* **Il gruppo di donne immobili**: per le sue performance (chiamate con una sigla progressiva: *VB01*, *VB08*, *VB35*, *VB52*) seleziona gruppi di giovani donne (da venti a cinquanta modelle) che restano in piedi immobili e in perfetto silenzio per circa tre ore all'interno di musei storici, gallerie o palazzi prestigiosi.
* **La disciplina del corpo**: le donne indossano scarpe con tacchi a spillo eleganti, parrucche con tagli identici e talvolta lingerie sofisticata, oppure sono completamente nude con il corpo truccato da un velo di cipria uniforme che le fa assomigliare a statue viventi. Hanno l'istruzione severa di non parlare con il pubblico, di non sorridere e di non muoversi se non per piccoli spostamenti lenti dettati dalla stanchezza fisica.
* **La memoria della pittura classica**: le pose e le disposizioni nello spazio si ispirano ai grandi maestri del passato: dalle figure perfette di Piero della Francesca alle vergini rinascimentali, dalle nobildonne del Barocco alle sculture in cera.

![Vanessa Beecroft, Performance VB52, 2003 - Modelle attorno al tavolo di cristallo, Castello di Rivoli](assets/corsi/dapl08/anno-2/storia-arte-2/images/beecroft_vb52.jpg)

---

### 3. La politica dello sguardo e le grandi collaborazioni

* **Ribaltare lo sguardo di chi osserva**: il pubblico entra nella sala e si trova davanti a un gruppo compatto di donne che non si lasciano avvicinare né sedurre. L'opera costringe chi guarda a interrogarsi sui propri desideri, sul senso di imbarazzo e su come la società della moda e della pubblicità utilizzi e oggettifichi il corpo femminile.
* **VB52 al Castello di Rivoli (2003)**: trentadue donne di varia età siedono attorno a un lungo tavolo trasparente di cristallo consumando un pasto rigoroso diviso per colori monocromatici (un giorno cibi solo rossi, un giorno solo arancioni, un giorno solo bianchi), mettendo in scena il rapporto ossessivo con il cibo e la bellezza.
* Negli anni Duemila si trasferisce a New York e a Los Angeles, collaborando con prestigiosi marchi di moda e con l'artista musicale Kanye West per la regia visiva delle sfilate *Yeezy*, portando il suo stile visivo dal museo alla cultura pop planetaria.`;

allData[30].keyPoints = [
  "Vanessa Beecroft rinnova la tradizione storica del 'tableau vivant' (quadro vivente) attraverso gruppi compatti di modelle.",
  "Le sue performer restano in piedi per ore in perfetto silenzio e immobilità, simili a statue classiche contemporanee.",
  "L'opera riflette sulla moda, sui canoni imposti di bellezza, sui disturbi alimentari e sullo sguardo voyeuristico del pubblico.",
  "Ha portato le sue celebri composizioni dai grandi musei (Castello di Rivoli, Guggenheim) alle collaborazioni pop con la moda e la musica."
];

// Capitolo 32: Pipilotti Rist e Andreas Gursky (indice 31)
allData[31].subtitle = "Videoinstallazioni colorate e liberatorie di Pipilotti Rist e fotografie monumentali del capitalismo globale di Gursky";
allData[31].summary = `### 1. La trasformazione dell'immagine negli anni Novanta

Negli anni Novanta la videoproiezione su grandi schermi e la fotografia digitale monumentale cambiano per sempre il volto delle mostre d'arte. Due maestri incarnano questa rivoluzione con esiti opposti ma complementari: la svizzera **Pipilotti Rist**, con video allegri, caldi, immersivi e carichi di sensualità, e il tedesco **Andreas Gursky**, con fotografie colossali, lucide e precisissime che mostrano il funzionamento dell'economia mondiale.

---

### 2. Pipilotti Rist: Colori vivaci, libertà del corpo e ironia

![Pipilotti Rist, Sip My Ocean, 1996 - Videoinstallazione a due canali con audio immersivo](assets/corsi/dapl08/anno-2/storia-arte-2/images/pipilotti_rist_sip_my_ocean.jpg)

![Andreas Gursky, Seilbahn, Dolomiten, 1987 / 99 Cent, 1999 - Fotografia monumentale a colori](assets/corsi/dapl08/anno-2/storia-arte-2/images/gursky_seilbahn.jpg)

Nata nel 1962 in Svizzera (il suo nome d'arte unisce Pippi Calzelunghe e il suo nome di battesimo Elisabeth Charlotte Rist), **Pipilotti Rist** crea ambienti video dove lo spettatore è invitato a rilassarsi e lasciarsi avvolgere:
* **Ambienti accoglienti e cuscini sul pavimento**: Rist toglie le rigide sedie dei musei e riempie le sale di morbidi divani, letti e grandi cuscini colorati su cui il pubblico può sdraiarsi comodamente a guardare le proiezioni sul soffitto e sulle pareti.
* **Ever Is Over All (1997, premiata alla Biennale di Venezia)**:
  * **Cosa accade nel video**: un filmato a rallentatore (*slow motion*) accompagnato da una melodia canticchiata spensierata e allegra. Una giovane donna vestita con un bell'abito azzurro e scarpe rosse con tacco cammina sorridente sul marciapiede, tenendo in mano un lungo fiore di metallo esotico. Con grazia ritmata, **colpisce con forza e manda in frantumi i finestrini delle automobili parcheggiate lungo la strada**. Una donna poliziotto che passa di lì in divisa le sorride con approvazione e la saluta con complicità.
  * **Significato dell'opera**: l'azione trasforma un gesto di distruzione in una danza di liberazione: l'automobile (simbolo del potere tecnologico, aggressivo e maschile) viene infranta dalla grazia della natura e della libertà femminile. Il video celebra la gioia e la solidarietà tra donne, diventando celeberrimo anche nella musica pop contemporanea.

---

### 3. Andreas Gursky: La fotografia monumentale e la mappa del capitale globale

Allievo dei coniugi Becher all'Accademia di Düsseldorf, **Andreas Gursky** (nato a Lipsia nel 1955) compie un salto di qualità storico: usa per primo il ritocco digitale al computer per creare fotografie immense, grandi come i quadri storici dei musei:

* **Lo sguardo dall'alto a fuoco totale**: Gursky fotografa da un punto di vista molto elevato e lontano. Nelle sue immagini **ogni dettaglio è perfettamente a fuoco**, dal primo piano fino all'orizzonte lontano. Chi guarda si sente come un osservatore neutrale che guarda la Terra dallo spazio.
* **I luoghi simbolo dell'economia moderna**:
  * *I mercati finanziari e le Borse valori* (Tokyo, Hong Kong, Chicago): oceani di broker in camicia che urlano e corrono immersi in una ragnatela infinita di monitor e grafici finanziari.
  * *La grande distribuzione e i consumi di massa*: i magazzini sterminati di Amazon, le fabbriche della Siemens, e gli enormi supermercati con corridoi chilometrici di scaffali pieni di prodotti tutti uguali a 99 centesimi (*99 Cent II Diptychon*, 1999).
* **L'individuo nella società globale**: nella visione di Gursky la singola persona umana appare come una minuscola formica anonima, un piccolo tassello ingranato nel gigantesco meccanismo della finanza e del commercio planetario.`;

allData[31].keyPoints = [
  "Negli anni Novanta la videoproiezione digitale trasforma i musei in spazi accoglienti, sensoriali e immersivi.",
  "Pipilotti Rist unisce colori psichedelici, musica e liberazione del corpo femminile ('Ever Is Over All', 1997).",
  "Andreas Gursky realizza fotografie monumentali al computer che ritraggono i centri del capitalismo globale (Borse, Amazon, 99 Cent).",
  "La prospettiva iper-dettagliata e dall'alto di Gursky mostra l'individuo come un piccolo elemento anonimo del mercato globale."
];

// Capitolo 33: Takashi Murakami e il Superflat (indice 32)
allData[32].subtitle = "Mr. DOB, i fiori sorridenti, la fabbrica d'arte Kaikai Kiki e l'unione tra pittura classica e manga";
allData[32].summary = `### 1. Dati biografici e formazione: Dalla pittura classica agli anime

Nato a Tokyo nel 1962, **Takashi Murakami** cresce appassionandosi fin da bambino ai cartoni animati giapponesi (*anime*), ai fumetti (*manga*) e al mondo dei videogiochi, tipici della cultura dei giovani appassionati noti come **Otaku**. Accanto a questo amore per la cultura pop, compie studi accademici severi: ottiene un dottorato di ricerca alla prestigiosa Università delle Belle Arti di Tokyo specializzandosi in **Nihonga**, la raffinatissima pittura classica tradizionale giapponese.

Questa doppia anima (la maestria millenaria dell'arte tradizionale unita all'esplosione commerciale dell'animazione moderna) è il segreto della sua rivoluzione artistica mondiale.

---

### 2. La teorizzazione del Superflat (Super-Piatto, 2000)

![Takashi Murakami, Superflat Rainbow Flowers & Mr. DOB - Sintesi Pop, estetica Otaku e fabbrica Kaikai Kiki](assets/corsi/dapl08/anno-2/storia-arte-2/images/murakami_superflat.jpg)

All'inizio degli anni Novanta Murakami elabora una visione teorica che battezza con il nome di **Superflat** (Super-Piatto):
* **La superficie piatta e senza prospettiva**: l'antica tradizione artistica giapponese (dalle xilografie di Hokusai fino ai manga) non ha mai usato la prospettiva geometrica occidentale con punto di fuga; ha sempre preferito **colori stesi in modo piatto, linee di contorno pulite e assenza di profondità illusoria**.
* **L'azzeramento delle distanze culturali**: *Superflat* significa anche che in Giappone non c'è più differenza tra «cultura alta» (i musei, i quadri per le élite) e «cultura bassa» (i giocattoli, i fumetti, i cartoni animati e gli spot commerciali). Tutto vive sullo stesso piano, accessibile e consumabile da tutti.
* **La memoria della bomba atomica**: Murakami spiega che la predilezione giapponese per i personaggi carini e infantili (*kawaii*) e per le catastrofi fantastiche (come mostri giganti e funghi nucleari colorati) è il modo in cui l'inconscio del popolo giapponese ha cercato di superare il trauma della Seconda Guerra Mondiale e delle bombe atomiche di Hiroshima e Nagasaki.

---

### 3. I personaggi celebri e la fabbrica Kaikai Kiki

* **Mr. DOB (1993)**: il celebre personaggio-simbolo dell'artista, con orecchie tonde che formano le lettere 'D' e 'B' e la testa che forma la 'O'. Ispirato a Topolino, a Doraemon e a Sonic, Mr. DOB cambia continuamente umore: a volte è un tenero cucciolo indifeso, altre volte si trasforma in un mostriciattolo con occhi allucinati e denti affilati.
* **I Fiori Sorridenti (*Smiling Flowers*)**: stese immense di margherite coloratissime con faccine sorridenti. Sotto l'apparenza di un'allegria contagiosa per bambini, i fiori nascondono un sorriso quasi forzato, che ricorda l'ottimismo imposto dalla società moderna.
* **La corporation Kaikai Kiki**: fondata sul modello delle botteghe rinascimentali e della Factory di Andy Warhol, è una grande azienda con centinaia di giovani assistenti tra Tokyo e New York che produce sculture perfette in fibra di vetro, grandi dipinti, film d'animazione, abbigliamento e gadget.
* **La collaborazione con Louis Vuitton (2003)**: su invito dello stilista Marc Jacobs, Murakami ridisegna il celebre logo di Louis Vuitton colorandolo con 33 tinte vivaci e stampandolo sulle borse di lusso, portando l'arte contemporanea all'interno della moda mondiale.`;

allData[32].keyPoints = [
  "Takashi Murakami unisce la pittura classica giapponese (Nihonga) alla cultura pop contemporanea di manga e anime (Otaku).",
  "Teorizza il concetto di 'Superflat': superficie visiva piatta e azzeramento della separazione tra arte colta e cultura di consumo.",
  "I suoi personaggi più famosi sono l'alter-ego 'Mr. DOB' e i celebri 'Fiori Sorridenti' multicolori.",
  "Con la sua azienda Kaikai Kiki e le collaborazioni con la moda (Louis Vuitton) unisce arte museale, design e mercato globale."
];

// Salva i dati aggiornati
const output = 'window.ARTE_DATA = ' + JSON.stringify(allData, null, 2) + ';\n';
fs.writeFileSync(dataFilePath, output, 'utf8');
console.log('Module 2 (Capitoli 20-33) aggiornato e semplificato con successo!');
