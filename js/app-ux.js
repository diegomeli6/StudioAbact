/**
 * App UX & Web Design — Logica specifica per la materia
 * Dipende da: js/core.js, data/dispense-data.js, krug-data.js, stull-data.js, 
 *             maeda-data.js, glossary-data.js
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getCurrentPdfChapters() {
    if (state.activePdf === 'dispense') return window.DISPENSE_DATA || [];
    if (state.activePdf === 'krug') return window.KRUG_DATA || [];
    if (state.activePdf === 'stull') return window.STULL_DATA || [];
    if (state.activePdf === 'maeda') return window.MAEDA_DATA || [];
    return [];
  }

  function getPdfDisplayName(key) {
    if (key === 'dispense') return '1. Dispense Professore';
    if (key === 'krug') return "2. Steve Krug — Don't Make Me Think";
    if (key === 'stull') return '3. Edward Stull — UX Design';
    if (key === 'maeda') return '4. John Maeda — Le leggi della semplicita\'';
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
      getQuizzesFromChapters(window.DISPENSE_DATA || [], 'Dispense Professore');
      getQuizzesFromChapters(window.KRUG_DATA || [], "Krug — Don't Make Me Think");
      getQuizzesFromChapters(window.STULL_DATA || [], 'Stull — UX Design');
      getQuizzesFromChapters(window.MAEDA_DATA || [], 'Maeda — Le leggi della semplicita\'');
    }
    return pool;
  }

  function updateProgressIndicators() {
    const webPdfs = ['dispense', 'krug', 'stull', 'maeda'];
    webPdfs.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'dispense') chaps = window.DISPENSE_DATA || [];
      if (pdfKey === 'krug') chaps = window.KRUG_DATA || [];
      if (pdfKey === 'stull') chaps = window.STULL_DATA || [];
      if (pdfKey === 'maeda') chaps = window.MAEDA_DATA || [];

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

  // Esponi globalmente per core.js
  window.updateProgressIndicators = updateProgressIndicators;

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
    
    // Forza materia web-design
    state.currentSubject = 'web-design';
    
    // Valida PDF attivo
    const validPdfs = ['dispense', 'krug', 'stull', 'maeda'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'dispense';
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
