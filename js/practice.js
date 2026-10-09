/**
 * Allenamento: ripasso a intervalli delle flashcard, simulazione dell'orale, progressi.
 * Vive dentro #view-exam (vista "Allenati"), accanto al simulatore d'esame di core.js.
 * Inizializzato da js/subject-app.js con StudyPractice.init({...}).
 * Dipende da: js/core.js (StudyCore).
 */
const StudyPractice = (function () {
  'use strict';

  const core = StudyCore;
  const state = core.state;
  const esc = core.escapeHtml;

  let ctx = null; // { subject, getModules, getCurrentPdfChapters, navigateTo }

  const SCOPES = [
    { value: 'chapter', label: 'Capitolo attuale' },
    { value: 'module', label: 'Modulo attivo' },
    { value: 'all', label: 'Tutta la materia' }
  ];

  const icon = (body, w = 16) =>
    `<svg width="${w}" height="${w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  const IC = {
    mic: icon('<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/>'),
    stop: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="5" y="5" width="14" height="14" rx="2"/></svg>',
    eye: icon('<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>'),
    next: icon('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>'),
    arrow: icon('<polyline points="9 18 15 12 9 6"/>', 14),
    clock: icon('<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>', 14)
  };

  // ── Raccolta dei contenuti per ambito ──

  function chaptersInScope(scope) {
    if (scope === 'chapter') {
      const chap = ctx.getCurrentPdfChapters()[state.activeChapIndex];
      return chap ? [chap] : [];
    }
    if (scope === 'module') return ctx.getCurrentPdfChapters();
    const seen = new Set();
    const all = [];
    ctx.getModules().forEach(m => m.chapters.forEach(c => {
      if (!seen.has(c.id)) { seen.add(c.id); all.push(c); }
    }));
    return all;
  }

  function cardsInScope(scope) {
    const cards = [];
    chaptersInScope(scope).forEach(chap => {
      (chap.flashcards || []).forEach((card, i) => cards.push({ card, chap, id: `${chap.id}-fc-${i}` }));
    });
    return cards;
  }

  function oralInScope(scope) {
    const items = [];
    chaptersInScope(scope).forEach(chap => {
      (chap.openQuestions || []).forEach((q, i) => {
        const item = typeof q === 'string' ? { question: q } : q;
        if (item && item.question) items.push({ ...item, chap, id: `${chap.id}-oq-${i}` });
      });
    });
    return items;
  }

  function scopeSelect(id, value) {
    return `
      <div class="select-wrapper">
        <select id="${id}" class="form-select">
          ${SCOPES.map(s => `<option value="${s.value}" ${s.value === value ? 'selected' : ''}>${s.label}</option>`).join('')}
        </select>
        <span class="select-chevron" aria-hidden="true">${icon('<polyline points="6 9 12 15 18 9"/>', 15)}</span>
      </div>`;
  }

  function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // ── Schede del pannello ──

  function switchPractice(name) {
    document.querySelectorAll('.practice-tab').forEach(t => t.classList.toggle('active', t.dataset.practice === name));
    document.querySelectorAll('.practice-panel').forEach(p => p.classList.toggle('active', p.id === `practice-panel-${name}`));
    if (name === 'review' && !reviewSession) renderReviewSetup();
    if (name === 'oral' && !oralSession) renderOralSetup();
    if (name === 'stats') renderStats();
    core.stopSpeech();
  }

  function updateDueBadge() {
    const badge = document.getElementById('review-due-badge');
    if (!badge) return;
    const due = cardsInScope('all').filter(c => core.isCardDue(c.id)).length;
    badge.hidden = due === 0;
    badge.textContent = due;
  }

  // ── Ripasso a intervalli ──

  let reviewScope = 'all';
  let reviewSession = null;

  function renderReviewSetup() {
    const root = document.getElementById('review-root');
    if (!root) return;
    const cards = cardsInScope(reviewScope);
    const due = cards.filter(c => core.isCardDue(c.id));
    const fresh = cards.filter(c => !core.getCardSrs(c.id));
    const learned = cards.filter(c => { const s = core.getCardSrs(c.id); return s && s.box >= 3; });

    root.innerHTML = `
      <div class="practice-card anim-enter">
        <div class="setup-group">
          <label for="review-scope">Ambito del ripasso:</label>
          ${scopeSelect('review-scope', reviewScope)}
        </div>
        <div class="practice-counters">
          <div class="practice-counter is-due"><strong>${due.length}</strong><span>da ripassare oggi</span></div>
          <div class="practice-counter"><strong>${fresh.length}</strong><span>mai viste</span></div>
          <div class="practice-counter is-good"><strong>${learned.length}</strong><span>memorizzate</span></div>
        </div>
        <div class="setup-group">
          <label>Schede nuove da aggiungere:</label>
          <div class="num-pills" id="review-new-pills">
            <button type="button" class="num-btn" data-new="0">Nessuna</button>
            <button type="button" class="num-btn active" data-new="10">10</button>
            <button type="button" class="num-btn" data-new="20">20</button>
          </div>
        </div>
        <button type="button" class="btn-primary-action" id="btn-start-review"></button>
        <p class="practice-note">Senza schede da ripassare né nuove, il ripasso di oggi è finito: torna domani.</p>
      </div>`;

    let newCount = 10;
    const startBtn = root.querySelector('#btn-start-review');
    const refreshBtn = () => {
      const total = due.length + Math.min(newCount, fresh.length);
      startBtn.textContent = total ? `Inizia il ripasso (${total} ${total === 1 ? 'scheda' : 'schede'})` : 'Niente da ripassare';
      startBtn.disabled = total === 0;
      root.querySelector('.practice-note').style.display = total ? 'none' : '';
    };
    root.querySelectorAll('#review-new-pills .num-btn').forEach(b => b.addEventListener('click', () => {
      root.querySelectorAll('#review-new-pills .num-btn').forEach(x => x.classList.toggle('active', x === b));
      newCount = parseInt(b.dataset.new, 10);
      refreshBtn();
    }));
    root.querySelector('#review-scope').addEventListener('change', e => { reviewScope = e.target.value; renderReviewSetup(); });
    startBtn.addEventListener('click', () => {
      const queue = shuffle(due.slice()).concat(shuffle(fresh.slice()).slice(0, newCount));
      reviewSession = { queue, index: 0, total: queue.length, grades: { again: 0, hard: 0, good: 0 }, requeued: new Set() };
      renderReviewCard();
    });
    refreshBtn();
  }

  function renderReviewCard() {
    const root = document.getElementById('review-root');
    const s = reviewSession;
    if (!s) return;
    if (s.index >= s.queue.length) return finishReview();
    const item = s.queue[s.index];
    const pct = Math.round((s.index / s.queue.length) * 100);

    root.innerHTML = `
      <div class="practice-session-bar">
        <span>Scheda ${s.index + 1} di ${s.queue.length}</span>
        <button type="button" class="btn-secondary-link" id="btn-end-review">Termina</button>
      </div>
      <div class="exam-progress-track"><div class="exam-progress-fill" style="width:${pct}%"></div></div>
      <p class="practice-source">${esc(item.chap.title)}</p>
      <div class="review-card-slot"></div>`;
    const cardEl = core.buildFlashcard(item.card, item.id, grade => {
      s.grades[grade]++;
      // Una scheda sbagliata torna una volta in fondo alla sessione
      if (grade === 'again' && !s.requeued.has(item.id)) {
        s.requeued.add(item.id);
        s.queue.push(item);
      }
      updateDueBadge();
      setTimeout(() => { s.index++; renderReviewCard(); }, 380);
    });
    cardEl.classList.add('anim-enter');
    root.querySelector('.review-card-slot').appendChild(cardEl);
    root.querySelector('#btn-end-review').addEventListener('click', finishReview);
  }

  function finishReview() {
    const root = document.getElementById('review-root');
    const s = reviewSession;
    reviewSession = null;
    if (!s) return renderReviewSetup();
    const done = s.grades.again + s.grades.hard + s.grades.good;
    root.innerHTML = `
      <div class="practice-card anim-enter">
        <h3 class="practice-result-title">Ripasso concluso: ${done} ${done === 1 ? 'scheda' : 'schede'}</h3>
        <div class="practice-counters">
          <div class="practice-counter is-good"><strong>${s.grades.good}</strong><span>sapevi</span></div>
          <div class="practice-counter"><strong>${s.grades.hard}</strong><span>incerte</span></div>
          <div class="practice-counter is-due"><strong>${s.grades.again}</strong><span>da rivedere</span></div>
        </div>
        <button type="button" class="btn-primary-action" id="btn-review-back">Torna al ripasso</button>
      </div>`;
    root.querySelector('#btn-review-back').addEventListener('click', renderReviewSetup);
    updateDueBadge();
  }

  // ── Simulazione dell'orale ──

  let oralScope = 'module';
  let oralSession = null;
  let recognition = null;
  let timerId = null;

  const RATINGS = {
    ok: { label: 'Risposta completa', cls: 'grade-good' },
    partial: { label: 'Parziale', cls: 'grade-hard' },
    review: { label: 'Da ripassare', cls: 'grade-again' }
  };

  function getRecognitionCtor() {
    return window.SpeechRecognition || window.webkitSpeechRecognition || null;
  }

  function stopRecording() {
    if (recognition) {
      try { recognition.stop(); } catch (e) { /* già fermo */ }
      recognition = null;
    }
  }

  function stopTimer() {
    clearInterval(timerId);
    timerId = null;
  }

  function renderOralSetup() {
    stopRecording();
    stopTimer();
    const root = document.getElementById('oral-root');
    if (!root) return;
    const items = oralInScope(oralScope);
    const rated = items.filter(i => state.oralLog[i.id]);
    const ok = rated.filter(i => state.oralLog[i.id].r === 'ok').length;

    root.innerHTML = `
      <div class="practice-card anim-enter">
        <div class="setup-group">
          <label for="oral-scope">Ambito delle domande:</label>
          ${scopeSelect('oral-scope', oralScope)}
        </div>
        <div class="practice-counters">
          <div class="practice-counter"><strong>${items.length}</strong><span>domande disponibili</span></div>
          <div class="practice-counter"><strong>${items.length - rated.length}</strong><span>mai provate</span></div>
          <div class="practice-counter is-good"><strong>${ok}</strong><span>risposte complete</span></div>
        </div>
        <button type="button" class="btn-primary-action" id="btn-start-oral" ${items.length ? '' : 'disabled'}>
          ${items.length ? 'Inizia la simulazione' : 'Nessuna domanda da orale in questo ambito'}
        </button>
        <p class="practice-note">Le domande mai provate e quelle da ripassare vengono proposte per prime.</p>
      </div>`;
    root.querySelector('#oral-scope').addEventListener('change', e => { oralScope = e.target.value; renderOralSetup(); });
    root.querySelector('#btn-start-oral').addEventListener('click', () => startOral(oralScope));
  }

  function startOral(scope) {
    const priority = { undefined: 0, review: 1, partial: 2, ok: 3 };
    const items = shuffle(oralInScope(scope)).sort((a, b) =>
      priority[(state.oralLog[a.id] || {}).r] - priority[(state.oralLog[b.id] || {}).r]);
    if (!items.length) return renderOralSetup();
    oralSession = { items, index: 0, results: { ok: 0, partial: 0, review: 0 } };
    renderOralQuestion();
  }

  // Concetti chiave da citare, ricavati dalla traccia di risposta (o dai punti chiave del capitolo):
  // grassetti e corsivi (termini e titoli), nomi propri e date. Si escludono quelli già nella domanda.
  const NAME_STOP = new Set(['Il', 'Lo', 'La', 'Le', 'Gli', 'I', 'Un', 'Una', 'Uno', 'In', 'Nel', 'Nella', 'Per', 'Con', 'Da', 'Dal', 'Dalla', 'Di', 'Del', 'Della', 'E', 'Ma', 'Se', 'Si', 'Non', 'Come', 'Questo', 'Questa', 'Secondo', 'Mentre', 'Anche', 'Ogni', 'Tra', 'Fra', 'Dopo', 'Prima', 'Infine', 'Inoltre', 'Infatti', 'Quando', 'Cosa', 'Che', 'Al', 'Alla', 'Sul', 'Sulla', 'Ciò', 'Sono', 'È']);

  function extractConcepts(item) {
    const source = item.modelAnswer || (item.chap.keyPoints || []).join('. ');
    const question = normalize(item.question);
    const found = [];
    const add = t => {
      t = t.trim().replace(/[.,;:]+$/, '');
      if (t.length < 3 || t.length > 60) return;
      if (question.includes(normalize(t).trim())) return;
      if (!found.some(f => normalize(f) === normalize(t))) found.push(t);
    };
    let m;
    const reMarked = /\*{1,2}([^*]{2,60})\*{1,2}/g;
    while ((m = reMarked.exec(source))) add(m[1]);
    const plain = source.replace(/\*+/g, '');
    const reYear = /\b(1[0-9]{3}|20[0-9]{2})\b/g;
    while ((m = reYear.exec(plain))) add(m[1]);
    // Sequenze di parole con la maiuscola non a inizio frase (es. "Jasper Johns", "Leo Castelli")
    const reName = /(^|[^.!?:\s]\s+)((?:[A-ZÀ-Ý][\p{L}'’-]+)(?:\s+(?:de|di|da|van|von|del|della|e)?\s*[A-ZÀ-Ý][\p{L}'’-]+){0,3})/gu;
    while ((m = reName.exec(plain))) {
      const name = m[2].split(/\s+/).filter(w => !NAME_STOP.has(w)).join(' ');
      if (name && /[A-ZÀ-Ý]/.test(name[0])) add(name);
    }
    return found.slice(0, 10);
  }

  function normalize(t) {
    return t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9 ]/g, ' ');
  }

  // Un concetto è citato se nella trascrizione compare almeno metà delle sue parole significative
  function isConceptMentioned(concept, transcript) {
    const words = normalize(concept).split(/\s+/).filter(w => w.length > 3);
    if (!words.length) return normalize(transcript).includes(normalize(concept).trim());
    const t = ' ' + normalize(transcript) + ' ';
    const hits = words.filter(w => t.includes(w.slice(0, Math.max(4, w.length - 2)))).length;
    return hits >= Math.ceil(words.length / 2);
  }

  function renderOralQuestion() {
    stopRecording();
    stopTimer();
    const root = document.getElementById('oral-root');
    const s = oralSession;
    if (!s) return;
    if (s.index >= s.items.length) return finishOral();
    const item = s.items[s.index];
    const Ctor = getRecognitionCtor();
    let transcript = '';
    let seconds = 0;

    root.innerHTML = `
      <div class="practice-session-bar">
        <span>Domanda ${s.index + 1} di ${s.items.length}</span>
        <button type="button" class="btn-secondary-link" id="btn-end-oral">Termina</button>
      </div>
      <div class="oral-card anim-enter">
        <p class="practice-source">Capitolo ${esc(String(item.chap.number))}: ${esc(item.chap.title)}</p>
        <h3 class="oral-question">${esc(item.question)}</h3>
        <div class="oral-toolbar">
          <span class="oral-timer" id="oral-timer">${IC.clock} 0:00</span>
          ${Ctor ? `<button type="button" class="btn-secondary-action" id="btn-oral-rec">${IC.mic} Registra la risposta</button>` : ''}
          <button type="button" class="btn-primary-action" id="btn-oral-reveal">${IC.eye} Mostra la traccia</button>
        </div>
        ${Ctor
          ? '<p class="practice-note">La registrazione trascrive la tua risposta con il riconoscimento vocale del browser e segnala quali nomi, date e termini della traccia hai citato.</p><div class="oral-transcript" id="oral-transcript" hidden></div>'
          : '<p class="practice-note">Rispondi ad alta voce come all\'esame, poi apri la traccia e confronta. (Il riconoscimento vocale non è disponibile in questo browser.)</p>'}
        <div class="oral-answer" id="oral-answer" hidden></div>
      </div>`;

    const timerEl = root.querySelector('#oral-timer');
    timerId = setInterval(() => {
      seconds++;
      timerEl.innerHTML = `${IC.clock} ${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`;
    }, 1000);

    root.querySelector('#btn-end-oral').addEventListener('click', finishOral);

    const recBtn = root.querySelector('#btn-oral-rec');
    const trEl = root.querySelector('#oral-transcript');
    if (recBtn) {
      recBtn.addEventListener('click', () => {
        if (recognition) {
          stopRecording();
          recBtn.classList.remove('is-recording');
          recBtn.innerHTML = `${IC.mic} Riprendi la registrazione`;
          return;
        }
        recognition = new Ctor();
        recognition.lang = 'it-IT';
        recognition.continuous = true;
        recognition.interimResults = true;
        let finalText = transcript;
        recognition.onresult = (e) => {
          let interim = '';
          for (let i = e.resultIndex; i < e.results.length; i++) {
            if (e.results[i].isFinal) finalText += e.results[i][0].transcript + ' ';
            else interim += e.results[i][0].transcript;
          }
          transcript = finalText;
          trEl.hidden = false;
          trEl.innerHTML = `${esc(finalText)}<span class="oral-interim">${esc(interim)}</span>`;
        };
        recognition.onerror = () => {
          trEl.hidden = false;
          trEl.textContent = transcript || 'Non è stato possibile usare il microfono: controlla i permessi del browser.';
        };
        recognition.onend = () => {
          if (recognition) { recognition = null; recBtn.classList.remove('is-recording'); recBtn.innerHTML = `${IC.mic} Riprendi la registrazione`; }
        };
        try {
          recognition.start();
          recBtn.classList.add('is-recording');
          recBtn.innerHTML = `${IC.stop} Ferma la registrazione`;
        } catch (e) {
          recognition = null;
        }
      });
    }

    root.querySelector('#btn-oral-reveal').addEventListener('click', (e) => {
      stopRecording();
      stopTimer();
      e.currentTarget.disabled = true;
      if (recBtn) recBtn.disabled = true;
      const ans = root.querySelector('#oral-answer');
      const concepts = extractConcepts(item);
      const keyPoints = item.chap.keyPoints || [];
      let conceptsHtml = '';
      if (concepts.length) {
        const chips = concepts.map(c => {
          const hit = transcript && isConceptMentioned(c, transcript);
          return `<span class="concept-chip ${transcript ? (hit ? 'is-hit' : 'is-miss') : ''}">${esc(c)}</span>`;
        }).join('');
        const hits = transcript ? concepts.filter(c => isConceptMentioned(c, transcript)).length : 0;
        conceptsHtml = `
          <h4>${transcript
            ? `Nomi, date e termini citati: ${hits} su ${concepts.length}`
            : (item.modelAnswer ? 'Nomi, date e termini della traccia' : 'Nomi, date e termini del capitolo')}</h4>
          <div class="concept-chips">${chips}</div>`;
      }
      ans.innerHTML = `
        ${conceptsHtml}
        ${item.modelAnswer ? `<h4>Traccia di risposta</h4><div class="oral-model">${core.formatMarkdown(item.modelAnswer)}</div>` : ''}
        ${keyPoints.length ? `<h4>Punti chiave del capitolo</h4><ul class="study-list">${keyPoints.map(k => `<li>${esc(k)}</li>`).join('')}</ul>` : ''}
        <h4>Come è andata?</h4>
        <div class="flashcard-grades oral-ratings">
          ${Object.entries(RATINGS).map(([k, r]) => `<button type="button" class="btn-grade ${r.cls}" data-r="${k}">${r.label}</button>`).join('')}
        </div>`;
      ans.hidden = false;
      ans.classList.add('anim-enter');
      ans.querySelectorAll('.btn-grade').forEach(b => b.addEventListener('click', () => {
        state.oralLog[item.id] = { r: b.dataset.r, date: core.todayKey(), seconds };
        s.results[b.dataset.r]++;
        core.logActivity();
        core.saveLocalState();
        s.index++;
        renderOralQuestion();
      }));
    });
  }

  function finishOral() {
    stopRecording();
    stopTimer();
    const s = oralSession;
    oralSession = null;
    if (!s) return renderOralSetup();
    const root = document.getElementById('oral-root');
    const done = s.results.ok + s.results.partial + s.results.review;
    root.innerHTML = `
      <div class="practice-card anim-enter">
        <h3 class="practice-result-title">Simulazione conclusa: ${done} ${done === 1 ? 'domanda' : 'domande'}</h3>
        <div class="practice-counters">
          <div class="practice-counter is-good"><strong>${s.results.ok}</strong><span>complete</span></div>
          <div class="practice-counter"><strong>${s.results.partial}</strong><span>parziali</span></div>
          <div class="practice-counter is-due"><strong>${s.results.review}</strong><span>da ripassare</span></div>
        </div>
        <button type="button" class="btn-primary-action" id="btn-oral-back">Nuova simulazione</button>
      </div>`;
    root.querySelector('#btn-oral-back').addEventListener('click', renderOralSetup);
  }

  // ── Progressi ──

  function computeStreak() {
    const d = new Date();
    if (!state.activity[core.todayKey(d)]) d.setDate(d.getDate() - 1);
    let n = 0;
    while (state.activity[core.todayKey(d)]) {
      n++;
      d.setDate(d.getDate() - 1);
    }
    return n;
  }

  function chapterStats(chap) {
    const quiz = chap.quiz || [];
    let answered = 0;
    let correct = 0;
    quiz.forEach((q, i) => {
      const a = state.quizAnswers[`${chap.id}-quiz-${i}`];
      if (a) {
        answered++;
        if (a.selectedIndex === core.getCorrectIndex(q)) correct++;
      }
    });
    const cards = (chap.flashcards || []).map((_, i) => core.getCardSrs(`${chap.id}-fc-${i}`));
    return {
      answered, correct, quizTotal: quiz.length,
      cardsTotal: cards.length,
      cardsLearned: cards.filter(c => c && c.box >= 3).length,
      cardsSeen: cards.filter(Boolean).length
    };
  }

  function pct(a, b) {
    return b > 0 ? Math.round((a / b) * 100) : 0;
  }

  function renderStats() {
    const root = document.getElementById('stats-root');
    if (!root) return;
    const modules = ctx.getModules();
    const allChaps = chaptersInScope('all');
    const tot = allChaps.reduce((acc, c) => {
      const st = chapterStats(c);
      acc.done += state.completed[c.id] ? 1 : 0;
      acc.answered += st.answered; acc.correct += st.correct;
      acc.cards += st.cardsTotal; acc.learned += st.cardsLearned;
      return acc;
    }, { done: 0, answered: 0, correct: 0, cards: 0, learned: 0 });
    const due = cardsInScope('all').filter(c => core.isCardDue(c.id)).length;
    const oral = oralInScope('all');
    const oralRated = oral.filter(o => state.oralLog[o.id]);
    const streak = computeStreak();

    // Ultime 5 settimane di attività (tutte le materie)
    const days = [];
    const d = new Date();
    d.setDate(d.getDate() - 34);
    for (let i = 0; i < 35; i++) {
      const k = core.todayKey(d);
      const n = state.activity[k] || 0;
      days.push(`<span class="activity-cell lvl-${n === 0 ? 0 : n < 5 ? 1 : n < 15 ? 2 : 3}" title="${k}: ${n} attività"></span>`);
      d.setDate(d.getDate() + 1);
    }

    const moduleRows = modules.map(m => {
      const s = m.chapters.reduce((acc, c) => {
        const st = chapterStats(c);
        acc.done += state.completed[c.id] ? 1 : 0;
        acc.answered += st.answered; acc.correct += st.correct;
        acc.cards += st.cardsTotal; acc.learned += st.cardsLearned;
        return acc;
      }, { done: 0, answered: 0, correct: 0, cards: 0, learned: 0 });
      const p = pct(s.done, m.chapters.length);
      return `
        <div class="stats-module-row">
          <div class="stats-module-name">${esc(m.label)}</div>
          <div class="stats-bar"><div class="stats-bar-fill" style="--w:${p}%"></div></div>
          <div class="stats-module-nums">
            <span>${s.done}/${m.chapters.length} capitoli</span>
            <span>${s.answered ? pct(s.correct, s.answered) + '% quiz corretti' : 'quiz non iniziati'}</span>
            <span>${s.learned}/${s.cards} schede memorizzate</span>
          </div>
        </div>`;
    }).join('');

    // Capitoli da rinforzare: quiz sotto il 70% o domande d'orale da ripassare
    const weak = [];
    modules.forEach(m => m.chapters.forEach((c, idx) => {
      const st = chapterStats(c);
      const oralBad = (c.openQuestions || []).some((_, i) => (state.oralLog[`${c.id}-oq-${i}`] || {}).r === 'review');
      const acc = st.answered >= 2 ? st.correct / st.answered : 1;
      if (acc < 0.7 || oralBad) {
        if (!weak.some(w => w.chap.id === c.id)) weak.push({ chap: c, key: m.key, idx, acc, st, oralBad });
      }
    }));
    weak.sort((a, b) => a.acc - b.acc);

    const history = state.examHistory.filter(h => h.subject === state.currentSubject).slice(-5).reverse();

    root.innerHTML = `
      <div class="stats-tiles anim-enter">
        <div class="stats-tile"><strong>${tot.done}<small>/${allChaps.length}</small></strong><span>capitoli completati</span></div>
        <div class="stats-tile"><strong>${tot.answered ? pct(tot.correct, tot.answered) + '%' : '-'}</strong><span>quiz corretti (${tot.correct} su ${tot.answered})</span></div>
        <div class="stats-tile"><strong>${tot.learned}<small>/${tot.cards}</small></strong><span>flashcard memorizzate${due ? `, ${due} da ripassare oggi` : ''}</span></div>
        <div class="stats-tile"><strong>${oralRated.length}<small>/${oral.length}</small></strong><span>domande d'orale provate</span></div>
        <div class="stats-tile is-accent"><strong>${streak}</strong><span>${streak === 1 ? 'giorno' : 'giorni'} di studio di fila</span></div>
      </div>

      <div class="stats-section">
        <h3>Attività delle ultime cinque settimane</h3>
        <div class="activity-grid">${days.join('')}</div>
        <p class="practice-note">Ogni quadrato è un giorno: più è scuro, più attività (capitoli, quiz, schede, domande) hai svolto in tutte le materie.</p>
      </div>

      <div class="stats-section">
        <h3>Avanzamento per modulo</h3>
        ${moduleRows}
      </div>

      <div class="stats-section">
        <h3>Da rinforzare</h3>
        ${weak.length ? `<div class="stats-weak-list">${weak.slice(0, 6).map((w, i) => `
          <button type="button" class="stats-weak-item" data-i="${i}">
            <span class="stats-weak-title">Capitolo ${esc(String(w.chap.number))}: ${esc(w.chap.title)}</span>
            <span class="stats-weak-meta">${w.st.answered >= 2 ? `quiz ${w.st.correct}/${w.st.answered}` : ''}${w.oralBad ? `${w.st.answered >= 2 ? ', ' : ''}orale da ripassare` : ''}</span>
            ${IC.arrow}
          </button>`).join('')}</div>`
          : '<p class="practice-note">Nessun capitolo critico per ora. I capitoli compaiono qui quando sbagli più del 30% dei quiz o segni una domanda d\'orale da ripassare.</p>'}
      </div>

      <div class="stats-section">
        <h3>Ultime simulazioni d'esame</h3>
        ${history.length ? `<div class="stats-history">${history.map(h => `
          <div class="stats-history-row">
            <span>${esc(h.date.split('-').reverse().join('/'))}</span>
            <span class="stats-history-scope">${esc(h.scope || '')}</span>
            <strong class="${h.grade >= 18 ? 'is-pass' : 'is-fail'}">${h.grade}/30</strong>
          </div>`).join('')}</div>`
          : '<p class="practice-note">Non hai ancora svolto simulazioni in questa materia.</p>'}
      </div>`;

    root.querySelectorAll('.stats-weak-item').forEach(b => b.addEventListener('click', () => {
      const w = weak[parseInt(b.dataset.i, 10)];
      ctx.navigateTo(w.key, w.idx);
    }));
    // Le barre partono da zero e si riempiono (animazione)
    requestAnimationFrame(() => root.querySelectorAll('.stats-bar-fill').forEach(el => el.classList.add('is-filled')));
  }

  // ── Avvio ──

  function init(options) {
    ctx = options;
    document.querySelectorAll('.practice-tab').forEach(t => t.addEventListener('click', () => switchPractice(t.dataset.practice)));

    const oralBtn = document.getElementById('btn-oral-chapter');
    if (oralBtn) {
      oralBtn.addEventListener('click', () => {
        core.switchView('exam');
        oralScope = 'chapter';
        switchPractice('oral');
        startOral('chapter');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Aggiorna il conteggio delle schede da ripassare quando si valutano dal capitolo
    document.addEventListener('click', (e) => {
      if (e.target.closest('.btn-grade')) setTimeout(updateDueBadge, 0);
    });
    document.querySelectorAll('.pill-btn').forEach(btn => btn.addEventListener('click', () => {
      if (btn.dataset.view !== 'exam') { stopRecording(); stopTimer(); }
      const active = document.querySelector('.practice-tab.active');
      if (btn.dataset.view === 'exam' && active && active.dataset.practice === 'stats') renderStats();
    }));
    // Dopo la sincronizzazione con l'account: aggiorna badge e progressi se visibili
    window.addEventListener('study:progress-synced', () => {
      updateDueBadge();
      const active = document.querySelector('.practice-tab.active');
      if (core.state.activeView === 'exam' && active && active.dataset.practice === 'stats') renderStats();
    });
    updateDueBadge();
  }

  return { init, switchPractice, updateDueBadge };
})();
