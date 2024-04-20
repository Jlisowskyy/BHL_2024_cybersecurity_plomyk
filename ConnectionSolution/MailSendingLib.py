# Autor: Jakub Lisowski, Jlisowskyy

import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    # Function performs full mail sending logic with to desired u
    def SendPreparedEmail(self, emailTitle: str, emailContent: str, srcMail: str, dstMail: str, passwd: str, link: str):
        emailContent = InplaceSrcEmailInMail(emailContent, srcMail)
        emailContent = InplaceLinkInMail(emailContent, link)

        self.SendMail(srcMail, passwd, dstMail, emailTitle, emailContent)

    @staticmethod
    def GenerateDummyLink(seq:str):
        return f"127.0.0.1/{seq}"


# Wrapping class assuming constant sending user
class UserMailSender:
    __srcMail: str
    __srcPasswd: str
    __sender: MailSender

    def __init__(self, server: str, port: int, mail: str, passwd: str):
        self.__srcMail = mail
        self.__srcPasswd = passwd
        self.__sender = MailSender(server, port)

    def SendMail(self, emailTitle: str, emailContent: str, dstMail: str, link: str = ""):
        self.__sender.SendPreparedEmail(emailTitle, emailContent, self.__srcMail, dstMail, self.__srcPasswd, link)


# Class used to send corporate courseMails
class Notifier:
    __sender: UserMailSender

    def __init__(self, server, port, mail, passwd):
        self.__sender = UserMailSender(server, port, mail, passwd)

    def NotifyAboutCourse(self, targetMail):
        self.__sender.SendMail("Chlopie ogarnij sie", "Powinienes udac sie na kurs z cybersecurity", targetMail)

