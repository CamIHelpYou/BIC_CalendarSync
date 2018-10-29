#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

'''
Created on Oct 17, 2018

@author: camli
'''

from HTML import getDates
from Parse import getEvents
from Calendar import modifyCal
import getpass

def main():

    user = input("User: ")
    password = getpass.getpass("Password: ")
    print("Gathering Dates...")
    print("If you get stuck here, the user/password is probably incorrect")
    dates = getDates(user, password)
    print("Creating Events...")
    Events = getEvents(dates)
    modifyCal(Events)
    print("done")

if __name__ == '__main__':
    main()
