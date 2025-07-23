from pydantic import BaseModel
from datetime import datetime

class FeatureModelInput(BaseModel):
    task: str
    text: str = None
    prompt: str = None

class FeatureModelOutput(BaseModel):
    result: str

class PromptInput(BaseModel):
    prompt: str

class GenerateOutput(BaseModel):
    content: str

class text_output(BaseModel):
    text: str

class text_input(BaseModel):
    text: str