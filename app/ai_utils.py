import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_summary(text: str) -> str:
    response = model.generate_content(f"You are the summarization expert. Read the following text and summarize it clearly: {text}")
    return response.text

def generate_response_from_prompt(prompt: str) -> str:
    response = model.generate_content(f"Generate content based on this prompt: {prompt}")
    return response.text
