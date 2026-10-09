/**
 * Studio ABA Catania — Core Engine
 * Modulo condiviso: stato, localStorage, rendering capitolo/flashcard/quiz,
 * simulatore d'esame, lettore vocale (TTS), tema, parser Markdown.
 * Caricato da ogni pagina di studio dopo js/layout.js; inizializzato da js/subject-app.js.
 */

const StudyCore = (function () {
  'use strict';

  // CHIAVE LOCAL STORAGE
  // Chiave storica mantenuta per non perdere i progressi già salvati dagli studenti
  const STORAGE_KEY = 'ux_web_study_state_v1';
  const THEME_KEY = 'aba_studio_theme';

  // STATO APPLICATIVO
  const state = {
    currentSubject: '',
    activePdf: '',
    activeChapIndex: 0,
    activeSubtab: 'summary',
    activeView: 'study',
    theme: 'light',
    completed: {},
    flashcardStatus: {},
    quizAnswers: {},
    srs: {},
    activity: {},
    examHistory: [],
    oralLog: {},
    examSession: null,
    ttsSpeed: 1
  };

  // Icone SVG usate dal motore (le icone del layout sono in js/layout.js)
  const ICONS = {
    circle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/></svg>',
    circleFilled: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg>',
    checkCircle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--accent-success)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    xCircle: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--accent-danger)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
    thumbsUp: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
    repeat: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>',
    star: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
  };

  // ── localStorage ──

  // Posizione di lettura salvata per ogni materia: { [subjectId]: { activePdf, activeChapIndex } }
  let positions = {};

  function loadLocalState(subjectId) {
    if (subjectId) state.currentSubject = subjectId;
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.completed) state.completed = parsed.completed;
        if (parsed.flashcardStatus) state.flashcardStatus = parsed.flashcardStatus;
        if (parsed.quizAnswers) state.quizAnswers = parsed.quizAnswers;
        if (parsed.srs) state.srs = parsed.srs;
        if (parsed.activity) state.activity = parsed.activity;
        if (Array.isArray(parsed.examHistory)) state.examHistory = parsed.examHistory;
        if (parsed.oralLog) state.oralLog = parsed.oralLog;
        if (parsed.positions) positions = parsed.positions;

        const pos = positions[state.currentSubject];
        if (pos) {
          state.activePdf = pos.activePdf;
          state.activeChapIndex = pos.activeChapIndex || 0;
        } else {
          // Formato precedente: un'unica posizione condivisa (subject-app.js la scarta se non valida)
          if (parsed.activePdf) state.activePdf = parsed.activePdf;
          if (typeof parsed.activeChapIndex === 'number') state.activeChapIndex = parsed.activeChapIndex;
        }
        state.activeView = parsed.activeView === 'exam' ? 'exam' : 'study';
        if (parsed.theme) state.theme = parsed.theme;
      }

      const globalTheme = localStorage.getItem(THEME_KEY);
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
      positions[state.currentSubject] = {
        activePdf: state.activePdf,
        activeChapIndex: state.activeChapIndex
      };
      const payload = {
        completed: state.completed,
        flashcardStatus: state.flashcardStatus,
        quizAnswers: state.quizAnswers,
        srs: state.srs,
        activity: state.activity,
        examHistory: state.examHistory.slice(-30),
        oralLog: state.oralLog,
        positions: positions,
        lastSubject: state.currentSubject,
        activeView: state.activeView,
        theme: state.theme
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
      localStorage.setItem(THEME_KEY, theme);
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

      let statusIcon;
      if (isDone) {
        statusIcon = `<span class="nav-icon done">${ICONS.checkCircle}</span>`;
      } else if (idx === state.activeChapIndex) {
        statusIcon = `<span class="nav-icon active-dot">${ICONS.circleFilled}</span>`;
      } else {
        statusIcon = `<span class="nav-icon">${ICONS.circle}</span>`;
      }

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
        if (window.innerWidth <= 860) {
          const sidebar = document.getElementById('sidebar');
          const backdrop = document.getElementById('sidebar-backdrop');
          if (sidebar) sidebar.classList.remove('mobile-open');
          if (backdrop) backdrop.classList.remove('active');
        }
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

    applyGlossary(summaryBody);
    renderOpenQuestions(chap);
    renderFlashcards(chap);
    renderQuiz(chap);

    replayAnimation(document.querySelector('#view-study .chapter-hero'), 'anim-enter');
    replayAnimation(document.getElementById('chap-summary-body'), 'anim-enter');

    const isDone = !!state.completed[chap.id];
    updateCompleteButtonState(isDone);

    const prevBtns = document.querySelectorAll('#btn-prev-chap, .btn-prev-chap');
    const nextBtns = document.querySelectorAll('#btn-next-chap, .btn-next-chap');
    const isFirst = state.activeChapIndex === 0;
    const isLast = state.activeChapIndex >= chapters.length - 1;

    prevBtns.forEach(btn => {
      btn.disabled = isFirst;
      btn.style.opacity = isFirst ? '0.45' : '1';
      btn.style.cursor = isFirst ? 'not-allowed' : 'pointer';
    });

    nextBtns.forEach(btn => {
      btn.disabled = isLast;
      btn.style.opacity = isLast ? '0.45' : '1';
      btn.style.cursor = isLast ? 'not-allowed' : 'pointer';
    });

    const pdfNameEl = document.getElementById('active-pdf-name');
    if (pdfNameEl) pdfNameEl.textContent = getPdfDisplayName(state.activePdf);
  }

  // ── Glossario ──
  // Se la pagina carica un glossario (window.GLOSSARY_DATA), la prima occorrenza di ogni termine
  // nella sintesi diventa un pulsante che mostra la definizione.

  let glossaryIndex = null;

  function getGlossaryIndex() {
    if (glossaryIndex) return glossaryIndex;
    const data = window.GLOSSARY_DATA || [];
    const entries = [];
    data.forEach(g => {
      const keys = [g.term.split(' (')[0].trim()];
      const inner = (g.term.match(/\(([^)]+)\)/) || [])[1];
      if (inner && !/\d|«/.test(inner)) {
        const alias = inner.split(' - ')[0].trim();
        if (alias.split(/\s+/).length >= 2) keys.push(alias);
      }
      keys.filter(k => k.length >= 4).forEach(k => entries.push({ key: k, entry: g }));
    });
    entries.sort((a, b) => b.key.length - a.key.length);
    const escRe = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    glossaryIndex = {
      entries,
      re: entries.length ? new RegExp('(^|[^\\p{L}])(' + entries.map(e => escRe(e.key)).join('|') + ')(?![\\p{L}])', 'iu') : null
    };
    return glossaryIndex;
  }

  function applyGlossary(container) {
    if (!container || !window.GLOSSARY_DATA) return;
    const idx = getGlossaryIndex();
    if (!idx.re) return;
    const used = new Set();
    const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
      acceptNode: n => n.parentElement.closest('h2, h3, h4, figcaption, .glossary-term, code, th')
        ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT
    });
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node => {
      let text = node.nodeValue;
      let m;
      const frag = document.createDocumentFragment();
      let changed = false;
      while (text && (m = idx.re.exec(text))) {
        const word = m[2];
        const hit = idx.entries.find(e => e.key.toLowerCase() === word.toLowerCase());
        const start = m.index + m[1].length;
        // I termini di una sola parola (es. "Contrasto") valgono solo con la maiuscola, per non marcare l'uso comune
        const skip = !hit || used.has(hit.entry.term) || (!/\s/.test(hit.key) && word !== hit.key);
        if (skip) {
          frag.appendChild(document.createTextNode(text.slice(0, start + word.length)));
          text = text.slice(start + word.length);
          continue;
        }
        used.add(hit.entry.term);
        frag.appendChild(document.createTextNode(text.slice(0, start)));
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'glossary-term';
        btn.textContent = word;
        btn.dataset.term = hit.entry.term;
        btn.dataset.def = hit.entry.def;
        btn.dataset.source = hit.entry.source || '';
        frag.appendChild(btn);
        text = text.slice(start + word.length);
        changed = true;
      }
      if (changed) {
        if (text) frag.appendChild(document.createTextNode(text));
        node.parentNode.replaceChild(frag, node);
      }
    });
  }

  function setupGlossaryPopover() {
    let pop = null;
    function close() {
      if (pop) { pop.remove(); pop = null; }
    }
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.glossary-term');
      if (!btn) {
        if (pop && !e.target.closest('.glossary-popover')) close();
        return;
      }
      const same = pop && pop.dataset.term === btn.dataset.term;
      close();
      if (same) return;
      pop = document.createElement('div');
      pop.className = 'glossary-popover';
      pop.dataset.term = btn.dataset.term;
      pop.setAttribute('role', 'dialog');
      pop.innerHTML = `
        <div class="glossary-popover-head">
          <strong>${escapeHtml(btn.dataset.term)}</strong>
          ${btn.dataset.source ? `<span>${escapeHtml(btn.dataset.source)}</span>` : ''}
        </div>
        <p>${escapeHtml(btn.dataset.def)}</p>`;
      document.body.appendChild(pop);
      const r = btn.getBoundingClientRect();
      const w = Math.min(340, window.innerWidth - 32);
      pop.style.width = w + 'px';
      pop.style.left = Math.max(16, Math.min(window.scrollX + r.left, window.scrollX + window.innerWidth - w - 16)) + 'px';
      pop.style.top = (window.scrollY + r.bottom + 8) + 'px';
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    window.addEventListener('resize', close);
  }

  // ── Domande da orale ──
  // Formati accettati: "testo domanda" oppure { question, modelAnswer }

  function renderOpenQuestions(chap) {
    const section = document.getElementById('open-questions-section');
    const listEl = document.getElementById('chap-open-questions');
    if (!section || !listEl) return;
    const items = (chap.openQuestions || [])
      .map(q => (typeof q === 'string' ? { question: q } : q))
      .filter(q => q && q.question);

    section.style.display = items.length ? '' : 'none';
    listEl.innerHTML = items.map(q => q.modelAnswer ? `
      <details class="open-question-item">
        <summary>${escapeHtml(q.question)}</summary>
        <div class="open-question-answer">${formatMarkdown(q.modelAnswer)}</div>
      </details>` : `
      <div class="open-question-item open-question-plain">${escapeHtml(q.question)}</div>`).join('');
  }

  // ── Ripasso a intervalli (flashcard) ──
  // Ogni scheda ha una "scatola" (0-5): più la ricordi, più il ripasso successivo si allontana.
  // state.srs[cardId] = { box, due: 'AAAA-MM-GG', reviews }
  const SRS_INTERVALS = [0, 1, 3, 7, 14, 30];

  function todayKey(date) {
    const d = date || new Date();
    const z = n => String(n).padStart(2, '0');
    return `${d.getFullYear()}-${z(d.getMonth() + 1)}-${z(d.getDate())}`;
  }

  function addDays(days) {
    const d = new Date();
    d.setDate(d.getDate() + days);
    return todayKey(d);
  }

  function daysUntil(key) {
    return Math.round((new Date(key) - new Date(todayKey())) / 86400000);
  }

  // Le schede valutate con la versione precedente ("Lo so bene" / "Da rivedere") entrano nel ripasso
  function getCardSrs(cardId) {
    if (state.srs[cardId]) return state.srs[cardId];
    const legacy = state.flashcardStatus[cardId];
    if (legacy === 'known') return { box: 2, due: todayKey(), reviews: 1 };
    if (legacy === 'cram') return { box: 0, due: todayKey(), reviews: 1 };
    return null;
  }

  function isCardDue(cardId) {
    const s = getCardSrs(cardId);
    return !!s && s.due <= todayKey();
  }

  // grade: 'again' (non la sapevo), 'hard' (incerta), 'good' (la sapevo)
  function gradeCard(cardId, grade) {
    const cur = getCardSrs(cardId) || { box: 0, reviews: 0 };
    let box;
    let days;
    if (grade === 'again') {
      box = 0; days = 0;
    } else if (grade === 'hard') {
      box = Math.max(1, cur.box); days = 1;
    } else {
      box = Math.min(SRS_INTERVALS.length - 1, Math.max(cur.box + 1, 2)); days = SRS_INTERVALS[box];
    }
    state.srs[cardId] = { box, due: addDays(days), reviews: (cur.reviews || 0) + 1 };
    state.flashcardStatus[cardId] = grade === 'good' ? 'known' : 'cram';
    logActivity();
    saveLocalState();
    return state.srs[cardId];
  }

  function describeCard(cardId) {
    const s = getCardSrs(cardId);
    if (!s) return { text: 'Nuova', cls: 'is-new' };
    const d = daysUntil(s.due);
    if (d <= 0) return { text: 'Da ripassare oggi', cls: 'is-due' };
    if (d === 1) return { text: 'Prossimo ripasso: domani', cls: 'is-scheduled' };
    return { text: `Prossimo ripasso: tra ${d} giorni`, cls: s.box >= 4 ? 'is-learned' : 'is-scheduled' };
  }

  // Attività giornaliera (per la serie di giorni di studio nelle statistiche)
  function logActivity() {
    const k = todayKey();
    state.activity[k] = (state.activity[k] || 0) + 1;
  }

  // Riavvia un'animazione CSS sullo stesso elemento
  function replayAnimation(el, cls) {
    if (!el) return;
    el.classList.remove(cls);
    void el.offsetWidth;
    el.classList.add(cls);
  }

  // ── Flashcards ──

  // Scheda con rotazione 3D e tre pulsanti di valutazione; usata nel capitolo e nel ripasso
  function buildFlashcard(card, cardId, onGraded) {
    const el = document.createElement('div');
    el.className = 'flashcard-card';
    const status = describeCard(cardId);
    el.innerHTML = `
      <button type="button" class="flashcard-flip" aria-label="Gira la scheda" aria-pressed="false">
        <span class="flashcard-inner">
          <span class="flashcard-face flashcard-front">
            <span class="flashcard-label">Domanda</span>
            <span class="flashcard-content">${escapeHtml(card.question)}</span>
            <span class="flashcard-hint">${ICONS.repeat} Tocca per girare</span>
          </span>
          <span class="flashcard-face flashcard-back">
            <span class="flashcard-label">Risposta</span>
            <span class="flashcard-answer">${escapeHtml(card.answer)}</span>
          </span>
        </span>
      </button>
      <div class="flashcard-footer">
        <span class="flashcard-due ${status.cls}">${status.text}</span>
        <div class="flashcard-grades" role="group" aria-label="Quanto la ricordavi?">
          <button type="button" class="btn-grade grade-again" data-grade="again">Non la sapevo</button>
          <button type="button" class="btn-grade grade-hard" data-grade="hard">Incerta</button>
          <button type="button" class="btn-grade grade-good" data-grade="good">La sapevo</button>
        </div>
      </div>
    `;
    const flip = el.querySelector('.flashcard-flip');
    flip.addEventListener('click', () => {
      const flipped = el.classList.toggle('is-flipped');
      flip.setAttribute('aria-pressed', String(flipped));
    });
    el.querySelectorAll('.btn-grade').forEach(btn => {
      btn.addEventListener('click', () => {
        gradeCard(cardId, btn.dataset.grade);
        const st = describeCard(cardId);
        const due = el.querySelector('.flashcard-due');
        due.className = `flashcard-due ${st.cls}`;
        due.textContent = st.text;
        el.querySelectorAll('.btn-grade').forEach(b => b.classList.toggle('active', b === btn));
        replayAnimation(due, 'anim-pop');
        if (onGraded) onGraded(btn.dataset.grade);
      });
    });
    return el;
  }

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
      const cardEl = buildFlashcard(card, `${chap.id}-fc-${idx}`);
      cardEl.style.setProperty('--stagger', idx);
      listEl.appendChild(cardEl);
    });
  }

  // ── Quiz ──

  // Indice della risposta corretta (alcuni file dati storici usano "correct")
  function getCorrectIndex(q) {
    return typeof q.correctIndex === 'number' ? q.correctIndex : q.correct;
  }

  // Ordine di visualizzazione delle opzioni, mescolato in modo stabile per ogni quiz:
  // la posizione della risposta giusta non è prevedibile ma non cambia a ogni ricarica.
  function getShuffledOrder(seedText, length) {
    let h = 2166136261;
    for (let i = 0; i < seedText.length; i++) {
      h ^= seedText.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    const order = Array.from({ length }, (_, i) => i);
    for (let i = length - 1; i > 0; i--) {
      h = Math.imul(h ^ (h >>> 15), 2246822507) >>> 0;
      const j = h % (i + 1);
      [order[i], order[j]] = [order[j], order[i]];
    }
    return order;
  }

  function renderQuiz(chap, justAnsweredId) {
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
      qCard.className = 'quiz-card' + (quizId === justAnsweredId ? ' just-answered' : '');
      qCard.style.setProperty('--stagger', qIdx);

      // data-oidx conserva l'indice originale dell'opzione: le risposte salvate restano valide
      const correctIndex = getCorrectIndex(q);
      const optionsHtml = getShuffledOrder(quizId, q.options.length).map(oIdx => {
        let extraClass = '';
        if (savedAns) {
          if (oIdx === correctIndex) extraClass = 'selected-correct';
          else if (oIdx === savedAns.selectedIndex) extraClass = 'selected-wrong';
        }
        return `
          <button class="quiz-option-btn ${extraClass}" data-quizid="${quizId}" data-oidx="${oIdx}" ${savedAns ? 'disabled' : ''}>
            ${escapeHtml(q.options[oIdx])}
          </button>
        `;
      }).join('');

      const explanationHtml = savedAns ? `
        <div class="quiz-explanation-box ${savedAns.selectedIndex === correctIndex ? 'is-correct' : 'is-wrong'}">
          <strong>${savedAns.selectedIndex === correctIndex ? ICONS.checkCircle + ' Corretto!' : ICONS.xCircle + ' Non corretto.'}</strong> ${escapeHtml(q.explanation || '')}
        </div>
      ` : '';

      qCard.innerHTML = `
        <h4 class="quiz-question-title">${qIdx + 1}. ${escapeHtml(q.question)}</h4>
        <div class="quiz-options">${optionsHtml}</div>
        <div class="quiz-exp-container" id="exp-${quizId}">${explanationHtml}</div>
      `;

      if (!savedAns) {
        qCard.querySelectorAll('.quiz-option-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            const oIdx = parseInt(btn.dataset.oidx, 10);
            const isCorrect = oIdx === correctIndex;
            state.quizAnswers[quizId] = { selectedIndex: oIdx, isCorrect: isCorrect };
            if (!isCorrect) {
              state.flashcardStatus[`quiz-error-${quizId}`] = 'cram';
            }
            logActivity();
            saveLocalState();
            renderQuiz(chap, quizId);
          });
        });
      }

      listEl.appendChild(qCard);
    });


    const answeredIds = quizzes.map((_, i) => `${chap.id}-quiz-${i}`).filter(id => state.quizAnswers[id]);
    if (answeredIds.length > 0) {
      const correct = quizzes.filter((q, i) => {
        const a = state.quizAnswers[`${chap.id}-quiz-${i}`];
        return a && a.selectedIndex === getCorrectIndex(q);
      }).length;
      const footer = document.createElement('div');
      footer.className = 'quiz-reset-bar';
      footer.innerHTML = `
        <span>Risposte corrette: <strong>${correct} / ${answeredIds.length}</strong></span>
        <button type="button" class="btn-secondary-action">${ICONS.repeat} Rifai i quiz del capitolo</button>
      `;
      footer.querySelector('button').addEventListener('click', () => {
        answeredIds.forEach(id => { delete state.quizAnswers[id]; });
        saveLocalState();
        renderQuiz(chap);
      });
      listEl.appendChild(footer);
    }
  }

  // ── Completamento ──

  function updateCompleteButtonState(isCompleted) {
    const btns = document.querySelectorAll('#btn-toggle-complete, .btn-toggle-complete');
    btns.forEach(btn => {
      const icon = btn.querySelector('.complete-icon') || btn.querySelector('#complete-icon') || document.getElementById('complete-icon');
      const text = btn.querySelector('.complete-text') || btn.querySelector('#complete-text') || document.getElementById('complete-text');

      if (isCompleted) {
        btn.classList.add('is-completed');
        if (icon) icon.innerHTML = ICONS.checkCircle;
        if (text) text.textContent = 'Capitolo Completato';
      } else {
        btn.classList.remove('is-completed');
        if (icon) icon.innerHTML = ICONS.circle;
        if (text) text.textContent = 'Segna come completato';
      }
    });
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

    if (!pool || pool.length === 0) {
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
        isCorrect: idx === getCorrectIndex(q)
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

    const scopeSelect = document.getElementById('exam-scope-select');
    const scopeLabel = scopeSelect && scopeSelect.selectedOptions[0] ? scopeSelect.selectedOptions[0].textContent : '';
    state.examSession = {
      scopeLabel: scope === 'current' ? getPdfDisplayName(state.activePdf) : scopeLabel,
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
    const progressFill = document.getElementById('exam-progress-fill');
    if (progressFill) progressFill.style.width = `${Math.round((session.currentIndex / session.questions.length) * 100)}%`;

    container.innerHTML = `
      <div class="quiz-card anim-enter" style="margin-top: 14px;">
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

    // Voto indicativo in trentesimi (sufficienza a 18, come all'esame)
    const grade = Math.round((correctCount / total) * 30);
    const gradeText = grade >= 18 ? `${grade}/30` : `${grade}/30 (insufficiente)`;
    titleEl.textContent = `Voto stimato: ${gradeText} — ${correctCount} risposte corrette su ${total} (${scorePct}%)`;

    if (scorePct >= 80) {
      feedbackEl.innerHTML = `${ICONS.star} Ottima preparazione! Hai dimostrato una comprensione solida dei concetti.`;
    } else if (scorePct >= 60) {
      feedbackEl.innerHTML = `${ICONS.thumbsUp} Buono, ma ci sono alcuni punti da rifinire nei capitoli corrispondenti.`;
    } else {
      feedbackEl.innerHTML = `${ICONS.repeat} Ti consigliamo di ripassare i capitoli con la modalità guidata e le flashcard.`;
    }

    state.examHistory.push({
      date: todayKey(), subject: state.currentSubject, scope: session.scopeLabel,
      correct: correctCount, total: total, grade: grade
    });
    logActivity();
    saveLocalState();

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

    html = html.replace(/^#### (.*?)$/gm, '\n\n<h4>$1</h4>\n\n');
    html = html.replace(/^### (.*?)$/gm, '\n\n<h3>$1</h3>\n\n');
    html = html.replace(/^## (.*?)$/gm, '\n\n<h2>$1</h2>\n\n');
    html = html.replace(/^---$/gm, '\n\n<hr class="summary-divider">\n\n');
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    html = html.replace(/```(html|css|js|)([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');

    html = html.replace(/((?:^(?:&gt;|>)[ \t]?[^\n]*(?:\r?\n|$))+)/gm, function (block) {
      const lines = block.trim().split(/\r?\n/).map(l => l.replace(/^(?:&gt;|>)[ \t]?/, '').trim()).filter(Boolean);
      return '\n\n<blockquote class="summary-quote">' + lines.join('<br>') + '</blockquote>\n\n';
    });

    // Liste non ordinate (- item, * item, • item)
    html = html.replace(/((?:^[•\-\*][ \t]+[^\n]+(?:\r?\n|$))+)/gm, function (match) {
      const items = match.trim().split(/\r?\n/).map(line => {
        const text = line.replace(/^[•\-\*][ \t]+/, '').trim();
        return `  <li>${text}</li>`;
      }).join('\n');
      return `\n\n<ul class="study-list">\n${items}\n</ul>\n\n`;
    });

    // Liste ordinate numerate (1. item, 2. item)
    html = html.replace(/((?:^\d+\.[ \t]+[^\n]+(?:\r?\n|$))+)/gm, function (match) {
      const items = match.trim().split(/\r?\n/).map(line => {
        const text = line.replace(/^\d+\.[ \t]+/, '').trim();
        return `  <li>${text}</li>`;
      }).join('\n');
      return `\n\n<ol class="study-list">\n${items}\n</ol>\n\n`;
    });

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
      if (!p.startsWith('<h') && !p.startsWith('<ul') && !p.startsWith('<ol') && !p.startsWith('<pre') && !p.startsWith('<div') && !p.startsWith('<hr') && !p.startsWith('<blockquote') && !p.startsWith('<figure')) {
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
      bar.classList.add('is-sticky');
    } else if (status === 'paused') {
      if (playIcon) playIcon.style.display = 'inline-flex';
      if (pauseIcon) pauseIcon.style.display = 'none';
      if (label) label.textContent = 'Riprendi';
      if (stopBtn) stopBtn.style.display = 'inline-flex';
      if (visualizer) visualizer.style.display = 'none';
      if (statusLabel) statusLabel.textContent = 'In pausa';
      bar.classList.add('is-playing');
      bar.classList.add('is-sticky');
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
      bar.classList.remove('is-sticky');
    }
  }

  function getItalianVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices() || [];
    if (!voices.length) return null;
    
    // 1. Voce Google italiano (Chromium desktop/Android)
    let voice = voices.find(v => v.lang && (v.lang === 'it-IT' || v.lang === 'it_IT') && v.name.toLowerCase().includes('google'));
    
    // 2. Voci neurali / naturali / Siri / migliorate
    if (!voice) {
      voice = voices.find(v => v.lang && (v.lang.startsWith('it') || v.lang.includes('IT')) && (v.name.includes('Natural') || v.name.includes('Neural') || v.name.includes('Siri') || v.name.includes('Enhanced') || v.name.includes('Migliorata')));
    }
    // 3. Voci standard italiane di sistema (iOS Alice/Federica/Luca/Paola e Android)
    if (!voice) {
      voice = voices.find(v => v.lang && (v.lang.toLowerCase() === 'it-it' || v.lang.toLowerCase() === 'it_it'));
    }
    // 4. Qualsiasi voce con prefisso it
    if (!voice) {
      voice = voices.find(v => v.lang && v.lang.toLowerCase().startsWith('it'));
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
        speakNextChunk();
      };

      utterance.onerror = (e) => {
        console.warn('TTS chunk avanza per errore/skip:', e);
        if (!ttsState.isSpeaking || ttsState.isPaused) return;
        ttsState.chunkIndex++;
        speakNextChunk();
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
    updateAudioBarUI('playing', chunks[0] || '');

    // Esegui la chiamata sincrona per non perdere il token di gesture utente nei browser mobile (iOS Safari / Android)
    speakNextChunk();
  }

  // ── Setup base per event listener condivisi ──

  function setupCoreEvents(getCurrentPdfChapters, renderSidebarFn, renderCurrentChapterFn, navigateFn) {
    // Sincronizzazione dinamica altezza sticky header per posizionamento preciso di sidebar e lettore vocale
    function syncStickyHeaderHeight() {
      const stickyHeader = document.querySelector('.study-sticky-header');
      if (stickyHeader) {
        const height = Math.round(stickyHeader.getBoundingClientRect().height);
        if (height > 0) {
          document.documentElement.style.setProperty('--sticky-header-height', `${height}px`);
        }
      }
    }

    syncStickyHeaderHeight();
    window.addEventListener('resize', syncStickyHeaderHeight, { passive: true });
    setupGlossaryPopover();
    if (typeof ResizeObserver !== 'undefined') {
      const stickyHeader = document.querySelector('.study-sticky-header');
      if (stickyHeader) {
        const ro = new ResizeObserver(() => syncStickyHeaderHeight());
        ro.observe(stickyHeader);
      }
    }

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
      if (e.key === THEME_KEY && e.newValue) {
        if (e.newValue !== state.theme) {
          applyTheme(e.newValue);
        }
      }
    });

    // Sidebar (desktop: collassabile; mobile: drawer)
    const sidebar = document.getElementById('sidebar');
    const sidebarCloseBtn = document.getElementById('btn-sidebar-close');
    const sidebarBackdrop = document.getElementById('sidebar-backdrop');
    const mobileDispenseModal = document.getElementById('mobile-dispense-overlay');
    const closeDispenseSheetBtn = document.getElementById('btn-close-dispense-sheet');

    function closeMobileSidebar() {
      if (sidebar) sidebar.classList.remove('mobile-open');
      if (sidebarBackdrop) sidebarBackdrop.classList.remove('active');
    }

    function openMobileSidebar() {
      if (sidebar) sidebar.classList.add('mobile-open');
      if (sidebarBackdrop) sidebarBackdrop.classList.add('active');
      if (mobileDispenseModal) mobileDispenseModal.classList.remove('active');
    }

    function openMobileDispense() {
      if (mobileDispenseModal) {
        populateMobileDispenseList();
        mobileDispenseModal.classList.add('active');
      }
      closeMobileSidebar();
    }

    function closeMobileDispense() {
      if (mobileDispenseModal) mobileDispenseModal.classList.remove('active');
    }

    function populateMobileDispenseList() {
      const listEl = document.getElementById('mobile-dispense-list');
      if (!listEl) return;
      listEl.innerHTML = '';
      const tabs = document.querySelectorAll('.pdf-tab');
      tabs.forEach(tab => {
        const key = tab.dataset.pdf;
        const title = tab.querySelector('.tab-title')?.textContent || key;
        const prog = tab.querySelector('.tab-progress-mini')?.textContent || '';
        const isActive = tab.classList.contains('active');

        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `mobile-dispense-item ${isActive ? 'active' : ''}`;
        btn.innerHTML = `
          <div class="mobile-dispense-item-left">
            <span class="mobile-dispense-dot"></span>
            <span class="mobile-dispense-item-title">${escapeHtml(title)}</span>
          </div>
          <span class="mobile-dispense-item-prog">${escapeHtml(prog)}</span>
        `;
        btn.addEventListener('click', () => {
          tab.click();
          closeMobileDispense();
        });
        listEl.appendChild(btn);
      });
    }

    const sidebarCollapseBtn = document.getElementById('btn-sidebar-collapse');
    const sidebarExpandBtn = document.getElementById('btn-sidebar-expand');

    if (sidebarCollapseBtn && sidebar) {
      sidebarCollapseBtn.addEventListener('click', () => {
        sidebar.classList.add('collapsed');
      });
    }

    if (sidebarExpandBtn && sidebar) {
      sidebarExpandBtn.addEventListener('click', () => {
        sidebar.classList.remove('collapsed');
      });
    }

    if (sidebarCloseBtn) sidebarCloseBtn.addEventListener('click', closeMobileSidebar);
    if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', () => {
      closeMobileSidebar();
      closeMobileDispense();
    });

    if (closeDispenseSheetBtn) closeDispenseSheetBtn.addEventListener('click', closeMobileDispense);
    if (mobileDispenseModal) {
      mobileDispenseModal.addEventListener('click', (e) => {
        if (e.target === mobileDispenseModal) closeMobileDispense();
      });
    }

    // Controlli menu mobile fisso in basso (Bottom Navigation Bar)
    const bottomChaptersBtn = document.getElementById('btn-bottom-chapters');
    const bottomDispenseBtn = document.getElementById('btn-bottom-dispense');
    const bottomMaterieBtn = document.getElementById('btn-bottom-materie');

    if (bottomChaptersBtn) {
      bottomChaptersBtn.addEventListener('click', () => {
        if (sidebar && sidebar.classList.contains('mobile-open')) {
          closeMobileSidebar();
        } else {
          openMobileSidebar();
        }
      });
    }

    if (bottomDispenseBtn) {
      bottomDispenseBtn.addEventListener('click', () => {
        if (mobileDispenseModal && mobileDispenseModal.classList.contains('active')) {
          closeMobileDispense();
        } else {
          openMobileDispense();
        }
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

    // Chapter navigation (collega sia i tasti superiori che inferiori)
    document.querySelectorAll('#btn-prev-chap, .btn-prev-chap').forEach(btn => {
      btn.addEventListener('click', () => {
        if (state.activeChapIndex > 0) navigateFn(state.activeChapIndex - 1);
      });
    });

    document.querySelectorAll('#btn-next-chap, .btn-next-chap').forEach(btn => {
      btn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        const currentChap = chaps[state.activeChapIndex];
        if (currentChap) {
          if (!state.completed[currentChap.id]) logActivity();
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
    });

    document.querySelectorAll('#btn-toggle-complete, .btn-toggle-complete').forEach(btn => {
      btn.addEventListener('click', () => {
        const chaps = getCurrentPdfChapters();
        const currentChap = chaps[state.activeChapIndex];
        if (currentChap) {
          const isCurrentlyDone = !!state.completed[currentChap.id];
          state.completed[currentChap.id] = !isCurrentlyDone;
          if (!isCurrentlyDone) logActivity();
          updateCompleteButtonState(!isCurrentlyDone);
          if (!isCurrentlyDone) document.querySelectorAll('.btn-toggle-complete').forEach(b => replayAnimation(b, 'anim-pop'));
          saveLocalState();
          renderSidebarFn();
        }
      });
    });

    // Pulsante Indietro desktop e tasto "Materie" mobile: tornano al corso/anno della materia
    const homeBtn = document.getElementById('btn-hub-nav');
    const hubHref = (homeBtn && homeBtn.dataset.href) || '../corsi.html';
    [homeBtn, bottomMaterieBtn].forEach(btn => {
      if (btn) btn.addEventListener('click', () => { window.location.href = hubHref; });
    });

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
      if ((img.src && img.src.includes('.svg')) || img.classList.contains('is-vector-diagram')) {
        lightbox.classList.add('is-svg');
      } else {
        lightbox.classList.remove('is-svg');
      }
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
    getCorrectIndex,
    buildFlashcard,
    getCardSrs,
    isCardDue,
    todayKey,
    logActivity,
    replayAnimation,
    stopSpeech,
    toggleSpeech
  };
})();
