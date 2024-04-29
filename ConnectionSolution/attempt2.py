import imaplib
import email
from email.header import decode_header
import webbrowser
import os

class ReceivedEmail:
    def __init__(self, text, subject, sender):
        self.text = text
        self.subject = subject
        self.sender = sender


class MessageScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.read_messages = 0

    def get_new_messages(self) -> list[ReceivedEmail]:
        # use your email provider's IMAP server, you can look for your provider's IMAP server on Google
        # or check this page: https://www.systoolsgroup.com/imap/
        # for office 365, it's this:
        imap_server = "outlook.office365.com"

        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL(imap_server)
        # authenticate
        imap.login(self.username, self.password)

        status, messages = imap.select("INBOX")
        # total number of emails
        messages = int(messages[0])

        # list of EmailMessages
        emailMessages = []

        n = self.read_messages
        for i in range(messages, n, -1):
            # update read messages
            self.read_messages = self.read_messages + 1
            # fetch the email message by ID
            message_text = ""
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                message_text += body
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            message_text += body
                    emailMessage = ReceivedEmail(message_text, subject, From)
                    emailMessages.append(emailMessage)
        # close the connection and logout
        imap.close()
        imap.logout()
        return emailMessages


if __name__ == '__main__':
    username = 'cyberplomyk@outlook.com'
    password = ''
    message_scraper = MessageScraper(username, password)
    emailMessages = message_scraper.get_new_messages()
    for message in emailMessages:
        print(message.sender)
        print("--------------------------------")
        print(message.subject)
        print("--------------------------------")
        print(message.text)
        print("--------------------------------")

    print("end of 1st batch===============================")
    emailMessages = message_scraper.get_new_messages()
    for message in emailMessages:
        print(message.sender)
        print("--------------------------------")
        print(message.subject)
        print("--------------------------------")
        print(message.text)
        print("--------------------------------")





