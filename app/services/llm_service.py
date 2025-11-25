import os, json, re
from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "osr_prompt.txt")

def extract_json(text: str) -> str:
    start = text.find("{")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{": depth += 1
        elif text[i] == "}": depth -= 1
        if depth == 0:
            return text[start:i+1]
    raise ValueError("JSON not found")

async def generate_osr(description: str) -> Dict[str, Any]:
    prompt = open(PROMPT_PATH).read().format(description=description)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content
    return json.loads(extract_json(content))
