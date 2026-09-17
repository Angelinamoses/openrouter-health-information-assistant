from app.config import SYSTEM_PROMPT
from app.llm import ask_llm


def main():

    print("=" * 50)
    print("     LOCAL HEALTH INFORMATION ASSISTANT")
    print("=" * 50)

    print("\nEducational information only.")
    print("This is not a substitute for professional medical advice.\n")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    while True:

        question = input("Ask a question: ")

        if question.lower().strip() == "exit":
            print("Goodbye!")
            break

        if not question.strip():
            continue

        messages.append({
            "role": "user",
            "content": question
        })

        answer = ask_llm(messages)

        if answer:

            print("\nAssistant:")
            print(answer)
            print()

            messages.append({
                "role": "assistant",
                "content": answer
            })


if __name__ == "__main__":
    main()