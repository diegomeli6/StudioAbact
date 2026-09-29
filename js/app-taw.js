/**
 * App Tecniche Audiovisive per il Web — Logica specifica per la materia
 * Dipende da: js/core.js, data/taw-data.js
 * Docente: Prof. Lorenzo Di Silvestro (ABTEC 42 - 8 CFA)
 * Accademia di Belle Arti di Catania
 * DIVIETO ASSOLUTO DI EMOJI
 */

(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;

  function getAllChapters() {
    if (window.TAW_DATA && Array.isArray(window.TAW_DATA.chapters)) {
      return window.TAW_DATA.chapters;
    }
    if (window.TAW_CHAPTERS) {
      return window.TAW_CHAPTERS;
    }
    if (Array.isArray(window.TAW_DATA)) {
      return window.TAW_DATA;
    }
    return [];
  }

  function getCurrentPdfChapters() {
    const all = getAllChapters();
    if (state.activePdf === 'taw-camera-linguaggio') return all.filter(c => c.module === 'taw-camera-linguaggio');
    if (state.activePdf === 'taw-movimenti-montaggio') return all.filter(c => c.module === 'taw-movimenti-montaggio');
    if (state.activePdf === 'taw-drammaturgia-produzione') return all.filter(c => c.module === 'taw-drammaturgia-produzione');
    if (state.activePdf === 'taw-post-web') return all.filter(c => c.module === 'taw-post-web');
    return all.filter(c => c.module === 'taw-camera-linguaggio');
  }

  function getPdfDisplayName(key) {
    if (key === 'taw-camera-linguaggio') return '1. Fotocamera & Linguaggio';
    if (key === 'taw-movimenti-montaggio') return '2. Dinamica & Montaggio';
    if (key === 'taw-drammaturgia-produzione') return '3. Sceneggiatura & Produzione';
    if (key === 'taw-post-web') return '4. Post-Produzione & Web';
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
      getQuizzesFromChapters(getAllChapters(), 'Tecniche Audiovisive per il Web');
    }
    return pool;
  }

  function updateProgressIndicators() {
    const pdfKeys = ['taw-camera-linguaggio', 'taw-movimenti-montaggio', 'taw-drammaturgia-produzione', 'taw-post-web'];
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
    state.currentSubject = 'taw';
    
    // Valida PDF attivo
    const validPdfs = ['taw-camera-linguaggio', 'taw-movimenti-montaggio', 'taw-drammaturgia-produzione', 'taw-post-web'];
    if (!validPdfs.includes(state.activePdf)) {
      state.activePdf = 'taw-camera-linguaggio';
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
