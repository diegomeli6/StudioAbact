/**
 * js/auth.js — Autenticazione Cloud & Sincronizzazione Multi-Piattaforma con Supabase
 * Piattaforma Didattica Studio — ABA Catania
 */

(function () {
  'use strict';

  // ── Configurazione Supabase ──
  const SUPABASE_URL = 'https://ivpctopxkvkcdvwbccml.supabase.co';
  const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml2cGN0b3B4a3ZrY2R2d2JjY21sIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODkwNDk1MzIsImV4cCI6MjEwNDYyNTUzMn0.acJDqcShn5pdbRglReXQEgRK-VUTiOylDzi46psKFfQ';

  let supabase = null;
  let currentUser = null;
  let syncDebounceTimer = null;

  // Inizializza il client Supabase
  function initSupabase() {
    if (window.supabase && typeof window.supabase.createClient === 'function') {
      supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      window.appSupabase = supabase;
      return true;
    }
    console.warn('Libreria Supabase non trovata. Includere @supabase/supabase-js.');
    return false;
  }

  // ── Metodi di Autenticazione ──

  async function signUp(email, password, displayName) {
    if (!supabase) return { error: { message: 'Client Supabase non inizializzato' } };
    const { data, error } = await supabase.auth.signUp({
      email: email.trim(),
      password: password,
      options: {
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
    if (!supabase) return;
    const { error } = await supabase.auth.signOut();
    currentUser = null;
    updateAuthUI();
    showToast('Hai effettuato il logout con successo.', 'info');
    return { error };
  }

  async function resetPassword(email) {
    if (!supabase) return { error: { message: 'Client non inizializzato' } };
    const { data, error } = await supabase.auth.resetPasswordForEmail(email.trim());
    return { data, error };
  }

  // ── Sincronizzazione Database Cloud ──

  // Carica tutti i progressi dell'utente dal cloud
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
      console.warn('Errore di rete cloud progress:', e);
      return [];
    }
  }

  // Invia i progressi al cloud (upsert)
  async function pushChapterProgressToCloud(userId, subject, chapterId, completed, quizScore = 0) {
    if (!supabase || !userId) return;
    try {
      const { error } = await supabase
        .from('user_progress')
        .upsert({
          user_id: userId,
          subject: subject,
          chapter_id: chapterId,
          completed: !!completed,
          quiz_score: quizScore,
          updated_at: new Date().toISOString()
        }, { onConflict: 'user_id,subject,chapter_id' });

      if (error) {
        console.warn('Errore push chapter a Supabase:', error);
      }
    } catch (e) {
      console.warn('Errore push chapter exception:', e);
    }
  }

  // Migrazione automatica: carica i progressi locali sul cloud al primo login
  async function migrateLocalStateToCloud(user) {
    if (!user) return;
    try {
      const localStateStr = localStorage.getItem('aba_studio_state_v2');
      if (!localStateStr) return;
      const localState = JSON.parse(localStateStr);
      const completed = localState.completed || {};
      const completedIds = Object.keys(completed).filter(k => completed[k]);

      if (completedIds.length === 0) return;

      const rows = completedIds.map(chapId => {
        const subj = chapId.startsWith('arte-') ? 'arte' : 'ux';
        return {
          user_id: user.id,
          subject: subj,
          chapter_id: chapId,
          completed: true,
          updated_at: new Date().toISOString()
        };
      });

      const { error } = await supabase
        .from('user_progress')
        .upsert(rows, { onConflict: 'user_id,subject,chapter_id' });

      if (!error) {
        console.log(`Migrati con successo ${rows.length} capitoli completati sul cloud!`);
      }
    } catch (e) {
      console.warn('Errore durante migrazione locale su cloud:', e);
    }
  }

  // Sincronizzazione bidirezionale al login
  async function syncOnLogin(user) {
    if (!user) return;
    showToast('Sincronizzazione dei progressi cloud in corso...', 'info');

    const cloudRows = await fetchCloudProgress(user.id);

    if (cloudRows.length > 0) {
      // Unisci i dati cloud con lo stato locale
      if (window.StudyCore && window.StudyCore.state) {
        cloudRows.forEach(row => {
          window.StudyCore.state.completed[row.chapter_id] = row.completed;
        });
        window.StudyCore.saveLocalState();
        if (typeof window.updateProgressIndicators === 'function') {
          window.updateProgressIndicators();
        }
      }
      showToast(`Sincronizzati ${cloudRows.length} elementi dal tuo account! ☁️`, 'success');
    } else {
      // Se sul cloud non c'è ancora nulla, migra i dati locali già presenti
      await migrateLocalStateToCloud(user);
      showToast('Progressi locali salvati sul tuo nuovo account cloud! ☁️', 'success');
    }

    updateAuthUI();
  }

  // Hook chiamato da core.js quando l'utente completa o modifica un capitolo
  function onStateSaved(payload) {
    if (!currentUser || !supabase) return;

    // Debounce per non sovraccaricare le chiamate di rete
    if (syncDebounceTimer) clearTimeout(syncDebounceTimer);
    syncDebounceTimer = setTimeout(async () => {
      const subject = payload.currentSubject || (window.location.pathname.includes('storia-arte') ? 'arte' : 'ux');
      const completedMap = payload.completed || {};

      for (const [chapId, isDone] of Object.entries(completedMap)) {
        if (isDone) {
          const itemSubj = chapId.startsWith('arte-') ? 'arte' : 'ux';
          await pushChapterProgressToCloud(currentUser.id, itemSubj, chapId, true);
        }
      }
      console.log('Progressi salvati sul cloud Supabase');
    }, 600);
  }

  // ── Interfaccia Grafica Utente (UI & Modale) ──

  function injectAuthUI() {
    // 1. Inserimento pulsante nel top-header / home-header
    const utilityContainers = document.querySelectorAll('.utility-btns');
    utilityContainers.forEach(container => {
      if (container.querySelector('#btn-auth-user')) return;

      const authBtn = document.createElement('button');
      authBtn.id = 'btn-auth-user';
      authBtn.className = 'btn-auth-user';
      authBtn.title = 'Accedi o registrati per sincronizzare i tuoi progressi';
      authBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span class="auth-btn-label">Accedi</span>
      `;
      authBtn.addEventListener('click', openAuthModal);
      container.insertBefore(authBtn, container.firstChild);
    });

    // 2. Creazione modale di autenticazione nel DOM
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
                <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path>
                <polyline points="17 21 17 13 7 13 7 21"></polyline>
                <polyline points="7 3 7 8 15 8"></polyline>
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
                  <div class="auth-sync-status">
                    <span class="sync-dot"></span> Sincronizzazione cloud attiva
                  </div>
                </div>
              </div>
              <div class="auth-user-stats">
                <p>I tuoi progressi sono salvati nel cloud e aggiornati in tempo reale su tutti i tuoi dispositivi (computer, tablet e telefono).</p>
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
                Crea un account o accedi per ritrovare i tuoi progressi su <strong>qualsiasi dispositivo</strong> (PC, smartphone o tablet).
              </p>
              <form id="form-auth-action">
                <div class="form-group" id="group-display-name" style="display: none;">
                  <label for="input-auth-name">Nome o Nickname</label>
                  <input type="text" id="input-auth-name" class="auth-input" placeholder="Es. Diego">
                </div>
                <div class="form-group">
                  <label for="input-auth-email">Indirizzo Email</label>
                  <input type="email" id="input-auth-email" class="auth-input" required placeholder="nome@esempio.it">
                </div>
                <div class="form-group">
                  <label for="input-auth-password">Password</label>
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

          </div>
        </div>
      `;
      document.body.appendChild(modal);

      // Eventi della modale
      document.getElementById('btn-close-auth-modal').addEventListener('click', closeAuthModal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeAuthModal();
      });

      document.getElementById('btn-toggle-auth-type').addEventListener('click', toggleAuthMode);
      document.getElementById('form-auth-action').addEventListener('submit', handleAuthSubmit);
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
    msgBox.style.display = 'none';

    if (isRegisterMode) {
      nameGroup.style.display = 'block';
      submitBtn.textContent = 'Crea Account Gratuito';
      question.textContent = 'Hai già un account?';
      toggleBtn.textContent = 'Accedi';
    } else {
      nameGroup.style.display = 'none';
      submitBtn.textContent = 'Accedi';
      question.textContent = 'Non hai ancora un account?';
      toggleBtn.textContent = 'Registrati gratis';
    }
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
        msgBox.textContent = 'Account creato! Ti abbiamo inviato una mail di conferma. Se l\'accesso è automatico puoi già iniziare.';
        msgBox.style.display = 'block';
        setTimeout(() => {
          closeAuthModal();
        }, 2000);
      } else {
        const { data, error } = await signIn(email, pass);
        if (error) throw error;
        msgBox.className = 'auth-feedback-box success';
        msgBox.textContent = 'Accesso riuscito! Sincronizzazione in corso...';
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

  function openAuthModal() {
    const modal = document.getElementById('auth-modal');
    if (!modal) return;
    const loggedView = document.getElementById('auth-logged-view');
    const guestView = document.getElementById('auth-guest-view');

    if (currentUser) {
      loggedView.style.display = 'block';
      guestView.style.display = 'none';
      const char = (currentUser.email || 'U').charAt(0).toUpperCase();
      document.getElementById('auth-user-avatar-char').textContent = char;
      document.getElementById('auth-user-display-email').textContent = currentUser.email;
      const displayName = (currentUser.user_metadata && currentUser.user_metadata.display_name) || currentUser.email.split('@')[0];
      document.getElementById('auth-user-display-name').textContent = displayName;
    } else {
      loggedView.style.display = 'none';
      guestView.style.display = 'block';
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
          <span class="auth-cloud-badge" title="Sincronizzato sul Cloud">☁️</span>
        `;
        btn.title = `Accesso effettuato come ${currentUser.email} (Clicca per gestire)`;
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

  function showToast(message, type = 'info') {
    let toast = document.getElementById('app-cloud-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'app-cloud-toast';
      toast.className = 'cloud-toast-notification';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.className = `cloud-toast-notification show ${type}`;
    setTimeout(() => {
      toast.classList.remove('show');
    }, 3500);
  }

  // Inizializzazione all'avvio
  async function init() {
    if (!initSupabase()) return;

    injectAuthUI();

    // Recupera la sessione attiva
    try {
      const { data: { session } } = await supabase.auth.getSession();
      if (session && session.user) {
        currentUser = session.user;
        updateAuthUI();
        await syncOnLogin(currentUser);
      } else {
        updateAuthUI();
      }
    } catch (e) {
      console.warn('Errore lettura sessione Supabase:', e);
    }

    // Ascolta cambi di stato login/logout
    supabase.auth.onAuthStateChange(async (event, session) => {
      if (event === 'SIGNED_IN' && session) {
        currentUser = session.user;
        updateAuthUI();
        await syncOnLogin(currentUser);
      } else if (event === 'SIGNED_OUT') {
        currentUser = null;
        updateAuthUI();
      }
    });
  }

  // Esponi per l'app
  window.AppAuth = {
    signUp,
    signIn,
    signOut,
    resetPassword,
    onStateSaved,
    getUser: () => currentUser,
    openModal: openAuthModal,
    closeModal: closeAuthModal
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
