# Autor: Jakub Lisowski, Jlisowskyy

import MailSendingLib as mLib


# Function is used to perform main functionality tests
def LogicTest():
    SendingTest()


# Iterates through mails contained in test fails and performs mail send
def SendingTest():
    sender = mLib.MailSender()

    with open("mailList", 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line[0] == '#':
                continue

            line = line.split(':')

            if len(line) != 2:
                continue

            sender.SendMail(line[0], line[1], "Jlisowskyy@gmail.com", "test", "test")


if __name__ == '__main__':
    LogicTest()
