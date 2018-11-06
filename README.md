# BIC_CalendarSync

Purpose: This script parses the HTML information from xCal for BICs, sorts this information, and pushes to a set of defined Google Calendars through Google Calendar's APIs. <br />

Will need the following libraries installed:<br />
    import datetime<br />
    import re<br />
    from googleapiclient.discovery import build<br />
    from httplib2 import Http<br />
    from oauth2client import file, client, tools<br />
    import getpass<br />
    from bs4 import BeautifulSoup<br />

Will also need to visit: https://developers.google.com/calendar/quickstart/python to create a 'credentials.json' file to use the google calendar APIs<br />
NOTE*: Google calendar APIs will have the same permissions as the user who created the credentials.json
