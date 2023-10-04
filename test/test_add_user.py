# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app, db, check_ui, json_users):
    user = json_users
    contacts_list_before = db.get_contacts_list()
    app.user.create(user)
    contacts_list_after = db.get_contacts_list()
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)
    if check_ui:
        assert sorted(contacts_list_before, key=User.id_or_max) == sorted(app.user.get_contacts_list(),
                                                                          key=User.id_or_max)
