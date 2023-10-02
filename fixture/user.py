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
        # wd = self.app.wd
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
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)
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
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        # Select user to delete
        wd.find_elements_by_name("selected[]")[index].click()
        # Submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contacts_cache = None

    def modify_first_user(self, user):
        self.modify_user_by_index(0, user)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        elements = wd.find_elements_by_xpath("//img[@alt='Edit']")
        element = elements[index]
        element.click()

    def modify_user_by_index(self, index, user):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        # update user information
        self.fill_form(user)
        # click Update
        wd.find_element_by_name("update").click()
        # return to home page
        self.return_to_home_page()
        self.contacts_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        # if not (wd.current_url.endswith("/addressbook/")\
        # and len(wd.find_elements_by_name("selected[]")) > 0):
        wd.find_element_by_link_text("home").click()

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_css_selector("td:nth-of-type(2)").text
                firstname = element.find_element_by_css_selector("td:nth-of-type(3)").text
                el_id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_css_selector("td:nth-of-type(4)").text
                emails = element.find_element_by_css_selector("td:nth-of-type(5)").text
                phones = element.find_element_by_css_selector("td:nth-of-type(6)").text
                self.contacts_cache.append(User(id=el_id, firstname=firstname, lastname=lastname,
                                                address=address, all_emails_from_home_page=emails,
                                                all_phones_from_home_page=phones))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return User(firstname=firstname, lastname=lastname, id=id, address=address,
                    home=home, mobile=mobile, work=work, phone2=phone2,
                    email=email, email2=email2, email3=email3)
