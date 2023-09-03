from selenium.webdriver.support.ui import Select
from model.user import User


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_element_by_name("selected[]")) > 0):
            wd.find_element_by_link_text("add new").click()

    def click_enter(self):
        wd = self.app.wd
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create(self, user):
        self.open_add_new_page()
        self.fill_form(user)
        self.click_enter()
        self.return_to_home_page()
        self.contacts_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, user):
        #wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("fax", user.fax)
        self.change_field_value("email", user.email)
        self.change_field_value("homepage", user.homepage)
        self.burtsday_fields("bday", user.bday)
        self.burtsday_fields("bmonth", user.bmonth)
        self.change_field_value("byear", user.byear)
        # secondary information
        self.change_field_value("address2", user.address2)
        self.change_field_value("phone2", user.phone2)
        self.change_field_value("notes", user.notes)

    def burtsday_fields(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
        wd.find_element_by_xpath("//option[@value='"+text+"']").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_user(self):
        wd = self.app.wd
        # Select user to delete
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contacts_cache = None

    def modify_first_user(self, user):
        wd = self.app.wd
        # click edit first user
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update user information
        self.fill_form(user)
        # click Update
        wd.find_element_by_name("update").click()
        # return to home page
        self.return_to_home_page()
        self.contacts_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        #if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("selected[]")) > 0):
        wd.find_element_by_link_text("home").click()

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                text1 = element.find_element_by_css_selector("td:nth-of-type(2)").text
                text2 = element.find_element_by_css_selector("td:nth-of-type(3)").text
                el_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(User(id=el_id, firstname=text2, lastname=text1))
        return list(self.contacts_cache)
