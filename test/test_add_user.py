# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    contacts_list_before = app.user.get_contacts_list()
    user = User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT",
                                    address="Tomsk", home="101010", mobile="89231234567",
                                    work="131313", fax="", email="alex224a@yandex.ru",
                                    email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                                    homepage="", bday="13", bday2=13, bmonth="September",
                                    byear="1988", address2="-", phone2="121212", notes="")
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max)\
        == sorted(contacts_list_after, key=User.id_or_max)


def test_add_empty_user(app):
    contacts_list_before = app.user.get_contacts_list()
    user = (User(firstname="", middlename="", lastname="", nickname="", title="",
                        company="", address="", home="", mobile="", work="", fax="",
                        email="", email2="", email3="", homepage="", bday="-", bday2=0,
                        bmonth="-", byear="", address2="", phone2="", notes=""))
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max)\
        == sorted(contacts_list_after, key=User.id_or_max)
