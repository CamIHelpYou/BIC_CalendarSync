'''
Created on Oct 22, 2018

@author: camli
'''
import datetime
import re
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from Class import Calendars, BodyBIC, BodyBeep

SCOPES = 'https://www.googleapis.com/auth/calendar'

def modifyCal(Events):
    '''
    Takes in all events and writes them to the calendars defined in Class.py
    '''
    #Google calendar authorization
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    #Call the calendar APIs
    now = datetime.datetime.utcnow()
    now = datetime.datetime(now.year, now.month, 1, 0, 0, 0, 0).isoformat() + 'Z' # 'Z' indicates UTC time
    for cal in Calendars:
        removeEvents(service, cal, now)
        addEvents(Events, service, cal)

def removeEvents(service, cal, now):
    '''
    Removes all BIC or Beeper events from the calendar starting at the begining of the present month
    '''
    print("Removing current events for " + cal["name"])
    events_result = service.events().list(calendarId=cal["id"], timeMin=now,
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    for event in events_result["items"]:
        check = ['BIC', 'Beeper']
        if any(x in event['summary'] for x in check):
            service.events().delete(calendarId=cal["id"], eventId=event["id"], sendNotifications=None, sendUpdates=None).execute()

def addEvents(Events, service, cal):
    '''
    Pushes events to calendars via API
    '''
    print("Pushing events for " + cal["name"])
    if cal["name"] is "BICS":
        for event in Events:
            if event.BIC is True:
                body = BodyBIC(event)
            elif event.Beeper is True:
                body = BodyBeep(event)
            service.events().insert(calendarId=cal["id"], body=body).execute()
    else:
        for event in Events:
            if cal["name"] == event.name:
                if event.BIC is True:
                    body = BodyBIC(event)
                elif event.Beeper is True:
                    body=BodyBeep(event)
                service.events().insert(calendarId=cal["id"], body=body).execute()
