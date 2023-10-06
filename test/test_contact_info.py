import re
from model.user import User


def test_info_on_home_page(app, db):
    if len(db.get_contacts_list()) == 0:
        app.user.create(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                             nickname="Valereech", title="", company="PT",
                             address="Tomsk", home="-", mobile="89231234567",
                             work="-", fax="", email="alex224a@yandex.ru",
                             email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                             homepage="", bday="13", bmonth="September",
                             byear="1988", address2="-", phone2="-", notes=""))
    contact_list_from_db = sorted(db.get_contacts_list(), key=User.id_or_max)
    for contact in contact_list_from_db:
        contact_from_home_page = sorted(app.user.get_contacts_list(), key=User.id_or_max)
        for item in contact_from_home_page:
            if contact == item:
                assert item.id == contact.id
                assert item.firstname == contact.firstname
                assert item.lastname == contact.lastname
                assert item.address == contact.address
                assert item.all_emails_from_home_page == merge_emails_like_on_home_page(contact)
                assert item.all_phones_from_home_page == merge_phones_like_on_home_page(contact)


def clear(s):
    return re.sub("[() -']", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.home, user.mobile, user.work, user.phone2]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [user.email, user.email2, user.email3])))
