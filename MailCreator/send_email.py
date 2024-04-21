from __future__ import print_function
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
from generete_mail import create_phishing_mail

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_email(to, subject, body):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_290268868296-3iqk2egh3ocsrpoqfn7fb7emmnfhaoau.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    send_message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message to {to} Message Id: {send_message["id"]}')


def send_email_linkedin(to, content):
    dict = create_phishing_mail(content)
    send_email(to, dict["temat"], dict["mail"])

# Example usage
send_email_linkedin("kmichaxx@gmail.com","""POST:
With the great pleasure I would like to announce that I am an ambassador of Wyciskarka Potencjału x NewsUp

I encourage you to join me, apply till the 16th of April!

OSOBA:
Gabriela Gacek
XXII Liceum Ogólnokształcące im. Jose Marti WarszawaXXII Liceum Ogólnokształcące im. Jose Marti Warszawa
English
Project Management / Content Creator / Social Activist / Speaker / Marketing team of #niezamłodzi / Ambasador of Wyciskarka Potencjału / Teacher at Webkorki
""")