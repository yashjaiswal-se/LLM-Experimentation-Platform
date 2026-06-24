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

