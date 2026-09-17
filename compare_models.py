import time
from app.llm import ask_llm


MODELS = [
    "liquid/lfm-2.5-2.6b:free",
    "qwen/qwen3-30b-a3b:free",
    "google/gemma-4-26b-a4b-it:free"
]


PROMPT = """
Explain electronic health records to a first-year
Health Informatics student in about 100 words.
"""


def count_words(text):
    return len(text.split())


for model in MODELS:

    print("\n" + "=" * 70)
    print("MODEL:", model)
    print("=" * 70)

    start_time = time.perf_counter()

    response = ask_llm(
        [
            {
                "role": "user",
                "content": PROMPT
            }
        ],
        model
    )

    end_time = time.perf_counter()

    latency = end_time - start_time

    if response:

        print("Latency:", round(latency, 2), "seconds")
        print("Word Count:", count_words(response))
        print("\nResponse:")
        print(response)

    else:

        print("Error occurred.")