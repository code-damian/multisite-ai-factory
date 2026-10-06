const crypto=require('crypto');
const {sb}=require('./_db');
const {requireUser}=require('./_auth');

function clean(v,n=10000){return String(v??'').trim().slice(0,n)}
function slugify(s){return clean(s,180).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,120)+'-'+crypto.randomBytes(3).toString('hex')}

module.exports=async(req,res)=>{
 try{
  const q=req.query||{};
  const action=clean(q.action||req.body?.action);

  if(req.method==='GET'&&action==='categories'){
   const c=await sb('webstrefa_forum_categories?select=*&order=sort_order.asc');
   return res.json({categories:c});
  }

  if(req.method==='GET'&&action==='topics'){
   const cat=clean(q.category);
   let path='webstrefa_forum_topics?select=id,title,slug,is_pinned,is_locked,views_count,replies_count,last_post_at,created_at,webstrefa_profiles(username,first_name,last_name,avatar_url,role,last_seen_at)&is_hidden=eq.false&order=is_pinned.desc,last_post_at.desc&limit=60';
   if(cat)path+='&category_id=eq.'+encodeURIComponent(cat);
   const t=await sb(path);
   return res.json({topics:t});
  }

  if(req.method==='GET'&&action==='topic'){
   const id=clean(q.id);
   if(!id)return res.status(400).json({error:'Brak tematu.'});
   const rows=await sb('webstrefa_forum_topics?select=*,webstrefa_profiles(username,first_name,last_name,avatar_url,role,last_seen_at)&id=eq.'+encodeURIComponent(id));
   if(!rows.length)return res.status(404).json({error:'Temat nie istnieje.'});
   const posts=await sb('webstrefa_forum_posts?select=id,body,is_hidden,edited_at,created_at,author_id,webstrefa_profiles(username,first_name,last_name,avatar_url,role,last_seen_at)&topic_id=eq.'+encodeURIComponent(id)+'&order=created_at.asc');
   const authors=[...new Set(posts.map(x=>x.author_id))];
   const stats={};
   for(const a of authors){
    const [pp,tt]=await Promise.all([
     sb('webstrefa_forum_posts?select=id&author_id=eq.'+encodeURIComponent(a)),
     sb('webstrefa_forum_topics?select=id&author_id=eq.'+encodeURIComponent(a))
    ]);
    stats[a]={posts:pp.length,topics:tt.length};
   }
   posts.forEach(x=>x.author_stats=stats[x.author_id]||{posts:0,topics:0});
   await sb('webstrefa_forum_topics?id='+encodeURIComponent(id),{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({views_count:(rows[0].views_count||0)+1})});
   return res.json({topic:rows[0],posts});
  }

  const me=await requireUser(req);
  if(me.error)return res.status(me.status).json({error:me.error});
  const u=me.user,p=me.profile;

  if(req.method==='POST'&&action==='topic'){
   const category=clean(req.body.categoryId),title=clean(req.body.title,180),body=clean(req.body.body,10000);
   if(title.length<5||body.length<2)return res.status(400).json({error:'Podaj tytuł i treść tematu.'});
   const c=await sb('webstrefa_forum_categories?select=id,is_locked&id=eq.'+encodeURIComponent(category));
   if(!c.length)return res.status(404).json({error:'Kategoria nie istnieje.'});
   if(c[0].is_locked&&!['admin','moderator'].includes(p.role))return res.status(403).json({error:'Ta kategoria jest zamknięta.'});
   const t=await sb('webstrefa_forum_topics',{method:'POST',headers:{Prefer:'return=representation'},body:JSON.stringify({category_id:category,author_id:u.id,title,slug:slugify(title),last_post_by:u.id})});
   const topic=t[0];
   await sb('webstrefa_forum_posts',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({topic_id:topic.id,author_id:u.id,body})});
   await sb('webstrefa_forum_topics?id='+topic.id,{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({replies_count:1,last_post_at:new Date().toISOString()})});
   return res.status(201).json({topic});
  }

  if(req.method==='POST'&&action==='post'){
   const topicId=clean(req.body.topicId),body=clean(req.body.body,10000);
   if(body.length<2)return res.status(400).json({error:'Treść posta jest za krótka.'});
   const rows=await sb('webstrefa_forum_topics?select=id,is_locked,is_hidden&is_hidden=eq.false&id=eq.'+encodeURIComponent(topicId));
   if(!rows.length)return res.status(404).json({error:'Temat nie istnieje.'});
   if(rows[0].is_locked&&!['admin','moderator'].includes(p.role))return res.status(403).json({error:'Temat jest zamknięty.'});
   const ins=await sb('webstrefa_forum_posts',{method:'POST',headers:{Prefer:'return=representation'},body:JSON.stringify({topic_id:topicId,author_id:u.id,body})});
   const cur=await sb('webstrefa_forum_topics?select=replies_count&id='+encodeURIComponent(topicId));
   await sb('webstrefa_forum_topics?id='+encodeURIComponent(topicId),{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({replies_count:(cur[0]?.replies_count||0)+1,last_post_at:new Date().toISOString(),last_post_by:u.id,updated_at:new Date().toISOString()})});
   return res.status(201).json({post:ins[0]});
  }

  if(req.method==='POST'&&action==='report'){
   const postId=clean(req.body.postId),topicId=clean(req.body.topicId),reason=clean(req.body.reason,120),details=clean(req.body.details,2000);
   if(!reason)return res.status(400).json({error:'Wybierz powód zgłoszenia.'});
   await sb('webstrefa_forum_reports',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({reporter_id:u.id,post_id:postId||null,topic_id:topicId||null,reason,details})});
   return res.json({ok:true});
  }

  return res.status(400).json({error:'Nieznana operacja forum.'});
 }catch(e){
  console.error(e);
  return res.status(500).json({error:e.message||'Forum error.'});
 }
};