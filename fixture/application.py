"""module providing class Application for create and destroy fixture"""
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:
    """Class Application"""
    def __init__(self):
        """Constructor of webdriver implementation and Helpers"""
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        """open_home_page"""
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        """destroy"""
        self.wd.quit()
