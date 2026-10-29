import os
import requests
import json
from dotenv import load_dotenv

input_text = "Write a function that prints out the Fibonacci sequence up to the 15th term. Assume the first term is 1."

load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")
if not key:
    raise RuntimeError("OpenRouter API key not found in environment variables.")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    },
    data=json.dumps(
        {
            "model": "nvidia/nemotron-3.5-super-vl:free",
            "messages": [
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            "reasoning": {"enabled": True},
        }
    ),
)

response.raise_for_status()
response = response.json()
response = response["choices"][0]["message"]["content"]
print(response)
