-- Studio ABA Catania: stato completo dei progressi (ripasso, quiz, attività, esami, orale)
-- Da eseguire una volta nella dashboard Supabase: SQL Editor > New query > Run.
-- I capitoli completati restano nella tabella user_progress.

create table if not exists public.user_state (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  data       jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.user_state enable row level security;

drop policy if exists "user_state: lettura del proprietario" on public.user_state;
create policy "user_state: lettura del proprietario"
  on public.user_state for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "user_state: inserimento del proprietario" on public.user_state;
create policy "user_state: inserimento del proprietario"
  on public.user_state for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "user_state: modifica del proprietario" on public.user_state;
create policy "user_state: modifica del proprietario"
  on public.user_state for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);
