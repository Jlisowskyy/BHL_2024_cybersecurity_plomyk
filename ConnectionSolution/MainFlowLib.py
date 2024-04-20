# Author: Jakub Lisowski, Jlisowskyy

import json
import time


# Class is used to store whole groups of workers

class WorkerData:
    def GatherInfo(self) -> str:
        return "lack of info"


class LinkedinData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    def GatherInfo(self):
        return "linkedin"


class FacebookData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    def GatherInfo(self) -> str:
        return "fb"


class TestCase:
    code: str
    start: float
    exp: int

    def IsExpired(self) -> bool:
        expSecs = float(self.exp * 3600 * 24)
        return time.time() > expSecs + self.start

    def IsClicked(self) -> bool:
        return False

    def IsReported(self) -> bool:
        return False

class Worker:
    name: str
    surname: str
    mail: str
    dataset: list[WorkerData]
    lastTest: float
    tests: list[TestCase]

    def __init__(self, name: str, surname: str, mail: str, dataset: list[WorkerData], points=0, lastTest=time.time()):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.dataset = dataset
        self.points = points
        self.lastTest = lastTest
        self.tests = list()

    def TestTime(self, interval: float) -> bool:
        actTime = time.time()
        return (actTime - self.lastTest) > interval


class Department:
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

    def PerformPhishingTest(self, worker: Worker):
        pass


    @staticmethod
    def ProcessWorkerTestCase(worker: Worker, test: TestCase):
        pass
    def CheckTests(self):
        for worker in self.workers:
            for test in worker.tests:
                self.ProcessWorkerTestCase(worker, test)




class DepartmentsDb:
    __departments: dict[str, Department]

    def __init__(self):
        self.__departments = dict()

    def AddDepartment(self, department: Department):
        if self.__departments.get(department.desc) is None:
            self.__departments[department.desc] = department

    def AddToDepartment(self, departmentDesc: str, worker: Worker):
        if self.__departments.get(departmentDesc) is not None:
            self.__departments[departmentDesc].workers.append(worker)

    def SetDepartmentInterval(self, departmentDesc: str, interval: int):
        dep = self.__departments.get(departmentDesc)
        if dep is not None:
            dep.interval = interval

    def SetDepartmentReportPoints(self, departmentDesc: str, reportPoints: int):
        dep = self.__departments.get(departmentDesc)
        if dep is not None:
            dep.reportPoints = reportPoints

    def SetDepartmentMissPoints(self, departmentDesc: str, missPoints: int):
        dep = self.__departments.get(departmentDesc)
        if dep is not None:
            dep.missPoints = missPoints

    def SetDepartmentClickPoints(self, departmentDesc: str, clickPoints: int):
        dep = self.__departments.get(departmentDesc)
        if dep is not None:
            dep.clickPoints = clickPoints

    def SetDepartmentCourseThreshold(self, departmentDesc: str, courseThreshold: int):
        dep = self.__departments.get(departmentDesc)
        if dep is not None:
            dep.courseThreshold = courseThreshold

    def ProcessTick(self):
        for key, dep in self.__departments.items():
            interval = dep.interval
            intervalInSecs = float(interval * 3600 * 24)

            for worker in dep.workers:
                if worker.TestTime(intervalInSecs):
                    worker.PerformPhishingTest()