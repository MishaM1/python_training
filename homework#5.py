# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from telephone import Telephones_class


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class new_user(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def test_valid_user_creation(self):
        wd = self.wd
        self.user_login(wd, "admin", "secret")
        self.create_user()

    def create_user(self):
        wd = self.wd
        self.name_and_address(wd, "a1", "b2", "c3", "d4", "mr.", "Addressbook co.", "test", "test test 2")
        self.telephones(wd, Telephones_class("456", "4568", "45689", "456688"))
        self.email(wd, "test1@co", "test333@dd", "test444@asa", "asd32")
        self.birth_date(wd, "//div[@id='content']/form/select[1]//option[3]",
                        "//div[@id='content']/form/select[2]//option[2]", "1998")
        self.anniversary_date(wd, "2010", "//div[@id='content']/form/select[3]//option[5]",
                              "//div[@id='content']/form/select[4]//option[6]")
        self.secondary_data(wd, "12312", "13231231231", "312312312")

    def secondary_data(self, wd, address2, phone2, notes):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def anniversary_date(self, wd, year, date_a, month_a):
        if not wd.find_element_by_xpath("%s" % date_a).is_selected():
            wd.find_element_by_xpath(date_a).click()
        if not wd.find_element_by_xpath("%s" % month_a).is_selected():
            wd.find_element_by_xpath(month_a).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % year)

    def birth_date(self, wd, date_b, month_b, year_b):
        if not wd.find_element_by_xpath("%s" % date_b).is_selected():
            wd.find_element_by_xpath(date_b).click()
        if not wd.find_element_by_xpath(date_b).is_selected():
            wd.find_element_by_xpath(date_b).click()
        if not wd.find_element_by_xpath("%s" % month_b).is_selected():
            wd.find_element_by_xpath(month_b).click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % year_b)

    def email(self, wd, email, email2, email3, homepage):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % homepage)

    def telephones(self, wd, telephones_1):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % telephones_1.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % telephones_1.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % telephones_1.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % telephones_1.fax)

    def name_and_address(self, wd, name, middlename, surname, nickname, title, company, address, address_personal):
        self.new_contact(wd)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % address)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % address_personal)

    def new_contact(self, wd):
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("add new").click()

    def user_login(self, wd, name, password):
        self.open_homepage(wd)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % name)
        wd.find_element_by_css_selector("html").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
