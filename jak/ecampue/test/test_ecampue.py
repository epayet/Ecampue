from unittest import TestCase

from jak.ecampue.ecampue import Ecampue
from jak.ecampue.test.test_ecampue_data import *
from datetime import date


class TestEcampue(TestCase):
    def setUp(self):
        self.ecampu = Ecampue()

    def test_getCourses_OneDay(self):
        self._connect()
        classes = self.ecampu.getCourses(date(2014, 02, 17), date(2014, 02, 17))
        self.assertEqual(len(classes), 3)
        self.assertEqual(classes, testCourses[0])

    def test_getCoursesInfo(self):
        self._connect()
        html = self.ecampu.getHtml("02/17/2014")
        courses = self.ecampu.getCoursesInfo(html, datetime(2014, 02, 17), date(2014, 02, 17))
        self.assertEqual(len(courses), 3)
        self.assertEqual(courses, testCourses[0])

    def test_getDates(self):
        self._connect()
        html = self.ecampu.getHtml("02/17/2014")
        dates = self.ecampu.getDates(html, datetime(2014, 02, 17))
        self.assertEqual(dates, expectedDates[0])

    def test_getCaseInfo_FirstCourse(self):
        style = "background-color:#FFDDFF;width:18.85000000000000000000000%;top:105.1500%;left:103.1200%;height:20.3111%;"
        caseInfo = self.ecampu.getCaseInfo(style)
        expectedCaseInfo = {"day": 0, "length": 2, "startHour": 9}
        self.assertEqual(caseInfo, expectedCaseInfo)

    def test_getCaseInfo_AnotherDay(self):
        style = "background-color:#FFDDFF;width:18.85000000000000000000000%;top:157.1500%;left:141.1200%;height:41.3111%;"
        caseInfo = self.ecampu.getCaseInfo(style)
        expectedCaseInfo = {"day": 2, "length": 4, "startHour": 14}
        self.assertEqual(caseInfo, expectedCaseInfo)

    def test_getCourseDay_FirstDay(self):
        day = self.ecampu.getCourseDay(103)
        self.assertEqual(day, 0)

    def test_getCourseDay_ThirdDay(self):
        day = self.ecampu.getCourseDay(141)
        self.assertEqual(day, 2)

    def test_getFirstDayWeeks_OneDay(self):
        weeks = self.ecampu._getFirstDayWeeks(date(2014, 02, 17), date(2014, 02, 17))
        self.assertEqual(len(weeks), 1)
        self.assertEqual(weeks[0], "02/17/2014")

    def test_getFirstDayWeeks_OneDayMiddleWeek(self):
        weeks = self.ecampu._getFirstDayWeeks(date(2014, 02, 19), date(2014, 02, 19))
        self.assertEqual(len(weeks), 1)
        self.assertEqual(weeks[0], "02/17/2014")

    def test_getFirstDayWeeks_OneEntireWeek(self):
        weeks = self.ecampu._getFirstDayWeeks(date(2014, 02, 17), date(2014, 02, 21))
        self.assertEqual(len(weeks), 1)
        self.assertEqual(weeks[0], "02/17/2014")

    def test_getFirstDayWeeks_ThreeWeeks(self):
        weeks = self.ecampu._getFirstDayWeeks(date(2014, 02, 17), date(2014, 03, 3))
        self.assertEqual(len(weeks), 3)
        expectedWeeks = ["03/03/2014", "02/24/2014", "02/17/2014"]
        self.assertEqual(weeks, expectedWeeks)

    def _connect(self):
        self.ecampu.connect("emmanuel.payet", "271ZAC")