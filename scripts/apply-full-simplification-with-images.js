const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 1. Estrai il file originale completo e integro dal commit b37add5
const dataFilePath = path.join(__dirname, '..', 'data', 'arte-data.js');
const b37Content = execSync('git show b37add5:data/arte-data.js', { maxBuffer: 10 * 1024 * 1024 }).toString();

const sandboxB37 = { window: {} };
eval(b37Content.replace('window.ARTE_DATA', 'sandboxB37.window.ARTE_DATA'));
const b37Data = sandboxB37.window.ARTE_DATA;

// 2. Verifica preliminare delle immagini originali su disco
const imgRegex = /!\[(.*?)\]\((.*?)\)/g;
let m;
let b37ImgCount = 0;
let missingBefore = 0;
while ((m = imgRegex.exec(b37Content)) !== null) {
  b37ImgCount++;
  const imgPath = path.join(__dirname, '..', m[2]);
  if (!fs.existsSync(imgPath)) {
    console.error(`Immagine mancante su disco in b37: ${m[2]}`);
    missingBefore++;
  }
}

if (b37ImgCount !== 63 || missingBefore !== 0) {
  throw new Error(`Errore preliminare immagini in b37: trovate ${b37ImgCount}, mancanti ${missingBefore}`);
}

console.log(`Verifica b37 completata: ${b37ImgCount} immagini totali, tutte presenti su disco.`);

// 3. Tabella delle sostituzioni lessicali mirate
const replacements = [
  // Frasi composte (da valutare prima dei singoli termini)
  [/\bspinta utopica, progressista e teleologica\b/gi, "spinta ideale, progressista e orientata a un fine unico"],
  [/\bgrandi racconti metastorici\b/gi, "grandi ideologie e teorie assolute sul destino dell'umanità"],
  [/\bctonia, tellurica e viscerale\b/gi, "legata alla terra, alle origini viscerali e primordiali"],
  [/\bvisione ctonia\b/gi, "visione legata alla terra profonda"],
  [/\bcesura radicale\b/gi, "svolta netta e radicale"],
  [/\bcesura epocale\b/gi, "rottura storica epocale"],
  [/\binsofferenza viscerale\b/gi, "profonda insofferenza"],
  [/\bprovincialismo istituzionale asfittico\b/gi, "chiuso provincialismo delle istituzioni"],
  [/\bnomade per antonomasia\b/gi, "il tipico artista nomade"],
  [/\bforme monumentali ed egoiche\b/gi, "forme monumentali e imponenti"],
  [/\bfeticcio della merce\b/gi, "culto ossessivo della merce"],
  [/\begemonia eurocentrica\b/gi, "dominio esclusivo della cultura occidentale"],
  [/\bspazio claustrofobico\b/gi, "spazio chiuso e opprimente"],
  [/\bpurgazione catartica\b/gi, "liberazione emotiva e purificazione"],

  // Singoli termini filosofici o critici astrusi
  [/\bteleologica\b/gi, "orientata a un fine unico"],
  [/\bteleologico\b/gi, "orientato a uno scopo predefinito"],
  [/\bteleologici\b/gi, "orientati a uno scopo predefinito"],
  [/\bteleologiche\b/gi, "orientate a uno scopo predefinito"],
  [/\bcesura\b/gi, "svolta netta"],
  [/\bcesure\b/gi, "fratture storiche"],
  [/\bmetastorici\b/gi, "universali e assoluti"],
  [/\bmetastorico\b/gi, "universale e assoluto"],
  [/\bmetastorica\b/gi, "universale e assoluta"],
  [/\bmetastoriche\b/gi, "universali e assolute"],
  [/\bctonia\b/gi, "legata alla terra profonda"],
  [/\bctonio\b/gi, "legato alla terra profonda"],
  [/\bctonii\b/gi, "legati alla terra profonda"],
  [/\bctonie\b/gi, "legate alla terra profonda"],
  [/\btellurica\b/gi, "legata alla forza della terra"],
  [/\btellurico\b/gi, "legato alla forza della terra"],
  [/\btellurici\b/gi, "legati alla forza della terra"],
  [/\btelluriche\b/gi, "legate alla forza della terra"],
  [/\baporia\b/gi, "contraddizione insolubile"],
  [/\baporie\b/gi, "contraddizioni insolubili"],
  [/\btaumaturgico\b/gi, "miracoloso e risanatore"],
  [/\btaumaturgica\b/gi, "miracolosa e risanatrice"],
  [/\btaumaturgici\b/gi, "miracolosi e risanatori"],
  [/\btaumaturgiche\b/gi, "miracolose e risanatrici"],
  [/\bapotropaico\b/gi, "protettivo contro il male"],
  [/\bapotropaica\b/gi, "protettiva contro il male"],
  [/\bapotropaici\b/gi, "protettivi contro il male"],
  [/\bapotropaiche\b/gi, "protettive contro il male"],
  [/\bescatologico\b/gi, "relativo al destino ultimo dell'uomo"],
  [/\bescatologica\b/gi, "relativa al destino finale"],
  [/\bescatologici\b/gi, "relativi al destino finale"],
  [/\bescatologia\b/gi, "riflessione sul destino ultimo"],
  [/\bgnoseologico\b/gi, "conoscitivo"],
  [/\bgnoseologica\b/gi, "della conoscenza"],
  [/\bgnoseologici\b/gi, "della conoscenza"],
  [/\bepistemologico\b/gi, "relativo alla conoscenza scientifica"],
  [/\bepistemologica\b/gi, "sulla natura della conoscenza"],
  [/\bepistemologici\b/gi, "relativi alla conoscenza"],
  [/\bermeneutico\b/gi, "interpretativo"],
  [/\bermeneutica\b/gi, "interpretativa"],
  [/\bpalinsesto\b/gi, "sovrapposizione di strati"],
  [/\bpalinsesti\b/gi, "sovrapposizioni di strati"],
  [/\babietto\b/gi, "abietto (disgustoso e degradato)"],
  [/\babietta\b/gi, "abietta (disgustosa e degradata)"],
  [/\babietti\b/gi, "abietti (disgustosi e degradati)"],
  [/\babiezione\b/gi, "degradazione estrema e disgusto"],
  [/\baniconico\b/gi, "privo di figure umane o animali"],
  [/\aniconica\b/gi, "priva di immagini figurative"],
  [/\baniconici\b/gi, "privi di immagini figurative"],
  [/\bdemiurgico\b/gi, "creativo e onnipotente"],
  [/\bdemiurgo\b/gi, "creatore supremo"],
  [/\bdemiurgica\b/gi, "creativa e ordinatrice"],
  [/\btautologico\b/gi, "chiuso su se stesso e ripetitivo"],
  [/\btautologica\b/gi, "chiusa su se stessa e ripetitiva"],
  [/\btautologia\b/gi, "ripetizione dello stesso concetto"],
  [/\btautologie\b/gi, "ripetizioni dello stesso concetto"],
  [/\bsolipsistico\b/gi, "isolato ed ego-centrato"],
  [/\bsolipsistica\b/gi, "chiusa in se stessa"],
  [/\beterotopico\b/gi, "spazio alternativo con proprie regole"],
  [/\beterotopica\b/gi, "spazio alternativo con proprie regole"],
  [/\beterotopia\b/gi, "spazio reale alternativo con proprie regole"],
  [/\beterotopie\b/gi, "spazi reali alternativi con proprie regole"],
  [/\bpanopticon\b/gi, "dispositivo di controllo e sorveglianza totale"],
  [/\bfeticizzazione\b/gi, "trasformazione in oggetto di culto o desiderio"],
  [/\breificazione\b/gi, "trasformazione dell'essere umano in merce"],
  [/\breificato\b/gi, "ridotto a oggetto o merce"],
  [/\breificata\b/gi, "ridotta a oggetto o merce"],
  [/\breificati\b/gi, "ridotti a oggetti o merci"],
  [/\btanatologico\b/gi, "legato alla morte"],
  [/\btanatologica\b/gi, "legata alla meditazione sulla morte"],
  [/\bcatartico\b/gi, "liberatorio e purificatore"],
  [/\bcatartica\b/gi, "liberatoria e purificatrice"],
  [/\bcatartici\b/gi, "liberatori e purificatori"],
  [/\bcatarsi\b/gi, "liberazione e purificazione interiore"],
  [/\bdiaspora\b/gi, "dispersione nel mondo di un popolo"],
  [/\bdiasporico\b/gi, "legato all'emigrazione e dispersione di un popolo"],
  [/\bdiasporica\b/gi, "legata all'emigrazione e alla dispersione culturale"],
  [/\banamorfosi\b/gi, "illusione ottica visibile solo da una precisa angolazione"],
  [/\banamorfico\b/gi, "visibile solo da una precisa prospettiva ottica"],
  [/\banamorfica\b/gi, "visibile solo da una precisa prospettiva ottica"],
  [/\bautopoietico\b/gi, "capace di rigenerarsi autonomamente"],
  [/\bautopoietica\b/gi, "capace di rigenerarsi e sostenersi da sola"],
  [/\bsinestetico\b/gi, "che unisce più sensi insieme"],
  [/\bsinestetica\b/gi, "che coinvolge più sensi contemporaneamente"],
  [/\bsinestetici\b/gi, "che uniscono più percezioni sensoriali"],
  [/\bsinestesia\b/gi, "fusione tra diversi sensi (colori, suoni, profumi)"],
  [/\bsinestesie\b/gi, "fusioni tra diversi sensi"],
  [/\bdecontestualizzazione\b/gi, "estrazione dal contesto originario"],
  [/\bdecontestualizzato\b/gi, "estratto dal suo ambiente originario"],
  [/\bdecontestualizzata\b/gi, "separata dal suo contesto originale"],
  [/\bautoreferenziale\b/gi, "che parla solo di se stesso"],
  [/\bautoreferenziali\b/gi, "chiusi nel riferimento a se stessi"],
  [/\bautoreferenzialità\b/gi, "ripiegamento su se stesso"],
  [/\bmitopoiesi\b/gi, "creazione di miti personali o collettivi"],
  [/\bmitopoietico\b/gi, "capace di generare nuovi miti"],
  [/\bmitopoietica\b/gi, "capace di generare miti simbolici"],
  [/\bpalingenesi\b/gi, "rinascita o rinnovamento radicale"],
  [/\bpalingenetico\b/gi, "di rinnovamento radicale"],
  [/\bpalingenetica\b/gi, "di rigenerazione radicale"],
  [/\bapodittici\b/gi, "categorici e perentori"],
  [/\bapodittico\b/gi, "categorico e perentorio"],
  [/\biconoclastia\b/gi, "rifiuto e distruzione dei modelli tradizionali"],
  [/\biconoclasta\b/gi, "sfidante e distruttore di modelli tradizionali"],
  [/\bsimulacro\b/gi, "simulacro (immagine o copia che sostituisce la realtà)"],
  [/\bsimulacri\b/gi, "simulacri (immagini o copie che sostituiscono la realtà)"],
  [/\bperturbante\b/gi, "perturbante (inquietante ed estraneo pur essendo familiare)"],
  [/\bperturbanti\b/gi, "perturbanti (inquietanti ed estranee pur essendo familiari)"],
  [/\bontologico\b/gi, "profondo ed esistenziale"],
  [/\bontologica\b/gi, "profonda ed esistenziale"],
  [/\bontologici\b/gi, "profondi ed esistenziali"],
  [/\bintersoggettività\b/gi, "relazione e scambio umano tra individui"],
  [/\bintersoggettivo\b/gi, "basato sulla relazione e sullo scambio tra individui"],
  [/\bprossemica\b/gi, "distanza fisica e relazionale nello spazio"],
  [/\bprossemico\b/gi, "relativo allo spazio e alla vicinanza fisica"],
  [/\beurocentrico\b/gi, "incentrato solo sulla cultura occidentale"],
  [/\beurocentrica\b/gi, "incentrata solo sulla cultura occidentale"],
  [/\basfittico\b/gi, "soffocante e privo di sbocchi"],
  [/\basfittica\b/gi, "soffocante e priva di sbocchi"],
  [/\bintrinsecamente\b/gi, "per sua natura"]
];

function simplifyText(text) {
  if (!text || typeof text !== 'string') return text;

  // 1. Isola e protegge i tag markdown delle immagini
  const tokens = [];
  const protectedText = text.replace(/!\[(.*?)\]\((.*?)\)/g, (match) => {
    const token = `___IMG_TOKEN_${tokens.length}___`;
    tokens.push(match);
    return token;
  });

  // 2. Applica le semplificazioni lessicali
  let result = protectedText;
  for (const [pattern, repl] of replacements) {
    result = result.replace(pattern, repl);
  }

  // 3. Ripristina i tag delle immagini al 100% identici
  tokens.forEach((tag, idx) => {
    result = result.replace(`___IMG_TOKEN_${idx}___`, tag);
  });

  return result;
}

function processObj(obj) {
  if (typeof obj === 'string') {
    return simplifyText(obj);
  }
  if (Array.isArray(obj)) {
    return obj.map(processObj);
  }
  if (obj && typeof obj === 'object') {
    const res = {};
    for (const k in obj) {
      res[k] = processObj(obj[k]);
    }
    return res;
  }
  return obj;
}

// 4. Elaborazione di tutti i capitoli
const processedData = processObj(b37Data);

// 5. Verifiche di integrità assolute
let finalImageCount = 0;
let finalMissingOnDisk = 0;
let mismatchWithB37 = 0;

for (let i = 0; i < 46; i++) {
  const origImgs = [];
  let match;
  const re1 = /!\[(.*?)\]\((.*?)\)/g;
  while ((match = re1.exec(b37Data[i].summary)) !== null) {
    origImgs.push(match[0]);
  }

  const procImgs = [];
  const re2 = /!\[(.*?)\]\((.*?)\)/g;
  while ((match = re2.exec(processedData[i].summary)) !== null) {
    finalImageCount++;
    procImgs.push(match[0]);
    const p = path.join(__dirname, '..', match[2]);
    if (!fs.existsSync(p)) {
      console.error(`Immagine mancante su disco in Cap ${i+1}: ${match[2]}`);
      finalMissingOnDisk++;
    }
  }

  if (JSON.stringify(origImgs) !== JSON.stringify(procImgs)) {
    console.error(`Discrepanza immagini nel capitolo ${i+1}!`);
    mismatchWithB37++;
  }
}

if (finalImageCount !== 63 || finalMissingOnDisk !== 0 || mismatchWithB37 !== 0) {
  throw new Error(`Verifica finale fallita! Immagini: ${finalImageCount}, Mancanti: ${finalMissingOnDisk}, Discrepanze: ${mismatchWithB37}`);
}

// Verifica zero emoji
const jsonString = JSON.stringify(processedData, null, 2);
const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F1E6}-\u{1F1FF}\u{1F600}-\u{1F64F}\u{1F680}-\u{1F6FF}\u{1FA70}-\u{1FAFF}]/u;
const emojiMatches = jsonString.match(new RegExp(emojiRegex, 'gu'));
if (emojiMatches && emojiMatches.length > 0) {
  throw new Error(`Rilevate ${emojiMatches.length} emoji unicode non permesse!`);
}

// 6. Scrittura del file data/arte-data.js
const outputCode = 'window.ARTE_DATA = ' + jsonString + ';\n';
fs.writeFileSync(dataFilePath, outputCode, 'utf8');

console.log('Operazione completata con successo!');
console.log(`- Capitoli elaborati: ${processedData.length}`);
console.log(`- Immagini ripristinate e verificate: ${finalImageCount}/63 (0 mancanti su disco)`);
console.log(`- Emoji presenti: 0`);
