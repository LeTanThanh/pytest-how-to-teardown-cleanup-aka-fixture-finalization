from emaillib import MailAdmin
from emaillib import Email

from pytest import fixture


@fixture
def mail_admin():
    return MailAdmin()


@fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    user.clear_mailbox()
    mail_admin.delete_user(user)


def test_send_email(sending_user, receiving_user):
    email = Email(subject='Hey!', body="How's it going")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox
