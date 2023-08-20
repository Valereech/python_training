from model.user import User


def test_mod_first_user(app):
    if app.user.count() == 0:
        app.user.create(User(firstname="Someone"))
    app.user.modify_first_user(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="", company="PT", address="Tomsk",
                                    home="-", mobile="89231234567", work="-", fax="", email="alex224a@yandex.ru",
                                    homepage="", bday="13", bday2=13, bmonth="September", byear="1988", address2="",
                                    phone2="", notes=""))
