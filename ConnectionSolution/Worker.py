from TestTypeClasses import *
from DataCollection import *

class Worker:
    name: str
    surname: str
    mail: str
    dataset: list[LinkedinData]
    lastTest: float
    tests: list[LinkTestCase]
    context: dict[dict[str,str,str,list[str]]] = {}

    # context is of structure:
    #
    # context = {
    #    'linkedin' = {
    #        "name_surname": str,
    #        "organization": str,
    #        "description": str,
    #        "posts": list[str],
    #    }
    # }
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