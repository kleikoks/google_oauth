from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/business.manage"]


def obtain_creds():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def create_service():
    creds = obtain_creds()
    try:
        service = build("mybusinessaccountmanagement", "v1", credentials=creds)
    except HttpError as err:
        print(err)


def main():
    create_service()


if __name__ == "__main__":
    main()

# https://console.cloud.google.com/home/dashboard
# https://discovery.googleapis.com/discovery/v1/apis
# https://googleapis.github.io/google-api-python-client/docs/dyn

