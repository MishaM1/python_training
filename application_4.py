from selenium.webdriver.firefox.webdriver import WebDriver
from python_training.fixture.session import SessionHelper


class Application4:

    def __init__ (self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def secondary_data(self, address2, phone2, notes):
        wd = self.wd
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

    def anniversary_date(self, year, date_a, month_a):
        wd = self.wd
        if not wd.find_element_by_xpath("%s" % date_a).is_selected():
            wd.find_element_by_xpath(date_a).click()
        if not wd.find_element_by_xpath("%s" % month_a).is_selected():
            wd.find_element_by_xpath(month_a).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % year)

    def birth_date(self, date_b, month_b, year_b):
        wd = self.wd
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

    def email(self, email, email2, email3, homepage):
        wd = self.wd
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

    def telephones(self, telephones_1):
        wd = self.wd
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

    def name_and_address(self, name, middlename, surname, nickname, title, company, address, address_personal):
        wd = self.wd
        self.new_contact()
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

    def new_contact(self):
        wd = self.wd
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("add new").click()

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

