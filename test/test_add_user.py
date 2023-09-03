# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    contacts_list_before = app.user.get_contacts_list()
    user = User(firstname="asf", middlename="adf", lastname="adsf", nickname="adsf", title="asdf",
                         company="asdf", address="asdf", home="123", mobile="123", work="sdfbhngf", fax="-",
                         email="asdf@asdgva.asd", homepage="-", bday="12", bday2=12, bmonth="July", byear="1988",
                         address2="dbs srg", phone2="-", notes="cbm kgjbsdfb  asdfvdgsgns")
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)


def test_add_empty_user(app):
    contacts_list_before = app.user.get_contacts_list()
    user = (User(firstname="", middlename="", lastname="", nickname="", title="",
                         company="", address="", home="", mobile="", work="", fax="",
                         email="", homepage="", bday="-", bday2=0, bmonth="-", byear="",
                         address2="", phone2="", notes=""))
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)
