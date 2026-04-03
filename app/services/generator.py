import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def clean_text(text: str):
    # remove Hindi (Devanagari script)
    return re.sub(r'[\u0900-\u097F]+', '', text)


def generate_answer(query, docs):
    context = "\n\n".join([clean_text(d) for d in docs])

    prompt = f"""
You are a strict legal information extraction system.

RULES:
- Answer ONLY in English
- Do NOT use Hindi or any other language
- Extract only factual information
- Be short and precise

QUESTION:
{query}

CONTEXT:
{context}

FORMAT:
Stolen Item:
Brand:
Model:
Final Answer (1 line):
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text