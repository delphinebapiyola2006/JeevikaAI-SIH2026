from sqlalchemy import Column, Integer, String, Float, Text
from app.db import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role_id = Column(String, unique=True, nullable=False)
    job_role = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    qp_code = Column(String)
    nsqf_level = Column(Integer)
    keywords = Column(Text)
    education_min = Column(String)
    employment_mode = Column(String)

class Opportunity(Base):
    __tablename__ = "opportunities"
    id = Column(Integer, primary_key=True)
    opportunity_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    district = Column(String, nullable=False)
    location_type = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    demand_level = Column(String)
    role_id = Column(String)
    source_type = Column(String)
