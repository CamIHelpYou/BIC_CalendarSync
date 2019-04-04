'''
Created on Oct 19, 2018

@author: camli
'''


class Month(object):
    def __init__(self, month, year, epoch, html):
        self.month = month
        self.year = year
        self.epoch = epoch
        self.html = html


class Event(object):
    def __init__(self, BIC, Beeper, date, name, east, west):
        self.BIC = BIC
        self.Beeper = Beeper
        self.date = date
        self.name = name
        self.east = east
        self.west = west
        self.oncall = ''

def BodyBIC(event):
    '''
    creates body for BIC calendar event
    '''
    body = {
        'end': {
            'date': event.date.strftime('%Y-%m-%d')
                        },
        'start': {
            'date': event.date.strftime('%Y-%m-%d')
                        },
        'summary': event.name + ' (' + event.oncall + ') - BIC'
    }

    return body

def BodyBeep(event):
    '''
    creates body for BIC calendar event
    '''
    body = {
        'end': {
            'date': event.date.strftime('%Y-%m-%d')
                        },
        'start': {
            'date': event.date.strftime('%Y-%m-%d')
                        },
        'summary': event.name + ' - Beeper'
    }

    return body


east = ['Alonso', 'Akshay', 'Ana', 'Bryan', 'Dan', 'Julio', 'Omar', 'Ray', 'Stephen', 'Sufian', 'Titus']

west = ['Ahsan', 'Cameron', 'Jon', 'Martin', 'Rahul', 'Ron', 'Roy', 'Silpa', 'Santiago']

monthMatch = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                  'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

nameMatch = {
    'acorredo': 'Alonso',
    'aguckin': 'Alex',
    'ahhaq': 'Ahsan',
    'aksmanch': 'Akshay',
    'anarami': 'Ana',
    'bhnegi': 'Bheem',
    'bfenlaso': 'Bryan',
    'camli': 'Cameron',
    'danirowe': 'Dan',
    'jalejand': 'Jon',
    'julijime': 'Julio',
    'mromeroa': 'Martin',
    'oriverav': 'Omar',
    'raywhiti': 'Ray',
    'roharrin': 'Roy',
    'rosimpki': 'Ron',
    'scherrav': 'Silpa',
    'sincadaz': 'Santiago',
    'spmann': 'Sean',
    'tpoulose': 'Titus',
    }

Calendars = [
    { 'name': 'BICS', 'id': '71bttebnjrf4aei0mmrot9ar5g@group.calendar.google.com'},
    { 'name': 'Cameron', 'id': 'cdl3022@gmail.com'},
    { 'name': 'Santiago', 'id': 'k9do3dsnml9f1t2hhgohb4nkm0@group.calendar.google.com'},
    { 'name': 'Ana', 'id': 'ptp7f56msrfe4j3hso1g8s5vc4@group.calendar.google.com'},
    { 'name': 'Titus', 'id': 'ajnp0kaduucav7k2nv0tsqd6v4@group.calendar.google.com'},
    { 'name': 'Ron', 'id': 'hlfk5gqetcr58laad9ismhcmqk@group.calendar.google.com'},
    { 'name': 'Silpa', 'id': '16ug28r67jfa5gd9afng0qtl14@group.calendar.google.com'}
     ]
