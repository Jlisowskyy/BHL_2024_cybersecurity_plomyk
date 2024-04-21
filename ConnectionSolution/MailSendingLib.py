# Autor: Jakub Lisowski, Jlisowskyy

import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from future import print_function
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path


# Function replaces link token inside mail content string
def InplaceLinkInMail(emailContent: str, link: str) -> str:
    return emailContent.replace("[link_token]", link)


def InplaceSrcEmailInMail(emailContent: str, mail: str) -> str:
    return emailContent.replace("[mail token]", mail)


# Class used to implement main mail sending logic
class MailSender:
    __serverName: str
    __serverPort: int

    def __init__(self, server="smtp.gmail.com", port=465):
        self.__serverName = server
        self.__serverPort = port

    def SendMail(self, srcMail, srcPasswd, dstMail, title, msg):
        # Preparing mail msg
        message = MIMEMultipart()
        message['From'] = srcMail
        message['To'] = dstMail
        message['Subject'] = title

        message.attach(MIMEText(msg, 'plain'))

        print(f"[ LOG ] Prepared msg:\n{message.as_string()}")

        with smtp.SMTP_SSL(self.__serverName, self.__serverPort) as server:
            server.login(srcMail, srcPasswd)
            server.sendmail(srcMail, srcMail, message.as_string())

        print("[ LOG ] Message sent")

    def SendMailWithGmailApi(self, dstMail, title, msg):
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']

        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'configs/client_secret_290268868296-3iqk2egh3ocsrpoqfn7fb7emmnfhaoau.apps.googleusercontent.com.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        message = MIMEText(msg)
        message['to'] = dstMail
        message['subject'] = title
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print("[ LOG ] Message sent")

    # Function performs full mail sending logic with to desired u
    def SendPreparedEmail(self, emailTitle: str, emailContent: str, srcMail: str, dstMail: str, link: str):
        emailContent = InplaceSrcEmailInMail(emailContent, srcMail)
        emailContent = InplaceLinkInMail(emailContent, link)

        self.SendMailWithGmailApi(dstMail, emailTitle, emailContent)

    @staticmethod
    def GenerateDummyLink(seq: str):
        return f"127.0.0.1/{seq}"


# Wrapping class assuming constant sending user
class UserMailSender:
    __srcMail: str
    __srcPasswd: str
    __sender: MailSender

    def __init__(self, mail: str):
        self.__srcMail = mail
        self.__sender = MailSender()

    def SendMail(self, emailTitle: str, emailContent: str, dstMail: str, link: str = ""):
        self.__sender.SendPreparedEmail(emailTitle, emailContent, self.__srcMail, dstMail, link)


# Class used to send corporate courseMails
class Notifier:
    __sender: UserMailSender

    def __init__(self, mail):
        self.__sender = UserMailSender(mail)

    def NotifyAboutCourse(self, targetMail):
        self.__sender.SendMail("Chlopie ogarnij sie", "Powinienes udac sie na kurs z cybersecurity", targetMail)
