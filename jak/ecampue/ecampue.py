from jak.Browser import Browser
from jak.ecampue.constants import *
from datetime import timedelta
from bs4 import BeautifulSoup
from jak.ecampue.constants import *
import re
from datetime import datetime


class Ecampue:

    def __init__(self):
        self._browser = Browser()

    def getCourses(self, dateStart, dateEnd):
        everyCourses = []
        firstDayWeeksRequested = self._getFirstDayWeeks(dateStart, dateEnd)
        for firstDayWeekStr in firstDayWeeksRequested:
            html = self.getHtml(firstDayWeekStr)
            #dateEnd a voir!!!!! en fonction de la semaine (indice de boucle)
            firstDayWeek = self.getDateFromFirstDay(firstDayWeekStr)
            courses = self.getCoursesInfo(html, firstDayWeek, dateEnd)
            everyCourses.extend(courses)
        return everyCourses

    def getCoursesInfo(self, html, firstDayWeek, dateEnd):
        courses = []

        names = self.getCoursesNamesTags(html)
        profs = self.getCoursesProfsTags(html)
        dates = self.getDates(html, firstDayWeek)

        for i in range(len(dates)):
            if dates[i]["dateStart"] <= dateEnd:
                course = {"name": names[i].nextSibling, "prof": profs[i].next, "dateStart": dates[i]["dateStart"], "dateEnd": dates[i]["dateEnd"]}
                courses.append(course)

        return courses

    def getHtml(self, firstDayWeek):
        url = ECAMPUE_URL_EMPLOI_DU_TEMPS + "?date=" + firstDayWeek
        self._browser.open(url)
        html = self._browser.br.response().read()
        return html

    def connect(self, user, mdp):
        self._browser.open(ECAMPUE_URL)
        self._browser.br.select_form(name="loginform")
        self._browser.br["__ac_name"] = user
        self._browser.br["__ac_password"] = mdp
        response2 = self._browser.br.submit()

    def getDates(self, html, firstDayWeek):
        soup = BeautifulSoup(html)
        casesTags = soup.findAll("div", {"class": "Case"})
        dates = []
        for caseTag in casesTags:
            style = caseTag.attrs["style"]
            caseInfo = self.getCaseInfo(style)
            if caseInfo is not None:
                dateStart = firstDayWeek+timedelta(days=caseInfo["day"], hours=caseInfo["startHour"])
                dateEnd = dateStart+timedelta(hours=caseInfo["length"])
                dateInfo = {"dateStart": dateStart, "dateEnd": dateEnd}
                dates.append(dateInfo)
        return dates

    def getCaseInfo(self, style):
        #background-color:#FFDDFF;width:18.85000000000000000000000%;top:157.1500%;left:141.1200%;height:41.3111%;
        m = re.match(r".*top:(\d*\.\d*)%;left:(\d*.\d*)%;height:(\d*.\d*)%;", style)
        if m is not None:
            top = int(float(m.group(1)))
            left = int(float(m.group(2)))
            height = int(float(m.group(3)))

            day = self.getCourseDay(left)
            length = self.getCourseLength(height)
            startHour = self.getCourseStartHour(top)

            return {"day": day, "length": length, "startHour": startHour}
        else:
            return None

    def getCourseDay(self, left):
        days = {103: 0, 122: 1, 141: 2, 161: 3, 180: 4}
        return days[left]

    def getCourseLength(self, height):
        length = {20: 2, 41: 4}
        return length[height]

    def getCourseStartHour(self, top):
        start = {105: 9, 126: 11, 157: 14, 179: 16}
        return start[top]

    def getCoursesNamesTags(self, html):
        soup = BeautifulSoup(html)
        classesNameTags = soup.findAll("div", {"class": "Presence"})
        return classesNameTags

    def getCoursesProfsTags(self, html):
        soup = BeautifulSoup(html)
        classesProfsTags = soup.findAll("td", {"class": "TCProf"})
        return classesProfsTags

    def _getFirstDayWeeks(self, dateStart, dateEnd):
        firstDayWeeks = []
        daysBetween = (dateEnd - dateStart).days
        for i in range(daysBetween+1):
            currentDate = dateEnd-timedelta(days=i)
            weekday = currentDate.weekday()
            firstDayWeek = currentDate-timedelta(days=weekday)
            date = firstDayWeek.strftime("%m/%d/%Y")
            if date not in firstDayWeeks:
                firstDayWeeks.append(date)
        return firstDayWeeks

    def getDateFromFirstDay(self, firstDayStr):
        split = firstDayStr.split("/")
        year = int(float(split[2]))
        month = int(float(split[0]))
        day = int(float(split[1]))
        return datetime(year, month, day)