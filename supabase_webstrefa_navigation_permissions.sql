alter table public.webstrefa_forum_categories add column if not exists min_role text not null default 'public' check (min_role in ('public','user','moderator','admin'));
alter table public.webstrefa_forum_topics add column if not exists min_role text not null default 'public' check (min_role in ('public','user','moderator','admin'));
update public.webstrefa_forum_categories set min_role='public' where min_role is null;
create index if not exists idx_forum_categories_role on public.webstrefa_forum_categories(min_role);
create index if not exists idx_forum_topics_role on public.webstrefa_forum_topics(min_role);
notify pgrst,'reload schema';