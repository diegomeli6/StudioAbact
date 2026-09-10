# Guida: Autenticazione Cloud & Sincronizzazione Multi-Piattaforma — Studio ABACT

Questa guida spiega passo-passo come configurare l'autenticazione utente e il database cloud con **Supabase (100% gratuito a vita)** per sincronizzare i progressi di studio (capitoli letti, quiz completati, flashcard e voti delle simulazioni d'esame) su **qualsiasi dispositivo** (PC, Mac, iPhone, Android, iPad).

---

## 1. Come funziona la sincronizzazione multi-dispositivo

Attualmente la piattaforma memorizza i dati esclusivamente in `localStorage` sul singolo browser del dispositivo usato.  
Configurando Supabase:
1. Lo studente crea un account (email e password).
2. Ogni volta che completa un capitolo, una flashcard o un quiz, il progresso viene inviato a un database sicuro PostgreSQL nel cloud.
3. Aprendo la piattaforma da un altro dispositivo (es. telefono o tablet) ed effettuando il login, i progressi vengono scaricati all'istante e mantenuti allineati.
4. Se il dispositivo va offline, l'app continua a funzionare normalmente e sincronizza i dati non appena torna la connessione.

---

## 2. Passo 1: Creazione progetto gratuito su Supabase

1. Accedi a **[supabase.com](https://supabase.com/)** e crea un account gratuito (basta anche accedere con GitHub).
2. Clicca su **New Project**.
3. Inserisci:
   - **Name**: `studio-abact`
   - **Database Password**: scegli e annota una password sicura.
   - **Region**: `Central Europe (Frankfurt)` (la più veloce e vicina per l'Italia).
   - **Plan**: **Free Tier (0 $/mese)**.
4. Clicca su **Create New Project**.

---

## 3. Passo 2: Copia delle credenziali pubbliche

Nel menu del progetto Supabase:
- Vai su **Project Settings** (icona ingranaggio in basso a sinistra) ➔ **API**.
- Troverai due parametri da copiare:
  1. `Project URL` (es. `https://xxxxxx.supabase.co`)
  2. `Project API Keys` ➔ `anon` `public` (la chiave che inizia con `eyJhbGciOi...`)

---

## 4. Passo 3: Script SQL per il Database (Copia e Incolla)

Nel menu a sinistra di Supabase, clicca su **SQL Editor** ➔ **New Query**, incolla questo codice e premi **Run**:

```sql
-- 1. Tabella dei profili utente
CREATE TABLE public.profiles (
  id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
  email TEXT NOT NULL,
  display_name TEXT,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Tabella dei progressi (capitoli, quiz, flashcard)
CREATE TABLE public.user_progress (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
  subject TEXT NOT NULL,         -- 'arte' oppure 'ux'
  chapter_id TEXT NOT NULL,      -- es. 'arte-c1'
  completed BOOLEAN DEFAULT false NOT NULL,
  quiz_score INTEGER DEFAULT 0,
  flashcards_known TEXT[] DEFAULT '{}',
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
  UNIQUE(user_id, subject, chapter_id)
);

-- 3. Tabella della cronologia simulazioni esame
CREATE TABLE public.exam_history (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
  subject TEXT NOT NULL,
  score_thirtieths INTEGER NOT NULL,
  correct_count INTEGER NOT NULL,
  total_questions INTEGER NOT NULL,
  exam_date TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Sicurezza: Row Level Security (RLS)
-- Ogni studente può accedere e modificare solo ed esclusivamente i propri record!
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.exam_history ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Utenti leggono solo proprio profilo" ON public.profiles
  FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Utenti aggiornano solo proprio profilo" ON public.profiles
  FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Utenti vedono solo propri progressi" ON public.user_progress
  FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Utenti inseriscono propri progressi" ON public.user_progress
  FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Utenti aggiornano propri progressi" ON public.user_progress
  FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Utenti vedono solo propri esami" ON public.exam_history
  FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Utenti inseriscono propri esami" ON public.exam_history
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Trigger automatico di creazione profilo alla registrazione
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, email, display_name)
  VALUES (new.id, new.email, split_part(new.email, '@', 1));
  RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

---

## 5. Passo 4: Come si integrerà nel sito web

Quando deciderai di attivarlo, l'integrazione consisterà in 3 semplici passaggi:

1. **Includere lo script Supabase** nei file HTML:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
   ```
2. **Aggiungere un modulo `js/auth.js`** che gestisce login, registrazione, logout e la sincronizzazione con `StudyCore.state`.
3. **Aggiungere il pulsante "Accedi"** nella testata del sito, che apre una finestra modale pulita ed elegante per inserire email e password.

Al primo accesso, l'applicazione prenderà automaticamente tutti i progressi già salvati su quel browser e li caricherà sul cloud, così non perderai nulla di quanto fatto finora!
