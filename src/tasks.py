import os
import httplib2shim

from factory import create_celery, create_app

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from src.helpers.mail_helpers import create_message, send_message

SCOPES = ['https://www.googleapis.com/auth/gmail.modify', "https://www.googleapis.com/auth/calendar"]

celery = create_celery(create_app())


@celery.task(name='send_html_email')
def send_html_email(message_text, email, subject, sender):
    # _dep = create_celery_app()
    # with _dep.app_context():

    httplib2shim.patch()
    CLIENT_SECRET_FILE = 'service.json'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #     # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())
    #     # http_auth = creds.authorize(httplib2shim.Http())
    # service = build('gmail', 'v1', credentials=creds)

    sender = sender
    to = email
    _message_text = message_text
    msg = create_message(sender, to, subject, _message_text)
    send_message(to, msg)
