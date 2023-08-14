from model.user import User


def test_delete_first_user(app):
    app.session.login(username="admin", password="secret")
    app.user.modify_first_user(User(firstname="asf", middlename="adf", lastname="adsf", nickname="adsf", title="asdf",
                         company="asdf", address="asdf", home="123", mobile="123", work="sdfbhngf", fax="-",
                         email="asdf@asdgva.asd", homepage="-", bday="12", bday2=12, bmonth="July", byear="1988",
                         address2="dbs srg", phone2="-", notes="cbm kgjbsdfb  asdfvdgsgns"))
    app.session.logout()