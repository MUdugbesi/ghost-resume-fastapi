# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import AIEnhanceReq, Resume
import json


app = FastAPI()

RESUME_STORAGE_PATH = 'saved_resume.json'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/ai-enhance")
def ai_enhance(req: AIEnhanceReq):
    enhancedMessage = f" Enhanced: {req.content.strip().capitalize()} with better language and tone."
    content = req.content.strip().capitalize()
    return {"enhanced_content": content, "enhanced_message": enhancedMessage}


# save resume as json
@app.post("/save-resume")
def save_resume(resume: dict):
    # save resume to json file
    with open(RESUME_STORAGE_PATH, "w") as f:
        json.dump(resume, f, indent=2)
    return {"status": 'Resume Saved Successfully!'}