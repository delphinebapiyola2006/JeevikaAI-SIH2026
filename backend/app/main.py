from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import Base, engine, get_db
from app.models.models import Role, Opportunity
from app.schemas import ProfileIn
from app.services.recommender import recommend

Base.metadata.create_all(bind=engine)
app = FastAPI(title="JeevikaAI API",version="1.0.0",description="Voice-first livelihood mapping and NSQF recommendation prototype.")

app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@app.get("/api/health")
def health(): return {"status":"ok","service":"JeevikaAI API"}

@app.get("/api/languages")
def languages(): return {"languages":["English","Tamil","Hindi","Kannada","Telugu","Malayalam"]}

@app.get("/api/roles")
def roles(search:str=Query("",max_length=100),db:Session=Depends(get_db)):
    q=db.query(Role)
    if search:
        like=f"%{search.lower()}%"
        q=q.filter(func.lower(Role.job_role).like(like) | func.lower(Role.keywords).like(like))
    return [{"role_id":r.role_id,"job_role":r.job_role,"sector":r.sector,"qp_code":r.qp_code,"nsqf_level":r.nsqf_level,"keywords":r.keywords,"education_min":r.education_min,"employment_mode":r.employment_mode} for r in q.all()]

@app.get("/api/opportunities")
def opportunities(district:str="",db:Session=Depends(get_db)):
    q=db.query(Opportunity)
    if district: q=q.filter(func.lower(Opportunity.district)==district.lower())
    return [{"opportunity_id":o.opportunity_id,"title":o.title,"sector":o.sector,"district":o.district,"location_type":o.location_type,"latitude":o.latitude,"longitude":o.longitude,"demand_level":o.demand_level,"role_id":o.role_id,"source_type":o.source_type} for o in q.all()]

@app.post("/api/profile")
def profile(p:ProfileIn):
    return {"profile_id":"DEMO-"+p.name.replace(" ","-").upper()[:20],"profile":p.model_dump(),"consent":"prototype-demo"}

@app.post("/api/recommend")
def recommendations(p:ProfileIn,db:Session=Depends(get_db)):
    roles=db.query(Role).all()
    opps=db.query(Opportunity).all()
    counts={}
    for o in opps: counts[o.role_id]=counts.get(o.role_id,0)+(1 if o.demand_level=="High" else .5)
    role_data=[{"role_id":r.role_id,"job_role":r.job_role,"sector":r.sector,"qp_code":r.qp_code,"nsqf_level":r.nsqf_level,"keywords":r.keywords or "","education_min":r.education_min or "8th","employment_mode":r.employment_mode or "Both"} for r in roles]
    return {"profile":p.model_dump(),"recommendations":recommend(p.model_dump(),role_data,counts)[:5]}

@app.get("/api/dashboard")
def dashboard(db:Session=Depends(get_db)):
    roles=db.query(Role).all(); opps=db.query(Opportunity).all()
    sectors={}; demand={}
    for o in opps:
        sectors[o.sector]=sectors.get(o.sector,0)+1
        demand[o.demand_level]=demand.get(o.demand_level,0)+1
    return {"beneficiaries_profiled":1284,"training_recommended":714,"training_enrolled":498,"completed":361,"employed":247,"self_employed":114,"role_count":len(roles),"opportunity_count":len(opps),"sector_counts":sectors,"demand_counts":demand,"data_status":"DEMO / SYNTHETIC"}
