from pathlib import Path
import csv
from app.db import Base, engine, SessionLocal
from app.models.models import Role, Opportunity

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "datasets"

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Role).count() == 0:
            with open(DATA/"nsqf_roles.csv",encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    db.add(Role(role_id=r["role_id"],job_role=r["job_role"],sector=r["sector"],
                        qp_code=r["qp_code"],nsqf_level=int(r["nsqf_level"]),keywords=r["keywords"],
                        education_min=r["education_min"],employment_mode=r["employment_mode"]))
        if db.query(Opportunity).count() == 0:
            with open(DATA/"opportunities.csv",encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    db.add(Opportunity(opportunity_id=r["opportunity_id"],title=r["title"],sector=r["sector"],
                        district=r["district"],location_type=r["location_type"],latitude=float(r["latitude"]),
                        longitude=float(r["longitude"]),demand_level=r["demand_level"],role_id=r["role_id"],
                        source_type=r["source_type"]))
        db.commit()
        print("Database seeded.")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
