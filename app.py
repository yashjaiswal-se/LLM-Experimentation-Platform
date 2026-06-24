import os
import sys

from dotenv import load_dotenv
import openai
from openai import OpenAI


def get_api_client() -> OpenAI:
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        sys.exit(
            "Critical Error: GROQ_API_KEY environment variable is missing."
        )

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )


def get_assistant_type():

    assistant_types = {
        "1": {
            "name": "Tutor",
            "description": "Learn concepts in a simple and structured way.",
            "system_prompt": (
                "You are a concise tutor. "
                "Explain concepts clearly with examples."
            ),
        },
        "2": {
            "name": "Researcher",
            "description": "Deep analysis and comparisons.",
            "system_prompt": (
                "You are a detailed researcher. "
                "Provide thorough explanations and comparisons."
            ),
        },
        "3": {
            "name": "Debate Expert",
            "description": "Challenge assumptions and provide counterarguments.",
            "system_prompt": (
                "You are a debate expert. "
                "Present counterarguments and challenge weak reasoning."
            ),
        },
        "4": {
            "name": "Code Reviewer",
            "description": "Review code and suggest improvements.",
            "system_prompt": (
                "You are an experienced code reviewer. "
                "Analyze code quality and suggest improvements."
            ),
        },
    }

    print("\n" + "=" * 50)
    print("AVAILABLE ASSISTANTS")
    print("=" * 50)

    for key, assistant in assistant_types.items():
        print(f"\n{key}. {assistant['name']}")
        print(f"   {assistant['description']}")

    while True:

        choice = input(
            "\nChoose assistant type: "
        ).strip()

        if choice in assistant_types:

            selected = assistant_types[choice]

            print("\nSelected:")
            print(f"{selected['name']}")
            print(f"{selected['description']}")

            return selected

        print("Invalid selection. Try again.")


def get_temperature():

    print("\n" + "=" * 50)
    print("TEMPERATURE GUIDE")
    print("=" * 50)

    print("0.0 - 0.3  -> Deterministic")
    print("0.4 - 0.8  -> Balanced")
    print("0.9 - 1.5  -> Creative")
    print("1.6 - 2.0  -> Highly Random")

    while True:

        try:

            temp = float(
                input("\nEnter temperature (0-2): ")
            )

            if 0 <= temp <= 2:

                print(
                    f"Temperature set to: {temp}"
                )

                return temp

            print(
                "Temperature must be between 0 and 2."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


def generate_response(
    client: OpenAI,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> str:

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=temperature,
        )

        return response.choices[0].message.content

    except openai.AuthenticationError:

        return (
            "Authentication Failed: "
            "Invalid API Key."
        )

    except openai.APIConnectionError:

        return (
            "Network Error: "
            "Unable to reach server."
        )

    except openai.APIStatusError as e:

        return (
            f"API Error ({e.status_code}): "
            f"{e.message}"
        )

    except Exception as e:

        return (
            f"Unexpected Error: {str(e)}"
        )


if __name__ == "__main__":

    client = get_api_client()

    assistant = get_assistant_type()

    temperature = get_temperature()
    
    print("\n"+"="*50)
    print("EXPERIMENT CONFIGURATION")
    print("\n"+"="*50)
    
    print(f"Assistant: {assistant['name']}")
    print(f"temperature: {temperature}")
    
    print("Ready for inference...")

    user_input = input(
        "\nEnter your prompt: "
    )

    output = generate_response(
        client,
        assistant["system_prompt"],
        user_input,
        temperature,
    )

    print("\n" + "=" * 50)
    print("RESPONSE")
    print("=" * 50)

    print(output)