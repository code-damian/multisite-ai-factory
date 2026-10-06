const {sb}=require('./_db');const {requireUser,adminFetch}=require('./_auth');
module.exports=async(req,res)=>{
 try{
  const me=await requireUser(req);if(me.error)return res.status(me.status).json({error:me.error});const a=String(req.body?.action||req.query?.action||'');
  if(req.method==='GET'&&a==='dashboard'){const id=me.user.id;const [topics,posts,comments,reviews]=await Promise.all([
    sb('webstrefa_forum_topics?select=id&author_id=eq.'+id),
    sb('webstrefa_forum_posts?select=id&author_id=eq.'+id),
    sb('webstrefa_blog_comments?select=id&author_id=eq.'+id),
    sb('webstrefa_reviews_v2?select=rating,text,created_at&user_id=eq.'+id)
  ]);return res.json({profile:me.profile,stats:{topics:topics.length,posts:posts.length,comments:comments.length,reviews:reviews.length},reviews})}
  if(req.method==='POST'&&a==='profile'){const b=req.body||{},allowed={first_name:String(b.firstName||'').trim().slice(0,80),last_name:String(b.lastName||'').trim().slice(0,80)||null,bio:String(b.bio||'').trim().slice(0,1000),avatar_url:String(b.avatarUrl||'').trim().slice(0,500)||null,gender:['Kobieta','Mężczyzna','Nie podano'].includes(b.gender)?b.gender:'Nie podano',updated_at:new Date().toISOString()};await sb('webstrefa_profiles?id='+me.user.id,{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify(allowed)});return res.json({ok:true})}
  if(req.method==='POST'&&a==='delete-account'){await adminFetch('users/'+me.user.id,{method:'DELETE'});return res.json({ok:true})}
  return res.status(400).json({error:'Nieznana operacja konta.'});
 }catch(e){console.error(e);return res.status(500).json({error:e.message||'Błąd panelu użytkownika.'})}
};