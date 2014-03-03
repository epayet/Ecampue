# coding: utf-8

from datetime import datetime

testCourses = []
testCourses.append([])
testCourses[0].append({"name": u"mobiles et VoIP", "prof": u"rouchaud philippe ", "dateStart": datetime(2014, 2, 17, 9), "dateEnd": datetime(2014, 2, 17, 11)})
testCourses[0].append({"name": u"Systèmes embarqués", "prof": u"cueille arnaud", "dateStart": datetime(2014, 02, 17, 11), "dateEnd": datetime(2014, 2, 17, 13)})
testCourses[0].append({"name": u"Projet IA & méth. de gestion de ", "prof": u"cueille arnaud", "dateStart": datetime(2014, 2, 17, 14), "dateEnd": datetime(2014, 2, 17, 18)})

expectedDates = []
expectedDates.append([])
expectedDates[0].append({"dateStart": datetime(2014, 2, 17, 9), "dateEnd": datetime(2014, 2, 17, 11)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 17, 11), "dateEnd": datetime(2014, 2, 17, 13)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 17, 14), "dateEnd": datetime(2014, 2, 17, 18)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 18, 9), "dateEnd": datetime(2014, 2, 18, 13)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 18, 14), "dateEnd": datetime(2014, 2, 18, 16)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 18, 16), "dateEnd": datetime(2014, 2, 18, 18)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 19, 9), "dateEnd": datetime(2014, 2, 19, 11)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 19, 11), "dateEnd": datetime(2014, 2, 19, 13)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 19, 14), "dateEnd": datetime(2014, 2, 19, 18)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 20, 9), "dateEnd": datetime(2014, 2, 20, 11)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 20, 11), "dateEnd": datetime(2014, 2, 20, 13)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 20, 14), "dateEnd": datetime(2014, 2, 20, 16)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 20, 16), "dateEnd": datetime(2014, 2, 20, 18)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 21, 9), "dateEnd": datetime(2014, 2, 21, 13)})
expectedDates[0].append({"dateStart": datetime(2014, 2, 21, 14), "dateEnd": datetime(2014, 2, 21, 18)})