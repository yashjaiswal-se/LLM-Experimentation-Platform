import os
import sys

from core.client import get_api_client
from core.history import save_interaction
from core.inference import generate_response
from ui.menus import get_assistant_type, get_temperature

def main():
    client = get_api_client()

    assistant = get_assistant_type()

    temperature = get_temperature()

    print("\n" + "=" * 50)
    print("EXPERIMENT CONFIGURATION")
    print("=" * 50)

    print(f"Assistant: {assistant['name']}")
    print(f"Temperature: {temperature}")

    print("\nReady for inference...")

    user_input = input("\nEnter your prompt: ")

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

    save_interaction(
        assistant["name"],
        temperature,
        "openai/gpt-oss-20b",
        user_input,
        output
    )


if __name__ == "__main__":
    main()