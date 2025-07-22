from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True)
    real_text = Column(String, nullable=False)
    summary_text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)