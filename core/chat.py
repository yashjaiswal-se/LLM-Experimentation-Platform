from core.inference import generate_response
from core.history import save_interaction


def start_chat_session(client, assistant, temperature):

    conversation = [
        {
            "role": "system",
            "content": assistant["system_prompt"]
        }
    ]

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Please enter a message.")
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("\nChat session ended.")
            break

        # Add user message to conversation history
        conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Generate response
        result = generate_response(
            client,
            conversation,
            temperature
        )

        # Extract content
        output = result["content"]

        # Display response
        print("\nAssistant:")
        print(output)

        # Display experiment metrics
        print("\n" + "-" * 50)
        print("EXPERIMENT METRICS")
        print("-" * 50)

        print(
            f"Prompt Tokens     : {result['prompt_tokens']}"
        )

        print(
            f"Completion Tokens : {result['completion_tokens']}"
        )

        print(
            f"Total Tokens      : {result['total_tokens']}"
        )

        print(
            f"Response Time     : {result['response_time']:.2f} sec"
        )

        # Store assistant response in memory
        conversation.append(
            {
                "role": "assistant",
                "content": output
            }
        )

        # Persist interaction
        save_interaction(
            assistant["name"],
            temperature,
            "openai/gpt-oss-20b",

            user_input,
            output,

            result["prompt_tokens"],
            result["completion_tokens"],
            result["total_tokens"],
            result["response_time"]
        )