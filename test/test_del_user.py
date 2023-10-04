import random
from model.user import User


def test_delete_some_user(app, db, check_ui):
    if db.get_contacts_list() == 0:
        app.user.create(User(firstname="New user"))
    contacts_list_before = db.get_contacts_list()
    user = random.choice(contacts_list_before)
    app.user.delete_user_by_id(user.id)
    assert len(contacts_list_before) - 1 == len(db.get_contacts_list())
    contacts_list_after = db.get_contacts_list()
    contacts_list_before.remove(user)
    assert contacts_list_before == contacts_list_after
    if check_ui:
        assert sorted(contacts_list_before, key=User.id_or_max) == sorted(app.user.get_contacts_list(),
                                                                          key=User.id_or_max)
