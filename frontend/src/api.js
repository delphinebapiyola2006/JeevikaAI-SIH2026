const api=async(path,opt={})=>{const r=await fetch(path,{headers:{"Content-Type":"application/json",...(opt.headers||{})},...opt});if(!r.ok)throw new Error(await r.text());return r.json()}
export const getDashboard=()=>api("/api/dashboard")
export const getOpportunities=()=>api("/api/opportunities")
export const recommend=p=>api("/api/recommend",{method:"POST",body:JSON.stringify(p)})
