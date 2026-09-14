const fs = require('fs');
const path = require('path');

const dataFilePath = path.join(__dirname, '..', 'data', 'arte-data.js');
let fileContent = fs.readFileSync(dataFilePath, 'utf8');

const sandbox = { window: {} };
eval(fileContent.replace('window.ARTE_DATA', 'sandbox.window.ARTE_DATA'));
const allData = sandbox.window.ARTE_DATA;

// Capitolo 41: Maurizio Cattelan (indice 40)
allData[40].subtitle = "L'ironia sul fallimento, La Nona Ora, Him, il dito medio a Piazza Affari e la banana con lo scotch";
allData[40].summary = `### 1. Dati biografici e formazione: L'outsider senza accademia

Nato a Padova nel 1960 da una famiglia di umili origini (madre donna delle pulizie e padre camionista), **Maurizio Cattelan** è una delle figure più celebri e discusse dell'arte contemporanea mondiale. A differenza di quasi tutti i suoi colleghi, non frequenta alcuna accademia d'arte né scuole di disegno: svolge disparati mestieri pratici (giardiniere, aiuto cuoco, operaio, impiegato all'obitorio) prima di avvicinarsi all'arte negli anni Ottanta a Forlì e a Milano realizzando mobili e oggetti d'arredo insoliti.

Questa posizione di 'intruso' nel sistema dell'arte diventa il suo punto di forza: Cattelan osserva i riti del collezionismo e delle gallerie con disincanto, ironia popolare e sagacia, trasformando la furbizia e la paura del fallimento nella sua firma più riconoscibile.

---

### 2. Poetica: Il fallimento come strategia e la fuga dal potere

La ricerca di Cattelan è un continuo **smascheramento delle contraddizioni e delle ipocrisie del nostro tempo**:
* **L'elusione del dovere artistico**: agli inizi della carriera, di fronte all'ansia di dover produrre una mostra, Cattelan chiude a chiave la galleria lasciando sulla porta il cartello *«Torno subito»* (1989), oppure scappa dalla finestra della galleria con una fune di lenzuola annodate (*Una domenica a Rivara*).
* **L'iperrealismo sconcertante e la tassidermia**: Cattelan non modella le sue sculture con le proprie mani, ma si affida a maestri artigiani della cera e della tassidermia (la conservazione di animali imbalsamati). Asini, cani, cavalli e piccioni diventano figure tragiche e al contempo comiche:
  * In *Novecento* (1997), un cavallo da corsa vero imbalsamato pende sospeso dal soffitto con cinghie di cuoio, con la testa e le zampe allungate verso il basso per gravità: un'immagine toccante della fatica e dell'impotenza umana di fronte al destino storico.

![Maurizio Cattelan, La Nona Ora, 1999 - Cera, abiti pontifici e frammento di meteorite](assets/corsi/dapl08/anno-2/storia-arte-2/images/cattelan_nona_ora.jpg)

---

### 3. I grandi scandali visivi internazionali

#### La Nona Ora (1999)
* Una scultura iperrealistica a grandezza naturale che raffigura **Papa Giovanni Paolo II vestito con i paramenti bianchi, abbattuto a terra e schiacciato da un pesante meteorite nero** caduto dal cielo attraverso una vetrata rotta del soffitto, su un sontuoso tappeto rosso. L'opera fece enorme scalpore: non era un attacco empio alla Chiesa, ma una meditazione sulla sofferenza dell'anziano pontefice e sulla fragilità di qualsiasi potere umano di fronte agli eventi imperscrutabili del cosmo.

#### Him (Lui, 2001)
* Vista da dietro all'interno di una stanza vuota, la scultura sembra un bambino in ginocchio con un completo di lana grigio che prega a mani giunte. Girandogli attorno per guardarlo in viso, lo spettatore scopre con brivido il volto inconfondibile di **Adolf Hitler con i baffetti**, ritratto con occhi tristi che chiedono pietà. L'opera riflette sulla presenza del male, ricordando che anche il peggior mostro della storia era un essere umano nato come un bambino innocente.

#### L.O.V.E. (Il dito medio a Piazza Affari, Milano, 2010)
* Monumentale scultura alta undici metri in prezioso marmo bianco di Carrara, collocata permanentemente al centro di Piazza degli Affari a Milano, davanti a Palazzo Mezzanotte (sede della Borsa Italiana). L'opera raffigura un saluto fascista in cui **tutte le dita della mano sono state mozzate, lasciando eretto solo il dito medio**. Un gesto beffardo e liberatorio rivolto al tempio dell'alta finanza speculativa.

#### Comedian (La banana con il nastro adesivo, 2019)
* Presentata alla fiera Art Basel Miami Beach: una vera banana fresca comprata al supermercato per pochi centesimi, attaccata al muro bianco dello stand con una striscia di nastro adesivo grigio da cantiere. Venduta a collezionisti per 120.000 dollari, l'opera è diventata un fenomeno mondiale di internet, dimostrando come nel mercato dell'arte contemporanea il valore economico non dipenda dalla materia preziosa, ma dal meccanismo della firma e della fiducia collettiva.`;

allData[40].keyPoints = [
  "Maurizio Cattelan diventa un maestro dell'arte contemporanea mondiale senza aver frequentato accademie d'arte.",
  "Usa animali imbalsamati e figure in cera iperrealistiche per toccare con ironia tagliente i tabù della morte e del potere.",
  "Opere celeberrime come 'La Nona Ora' (il Papa schiacciato dal meteorite) e 'Him' (Hitler bambino che prega) interrogano il sacro e il male.",
  "Con 'L.O.V.E.' a Milano e 'Comedian' (la banana attaccata al muro con lo scotch) unisce satira politica e provocazione sul mercato dell'arte."
];

// Capitolo 42: Damien Hirst & Young British Art (indice 41)
allData[41].subtitle = "Lo squalo sotto formaldeide, la mostra Freeze, gli armadietti di medicine e il teschio di diamanti";
allData[41].summary = `### 1. La mostra Freeze (1988) e l'esplosione dei Young British Artists

Nato a Bristol nel 1965 e cresciuto a Leeds, **Damien Hirst** studia al Goldsmiths College di Londra. Nel 1988, ancora studente, compie una mossa organizzativa che cambia la storia dell'arte britannica: organizza la storica mostra autogestita **Freeze** all'interno di un magazzino portuale abbandonato nei docks di Londra, esponendo le opere dei suoi compagni di corso (i futuri *Young British Artists* o YBA, tra cui Sarah Lucas, Gary Hume e Michael Landy).

La mostra viene visitata dal grande magnate della pubblicità e collezionista **Charles Saatchi**, che decide di comprare in blocco molte opere e di finanziare le idee più audaci e costose di Hirst.

---

### 2. Poetica: La morte inevitabile, la scienza e l'illusione dei farmaci

La ricerca di Hirst gira attorno a un tema universale e antico: il **memento mori** (il ricordo della morte e la caducità dell'esistenza), affrontato però attraverso il linguaggio asettico della medicina e dell'industria moderna:
* **La serie Natural History e gli animali in formaldeide**: Hirst prende carcasse di animali veri (mucche, pecore, squali, maiali sezionati a metà) e le immerge per sempre dentro grandi teche di vetro e acciaio riempite di una soluzione azzurrina di formaldeide (liquido conservante usato nei laboratori scientifici).
  * Il capolavoro è **The Physical Impossibility of Death in the Mind of Someone Living** (L'impossibilità fisica della morte nella mente di un vivo, 1991): un gigantesco squalo tigre lungo oltre quattro metri, con la bocca spalancata e i denti aguzzi, sospeso nel liquido limpido. L'animale sembra nuotare vivo verso lo spettatore, suscitando al contempo terrore ancestrale e fredda curiosità scientifica.
* **Le farmacie e gli armadietti per medicinali (*Medicine Cabinets*, *Pharmacy*)**: armadietti asettici in acciaio inossidabile che contengono migliaia di confezioni di pillole, sciroppi e farmaci veri disposti con ordine geometrico. Hirst mette a nudo come la società contemporanea abbia sostituito la fede religiosa con la cieca fiducia nella medicina e nei prodotti farmaceutici per scacciare la paura della vecchiaia e della morte.

![Damien Hirst, For the Love of God, 2007 - Calco in platino di teschio umano con 8.601 diamanti](assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_skull.jpg)

---

### 3. Dal teschio di diamanti all'asta record da Sotheby's

* **For the Love of God (Per l'amor di Dio, 2007)**: un calco in platino purissimo ricavato da un vero teschio umano del Settecento, incastonato con **8.601 diamanti naturali purissimi** per un totale di oltre 1.100 carati, con al centro della fronte un enorme diamante rosa a goccia da 52 carati, e con i denti umani originali puliti e conservati. Con un costo di produzione record di 15 milioni di sterline, l'opera è un abbagliante monumento alla vanità umana: la morte viene ricoperta dallo sfarzo del lusso estremo.
* **L'asta Beautiful Inside My Head Forever (Sotheby's Londra, 15-16 settembre 2008)**: compiendo un gesto senza precedenti nella storia dell'arte, Hirst salta del tutto le gallerie d'arte private e vende 223 sue opere nuove direttamente all'asta pubblica da Sotheby's. L'evento incassa la cifra record di 111 milioni di sterline proprio nelle stesse ore in cui a Wall Street falliva la banca d'affari Lehman Brothers: consacrando Hirst come l'imprenditore artistico più potente del millennio.`;

allData[41].keyPoints = [
  "Damien Hirst lancia il movimento dei Young British Artists (YBA) a Londra con la celebre mostra autogestita 'Freeze' (1988).",
  "La sua opera affronta il tema universale della morte attraverso teche asettiche e animali conservati in formaldeide (lo squalo tigre).",
  "Nelle serie delle 'Farmacie' svela l'illusione della società moderna di sconfiggere la morte attraverso il consumo di medicinali.",
  "Con 'For the Love of God' (il teschio ricoperto di 8.601 diamanti) e l'asta record da Sotheby's nel 2008 unisce arte, sfarzo e finanza."
];

// Capitolo 43: Banksy (indice 42)
allData[42].subtitle = "La street art con gli stencil, l'anonimato a Bristol, Betlemme e il quadro triturato all'asta";
allData[42].summary = `### 1. Le origini a Bristol e l'invenzione dello Stencil rapido

Nato a Bristol (Gran Bretagna) presumibilmente attorno al 1974, la vera identità anagrafica di **Banksy** rimane tuttora rigorosamente segreta. Inizia a dipingere graffiti a mano libera nei primi anni Novanta nella vivace scena musicale e underground di Bristol (la città dei Massive Attack e della musica trip-hop).

Presto si accorge che dipingere a mano libera con la bomboletta richiede troppo tempo sui muri, esponendolo al rischio continuo di essere sorpreso e arrestato dalla polizia:
* **La svolta della tecnica dello Stencil**: Banksy comincia a preparare a casa le maschere sagomate su cartone (*stencil*). Arrivato di notte davanti al muro prescelto, gli basta appoggiare la maschera e spruzzare la vernice spray per pochi secondi, ottenendo un disegno perfetto, nitido e immediato in pochissimo tempo prima di dileguarsi nel buio.
* **L'anonimato come strategia di libertà**: non svelare la propria faccia non è solo una protezione legale dai processi penali per danneggiamento, ma una potentissima scelta concettuale: senza un volto da celebrità, al centro dell'attenzione rimangono unicamente **il messaggio politico, l'ironia e l'opera pubblica**.

---

### 2. Poetica: La satira del potere, la pace e la difesa dei più deboli

Le immagini di Banksy sono chiare, dirette e comprensibili a chiunque passi per strada:
* **I Topi (*Rats*)**: uno dei suoi soggetti più amati e frequenti. I topi simboleggiano le persone comuni, gli emarginati e i reietti della società: animali che vivono nelle fogne, perseguitati e disprezzati, ma capaci di moltiplicarsi in silenzio e far saltare le città con la loro intelligenza collettiva.
* **Il ribaltamento dei simboli del potere**: due poliziotti maschi britannici in divisa che si baciano teneramente sulla bocca (*Kissing Coppers*), guardie della regina che fanno la pipì contro un muro, scimmie con cartelli appesi al collo che recitano *«Ridete adesso, ma un giorno saremo noi a comandare»*.

![Banksy, Love is in the Bin (Girl with Balloon triturata all'asta da Sotheby's Londra, 2018)](assets/corsi/dapl08/anno-2/storia-arte-2/images/banksy_love_bin.jpg)

---

### 3. I grandi progetti e le azioni storiche

#### Betlemme e il Muro di separazione in Cisgiordania (2005 e 2017)
* Banksy si reca più volte in Palestina e dipinge direttamente sulla colossale barriera di cemento armato costruita da Israele: realizza immagini di bambini che volano via aggrappati a mazzi di palloncini, o una finestra aperta che svela una spiaggia tropicale soleggiata al di là del muro grigio.
* Nel 2017 apre a Betlemme il **Walled Off Hotel**, un vero albergo funzionante a pochi metri dal muro, ironicamente pubblicizzato come «l'hotel con la peggior vista al mondo», per attirare l'attenzione dei viaggiatori internazionali sull'ingiustizia dell'occupazione militare.

#### Love is in the Bin (L'autodistruzione da Sotheby's, 2018)
* Il 5 ottobre 2018, all'asta di Sotheby's a Londra, la celebre tela *Girl with Balloon* (La bambina con il palloncino) viene battuta all'asta per oltre 1 milione di sterline. Nel preciso istante in cui il battitore batte il martello, scatta un meccanismo nascosto: **un trituratore di carta installato segretamente da Banksy dentro la pesante cornice dorata comincia a sminuzzare la tela a strisce verticali**.
* L'opera si blocca a metà lasciando il palloncino intatto e la parte inferiore tagliata a fettine: ribattezzata *Love is in the Bin*, è diventata una delle più geniali denunce storiche contro la speculazione finanziaria nel mercato dell'arte contemporanea.`;

allData[42].keyPoints = [
  "Banksy conserva l'anonimato totale, trasformando la street art e la tecnica dello stencil in una potente arma di comunicazione virale.",
  "I suoi soggetti ricorrenti (i topi, i poliziotti, i bambini) usano un'ironia immediata per difendere i diritti umani contro le guerre e il potere.",
  "Ha dipinto sul Muro di separazione in Cisgiordania e aperto il 'Walled Off Hotel' a Betlemme per denunciare l'oppressione in Palestina.",
  "Nel 2018 compie l'azione clamorosa da Sotheby's triturando la tela 'Girl with Balloon' all'istante dopo essere stata battuta all'asta."
];

// Capitolo 44: Ai Weiwei (indice 43)
allData[43].subtitle = "La ceramica millenaria cinese, i 100 milioni di semi di girasole, la denuncia del terremoto e la prigionia";
allData[43].summary = `### 1. Dati biografici: La memoria dell'esilio e la vita a New York

Nato a Pechino nel 1957, **Ai Weiwei** è figlio di Ai Qing, uno dei più illustri poeti cinesi del Novecento, perseguitato e mandato ai lavori forzati nei campi di rieducazione durante la Rivoluzione Culturale di Mao Zedong. Cresciuto con il padre in esilio ai confini del deserto del Gobi pulendo latrine pubbliche, Ai Weiwei impara fin da bambino il prezzo del coraggio e della libertà di pensiero.

Tra il 1981 e il 1993 vive a New York, nell'East Village, scoprendo il *ready-made* di Marcel Duchamp, la Pop Art di Andy Warhol e la fotografia di strada. Rientrato a Pechino nel 1993 per assistere il padre malato, diventa il punto di riferimento assoluto per i giovani artisti d'avanguardia cinesi.

---

### 2. Poetica: La maestria artigianale cinese e la sfida al potere autoritario

Ai Weiwei unisce la millenaria sapienza manuale della tradizione cinese alla contestazione politica più coraggiosa:
* **La distruzione del reperto antico (*Dropping a Han Dynasty Urn*, 1995)**: una celeberrima sequenza di tre fotografie in bianco e nero in cui l'artista lascia cadere deliberatamente dalle mani un prezioso vaso cerimoniale di terracotta della dinastia Han (vecchio di duemila anni), facendolo andare in mille pezzi sul pavimento. Un'azione provocatoria che riflette su come il governo comunista cinese abbia distrutto la propria memoria storica e sul vero significato del valore culturale.
* **Il recupero dell'artigianato storico**: usa legni pregiati recuperati da templi antichi distrutti, mobili di epoca Qing e la maestria dei vasai storici di Jingdezhen per creare sculture perfette che sfidano le contraddizioni della Cina moderna.

![Ai Weiwei, Sunflower Seeds, 2010 - 100 milioni di semi di girasole in porcellana dipinti a mano, Tate Modern](assets/corsi/dapl08/anno-2/storia-arte-2/images/ai_weiwei_seeds.jpg)

---

### 3. I grandi progetti civili e la persecuzione di Stato

#### Sunflower Seeds (Semi di girasole, 2010, Tate Modern)
* Ai Weiwei riempie l'immensa *Turbine Hall* della Tate Modern con **100 milioni di semi di girasole in porcellana a grandezza naturale, modellati e dipinti a mano uno ad uno da oltre milleseicento artigiani** della città storica della ceramica di Jingdezhen.
* I semi formano un immenso mare grigio calpestabile: il seme di girasole era il cibo umile condiviso dalla popolazione durante le carestie della Rivoluzione Culturale (quando la propaganda descriveva Mao come il Sole e il popolo come i girasoli che si volgevano verso di lui). L'opera celebra la dignità del lavoro artigianale contro la produzione industriale di massa e simboleggia la moltitudine delle voci del popolo cinese.

#### L'inchiesta cittadina sul terremoto del Sichuan (2008) e l'installazione Remembering
* Nel maggio 2008 un violento terremoto devasta la regione del Sichuan, provocando il crollo di decine di scuole mal costruite e la morte di migliaia di bambini. Di fronte al silenzio e alla censura del governo cinese, Ai Weiwei organizza un'inchiesta cittadina indipendente su internet per scoprire e pubblicare i nomi e le date di nascita di tutti i 5.385 bambini deceduti.
* Sulla facciata della Haus der Kunst di Monaco di Baviera realizza **Remembering** (2009): un'immensa scritta murale composta da **9.000 zainetti scolastici colorati**, che compone una frase straziante pronunciata dalla madre di una delle piccole vittime: *«Ha vissuto felicemente su questa terra per sette anni»*.

#### L'arresto segreto (2011)
* A causa del suo impegno civile senza compromessi, il 3 aprile 2011 viene arrestato all'aeroporto di Pechino e tenuto prigioniero in una località segreta per **81 giorni senza accuse formali**, sorvegliato a vista 24 ore su 24 da due guardie militari anche mentre dormiva o si lavava. Liberato solo grazie alla mobilitazione internazionale dei musei di tutto il mondo, oggi vive e lavora in Europa continuando la sua instancabile battaglia per i diritti civili e per i rifugiati politici.`;

allData[43].keyPoints = [
  "Ai Weiwei è il più celebre artista e dissidente cinese contemporaneo, impegnato nella difesa dei diritti umani e della libertà di parola.",
  "Unisce l'eredità dell'artigianato classico cinese (porcellana, legni antichi) alle tecniche concettuali occidentali.",
  "In 'Sunflower Seeds' (Tate Modern 2010) raccoglie 100 milioni di semi di porcellana dipinti a mano da artigiani tradizionali.",
  "Con 'Remembering' ha denunciato la corruzione statale nel crollo delle scuole del Sichuan usando 9.000 zainetti scolastici colorati."
];

// Capitolo 45: Olafur Eliasson (indice 44)
allData[44].subtitle = "La fenomenologia della percezione, il sole artificiale alla Tate Modern, i ghiacci che si sciolgono e la luce";
allData[44].summary = `### 1. Dati biografici e lo Studio a Berlino: L'arte come laboratorio scientifico

Nato a Copenaghen nel 1967 da genitori islandesi (padre cuoco e pittore paesaggista), **Olafur Eliasson** trascorre l'infanzia e le vacanze giovanili esplorando i paesaggi incontaminati dell'Islanda: ghiacciai immensi, vulcani attivi, cascate impetuose e aurore boreali. Studia all'Accademia Reale di Belle Arti di Copenaghen prima di stabilirsi a Berlino.

Nel 1995 fonda lo **Studio Olafur Eliasson**: non un semplice studio di pittore solitario, ma un grande laboratorio interdisciplinare che riunisce oltre novanta professionisti tra architetti, ingegneri, fabbri, matematici, storici dell'arte e cuochi, dove arte e ricerca scientifica collaborano quotidianamente.

---

### 2. Poetica: La percezione dei sensi e la cura per il pianeta

La ricerca di Eliasson pone al centro l'esperienza diretta e viva di chi guarda:
* **La percezione soggettiva: «Your engagement produces the artwork»**: per Eliasson l'opera d'arte non esiste come oggetto isolato, ma si accende solo nel momento esatto in cui i sensi e il corpo del visitatore la attraversano e la sperimentano. Ognuno vive la luce e lo spazio in modo unico e personale.
* **I fenomeni naturali ricreati nello spazio umano**: porta all'interno dei musei gli elementi primari della terra: nebbia fitta, vapore acqueo, arcobaleni, cascate artificiali, muschio e frammenti di ghiaccio millenario.
* **L'impegno ecologico e climatico**: l'artista usa la bellezza dei fenomeni naturali non per stupire con semplici effetti speciali, ma per risvegliare nel pubblico la consapevolezza della fragilità del nostro pianeta di fronte al riscaldamento globale.

![Olafur Eliasson, The Weather Project, 2003 - Sole artificiale e specchio gigante nella Turbine Hall, Tate Modern](assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_weather_project.jpg)

---

### 3. Analisi delle opere cardine

#### The Weather Project (2003, Tate Modern, Londra)
* L'installazione che ha segnato un'epoca: Eliasson trasforma la gigantesca *Turbine Hall* della Tate Modern in una cattedrale laica della natura.
* **Come era realizzata l'opera**:
  * Sul fondo della sala installa un **colossale sole semicircolare artificiale**, composto da centinaia di speciali lampade al sodio a luce gialla monocromatica;
  * L'intero soffitto della sala (a decine di metri d'altezza) viene rivestito da una **superficie continua a specchio** che riflette il semicerchio facendolo apparire come un sole sferico perfetto e duplicando l'intero spazio;
  * Macchine speciali diffondono continuamente nell'aria una **nebbia sottile di zucchero e acqua**, che diffonde la luce dorata in tutto l'ambiente.
* **La reazione del pubblico**: oltre due milioni di visitatori si sdraiarono sul pavimento della sala a contemplare la luce e a guardare il proprio riflesso sul soffitto a specchio, creando una straordinaria comunità di persone rilassate e in dialogo tra loro.

#### Beauty (1993)
* In una stanza completamente buia, una sottile cortina d'acqua scende a pioggia dal soffitto come una cascata nebulizzata, illuminata da un singolo fascio di luce bianca. Lo spettatore che si muove nella stanza vede apparire un **meraviglioso arcobaleno luminoso**: poiché l'arcobaleno dipende dall'angolo visivo tra la luce, le gocce d'acqua e gli occhi di chi guarda, l'arcobaleno visto da ciascuna persona è assolutamente unico e irripetibile.

#### Ice Watch (2014, Parigi e Londra)
* In occasione della Conferenza sul Clima COP21 a Parigi e successivamente davanti alla Tate Modern di Londra, Eliasson trasporta **enormi blocchi di ghiaccio millenario staccatisi dai fiordi della Groenlandia**, disponendoli in cerchio sulla piazza come le ore di un orologio. I passanti potevano toccare con le proprie mani la superficie gelata, ascoltare i crepitii delle bolle d'aria preistoriche imprigionate nel ghiaccio e vedere l'acqua sciogliersi lentamente sull'asfalto, sperimentando in modo concreto e toccante l'urgenza dello scioglimento dei ghiacciai polari.`;

allData[44].keyPoints = [
  "Olafur Eliasson lavora a Berlino con uno studio multidisciplinare di scienziati, architetti e artigiani.",
  "La sua poetica mette al centro la percezione viva dello spettatore: l'opera d'arte esiste solo nell'esperienza sensoriale di chi la guarda.",
  "In 'The Weather Project' (Tate Modern 2003) crea un sole artificiale gigante e un soffitto a specchio che unisce milioni di persone.",
  "Con 'Ice Watch' porta blocchi di ghiaccio della Groenlandia nelle piazze europee per far toccare con mano l'emergenza climatica."
];

// Capitolo 46: Miguel Chevalier (indice 45)
allData[45].subtitle = "Dalla Computer Art pionieristica del 1978 alle piante virtuali di Sur-Natures e alle opere con l'Intelligenza Artificiale";
allData[45].summary = `### 1. Il primato storico della Computer Art e la formazione

**Miguel Chevalier** nasce a Città del Messico nel 1959 e si trasferisce da ragazzo a Parigi. Compie studi artistici d'eccellenza nelle massime istituzioni francesi e internazionali:
* L'**École Nationale Supérieure des Beaux-Arts** di Parigi (diplomato nel 1980);
* L'**École Nationale Supérieure des Arts Décoratifs** di Parigi;
* Il celebre **Pratt Institute** di New York (1983-1984), dove sperimenta i primi grandi computer da calcolo e incontra i pionieri della grafica digitale.

A partire dal **1978**, Chevalier compie una scelta pionieristica che segnerà tutta la sua carriera: sceglie il **computer** e il codice informatico come suo unico e fondamentale strumento di espressione artistica. All'epoca i computer non avevano finestre grafiche facili né mouse: le immagini non si disegnavano a mano, ma venivano calcolate riga per riga digitando formule matematiche e stringhe di comando. Chevalier è universalmente riconosciuto come uno dei **padri fondatori della Digital Art e della Computer Art nel mondo**.

---

### 2. Poetica: Il Pixel come nuova tessera di mosaico e la Natura Virtuale

La ricerca di Miguel Chevalier attraversa oltre quarant'anni di continua evoluzione tecnologica:
* **Il Pixel come nuova tessera di mosaico**: Chevalier propone un paragone storico-artistico affascinante: **il pixel è l'erede contemporaneo della tessera di pietra del mosaico romano e bizantino**, del puntino di colore nel Puntinismo di Georges Seurat e della pennellata geometrica di Paul Cézanne. Il pixel è la particella elementare della visione digitale moderna: ingrandito su scale monumentali, diventa una meravigliosa superficie luminosa di forme geometriche e colori vibranti.
* **La Natura Artificiale e la Botanica Virtuale**: Chevalier indaga l'incontro tra mondo vegetale e formule informatiche. Crea software capaci di generare piante digitali che crescono secondo leggi biologiche simulate al computer (formule matematiche e geometrie frattali). Nascono così giardini virtuali con semi che germogliano, steli che fioriscono, mutano colore, invecchiano e rinascono in un ciclo continuo e sempre diverso.
* **Installazioni interattive che reagiscono al corpo**: le opere di Chevalier non sono video registrati che si ripetono uguali in cerchio. Sono **opere create in tempo reale dal software**: non si ripetono mai due volte identiche. Inoltre, grazie a sensori a infrarossi e telecamere di movimento, le proiezioni reagiscono all'istante al passaggio, ai passi e ai gesti delle persone nello spazio.

![Miguel Chevalier, Pixels - Une expérience interactive avec l'univers créatif de l'IA, 2024, proiezione immersiva interattiva](assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_pixels.jpg)

---

### 3. Le opere cardine e il dialogo con l'Intelligenza Artificiale

#### Pixels - Una esperienza interattiva con l'universo creativo dell'IA (2024)
* Nella sua recente mostra monografica, Chevalier affronta l'impatto dell'**Intelligenza Artificiale generativa** e delle reti neurali informatiche nell'arte contemporanea.
* L'artista non subisce passivamente la macchina, ma collabora con essa: alimenta i modelli di intelligenza artificiale con il proprio archivio quarantennale di disegni, pixel e piante frattali.
* Nelle sale del museo, migliaia di pixel colorati fluttuano come polvere luminosa sulle pareti e sui pavimenti; al passaggio dei visitatori, la rete neurale riorganizza i pixel all'istante generando forme meravigliose che fondono volti umani, architetture barocche e coralli sottomarini, realizzando una nuova alleanza creativa tra mente umana e computer.

#### Sur-Natures e Fractal Flowers (1998-2015)
![Miguel Chevalier, Sur-Natures, software generativo 3D, piante virtuali interattive](assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_surnatures.jpg)

* Grandiosi giardini virtuali proiettati a 360 gradi sulle pareti. Fiori giganti con petali geometrici fluttuano su fondi scuri. Quando i visitatori si avvicinano, le piante reagiscono piegandosi verso di loro, aprendo i calici e diffondendo suoni armonici, prima di perdere i petali in una pioggia di pixel e far nascere una nuova generazione di fiori digitali.

#### Magic Carpets (Tappeti Magici)
* Proiettati sui pavimenti di monumentali cattedrali storiche o castelli antichi (come a Castel del Monte), enormi tappeti digitali luminosi si compongono di intrecci geometrici ispirati all'arte araba e alla matematica. Camminando sulla pietra antica, i visitatori vedono le linee geometriche ondeggiare e aprirsi sotto le proprie scarpe come onde d'acqua, unendo in modo suggestivo l'architettura del passato alla magia immateriale della luce digitale.`;

allData[45].keyPoints = [
  "Pioniere mondiale della Computer Art, Miguel Chevalier sperimenta con i computer fin dal 1978 tra Parigi e New York.",
  "Paragona il Pixel moderno alla tessera di pietra del mosaico antico e al puntino di colore del Puntinismo di Seurat.",
  "Crea la 'Natura Artificiale' attraverso software generativi che fanno fiorire piante ed erbari digitali in tempo reale ('Sur-Natures').",
  "Le sue opere non sono video registrati, ma flussi visivi che mutano continuamente reagendo ai movimenti dei visitatori.",
  "Con la recente mostra 'Pixels IA' (2024) esplora la collaborazione creativa tra intuizione umana e Intelligenza Artificiale.",
  "Nei 'Magic Carpets' proietta tappeti geometrici interattivi sui pavimenti di cattedrali e castelli storici, fondendo passato e futuro."
];

// Salva i dati aggiornati
const output = 'window.ARTE_DATA = ' + JSON.stringify(allData, null, 2) + ';\n';
fs.writeFileSync(dataFilePath, output, 'utf8');
console.log('Module 4 (Capitoli 41-46) aggiornato e semplificato con successo!');
