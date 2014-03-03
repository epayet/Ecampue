# coding: utf-8

from datetime import datetime
import pytz
from icalendar import vCalAddress, vText, Calendar, Event
import tempfile, os

def createICalFile(courses, name="default.ics", path=os.getcwd()):
    cal = Calendar()

    #Some properties are required to be compliant:
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    for course in courses:
        event = Event()
        summary = course["name"]
        if isinstance(course["prof"], basestring):
            summary += " : " + course["prof"]
        event.add('summary', summary)
        event.add('dtstart', datetime(course["dateStart"].year, course["dateStart"].month, course["dateStart"].day, course["dateStart"].hour-1, 0, 0, tzinfo=pytz.utc))
        event.add('dtend', datetime(course["dateEnd"].year, course["dateEnd"].month, course["dateEnd"].day, course["dateEnd"].hour-1, 0, 0, tzinfo=pytz.utc))
        #event.add('dtstamp', datetime(2014, 2, 22, 0, 10, 0, tzinfo=pytz.utc))

        #A property with parameters. Notice that they are an attribute on the value:
        organizer = vCalAddress('MAILTO:noone@example.com')

        #Automatic encoding is not yet implemented for parameter values, so you must use the ‘v*’ types you can import from the icalendar package (they’re defined in icalendar.prop):
        organizer.params['cn'] = vText(course["prof"])
        organizer.params['role'] = vText('CHAIR')
        event['organizer'] = organizer
        event['location'] = vText('EPSI')

        event['uid'] = course["dateStart"].strftime("%Y-%m-%d%H:%M") + '/27346262376@mxm.dk'
        event.add('priority', 5)

        attendee = vCalAddress('MAILTO:maxm@example.com')
        attendee.params['cn'] = vText('Etudiant')
        attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
        event.add('attendee', attendee, encode=0)

        attendee = vCalAddress('MAILTO:the-dude@example.com')
        attendee.params['cn'] = vText('The Dude')
        attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
        event.add('attendee', attendee, encode=0)
        #Add the event to the calendar:
        cal.add_component(event)

    #Write to disk:
    if path is None:
        path = os.getcwd()
    f = open(os.path.join(path, name), 'wb')
    f.write(cal.to_ical())
    f.close()

def createSimpleICalFile():
    cal = Calendar()

    #Some properties are required to be compliant:
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')
    #We need at least one subcomponent for a calendar to be compliant:
    event = Event()
    event.add('summary', 'Python meeting about calendaring')
    event.add('dtstart', datetime(2014,2,22,8,0,0,tzinfo=pytz.utc))
    event.add('dtend', datetime(2014,2,22,10,0,0,tzinfo=pytz.utc))
    event.add('dtstamp', datetime(2014,2,22,0,10,0,tzinfo=pytz.utc))

    #A property with parameters. Notice that they are an attribute on the value:
    organizer = vCalAddress('MAILTO:noone@example.com')

    #Automatic encoding is not yet implemented for parameter values, so you must use the ‘v*’ types you can import from the icalendar package (they’re defined in icalendar.prop):
    organizer.params['cn'] = vText('Max Rasmussen')
    organizer.params['role'] = vText('CHAIR')
    event['organizer'] = organizer
    event['location'] = vText('Odense, Denmark')

    event['uid'] = '20050115T101010/27346262376@mxm.dk'
    event.add('priority', 5)

    attendee = vCalAddress('MAILTO:maxm@example.com')
    attendee.params['cn'] = vText('Max Rasmussen')
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)

    attendee = vCalAddress('MAILTO:the-dude@example.com')
    attendee.params['cn'] = vText('The Dude')
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)
    #Add the event to the calendar:
    cal.add_component(event)

    #Write to disk:
    f = open(os.path.join(os.getcwd(), 'example.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()