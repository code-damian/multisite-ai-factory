const crypto=require('crypto');
const {sb}=require('./_db');
const SITE='https://site-multisite-ai-factory.vercel.app';
const url=()=>process.env.SUPABASE_URL;
const pub=()=>process.env.SUPABASE_PUBLISHABLE_KEY||process.env.SUPABASE_ANON_KEY;
const secret=()=>process.env.SUPABASE_SECRET_KEY||process.env.SUPABASE_SERVICE_ROLE_KEY;
async function authFetch(path,options={}){const r=await fetch(url()+'/auth/v1/'+path,{...options,headers:{apikey:pub(),'Content-Type':'application/json',...(options.headers||{})}});const t=await r.text();let d;try{d=t?JSON.parse(t):null}catch{d={raw:t}}if(!r.ok)throw new Error(d?.msg||d?.message||d?.error_description||d?.error||'Błąd autoryzacji');return d}
async function adminFetch(path,options={}){const k=secret();const r=await fetch(url()+'/auth/v1/admin/'+path,{...options,headers:{apikey:k,Authorization:'Bearer '+k,'Content-Type':'application/json',...(options.headers||{})}});const t=await r.text();let d;try{d=t?JSON.parse(t):null}catch{d={raw:t}}if(!r.ok)throw new Error(d?.msg||d?.message||d?.error||'Błąd administracyjny Auth');return d}
async function currentUser(req){const h=req.headers.authorization||'';if(!h.startsWith('Bearer '))return null;try{return await authFetch('user',{headers:{Authorization:h}})}catch{return null}}
async function profileFor(id){const rows=await sb('webstrefa_profiles?select=*&id=eq.'+encodeURIComponent(id));return rows[0]||null}
async function requireUser(req){const u=await currentUser(req);if(!u)return {error:'Zaloguj się, aby kontynuować.',status:401};const p=await profileFor(u.id);if(!p)return {error:'Profil użytkownika nie został jeszcze utworzony.',status:409};if(p.is_banned)return {error:'To konto jest zablokowane.',status:403};await sb('webstrefa_profiles?id=eq.'+u.id,{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({last_seen_at:new Date().toISOString(),updated_at:new Date().toISOString()})});return {user:u,profile:p}}
function hashIp(ip){return crypto.createHash('sha256').update((process.env.AUTH_SECRET||'webstrefa-rate')+'|'+ip).digest('hex')}
module.exports={SITE,authFetch,adminFetch,currentUser,profileFor,requireUser,hashIp};