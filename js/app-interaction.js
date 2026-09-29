/**
 * App Interaction Design — Logica specifica per la materia
 * Dipende da: js/core.js, data/interaction-data.js
 * Docente: Prof. Giulio Interlandi (ABTEC 42 - 8 CFA)
 * Accademia di Belle Arti di Catania
 * DIVIETO ASSOLUTO DI EMOJI
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getAllChapters() {
    if (window.INTERACTION_DATA && Array.isArray(window.INTERACTION_DATA.chapters)) {
      return window.INTERACTION_DATA.chapters;
    }
    if (window.INTERACTION_CHAPTERS) {
      return window.INTERACTION_CHAPTERS;
    }
    if (Array.isArray(window.INTERACTION_DATA)) {
      return window.INTERACTION_DATA;
    }
    return [];
  }

  function getCurrentPdfChapters() {
    const all = getAllChapters();
    if (state.activePdf === 'ixd-fondamenti-design-thinking') return all.filter(c => c.module === 'ixd-fondamenti-design-thinking');
    if (state.activePdf === 'ixd-user-research') return all.filter(c => c.module === 'ixd-user-research');
    if (state.activePdf === 'ixd-teoria-sociologia') return all.filter(c => c.module === 'ixd-teoria-sociologia');
    if (state.activePdf === 'ixd-strumenti-prototipazione') return all.filter(c => c.module === 'ixd-strumenti-prototipazione');
    return all.filter(c => c.module === 'ixd-fondamenti-design-thinking');
  }

  function getPdfDisplayName(key) {
    if (key === 'ixd-fondamenti-design-thinking') return '1. Fondamenti & Design Thinking';
    if (key === 'ixd-user-research') return '2. Metodologie & User Research';
    if (key === 'ixd-teoria-sociologia') return '3. Esperienza & Sociologia';
    if (key === 'ixd-strumenti-prototipazione') return '4. Prototipazione & Strumenti';
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
      getQuizzesFromChapters(getAllChapters(), 'Interaction Design');
    }
    return pool;
  }

  function updateProgressIndicators() {
    const pdfKeys = ['ixd-fondamenti-design-thinking', 'ixd-user-research', 'ixd-teoria-sociologia', 'ixd-strumenti-prototipazione'];
    const all = getAllChapters();
    pdfKeys.forEach(pdfKey => {
      let chaps = all.filter(c => c.module === pdfKey);

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
    
    // Imposta materia attiva
    state.currentSubject = 'interaction';
    
    // Valida PDF attivo
    const validPdfs = ['ixd-fondamenti-design-thinking', 'ixd-user-research', 'ixd-teoria-sociologia', 'ixd-strumenti-prototipazione'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'ixd-fondamenti-design-thinking';
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

  // Avvio al caricamento del DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
