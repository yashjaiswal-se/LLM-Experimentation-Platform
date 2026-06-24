import os
import sys

import openai
from openai import OpenAI

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