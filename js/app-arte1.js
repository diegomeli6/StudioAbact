/**
 * App Storia dell'Arte Contemporanea 1 — Logica specifica per la materia (1° Anno DAPL08)
 * Dipende da: js/core.js, data/arte1-data.js
 * Rispetto assoluto: ZERO EMOJI
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getCurrentPdfChapters() {
    const allArte1 = window.ARTE1_DATA || [];
    if (state.activePdf === 'arte1-anni50') return allArte1.filter(c => c.module === 'anni50');
    if (state.activePdf === 'arte1-anni60') return allArte1.filter(c => c.module === 'anni60');
    if (state.activePdf === 'arte1-anni70') return allArte1.filter(c => c.module === 'anni70');
    if (state.activePdf === 'arte1-monografie') return allArte1.filter(c => c.module === 'monografie');
    // Fallback per sotto-moduli monografie
    if (state.activePdf === 'arte1-magritte') return allArte1.filter(c => c.id === 'arte1-c54');
    if (state.activePdf === 'arte1-manray') return allArte1.filter(c => c.id === 'arte1-c55');
    if (state.activePdf === 'arte1-warhol') return allArte1.filter(c => c.id === 'arte1-c56');
    return allArte1.filter(c => c.module === 'anni50');
  }

  function getPdfDisplayName(key) {
    if (key === 'arte1-anni50') return "1. Anni '50 — L'Informale e il Dopoguerra";
    if (key === 'arte1-anni60') return "2. Anni '60 — Dalla Pop Art all'Arte Povera";
    if (key === 'arte1-anni70') return "3. Anni '70 — Smaterializzazione, Spazio e Corpo";
    if (key === 'arte1-monografie') return "4. Monografie — Magritte, Man Ray, Warhol";
    if (key === 'arte1-magritte') return "René Magritte — Il Mistero del Visibile";
    if (key === 'arte1-manray') return "Man Ray — Dall'Avanguardia Dada alle Rayografie";
    if (key === 'arte1-warhol') return "Andy Warhol — La Macchina delle Icone e la Factory";
    return key;
  }

  function getExamPool(scope, _getCurrentPdf, _getDisplayName) {
    let pool = [];
    const getQuizzesFromChapters = (chapList, sourceName) => {
      chapList.forEach(chap => {
        const list = (chap.examQuiz && chap.examQuiz.length > 0) ? chap.examQuiz : (chap.quiz || []);
        list.forEach(q => {
          pool.push({
            ...q,
            sourceName: sourceName,
            chapNum: chap.number,
            chapTitle: chap.title
          });
        });
      });
    };

    if (scope === 'current') {
      getQuizzesFromChapters(getCurrentPdfChapters(), getPdfDisplayName(state.activePdf));
    } else {
      getQuizzesFromChapters(window.ARTE1_DATA || [], "Storia dell'Arte Contemporanea 1");
    }
    return pool;
  }

  function updateProgressIndicators() {
    const arte1Pdfs = ['arte1-anni50', 'arte1-anni60', 'arte1-anni70', 'arte1-monografie'];
    const allArte1 = window.ARTE1_DATA || [];
    arte1Pdfs.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'arte1-anni50') chaps = allArte1.filter(c => c.module === 'anni50');
      if (pdfKey === 'arte1-anni60') chaps = allArte1.filter(c => c.module === 'anni60');
      if (pdfKey === 'arte1-anni70') chaps = allArte1.filter(c => c.module === 'anni70');
      if (pdfKey === 'arte1-monografie') chaps = allArte1.filter(c => c.module === 'monografie');

      let done = 0;
      chaps.forEach(c => {
        if (state.completed[c.id]) done++;
      });

      const badge = document.getElementById(`prog-mini-${pdfKey}`);
      if (badge) badge.textContent = `${done}/${chaps.length}`;

      if (pdfKey === state.activePdf) {
        const pct = chaps.length > 0 ? Math.round((done / chaps.length) * 100) : 0;
        const barText = document.getElementById('active-pdf-progress-text');
        if (barText) barText.textContent = `Progresso: ${pct}% (${done} di ${chaps.length} completati)`;
      }
    });
  }

  // Esponi globalmente per core.js e auth.js
  window.updateProgressIndicators = updateProgressIndicators;
  window.doRenderSidebar = doRenderSidebar;
  window.doRenderChapter = doRenderChapter;

  function doRenderSidebar() {
    core.renderSidebar(getCurrentPdfChapters, doNavigate);
  }

  function doRenderChapter() {
    core.renderCurrentChapter(getCurrentPdfChapters, getPdfDisplayName);
  }

  function doNavigate(idx) {
    core.navigateToChapter(idx, getCurrentPdfChapters, doRenderSidebar, doRenderChapter);
  }

  function init() {
    core.loadLocalState();

    // Forza materia arte1
    state.currentSubject = 'arte1';

    // Valida PDF attivo
    const validPdfs = ['arte1-anni50', 'arte1-anni60', 'arte1-anni70', 'arte1-monografie', 'arte1-magritte', 'arte1-manray', 'arte1-warhol'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'arte1-anni50';
      state.activeChapIndex = 0;
    }

    core.applyTheme(state.theme);

    // Attiva la tab corretta
    document.querySelectorAll('.pdf-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.pdf === state.activePdf);
    });

    // Setup events
    core.setupCoreEvents(getCurrentPdfChapters, doRenderSidebar, doRenderChapter, doNavigate);
    core.setupExamEvents(getCurrentPdfChapters, getPdfDisplayName, getExamPool);

    // Render iniziale
    core.switchView(state.activeView || 'study');
    doRenderSidebar();
    doRenderChapter();
    updateProgressIndicators();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
