import MainFlowLib as fLib

def getTestSet() -> [fLib.Worker]:
    rv = list()

    rv.append(fLib.Worker("jason", "darulo", "Jlisowskyysnk@gmail.com", [fLib.LinkedinData("https://www.linkedin.com/in/john-smith-78b294305/")]))

    return rv