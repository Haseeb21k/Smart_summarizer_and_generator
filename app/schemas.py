from pydantic import BaseModel
from datetime import datetime

class text_input(BaseModel):
    text: str

class text_output(BaseModel):
    id: int
    summary_text: str
    created_at: datetime

    class Config:
        orm_mode = True