from __future__ import print_function
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

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

# Example usage
send_email("jlisowskyy@gmail.com", "kuba to kupka", "siema fhehe")