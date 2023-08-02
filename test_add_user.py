# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.fill_user_form(wd, firstname="asf", middlename="adf", lastname="adsf", nickname="adsf", title="asdf",
                            company="asdf", address="asdf", home="123", mobile="123", work="sdfbhngf", fax="-",
                            email="asdf@asdgva.asd", homepage="-", bday="12", bday2=12, bmonth="July", byear="1988",
                            address2="dbs srg", phone2="-", notes="cbm kgjbsdfb  asdfvdgsgns")
        self.click_enter(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.fill_user_form(wd, firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="",
                            email="", homepage="", bday="-", bday2=0, bmonth="-", byear="",
                            address2="", phone2="", notes="")
        self.click_enter(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_user_form(self, wd, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work,
                       fax, email, homepage, bday, bday2, bmonth, byear, address2, phone2, notes):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        wd.find_element_by_xpath("//div[@id='content']/form/label[19]").click()
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        wd.find_element_by_xpath("//option[@value='" + str(bday2) + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        wd.find_element_by_xpath("//option[@value='" + str(bmonth) + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        wd.find_element_by_name("theform").click()
        # secondary information
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)

    def click_enter(self, wd):
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
