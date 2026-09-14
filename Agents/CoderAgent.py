import os
from strands import Agent,tool
from strands.models.ollama import OllamaModel

@tool
def create_file(file_name: str, extension: str,location="C:/"):
    """
    This Tool helps to create a file 

    Args:
        file_name: name of the file
        extension: the extension(name) of the file 
        location: by default C Drive  
    """
    
    file_path = os.path.join(location, f"{file_name}.{extension}")
    open(file_path, "w").close()
    return f"File: {file_name}.{extension} Has Been Created in \n{file_path}"

@tool
def write_file(file_path:str, content:str):
    """
    This Tool helps to Write Some Content int the File 

    Args:
        file_path: The File Location 
        content: The content of the file
    """
    try:
        with open(file_path, "w") as file:
            file.write(f"{content}")
    except Exception as e:
        return f"Error : \n{e}"

@tool
def read_file(file_path:str,n:int):
    """
    This Tool helps to Read the content in the file and View it in Notepad
    
    Args:
        file_path: the Location Of the File 
        n: 1 to open the file in notepad default is 0
    """
    if n==1:
        os.system(f'notepad "{file_path}"')

    with open(file_path, "r") as file:
        content = file.read()

    return content
def suppress_events(**kwargs):
    pass


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:1.7b"
)

agent = Agent(model=model,
              tools=[create_file,write_file,read_file],

system_prompt = """
You are a Coding Assistant. You write, read, and debug code using the available file tools.

**IF AN ONLY IF**
USER want anything to open in notepad use the tool read_file with n value 1
""",
callback_handler=suppress_events
)


def coder_assistant(prompt:str):

    return agent(prompt=prompt)

