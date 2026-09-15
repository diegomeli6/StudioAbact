const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const dataFilePath = path.join(__dirname, '..', 'data', 'arte-data.js');
let currentContent = fs.readFileSync(dataFilePath, 'utf8');

const sandboxCurrent = { window: {} };
eval(currentContent.replace('window.ARTE_DATA', 'sandboxCurrent.window.ARTE_DATA'));
const currentData = sandboxCurrent.window.ARTE_DATA;

// Estrai b37add5
const b37Content = execSync('git show b37add5:data/arte-data.js', { maxBuffer: 10 * 1024 * 1024 }).toString();
const sandboxB37 = { window: {} };
eval(b37Content.replace('window.ARTE_DATA', 'sandboxB37.window.ARTE_DATA'));
const b37Data = sandboxB37.window.ARTE_DATA;

const imgRegex = /!\[(.*?)\]\((.*?)\)/g;

// Per ciascun capitolo, prendi la lista esatta delle immagini da b37Data
for (let i = 0; i < 46; i++) {
  const b37Images = [];
  let m;
  while ((m = imgRegex.exec(b37Data[i].summary)) !== null) {
    b37Images.push(m[0]);
  }

  // Sostituisci o ripristina con precisione chirurgica le immagini nel summary del capitolo corrente
  let summary = currentData[i].summary;

  // Rimuovi eventuali immagini correnti errate per reinserire esattamente quelle originali di b37Data
  // Ma facciamolo in modo mirato:
  // Cap 4 (Clemente)
  if (i === 3) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/clemente_.*?\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 5 (Cucchi)
  else if (i === 4) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/cucchi_.*?\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 8 (Schnabel & Salle)
  else if (i === 7) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/schnabel_.*?\.jpg\)/g,
      b37Images[0] + '\n\n' + b37Images[1]
    );
  }
  // Cap 9 (Neue Wilde)
  else if (i === 8) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/fetting_.*?\.jpg\)/g,
      b37Images[0] + '\n\n' + b37Images[1]
    );
  }
  // Cap 12 (Polke & Richter)
  else if (i === 11) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/polke_rasterbild\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 14 (Haring)
  else if (i === 13) {
    // Inserisci anche la seconda immagine (Tuttomondo) nella sezione 3
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /### 3\. Democratizzazione dell'arte, attivismo e impegno civile/g,
        '### 3. Democratizzazione dell\'arte, attivismo e impegno civile\n\n' + b37Images[1]
      );
    }
  }
  // Cap 15 (Sherman)
  else if (i === 14) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/sherman_.*?\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 16 (Kruger & Prince)
  else if (i === 15) {
    // Aggiungi Prince nella sezione 2
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /### 2\. Richard Prince e l'Appropriazionismo puro: La 'Re-Photography'/g,
        '### 2. Richard Prince e l\'Appropriazionismo puro: La \'Re-Photography\'\n\n' + b37Images[1]
      );
    }
  }
  // Cap 17 (Becher)
  else if (i === 16) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/becher_.*?\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 21 (Shonibare & Kentridge)
  else if (i === 20) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/shonibare_the_swing\.jpg\)/g,
      b37Images[0]
    );
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /### 3\. William Kentridge: La memoria dell'Apartheid e il disegno cancellato/g,
        '### 3. William Kentridge: La memoria dell\'Apartheid e il disegno cancellato\n\n' + b37Images[1]
      );
    }
  }
  // Cap 22 (Orozco & Hatoum)
  else if (i === 21) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/hatoum_homebound\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 23 (Gonzalez-Torres)
  else if (i === 22) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/gonzalez_torres_lovers\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 24 (Neshat & Walker)
  else if (i === 23) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/kara_walker_silhouette\.jpg\)/g,
      b37Images[1]
    );
    if (!summary.includes(b37Images[0])) {
      summary = summary.replace(
        /### 2\. Shirin Neshat: Il velo, la poesia persiana e il fuoco delle armi/g,
        '### 2. Shirin Neshat: Il velo, la poesia persiana e il fuoco delle armi\n\n' + b37Images[0]
      );
    }
  }
  // Cap 27 (Barney)
  else if (i === 26) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/barney_cremaster3\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 28 (Chapman & Ray)
  else if (i === 27) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/charles_ray_family\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 29 (Bourriaud)
  else if (i === 28) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/arte_relazionale_generale\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 30 (Tiravanija & Höller)
  else if (i === 29) {
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /### 2\. Carsten Höller: Lo scienziato che fa nascere il dubbio e gli scivoli monumentali/g,
        '### 2. Carsten Höller: Lo scienziato che fa nascere il dubbio e gli scivoli monumentali\n\n' + b37Images[1]
      );
    }
  }
  // Cap 31 (Beecroft)
  else if (i === 30) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/beecroft_vb52\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 35 (Paci)
  else if (i === 34) {
    // Sostituisci l'immagine con quella di b37
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/paci_apparizione\.jpg\)/g,
      ''
    );
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/paci_centro_permanenza\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 36 (Vezzoli)
  else if (i === 35) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/vezzoli_caligula\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 38 (Hirschhorn)
  else if (i === 37) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/hirschhorn_gramsci\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 39 (Cao Fei)
  else if (i === 38) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/cao_fei_utopia\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 41 (Cattelan)
  else if (i === 40) {
    // Cap 41 ha 3 immagini in b37
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/cattelan_nona_ora\.jpg\)/g,
      b37Images[0]
    );
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /#### Him \(Lui, 2001\)/g,
        b37Images[1] + '\n\n#### Him (Lui, 2001)'
      );
    }
    if (!summary.includes(b37Images[2])) {
      summary = summary.replace(
        /#### L\.O\.V\.E\. \(Il dito medio a Piazza Affari, Milano, 2010\)/g,
        b37Images[2] + '\n\n#### L.O.V.E. (Il dito medio a Piazza Affari, Milano, 2010)'
      );
    }
  }
  // Cap 42 (Hirst)
  else if (i === 41) {
    // Cap 42 ha 3 immagini in b37
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/hirst_skull\.jpg\)/g,
      b37Images[2]
    );
    if (!summary.includes(b37Images[0])) {
      summary = summary.replace(
        /### 2\. Poetica: La morte inevitabile, la scienza e l'illusione dei farmaci/g,
        '### 2. Poetica: La morte inevitabile, la scienza e l\'illusione dei farmaci\n\n' + b37Images[0]
      );
    }
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /### 3\. Dal teschio di diamanti all'asta record da Sotheby's/g,
        b37Images[1] + '\n\n### 3. Dal teschio di diamanti all\'asta record da Sotheby\'s'
      );
    }
  }
  // Cap 43 (Banksy)
  else if (i === 42) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/banksy_love_bin\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 44 (Ai Weiwei)
  else if (i === 43) {
    summary = summary.replace(
      /!\[.*?\]\(assets\/corsi\/dapl08\/anno-2\/storia-arte-2\/images\/ai_weiwei_seeds\.jpg\)/g,
      b37Images[0]
    );
  }
  // Cap 45 (Eliasson)
  else if (i === 44) {
    if (!summary.includes(b37Images[1])) {
      summary = summary.replace(
        /#### Ice Watch \(2014, Parigi e Londra\)/g,
        b37Images[1] + '\n\n#### Ice Watch (2014, Parigi e Londra)'
      );
    }
  }

  currentData[i].summary = summary;
}

const output = 'window.ARTE_DATA = ' + JSON.stringify(currentData, null, 2) + ';\n';
fs.writeFileSync(dataFilePath, output, 'utf8');
console.log('Ripristino delle immagini originali completato!');
