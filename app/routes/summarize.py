# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.db import SessionLocal
# from app import models, schemas
# from app.ai_utils import get_summary

# router = APIRouter(prefix="/summarize", tags=["summarize"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/", response_model=schemas.text_output)
# def summarize_text(data: schemas.text_input, db: Session = Depends(get_db)):
#     summary = get_summary(data.text)

#     db_summary = models.Summary(real_text=data.text, summary_text=summary)
#     db.add(db_summary)
#     db.commit()
#     db.refresh(db_summary)

#     return db_summary