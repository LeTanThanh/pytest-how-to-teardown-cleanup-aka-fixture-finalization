from emaillib import MailAdmin
from emaillib import Email

from pytest import fixture


@fixture
def mail_admin():
    return MailAdmin()


@fixture
def sending_user(mail_admin, request):
    user = mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)

    return user


@fixture
def receiving_user(mail_admin, request):
    user = mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)

    return user


@fixture
def email(sending_user, receiving_user, request):
    sending_email = Email(subject="Hey!", body="How's it going")
    sending_user.send_email(sending_email, receiving_user)

    def clear_mailbox():
        receiving_user.clear_mailbox()

    request.addfinalizer(clear_mailbox)

    return sending_email

def test_email_received(receiving_user, email):
    assert email in receiving_user.inbox
