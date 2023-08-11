# -*- coding: utf-8 -*-
import pytest

from application import Application
from user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinilaizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_new_page()
    app.fill_user_form(User(firstname="asf", middlename="adf", lastname="adsf", nickname="adsf", title="asdf",
                            company="asdf", address="asdf", home="123", mobile="123", work="sdfbhngf", fax="-",
                            email="asdf@asdgva.asd", homepage="-", bday="12", bday2=12, bmonth="July", byear="1988",
                            address2="dbs srg", phone2="-", notes="cbm kgjbsdfb  asdfvdgsgns"))
    app.click_enter()
    app.return_to_home_page()
    app.logout()


def test_add_empty_user(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_new_page()
    app.fill_user_form(User(firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="",
                            email="", homepage="", bday="-", bday2=0, bmonth="-", byear="",
                            address2="", phone2="", notes=""))
    app.click_enter()
    app.return_to_home_page()
    app.logout()
