/**
 * Logica di pagina generica per ogni materia.
 * Legge la configurazione da window.SUBJECTS (js/subjects.js) in base a <body data-subject>.
 * Dipende da: js/subjects.js, js/core.js, file dati della materia.
 */
(function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;
  const registry = window.SubjectRegistry;
  const subjectId = document.body.dataset.subject;
  const subject = registry.SUBJECTS[subjectId];
  if (!subject) return;

  const modulesByKey = {};
  subject.modules.forEach(m => { modulesByKey[m.key] = m; });

  function getCurrentPdfChapters() {
    const mod = modulesByKey[state.activePdf] || subject.modules[0];
    return registry.getModuleChapters(mod);
  }

  function getPdfDisplayName(key) {
    const mod = modulesByKey[key];
    return mod ? mod.label : key;
  }

  function getExamPool(scope) {
    const pool = [];
    const addChapters = (chapters, sourceName) => {
      chapters.forEach(chap => {
        const list = (chap.examQuiz && chap.examQuiz.length > 0) ? chap.examQuiz : (chap.quiz || []);
        list.forEach(q => pool.push({ ...q, sourceName, chapNum: chap.number, chapTitle: chap.title }));
      });
    };

    const extra = (subject.extraScopes || []).find(s => s.value === scope);
    if (extra) {
      extra.modules.forEach(key => {
        addChapters(registry.getModuleChapters(modulesByKey[key]).filter(extra.filter), extra.label);
      });
    } else if (scope === 'current') {
      addChapters(getCurrentPdfChapters(), getPdfDisplayName(state.activePdf));
    } else {
      subject.modules.forEach(mod => addChapters(registry.getModuleChapters(mod), mod.label));
    }
    return pool;
  }

  function updateProgressIndicators() {
    subject.modules.forEach(mod => {
      const chaps = registry.getModuleChapters(mod);
      const done = chaps.filter(c => state.completed[c.id]).length;

      const badge = document.getElementById(`prog-mini-${mod.key}`);
      if (badge) badge.textContent = `${done}/${chaps.length}`;

      if (mod.key === state.activePdf) {
        const pct = chaps.length > 0 ? Math.round((done / chaps.length) * 100) : 0;
        const barText = document.getElementById('active-pdf-progress-text');
        if (barText) barText.textContent = `${done} di ${chaps.length} capitoli completati`;
        const barFill = document.getElementById('session-progress-fill');
        if (barFill) barFill.style.width = `${pct}%`;
      }
    });
  }

  function doRenderSidebar() {
    core.renderSidebar(getCurrentPdfChapters, doNavigate);
  }

  function doRenderChapter() {
    core.renderCurrentChapter(getCurrentPdfChapters, getPdfDisplayName);
  }

  function doNavigate(idx) {
    core.navigateToChapter(idx, getCurrentPdfChapters, doRenderSidebar, doRenderChapter);
  }

  // Porta a un capitolo di qualunque modulo (usato dai Progressi)
  function navigateTo(moduleKey, idx) {
    if (!modulesByKey[moduleKey]) return;
    state.activePdf = moduleKey;
    document.querySelectorAll('.pdf-tab').forEach(t => t.classList.toggle('active', t.dataset.pdf === moduleKey));
    core.switchView('study');
    doNavigate(idx);
    updateProgressIndicators();
  }

  function getModules() {
    return subject.modules.map(m => ({ key: m.key, label: m.label, chapters: registry.getModuleChapters(m) }));
  }

  // Esposti per core.js (saveLocalState) e auth.js (refresh dopo sync cloud)
  window.updateProgressIndicators = updateProgressIndicators;
  window.doRenderSidebar = doRenderSidebar;
  window.doRenderChapter = doRenderChapter;
  window.getCurrentPdfChapters = getCurrentPdfChapters;

  function init() {
    core.loadLocalState(subjectId);

    if (!modulesByKey[state.activePdf]) {
      state.activePdf = subject.modules[0].key;
      state.activeChapIndex = 0;
    }

    core.applyTheme(state.theme);

    document.querySelectorAll('.pdf-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.pdf === state.activePdf);
    });

    core.setupCoreEvents(getCurrentPdfChapters, doRenderSidebar, doRenderChapter, doNavigate);
    core.setupExamEvents(getCurrentPdfChapters, getPdfDisplayName, getExamPool);

    if (typeof StudyPractice !== 'undefined') {
      StudyPractice.init({ subject, getModules, getCurrentPdfChapters, navigateTo });
    }

    core.switchView(state.activeView || 'study');
    doRenderSidebar();
    doRenderChapter();
    updateProgressIndicators();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
