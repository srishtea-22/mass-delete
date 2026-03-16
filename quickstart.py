import os.path
import argparse

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  # take arguments from user
  parser = argparse.ArgumentParser(description="Delete emails by keyword, sender or both")

  parser.add_argument("--sender", help="Email address of the sender")
  parser.add_argument("--keyword", help="Keyword to search for in emails")

  args = parser.parse_args()

  if not args.keyword and not args.sender:
    parser.error("Plese provide at least one of --sender or --keyword")
  
  try:
    filter_emails(args, creds)

  except HttpError as error:
    print(f"An error occurred: {error}")


def filter_emails(args, creds):
    query_parts = []
    if args.sender:
      query_parts.append(f"from:{args.sender}")
    if args.keyword:
      query_parts.append(args.keyword)

    query = " ".join(query_parts)

    service = build("gmail", "v1", credentials=creds)
    emails = service.users().messages().list(userId="me", q=query).execute()
    print(emails)


if __name__ == "__main__":
  main()