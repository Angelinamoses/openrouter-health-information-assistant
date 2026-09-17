import json
from app.llm import ask_llm


MODEL = "liquid/lfm-2.5-2.6b:free"


def get_health_json(condition):

    system_prompt = """
You are a health informatics educational assistant.

Return the information as valid JSON.

The JSON must contain exactly these fields:

condition
definition
risk_factors
symptoms
diagnosis
prevention

Do not include markdown.
Do not include explanations outside the JSON.
"""

    user_prompt = f"Provide structured information about {condition}."


    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = ask_llm(messages, MODEL)

    return response


result = get_health_json("Diabetes mellitus")

print("\nRAW MODEL OUTPUT:")
print(result)


try:

    # Remove Markdown code fences if the model adds them
    cleaned_result = result.strip()

    if cleaned_result.startswith("```json"):
        cleaned_result = cleaned_result[7:]

    if cleaned_result.endswith("```"):
        cleaned_result = cleaned_result[:-3]

    data = json.loads(cleaned_result)

    print("\nJSON VALIDATION:")
    print("Valid JSON")

    print("\nCONDITION:")
    print(data["condition"])

    print("\nDEFINITION:")
    print(data["definition"])

    print("\nRISK FACTORS:")
    for risk in data["risk_factors"]:
        print("-", risk)

    print("\nSYMPTOMS:")
    for symptom in data["symptoms"]:
        print("-", symptom)

    print("\nDIAGNOSIS:")
    for item in data["diagnosis"]:
        print("-", item)

    print("\nPREVENTION:")
    for item in data["prevention"]:
        print("-", item)


except json.JSONDecodeError:
    print("\nJSON VALIDATION:")
    print("Invalid JSON")