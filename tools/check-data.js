#!/usr/bin/env node
/**
 * Verifica di qualita del progetto. Uso:  node tools/check-data.js
 *
 * ERRORI (da correggere sempre):
 *  - capitoli/quiz non coerenti con stats in data/corsi-data.js
 *  - ID capitolo duplicati o senza il prefisso dichiarato in js/subjects.js
 *  - quiz con opzioni != 4, correctIndex mancante o fuori range, spiegazione assente
 *  - immagini referenziate nelle sintesi ma assenti in assets/
 *  - emoji in qualsiasi file sorgente
 * AVVISI (qualita dei contenuti):
 *  - quiz in cui la risposta corretta è nettamente la più lunga (indizio involontario)
 *  - sintesi troppo brevi per lo studio universitario
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.join(__dirname, '..');
const MIN_SUMMARY_WORDS = 500;
const LONGEST_RATIO = 1.3; // risposta corretta più lunga del 30% rispetto alla seconda

const errors = [];
const warnings = [];

function loadScript(rel, ctx) {
  vm.runInContext(fs.readFileSync(path.join(ROOT, rel), 'utf8'), ctx, { filename: rel });
}

const ctx = { window: {} };
vm.createContext(ctx);
loadScript('data/corsi-data.js', ctx);
loadScript('js/subjects.js', ctx);
fs.readdirSync(path.join(ROOT, 'data'))
  .filter(f => f.endsWith('-data.js') && f !== 'corsi-data.js')
  .forEach(f => loadScript('data/' + f, ctx));

const { SUBJECTS, getModuleChapters } = ctx.window.SubjectRegistry;
const ABA = ctx.window.ABA_DATA;

// Materie del piano di studi che puntano a una pagina
const materieByPage = {};
Object.values(ABA.PIANI_STUDIO).forEach(anni => anni.forEach(anno => (anno.materie || []).forEach(m => {
  if (m.page) materieByPage[m.page] = m;
})));

Object.entries(SUBJECTS).forEach(([id, subject]) => {
  const pageRel = `pages/${id}.html`;
  if (!fs.existsSync(path.join(ROOT, pageRel))) errors.push(`${id}: manca ${pageRel}`);
  const materia = materieByPage[pageRel];
  if (!materia) errors.push(`${id}: nessuna materia in corsi-data.js con page "${pageRel}"`);

  const seen = new Set();
  let chapterCount = 0;
  let quizCount = 0;
  let biased = 0;

  subject.modules.forEach(mod => {
    const chapters = getModuleChapters(mod);
    if (chapters.length === 0) errors.push(`${id}/${mod.key}: nessun capitolo (source=${mod.source}, module=${mod.module || '-'})`);
    chapters.forEach(c => {
      chapterCount++;
      const where = `${id}/${c.id}`;
      if (seen.has(c.id)) errors.push(`${where}: ID duplicato`);
      seen.add(c.id);
      if (!subject.idPrefixes.some(p => c.id.startsWith(p))) errors.push(`${where}: ID senza prefisso ${subject.idPrefixes.join('|')}`);

      const words = (c.summary || '').split(/\s+/).filter(Boolean).length;
      if (words < MIN_SUMMARY_WORDS) warnings.push(`${where}: sintesi breve (${words} parole, minimo consigliato ${MIN_SUMMARY_WORDS})`);

      (c.summary || '').replace(/!\[[^\]]*\]\(([^)]+)\)/g, (_, src) => {
        if (/^https?:/.test(src)) return;
        const file = path.join(ROOT, src.replace(/^(\.\.\/)+/, ''));
        if (!fs.existsSync(file)) errors.push(`${where}: immagine mancante ${src}`);
      });

      (c.quiz || []).forEach((q, i) => {
        quizCount++;
        const qw = `${where} quiz ${i + 1}`;
        if (!Array.isArray(q.options) || q.options.length !== 4) errors.push(`${qw}: servono 4 opzioni`);
        if (!Number.isInteger(q.correctIndex) || q.correctIndex < 0 || q.correctIndex >= (q.options || []).length) {
          errors.push(`${qw}: correctIndex mancante o non valido`);
          return;
        }
        if (!q.explanation) errors.push(`${qw}: spiegazione mancante`);
        const lens = q.options.map(o => o.length);
        const others = lens.filter((_, j) => j !== q.correctIndex);
        if (lens[q.correctIndex] > Math.max(...others) * LONGEST_RATIO) biased++;
      });
    });
  });

  if (materia && materia.stats) {
    if (materia.stats.capitoli !== chapterCount) errors.push(`${id}: stats.capitoli=${materia.stats.capitoli} ma i capitoli sono ${chapterCount}`);
    if (materia.stats.quiz !== quizCount) errors.push(`${id}: stats.quiz=${materia.stats.quiz} ma i quiz sono ${quizCount}`);
  }
  if (biased > 0) {
    warnings.push(`${id}: ${biased}/${quizCount} quiz (${Math.round(100 * biased / quizCount)}%) hanno la risposta corretta nettamente più lunga delle altre`);
  }
});

// Emoji in tutti i file sorgente
const EMOJI = /\p{Extended_Pictographic}/u;
const ALLOWED = new Set(['©', '®', '™']); // (c) (R) TM
function scan(dir) {
  fs.readdirSync(dir, { withFileTypes: true }).forEach(e => {
    if (['.git', 'node_modules', 'assets'].includes(e.name)) return;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) return scan(full);
    if (!/\.(html|js|css|md|json)$/.test(e.name) || e.name === 'supabase.min.js') return;
    fs.readFileSync(full, 'utf8').split('\n').forEach((line, n) => {
      for (const ch of line) {
        if (EMOJI.test(ch) && !ALLOWED.has(ch)) {
          errors.push(`${path.relative(ROOT, full)}:${n + 1}: emoji vietata "${ch}"`);
          break;
        }
      }
    });
  });
}
scan(ROOT);

warnings.forEach(w => console.log('AVVISO  ' + w));
errors.forEach(e => console.log('ERRORE  ' + e));
console.log(`\n${errors.length} errori, ${warnings.length} avvisi`);
process.exit(errors.length ? 1 : 0);
