# coding: utf-8

from jak.ecampue.ecampue import Ecampue
import sys
from datetime import timedelta
import datetime
from jak.ecampue.ecampueCalendar import createICalFile

if __name__ == '__main__':
    ecampu = Ecampue()
    ecampu.connect("emmanuel.payet", "271ZAC")
    now = datetime.datetime.now()
    end = now+timedelta(days=90)
    courses = ecampu.getCourses(now, end)
    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]
    createICalFile(courses, "i4-groupeB.ics", path)