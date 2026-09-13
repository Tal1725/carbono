import{createClient}from'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.115.0/+esm';

export const supabase=createClient('https://aemnbyxfqzntqztisoum.supabase.co','sb_publishable_plnF9bvrN3oJl0NQw8ZnBw_xb7yLoRk',{auth:{persistSession:true,autoRefreshToken:true,detectSessionInUrl:true}});

export const normalizeUsername=(value)=>String(value||'').trim().replace(/^@/,'').toLowerCase();
export const validUsername=(u)=>/^[a-z0-9_]{3,24}$/.test(u);
const authIdentifier=(u)=>`${u}@accounts.nexo.invalid`;

export async function signUpUsername(username,password,displayName){
  const u=normalizeUsername(username);
  if(!validUsername(u)) throw new Error('O @usuário deve ter 3–24 caracteres: letras, números ou _.');
  if(String(password||'').length<8) throw new Error('A senha precisa ter pelo menos 8 caracteres.');
  const{data,error}=await supabase.auth.signUp({email:authIdentifier(u),password,options:{data:{username:u,display_name:displayName||u}}});
  if(error)throw error;
  if(!data.session) throw new Error('A conta foi criada, mas este projeto exige confirmação de e-mail. Para o NEXO funcionar sem telefone/e-mail visível, desative a confirmação de e-mail no Auth do projeto.');
  return data;
}

export async function signInUsername(username,password){
  const u=normalizeUsername(username);
  if(!validUsername(u)) throw new Error('Digite um @usuário válido.');
  const{data,error}=await supabase.auth.signInWithPassword({email:authIdentifier(u),password});
  if(error)throw error;
  return data;
}

export async function signOut(){return supabase.auth.signOut()}
