from random import randrange
from model.user import User


def test_mod_some_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="Someone"))
    contacts_list_before = app.user.get_contacts_list()
    user = (User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT", address="Tomsk",
                                    home="-", mobile="89231234567", work="-", fax="", email="alex224a@yandex.ru",
                                    homepage="", bday="13", bday2=13, bmonth="September", byear="1988", address2="",
                                    phone2="", notes=""))
    index = randrange(0, len(contacts_list_before))
    user.id = contacts_list_before[index].id
    app.user.modify_user_by_index(index, user)
    contacts_list_after = app.user.get_contacts_list()
    assert len(contacts_list_before) == len(contacts_list_after)
    contacts_list_before[index] = user
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)
