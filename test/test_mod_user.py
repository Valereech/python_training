from model.user import User


def modify_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.modify_first_user(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                                    nickname="Valereech", title="-", company="PT", address="Tomsk",
                                    home="-", mobile="8923123456", email="asdf@asdgva.asd", bday="13",
                                    bday2=13, bmonth="September", byear="1988"))
    app.session.logout()