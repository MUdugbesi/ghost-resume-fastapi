from pydantic import BaseModel;
from typing import List, Dict;

# --- /ai-enhance --- 
class AIEnhanceReq(BaseModel):
    section: str
    content: str

class AIEnhanceRes(BaseModel):
    enhanced_content: str
    enhanced_message: str

# --- save resume --- 
class EducationItem(BaseModel):
     school: str
     year: str

class ExperienceItem(BaseModel):
     title: str
     roles: str

class Resume(BaseModel):
     name: str
     education: List[EducationItem]
     experience: List[ExperienceItem]
     skills: List[str]

