import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_user_session(log_text):
    messages = [
        {"role": "system", "content": "You are an assistant that summarizes system or user log files into plain language."},
        {"role": "user", "content": f"Summarize this log file:\n{log_text}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

