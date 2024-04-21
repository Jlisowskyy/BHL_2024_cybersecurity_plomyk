# Author: Jakub Lisowski, Jlisowskyy

import json
import threading
import time

import MailSendingLib as mLib

from DataCollection import *
import MailGenerator as mg
import Helpers as hp

class LinkTestCase:
    start: float
    exp: int
    isClicked: bool
    isReported: bool

    def __init__(self, exp: int = 3):
        self.start = time.time()
        self.exp = exp
        self.isReported = False
        self.isClicked = False

    def IsExpired(self) -> bool:
        expSecs = float(self.exp * 3600 * 24)
        return time.time() > expSecs + self.start

    def IsClicked(self) -> bool:
        return self.isClicked

    def IsReported(self) -> bool:
        return self.isReported


class Worker:
    name: str
    surname: str
    mail: str
    dataset: list[LinkedinData]
    lastTest: float
    tests: list[LinkTestCase]

    def __init__(self, name: str, surname: str, mail: str, dataset: list[LinkedinData], points=0, lastTest=time.time()):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.dataset = dataset
        self.points = points
        self.lastTest = lastTest
        self.tests = list()

    # TODO: Scale time accordingly to actual user points
    def ShouldBeTested(self, interval: float) -> bool:
        actTime = time.time()
        return (actTime - self.lastTest) > interval

    def ToDict(self):
        links_strings = []
        for workerData in self.dataset:
            links_strings.append(workerData.link)
        return {
            "name": self.name,
            "surname": self.surname,
            "mail": self.mail,
            "dataset": links_strings,
            "points": self.points,
            "lastTest": self.lastTest,
            "tests": self.tests
        }


class Department:
    Notifier = mLib.Notifier("smtp.gmail.com", 465, "bhlmock1@gmail.com", "jwhybzganebqsgsl")
    ScamSender = mLib.UserMailSender("smtp.gmail.com", 465, "bhlmock1@gmail.com", "jwhybzganebqsgsl")

    desc: str
    interval: int
    reportPoints: int
    missPoints: int
    clickPoints: int
    courseThreshold: int
    workers: list[Worker]

    def __init__(self, desc: str, interval: int = 7, reportPoints: int = 5, missPoints: int = -5,
                 clickPoints: int = -10, courceThreshold: int = -20):
        self.desc = desc
        self.interval = interval
        self.reportPoints = reportPoints
        self.missPoints = missPoints
        self.clickPoints = clickPoints
        self.courseThreshold = courceThreshold
        self.workers = list()

    def PerformPhishingTest(self, worker: Worker, testDB: dict[str, LinkTestCase]):
        test = LinkTestCase()

        keyseq = hp.GenerateRandomSequence(32)
        while testDB.get(keyseq) is not None:
            keyseq = hp.GenerateRandomSequence(32)

        testDB[keyseq] = test

        link = mLib.MailSender.GenerateDummyLink(keyseq)
        [title, content] = mg.GetMailParams(worker.dataset)

        self.ScamSender.SendMail(title, content, worker.mail, link)

    # true -> test finished, false -> test ongoing
    def ProcessWorkerTestCase(self, worker: Worker, test: LinkTestCase) -> bool:
        if test.IsClicked():
            worker.points += self.clickPoints
            return True

        if test.IsExpired():
            worker.points += self.missPoints
            return True

        if test.IsReported():
            worker.points += self.reportPoints
            return True

        return False

    @staticmethod
    def SendNotification(worker: Worker):
        Department.Notifier.NotifyAboutCourse(worker.mail)

    def ProcessWorkerPointsStatus(self, worker: Worker):

        # Worker should attend to cybersecurity courses
        if worker.points < self.courseThreshold:
            self.SendNotification(worker)
            worker.points = 0
            return

    def ProcessTick(self, intervalInSecs: float, testDB: dict[str, LinkTestCase]):

        for worker in self.workers:
            if worker.ShouldBeTested(intervalInSecs):
                self.PerformPhishingTest(worker, testDB)

            ongoingTests = list()

            for test in worker.tests:
                if self.ProcessWorkerTestCase(worker, test):
                    self.ProcessWorkerPointsStatus(worker)
                else:
                    ongoingTests.append(test)

            worker.tests = ongoingTests


class DepartmentsDb:
    __departments: dict[str, Department]
    __ongoingTests: dict[str, LinkTestCase]
    __lock: threading.Lock

    def __init__(self):
        self.__departments = dict()
        self.__ongoingTests = dict()
        self.__lock = threading.Lock()

    def AddDepartment(self, department: Department):
        with self.__lock:
            if self.__departments.get(department.desc) is None:
                self.__departments[department.desc] = department

    def AddToDepartment(self, departmentDesc: str, worker: Worker):
        with self.__lock:
            if self.__departments.get(departmentDesc) is not None:
                self.__departments[departmentDesc].workers.append(worker)

    def SetDepartmentInterval(self, departmentDesc: str, interval: int):
        with self.__lock:
            dep = self.__departments.get(departmentDesc)
            if dep is not None:
                dep.interval = interval

    def SetDepartmentReportPoints(self, departmentDesc: str, reportPoints: int):
        with self.__lock:
            dep = self.__departments.get(departmentDesc)
            if dep is not None:
                dep.reportPoints = reportPoints

    def SetDepartmentMissPoints(self, departmentDesc: str, missPoints: int):
        with self.__lock:
            dep = self.__departments.get(departmentDesc)
            if dep is not None:
                dep.missPoints = missPoints

    def SetDepartmentClickPoints(self, departmentDesc: str, clickPoints: int):
        with self.__lock:
            dep = self.__departments.get(departmentDesc)
            if dep is not None:
                dep.clickPoints = clickPoints

    def SetDepartmentCourseThreshold(self, departmentDesc: str, courseThreshold: int):
        with self.__lock:
            dep = self.__departments.get(departmentDesc)
            if dep is not None:
                dep.courseThreshold = courseThreshold

    def ProcessTick(self):
        with self.__lock:
            for key, dep in self.__departments.items():
                interval = dep.interval
                intervalInSecs = float(interval * 3600 * 24)
                dep.ProcessTick(intervalInSecs, self.__ongoingTests)

    def GetDepartments(self) -> list[Department]:
        return self.__departments.keys()
