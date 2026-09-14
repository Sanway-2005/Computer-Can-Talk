from strands import Agent
from strands.models.ollama import OllamaModel
from MyModules.MemoryEngine import MemoryEngine
from MyModules.EmailEngine import EMAILMANAGER


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:1.7b"
)


email_manager = EMAILMANAGER()
memory = MemoryEngine()
def suppress_events(**kwargs):
    pass

email_analyst = Agent(

    model=model,

    tools=[
        email_manager.process_unread_emails
    ],

    system_prompt="""
You are an Email Analysit , You Analyze Unread Emails, and You can INTERACT with User

**IF AND ONLY IF user request to check mail do the following**
Step 1:
process_unread_emails()
Step 2:
Give Summary To The User 
Summary Formate :
Content : 2-3 Lines Of Explanation
category : News,Blog, Job , Etc
Urgency : 1-10 How much urgent Is To Reply

**DO NOT**
1)Asking User about the user's Gamil


**YOU ARE ONLY ALLOWED TO CALL THE TOOL ONES PER QUERY**
""",
callback_handler=suppress_events
)

email_drafter = Agent(
    model=model,
    tools=[email_manager.send_email,memory.recall_memory],
    system_prompt="""
    You are an Email Drafter Agent. You can Write Emails and Send, and You can INTERACT with User

    **IF AND ONLY IF user REQUEST to write or draft or send mail do the following**
    - Ask the subject and content of the email.
    - never ask user's Email you wont be needing that the you have required tool for sending email
    - Write a professional email body.
    - Use a polite and natural tone.
    - Keep the email concise.
    - *Always Fetch the INFORMATION about the USER by recall_memory tool*
    - Do not invent important information such as names, dates, or facts.
    - If the user specifies a tone such as formal, friendly, apologetic,
      or urgent, follow that tone.


    *MUST*
    **Before sending Confirm With the User**
    """,
    callback_handler=suppress_events
)


email_manager.connect_impa()

def Worker_agent(prompt:str):

    if prompt.startswith("W2:"):
        prompt = prompt.replace("W2:","",1).strip()
        response =email_drafter(prompt)
    else:
        prompt = prompt.replace("W1:","",1).strip()
        response =email_analyst(prompt) 

    return response

