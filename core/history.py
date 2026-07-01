import json

from datetime import datetime
from pathlib import Path


def save_interaction(
    assistant_name: str,
    temperature: float,
    model: str,
    prompt: str,
    response: str,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    response_time: float,
):
    history_path = Path("history/interactions.json")

    interaction = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "assistant": assistant_name,
        "temperature": temperature,
        "model": model,

        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,

        "response_time": round(response_time, 3),

        "prompt": prompt,
        "response": response,

        "prompt_length": len(prompt),
        "response_length": len(response),
        "response_word_count": len(response.split())
    }

    try:

        if history_path.exists():

            with open(
                history_path,
                "r",
                encoding="utf-8"
            ) as file:

                history = json.load(file)

        else:
            history = []

        history.append(interaction)

        with open(
            history_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    except Exception as e:

        print(
            f"Failed to save interaction: {e}"
        )