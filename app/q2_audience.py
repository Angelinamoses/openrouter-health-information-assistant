from app.llm import ask_llm


MODEL = "liquid/lfm-2.5-2.6b:free"


def explain_for_audience(term, audience):

    system_prompt = f"""
You are a health informatics educational assistant.

Explain the medical term "{term}" specifically for a {audience}.

Adapt:
- language
- terminology
- depth of explanation
- examples

Keep the explanation educational and accurate.
"""

    user_prompt = f"Explain {term} to a {audience}."


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

    return ask_llm(messages, MODEL)


audiences = [
    "10-year-old child",
    "patient",
    "nurse",
    "medical student",
    "Health Informatics student"
]


term = "Hypertension"


for audience in audiences:

    print("\n" + "=" * 70)
    print("AUDIENCE:", audience)
    print("=" * 70)

    response = explain_for_audience(term, audience)

    if response:
        print(response)
    else:
        print("Error: No response received.")