# Author: Jakub Lisowski, Jlisowskyy

# This whole class was supposed to scrape different media for data about a worker. 
# But it was never implemented since it's resolved differently in the final solution.
# For the demo, we simply scrape everyones linkedin profile at the beginning of the program.

class WorkerData:
    def GatherInfo(self) -> str:
        raise NotImplementedError


class LinkedinData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    def GatherInfo(self):
        raise NotImplementedError


class FacebookData(WorkerData):
    link: str

    def __init__(self, link: str):
        self.link = link

    def GatherInfo(self) -> str:
        raise NotImplementedError
    