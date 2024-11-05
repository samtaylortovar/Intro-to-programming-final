import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]
print("If it doesn't apply/skip, press enter")
event_name_1 = input("what is the event name? ")
description_1 = input("What is the description of the event? ")
location_1 = input("What is the location of the event? ")
event_day_start = input("Enter the event start date (YYYY-MM-DD): ")
event_time_start = input("Enter the event start time (HH:MM): ")
event_day_end = input(f"Enter the event end date (YYYY-MM-DD)(if same day, skip) [default: {event_day_start}]: ") or event_day_start
event_time_end = input("Enter the event end time (HH:MM): ")
attendee_1 = input("Please type the email of the attendee: ")

start_date_time = f"{event_day_start}T{event_time_start}:00"
end_date_time = f"{event_day_end}T{event_time_end}:00"

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
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

    try:
        service = build("calendar", "v3", credentials=creds)
        event = {
            'summary': event_name_1,
            'location': location_1,
            'description': description_1,
            'start': {
                'dateTime': start_date_time,
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end_date_time,
                'timeZone': 'America/Los_Angeles',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': [
                {'email': 'ilovecalanderssomuch@gmail.com'},
               
            ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"\nEvent '{event.get('summary')}' created successfully!")
        print(f"Location: {event.get('location')}")
        print(f"Start Time: {event['start']['dateTime'][:10]} {event['start']['dateTime'][11:19]}")
        print(f"End Time: {event['end']['dateTime'][:10]} {event['end']['dateTime'][11:19]}")

    except HttpError as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()

