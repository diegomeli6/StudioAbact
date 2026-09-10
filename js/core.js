/**
 * Studio ABA Catania — Core Engine
 * Modulo condiviso: stato, localStorage, rendering, esame, tema, utility
 * Caricato da ogni pagina-materia
 */

const StudyCore = (function () {
  'use strict';

  // CHIAVE LOCAL STORAGE
  const STORAGE_KEY = 'ux_web_study_state_v1';

  // STATO APPLICATIVO
  const state = {
    currentSubject: 'web-design',
    activePdf: 'dispense',
    activeChapIndex: 0,
    activeSubtab: 'summary',
    activeView: 'study',
    theme: 'light',
    sidebarOpen: true,
    completed: {},
    flashcardStatus: {},
    quizAnswers: {},
    examSession: null,
    ttsSpeed: 1
  };

  // SVG Icons — sostituzione emoji
  const ICONS = {
    study: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    exam: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>',
    theme: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>',
    save: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>',
    menu: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
    lock: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    home: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    summary: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
    flashcard: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M12 4v16"/></svg>',
    quiz: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    check: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    circle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/></svg>',
    circleFilled: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg>',
    arrowLeft: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>',
    arrowRight: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    anchor: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="3"/><line x1="12" y1="22" x2="12" y2="8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/></svg>',
    pin: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    checkCircle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--accent-success)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    xCircle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--accent-danger)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
    download: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    upload: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>',
    trash: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>',
    thumbsUp: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
    repeat: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>',
    close: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    star: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
  };

  // ── localStorage ──

  function loadLocalState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.currentSubject) state.currentSubject = parsed.currentSubject;
        if (parsed.completed) state.completed = parsed.completed;
        if (parsed.flashcardStatus) state.flashcardStatus = parsed.flashcardStatus;
        if (parsed.quizAnswers) state.quizAnswers = parsed.quizAnswers;
        if (parsed.activePdf) state.activePdf = parsed.activePdf;
        if (typeof parsed.activeChapIndex === 'number') state.activeChapIndex = parsed.activeChapIndex;
        if (parsed.activeView) {
          state.activeView = (parsed.activeView === 'cram' || parsed.activeView === 'glossary') ? 'study' : parsed.activeView;
        }
        if (parsed.theme) state.theme = parsed.theme;
      }

      const globalTheme = localStorage.getItem('aba_studio_theme') || localStorage.getItem('studio_home_theme');
      if (globalTheme) {
        state.theme = globalTheme;
      }

      const savedSpeed = localStorage.getItem('aba_tts_speed');
      if (savedSpeed) {
        const parsed = parseFloat(savedSpeed);
        state.ttsSpeed = (parsed === 1.25) ? 1.25 : 1;
      } else {
        state.ttsSpeed = 1;
      }
    } catch (e) {
      console.warn("Impossibile leggere localStorage:", e);
    }
  }

  function saveLocalState() {
    try {
      const payload = {
        currentSubject: state.currentSubject,
        completed: state.completed,
        flashcardStatus: state.flashcardStatus,
        quizAnswers: state.quizAnswers,
        activePdf: state.activePdf,
        activeChapIndex: state.activeChapIndex,
        activeView: state.activeView,
        theme: state.theme,
        ttsSpeed: state.ttsSpeed
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
      if (typeof updateProgressIndicators === 'function') updateProgressIndicators();
      if (window.AppAuth && typeof window.AppAuth.onStateSaved === 'function') {
        window.AppAuth.onStateSaved(payload);
      }
    } catch (e) {
      console.warn("Impossibile salvare in localStorage:", e);
    }
  }

  // ── Tema ──

  function applyTheme(theme) {
    state.theme = theme;
    if (theme === 'dark') {
      document.body.classList.remove('theme-light');
      document.body.classList.add('theme-dark');
    } else {
      document.body.classList.remove('theme-dark');
      document.body.classList.add('theme-light');
    }
    try {
      localStorage.setItem('aba_studio_theme', theme);
      localStorage.setItem('studio_home_theme', theme);
    } catch (e) {}
  }

  function toggleTheme() {
    const nextTheme = state.theme === 'light' ? 'dark' : 'light';
    applyTheme(nextTheme);
    saveLocalState();
  }

  // ── Vista ──

  function switchView(viewName) {
    stopSpeech();
    state.activeView = viewName;
    document.querySelectorAll('.pill-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.view === viewName);
    });
    document.querySelectorAll('.view-panel').forEach(panel => {
      panel.classList.toggle('active', panel.id === `view-${viewName}`);
    });

    const sidebar = document.getElementById('sidebar');
    const pdfNav = document.getElementById('pdf-selector-nav');
    const sessionBar = document.getElementById('session-bar');
    const viewPills = document.getElementById('header-view-pills');
    const contentArea = document.getElementById('content-area');

    if (viewName === 'hub') {
      if (sidebar) sidebar.style.display = 'none';
      if (pdfNav) pdfNav.style.display = 'none';
      if (sessionBar) sessionBar.style.display = 'none';
      if (viewPills) viewPills.style.opacity = '0.35';
      if (contentArea) contentArea.style.maxWidth = '1050px';
    } else {
      if (sidebar) sidebar.style.display = 'flex';
      if (pdfNav) pdfNav.style.display = 'flex';
      if (sessionBar) sessionBar.style.display = 'flex';
      if (viewPills) viewPills.style.opacity = '1';
      if (contentArea) contentArea.style.maxWidth = '940px';
    }
  }

  function switchSubtab(subtabName) {
    stopSpeech();
    if (subtabName !== 'summary' && subtabName !== 'flashcards' && subtabName !== 'quiz') {
      subtabName = 'summary';
    }
    state.activeSubtab = subtabName;
    document.querySelectorAll('.subtab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.subtab === subtabName);
    });
    document.querySelectorAll('.subtab-panel').forEach(panel => {
      panel.classList.toggle('active', panel.id === `subtab-panel-${subtabName}`);
    });
  }

  // ── Navigazione ──

  function navigateToChapter(idx, getCurrentPdfChapters, renderSidebar, renderCurrentChapter) {
    const chapters = getCurrentPdfChapters();
    if (idx < 0 || idx >= chapters.length) return;

    state.activeChapIndex = idx;
    switchSubtab('summary');
    renderSidebar();
    renderCurrentChapter();
    saveLocalState();
    window.scrollTo({ top: 0, behavior: 'smooth' });

    setTimeout(() => {
      const activeNavEl = document.querySelector('.chapter-nav-item.active');
      if (activeNavEl) {
        activeNavEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }, 60);
  }

  // ── Rendering sidebar ──

  function renderSidebar(getCurrentPdfChapters, onNavigate) {
    const chapters = getCurrentPdfChapters();
    const listEl = document.getElementById('chapter-list');
    const statsEl = document.getElementById('sidebar-stats-count');
    const fillEl = document.getElementById('sidebar-progress-fill');

    if (!listEl) return;
    listEl.innerHTML = '';

    let completedCount = 0;
    let currentPartNum = null;

    chapters.forEach((chap, idx) => {
      const isDone = !!state.completed[chap.id];
      if (isDone) completedCount++;

      if (chap.partNum && chap.partNum !== currentPartNum) {
        currentPartNum = chap.partNum;
        const partHeader = document.createElement('div');
        partHeader.className = 'chapter-part-header';
        partHeader.textContent = chap.partTitle || `Parte ${currentPartNum}`;
        listEl.appendChild(partHeader);
      }

      const item = document.createElement('div');
      item.className = 'chapter-nav-item';
      if (idx === state.activeChapIndex) item.classList.add('active');

      const statusIcon = isDone
        ? `<span class="nav-icon done">${ICONS.checkCircle}</span>`
        : (idx === state.activeChapIndex
          ? `<span class="nav-icon active-dot">${ICONS.circleFilled}</span>`
          : `<span class="nav-icon">${ICONS.circle}</span>`);

      item.innerHTML = `
        <span class="chapter-nav-status">${statusIcon}</span>
        <div class="chapter-nav-info">
          <span class="chapter-nav-num">Capitolo ${chap.number}</span>
          <span class="chapter-nav-title">${escapeHtml(chap.title)}</span>
        </div>
      `;

      item.addEventListener('click', () => {
        onNavigate(idx);
        switchView('study');
      });

      listEl.appendChild(item);
    });

    const percent = chapters.length > 0 ? Math.round((completedCount / chapters.length) * 100) : 0;
    if (statsEl) statsEl.textContent = `${completedCount}/${chapters.length} (${percent}%)`;
    if (fillEl) fillEl.style.width = `${percent}%`;
  }

  // ── Rendering capitolo ──

  function renderCurrentChapter(getCurrentPdfChapters, getPdfDisplayName) {
    stopSpeech();
    const chapters = getCurrentPdfChapters();
    if (chapters.length === 0) return;
    if (state.activeChapIndex >= chapters.length) state.activeChapIndex = 0;
    const chap = chapters[state.activeChapIndex];

    const partBadge = document.getElementById('chap-part-badge');
    const numEl = document.getElementById('chap-number');
    const titleEl = document.getElementById('chap-title');
    const subtitleEl = document.getElementById('chap-subtitle');
    const timeEl = document.getElementById('chap-read-time');

    if (partBadge) {
      if (chap.partTitle) {
        partBadge.textContent = chap.partTitle;
        partBadge.style.display = 'inline-block';
      } else {
        partBadge.style.display = 'none';
      }
    }

    if (numEl) numEl.textContent = `Capitolo ${chap.number}`;
    if (titleEl) titleEl.textContent = chap.title;
    if (subtitleEl) subtitleEl.textContent = chap.subtitle || (chap.anchorTitle ? `Ancora: ${chap.anchorTitle}` : '');
    if (timeEl) timeEl.textContent = `Tempo stimato: ${chap.readTime || '8 min'}`;

    const anchorBox = document.getElementById('anchor-story-box');
    const anchorTitle = document.getElementById('story-anchor-title');
    const anchorText = document.getElementById('story-anchor-text');
    if (anchorBox) {
      if (chap.anchorTitle && chap.anchorText) {
        anchorTitle.textContent = chap.anchorTitle;
        anchorText.textContent = chap.anchorText;
        anchorBox.style.display = 'block';
      } else {
        anchorBox.style.display = 'none';
      }
    }

    const summaryBody = document.getElementById('chap-summary-body');
    if (summaryBody) {
      summaryBody.innerHTML = formatMarkdown(chap.summary || 'Nessuna sintesi disponibile.');
    }

    const keyPointsEl = document.getElementById('chap-key-points');
    if (keyPointsEl) {
      keyPointsEl.innerHTML = '';
      (chap.keyPoints || []).forEach(pt => {
        const li = document.createElement('li');
        li.textContent = pt;
        keyPointsEl.appendChild(li);
      });
    }

    renderFlashcards(chap);
    renderQuiz(chap);

    const isDone = !!state.completed[chap.id];
    updateCompleteButtonState(isDone);

    const prevBtn = document.getElementById('btn-prev-chap');
    const nextBtn = document.getElementById('btn-next-chap');
    if (prevBtn) {
      const isFirst = state.activeChapIndex === 0;
      prevBtn.disabled = isFirst;
      prevBtn.style.opacity = isFirst ? '0.45' : '1';
      prevBtn.style.cursor = isFirst ? 'not-allowed' : 'pointer';
    }
    if (nextBtn) {
      const isLast = state.activeChapIndex >= chapters.length - 1;
      nextBtn.disabled = isLast;
      nextBtn.style.opacity = isLast ? '0.45' : '1';
      nextBtn.style.cursor = isLast ? 'not-allowed' : 'pointer';
    }

    const pdfNameEl = document.getElementById('active-pdf-name');
    if (pdfNameEl) pdfNameEl.textContent = getPdfDisplayName(state.activePdf);
  }

  // ── Flashcards ──

  function renderFlashcards(chap) {
    const listEl = document.getElementById('chap-flashcards-list');
    const countEl = document.getElementById('count-fc');
    const cards = chap.flashcards || [];

    if (countEl) countEl.textContent = cards.length;
    if (!listEl) return;
    listEl.innerHTML = '';

    if (cards.length === 0) {
      listEl.innerHTML = '<p class="text-muted">Nessuna flashcard disponibile per questo capitolo.</p>';
      return;
    }

    cards.forEach((card, idx) => {
      const cardId = `${chap.id}-fc-${idx}`;
      const status = state.flashcardStatus[cardId];

      const cardEl = document.createElement('div');
      cardEl.className = 'flashcard-card';

      cardEl.innerHTML = `
        <div class="flashcard-body" id="fc-body-${cardId}">
          <span class="flashcard-label">Domanda (Clicca per girare)</span>
          <div class="flashcard-content">${escapeHtml(card.question)}</div>
          <div class="flashcard-answer-revealed" style="display: none;" id="fc-ans-${cardId}">
            <span class="flashcard-label" style="color: var(--accent-primary);">Risposta</span>
            <p>${escapeHtml(card.answer)}</p>
          </div>
        </div>
        <div class="flashcard-footer">
          <button class="btn-card-action known ${status === 'known' ? 'active' : ''}" data-act="known" data-id="${cardId}">
            ${ICONS.thumbsUp} Lo so bene
          </button>
          <button class="btn-card-action cram ${status === 'cram' ? 'active' : ''}" data-act="cram" data-id="${cardId}">
            ${ICONS.repeat} Da rivedere
          </button>
        </div>
      `;

      const body = cardEl.querySelector(`#fc-body-${cardId}`);
      const ans = cardEl.querySelector(`#fc-ans-${cardId}`);
      body.addEventListener('click', (e) => {
        if (e.target.closest('.flashcard-footer')) return;
        const isHidden = ans.style.display === 'none';
        ans.style.display = isHidden ? 'block' : 'none';
      });

      cardEl.querySelectorAll('.btn-card-action').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const act = btn.dataset.act;
          const id = btn.dataset.id;
          state.flashcardStatus[id] = act;
          saveLocalState();
          cardEl.querySelectorAll('.btn-card-action').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
        });
      });

      listEl.appendChild(cardEl);
    });
  }

  // ── Quiz ──

  function renderQuiz(chap) {
    const listEl = document.getElementById('chap-quiz-list');
    const quizzes = chap.quiz || [];
    if (!listEl) return;
    listEl.innerHTML = '';

    if (quizzes.length === 0) {
      listEl.innerHTML = '<p class="text-muted">Nessun quiz a scelta multipla per questo capitolo.</p>';
      return;
    }

    quizzes.forEach((q, qIdx) => {
      const quizId = `${chap.id}-quiz-${qIdx}`;
      const savedAns = state.quizAnswers[quizId];

      const qCard = document.createElement('div');
      qCard.className = 'quiz-card';

      const optionsHtml = q.options.map((opt, oIdx) => {
        let extraClass = '';
        if (savedAns) {
          if (oIdx === q.correctIndex) extraClass = 'selected-correct';
          else if (oIdx === savedAns.selectedIndex) extraClass = 'selected-wrong';
        }
        return `
          <button class="quiz-option-btn ${extraClass}" data-quizid="${quizId}" data-oidx="${oIdx}" ${savedAns ? 'disabled' : ''}>
            ${escapeHtml(opt)}
          </button>
        `;
      }).join('');

      const explanationHtml = savedAns ? `
        <div class="quiz-explanation-box">
          <strong>${savedAns.isCorrect ? ICONS.checkCircle + ' Corretto!' : ICONS.xCircle + ' Non corretto.'}</strong> ${escapeHtml(q.explanation || '')}
        </div>
      ` : '';

      qCard.innerHTML = `
        <h4 class="quiz-question-title">${qIdx + 1}. ${escapeHtml(q.question)}</h4>
        <div class="quiz-options">${optionsHtml}</div>
        <div class="quiz-exp-container" id="exp-${quizId}">${explanationHtml}</div>
      `;

      qCard.querySelectorAll('.quiz-option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const oIdx = parseInt(btn.dataset.oidx, 10);
          const isCorrect = oIdx === q.correctIndex;
          state.quizAnswers[quizId] = { selectedIndex: oIdx, isCorrect: isCorrect };
          if (!isCorrect) {
            state.flashcardStatus[`quiz-error-${quizId}`] = 'cram';
          }
          saveLocalState();
          renderQuiz(chap);
        });
      });

      listEl.appendChild(qCard);
    });
  }

  // ── Completamento ──

  function updateCompleteButtonState(isCompleted) {
    const btn = document.getElementById('btn-toggle-complete');
    const icon = document.getElementById('complete-icon');
    const text = document.getElementById('complete-text');
    if (!btn) return;

    if (isCompleted) {
      btn.classList.add('is-completed');
      if (icon) icon.innerHTML = ICONS.checkCircle;
      if (text) text.textContent = 'Capitolo Completato';
    } else {
      btn.classList.remove('is-completed');
      if (icon) icon.innerHTML = ICONS.circle;
      if (text) text.textContent = 'Segna come completato';
    }
  }

  // ── Simulatore esame ──

  function setupExamEvents(getCurrentPdfChapters, getPdfDisplayName, getExamPool) {
    const scopeSelect = document.getElementById('exam-scope-select');
    let chosenCount = 10;

    document.querySelectorAll('.num-pills .num-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.num-pills .num-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        chosenCount = parseInt(btn.dataset.count, 10);
      });
    });

    const startBtn = document.getElementById('btn-start-exam');
    if (startBtn) {
      startBtn.addEventListener('click', () => {
        const scope = scopeSelect ? scopeSelect.value : 'current';
        startExamSession(scope, chosenCount, getCurrentPdfChapters, getPdfDisplayName, getExamPool);
      });
    }

    const abortBtn = document.getElementById('btn-abort-exam');
    if (abortBtn) {
      abortBtn.addEventListener('click', () => {
        state.examSession = null;
        document.getElementById('exam-active-box').style.display = 'none';
        document.getElementById('exam-setup-box').style.display = 'flex';
      });
    }

    const retryBtn = document.getElementById('btn-retry-exam');
    if (retryBtn) {
      retryBtn.addEventListener('click', () => {
        document.getElementById('exam-result-box').style.display = 'none';
        document.getElementById('exam-setup-box').style.display = 'flex';
      });
    }
  }

  function startExamSession(scope, count, getCurrentPdfChapters, getPdfDisplayName, getExamPool) {
    let pool = getExamPool(scope, getCurrentPdfChapters, getPdfDisplayName);

    if (pool.length === 0) {
      alert("Nessun quiz disponibile per questo ambito.");
      return;
    }

    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }

    const rawSelected = pool.slice(0, Math.min(count, pool.length));
    const selectedQuestions = rawSelected.map(q => {
      const opts = q.options.map((opt, idx) => ({
        text: opt,
        isCorrect: idx === q.correctIndex
      }));
      for (let i = opts.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [opts[i], opts[j]] = [opts[j], opts[i]];
      }
      return {
        ...q,
        options: opts.map(o => o.text),
        correctIndex: opts.findIndex(o => o.isCorrect)
      };
    });

    state.examSession = {
      questions: selectedQuestions,
      currentIndex: 0,
      answers: []
    };

    document.getElementById('exam-setup-box').style.display = 'none';
    document.getElementById('exam-result-box').style.display = 'none';
    document.getElementById('exam-active-box').style.display = 'block';

    renderExamQuestion();
  }

  function renderExamQuestion() {
    const session = state.examSession;
    if (!session) return;

    const counterEl = document.getElementById('exam-question-counter');
    const container = document.getElementById('exam-card-container');
    if (!container) return;

    const q = session.questions[session.currentIndex];
    counterEl.textContent = `Domanda ${session.currentIndex + 1} di ${session.questions.length} (${q.sourceName})`;

    container.innerHTML = `
      <div class="quiz-card" style="margin-top: 14px;">
        <div style="font-size: 11px; color: var(--text-muted); font-weight: 700; margin-bottom: 6px;">
          ${q.sourceName} - Capitolo ${q.chapNum}: ${escapeHtml(q.chapTitle)}
        </div>
        <h3 class="quiz-question-title" style="font-size: 17px;">${escapeHtml(q.question)}</h3>
        <div class="quiz-options">
          ${q.options.map((opt, idx) => `
            <button class="quiz-option-btn" data-idx="${idx}">${escapeHtml(opt)}</button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.quiz-option-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const selectedIdx = parseInt(btn.dataset.idx, 10);
        const isCorrect = selectedIdx === q.correctIndex;

        session.answers.push({
          question: q.question,
          selectedIdx: selectedIdx,
          correctIndex: q.correctIndex,
          isCorrect: isCorrect,
          explanation: q.explanation,
          options: q.options
        });

        session.currentIndex++;
        if (session.currentIndex < session.questions.length) {
          renderExamQuestion();
        } else {
          finishExamSession();
        }
      });
    });
  }

  function finishExamSession() {
    const session = state.examSession;
    if (!session) return;

    document.getElementById('exam-active-box').style.display = 'none';
    const resultBox = document.getElementById('exam-result-box');
    resultBox.style.display = 'block';

    const correctCount = session.answers.filter(a => a.isCorrect).length;
    const total = session.answers.length;
    const scorePct = Math.round((correctCount / total) * 100);

    const titleEl = document.getElementById('exam-score-title');
    const feedbackEl = document.getElementById('exam-score-feedback');
    const reviewList = document.getElementById('exam-review-list');

    titleEl.textContent = `Punteggio Finale: ${correctCount} / ${total} (${scorePct}%)`;

    if (scorePct >= 80) {
      feedbackEl.innerHTML = `${ICONS.star} Ottima preparazione! Hai dimostrato una comprensione solida dei concetti.`;
    } else if (scorePct >= 60) {
      feedbackEl.innerHTML = `${ICONS.thumbsUp} Buono, ma ci sono alcuni punti da rifinire nei capitoli corrispondenti.`;
    } else {
      feedbackEl.innerHTML = `${ICONS.repeat} Ti consigliamo di ripassare i capitoli con la modalità guidata e le flashcard.`;
    }

    reviewList.innerHTML = '';
    session.answers.forEach((ans, idx) => {
      const item = document.createElement('div');
      item.className = 'cram-item-card';
      item.style.borderLeftColor = ans.isCorrect ? 'var(--accent-success)' : 'var(--accent-danger)';
      item.style.marginTop = '12px';

      item.innerHTML = `
        <div style="font-weight: 700; font-size: 12px; margin-bottom: 4px;">
          ${ans.isCorrect ? ICONS.checkCircle + ' Risposta Corretta' : ICONS.xCircle + ' Errore'} (Domanda ${idx + 1})
        </div>
        <p style="font-weight: 600; margin-bottom: 8px;">${escapeHtml(ans.question)}</p>
        <p style="font-size: 13px; color: var(--text-muted);">Tua risposta: <strong>${escapeHtml(ans.options[ans.selectedIdx])}</strong></p>
        ${!ans.isCorrect ? `<p style="font-size: 13px; color: var(--accent-success);">Risposta esatta: <strong>${escapeHtml(ans.options[ans.correctIndex])}</strong></p>` : ''}
        <div class="cram-answer" style="margin-top: 8px;">${escapeHtml(ans.explanation || '')}</div>
      `;
      reviewList.appendChild(item);
    });

    state.examSession = null;
  }



  // ── Utility: Markdown parser ──

  function formatMarkdown(text) {
    if (!text) return '';
    let html = escapeHtml(text);

    // Tables
    html = html.replace(/((?:\|[^\n]+\|\r?\n)+)/g, function (tableBlock) {
      const rows = tableBlock.trim().split(/\r?\n/).filter(r => r.trim());
      if (rows.length < 2) return tableBlock;
      let tableHtml = '<div class="table-responsive"><table class="academic-table">';
      rows.forEach((row, rIdx) => {
        if (row.match(/^\|(?:\s*:?-+:?\s*\|)+$/)) return;
        const cells = row.split('|').slice(1, -1);
        if (rIdx === 0) {
          tableHtml += '<thead><tr>';
          cells.forEach(c => { tableHtml += `<th>${c.trim()}</th>`; });
          tableHtml += '</tr></thead><tbody>';
        } else {
          tableHtml += '<tr>';
          cells.forEach(c => { tableHtml += `<td>${c.trim()}</td>`; });
          tableHtml += '</tr>';
        }
      });
      tableHtml += '</tbody></table></div>';
      return tableHtml;
    });

    html = html.replace(/^#### (.*?)$/gm, '<h4>$1</h4>');
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
    html = html.replace(/^---$/gm, '<hr class="summary-divider">');
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/```(html|css|js|)([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');

    html = html.replace(/((?:^(?:&gt;|>)[ \t]?[^\n]*(?:\r?\n|$))+)/gm, function (block) {
      const lines = block.trim().split(/\r?\n/).map(l => l.replace(/^(?:&gt;|>)[ \t]?/, '').trim()).filter(Boolean);
      return '\n\n<blockquote class="summary-quote">' + lines.join('<br>') + '</blockquote>\n\n';
    });

    html = html.replace(/^[•\-\*] (.*?)$/gm, '<li>$1</li>');
    html = html.replace(/!\[(.*?)\]\((.*?)\)/g, function (match, alt, src) {
      let resolvedSrc = (src || '').trim();
      const inPagesSubdir = window.location.pathname.includes('/pages/') || 
                            document.querySelector('link[href*="../styles.css"]') !== null;
      if (inPagesSubdir) {
        if (!resolvedSrc.startsWith('http') && !resolvedSrc.startsWith('/') && !resolvedSrc.startsWith('../') && !resolvedSrc.startsWith('data:')) {
          resolvedSrc = '../' + resolvedSrc;
        }
      } else {
        if (resolvedSrc.startsWith('../assets/')) {
          resolvedSrc = resolvedSrc.replace(/^\.\.\//, '');
        }
      }
      return `<figure class="artwork-figure"><img src="${resolvedSrc}" alt="${escapeHtml(alt)}" class="artwork-img" loading="lazy" onerror="this.classList.add('img-load-error')"><figcaption class="artwork-caption">${alt}</figcaption></figure>`;
    });

    html = html.split('\n\n').map(p => {
      p = p.trim();
      if (!p) return '';
      if (!p.startsWith('<h') && !p.startsWith('<ul') && !p.startsWith('<pre') && !p.startsWith('<div') && !p.startsWith('<hr') && !p.startsWith('<blockquote') && !p.startsWith('<figure')) {
        return `<p>${p.replace(/\n/g, '<br>')}</p>`;
      }
      return p;
    }).filter(Boolean).join('\n');

    return html;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // ── Modulo Lettura Vocale Sintesi (Text-To-Speech) ──
  const ttsState = {
    isSpeaking: false,
    isPaused: false,
    chunks: [],
    chunkIndex: 0,
    currentChapter: null
  };

  // Riferimento globale per evitare la distruzione premature da Garbage Collection in V8
  window._activeTtsUtterance = null;

  function stripMarkdownForSpeech(md) {
    if (!md) return '';
    return md
      .replace(/```[\s\S]*?```/g, '') // rimuovi blocchi codice
      .replace(/`([^`]+)`/g, '$1') // inline code
      .replace(/!\[.*?\]\(.*?\)/g, '') // immagini
      .replace(/\[(.*?)\]\(.*?\)/g, '$1') // link
      .replace(/<[^>]+>/g, '') // html tag
      .replace(/#{1,6}\s*(.*)/g, '$1.') // intestazioni con punto
      .replace(/(\*\*|__)(.*?)\1/g, '$2') // grassetto
      .replace(/(\*|_)(.*?)\1/g, '$2') // corsivo
      .replace(/^\s*[-*+]\s+/gm, '') // liste
      .replace(/^\s*\d+\.\s+/gm, '') // elenchi numerati
      .replace(/^>\s*/gm, '') // citazioni
      .replace(/---+/g, '') // separatori
      .replace(/\n\s*\n/g, '. ') // newline doppie
      .replace(/\n/g, ' ') // newline singole
      .replace(/\s+/g, ' ') // spazi multipli
      .trim();
  }

  // Suddivide il testo in frasi/spezzoni non superiori a ~160 caratteri
  // per prevenire il freeze/silenzio dell'engine vocale di Chrome/Safari su macOS
  function splitIntoSpeechChunks(text, maxLen = 160) {
    if (!text) return [];
    const rawSentences = text.split(/(?<=[.!?;\n])\s+/);
    const chunks = [];

    rawSentences.forEach(sentence => {
      const trimmed = sentence.trim();
      if (!trimmed) return;

      if (trimmed.length <= maxLen) {
        chunks.push(trimmed);
      } else {
        const subParts = trimmed.split(/(?<=[,:])\s+/);
        let current = '';

        subParts.forEach(part => {
          if ((current + ' ' + part).trim().length <= maxLen) {
            current = (current + ' ' + part).trim();
          } else {
            if (current) chunks.push(current);
            if (part.length > maxLen) {
              const words = part.split(/\s+/);
              let wCurrent = '';
              words.forEach(w => {
                if ((wCurrent + ' ' + w).trim().length <= maxLen) {
                  wCurrent = (wCurrent + ' ' + w).trim();
                } else {
                  if (wCurrent) chunks.push(wCurrent);
                  wCurrent = w;
                }
              });
              if (wCurrent) chunks.push(wCurrent);
              current = '';
            } else {
              current = part;
            }
          }
        });
        if (current) chunks.push(current);
      }
    });

    return chunks.filter(c => c.length > 0);
  }

  function stopSpeech() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    window._activeTtsUtterance = null;
    ttsState.isSpeaking = false;
    ttsState.isPaused = false;
    ttsState.chunks = [];
    ttsState.chunkIndex = 0;
    ttsState.currentChapter = null;
    updateAudioBarUI('idle');
  }

  function updateAudioBarUI(status, snippet = '') {
    const playIcon = document.getElementById('audio-icon-play');
    const pauseIcon = document.getElementById('audio-icon-pause');
    const label = document.getElementById('audio-btn-label');
    const stopBtn = document.getElementById('btn-audio-stop');
    const visualizer = document.getElementById('audio-visualizer');
    const statusLabel = document.getElementById('audio-status-label');
    const bar = document.getElementById('summary-audio-bar');

    if (!bar) return;

    if (status === 'playing') {
      if (playIcon) playIcon.style.display = 'none';
      if (pauseIcon) pauseIcon.style.display = 'inline-flex';
      if (label) label.textContent = 'Pausa';
      if (stopBtn) stopBtn.style.display = 'inline-flex';
      if (visualizer) visualizer.style.display = 'flex';
      if (statusLabel) {
        if (snippet) {
          const short = snippet.length > 50 ? snippet.slice(0, 48) + '...' : snippet;
          statusLabel.textContent = `Lettura: "${short}"`;
          statusLabel.title = snippet;
        } else {
          statusLabel.textContent = 'Riproduzione in corso...';
        }
      }
      bar.classList.add('is-playing');
    } else if (status === 'paused') {
      if (playIcon) playIcon.style.display = 'inline-flex';
      if (pauseIcon) pauseIcon.style.display = 'none';
      if (label) label.textContent = 'Riprendi';
      if (stopBtn) stopBtn.style.display = 'inline-flex';
      if (visualizer) visualizer.style.display = 'none';
      if (statusLabel) statusLabel.textContent = 'In pausa';
      bar.classList.add('is-playing');
    } else {
      // idle
      if (playIcon) playIcon.style.display = 'inline-flex';
      if (pauseIcon) pauseIcon.style.display = 'none';
      if (label) label.textContent = 'Ascolta Sintesi';
      if (stopBtn) stopBtn.style.display = 'none';
      if (visualizer) visualizer.style.display = 'none';
      if (statusLabel) {
        statusLabel.textContent = 'Lettore vocale pronto';
        statusLabel.title = '';
      }
      bar.classList.remove('is-playing');
    }
  }

  function getItalianVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices() || [];
    
    // Esclusivamente Google italiano (voce neurale di alta qualità e intonazione naturale)
    let voice = voices.find(v => v.lang && (v.lang === 'it-IT' || v.lang === 'it_IT') && v.name.toLowerCase().includes('google'));
    
    // Fallback trasparente per browser non-Chromium (Safari/Firefox)
    if (!voice) {
      voice = voices.find(v => v.lang && (v.lang.startsWith('it') || v.lang.includes('IT')) && (v.name.includes('Natural') || v.name.includes('Neural') || v.name.includes('Siri') || v.name.includes('Enhanced') || v.name.includes('Migliorata')));
    }
    if (!voice) {
      voice = voices.find(v => v.lang && (v.lang === 'it-IT' || v.lang === 'it_IT') && !v.name.includes('Compact'));
    }
    if (!voice) {
      voice = voices.find(v => v.lang && (v.lang.startsWith('it') || v.lang.includes('IT')));
    }
    return voice || null;
  }

  function speakNextChunk() {
    if (!ttsState.isSpeaking || ttsState.isPaused) return;

    if (ttsState.chunkIndex >= ttsState.chunks.length) {
      stopSpeech();
      return;
    }

    const chunkText = ttsState.chunks[ttsState.chunkIndex];
    if (!chunkText || !chunkText.trim()) {
      ttsState.chunkIndex++;
      speakNextChunk();
      return;
    }

    updateAudioBarUI('playing', chunkText);

    try {
      const utterance = new SpeechSynthesisUtterance(chunkText);
      utterance.lang = 'it-IT';
      utterance.rate = state.ttsSpeed || 1.0;
      utterance.pitch = 1.0;

      const voice = getItalianVoice();
      if (voice) utterance.voice = voice;

      utterance.onend = () => {
        if (!ttsState.isSpeaking || ttsState.isPaused) return;
        ttsState.chunkIndex++;
        setTimeout(speakNextChunk, 70);
      };

      utterance.onerror = (e) => {
        console.warn('TTS chunk avanza per errore/skip:', e);
        if (!ttsState.isSpeaking || ttsState.isPaused) return;
        ttsState.chunkIndex++;
        setTimeout(speakNextChunk, 70);
      };

      window._activeTtsUtterance = utterance;

      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }

      window.speechSynthesis.speak(utterance);
    } catch (err) {
      console.error('Errore riproduzione vocale chunk:', err);
      stopSpeech();
    }
  }

  function toggleSpeech(currentChapter) {
    if (!('speechSynthesis' in window)) {
      alert('La sintesi vocale non è supportata dal tuo browser.');
      return;
    }

    if (ttsState.isSpeaking && ttsState.currentChapter === currentChapter) {
      if (ttsState.isPaused) {
        ttsState.isPaused = false;
        speakNextChunk();
      } else {
        ttsState.isPaused = true;
        window.speechSynthesis.cancel();
        updateAudioBarUI('paused');
      }
      return;
    }

    stopSpeech();

    if (!currentChapter) return;

    let textParts = [];
    if (currentChapter.title) {
      textParts.push(currentChapter.title);
    }
    if (currentChapter.anchorText) {
      textParts.push(`Storia àncora mnemonica: ${currentChapter.anchorTitle || ''}. ${currentChapter.anchorText}`);
    }
    if (currentChapter.summary) {
      textParts.push(currentChapter.summary);
    }

    const clean = stripMarkdownForSpeech(textParts.join('. '));
    const chunks = splitIntoSpeechChunks(clean);

    if (!chunks || chunks.length === 0) {
      alert('Nessun testo da leggere in questo capitolo.');
      return;
    }

    ttsState.isSpeaking = true;
    ttsState.isPaused = false;
    ttsState.chunks = chunks;
    ttsState.chunkIndex = 0;
    ttsState.currentChapter = currentChapter;

    if (window.speechSynthesis.getVoices().length === 0) {
      window.speechSynthesis.onvoiceschanged = () => {
        speakNextChunk();
      };
      setTimeout(() => {
        if (ttsState.isSpeaking && !window.speechSynthesis.speaking) {
          speakNextChunk();
        }
      }, 250);
    } else {
      speakNextChunk();
    }
  }

  // ── Setup base per event listener condivisi ──

  function setupCoreEvents(getCurrentPdfChapters, renderSidebarFn, renderCurrentChapterFn, navigateFn) {
    // Audio Player TTS
    const audioPlayBtn = document.getElementById('btn-audio-listen');
    const audioStopBtn = document.getElementById('btn-audio-stop');

    // Multiplicatori di velocità (1x, 1.25x)
    function updateSpeedPillsUI(speed) {
      const normalized = (speed === 1.25) ? 1.25 : 1;
      document.querySelectorAll('.speed-pill').forEach(pill => {
        pill.classList.toggle('active', parseFloat(pill.dataset.speed) === normalized);
      });
    }

    updateSpeedPillsUI(state.ttsSpeed || 1);

    document.querySelectorAll('.speed-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        const speed = parseFloat(pill.dataset.speed);
        state.ttsSpeed = (speed === 1.25) ? 1.25 : 1;
        localStorage.setItem('aba_tts_speed', state.ttsSpeed.toString());
        updateSpeedPillsUI(state.ttsSpeed);

        if (ttsState.isSpeaking && !ttsState.isPaused) {
          window.speechSynthesis.cancel();
          speakNextChunk();
        }
      });
    });

    if (audioPlayBtn) {
      audioPlayBtn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        const currentChap = chaps[state.activeChapIndex];
        if (currentChap) toggleSpeech(currentChap);
      });
    }
    if (audioStopBtn) {
      audioStopBtn.addEventListener('click', stopSpeech);
    }
    window.addEventListener('beforeunload', stopSpeech);

    // Theme toggle
    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) themeBtn.addEventListener('click', toggleTheme);

    // Sincronizzazione tema globale in tempo reale fra schede/pagine
    window.addEventListener('storage', (e) => {
      if ((e.key === 'aba_studio_theme' || e.key === 'studio_home_theme') && e.newValue) {
        if (e.newValue !== state.theme) {
          applyTheme(e.newValue);
        }
      }
    });

    // Sidebar toggle
    const sidebarToggleBtn = document.getElementById('btn-sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    if (sidebarToggleBtn && sidebar) {
      sidebarToggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
      });
    }



    // View pills
    document.querySelectorAll('.pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        switchView(btn.dataset.view);
      });
    });

    // Subtabs
    document.querySelectorAll('.subtab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        switchSubtab(btn.dataset.subtab);
      });
    });

    // PDF tabs — Cambio dispensa: va a vista Studio, sottoscheda Sintesi e primo capitolo non completato
    document.querySelectorAll('.pdf-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const pdfKey = tab.dataset.pdf;
        if (pdfKey !== state.activePdf) {
          stopSpeech();
          state.activePdf = pdfKey;
          
          document.querySelectorAll('.pdf-tab').forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          // Passa sempre a vista Studio e sottoscheda Sintesi
          switchView('study');
          switchSubtab('summary');

          // Trova il primo capitolo non completato della nuova dispensa
          const chapters = getCurrentPdfChapters();
          let targetIdx = chapters.findIndex(c => !state.completed[c.id]);
          if (targetIdx === -1) {
            targetIdx = 0; // Se tutti sono completati, riparte dal primo capitolo
          }
          state.activeChapIndex = targetIdx;

          renderSidebarFn();
          renderCurrentChapterFn();
          saveLocalState();
          window.scrollTo({ top: 0, behavior: 'smooth' });

          setTimeout(() => {
            const activeNavEl = document.querySelector('.chapter-nav-item.active');
            if (activeNavEl) {
              activeNavEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
            }
          }, 80);
        }
      });
    });

    // Chapter navigation
    const prevBtn = document.getElementById('btn-prev-chap');
    const nextBtn = document.getElementById('btn-next-chap');
    const completeBtn = document.getElementById('btn-toggle-complete');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.activeChapIndex > 0) navigateFn(state.activeChapIndex - 1);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        const currentChap = chaps[state.activeChapIndex];
        if (currentChap) {
          state.completed[currentChap.id] = true;
          saveLocalState();
        }
        if (state.activeChapIndex < chaps.length - 1) {
          navigateFn(state.activeChapIndex + 1);
        } else {
          updateCompleteButtonState(true);
          renderSidebarFn();
        }
      });
    }

    if (completeBtn) {
      completeBtn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        const currentChap = chaps[state.activeChapIndex];
        if (currentChap) {
          const isCurrentlyDone = !!state.completed[currentChap.id];
          state.completed[currentChap.id] = !isCurrentlyDone;
          updateCompleteButtonState(!isCurrentlyDone);
          saveLocalState();
          renderSidebarFn();
        }
      });
    }

    // Home button
    const homeBtn = document.getElementById('btn-hub-nav');
    if (homeBtn) {
      homeBtn.addEventListener('click', () => {
        window.location.href = homeBtn.dataset.href || '../index.html';
      });
    }

    // Lightbox modal per le opere d'arte
    document.addEventListener('click', (e) => {
      const img = e.target.closest('.artwork-img');
      if (!img) return;
      let lightbox = document.getElementById('artwork-lightbox-modal');
      if (!lightbox) {
        lightbox = document.createElement('div');
        lightbox.id = 'artwork-lightbox-modal';
        lightbox.className = 'artwork-lightbox-overlay';
        lightbox.innerHTML = `
          <div class="artwork-lightbox-content">
            <button class="artwork-lightbox-close" aria-label="Chiudi ingrandimento">&times;</button>
            <img class="artwork-lightbox-img" src="" alt="">
            <div class="artwork-lightbox-caption"></div>
          </div>
        `;
        document.body.appendChild(lightbox);
        lightbox.addEventListener('click', (evt) => {
          if (evt.target === lightbox || evt.target.closest('.artwork-lightbox-close')) {
            lightbox.classList.remove('active');
          }
        });
        document.addEventListener('keydown', (evt) => {
          if (evt.key === 'Escape' && lightbox.classList.contains('active')) {
            lightbox.classList.remove('active');
          }
        });
      }
      const fig = img.closest('.artwork-figure');
      const caption = fig ? fig.querySelector('.artwork-caption') : null;
      const lbImg = lightbox.querySelector('.artwork-lightbox-img');
      const lbCap = lightbox.querySelector('.artwork-lightbox-caption');
      lbImg.src = img.src;
      lbImg.alt = img.alt || '';
      lbCap.innerHTML = caption ? caption.innerHTML : (img.alt || '');
      lightbox.classList.add('active');
    });
  }

  // ── Public API ──

  return {
    state,
    ICONS,
    loadLocalState,
    saveLocalState,
    applyTheme,
    toggleTheme,
    switchView,
    switchSubtab,
    navigateToChapter,
    renderSidebar,
    renderCurrentChapter,
    renderFlashcards,
    renderQuiz,
    updateCompleteButtonState,
    setupExamEvents,
    setupCoreEvents,
    formatMarkdown,
    escapeHtml,
    stopSpeech,
    toggleSpeech
  };
})();
