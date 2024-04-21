import MailGenerator
from MainFlowLib import Worker
from logging import log, INFO, ERROR, DEBUG

class MailSandbox:
    def __init__(self):
        self.worker = Worker("Jan", "Kowalski", "FakeMail", [])
        self.worker.context = {
            'linkedin': {
                'name_surname': 'Jan Kowalski',
                'organization': 'Google',
                'description': 'Architect and ex-CTO focused on high performance and scalable web applications. Trainer, consultant and conference speaker. He has been working for several companies on PHP projects for millions of active users, from biggest social network and instant-messaging software in Poland to multi-billion PV content personalization and discovery platform. EventStorming evangelist. ',
                'posts': ['Zostały ostatnie miejsca na intensywny EventStorming w przyszłym tygodniu :) Jeśli chcesz zacząć stosować tę technikę z zespołem w projekcie, łączyć ją z podejściem Domain-Driven Design, zapraszam! Szczegóły poniżej.', 'Post2']
            }
        }


    def GenerateMail(self):

        log(INFO, "Mail generated")
        [title, content] = MailGenerator.GetMailParams(self.worker.context, self.worker.name, self.worker.surname)

        log(INFO, f"Title: {title}")
        log(INFO, f"Content: {content}")

        return title, content


if __name__ == '__main__':
    ms = MailSandbox()
    ms.GenerateMail()

