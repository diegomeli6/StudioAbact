/**
 * Studio UX & Web Design - Logic & State Engine
 * 100% Client-side, privacy-focused with localStorage persistence
 */

(function () {
  'use strict';

  // CHIAVE LOCAL STORAGE
  const STORAGE_KEY = 'ux_web_study_state_v1';

  // STATO APPLICATIVO
  const state = {
    currentSubject: 'web-design', // 'web-design' | 'hub'
    activePdf: 'dispense', // 'dispense' | 'krug' | 'stull' | 'cards'
    activeChapIndex: 0,
    activeSubtab: 'summary', // 'summary' | 'flashcards' | 'quiz' | 'open' | 'notes'
    activeView: 'study', // 'hub' | 'study' | 'cram' | 'exam' | 'glossary'
    theme: 'light',
    sidebarOpen: true,
    
    // Progressi salvati
    completed: {}, // id: boolean
    flashcardStatus: {}, // id: 'known' | 'cram'
    quizAnswers: {}, // quizId: { selectedIndex, isCorrect }
    openStatus: {}, // openId: 'known' | 'cram'
    notes: {}, // chapId: string
    
    // Sessione esame
    examSession: null
  };

  // Caricamento dati iniziali da localStorage
  function loadLocalState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.currentSubject) state.currentSubject = parsed.currentSubject;
        if (parsed.completed) state.completed = parsed.completed;
        if (parsed.flashcardStatus) state.flashcardStatus = parsed.flashcardStatus;
        if (parsed.quizAnswers) state.quizAnswers = parsed.quizAnswers;
        if (parsed.openStatus) state.openStatus = parsed.openStatus;
        if (parsed.notes) state.notes = parsed.notes;
        if (parsed.activePdf) state.activePdf = parsed.activePdf;
        if (typeof parsed.activeChapIndex === 'number') state.activeChapIndex = parsed.activeChapIndex;
        if (parsed.activeView) state.activeView = parsed.activeView;
        if (parsed.theme) state.theme = parsed.theme;
      }
    } catch (e) {
      console.warn("Impossibile leggere localStorage:", e);
    }
  }

  // Salvataggio permanente in localStorage
  function saveLocalState() {
    try {
      const payload = {
        currentSubject: state.currentSubject,
        completed: state.completed,
        flashcardStatus: state.flashcardStatus,
        quizAnswers: state.quizAnswers,
        openStatus: state.openStatus,
        notes: state.notes,
        activePdf: state.activePdf,
        activeChapIndex: state.activeChapIndex,
        activeView: state.activeView,
        theme: state.theme
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
      updateProgressIndicators();
      updateCramCounter();
    } catch (e) {
      console.warn("Impossibile salvare in localStorage:", e);
    }
  }

  // Recupera la lista capitoli per il PDF/Modulo corrente
  function getCurrentPdfChapters() {
    if (state.currentSubject === 'arte' || (state.activePdf && state.activePdf.startsWith('arte-'))) {
      const allArte = window.ARTE_DATA || [];
      if (state.activePdf === 'arte-anni80') return allArte.filter(c => c.module === 'anni80');
      if (state.activePdf === 'arte-hirst') return allArte.filter(c => c.module === 'hirst');
      if (state.activePdf === 'arte-eliasson') return allArte.filter(c => c.module === 'eliasson');
      if (state.activePdf === 'arte-chevalier') return allArte.filter(c => c.module === 'chevalier');
      return allArte.filter(c => c.module === 'anni80');
    }
    if (state.activePdf === 'dispense') return window.DISPENSE_DATA || [];
    if (state.activePdf === 'krug') return window.KRUG_DATA || [];
    if (state.activePdf === 'stull') return window.STULL_DATA || [];
    if (state.activePdf === 'cards') return window.CARDS_DATA || [];
    return [];
  }

  function getPdfDisplayName(key) {
    if (key === 'dispense') return '1. Dispense Professore';
    if (key === 'krug') return "2. Steve Krug — Don't Make Me Think";
    if (key === 'stull') return '3. Edward Stull — UX Design';
    if (key === 'cards') return '4. Codice Progetto Esame (HTML & CSS)';
    if (key === 'arte-anni80') return "1. Arte Contemporanea Anni '80";
    if (key === 'arte-hirst') return '2. Damien Hirst & Young British Artists';
    if (key === 'arte-eliasson') return '3. Olafur Eliasson — Luce e Percezione';
    if (key === 'arte-chevalier') return '4. Miguel Chevalier — Pixel, IA & Virtuale';
    return key;
  }

  // Inizializzazione applicativa
  function init() {
    loadLocalState();
    applyTheme(state.theme);
    setupEventListeners();

    // Sincronizza gruppi tab con la materia attiva
    const groupWeb = document.getElementById('tabs-group-webdesign');
    const groupArte = document.getElementById('tabs-group-arte');
    const cardsOpt = document.getElementById('exam-scope-cards-opt');
    const brandTitle = document.getElementById('brand-main-title');

    if (state.currentSubject === 'arte') {
      if (groupWeb) groupWeb.style.display = 'none';
      if (groupArte) groupArte.style.display = 'flex';
      if (brandTitle) brandTitle.textContent = "Storia dell'Arte Contemporanea";
      if (cardsOpt) cardsOpt.style.display = 'none';
      if (!state.activePdf || !state.activePdf.startsWith('arte-')) {
        state.activePdf = 'arte-anni80';
        state.activeChapIndex = 0;
      }
      document.querySelectorAll('#tabs-group-arte .pdf-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.pdf === state.activePdf);
      });
    } else {
      if (groupWeb) groupWeb.style.display = 'flex';
      if (groupArte) groupArte.style.display = 'none';
      if (brandTitle) brandTitle.textContent = "UX & Web Design";
      if (cardsOpt) cardsOpt.style.display = 'block';
      if (!state.activePdf || state.activePdf.startsWith('arte-')) {
        state.activePdf = 'dispense';
        state.activeChapIndex = 0;
      }
      document.querySelectorAll('#tabs-group-webdesign .pdf-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.pdf === state.activePdf);
      });
    }

    if (state.activeView === 'hub') {
      switchView('hub');
    } else {
      switchView(state.activeView || 'study');
      renderSidebar();
      renderCurrentChapter();
    }

    updateProgressIndicators();
    updateCramCounter();
    renderGlossary();
  }

  // GESTIONE TEMA
  function applyTheme(theme) {
    state.theme = theme;
    if (theme === 'dark') {
      document.body.classList.remove('theme-light');
      document.body.classList.add('theme-dark');
    } else {
      document.body.classList.remove('theme-dark');
      document.body.classList.add('theme-light');
    }
  }

  function toggleTheme() {
    const nextTheme = state.theme === 'light' ? 'dark' : 'light';
    applyTheme(nextTheme);
    saveLocalState();
  }

  // EVENT LISTENERS GENERALI
  function setupEventListeners() {
    // Switch PDF tabs
    document.querySelectorAll('.pdf-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const pdfKey = tab.dataset.pdf;
        if (pdfKey !== state.activePdf) {
          state.activePdf = pdfKey;
          state.activeChapIndex = 0;
          document.querySelectorAll('.pdf-tab').forEach(t => t.classList.remove('active'));
          tab.classList.add('active');
          renderSidebar();
          renderCurrentChapter();
          saveLocalState();
        }
      });
    });

    // Switch viste (Studio, Ripasso, Test, Glossario)
    document.querySelectorAll('.pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const view = btn.dataset.view;
        switchView(view);
      });
    });

    // Theme toggle button
    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) themeBtn.addEventListener('click', toggleTheme);

    // Sidebar toggle button
    const sidebarToggleBtn = document.getElementById('btn-sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    if (sidebarToggleBtn && sidebar) {
      sidebarToggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
      });
    }

    // Modal data backup
    const modalBtn = document.getElementById('btn-data-modal');
    const modalClose = document.getElementById('btn-close-modal');
    const dataModal = document.getElementById('data-modal');
    if (modalBtn && dataModal) {
      modalBtn.addEventListener('click', () => dataModal.style.display = 'flex');
    }
    if (modalClose && dataModal) {
      modalClose.addEventListener('click', () => dataModal.style.display = 'none');
    }

    // Export backup
    const exportBtn = document.getElementById('btn-export-backup');
    if (exportBtn) {
      exportBtn.addEventListener('click', exportBackupJson);
    }

    // Import backup trigger
    const importBtn = document.getElementById('btn-trigger-import');
    const importInput = document.getElementById('input-import-file');
    if (importBtn && importInput) {
      importBtn.addEventListener('click', () => importInput.click());
      importInput.addEventListener('change', importBackupJson);
    }

    // Reset data
    const resetBtn = document.getElementById('btn-reset-data');
    if (resetBtn) {
      resetBtn.addEventListener('click', resetAllData);
    }

    // Switch Materia / Hub
    const hubNavBtn = document.getElementById('btn-hub-nav');
    if (hubNavBtn) {
      hubNavBtn.addEventListener('click', () => {
        state.currentSubject = 'hub';
        switchView('hub');
        saveLocalState();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    const enterWebBtn = document.getElementById('btn-enter-webdesign');
    if (enterWebBtn) {
      enterWebBtn.addEventListener('click', () => {
        switchSubject('web-design');
      });
    }

    const enterArteBtn = document.getElementById('btn-enter-arte');
    if (enterArteBtn) {
      enterArteBtn.addEventListener('click', () => {
        switchSubject('arte');
      });
    }

    // Subtabs capitolo (Sintesi, Flashcard, Quiz, Domande, Note)
    document.querySelectorAll('.subtab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const subtab = btn.dataset.subtab;
        switchSubtab(subtab);
      });
    });

    // Navigazione capitoli footer (risolve il bug del reset tab e aggiornamento sidebar)
    const prevBtn = document.getElementById('btn-prev-chap');
    const nextBtn = document.getElementById('btn-next-chap');
    const completeBtn = document.getElementById('btn-toggle-complete');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.activeChapIndex > 0) {
          navigateToChapter(state.activeChapIndex - 1);
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        if (state.activeChapIndex < chaps.length - 1) {
          navigateToChapter(state.activeChapIndex + 1);
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
          renderSidebar();
        }
      });
    }

    // Note input auto-save
    const notesInput = document.getElementById('chap-notes-input');
    if (notesInput) {
      let timeout = null;
      notesInput.addEventListener('input', () => {
        const statusEl = document.getElementById('notes-save-status');
        if (statusEl) statusEl.textContent = 'Salvataggio in corso...';
        clearTimeout(timeout);
        timeout = setTimeout(() => {
          const chaps = getCurrentPdfChapters();
          const currentChap = chaps[state.activeChapIndex];
          if (currentChap) {
            state.notes[currentChap.id] = notesInput.value;
            saveLocalState();
            if (statusEl) statusEl.textContent = 'Salvato in locale ✓';
          }
        }, 500);
      });
    }

    // Cramming view filter
    const cramFilter = document.getElementById('cram-filter-select');
    if (cramFilter) {
      cramFilter.addEventListener('change', renderCramList);
    }

    // Exam simulator setup
    setupExamEvents();

    // Glossary search and filters
    const searchInput = document.getElementById('glossary-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', filterGlossary);
    }
    document.querySelectorAll('#glossary-source-filters .filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#glossary-source-filters .filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        filterGlossary();
      });
    });
  }

  // CAMBIO MATERIA (Web Design <-> Storia dell'Arte)
  function switchSubject(subjectKey, targetPdf) {
    state.currentSubject = subjectKey;
    const groupWeb = document.getElementById('tabs-group-webdesign');
    const groupArte = document.getElementById('tabs-group-arte');
    const cardsOpt = document.getElementById('exam-scope-cards-opt');
    const brandTitle = document.getElementById('brand-main-title');

    if (subjectKey === 'arte') {
      if (groupWeb) groupWeb.style.display = 'none';
      if (groupArte) groupArte.style.display = 'flex';
      if (brandTitle) brandTitle.textContent = "Storia dell'Arte Contemporanea";
      if (cardsOpt) cardsOpt.style.display = 'none';

      if (!state.activePdf || !state.activePdf.startsWith('arte-')) {
        state.activePdf = targetPdf || 'arte-anni80';
        state.activeChapIndex = 0;
      }
      document.querySelectorAll('#tabs-group-arte .pdf-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.pdf === state.activePdf);
      });
    } else {
      state.currentSubject = 'web-design';
      if (groupWeb) groupWeb.style.display = 'flex';
      if (groupArte) groupArte.style.display = 'none';
      if (brandTitle) brandTitle.textContent = "UX & Web Design";
      if (cardsOpt) cardsOpt.style.display = 'block';

      if (!state.activePdf || state.activePdf.startsWith('arte-')) {
        state.activePdf = targetPdf || 'dispense';
        state.activeChapIndex = 0;
      }
      document.querySelectorAll('#tabs-group-webdesign .pdf-tab').forEach(t => {
        t.classList.toggle('active', t.dataset.pdf === state.activePdf);
      });
    }

    state.activeSubtab = 'summary';
    switchView('study');
    renderSidebar();
    renderCurrentChapter();
    updateProgressIndicators();
    updateCramCounter();
    saveLocalState();
  }

  // CAMBIO VISTA (Hub / Studio / Ripasso / Test / Glossario)
  function switchView(viewName) {
    state.activeView = viewName;
    document.querySelectorAll('.pill-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.view === viewName);
    });
    document.querySelectorAll('.view-panel').forEach(panel => {
      panel.classList.toggle('active', panel.id === `view-${viewName}`);
    });

    // Gestione visibilità sidebar, selettore PDF e session bar se ci si trova nell'Hub
    const sidebar = document.getElementById('sidebar');
    const pdfNav = document.getElementById('pdf-selector-nav');
    const sessionBar = document.getElementById('session-bar');
    const brandTitle = document.getElementById('brand-main-title');
    const viewPills = document.getElementById('header-view-pills');
    const contentArea = document.getElementById('content-area');

    if (viewName === 'hub') {
      if (sidebar) sidebar.style.display = 'none';
      if (pdfNav) pdfNav.style.display = 'none';
      if (sessionBar) sessionBar.style.display = 'none';
      if (viewPills) viewPills.style.opacity = '0.35';
      if (brandTitle) brandTitle.textContent = 'Hub Materie Universitarie';
      if (contentArea) contentArea.style.maxWidth = '1050px';
    } else {
      if (sidebar) sidebar.style.display = 'flex';
      if (pdfNav) pdfNav.style.display = 'flex';
      if (sessionBar) sessionBar.style.display = 'flex';
      if (viewPills) viewPills.style.opacity = '1';
      if (brandTitle) brandTitle.textContent = state.currentSubject === 'arte' ? "Storia dell'Arte Contemporanea" : "UX & Web Design";
      if (contentArea) contentArea.style.maxWidth = '900px';
    }

    if (viewName === 'cram') {
      renderCramList();
    } else if (viewName === 'glossary') {
      renderGlossary();
    }
  }

  // CAMBIO SUBTAB CAPITOLO (Sintesi, Flashcard, Quiz, Domande, Note)
  function switchSubtab(subtabName) {
    state.activeSubtab = subtabName;
    document.querySelectorAll('.subtab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.subtab === subtabName);
    });
    document.querySelectorAll('.subtab-panel').forEach(panel => {
      panel.classList.toggle('active', panel.id === `subtab-panel-${subtabName}`);
    });
  }

  // NAVIGAZIONE CENTRALIZZATA TRA I CAPITOLI
  // Risolve definitivamente il bug: resetta sempre a 'summary' e sincronizza la sidebar sinistra
  function navigateToChapter(idx) {
    const chapters = getCurrentPdfChapters();
    if (idx < 0 || idx >= chapters.length) return;

    state.activeChapIndex = idx;

    // Resetta SEMPRE alla scheda "Sintesi & Concetti"
    switchSubtab('summary');

    // Aggiorna l'indice dei capitoli a sinistra (classe active e icona 🔵)
    renderSidebar();

    // Renderizza il capitolo selezionato
    renderCurrentChapter();

    // Salva lo stato in localStorage
    saveLocalState();

    // Scorri la finestra in cima
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Scorri visivamente l'elemento attivo nella sidebar sinistra affinché sia visibile
    setTimeout(() => {
      const activeNavEl = document.querySelector('.chapter-nav-item.active');
      if (activeNavEl) {
        activeNavEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }, 60);
  }

  // RENDERING SIDEBAR CAPITOLI
  function renderSidebar() {
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

      // Per Stull, aggiungi header delle parti
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

      const statusIcon = isDone ? '✅' : (idx === state.activeChapIndex ? '🔵' : '⚪');

      item.innerHTML = `
        <span class="chapter-nav-status">${statusIcon}</span>
        <div class="chapter-nav-info">
          <span class="chapter-nav-num">Capitolo ${chap.number}</span>
          <span class="chapter-nav-title">${escapeHtml(chap.title)}</span>
        </div>
      `;

      item.addEventListener('click', () => {
        navigateToChapter(idx);
        switchView('study');
      });

      listEl.appendChild(item);
    });

    const percent = chapters.length > 0 ? Math.round((completedCount / chapters.length) * 100) : 0;
    if (statsEl) statsEl.textContent = `${completedCount}/${chapters.length} (${percent}%)`;
    if (fillEl) fillEl.style.width = `${percent}%`;
  }

  // RENDERING CAPITOLO CORRENTE
  function renderCurrentChapter() {
    const chapters = getCurrentPdfChapters();
    if (chapters.length === 0) return;

    // Boundary check
    if (state.activeChapIndex >= chapters.length) state.activeChapIndex = 0;
    const chap = chapters[state.activeChapIndex];

    // Aggiorna hero
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

    // Aggiorna Storia-Ancora (per Stull)
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

    // Sintesi approfondita HTML
    const summaryBody = document.getElementById('chap-summary-body');
    if (summaryBody) {
      summaryBody.innerHTML = formatMarkdown(chap.summary || 'Nessuna sintesi disponibile.');
    }

    // Punti chiave
    const keyPointsEl = document.getElementById('chap-key-points');
    if (keyPointsEl) {
      keyPointsEl.innerHTML = '';
      (chap.keyPoints || []).forEach(pt => {
        const li = document.createElement('li');
        li.textContent = pt;
        keyPointsEl.appendChild(li);
      });
    }

    // Flashcards
    renderFlashcards(chap);

    // Quiz
    renderQuiz(chap);

    // Domande d'esame aperte
    renderOpenQuestions(chap);

    // Note personali
    const notesInput = document.getElementById('chap-notes-input');
    const notesStatus = document.getElementById('notes-save-status');
    if (notesInput) {
      notesInput.value = state.notes[chap.id] || '';
      if (notesStatus) notesStatus.textContent = state.notes[chap.id] ? 'Salvato in locale ✓' : '';
    }

    // Pulsante completato
    const isDone = !!state.completed[chap.id];
    updateCompleteButtonState(isDone);

    // Disabilita/Abilita bottoni navigazione footer
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

    // Aggiorna session bar
    const pdfNameEl = document.getElementById('active-pdf-name');
    if (pdfNameEl) pdfNameEl.textContent = getPdfDisplayName(state.activePdf);
  }

  // RENDERING FLASHCARDS
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
      const status = state.flashcardStatus[cardId]; // 'known' | 'cram' | undefined

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
            ✔️ Lo so bene
          </button>
          <button class="btn-card-action cram ${status === 'cram' ? 'active' : ''}" data-act="cram" data-id="${cardId}">
            🔁 Da rivedere
          </button>
        </div>
      `;

      // Flip card
      const body = cardEl.querySelector(`#fc-body-${cardId}`);
      const ans = cardEl.querySelector(`#fc-ans-${cardId}`);
      body.addEventListener('click', (e) => {
        if (e.target.closest('.flashcard-footer')) return;
        const isHidden = ans.style.display === 'none';
        ans.style.display = isHidden ? 'block' : 'none';
      });

      // Azioni bottoni
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

  // RENDERING QUIZ
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
      const savedAns = state.quizAnswers[quizId]; // { selectedIndex, isCorrect }

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
          <strong>${savedAns.isCorrect ? '✅ Corretto!' : '❌ Non corretto.'}</strong> ${escapeHtml(q.explanation || '')}
        </div>
      ` : '';

      qCard.innerHTML = `
        <h4 class="quiz-question-title">${qIdx + 1}. ${escapeHtml(q.question)}</h4>
        <div class="quiz-options">${optionsHtml}</div>
        <div class="quiz-exp-container" id="exp-${quizId}">${explanationHtml}</div>
      `;

      // Event listeners per opzioni
      qCard.querySelectorAll('.quiz-option-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const oIdx = parseInt(btn.dataset.oidx, 10);
          const isCorrect = oIdx === q.correctIndex;
          state.quizAnswers[quizId] = { selectedIndex: oIdx, isCorrect: isCorrect };
          
          // Se errato, segna automaticamente per il ripasso mirato
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

  // RENDERING DOMANDE APERTE D'ESAME
  function renderOpenQuestions(chap) {
    const listEl = document.getElementById('chap-open-list');
    const questions = chap.openQuestions || [];
    if (!listEl) return;
    listEl.innerHTML = '';

    if (questions.length === 0) {
      listEl.innerHTML = '<p class="text-muted">Nessuna domanda aperta per questo capitolo.</p>';
      return;
    }

    questions.forEach((q, idx) => {
      const qId = `${chap.id}-open-${idx}`;
      const status = state.openStatus[qId];

      const card = document.createElement('div');
      card.className = 'open-card';

      card.innerHTML = `
        <div class="open-question-text">❓ ${escapeHtml(q.question)}</div>
        <button class="open-toggle-btn" id="btn-toggle-${qId}">Mostra Risposta Modello</button>
        <div class="open-model-answer" id="ans-${qId}" style="display: none;">
          <strong>💡 Risposta Modello & Punti Chiave d'Esame:</strong>
          <p style="margin-top: 8px;">${escapeHtml(q.modelAnswer)}</p>
          <div style="margin-top: 12px; display: flex; gap: 8px;">
            <button class="btn-card-action known ${status === 'known' ? 'active' : ''}" data-act="known">
              ✔️ Risposta acquisita
            </button>
            <button class="btn-card-action cram ${status === 'cram' ? 'active' : ''}" data-act="cram">
              🔁 Aggiungi a ripasso
            </button>
          </div>
        </div>
      `;

      const toggleBtn = card.querySelector(`#btn-toggle-${qId}`);
      const ansBox = card.querySelector(`#ans-${qId}`);
      toggleBtn.addEventListener('click', () => {
        const isHidden = ansBox.style.display === 'none';
        ansBox.style.display = isHidden ? 'block' : 'none';
        toggleBtn.textContent = isHidden ? 'Nascondi Risposta Modello' : 'Mostra Risposta Modello';
      });

      card.querySelectorAll('.btn-card-action').forEach(b => {
        b.addEventListener('click', () => {
          const act = b.dataset.act;
          state.openStatus[qId] = act;
          saveLocalState();
          card.querySelectorAll('.btn-card-action').forEach(btn => btn.classList.remove('active'));
          b.classList.add('active');
        });
      });

      listEl.appendChild(card);
    });
  }

  // AGGIORNA STATO PULSANTE COMPLETATO
  function updateCompleteButtonState(isCompleted) {
    const btn = document.getElementById('btn-toggle-complete');
    const icon = document.getElementById('complete-icon');
    const text = document.getElementById('complete-text');
    if (!btn) return;

    if (isCompleted) {
      btn.classList.add('is-completed');
      if (icon) icon.textContent = '✅';
      if (text) text.textContent = 'Capitolo Completato';
    } else {
      btn.classList.remove('is-completed');
      if (icon) icon.textContent = '⚪';
      if (text) text.textContent = 'Segna come completato';
    }
  }

  // AGGIORNA PERCENTUALI E MINI COUNTERS
  function updateProgressIndicators() {
    const webPdfs = ['dispense', 'krug', 'stull', 'cards'];
    webPdfs.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'dispense') chaps = window.DISPENSE_DATA || [];
      if (pdfKey === 'krug') chaps = window.KRUG_DATA || [];
      if (pdfKey === 'stull') chaps = window.STULL_DATA || [];
      if (pdfKey === 'cards') chaps = window.CARDS_DATA || [];

      let done = 0;
      chaps.forEach(c => {
        if (state.completed[c.id]) done++;
      });

      const badge = document.getElementById(`prog-mini-${pdfKey}`);
      if (badge) badge.textContent = `${done}/${chaps.length}`;

      if (state.currentSubject === 'web-design' && pdfKey === state.activePdf) {
        const pct = chaps.length > 0 ? Math.round((done / chaps.length) * 100) : 0;
        const barText = document.getElementById('active-pdf-progress-text');
        if (barText) barText.textContent = `Progresso: ${pct}% (${done} di ${chaps.length} completati)`;
      }
    });

    const artePdfs = ['arte-anni80', 'arte-hirst', 'arte-eliasson', 'arte-chevalier'];
    const allArte = window.ARTE_DATA || [];
    artePdfs.forEach(pdfKey => {
      let chaps = [];
      if (pdfKey === 'arte-anni80') chaps = allArte.filter(c => c.module === 'anni80');
      if (pdfKey === 'arte-hirst') chaps = allArte.filter(c => c.module === 'hirst');
      if (pdfKey === 'arte-eliasson') chaps = allArte.filter(c => c.module === 'eliasson');
      if (pdfKey === 'arte-chevalier') chaps = allArte.filter(c => c.module === 'chevalier');

      let done = 0;
      chaps.forEach(c => {
        if (state.completed[c.id]) done++;
      });

      const badge = document.getElementById(`prog-mini-${pdfKey}`);
      if (badge) badge.textContent = `${done}/${chaps.length}`;

      if (state.currentSubject === 'arte' && pdfKey === state.activePdf) {
        const pct = chaps.length > 0 ? Math.round((done / chaps.length) * 100) : 0;
        const barText = document.getElementById('active-pdf-progress-text');
        if (barText) barText.textContent = `Progresso: ${pct}% (${done} di ${chaps.length} completati)`;
      }
    });
  }

  // AGGIORNA CONTATORE RIPASSO MIRATO
  function updateCramCounter() {
    let count = 0;
    Object.values(state.flashcardStatus).forEach(st => { if (st === 'cram') count++; });
    Object.values(state.openStatus).forEach(st => { if (st === 'cram') count++; });

    const badge = document.getElementById('cram-badge');
    if (badge) badge.textContent = count;
  }

  // RENDERING VISTA RIPASSO MIRATO (SMART CRAMMING)
  function renderCramList() {
    const filterSelect = document.getElementById('cram-filter-select');
    const filter = filterSelect ? filterSelect.value : 'all';
    const listEl = document.getElementById('cram-items-list');
    const totalEl = document.getElementById('cram-total-label');
    if (!listEl) return;
    listEl.innerHTML = '';

    let allPdfs = [];
    if (state.currentSubject === 'arte') {
      const allArte = window.ARTE_DATA || [];
      allPdfs = [
        { key: 'arte-anni80', name: "Arte Anni '80", data: allArte.filter(c => c.module === 'anni80') },
        { key: 'arte-hirst', name: 'Damien Hirst & YBA', data: allArte.filter(c => c.module === 'hirst') },
        { key: 'arte-eliasson', name: 'Olafur Eliasson', data: allArte.filter(c => c.module === 'eliasson') },
        { key: 'arte-chevalier', name: 'Miguel Chevalier & IA', data: allArte.filter(c => c.module === 'chevalier') }
      ];
    } else {
      allPdfs = [
        { key: 'dispense', name: 'Dispense Professore', data: window.DISPENSE_DATA || [] },
        { key: 'krug', name: "Krug — Don't Make Me Think", data: window.KRUG_DATA || [] },
        { key: 'stull', name: 'Stull — UX Design', data: window.STULL_DATA || [] },
        { key: 'cards', name: 'Codice Progetto Esame', data: window.CARDS_DATA || [] }
      ];
    }

    const itemsToReview = [];

    allPdfs.forEach(pdf => {
      if (filter !== 'all' && filter !== pdf.key) return;

      pdf.data.forEach(chap => {
        // Controlla Flashcards
        (chap.flashcards || []).forEach((fc, fcIdx) => {
          const fcId = `${chap.id}-fc-${fcIdx}`;
          if (state.flashcardStatus[fcId] === 'cram') {
            itemsToReview.push({
              type: 'Flashcard',
              pdfName: pdf.name,
              chapTitle: `Capitolo ${chap.number}: ${chap.title}`,
              question: fc.question,
              answer: fc.answer,
              id: fcId,
              storeType: 'fc'
            });
          }
        });

        // Controlla Domande Aperte
        (chap.openQuestions || []).forEach((oq, oqIdx) => {
          const oqId = `${chap.id}-open-${oqIdx}`;
          if (state.openStatus[oqId] === 'cram') {
            itemsToReview.push({
              type: "Domanda d'Esame",
              pdfName: pdf.name,
              chapTitle: `Capitolo ${chap.number}: ${chap.title}`,
              question: oq.question,
              answer: oq.modelAnswer,
              id: oqId,
              storeType: 'open'
            });
          }
        });

        // Controlla Quiz sbagliati
        (chap.quiz || []).forEach((q, qIdx) => {
          const quizId = `${chap.id}-quiz-${qIdx}`;
          const errId = `quiz-error-${quizId}`;
          if (state.flashcardStatus[errId] === 'cram') {
            itemsToReview.push({
              type: 'Quiz Errato',
              pdfName: pdf.name,
              chapTitle: `Capitolo ${chap.number}: ${chap.title}`,
              question: q.question,
              answer: `Risposta corretta: ${q.options[q.correctIndex]}. Spiegazione: ${q.explanation}`,
              id: errId,
              storeType: 'fc'
            });
          }
        });
      });
    });

    if (totalEl) totalEl.textContent = `Elementi da ripassare: ${itemsToReview.length}`;

    if (itemsToReview.length === 0) {
      listEl.innerHTML = `
        <div style="background: var(--bg-surface); padding: 32px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border-color);">
          <div style="font-size: 32px; margin-bottom: 8px;">🎉</div>
          <h3 style="font-size: 18px; margin-bottom: 6px;">Nessun elemento da ripassare al momento!</h3>
          <p style="color: var(--text-muted); font-size: 14px;">Quando incontri un concetto ostico nei capitoli o sbagli un quiz, contrassegnalo con «Da rivedere»: apparirà automaticamente qui per il consolidamento.</p>
        </div>
      `;
      return;
    }

    itemsToReview.forEach(item => {
      const card = document.createElement('div');
      card.className = 'cram-item-card';

      card.innerHTML = `
        <div class="cram-meta">${item.pdfName} • ${item.chapTitle} • <span style="color: var(--accent-warning);">${item.type}</span></div>
        <div class="cram-question">${escapeHtml(item.question)}</div>
        <div class="cram-answer">${escapeHtml(item.answer)}</div>
        <button class="btn-primary-action" style="padding: 6px 12px; font-size: 13px;" id="btn-mastered-${item.id}">
          ✓ Ho imparato questo concetto (Rimuovi)
        </button>
      `;

      card.querySelector(`#btn-mastered-${item.id}`).addEventListener('click', () => {
        if (item.storeType === 'fc') {
          state.flashcardStatus[item.id] = 'known';
        } else if (item.storeType === 'open') {
          state.openStatus[item.id] = 'known';
        }
        saveLocalState();
        renderCramList();
      });

      listEl.appendChild(card);
    });
  }

  // GESTIONE SIMULATORE ESAME (QUIZ CASUALI)
  function setupExamEvents() {
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
        startExamSession(scope, chosenCount);
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

  function startExamSession(scope, count) {
    let pool = [];

    const getQuizzesFromChapters = (chapList, sourceName) => {
      chapList.forEach(chap => {
        // Privilegia il banco dedicato d'esame per il Test, con fallback sui quiz del capitolo
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

    if (state.currentSubject === 'arte') {
      if (scope === 'current') {
        const currentList = getCurrentPdfChapters();
        getQuizzesFromChapters(currentList, getPdfDisplayName(state.activePdf));
      } else {
        getQuizzesFromChapters(window.ARTE_DATA || [], "Storia dell'Arte Contemporanea");
      }
    } else {
      if (scope === 'current') {
        const currentList = getCurrentPdfChapters();
        getQuizzesFromChapters(currentList, getPdfDisplayName(state.activePdf));
      } else if (scope === 'cards') {
        getQuizzesFromChapters(window.CARDS_DATA || [], 'Codice Progetto Esame (HTML & CSS)');
      } else {
        getQuizzesFromChapters(window.DISPENSE_DATA || [], 'Dispense Professore');
        getQuizzesFromChapters(window.KRUG_DATA || [], "Krug — Don't Make Me Think");
        getQuizzesFromChapters(window.STULL_DATA || [], 'Stull — UX Design');
        getQuizzesFromChapters(window.CARDS_DATA || [], 'Codice Progetto Esame (HTML & CSS)');
      }
    }

    if (pool.length === 0) {
      alert("Nessun quiz disponibile per questo ambito.");
      return;
    }

    // Mescola pool delle domande (Fisher-Yates)
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }

    const rawSelected = pool.slice(0, Math.min(count, pool.length));

    // Rimescola dinamicamente le opzioni per ogni domanda del test
    // garantendo che la risposta corretta non si trovi sempre in prima o seconda posizione
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
          ${q.sourceName} • Capitolo ${q.chapNum}: ${escapeHtml(q.chapTitle)}
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
      feedbackEl.textContent = '🌟 Ottima preparazione! Hai dimostrato una comprensione solida dei concetti.';
    } else if (scorePct >= 60) {
      feedbackEl.textContent = '👍 Buono, ma ci sono alcuni punti da rifinire nei capitoli corrispondenti.';
    } else {
      feedbackEl.textContent = '⚠️ Ti consigliamo di ripassare i capitoli con la modalità guidata e le flashcard.';
    }

    reviewList.innerHTML = '';
    session.answers.forEach((ans, idx) => {
      const item = document.createElement('div');
      item.className = 'cram-item-card';
      item.style.borderLeftColor = ans.isCorrect ? 'var(--accent-success)' : 'var(--accent-danger)';
      item.style.marginTop = '12px';

      item.innerHTML = `
        <div style="font-weight: 700; font-size: 12px; margin-bottom: 4px;">
          ${ans.isCorrect ? '✅ Risposta Corretta' : '❌ Errore'} (Domanda ${idx + 1})
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

  // GLOSSARIO & RICERCA
  function renderGlossary() {
    filterGlossary();
  }

  function filterGlossary() {
    const input = document.getElementById('glossary-search-input');
    const query = input ? input.value.toLowerCase().trim() : '';
    const activeChip = document.querySelector('#glossary-source-filters .filter-chip.active');
    const filterSource = activeChip ? activeChip.dataset.source : 'all';

    const container = document.getElementById('glossary-items-container');
    if (!container) return;
    container.innerHTML = '';

    const items = window.GLOSSARY_DATA || [];
    const filtered = items.filter(item => {
      // Filtro fonte
      if (filterSource !== 'all') {
        if (!item.source.toLowerCase().includes(filterSource.toLowerCase())) return false;
      }
      // Filtro ricerca
      if (!query) return true;
      return item.term.toLowerCase().includes(query) || item.def.toLowerCase().includes(query);
    });

    if (filtered.length === 0) {
      container.innerHTML = '<p class="text-muted" style="grid-column: 1 / -1; padding: 20px;">Nessun termine trovato per questa ricerca.</p>';
      return;
    }

    filtered.forEach(item => {
      const card = document.createElement('div');
      card.className = 'glossary-card';
      card.innerHTML = `
        <div class="glossary-card-header">
          <span class="glossary-term">${escapeHtml(item.term)}</span>
          <span class="glossary-source-badge">${escapeHtml(item.source)}</span>
        </div>
        <p class="glossary-def">${escapeHtml(item.def)}</p>
      `;
      container.appendChild(card);
    });
  }

  // EXPORT BACKUP JSON
  function exportBackupJson() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(localStorage.getItem(STORAGE_KEY) || "{}");
    const downloadAnchor = document.createElement('a');
    const dateStr = new Date().toISOString().split('T')[0];
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `backup_studio_ux_${dateStr}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  }

  // IMPORT BACKUP JSON
  function importBackupJson(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
      try {
        const content = e.target.result;
        const parsed = JSON.parse(content);
        if (parsed && typeof parsed === 'object') {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(parsed));
          alert("Backup importato con successo! La pagina verrà ricaricata.");
          window.location.reload();
        } else {
          alert("File backup non valido.");
        }
      } catch (err) {
        alert("Errore nella lettura del file backup: " + err.message);
      }
    };
    reader.readAsText(file);
  }

  // RESET TUTTI I DATI
  function resetAllData() {
    if (confirm("Sei sicuro di voler azzerare tutti i progressi e le note? L'operazione è irreversibile a meno che tu non abbia esportato un backup.")) {
      localStorage.removeItem(STORAGE_KEY);
      window.location.reload();
    }
  }

  // UTILITY PARSER MARKDOWN
  function formatMarkdown(text) {
    if (!text) return '';
    let html = escapeHtml(text);

    // Tables
    html = html.replace(/((?:\|[^\n]+\|\r?\n)+)/g, function (tableBlock) {
      const rows = tableBlock.trim().split(/\r?\n/).filter(r => r.trim());
      if (rows.length < 2) return tableBlock;
      let tableHtml = '<div class="table-responsive"><table class="academic-table">';
      let isHeader = true;

      rows.forEach((row, rIdx) => {
        // Skip separator row (| :--- | :--- |)
        if (row.match(/^\|(?:\s*:?-+:?\s*\|)+$/)) {
          isHeader = false;
          return;
        }
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

    // Headings
    html = html.replace(/^#### (.*?)$/gm, '<h4>$1</h4>');
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
    // Horizontal rules
    html = html.replace(/^---$/gm, '<hr class="summary-divider">');
    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Italic
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    // Code blocks
    html = html.replace(/```(html|css|js|)([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
    // Inline code
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');

    // Blockquotes (markdown > or &gt;)
    html = html.replace(/((?:^(?:&gt;|>)[ \t]?[^\n]*(?:\r?\n|$))+)/gm, function (block) {
      const lines = block.trim().split(/\r?\n/).map(l => l.replace(/^(?:&gt;|>)[ \t]?/, '').trim()).filter(Boolean);
      return '\n\n<blockquote class="summary-quote">' + lines.join('<br>') + '</blockquote>\n\n';
    });

    // Bullets
    html = html.replace(/^[•\-\*] (.*?)$/gm, '<li>$1</li>');
    // Wrap consecutive lis in ul
    html = html.replace(/(<li>.*<\/li>(\n|))+/g, '<ul>$&</ul>');
    // Paragraphs
    html = html.split('\n\n').map(p => {
      p = p.trim();
      if (!p) return '';
      if (!p.startsWith('<h') && !p.startsWith('<ul') && !p.startsWith('<pre') && !p.startsWith('<div') && !p.startsWith('<hr') && !p.startsWith('<blockquote')) {
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

  // BOOTSTRAP
  document.addEventListener('DOMContentLoaded', init);

})();
