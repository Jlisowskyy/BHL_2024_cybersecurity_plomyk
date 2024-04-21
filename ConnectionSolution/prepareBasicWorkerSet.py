import time

import MainFlowLib as fLib

def getTestSet() -> [fLib.Worker]:
    rv = list()

    rv.append(fLib.Worker("Jason", "Darulo", "Jlisowskyysnk@gmail.com",
                          [fLib.LinkedinData("https://www.linkedin.com/in/john-smith-78b294305/")],
                          lastTest=time.time()))
    rv.append(fLib.Worker("Cristiano", "Ronaldo", "Jlisowskyysnk@gmail.com",
                          [fLib.LinkedinData("https://www.linkedin.com/in/john-smith-78b294305/")],
                          lastTest=time.time()))
    rv.append(fLib.Worker("Ronaldinho", "Gaucho", "Jlisowskyysnk@gmail.com",
                          [fLib.LinkedinData("https://www.linkedin.com/in/john-smith-78b294305/")],
                          lastTest=time.time()))

    return rv