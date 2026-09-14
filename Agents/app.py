from CoderAgent import coder_assistant
from EmailAgent import Worker_agent
from MemoryAgent import memory_agent
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

console = Console()
def run_agent(user_input:str):
    if user_input == '-help':
        return "W1: your prompt(Email Analyzer) \n W2: your prompt(Email Drafter)\nC: your prompt(Coding helper)"
    if user_input.startswith('C:'):
        user_input = user_input.replace("C:",'').strip()
        return coder_assistant(user_input)
    
    elif user_input.startswith('W1:') or user_input.startswith('W2:'):
        return Worker_agent(user_input)

    else:
        return memory_agent(user_input.strip())
    

console.print(Panel(Align.center("ASSISTANT IS ONLINE."),style="bold purple"))

while True:

    user_input = prompt(
    HTML('<b><ansigreen>You: </ansigreen></b>'),
    placeholder=HTML('<style fg="ansibrightblack">  Type -help...</style>')
)
    if not user_input:
        continue
    elif user_input in ['quit','exit']:
        break

    with console.status("[bold yellow]...Thinking...[/bold yellow]",spinner="arc"):
        response =str(run_agent(user_input=user_input))

    console.print(
    Panel(
        response,
        title="AGENT",
        title_align="center",
        style="white"
    )
)
    
    