import MainFlowLib as mfl

class DbMaintainer:
    db : mfl.DepartmentsDb
    shouldMaintain: bool = True

    def __init__(self, depDB: mfl.DepartmentsDb):
        self.db = depDB

    def StartMaintaining(self, checkIntervalSecs: float):
        while self.shouldMaintain:
            self.db.ProcessTick()
