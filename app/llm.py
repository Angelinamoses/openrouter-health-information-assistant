import os
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"

API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_llm(messages, model):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=60
    )

    if response.status_code == 200:

        result = response.json()

        return result["choices"][0]["message"]["content"]

    else:

        print("API Error:", response.status_code)
        print(response.text)

        return None