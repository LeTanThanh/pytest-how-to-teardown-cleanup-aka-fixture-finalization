class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other_user):
        other_user.receive_email(email)

    def receive_email(self, email):
        self.index.append(email)


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body


class MailAdminClient:
    def __init__(self):
        self.users = []

    def create_user(self):
        user = MailUser()
        self.users.append(user)

        return user

    def delete_user(self, user):
        self.users.remove(user)
