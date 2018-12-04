'''
Created on Oct 19, 2018

@author: camli
'''
from bs4 import BeautifulSoup
from Class import Event, monthMatch, nameMatch, east, west

import re
import datetime
def getEvents(dates):
    '''
    This function takes Month objects and parses all the events, returning an Array of Event objects
    '''
    Events = []
    for date in dates:
        soup = BeautifulSoup(date.html, 'html.parser')
        createEvents(soup.get_text(), date, Events)
    return Events

def createEvents(text, date, Events):
    '''
    Gets passed a web page to parse. Returns calendar events for the given month
    '''
    text = text.split("\n")
    month = 0
    day = 0
    Beepers = []

    for line in text:
        monthSearch = re.search(r'(?<=\s-\s[1]\s-\s)\w+', line)
        daySearch = re.search(r'(\s-\s)([0-9]+)(\s-\s)', line)
        bicName = re.search(r'(\w+)(\s-\sBIC)', line)
        beepName = re.search(r'(\w+)(\s-\sBeeper)', line)
        Holiday = re.search(r'(\w+)(\s-\sPH)', line)

        if monthSearch is not None:
            if month is 0:
                month = monthMatch[monthSearch.group(0)]
            else:
                break

        if daySearch is not None:
            day = int(daySearch.group(2))

        if bicName is not None:
            if nameMatch.get(bicName.group(1)) is None:
                print(bicName.group(1) + " is not defined")
                name = ""
            else:
                name = nameMatch[bicName.group(1)]
            if name in east:
                tmpEvent = Event(True, False, datetime.date(date.year, month, day), name, True, False)
                Events.append(tmpEvent)
            elif name in west:
                tmpEvent = Event(True, False, datetime.date(date.year, month, day), name, False, True)
                Events.append(tmpEvent)

        if beepName is not None:
            if nameMatch.get(beepName.group(1)) is None:
                print(bicName.group(1) + " is not defined")
                name = ""
            else:
                name = nameMatch[beepName.group(1)]
                tmpEvent = Event(False, True, datetime.date(date.year, month, day), name, False, False)
                Events.append(tmpEvent)
                Beepers.append(tmpEvent)

        if Holiday is not None:
            if nameMatch.get(Holiday.group(1)) is None:
                print(bicName.group(1) + " is not defined")
                name = ""
            else:
                name = nameMatch[Holiday.group(1)]
            if name in east:
                tmpEvent = Event(True, False, datetime.date(date.year, month, day), name, True, False)
                Events.append(tmpEvent)
            elif name in west:
                tmpEvent = Event(True, False, datetime.date(date.year, month, day), name, False, True)
                Events.append(tmpEvent)

    Events = insertBeeper(Beepers, Events)


def insertBeeper(Beepers, Events):
    '''
    Inserts whoever is on call (beeper) into the event objects. Returns modified Events array
    '''
    for beep in Beepers:
        for event in Events:
            if beep.date == event.date:
                if beep.name == event.name:
                    continue
                else:
                    event.oncall = beep.name
    return Events
