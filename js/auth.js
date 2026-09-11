/**
 * js/auth.js — Autenticazione e Sincronizzazione con Supabase
 * Piattaforma Didattica Studio — ABA Catania
 */

(function () {
  'use strict';

  // Cattura l'hash e i parametri URL all'avvio prima che Supabase possa pulirli
  const initialHash = window.location.hash || '';
  const initialSearch = window.location.search || '';

  // -- Configurazione Supabase --
  const SUPABASE_URL = 'https://ivpctopxkvkcdvwbccml.supabase.co';
  const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml2cGN0b3B4a3ZrY2R2d2JjY21sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODkwNDk1MzIsImV4cCI6MjEwNDYyNTUzMn0.acJDqcShn5pdbRglReXQEgRK-VUTiOylDzi46psKFfQ';
  const LOCAL_STORAGE_KEY = 'ux_web_study_state_v1';

  let supabase = null;
  let currentUser = null;
  let realtimeChannel = null;
  let isSyncing = false;
  let syncDebounceTimer = null;
  let toastTimer = null;

  // Inizializza il client Supabase
  function initSupabase() {
    if (window.supabase && typeof window.supabase.createClient === 'function') {
      supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      window.appSupabase = supabase;
      return true;
    }
    console.warn('Libreria Supabase non trovata.');
    return false;
  }

  // Restituisce l'URL corrente pulito dall'hash per il redirect Supabase
  function getRedirectUrl() {
    try {
      const url = new URL(window.location.href);
      url.hash = '';
      return url.origin + url.pathname;
    } catch (e) {
      return window.location.href.split('#')[0].split('?')[0];
    }
  }

  // -- Metodi di Autenticazione --

  async function signUp(email, password, displayName) {
    if (!supabase) return { error: { message: 'Client Supabase non inizializzato' } };
    const redirectTo = getRedirectUrl();
    const { data, error } = await supabase.auth.signUp({
      email: email.trim(),
      password: password,
      options: {
        emailRedirectTo: redirectTo,
        data: {
          display_name: displayName || email.split('@')[0]
        }
      }
    });
    return { data, error };
  }

  async function signIn(email, password) {
    if (!supabase) return { error: { message: 'Client Supabase non inizializzato' } };
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.trim(),
      password: password
    });
    return { data, error };
  }

  async function signOut() {
    if (supabase) {
      try {
        await supabase.auth.signOut();
      } catch (e) {
        console.warn('Errore durante la disconnessione Supabase:', e);
      }
    }
    currentUser = null;

    // Rimuovi progressi locali e token Supabase
    try {
      localStorage.removeItem(LOCAL_STORAGE_KEY);
      localStorage.removeItem('aba_studio_state_v2');
      Object.keys(localStorage).forEach(k => {
        if (k.startsWith('sb-') && k.endsWith('-auth-token')) {
          localStorage.removeItem(k);
        }
      });
    } catch (e) {}

    // Resetta lo stato in memoria se StudyCore e' disponibile
    if (window.StudyCore && window.StudyCore.state) {
      window.StudyCore.state.completed = {};
      window.StudyCore.state.quizAnswers = {};
      window.StudyCore.state.flashcardStatus = {};
    }

    // Ricarica la pagina per azzerare completamente il DOM e mostrare il login wall
    window.location.reload();
  }

  async function resetPassword(email) {
    if (!supabase) return { error: { message: 'Client non inizializzato' } };
    const redirectTo = getRedirectUrl();
    const { data, error } = await supabase.auth.resetPasswordForEmail(email.trim(), {
      redirectTo: redirectTo
    });
    return { data, error };
  }

  async function updateUserPassword(newPassword) {
    if (!supabase) return { error: { message: 'Client Supabase non inizializzato' } };
    const { data, error } = await supabase.auth.updateUser({
      password: newPassword
    });
    return { data, error };
  }

  // -- Sincronizzazione Database & Realtime Multi-Device --

  async function fetchCloudProgress(userId) {
    if (!supabase || !userId) return [];
    try {
      const { data, error } = await supabase
        .from('user_progress')
        .select('*')
        .eq('user_id', userId);

      if (error) {
        console.warn('Errore lettura progressi da Supabase:', error);
        return [];
      }
      return data || [];
    } catch (e) {
      console.warn('Errore di rete durante lettura progressi:', e);
      return [];
    }
  }

  // Sincronizzazione intelligente bidirezionale (Merge Locale <-> Cloud)
  async function syncCloudProgress(user, silent = false) {
    if (!user || !supabase || isSyncing) return;
    isSyncing = true;

    try {
      // 1. Recupera stato locale attuale
      let localCompleted = {};
      if (window.StudyCore && window.StudyCore.state && window.StudyCore.state.completed) {
        localCompleted = { ...window.StudyCore.state.completed };
      }
      try {
        const saved = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY) || '{}');
        if (saved && saved.completed) {
          localCompleted = { ...saved.completed, ...localCompleted };
        }
      } catch (e) {}

      // 2. Scarica progressi completi salvati nel cloud
      const cloudRows = await fetchCloudProgress(user.id);
      const cloudMap = {};
      cloudRows.forEach(row => {
        cloudMap[row.chapter_id] = row.completed;
      });

      // 3. MERGE: qualsiasi capitolo completato in locale o su cloud viene preservato
      const mergedCompleted = { ...cloudMap, ...localCompleted };

      // 4. Identifica i capitoli presenti in locale ma mancanti o diversi sul cloud
      const rowsToUpload = [];
      Object.entries(mergedCompleted).forEach(([chapId, isDone]) => {
        if (isDone && cloudMap[chapId] !== true) {
          rowsToUpload.push({
            user_id: user.id,
            subject: chapId.startsWith('arte-') ? 'arte' : 'ux',
            chapter_id: chapId,
            completed: true,
            updated_at: new Date().toISOString()
          });
        }
      });

      // 5. Se ci sono progressi locali non ancora su Supabase, caricali in BATCH istantaneo
      if (rowsToUpload.length > 0) {
        const { error } = await supabase
          .from('user_progress')
          .upsert(rowsToUpload, { onConflict: 'user_id,subject,chapter_id' });

        if (error) {
          console.warn('[Cloud Sync] Errore upload batch:', error);
        } else {
          console.log(`[Cloud Sync] ${rowsToUpload.length} capitoli caricati con successo nel cloud`);
        }
      }

      // 6. Aggiorna SEMPRE localStorage (fondamentale per index.html e funzionamento offline)
      try {
        let saved = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY) || '{}');
        saved.completed = mergedCompleted;
        localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(saved));
      } catch (e) {}

      // 7. Aggiorna StudyCore in memoria se ci troviamo in una pagina di studio
      if (window.StudyCore && window.StudyCore.state) {
        window.StudyCore.state.completed = mergedCompleted;
      }

      // 8. Aggiorna l'interfaccia utente grafica su tutta la pagina
      triggerUIProgressRefresh(mergedCompleted);

      // 9. Attiva canale Realtime per ascoltare modifiche da altri dispositivi
      setupRealtimeSubscription(user.id);
    } catch (err) {
      console.warn('[Cloud Sync] Errore durante la sincronizzazione:', err);
    } finally {
      isSyncing = false;
    }
  }

  // Notifica UI e componenti grafici di studio o home
  function triggerUIProgressRefresh(completedMap) {
    if (typeof window.updateProgressIndicators === 'function') {
      window.updateProgressIndicators();
    }
    if (typeof window.doRenderSidebar === 'function') {
      window.doRenderSidebar();
    }
    if (typeof window.doRenderChapter === 'function') {
      window.doRenderChapter();
    }
    if (window.StudyCore && typeof window.StudyCore.updateCompleteButtonState === 'function') {
      const chaps = (typeof window.getCurrentPdfChapters === 'function') ? window.getCurrentPdfChapters() : [];
      const currentChap = chaps[window.StudyCore.state.activeChapIndex];
      if (currentChap) {
        window.StudyCore.updateCompleteButtonState(!!completedMap[currentChap.id]);
      }
    }
    // Evento globale personalizzato per la Home (index.html) e altri listener
    window.dispatchEvent(new CustomEvent('study:progress-synced', { detail: { completed: completedMap } }));
  }

  // Canale Realtime Supabase (Postgres Changes + Broadcast per sincronizzazione immediata PC <-> Telefono)
  function setupRealtimeSubscription(userId) {
    if (!supabase || !userId) return;
    if (realtimeChannel) {
      try { supabase.removeChannel(realtimeChannel); } catch (e) {}
    }

    realtimeChannel = supabase.channel('user_sync_' + userId, {
      config: { broadcast: { self: false } }
    });

    // 1. Messaggi Broadcast peer-to-peer istantanei (latenza 30-80ms via WebSocket)
    realtimeChannel.on('broadcast', { event: 'progress_sync' }, (data) => {
      console.log('[Realtime Broadcast] Ricevuto progresso da altro dispositivo:', data);
      if (data && data.payload && data.payload.completed) {
        applyRemoteProgressUpdate(data.payload.completed);
      }
    });

    // 2. Modifiche Postgres Database (quando il database scrive le righe)
    realtimeChannel.on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'user_progress',
        filter: `user_id=eq.${userId}`
      },
      (payload) => {
        console.log('[Realtime Postgres] Modifica riga ricevuta:', payload);
        const row = payload.new;
        if (row && row.chapter_id) {
          applyRemoteProgressUpdate({ [row.chapter_id]: row.completed });
        }
      }
    );

    realtimeChannel.subscribe((status) => {
      console.log('[Realtime] Stato canale WebSocket:', status);
    });
  }

  // Applica progressi ricevuti in tempo reale da un altro dispositivo
  function applyRemoteProgressUpdate(incomingMap) {
    let currentMap = {};
    if (window.StudyCore && window.StudyCore.state && window.StudyCore.state.completed) {
      currentMap = window.StudyCore.state.completed;
    } else {
      try {
        const saved = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY) || '{}');
        currentMap = saved.completed || {};
      } catch (e) {}
    }

    const merged = { ...currentMap, ...incomingMap };

    try {
      let saved = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY) || '{}');
      saved.completed = merged;
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(saved));
    } catch (e) {}

    if (window.StudyCore && window.StudyCore.state) {
      window.StudyCore.state.completed = merged;
    }

    triggerUIProgressRefresh(merged);
  }

  // Hook chiamato da core.js quando l'utente modifica lo stato di un capitolo
  function onStateSaved(payload) {
    if (!currentUser || !supabase || isSyncing) return;

    if (syncDebounceTimer) clearTimeout(syncDebounceTimer);
    syncDebounceTimer = setTimeout(async () => {
      const completedMap = payload.completed || {};

      // 1. Invio Broadcast immediato a tutti gli altri dispositivi collegati (es. telefono)
      if (realtimeChannel) {
        try {
          realtimeChannel.send({
            type: 'broadcast',
            event: 'progress_sync',
            payload: { completed: completedMap }
          });
        } catch (e) {}
      }

      // 2. Salvataggio batch nel database Supabase
      const rows = Object.entries(completedMap).map(([chapId, isDone]) => ({
        user_id: currentUser.id,
        subject: chapId.startsWith('arte-') ? 'arte' : 'ux',
        chapter_id: chapId,
        completed: !!isDone,
        updated_at: new Date().toISOString()
      }));

      if (rows.length === 0) return;

      try {
        const { error } = await supabase
          .from('user_progress')
          .upsert(rows, { onConflict: 'user_id,subject,chapter_id' });

        if (error) {
          console.warn('[Cloud Sync] Errore salvataggio progresso:', error);
        }
      } catch (e) {
        console.warn('[Cloud Sync] Errore di rete:', e);
      }
    }, 250);
  }

  function removeLoginWall() {
    const wall = document.getElementById('auth-login-wall');
    if (wall) wall.remove();
  }

  // -- Gestione Redirect e Token URL --

  function cleanAuthUrl() {
    try {
      if (window.history && window.history.replaceState) {
        const url = new URL(window.location.href);
        url.hash = '';
        url.searchParams.delete('type');
        url.searchParams.delete('error');
        url.searchParams.delete('error_code');
        url.searchParams.delete('error_description');
        url.searchParams.delete('auth_confirmed');
        const cleanSearch = url.searchParams.toString();
        const finalUrl = url.pathname + (cleanSearch ? '?' + cleanSearch : '');
        window.history.replaceState(null, document.title, finalUrl);
      }
    } catch (e) {
      console.warn('Impossibile pulire i parametri URL:', e);
    }
  }

  function handleUrlRedirectEvents() {
    // 1. Controllo errori nel link ricevuto via mail (es. link scaduto o già usato)
    if (initialHash.includes('error=') || initialSearch.includes('error=')) {
      const fullParams = new URLSearchParams(initialHash.startsWith('#') ? initialHash.slice(1) : initialSearch);
      const desc = fullParams.get('error_description') || 'Il link email non è valido o è scaduto.';
      cleanAuthUrl();
      setTimeout(() => {
        showToast(desc.replace(/\+/g, ' '), 'error', 6500);
      }, 500);
      return;
    }

    // 2. Controllo conferma iscrizione (type=signup)
    if (initialHash.includes('type=signup') || initialSearch.includes('type=signup') || initialSearch.includes('auth_confirmed=true')) {
      setTimeout(() => {
        showToast('Email confermata con successo. Il tuo account è attivo.', 'success', 6000);
        cleanAuthUrl();
      }, 600);
      return;
    }

    // 3. Controllo ripristino password (type=recovery)
    if (initialHash.includes('type=recovery') || initialSearch.includes('type=recovery')) {
      setTimeout(() => {
        showToast('Accesso per ripristino password autorizzato. Imposta la tua nuova password.', 'info', 6000);
        openPasswordRecoveryModal();
        cleanAuthUrl();
      }, 600);
      return;
    }
  }

  // -- Interfaccia Grafica Utente --

  function injectAuthUI() {
    const utilityContainers = document.querySelectorAll('.utility-btns');
    utilityContainers.forEach(container => {
      if (container.querySelector('#btn-auth-user')) return;

      const authBtn = document.createElement('button');
      authBtn.id = 'btn-auth-user';
      authBtn.className = 'btn-auth-user';
      authBtn.title = 'Accedi o registrati';
      authBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span class="auth-btn-label">Accedi</span>
      `;
      authBtn.addEventListener('click', openAuthModal);
      container.appendChild(authBtn);
    });

    // Creazione modale di autenticazione
    if (!document.getElementById('auth-modal')) {
      const modal = document.createElement('div');
      modal.id = 'auth-modal';
      modal.className = 'modal-overlay auth-modal-overlay';
      modal.style.display = 'none';
      modal.innerHTML = `
        <div class="modal-card auth-modal-card">
          <div class="modal-header">
            <h3 id="auth-modal-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              Account Studio ABA Catania
            </h3>
            <button class="modal-close" id="btn-close-auth-modal" aria-label="Chiudi finestra">&times;</button>
          </div>
          <div class="modal-body">
            
            <!-- VISTA UTENTE LOGGATO -->
            <div id="auth-logged-view" style="display: none;">
              <div class="auth-user-card">
                <div class="auth-user-avatar" id="auth-user-avatar-char">U</div>
                <div class="auth-user-info">
                  <div class="auth-user-name" id="auth-user-display-name">Studente</div>
                  <div class="auth-user-email" id="auth-user-display-email">email@esempio.it</div>
                </div>
              </div>
              <div class="auth-user-stats">
                <p>I tuoi progressi vengono salvati automaticamente e sono disponibili su tutti i tuoi dispositivi.</p>
              </div>
              <button id="btn-auth-logout" class="btn-danger" style="width: 100%; margin-top: 16px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                  <polyline points="16 17 21 12 16 7"></polyline>
                  <line x1="21" y1="12" x2="9" y2="12"></line>
                </svg>
                Disconnetti Account
              </button>
            </div>

            <!-- VISTA FORM LOGIN / REGISTRAZIONE -->
            <div id="auth-guest-view">
              <p class="auth-intro-desc">
                Crea un account o accedi per utilizzare la piattaforma di studio.
              </p>
              <form id="form-auth-action">
                <div class="form-group" id="group-display-name" style="display: none;">
                  <label for="input-auth-name">Nome o Nickname</label>
                  <input type="text" id="input-auth-name" class="auth-input" placeholder="Es. Mario Rossi">
                </div>
                <div class="form-group">
                  <label for="input-auth-email">Indirizzo Email</label>
                  <input type="email" id="input-auth-email" class="auth-input" required placeholder="nome@esempio.it">
                </div>
                <div class="form-group">
                  <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
                    <label for="input-auth-password" style="margin-bottom: 0;">Password</label>
                    <button type="button" id="btn-to-forgot-view" class="btn-link-auth" style="font-size: 12px; opacity: 0.85; cursor: pointer;">Password dimenticata?</button>
                  </div>
                  <input type="password" id="input-auth-password" class="auth-input" required minlength="6" placeholder="Minimo 6 caratteri">
                </div>

                <div id="auth-msg-box" class="auth-feedback-box" style="display: none;"></div>

                <button type="submit" id="btn-submit-auth" class="btn-primary-action auth-submit-btn">
                  Accedi
                </button>
              </form>

              <div class="auth-switch-prompt">
                <span id="auth-switch-question">Non hai ancora un account?</span>
                <button type="button" id="btn-toggle-auth-type" class="btn-link-auth">Registrati gratis</button>
              </div>
            </div>

            <!-- VISTA PASSWORD DIMENTICATA -->
            <div id="auth-forgot-view" style="display: none;">
              <p class="auth-intro-desc">
                Inserisci l'indirizzo email associato al tuo account. Riceverai un link per reimpostare la tua password.
              </p>
              <form id="form-auth-forgot">
                <div class="form-group">
                  <label for="input-forgot-email">Indirizzo Email</label>
                  <input type="email" id="input-forgot-email" class="auth-input" required placeholder="nome@esempio.it">
                </div>
                <div id="auth-forgot-msg-box" class="auth-feedback-box" style="display: none;"></div>
                <button type="submit" id="btn-submit-forgot" class="btn-primary-action auth-submit-btn">
                  Invia Email di Ripristino
                </button>
              </form>
              <div class="auth-switch-prompt">
                <button type="button" id="btn-back-from-forgot" class="btn-link-auth">Torna all'accesso</button>
              </div>
            </div>

            <!-- VISTA REIMPOSTA NUOVA PASSWORD (DOPO LINK EMAIL) -->
            <div id="auth-recovery-view" style="display: none;">
              <p class="auth-intro-desc">
                Accesso verificato con successo. Inserisci e conferma la nuova password del tuo account.
              </p>
              <form id="form-auth-recovery">
                <div class="form-group">
                  <label for="input-recovery-password">Nuova Password</label>
                  <input type="password" id="input-recovery-password" class="auth-input" required minlength="6" placeholder="Minimo 6 caratteri">
                </div>
                <div class="form-group">
                  <label for="input-recovery-confirm">Conferma Nuova Password</label>
                  <input type="password" id="input-recovery-confirm" class="auth-input" required minlength="6" placeholder="Ripeti la nuova password">
                </div>
                <div id="auth-recovery-msg-box" class="auth-feedback-box" style="display: none;"></div>
                <button type="submit" id="btn-submit-recovery" class="btn-primary-action auth-submit-btn">
                  Salva Nuova Password
                </button>
              </form>
            </div>

          </div>
        </div>
      `;
      document.body.appendChild(modal);

      document.getElementById('btn-close-auth-modal').addEventListener('click', closeAuthModal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeAuthModal();
      });

      document.getElementById('btn-toggle-auth-type').addEventListener('click', toggleAuthMode);
      document.getElementById('form-auth-action').addEventListener('submit', handleAuthSubmit);
      document.getElementById('btn-to-forgot-view').addEventListener('click', showForgotView);
      document.getElementById('btn-back-from-forgot').addEventListener('click', showGuestView);
      document.getElementById('form-auth-forgot').addEventListener('submit', handleForgotSubmit);
      document.getElementById('form-auth-recovery').addEventListener('submit', handleRecoverySubmit);
      document.getElementById('btn-auth-logout').addEventListener('click', async () => {
        await signOut();
        closeAuthModal();
      });
    }
  }

  let isRegisterMode = false;

  function toggleAuthMode() {
    isRegisterMode = !isRegisterMode;
    const nameGroup = document.getElementById('group-display-name');
    const submitBtn = document.getElementById('btn-submit-auth');
    const question = document.getElementById('auth-switch-question');
    const toggleBtn = document.getElementById('btn-toggle-auth-type');
    const msgBox = document.getElementById('auth-msg-box');
    if (msgBox) msgBox.style.display = 'none';

    if (isRegisterMode) {
      nameGroup.style.display = 'block';
      submitBtn.textContent = 'Crea Account Gratuito';
      question.textContent = 'Hai gia un account?';
      toggleBtn.textContent = 'Accedi';
    } else {
      nameGroup.style.display = 'none';
      submitBtn.textContent = 'Accedi';
      question.textContent = 'Non hai ancora un account?';
      toggleBtn.textContent = 'Registrati gratis';
    }
  }

  function showForgotView() {
    const guestView = document.getElementById('auth-guest-view');
    const forgotView = document.getElementById('auth-forgot-view');
    const recoveryView = document.getElementById('auth-recovery-view');
    const loggedView = document.getElementById('auth-logged-view');
    const msgBox = document.getElementById('auth-forgot-msg-box');

    if (guestView) guestView.style.display = 'none';
    if (recoveryView) recoveryView.style.display = 'none';
    if (loggedView) loggedView.style.display = 'none';
    if (forgotView) forgotView.style.display = 'block';
    if (msgBox) msgBox.style.display = 'none';

    const modalTitle = document.getElementById('auth-modal-title');
    if (modalTitle) {
      modalTitle.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="16" x2="12" y2="12"></line>
          <line x1="12" y1="8" x2="12.01" y2="8"></line>
        </svg>
        Ripristino Password
      `;
    }
  }

  function showGuestView() {
    const guestView = document.getElementById('auth-guest-view');
    const forgotView = document.getElementById('auth-forgot-view');
    const recoveryView = document.getElementById('auth-recovery-view');
    const loggedView = document.getElementById('auth-logged-view');

    if (forgotView) forgotView.style.display = 'none';
    if (recoveryView) recoveryView.style.display = 'none';
    if (loggedView) loggedView.style.display = 'none';
    if (guestView) guestView.style.display = 'block';

    const modalTitle = document.getElementById('auth-modal-title');
    if (modalTitle) {
      modalTitle.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        Account Studio ABA Catania
      `;
    }
  }

  function openPasswordRecoveryModal() {
    const modal = document.getElementById('auth-modal');
    if (!modal) return;
    const guestView = document.getElementById('auth-guest-view');
    const forgotView = document.getElementById('auth-forgot-view');
    const recoveryView = document.getElementById('auth-recovery-view');
    const loggedView = document.getElementById('auth-logged-view');
    const msgBox = document.getElementById('auth-recovery-msg-box');

    if (guestView) guestView.style.display = 'none';
    if (forgotView) forgotView.style.display = 'none';
    if (loggedView) loggedView.style.display = 'none';
    if (recoveryView) recoveryView.style.display = 'block';
    if (msgBox) msgBox.style.display = 'none';

    const modalTitle = document.getElementById('auth-modal-title');
    if (modalTitle) {
      modalTitle.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
        </svg>
        Imposta Nuova Password
      `;
    }

    modal.style.display = 'flex';
  }

  async function handleAuthSubmit(e) {
    e.preventDefault();
    const email = document.getElementById('input-auth-email').value;
    const pass = document.getElementById('input-auth-password').value;
    const name = document.getElementById('input-auth-name').value;
    const submitBtn = document.getElementById('btn-submit-auth');
    const msgBox = document.getElementById('auth-msg-box');

    submitBtn.disabled = true;
    submitBtn.textContent = 'Attendere...';
    msgBox.style.display = 'none';

    try {
      if (isRegisterMode) {
        const { data, error } = await signUp(email, pass, name);
        if (error) throw error;
        if (data && data.user && data.user.identities && data.user.identities.length === 0) {
          throw new Error('Questa email risulta già registrata. Prova ad accedere.');
        }
        msgBox.className = 'auth-feedback-box success';
        msgBox.innerHTML = '<strong>Account creato con successo.</strong><br>Abbiamo inviato l\'email di conferma: controlla la tua casella di posta e <strong>verifica anche nella cartella SPAM o Posta indesiderata</strong>.';
        msgBox.style.display = 'block';
        setTimeout(() => {
          closeAuthModal();
        }, 6000);
      } else {
        const { data, error } = await signIn(email, pass);
        if (error) throw error;
        msgBox.className = 'auth-feedback-box success';
        msgBox.textContent = 'Accesso effettuato.';
        msgBox.style.display = 'block';
        setTimeout(() => {
          closeAuthModal();
        }, 1000);
      }
    } catch (err) {
      msgBox.className = 'auth-feedback-box error';
      msgBox.textContent = err.message || 'Errore durante l\'autenticazione. Riprova.';
      msgBox.style.display = 'block';
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = isRegisterMode ? 'Crea Account Gratuito' : 'Accedi';
    }
  }

  async function handleForgotSubmit(e) {
    e.preventDefault();
    const email = document.getElementById('input-forgot-email').value;
    const submitBtn = document.getElementById('btn-submit-forgot');
    const msgBox = document.getElementById('auth-forgot-msg-box');

    submitBtn.disabled = true;
    submitBtn.textContent = 'Invio in corso...';
    msgBox.style.display = 'none';

    try {
      const { error } = await resetPassword(email);
      if (error) throw error;
      msgBox.className = 'auth-feedback-box success';
      msgBox.innerHTML = '<strong>Email inviata.</strong><br>Controlla la tua casella di posta e <strong>verifica anche nella cartella SPAM o Posta indesiderata</strong> per reimpostare la password.';
      msgBox.style.display = 'block';
    } catch (err) {
      msgBox.className = 'auth-feedback-box error';
      msgBox.textContent = err.message || 'Errore durante l\'invio. Riprova.';
      msgBox.style.display = 'block';
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Invia Email di Ripristino';
    }
  }

  async function handleRecoverySubmit(e) {
    e.preventDefault();
    const pass = document.getElementById('input-recovery-password').value;
    const confirmPass = document.getElementById('input-recovery-confirm').value;
    const submitBtn = document.getElementById('btn-submit-recovery');
    const msgBox = document.getElementById('auth-recovery-msg-box');

    if (pass !== confirmPass) {
      msgBox.className = 'auth-feedback-box error';
      msgBox.textContent = 'Le due password inserite non coincidono.';
      msgBox.style.display = 'block';
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Salvataggio in corso...';
    msgBox.style.display = 'none';

    try {
      const { error } = await updateUserPassword(pass);
      if (error) throw error;
      msgBox.className = 'auth-feedback-box success';
      msgBox.textContent = 'Password aggiornata con successo. Accesso completato.';
      msgBox.style.display = 'block';
      showToast('Password aggiornata con successo.', 'success', 5000);
      setTimeout(() => {
        closeAuthModal();
      }, 2000);
    } catch (err) {
      msgBox.className = 'auth-feedback-box error';
      msgBox.textContent = err.message || 'Errore durante l\'aggiornamento della password.';
      msgBox.style.display = 'block';
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Salva Nuova Password';
    }
  }

  function openAuthModal() {
    const modal = document.getElementById('auth-modal');
    if (!modal) return;
    const loggedView = document.getElementById('auth-logged-view');
    const guestView = document.getElementById('auth-guest-view');
    const forgotView = document.getElementById('auth-forgot-view');
    const recoveryView = document.getElementById('auth-recovery-view');

    showGuestView();

    if (currentUser) {
      if (loggedView) loggedView.style.display = 'block';
      if (guestView) guestView.style.display = 'none';
      if (forgotView) forgotView.style.display = 'none';
      if (recoveryView) recoveryView.style.display = 'none';

      const char = (currentUser.email || 'U').charAt(0).toUpperCase();
      document.getElementById('auth-user-avatar-char').textContent = char;
      document.getElementById('auth-user-display-email').textContent = currentUser.email;
      const displayName = (currentUser.user_metadata && currentUser.user_metadata.display_name) || currentUser.email.split('@')[0];
      document.getElementById('auth-user-display-name').textContent = displayName;
    } else {
      if (loggedView) loggedView.style.display = 'none';
      if (guestView) guestView.style.display = 'block';
      if (forgotView) forgotView.style.display = 'none';
      if (recoveryView) recoveryView.style.display = 'none';
    }

    modal.style.display = 'flex';
  }

  function closeAuthModal() {
    const modal = document.getElementById('auth-modal');
    if (modal) modal.style.display = 'none';
  }

  function updateAuthUI() {
    const btns = document.querySelectorAll('#btn-auth-user');
    btns.forEach(btn => {
      if (currentUser) {
        const char = (currentUser.email || 'U').charAt(0).toUpperCase();
        const shortName = (currentUser.user_metadata && currentUser.user_metadata.display_name) || currentUser.email.split('@')[0];
        btn.classList.add('logged-in');
        btn.innerHTML = `
          <span class="auth-avatar-circle">${char}</span>
          <span class="auth-btn-label">${shortName}</span>
        `;
        btn.title = 'Gestisci il tuo account';
      } else {
        btn.classList.remove('logged-in');
        btn.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <span class="auth-btn-label">Accedi</span>
        `;
        btn.title = 'Accedi o registrati per sincronizzare i tuoi progressi';
      }
    });
  }

  function showToast(message, type = 'info', duration = 4500) {
    let toast = document.getElementById('app-cloud-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'app-cloud-toast';
      toast.className = 'cloud-toast-notification';
      document.body.appendChild(toast);
    }

    const iconSvg = type === 'success'
      ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>`
      : type === 'error'
      ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>`
      : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>`;

    toast.innerHTML = `${iconSvg}<span>${message}</span>`;
    toast.className = `cloud-toast-notification show ${type}`;

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  // Inizializzazione
  async function init() {
    if (!initSupabase()) return;

    injectAuthUI();
    removeLoginWall();

    // Gestione atterraggio da link di redirect (conferma o recovery)
    handleUrlRedirectEvents();

    // Listener per risveglio da standby / sblocco schermo su smartphone
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && currentUser) {
        syncCloudProgress(currentUser, true);
      }
    });
    window.addEventListener('focus', () => {
      if (currentUser) {
        syncCloudProgress(currentUser, true);
      }
    });

    // Recupera la sessione attiva
    try {
      const { data: { session } } = await supabase.auth.getSession();
      if (session && session.user) {
        currentUser = session.user;
        updateAuthUI();
        await syncCloudProgress(currentUser);
      } else {
        currentUser = null;
        updateAuthUI();
        // Se siamo su smartphone e non loggati, mostra un promemoria discreto una volta
        if (window.innerWidth <= 768 && !sessionStorage.getItem('aba_login_prompt_shown')) {
          sessionStorage.setItem('aba_login_prompt_shown', 'true');
          setTimeout(() => {
            if (!currentUser) {
              showToast('Accedi al tuo account per sincronizzare i progressi completati su PC.', 'info', 6000);
            }
          }, 1500);
        }
      }
    } catch (e) {
      console.warn('Errore lettura sessione:', e);
      currentUser = null;
      updateAuthUI();
    }

    // Ascolta cambi di stato login/logout/recovery
    supabase.auth.onAuthStateChange(async (event, session) => {
      if (event === 'PASSWORD_RECOVERY') {
        showToast('Accesso per ripristino password autorizzato. Imposta la nuova password.', 'info', 6000);
        openPasswordRecoveryModal();
      } else if (event === 'SIGNED_IN' && session) {
        currentUser = session.user;
        updateAuthUI();
        await syncCloudProgress(currentUser);
        window.dispatchEvent(new CustomEvent('auth:change', { detail: { user: currentUser } }));
      } else if (event === 'SIGNED_OUT') {
        currentUser = null;
        if (realtimeChannel) {
          try { supabase.removeChannel(realtimeChannel); } catch (e) {}
          realtimeChannel = null;
        }
        try {
          localStorage.removeItem(LOCAL_STORAGE_KEY);
          localStorage.removeItem('aba_studio_state_v2');
        } catch (e) {}
        if (window.StudyCore && window.StudyCore.state) {
          window.StudyCore.state.completed = {};
        }
        updateAuthUI();
        triggerUIProgressRefresh({});
        window.dispatchEvent(new CustomEvent('auth:change', { detail: { user: null } }));
      }
    });
  }

  // Esponi per l'app
  window.AppAuth = {
    signUp,
    signIn,
    signOut,
    resetPassword,
    updateUserPassword,
    onStateSaved,
    syncCloudProgress,
    showToast,
    getUser: () => currentUser,
    openModal: openAuthModal,
    openAuthModal,
    closeModal: closeAuthModal,
    openRecoveryModal: openPasswordRecoveryModal
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
