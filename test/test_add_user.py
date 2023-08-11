# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user import User


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.fill_user_form(User(firstname="asf", middlename="adf", lastname="adsf", nickname="adsf", title="asdf",
                            company="asdf", address="asdf", home="123", mobile="123", work="sdfbhngf", fax="-",
                            email="asdf@asdgva.asd", homepage="-", bday="12", bday2=12, bmonth="July", byear="1988",
                            address2="dbs srg", phone2="-", notes="cbm kgjbsdfb  asdfvdgsgns"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.user.fill_user_form(User(firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="",
                            email="", homepage="", bday="-", bday2=0, bmonth="-", byear="",
                            address2="", phone2="", notes=""))
    app.session.logout()
