from random import randrange
import re
from model.user import User

def test_info_on_home_page(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT",
                                    address="Tomsk", home="101010", mobile="89231234567",
                                    work="131313", fax="", email="alex224a@yandex.ru",
                                    email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                                    homepage="", bday="13", bday2=13, bmonth="September",
                                    byear="1988", address2="-", phone2="121212", notes=""))
    contact_list = app.user.get_contacts_list()
    index = randrange(0, len(contact_list))
    contact_from_home_page = app.user.get_contacts_list()[index]
    contact_from_edit_page = app.user.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.home, user.mobile, user.work, user.phone2]))))

def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.email, user.email2, user.email3]))))
