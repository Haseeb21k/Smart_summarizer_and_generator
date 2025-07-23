# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.ai_utils import generate_response_from_prompt

# router = APIRouter(prefix="/generate", tags=["Generate Content"])

# class PromptInput(BaseModel):
#     prompt: str

# class GenerateOutput(BaseModel):
#     content: str

# @router.post("/", response_model=GenerateOutput)
# def generate_from_prompt(data: PromptInput):
#     content = generate_response_from_prompt(data.prompt)
#     return {"content": content}
