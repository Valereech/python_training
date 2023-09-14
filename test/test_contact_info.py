from random import randrange
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
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3
    assert contact_from_home_page.home == contact_from_edit_page.home
    assert contact_from_home_page.mobile == contact_from_edit_page.mobile
    assert contact_from_home_page.work == contact_from_edit_page.work
    assert contact_from_home_page.phone2 == contact_from_edit_page.phone2
