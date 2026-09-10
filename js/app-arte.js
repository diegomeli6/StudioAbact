/**
 * App Storia dell'Arte Contemporanea — Logica specifica per la materia
 * Dipende da: js/core.js, data/arte-data.js
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getCurrentPdfChapters() {
    const allArte = window.ARTE_DATA || [];
    if (state.activePdf === 'arte-anni80') return allArte.filter(c => c.module === 'anni80');
    if (state.activePdf === 'arte-anni90') return allArte.filter(c => c.module === 'anni90');
    if (state.activePdf === 'arte-duemila') return allArte.filter(c => c.module === 'duemila');
    if (state.activePdf === 'arte-monografie') return allArte.filter(c => c.module === 'monografie');
    // Fallback per sotto-moduli monografie
    if (state.activePdf === 'arte-hirst') return allArte.filter(c => c.module === 'monografie' && c.id.includes('hirst'));
    if (state.activePdf === 'arte-eliasson') return allArte.filter(c => c.module === 'monografie' && c.id.includes('eliasson'));
    if (state.activePdf === 'arte-chevalier') return allArte.filter(c => c.module === 'monografie' && c.id.includes('chevalier'));
    return allArte.filter(c => c.module === 'anni80');
  }

  function getPdfDisplayName(key) {
    if (key === 'arte-anni80') return "1. Arte Contemporanea Anni '80";
    if (key === 'arte-anni90') return "2. Arte Contemporanea Anni '90";
    if (key === 'arte-duemila') return '3. Anni Duemila — Il Secolo a Uncinetto';
    if (key === 'arte-monografie') return '4. Monografie & Artisti Guida';
    if (key === 'arte-hirst') return 'Damien Hirst & Young British Artists';
    if (key === 'arte-eliasson') return 'Olafur Eliasson — Luce e Spazio';
    if (key === 'arte-chevalier') return 'Miguel Chevalier — Pixel e IA';
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
      getQuizzesFromChapters(window.ARTE_DATA || [], "Storia dell'Arte Contemporanea");
    }
    return pool;
  }

  function updateProgressIndicators() {
    const artePdfs = ['arte-anni80', 'arte-anni90', 'arte-duemila', 'arte-monografie'];
    const allArte = window.ARTE_DATA || [];
    artePdfs.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'arte-anni80') chaps = allArte.filter(c => c.module === 'anni80');
      if (pdfKey === 'arte-anni90') chaps = allArte.filter(c => c.module === 'anni90');
      if (pdfKey === 'arte-duemila') chaps = allArte.filter(c => c.module === 'duemila');
      if (pdfKey === 'arte-monografie') chaps = allArte.filter(c => c.module === 'monografie');

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
    
    // Forza materia arte
    state.currentSubject = 'arte';
    
    // Valida PDF attivo
    const validPdfs = ['arte-anni80', 'arte-anni90', 'arte-duemila', 'arte-monografie', 'arte-hirst', 'arte-eliasson', 'arte-chevalier'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'arte-anni80';
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
