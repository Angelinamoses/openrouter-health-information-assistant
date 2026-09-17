import os
import requests


URL = "https://openrouter.ai/api/v1/chat/completions"

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "liquid/lfm-2.5-2.6b:free"


def ask_llm(messages):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": messages
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=60
    )

    print("Status:", response.status_code)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]

    print("API Error:", response.status_code)
    print(response.text)

    return None