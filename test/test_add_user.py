# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string


def random_string(prefix, maxlen):
    if prefix == "bmonth":
        month = ("January", "February", "March", "April", "May", "June", "July", "August",
                 "September", "October", "November", "December")
        return "".join(str(random.choice(month)))
    elif prefix == "bday":
        day = list(range(1, 31))
        return "".join(str(random.choice(day)))
    elif prefix == "byear":
        year = list(range(1, 2023))
        return "".join(str(random.choice(year)))
    else:
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(firstname="", middlename="", lastname="", nickname="", title="",
                 company="", address="", home="", mobile="", work="", fax="",
                 email="", email2="", email3="", homepage="", bday="-",
                 bmonth="-", byear="", address2="", phone2="", notes="")] + [
               User(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                    title=random_string("title", 20), company=random_string("company", 20),
                    address=random_string("address", 20), home=random_string("home", 11),
                    mobile=random_string("mobile", 11), work=random_string("work", 11),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                    bday=random_string("bday", 2), bmonth=random_string("bmonth", 2), byear=random_string("byear", 4),
                    address2=random_string("address2", 30), phone2=random_string("phone2", 11),
                    notes=random_string("notes", 40))
               for i in range(5)
           ]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    contacts_list_before = app.user.get_contacts_list()
    app.user.create(user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
    contacts_list_before.append(user)
    assert sorted(contacts_list_before, key=User.id_or_max) \
           == sorted(contacts_list_after, key=User.id_or_max)
