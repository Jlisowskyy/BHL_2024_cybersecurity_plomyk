# Author: Jakub Lisowski, Jlisowskyy

import threading
import MailSendingLib as mLib
import MailGenerator as mg
import Helpers as hp
import TestTypeClasses as ttc
import UpdatingReports
import json

from ws.ws.spiders.Worker import *
import scrape_linkedin as sl

class Department:
    Notifier = mLib.Notifier("bhlmock1@gmail.com")
    ScamSender = mLib.UserMailSender("bhlmock1@gmail.com")

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

    def PerformPhishingTest(self, worker: Worker, testDB: dict[str, ttc.LinkTestCase]):
        test = ttc.LinkTestCase()

        keyseq = hp.GenerateRandomSequence(32)
        while testDB.get(keyseq) is not None:
            keyseq = hp.GenerateRandomSequence(32)

        testDB[keyseq] = test

        link = mLib.MailSender.GenerateDummyLink(keyseq)
        [title, content] = mg.GetMailParams(worker.context, worker.name, worker.surname)

        self.ScamSender.SendMail(title, content, worker.mail, link)
        worker.lastTest = time.time()

    # true -> test finished, false -> test ongoing
    def ProcessWorkerTestCase(self, worker: Worker, test: ttc.LinkTestCase) -> bool:
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

    def ProcessTick(self, intervalInSecs: float, testDB: dict[str, ttc.LinkTestCase]):

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
    ongoingTests: dict[str, ttc.LinkTestCase]
    __lock: threading.Lock

    def __init__(self):
        self.__departments = dict()
        self.ongoingTests = dict()
        self.__lock = threading.Lock()

    def BeginScraping(self):
        workers = self.GetWorkers()

        emails = []
        linkedin_urls = []
        workerList = []

        for worker in workers:
            emails.append(worker[0])
            linkedin_urls.append(worker[1].link)
            workerList.append(worker[2])
        
        # This takes a long time to finish
        sl.crawl_linkedin(emails, linkedin_urls, workerList)


    def AddDepartment(self, department: Department):
        with self.__lock:
            if self.__departments.get(department.desc) is None:
                self.__departments[department.desc] = department

    def AddToDepartment(self, departmentDesc: str, worker: Worker):
        with self.__lock:
            if self.__departments.get(departmentDesc) is not None:
                self.__departments[departmentDesc].workers.append(worker)

    def UpdateDepartaments(self, deps: list[Department]):
        with self.__lock:
            for dep in deps:
                if self.__departments.get(dep.desc) is not None:
                    depToUpdate = self.__departments.get(dep.desc)

                    depToUpdate.interval = dep.interval
                    depToUpdate.missPoints = dep.missPoints
                    depToUpdate.clickPoints = dep.clickPoints
                    depToUpdate.courseThreshold = dep.courseThreshold

    def ProcessTick(self):
        username = 'cyberplomyk@outlook.com'
        password = 'Lukaszjestcyborgiem'

        with self.__lock:
            updater = UpdatingReports.UpdateDatabase(self, username, password)
            updater.UpdateDatabaseReports()

            for key, dep in self.__departments.items():
                interval = dep.interval
                intervalInSecs = float(interval * 3600 * 24)
                dep.ProcessTick(intervalInSecs, self.ongoingTests)

    def GetDepartments(self):
        return self.__departments.keys()
    
    def GetWorkers(self):
        rv = list()
        
        for _, dep in self.__departments.items():
            for worker in dep.workers:
                if len(worker.dataset) != 0:
                    rv.append([worker.mail, worker.dataset[0], worker])

        return rv

    def SaveUsers(self, filepath):
        with self.__lock:
            rv = list()

            for dep in self.__departments.values():
                for worker in dep.workers:
                    rv.append(json.dumps(worker.ToDict()))

            with open(filepath, 'w') as file:
                file.write(json.dumps(rv))
