import threading
import time

import MainFlowLib as mfl


class DbMaintainer:
    db: mfl.DepartmentsDb
    shouldMaintain: bool = True
    __thread: threading.Thread

    def __init__(self, depDB: mfl.DepartmentsDb):
        self.db = depDB

    def __maintainingFunction(self, checkIntervalSecs: float):
        while self.shouldMaintain:
            self.db.ProcessTick()
            time.sleep(checkIntervalSecs)

    def StartMaintaining(self, checkIntervalSecs: float):
        self.__thread = threading.Thread(target=self.__maintainingFunction, args=(checkIntervalSecs,))
        self.__thread.start()

    def StopMaintaining(self):
        self.shouldMaintain = False
        self.__thread.join()

