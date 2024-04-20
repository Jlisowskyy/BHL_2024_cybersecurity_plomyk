# Autor: Jakub Lisowski, Jlisowskyy

import smtplib as smtp
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function replaces link token inside mail content string
def InplaceLinkInMail(emailContent: str, link: str) -> str:
    return emailContent.replace("[link_token]", link)

def InplaceSrcEmailInMail(emailContent: str, mail: str) -> str:
    return emailContent.replace("[mail token]", mail)

# Class used to implement main mail sending logic
class MailSender:
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

    # Function performs full mail sending logic with to desired u
    def SendPreparedEmail(self, emailTitle: str, emailContent: str, srcMail: str, dstMail: str, passwd: str, link: str):
        emailContent = InplaceSrcEmailInMail(emailContent, srcMail)
        emailContent = InplaceLinkInMail(emailContent, link)

        self.SendMail(srcMail, passwd, dstMail, emailTitle, emailContent)