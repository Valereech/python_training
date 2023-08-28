from model.user import User


def test_delete_first_user(app):
    contacts_list_before = app.user.get_contacts_list()
    if app.user.count() == 0:
        app.user.create(User(firstname="New user"))
    app.user.delete_first_user()
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) - 1 == len(contacts_list_after)
    contacts_list_before[0:1] = []
    assert contacts_list_before == contacts_list_after
