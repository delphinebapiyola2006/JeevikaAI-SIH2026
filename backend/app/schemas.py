from pydantic import BaseModel, Field
from typing import List

class ProfileIn(BaseModel):
    name: str = "Demo Beneficiary"
    language: str = "Tamil"
    education: str = "12th"
    family_occupation: str = ""
    current_occupation: str = ""
    skills: List[str] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list)
    mobility: str = "Local"
    employment_preference: str = "Either"
    district: str = "Coimbatore"
