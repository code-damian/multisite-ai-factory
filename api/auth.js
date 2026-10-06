const {authFetch,adminFetch,profileFor,hashIp,SITE}=require('./_auth');
const {sb}=require('./_db');
const dns=require('dns').promises;
const crypto=require('crypto');
const DISPOSABLE=new Set(['mailinator.com','guerrillamail.com','guerrillamail.org','10minutemail.com','10minutemail.net','temp-mail.org','temp-mail.io','tempmail.com','tempmailo.com','yopmail.com','sharklasers.com','guerrillamailblock.com','getnada.com','emailondeck.com','dispostable.com','trashmail.com','trashmail.me','throwawaymail.com','fakeinbox.com','maildrop.cc','mintemail.com','moakt.com','mailnesia.com','mytemp.email','emailfake.com','fakemail.net','mailpoof.com']);
function clean(v,n=500){return String(v??'').trim().slice(0,n)}
function validDate(v){const d=new Date(v+'T00:00:00');return /^\d{4}-\d{2}-\d{2}$/.test(v)&&!Number.isNaN(d.getTime())&&d<=new Date()}
async function emailAllowed(email){
 const domain=email.split('@')[1]?.toLowerCase()||'';
 if(!domain||DISPOSABLE.has(domain)||domain.includes('tempmail')||domain.includes('temporary')||domain.includes('disposable'))return false;
 try{const mx=await dns.resolveMx(domain);return mx&&mx.length>0}catch{return false}
}
async function rateLimit(ip,email){
 const ih=hashIp(ip),eh=crypto.createHash('sha256').update(email).digest('hex');
 const rows=await sb('webstrefa_registration_attempts?select=id,created_at&ip_hash=eq.'+ih+'&created_at=gte.'+encodeURIComponent(new Date(Date.now()-3600000).toISOString()));
 if(rows.length>=6)throw Object.assign(new Error('Zbyt wiele prób rejestracji. Spróbuj ponownie później.'),{status:429});
 await sb('webstrefa_registration_attempts',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({ip_hash:ih,email_hash:eh})});
}
module.exports=async(req,res)=>{
 try{
  if(req.method==='GET'){
   const h=req.headers.authorization||''; if(!h.startsWith('Bearer '))return res.status(401).json({error:'Brak sesji'});
   const u=await require('./_auth').currentUser(req); if(!u)return res.status(401).json({error:'Sesja wygasła.'});
   const p=await profileFor(u.id); if(!p)return res.status(409).json({error:'Profil nie został znaleziony.'});
   return res.json({user:u,profile:p});
  }
  if(req.method!=='POST')return res.status(405).json({error:'Metoda niedozwolona'});
  const b=req.body||{},action=clean(b.action);
  if(action==='register'){
   if(clean(b.website))return res.status(400).json({error:'Nieprawidłowa rejestracja.'});
   if(Date.now()-Number(b.startedAt||0)<2500)return res.status(400).json({error:'Formularz został wysłany zbyt szybko.'});
   const first=clean(b.firstName,80),last=clean(b.lastName,80),username=clean(b.username,32).toLowerCase(),email=clean(b.email,200).toLowerCase(),password=String(b.password||''),birth=clean(b.birthDate,10),gender=['Kobieta','Mężczyzna','Nie podano'].includes(b.gender)?b.gender:'Nie podano';
   if(first.length<2)return res.status(400).json({error:'Imię musi mieć co najmniej 2 znaki.'});
   if(username.length<5||!/^[a-z0-9._-]+$/.test(username))return res.status(400).json({error:'Login musi mieć minimum 5 znaków i zawierać tylko litery, cyfry, kropkę, myślnik lub podkreślenie.'});
   if(password.length<8)return res.status(400).json({error:'Hasło musi mieć minimum 8 znaków.'});
   if(username===password.toLowerCase())return res.status(400).json({error:'Login nie może być taki sam jak hasło.'});
   if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))return res.status(400).json({error:'Podaj poprawny adres e-mail.'});
   if(!validDate(birth))return res.status(400).json({error:'Podaj prawidłową datę urodzenia.'});
   if(!b.termsAccepted)return res.status(400).json({error:'Zaakceptuj regulamin WebStrefy.'});
   const age=new Date().getFullYear()-new Date(birth+'T00:00:00').getFullYear();if(age<13)return res.status(400).json({error:'Rejestracja jest dostępna od 13 roku życia.'});
   const ip=String(req.headers['x-forwarded-for']||req.socket?.remoteAddress||'unknown').split(',')[0].trim();
   await rateLimit(ip,email);
   if(!(await emailAllowed(email)))return res.status(400).json({error:'Ten adres wygląda na tymczasowy lub nie ma poprawnej konfiguracji pocztowej. Użyj stałego adresu e-mail.'});
   const taken=await sb('webstrefa_profiles?select=id&username=eq.'+encodeURIComponent(username));if(taken.length)return res.status(409).json({error:'Ten login jest już zajęty.'});
   const d=await authFetch('signup',{method:'POST',body:JSON.stringify({email,password,options:{data:{username,first_name:first,last_name:last,gender,birth_date:birth},emailRedirectTo:SITE+'/?auth=confirmed#konto'}})});
   const uid=d.user?.id;if(!uid)throw new Error('Nie udało się utworzyć użytkownika.');
   try{await sb('webstrefa_profiles',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({id:uid,username,first_name:first,last_name:last||null,birth_date:birth,gender,role:'user',terms_accepted_at:new Date().toISOString()})})}catch(e){await adminFetch('users/'+uid,{method:'DELETE'}).catch(()=>{});throw e}
   await sb('webstrefa_audit_logs',{method:'POST',headers:{Prefer:'return=minimal'},body:JSON.stringify({actor_id:uid,action:'registration_created',target_type:'user',target_id:uid,metadata:{email_verification_required:true}})}).catch(()=>{});
   return res.status(201).json({ok:true,requiresEmailConfirmation:true,message:'Konto utworzone. Sprawdź e-mail i kliknij przycisk potwierdzenia. Dopiero wtedy konto będzie aktywne.'});
  }
  if(action==='login'){
   const email=clean(b.email,200).toLowerCase(),password=String(b.password||'');if(!email||!password)return res.status(400).json({error:'Podaj e-mail i hasło.'});
   const d=await authFetch('token?grant_type=password',{method:'POST',body:JSON.stringify({email,password})});
   const p=await profileFor(d.user.id);if(!p)return res.status(409).json({error:'Brak profilu.'});if(p.is_banned)return res.status(403).json({error:'To konto jest zablokowane.'});
   await sb('webstrefa_profiles?id=eq.'+d.user.id,{method:'PATCH',headers:{Prefer:'return=minimal'},body:JSON.stringify({last_seen_at:new Date().toISOString()})});
   return res.json({access_token:d.access_token,refresh_token:d.refresh_token,user:d.user,profile:p});
  }
  if(action==='password-reset'){
   const email=clean(b.email,200).toLowerCase();if(!email)return res.status(400).json({error:'Podaj e-mail.'});
   await authFetch('recover',{method:'POST',body:JSON.stringify({email,gotrue_meta_security:{},redirect_to:SITE+'/?auth=recovery#konto'})});
   return res.json({ok:true,message:'Jeśli konto istnieje, wysłaliśmy wiadomość z instrukcją zmiany hasła.'});
  }
  if(action==='change-password'){
   const token=String(b.accessToken||'');if(!token)return res.status(401).json({error:'Brak sesji.'});const p=String(b.password||'');if(p.length<8)return res.status(400).json({error:'Hasło musi mieć minimum 8 znaków.'});
   await authFetch('user',{method:'PUT',headers:{Authorization:'Bearer '+token},body:JSON.stringify({password:p})});return res.json({ok:true,message:'Hasło zostało zmienione. Otrzymasz również powiadomienie bezpieczeństwa.'});
  }
  if(action==='change-email'){
   const token=String(b.accessToken||''),email=clean(b.email,200).toLowerCase();if(!token||!email)return res.status(400).json({error:'Podaj sesję i nowy e-mail.'});if(!(await emailAllowed(email)))return res.status(400).json({error:'Ten adres e-mail nie jest akceptowany.'});
   await authFetch('user',{method:'PUT',headers:{Authorization:'Bearer '+token},body:JSON.stringify({email,email_redirect_to:SITE+'/?auth=email-changed#konto'})});return res.json({ok:true,message:'Na nowy adres została wysłana wiadomość potwierdzająca zmianę.'});
  }
  return res.status(400).json({error:'Nieznana operacja.'});
 }catch(e){console.error(e);return res.status(e.status||500).json({error:e.message||'Błąd serwera.'})}
};