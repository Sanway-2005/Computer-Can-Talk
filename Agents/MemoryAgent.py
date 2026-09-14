from strands import Agent,tool
from strands.models.ollama import OllamaModel

from MyModules.MemoryEngine import MemoryEngine

model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:1.7b"
)

def suppress_events(**kwargs):
    pass

@tool
def save_memory(prompt:str,context:str) -> int:
    """
    The is Tool Helps To SAVE Memory In the Data Base. IF you get New Information about the
    user this tool will help you to SAVE the information in database 
    

    Args:
        prompt: The  prompt You want to store
        context: This is The context Of The thing you stored[3-4]words
        
    """
    memory = MemoryEngine()
    return memory.save_memory(context+" "+prompt)




system_prompt = """
You are a Simple Chatbot Follow User Commands,
and Your TASK is to INTERACT with The User

**NOTES**
1)You will Not Entertain Any Email Related Work
2)You will not Enterain Any Conding Realted Work
3)DO NOT HALUCINATE OR PREDICT ANY INFORMATION


**MUST**
You will USE THE TOOL ONLY WHEN THE USER WILL SAY To SAVE SOMETHING
WHILE USING TOOL ALWAYS ALWAYS PROVIDE CONTEXT WHAT YOU ARE SAVING
"""

agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[save_memory],
    callback_handler=suppress_events
)
memory = MemoryEngine()

def memory_agent(prompt:str):

    aug_p = f"""
USER's Information \n
{memory.recall_memory(prompt)}\n\n

USER QUERY : {prompt}
"""
    return  agent(aug_p)


