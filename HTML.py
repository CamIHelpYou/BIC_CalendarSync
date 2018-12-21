'''
Created on Oct 19, 2018

@author: camli
'''

from requests import get
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from contextlib import closing
from Class import Month
from bs4 import BeautifulSoup

import datetime

def getDates(user, password):
    '''
    Returns a list of month class types of each month (including this month) for the next 6 months from now.
    Also gets the raw html for each month
    '''

    dates = []
    today = datetime.date.today()
    today = datetime.date(today.year, today.month, 1)
    epochTime = datetime.datetime(today.year, today.month, 1).timestamp()
    url = 'https://xcalendar.cisco.com/index.php?VIEWDATE=' + str(epochTime) + '&VIEWTYPE=month&GROUP=sspt-dna-us&FILTER=0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
    tmpMonth = Month(today.month, today.year, epochTime, simple_get(url, user, password))
    dates.append(tmpMonth)

    for x in range(1,6):
        if today.month == 12:
            today = datetime.date(today.year + 1, 1, 1)
        else:
            today = datetime.date(today.year, today.month + 1, 1)
        epochTime = datetime.datetime(today.year, today.month, 1).timestamp()
        url = 'https://xcalendar.cisco.com/index.php?VIEWDATE=' + str(epochTime) + '&VIEWTYPE=month&GROUP=sspt-dna-us&FILTER=0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
        tmpMonth = Month(today.month, today.year, epochTime, simple_get(url, user, password))
        dates.append(tmpMonth)

    return dates

def simple_get(url, user, password):
    '''
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    '''
    try:
        with closing(get(url, auth=HTTPBasicAuth(user, password))) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    '''
    Returns True if the response seems to be HTML, False otherwise.
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):

    '''
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    '''
    print(e)
