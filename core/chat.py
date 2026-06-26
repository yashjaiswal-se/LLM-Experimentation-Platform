from core.inference import generate_response
from core.history import save_interaction

def start_chat_session(client,assistant,temperature):
    conversation=[
        {
            "role":"system",
            "content":assistant["system_prompt"]
        }
    ]
    while True:
        user_input=input("\nYou: ").strip()
        
        if not user_input:
            print("Please enter a message.")
            continue
        
        if user_input.lower() in ["exit","quit"]:
            print("\nChat session ended.")
            break
        conversation.append(
            {
                "role":"user",
                "content":user_input
            }
        )
        output=generate_response(
            client,
            conversation,
            temperature
        )
        print("\nAssistant:")
        print(output)
        conversation.append(
         {
        "role": "assistant",
        "content": output
        }
        )
        save_interaction(
         assistant["name"],
        temperature,
        "openai/gpt-oss-20b",
        user_input,
        output
        )