# Guida Completa: Configurazione Gmail SMTP su Supabase e Template Email

Questa guida spiega passo-passo come utilizzare un account Gmail dedicato come server SMTP gratuito per il tuo progetto Supabase. In questo modo sblocchi la modifica delle email di sistema e puoi personalizzare la grafica e i testi in italiano per tutti gli studenti.

---

## 1. Creazione dell'Account Gmail Dedicato

Quando Google chiede il tipo di account:
- Seleziona: **"Per uso personale"** (NON selezionare "Per lavoro", altrimenti richiede l'abbonamento a Google Workspace). L'account personale e 100% gratuito e include tutte le funzioni necessarie.

Suggerimenti per la compilazione:
1. Vai su **[accounts.google.com/signup](https://accounts.google.com/signup)**.
2. Scegli **"Per uso personale"**.
3. Inserisci:
   - **Nome**: `Studio`
   - **Cognome**: `Accademia CT`
   - **Indirizzo email desiderato**: ad esempio `studio.accademia.ct@gmail.com`, `accademia.studio.ct@gmail.com` oppure `piattaforma.accademia.ct@gmail.com`
4. Imposta una password e completa la registrazione (se richiesto, inserisci il tuo numero di telefono per la sicurezza).

---

## 2. Generazione della "Password per le app" su Google

Per motivi di sicurezza, Google non consente a servizi esterni (come Supabase) di accedere con la password principale della casella. Si genera quindi una "Password per le app" di 16 caratteri dedicata esclusivamente a Supabase.

1. Accedi all'account Gmail appena creato e vai su **[myaccount.google.com/security](https://myaccount.google.com/security)** (sezione **Sicurezza**).
2. Nella sezione **Come accedi a Google**:
   - Assicurati che la **Verifica in due passaggi** sia **Attiva** (se disattiva, attivala seguendo la procedura a schermo con il tuo cellulare).
3. Una volta attiva la verifica in due passaggi, vai direttamente al link:
   **[myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)**
   *(Se non vedi la pagina, digita "Password per le app" nella barra di ricerca in alto nella pagina del tuo account Google)*.
4. Nel campo **Nome dell'app**, scrivi:
   `Supabase Studio`
5. Clicca sul pulsante **Crea**.
6. Google mostrera una finestra con un codice di 16 caratteri (es. `abcd efgh ijkl mnop`).
7. **Copia questo codice di 16 lettere** (puoi copiarlo con o senza spazi, Supabase lo accettera ugualmente). Conservalo, ti servira subito nel passaggio successivo.

---

## 3. Configurazione SMTP su Supabase

1. Accedi a **[supabase.com/dashboard](https://supabase.com/dashboard)** e apri il tuo progetto.
2. Nella barra laterale a sinistra, clicca sull'icona **Authentication** (icona a forma di lucchetto o utenti).
3. Nel menu di sinistra, sotto **Configuration**, clicca su **SMTP Settings** (oppure **Sign In / Providers** -> **Email**).
4. Attiva la spunta o l'interruttore **Enable Custom SMTP**.
5. Compila i campi esattamente in questo modo:

| Campo | Valore da inserire |
| :--- | :--- |
| **Sender email** | L'indirizzo Gmail appena creato (es. `studio.accademia.ct@gmail.com`) |
| **Sender name** | `Piattaforma di Studio — Accademia CT` |
| **Host** | `smtp.gmail.com` |
| **Port number** | `465` |
| **Minimum interval between emails** | `60` (o `1` per invii immediati) |
| **SMTP Username** | Il tuo indirizzo Gmail completo (es. `studio.accademia.ct@gmail.com`) |
| **SMTP Password** | La password per le app di 16 lettere generata da Google (senza spazi) |

6. Clicca su **Save changes** in fondo alla schermata.

Non appena salvato, Supabase effettua un test di connessione. Da questo istante in poi:
- Tutte le email partiranno direttamente dall'indirizzo Google della piattaforma.
- Il limite di invio e di 500 email al giorno (gratuito).
- La sezione **Email Templates** su Supabase si sblocca definitivamente.

---

## 4. Codici HTML per i Template delle Email

Ora che l'SMTP e attivo, vai in **Authentication** -> **Email Templates** e personalizza le email in italiano.

---

### Template 1: Conferma Iscrizione (Confirm signup)

- Seleziona la scheda: **Confirm signup**
- **Subject**:
  `Conferma la tua registrazione - Piattaforma di Studio ABA Catania`
- **Message body (HTML)**:

```html
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 32px 24px; background-color: #0f172a; color: #f8fafc; border-radius: 12px; border: 1px solid #1e293b;">
  <div style="border-bottom: 1px solid #1e293b; padding-bottom: 20px; margin-bottom: 24px;">
    <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #38bdf8; margin-bottom: 6px;">Accademia di Belle Arti di Catania</div>
    <h2 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: -0.02em;">Piattaforma Didattica di Studio</h2>
  </div>
  
  <p style="font-size: 16px; line-height: 1.6; color: #e2e8f0; margin-bottom: 16px;">
    Gentile studente,
  </p>
  
  <p style="font-size: 15px; line-height: 1.6; color: #94a3b8; margin-bottom: 24px;">
    Grazie per esserti registrato. Per confermare il tuo indirizzo email e attivare la sincronizzazione in tempo reale di capitoli letti, quiz, flashcard e voti delle simulazioni d'esame su tutti i tuoi dispositivi, clicca sul pulsante sottostante:
  </p>
  
  <div style="text-align: center; margin: 32px 0;">
    <a href="{{ .ConfirmationURL }}" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 15px; letter-spacing: 0.01em;">
      Conferma Indirizzo Email
    </a>
  </div>
  
  <p style="font-size: 14px; line-height: 1.6; color: #94a3b8; margin-bottom: 28px;">
    Una volta confermata la registrazione, verrai reindirizzato direttamente alla piattaforma con la sessione attiva e i tuoi progressi protetti nel cloud.
  </p>
  
  <div style="border-top: 1px solid #1e293b; padding-top: 20px; margin-top: 32px;">
    <p style="font-size: 12.5px; line-height: 1.5; color: #64748b; margin: 0 0 10px 0;">
      Se non hai richiesto tu la creazione di questo account, puoi tranquillamente ignorare questo messaggio.
    </p>
    <p style="font-size: 12px; line-height: 1.5; color: #64748b; margin: 0;">
      Se il pulsante non e cliccabile, copia e incolla questo indirizzo nella barra del browser:<br>
      <span style="color: #38bdf8; word-break: break-all;">{{ .ConfirmationURL }}</span>
    </p>
  </div>
</div>
```

- Clicca su **Save** in fondo alla scheda.

---

### Template 2: Ripristino Password (Reset Password)

- Seleziona la scheda: **Reset Password**
- **Subject**:
  `Ripristino password - Piattaforma di Studio ABA Catania`
- **Message body (HTML)**:

```html
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 32px 24px; background-color: #0f172a; color: #f8fafc; border-radius: 12px; border: 1px solid #1e293b;">
  <div style="border-bottom: 1px solid #1e293b; padding-bottom: 20px; margin-bottom: 24px;">
    <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #38bdf8; margin-bottom: 6px;">Accademia di Belle Arti di Catania</div>
    <h2 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: -0.02em;">Piattaforma Didattica di Studio</h2>
  </div>
  
  <p style="font-size: 16px; line-height: 1.6; color: #e2e8f0; margin-bottom: 16px;">
    Richiesta di ripristino password
  </p>
  
  <p style="font-size: 15px; line-height: 1.6; color: #94a3b8; margin-bottom: 24px;">
    E stata richiesta la reimpostazione della password per il tuo account. Clicca sul pulsante sottostante per impostare una nuova password:
  </p>
  
  <div style="text-align: center; margin: 32px 0;">
    <a href="{{ .ConfirmationURL }}" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 15px; letter-spacing: 0.01em;">
      Imposta Nuova Password
    </a>
  </div>
  
  <p style="font-size: 14px; line-height: 1.6; color: #94a3b8; margin-bottom: 28px;">
    Il link e protetto e puo essere utilizzato una sola volta.
  </p>
  
  <div style="border-top: 1px solid #1e293b; padding-top: 20px; margin-top: 32px;">
    <p style="font-size: 12.5px; line-height: 1.5; color: #64748b; margin: 0 0 10px 0;">
      Se non hai effettuato tu questa richiesta, ignora questa comunicazione: la tua password attuale rimarra invariata e nessun accesso verra consentito.
    </p>
    <p style="font-size: 12px; line-height: 1.5; color: #64748b; margin: 0;">
      Link alternativo da copiare nel browser:<br>
      <span style="color: #38bdf8; word-break: break-all;">{{ .ConfirmationURL }}</span>
    </p>
  </div>
</div>
```

- Clicca su **Save** in fondo alla scheda.

---

### Template 3: Cambio Indirizzo Email (Change Email Address)

- Seleziona la scheda: **Change Email Address**
- **Subject**:
  `Conferma variazione indirizzo email - Piattaforma di Studio ABA Catania`
- **Message body (HTML)**:

```html
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 32px 24px; background-color: #0f172a; color: #f8fafc; border-radius: 12px; border: 1px solid #1e293b;">
  <div style="border-bottom: 1px solid #1e293b; padding-bottom: 20px; margin-bottom: 24px;">
    <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #38bdf8; margin-bottom: 6px;">Accademia di Belle Arti di Catania</div>
    <h2 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: -0.02em;">Piattaforma Didattica di Studio</h2>
  </div>
  
  <p style="font-size: 16px; line-height: 1.6; color: #e2e8f0; margin-bottom: 16px;">
    Conferma del nuovo indirizzo email
  </p>
  
  <p style="font-size: 15px; line-height: 1.6; color: #94a3b8; margin-bottom: 24px;">
    Abbiamo ricevuto una richiesta di aggiornamento dell'indirizzo email del tuo account. Per confermare la modifica, clicca sul pulsante sottostante:
  </p>
  
  <div style="text-align: center; margin: 32px 0;">
    <a href="{{ .ConfirmationURL }}" style="display: inline-block; background-color: #0284c7; color: #ffffff; text-decoration: none; padding: 14px 32px; border-radius: 8px; font-weight: 600; font-size: 15px;">
      Conferma Nuovo Indirizzo
    </a>
  </div>
  
  <div style="border-top: 1px solid #1e293b; padding-top: 20px; margin-top: 32px;">
    <p style="font-size: 12.5px; line-height: 1.5; color: #64748b; margin: 0;">
      Se non hai richiesto tu la variazione, contatta l'amministrazione della piattaforma.
    </p>
  </div>
</div>
```

- Clicca su **Save** in fondo alla scheda.

---

## 5. Come Funziona il Flusso Completo

1. Uno studente si registra sul sito inserendo email e password.
2. Supabase si connette al server SMTP di Google (`smtp.gmail.com`) e invia la mail con l'aspetto grafico personalizzato.
3. Il mittente visualizzato dallo studente sara:  
   `Piattaforma di Studio — Accademia CT <studio.accademia.ct@gmail.com>`.
4. Lo studente clicca sul pulsante **Conferma Indirizzo Email**.
5. Il browser atterra su `https://diegomeli6.github.io/StudioAbact/`.
6. Lo script `js/auth.js`:
   - Mostra il messaggio in primo piano: **"Email confermata con successo. Il tuo account e attivo."**
   - Esegue il login automatico e rimuove il blocco sui capitoli.
   - Pulisce i parametri tecnici dalla barra degli indirizzi del browser.
