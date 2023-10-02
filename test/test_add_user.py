# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app, json_users):
    user = json_users
    contacts_list_before = app.user.get_contacts_list()
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)
