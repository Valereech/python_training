from model.user import User
from random import randrange


def test_delete_some_user(app):
    contacts_list_before = app.user.get_contacts_list()
    if app.user.count() == 0:
        app.user.create(User(firstname="New user"))
    index = randrange(0, len(contacts_list_before))
    app.user.delete_user_by_index(index)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) - 1 == len(contacts_list_after)
    contacts_list_before[index:index + 1] = []
    assert contacts_list_before == contacts_list_after
