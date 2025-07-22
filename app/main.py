from fastapi import FastAPI
from app.routes import summarize
from app.db import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(summarize.router)