import json

from datetime import datetime
from pathlib import Path

def save_interaction(
    assistant_name: str,
    temperature: float,
    model: str,
    prompt:str,
    response: str
):
    history_path=Path("history/interactions.json")
    
    interaction={
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "assistant": assistant_name,
        "temperature": temperature,
        "model": model,
        "prompt": prompt,
        "response": response
    }
    
    try:
        if history_path.exists():
            with open(history_path,"r",encoding="utf-8") as file:
                history=json.load(file)
        else:
            history=[]
            
        history.append(interaction)
        
        with open(history_path,"w",encoding="utf-8") as file:
            json.dump(history,file,indent=4)
    except Exception as e:
        print(f"Failed to save interaction: {e}")
        