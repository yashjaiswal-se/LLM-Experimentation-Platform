from core.client import get_api_client
from core.chat import start_chat_session

from ui.menus import (
    get_assistant_type,
    get_temperature
)


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

    start_chat_session(
        client,
        assistant,
        temperature
    )


if __name__ == "__main__":
    main()