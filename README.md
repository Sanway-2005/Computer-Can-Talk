# Computer-Can-Talk
I have build an Ai assistant that can do help you do debug or write code for you , check your mail draft a mail , remember your personal details forever 

## HOW TO RUN THE AI ASSISTANT

### STEP-1
1) Download The Entire Code Base From The Git HUb
2) open the .env file
<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/15adede2-b03f-411d-be23-6c47cafb4ec9" />
 
3)Fill The email account with your email **Recommended Use Test mail**
  
4) Fill the Email Password **This is not your Email Password**
5) go to the link  [Link Text]https://myaccount.google.com/
6) Use the Search bar and Type App Password and click it 

  <img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/05db2590-470b-4ed0-909c-d5f3d2760dfd" />

7)Write App name Of your choice and click create and copy that password and put it into the env file under EMAIL_PASSWORD

        
### STEP-2
1) Download Python Version 3.10.9 https://www.python.org/

2)Download **OLLAMA**

<img width="600" height="700" alt="image" src="https://github.com/user-attachments/assets/d9b31a44-541a-4bf5-9143-d1494bd34757" />

3) Open Terminal and go to the Folder where all the files is Located

<img width="600" height="447" alt="image" src="https://github.com/user-attachments/assets/11897b3b-110a-4ca3-8fc4-2f992fee82c7" />

### STEP-3 
1) **TYPE THE FOLLOWING COMMANDS**

a)ollama pull qwen3:1.7b

b) python -m venv .venv

c) .venv\Scripts\activate

d) pip install -r req.txt

e)clear

f) python Agents\app.py

WOOOOOO THE AGENT IS NOW ONLINE DEMO :-

<img width="1467" height="322" alt="image" src="https://github.com/user-attachments/assets/c8cc814d-0411-4114-8d1f-c293f9fd9035" />

## AGENTS COMMANDS

COMMANDS
C:[your Prompt] {Coding agent will reply}

W1:[Your Prompt] {Email Analist will reply who can Check your mail}

**Remember Only The memory Agent will remember your name Whom Your taliking without any Command**
