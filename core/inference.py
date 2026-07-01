import openai
from openai import OpenAI


def generate_response(
    client: OpenAI,
    messages: list,
    temperature: float,
) -> dict:
    """
    Generate a response from the LLM and return
    both the content and usage metrics.

    Args:
        client: OpenAI client instance.
        messages: Conversation history.
        temperature: Creativity parameter.

    Returns:
        Dictionary containing response text and metrics.
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=temperature,
        )

        return {
            "content": response.choices[0].message.content,
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
            "response_time": response.usage.total_time,
        }

    except openai.AuthenticationError:
        return {
            "content": "Authentication Failed: Invalid API Key.",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "response_time": 0,
        }

    except openai.APIConnectionError:
        return {
            "content": "Network Error: Unable to reach server.",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "response_time": 0,
        }

    except openai.APIStatusError as e:
        return {
            "content": f"API Error ({e.status_code}): {e.message}",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "response_time": 0,
        }

    except Exception as e:
        return {
            "content": f"Unexpected Error: {str(e)}",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "response_time": 0,
        }