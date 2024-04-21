import MainFlowLib as mfl
import DbMaintaining as dbm
import DummyPageHost as dph

class Application:

    def __init__(self, loadPath: str, checkInterval: int = 10):
        self.db = mfl.DepartmentsDb()
        self.__maintainer = dbm.DbMaintainer(self.db)
        self.__interval = checkInterval

    def Run(self):
        dph.RunFlask()
        self.__maintainer.StartMaintaining(self.__interval)

    def StopApplication(self):
        self.__maintainer.StopMaintaining()