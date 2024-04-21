# Autor: Jakub Lisowski, Jlisowskyy
import time

import MailSendingLib as mLib
import MainFlowLib as fLib
import prepareBasicWorkerSet
import ConfigDeserialization as cd
import Application as App

# Function is used to perform main functionality tests
def LogicTest():
    # SendingTest()
    # GmailSendingTest()
    FlowTests()


#  TEST FILE FORMAT:
# smtp:port
# mail:passwd
# mail:passwd
# ...

# Function is used to parse mail smtp params from testFile
def OpenSender(line) -> mLib.MailSender | None:
    line = line.split(':')
    if not line or len(line) != 2:
        return None

    return mLib.MailSender(line[0], int(line[1]))


# Iterates through mails contained in test fails and performs mail send
# Functions opens ./mailList file and read from the first line smtp parameters then iterates through
# all mails contained in the file to perform mail sending test
def SendingTest():
    lineCnt = 0
    with open("mailList", 'r') as file:
        for line in file:
            lineCnt += 1
            line = line.strip()

            if lineCnt == 1:
                sender = OpenSender(line)
                continue

            if not line or line[0] == '#':
                continue

            line = line.split(':')

            if len(line) != 2:
                continue

            sender.SendMail(line[0], line[1], "Jlisowskyy@gmail.com", "test", "test")

def GmailSendingTest():
    sender = mLib.MailSender()
    sender.SendMailWithGmailApi("Jlisowskyy@gmail.com", "test", "test")


# Function performs tests of departments database
def FlowTests():
    app = App.Application("configs/departmentSetup.json", "configs/basicWorkerSet.json")
    app.Run()
    app.GetDepartments()
    time.sleep(100000)

if __name__ == '__main__':
    LogicTest()
