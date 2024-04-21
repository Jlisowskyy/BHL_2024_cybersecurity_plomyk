import MainFlowLib as mfl
import DbMaintaining as dbm
import DummyPageHost as dph
import ConfigDeserialization as cd

class Application:

    def __init__(self, loadDepartmentPaht: str, loadWorkersPath: str, checkInterval: int = 10):
        self.db = mfl.DepartmentsDb()
        self.__maintainer = dbm.DbMaintainer(self.db)
        self.__interval = checkInterval

        self.LoadDepartments(loadDepartmentPaht)
        self.LoadWorkers(loadWorkersPath)

    def Run(self):
        self.db.BeginScraping()
        dph.RunFlask()
        self.__maintainer.StartMaintaining(self.__interval)

    def StopApplication(self):
        self.__maintainer.StopMaintaining()

    def LoadDepartments(self, loadPath: str):
        with open(loadPath, 'r') as f:
            content = f.read()

        dpList = cd.init_departments(content)
        for dp in dpList:
            self.db.AddDepartment(dp)

    def LoadWorkers(self, WorkersPath: str):
        with open(WorkersPath, 'r') as f:
            content = f.read()

        workers = cd.init_workers(content)
        for dep, worker in workers:
            self.db.AddToDepartment(dep, worker)

    def GetDepartments(self):
        print(','.join(dep for dep in self.db.GetDepartments()))

    def UpdateDepartments(self, departments: str):
        deps = cd.init_departments(departments)
        self.db.UpdateDepartaments(deps)