class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, receive_user):
        receive_user.receive_email(email)

    def receive_email(self, email):
        self.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body


class MailAdmin:
    def __init__(self):
        self.users = []

    def create_user(self):
        user = MailUser()
        self.users.append(user)

        return user

    def delete_user(self, user):
        self.users.remove(user)
