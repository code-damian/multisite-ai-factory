create extension if not exists pgcrypto;

-- ===== WEBSTREFA: IDENTITY / PROFILES =====
create table if not exists public.webstrefa_profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text not null unique,
  first_name text not null,
  last_name text,
  birth_date date not null,
  gender text not null default 'Nie podano' check (gender in ('Kobieta','Mężczyzna','Nie podano')),
  role text not null default 'user' check (role in ('user','moderator','admin')),
  avatar_url text,
  bio text default '',
  is_banned boolean not null default false,
  ban_reason text,
  terms_accepted_at timestamptz not null default now(),
  last_seen_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.webstrefa_registration_attempts (
  id uuid primary key default gen_random_uuid(),
  ip_hash text not null,
  email_hash text,
  created_at timestamptz not null default now()
);

create table if not exists public.webstrefa_audit_logs (
  id uuid primary key default gen_random_uuid(),
  actor_id uuid references auth.users(id) on delete set null,
  action text not null,
  target_type text,
  target_id uuid,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

-- ===== REVIEWS / CONTACT =====
create table if not exists public.webstrefa_reviews_v2 (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null unique references auth.users(id) on delete cascade,
  rating integer not null check (rating between 1 and 5),
  text text not null check (char_length(text) between 5 and 3000),
  status text not null default 'published' check (status in ('published','hidden','pending')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.webstrefa_contacts_v2 (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete set null,
  name text not null,
  email text not null,
  type text not null,
  budget text,
  scope text not null,
  message text not null,
  status text not null default 'new' check (status in ('new','in_progress','answered','archived')),
  created_at timestamptz not null default now()
);

-- ===== FORUM =====
create table if not exists public.webstrefa_forum_categories (
  id uuid primary key default gen_random_uuid(),
  name text not null unique,
  slug text not null unique,
  description text not null default '',
  icon text not null default '▦',
  sort_order integer not null default 0,
  is_locked boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.webstrefa_forum_topics (
  id uuid primary key default gen_random_uuid(),
  category_id uuid not null references public.webstrefa_forum_categories(id) on delete cascade,
  author_id uuid not null references auth.users(id) on delete cascade,
  title text not null check (char_length(title) between 5 and 180),
  slug text not null unique,
  is_pinned boolean not null default false,
  is_locked boolean not null default false,
  is_hidden boolean not null default false,
  views_count integer not null default 0,
  replies_count integer not null default 0,
  last_post_at timestamptz not null default now(),
  last_post_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.webstrefa_forum_posts (
  id uuid primary key default gen_random_uuid(),
  topic_id uuid not null references public.webstrefa_forum_topics(id) on delete cascade,
  author_id uuid not null references auth.users(id) on delete cascade,
  body text not null check (char_length(body) between 2 and 10000),
  is_hidden boolean not null default false,
  edited_at timestamptz,
  created_at timestamptz not null default now()
);

create table if not exists public.webstrefa_forum_reports (
  id uuid primary key default gen_random_uuid(),
  reporter_id uuid not null references auth.users(id) on delete cascade,
  post_id uuid references public.webstrefa_forum_posts(id) on delete cascade,
  topic_id uuid references public.webstrefa_forum_topics(id) on delete cascade,
  reason text not null,
  details text,
  status text not null default 'open' check (status in ('open','reviewing','resolved','rejected')),
  handled_by uuid references auth.users(id) on delete set null,
  handled_at timestamptz,
  created_at timestamptz not null default now()
);

-- ===== BLOG =====
create table if not exists public.webstrefa_blog_posts (
  id uuid primary key default gen_random_uuid(),
  author_id uuid not null references auth.users(id) on delete cascade,
  title text not null,
  slug text not null unique,
  excerpt text not null default '',
  body text not null default '',
  cover_url text,
  status text not null default 'draft' check (status in ('draft','published','archived')),
  tags text[] not null default '{}',
  views_count integer not null default 0,
  published_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.webstrefa_blog_comments (
  id uuid primary key default gen_random_uuid(),
  post_id uuid not null references public.webstrefa_blog_posts(id) on delete cascade,
  author_id uuid not null references auth.users(id) on delete cascade,
  body text not null check (char_length(body) between 2 and 5000),
  is_hidden boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- ===== USER NOTIFICATIONS / BOOKMARKS =====
create table if not exists public.webstrefa_notifications (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  type text not null,
  title text not null,
  body text not null default '',
  link text,
  is_read boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists public.webstrefa_bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  topic_id uuid references public.webstrefa_forum_topics(id) on delete cascade,
  blog_post_id uuid references public.webstrefa_blog_posts(id) on delete cascade,
  created_at timestamptz not null default now(),
  check ((topic_id is not null) <> (blog_post_id is not null))
);

-- ===== DEFAULT FORUM STRUCTURE =====
insert into public.webstrefa_forum_categories (name,slug,description,icon,sort_order)
values
('Programowanie','programowanie','Języki programowania, architektura, dobre praktyki i rozwiązania problemów.','</>',10),
('Web / Front-end','web-front-end','HTML, CSS, JavaScript, UI, UX, responsywność i nowoczesny web.','◫',20),
('Back-end / API','back-end-api','Serwery, API, bazy danych, autoryzacja i integracje.','⌘',30),
('AI / Sztuczna inteligencja','ai','Modele AI, automatyzacje, agenci, prompt engineering i nowe narzędzia.','✦',40),
('Aplikacje i programy','aplikacje','Aplikacje desktopowe, mobilne, SaaS i narzędzia dla firm.','▣',50),
('Gotowe rozwiązania','gotowe-rozwiazania','Szablony, komponenty, skrypty, snippet-y i projekty do nauki.','⚙',60),
('Baza wiedzy','baza-wiedzy','Poradniki, rozwiązania, checklisty i materiały edukacyjne.','?',70),
('Luźne rozmowy','luzne-rozmowy','Społeczność WebStrefy, projekty użytkowników i rozmowy poza kodem.','☰',80)
on conflict (slug) do update set name=excluded.name,description=excluded.description,icon=excluded.icon,sort_order=excluded.sort_order;

-- ===== INDEXES =====
create index if not exists idx_profiles_role on public.webstrefa_profiles(role);
create index if not exists idx_profiles_last_seen on public.webstrefa_profiles(last_seen_at);
create index if not exists idx_reg_attempts_ip_created on public.webstrefa_registration_attempts(ip_hash,created_at);
create index if not exists idx_topics_category on public.webstrefa_forum_topics(category_id);
create index if not exists idx_topics_author on public.webstrefa_forum_topics(author_id);
create index if not exists idx_topics_last_post on public.webstrefa_forum_topics(last_post_at desc);
create index if not exists idx_posts_topic on public.webstrefa_forum_posts(topic_id,created_at);
create index if not exists idx_posts_author on public.webstrefa_forum_posts(author_id);
create index if not exists idx_blog_status on public.webstrefa_blog_posts(status,published_at desc);
create index if not exists idx_comments_post on public.webstrefa_blog_comments(post_id,created_at);
create index if not exists idx_notifications_user on public.webstrefa_notifications(user_id,is_read,created_at desc);

-- ===== RLS =====
alter table public.webstrefa_profiles enable row level security;
alter table public.webstrefa_registration_attempts enable row level security;
alter table public.webstrefa_audit_logs enable row level security;
alter table public.webstrefa_reviews_v2 enable row level security;
alter table public.webstrefa_contacts_v2 enable row level security;
alter table public.webstrefa_forum_categories enable row level security;
alter table public.webstrefa_forum_topics enable row level security;
alter table public.webstrefa_forum_posts enable row level security;
alter table public.webstrefa_forum_reports enable row level security;
alter table public.webstrefa_blog_posts enable row level security;
alter table public.webstrefa_blog_comments enable row level security;
alter table public.webstrefa_notifications enable row level security;
alter table public.webstrefa_bookmarks enable row level security;

-- Server API owns these tables; browser access is intentionally denied.
revoke all on all tables in schema public from anon, authenticated;
grant select,insert,update,delete on all tables in schema public to service_role;

notify pgrst, 'reload schema';