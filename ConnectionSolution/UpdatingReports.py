import MainFlowLib as MFL
import attempt2 as EmailScanner


class UpdateDatabase:
    email_scanner: EmailScanner.MessageScraper
    def __init__(self, db: MFL.DepartmentsDb, username: str, password: str):
        self.db = db
        self.username = username
        self.password = password
        self.email_scanner = EmailScanner.MessageScraper(username, password)

    def UpdateDatabaseReports(self):
        newEmails = self.email_scanner.get_new_messages()
        for key, value in self.db.__ongoingTests.items():
            link = "127.0.0.1/" + key
            for email in newEmails:
                if link in email.text:
                    value.isReported = True





