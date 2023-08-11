# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="dfgdfgdg", header="dfgdfgdg", footer="dfgdfgdfg"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_groups_page()
        self.logout()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
