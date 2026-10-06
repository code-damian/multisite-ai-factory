create extension if not exists pgcrypto;

create table if not exists public.webstrefa_users (
  id uuid primary key,
  name text not null,
  email text unique not null,
  password_hash text not null,
  password_salt text not null,
  created_at timestamptz default now()
);

create table if not exists public.webstrefa_reviews (
  id uuid primary key,
  user_id uuid unique not null references public.webstrefa_users(id) on delete cascade,
  rating integer not null check (rating between 1 and 5),
  text text not null,
  created_at timestamptz default now()
);

create table if not exists public.webstrefa_contacts (
  id uuid primary key,
  name text not null,
  email text not null,
  type text not null,
  budget text,
  scope text not null,
  message text not null,
  created_at timestamptz default now()
);

alter table public.webstrefa_users enable row level security;
alter table public.webstrefa_reviews enable row level security;
alter table public.webstrefa_contacts enable row level security;

revoke all on table public.webstrefa_users from anon, authenticated;
revoke all on table public.webstrefa_reviews from anon, authenticated;
revoke all on table public.webstrefa_contacts from anon, authenticated;

grant select, insert, update, delete on table public.webstrefa_users to service_role;
grant select, insert, update, delete on table public.webstrefa_reviews to service_role;
grant select, insert, update, delete on table public.webstrefa_contacts to service_role;

notify pgrst, 'reload schema';