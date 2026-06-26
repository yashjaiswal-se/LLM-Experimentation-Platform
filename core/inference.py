import os
import sys

import openai
from openai import OpenAI
def generate_response(
    client: OpenAI,
    messages: list,
    temperature: float,
) -> str:

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
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