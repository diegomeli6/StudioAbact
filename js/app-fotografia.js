/**
 * App Fotografia Digitale — Logica specifica per la materia
 * Dipende da: js/core.js, data/fotografia-data.js
 * Docente: Prof. Carmelo Bongiorno (ABPR 31 - 8 CFA)
 * Accademia di Belle Arti di Catania
 * DIVIETO ASSOLUTO DI EMOJI
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getAllChapters() {
    if (window.FOTOGRAFIA_DATA && Array.isArray(window.FOTOGRAFIA_DATA.chapters)) {
      return window.FOTOGRAFIA_DATA.chapters;
    }
    if (window.FOTOGRAFIA_CHAPTERS) {
      return window.FOTOGRAFIA_CHAPTERS;
    }
    if (Array.isArray(window.FOTOGRAFIA_DATA)) {
      return window.FOTOGRAFIA_DATA;
    }
    return [];
  }

  function getCurrentPdfChapters() {
    const all = getAllChapters();
    if (state.activePdf === 'foto-tecnica') return all.filter(c => c.module === 'foto-tecnica');
    if (state.activePdf === 'foto-teoria') return all.filter(c => c.module === 'foto-teoria');
    if (state.activePdf === 'foto-autori') return all.filter(c => c.module === 'foto-autori');
    if (state.activePdf === 'foto-maestri') return all.filter(c => c.module === 'foto-maestri');
    return all.filter(c => c.module === 'foto-tecnica');
  }

  function getPdfDisplayName(key) {
    if (key === 'foto-tecnica') return '1. Tecnica & Grammatica';
    if (key === 'foto-teoria') return '2. Teoria & Inconscio';
    if (key === 'foto-autori') return '3. I 15 Autori Contemporanei';
    if (key === 'foto-maestri') return '4. I Grandi Maestri Storici';
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
      getQuizzesFromChapters(getAllChapters(), 'Fotografia Digitale');
    }
    return pool;
  }

  function updateProgressIndicators() {
    const pdfKeys = ['foto-tecnica', 'foto-teoria', 'foto-autori', 'foto-maestri'];
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
    
    // Forza materia fotografia
    state.currentSubject = 'fotografia';
    
    // Valida PDF attivo
    const validPdfs = ['foto-tecnica', 'foto-teoria', 'foto-autori', 'foto-maestri'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'foto-tecnica';
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
