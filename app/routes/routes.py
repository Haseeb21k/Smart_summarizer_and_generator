from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_505_HTTP_VERSION_NOT_SUPPORTED
from app.db import SessionLocal
from app import models, schemas
from app.ai_utils import get_summary, generate_response_from_prompt
from app.schemas import PromptInput, GenerateOutput, text_output

# router = APIRouter(prefix="/features", tags=["AI Features"])

# @router.post("/", response_model=schemas.FeatureModelOutput)
# def feature_input(data: schemas.FeatureModelInput):
#     task = data.task.lower()

#     if task == "summarize":
#         if not data.text:
#             raise HTTPException(status_code=400, detail="Text required")
#         result = get_summary(data.text)

#     elif task == "generate":
#         if not data.prompt:
#             raise HTTPException(status_code=400, detail="Prompt is required to generate")
#         result = generate_response_from_prompt(data.prompt)

#     else:
#         raise HTTPException(status_code=400, detail="Invalid Task, Use 'summarize' or 'generate'")

#     return {"result": result}


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/generate", response_model=GenerateOutput)
def generate_from_prompt(data: PromptInput):
    content = generate_response_from_prompt(data.prompt)
    return {"content": content}

@router.post("/summarize", response_model=schemas.text_output)
def summarize_text(data: schemas.text_input, db: Session = Depends(get_db)):
    summary = get_summary(data.text)

    db_summary = models.Summary(real_text=data.text, summary_text=summary)
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return text_output(text=summary)