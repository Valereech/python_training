import random
from model.user import User


def test_mod_some_user(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.user.create(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT",
                                    address="Tomsk", home="-", mobile="89231234567",
                                    work="-", fax="", email="alex224a@yandex.ru",
                                    email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                                    homepage="", bday="13", bmonth="September",
                                    byear="1988", address2="-", phone2="-", notes=""))
    contacts_list_before = db.get_contacts_list()
    data_to_edit = (User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT",
                                    address="Tomsk", home="101010", mobile="89231234567",
                                    work="131313", fax="", email="alex224a@yandex.ru",
                                    email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                                    homepage="", bday="13", bmonth="September",
                                    byear="1988", address2="-", phone2="121212", notes=""))
    user = random.choice(contacts_list_before)
    contacts_list_before.remove(user)
    data_to_edit.id = user.id
    contacts_list_before.append(data_to_edit)
    app.user.modify_user_by_id(user.id, data_to_edit)
    contacts_list_after = db.get_contacts_list()
    assert len(contacts_list_before) == len(db.get_contacts_list())
    assert sorted(contacts_list_before, key=User.id_or_max) == sorted(contacts_list_after, key=User.id_or_max)
    if check_ui:
        assert sorted(contacts_list_before, key=User.id_or_max) == sorted(app.user.get_contacts_list(),
                                                                          key=User.id_or_max)
