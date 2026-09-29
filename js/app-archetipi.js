/**
 * App Archetipi dell'immaginario — Logica specifica per la materia
 * Dipende da: js/core.js, data/archetipi-data.js
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getAllChapters() {
    if (window.ARCHETIPI_DATA && Array.isArray(window.ARCHETIPI_DATA.chapters)) {
      return window.ARCHETIPI_DATA.chapters;
    }
    if (window.ARCHETIPI_CHAPTERS) {
      return window.ARCHETIPI_CHAPTERS;
    }
    if (Array.isArray(window.ARCHETIPI_DATA)) {
      return window.ARCHETIPI_DATA;
    }
    return [];
  }

  function getCurrentPdfChapters() {
    const all = getAllChapters();
    if (state.activePdf === 'archetipi-ecologica') return all.filter(c => c.module === 'archetipi-ecologica');
    if (state.activePdf === 'archetipi-jung') return all.filter(c => c.module === 'archetipi-jung');
    if (state.activePdf === 'archetipi-simbologia') return all.filter(c => c.module === 'archetipi-simbologia');
    return all.filter(c => c.module === 'archetipi-ecologica');
  }

  function getPdfDisplayName(key) {
    if (key === 'archetipi-ecologica') return '1. Verso una Dimensione Ecologica';
    if (key === 'archetipi-jung') return '2. Inconscio Collettivo & Archetipi';
    if (key === 'archetipi-simbologia') return '3. Linguaggi Simbolici & Epigenetica';
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
      getQuizzesFromChapters(getAllChapters(), "Archetipi dell'immaginario");
    }
    return pool;
  }

  function updateProgressIndicators() {
    const pdfKeys = ['archetipi-ecologica', 'archetipi-jung', 'archetipi-simbologia'];
    const all = getAllChapters();
    pdfKeys.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'archetipi-ecologica') chaps = all.filter(c => c.module === 'archetipi-ecologica');
      if (pdfKey === 'archetipi-jung') chaps = all.filter(c => c.module === 'archetipi-jung');
      if (pdfKey === 'archetipi-simbologia') chaps = all.filter(c => c.module === 'archetipi-simbologia');

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
    
    // Forza materia archetipi
    state.currentSubject = 'archetipi';
    
    // Valida PDF attivo
    const validPdfs = ['archetipi-ecologica', 'archetipi-jung', 'archetipi-simbologia'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'archetipi-ecologica';
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
