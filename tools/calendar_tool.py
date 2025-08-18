from datetime import timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(summary, start_time, duration_minutes=30):
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    service = build("calendar", "v3", credentials=creds)

    end_time = start_time + timedelta(minutes=duration_minutes)
    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'},
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return f"✅ Event created: {event.get('htmlLink')}"
