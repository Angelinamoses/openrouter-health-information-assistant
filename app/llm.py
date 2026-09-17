import requests

from app.config import OPENROUTER_API_KEY, MODEL_NAME, SYSTEM_PROMPT


URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_llm(messages):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
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

    if response.status_code == 200:

        result = response.json()

        answer = result["choices"][0]["message"]["content"]

        return answer

    else:

        print("API Error:", response.status_code)
        print(response.text)

        return None
def ask_structured(question):

    messages = [
        {
            "role": "system",
            "content": """
You are a health informatics educational assistant.

Return the answer as valid JSON with exactly these fields:

condition
definition
risk_factors
symptoms
diagnosis
prevention

Do not add markdown or extra text.
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    return ask_llm(messages)