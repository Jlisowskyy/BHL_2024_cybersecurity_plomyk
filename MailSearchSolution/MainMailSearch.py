from imapclient import IMAPClient
import mailparser
import email
import imaplib
import email
from email.utils import parseaddr


class MailScraper:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def get_outlook_emails(self):
        with IMAPClient(self.host) as server:
            server.login(self.username, self.password)
            server.select_folder('INBOX')
            messages = server.search(['ALL', ])  # in your case: ['FROM', 'email@outlook.example']

            # for each unseen email in the inbox
            for uid, message_data in server.fetch(messages, 'RFC822').items():
                 email_message = email.message_from_bytes(message_data[b"RFC822"])
                 # subject = email_message.subject.decode('utf-8')
                 subject2 = email_message.get("Subject")
                 print(email_message.get("From"), subject2)

            for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
                envelope = data[b'ENVELOPE']
                subject = envelope.subject.decode('utf-8')
                print('ID #%d: "%s" received %s' % (msgid, subject, envelope.date))


if __name__ == '__main__':
    # LogicTest()
    username = 'cyberplomyk@outlook.com'
    password = ''
    host = 'imap-mail.outlook.com'
    mailScraper = MailScraper(host, username, password)
    mailScraper.get_outlook_emails()
