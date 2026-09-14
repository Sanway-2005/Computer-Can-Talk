import os
import imaplib
import smtplib

from email.header import decode_header
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from strands import tool
from email.message import EmailMessage
import email

load_dotenv()



class EMAILMANAGER :
    def __init__(self):
        self.password = os.getenv("EMAIL_PASSWORD")
        self.email_user = os.getenv("EMAIL_ACCOUNT")
        self.imap_server = os.getenv("IMAP_SERVER")



    @tool
    def connect_impa(self):
        """
        THIS TOOL HELPS TO LOGGIN TO THE USER ACCOUNT , NO PASSWWORD NOTHING NEEDED
        THIS TOOL AUTOMATICALLY HELPS TO CONNECT THE USER'S GMAIL
        """
        try:
            self.mail = imaplib.IMAP4_SSL(self.imap_server)
            self.mail.login(user=self.email_user,password=self.password)
            return f"Successfully Logged in to <{self.email_user}>"
        except Exception as e:
            return f"Error \n{e}"

    def clean_text(self,raw_html):
        soup = BeautifulSoup(raw_html,"html.parser")
        return soup.get_text(separator=' ',strip=True)

    @tool
    def process_unread_emails(self):
        """
        This Tool helps to Process User's Unread Emails 
        """
        
        self.mail.select("inbox")

        status,message = self.mail.search(None,"UNSEEN")
        email_ids = message[0].split()[-1]

        _,msg_data = self.mail.fetch(email_ids,"(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part,tuple):
                msg = email.message_from_bytes(response_part[1])

                subject ,encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject,bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")

                sender = msg.get("From")

                body =""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if "attachment" not in content_disposition:
                            if content_type == "text/plain":
                                body += part.get_payload(decode=True).decode()
                            elif content_type == "text/html":
                                html_content = part.get_payload(decode=True).decode()
                                body += self.clean_text(html_content)
                else:
                    payload = msg.get_payload(decode=True)

                    if payload:
                        body = payload.decode("utf-8", errors="ignore")
                    body = self.clean_text(body)

        prompt = f"""
        Email Fetched SuccessFully 
        Here is the Fetched Email :


        FROM : {sender}

        SUBJEXT : {subject}

        BODY : {body[:2000]}
"""
        return prompt


    @tool
    def send_email(self,to, subject, body):
        """
        This Tool Helps To Send Email:

        Args:
        to: sender's Email Adress
        subject : Subject of The Email You want To send
        Body : Body OF The Email You Want To Send 
        """

        msg = EmailMessage()

        msg["From"] = self.email_user
        msg["To"] = to
        msg["Subject"] = subject

        msg.set_content(body)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                self.email_user,
                self.password
            )

            smtp.send_message(msg)
            return f"EMAIL SUCCESSFULLY SEND TO <{to}>"







