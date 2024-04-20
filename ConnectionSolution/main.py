# Autor: Jakub Lisowski, Jlisowskyy

import MailSendingLib as mLib


# Function is used to perform main functionality tests
def LogicTest():
    mLib.SendPreparedEmail("Jlisowskyy@gmail.com", "elo elo", "basic template [link_token]")


if __name__ == '__main__':
    LogicTest()