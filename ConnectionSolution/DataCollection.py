# Author: Jakub Lisowski, Jlisowskyy

class WorkerData:
    def GatherInfo(self) -> str:
        return "lack of info"


class LinkedinData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    # TODO:
    def GatherInfo(self):
        return "linkedin"


class FacebookData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    def GatherInfo(self) -> str:
        return "fb"
    