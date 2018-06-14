class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.contact_text("firstname", contact.first_name)
        self.contact_text("lastname", contact.last_name)
        self.contact_text("address", contact.address)
        self.contact_text("home", contact.home_phone)
        self.contact_text("mobile", contact.mobile_phone)
        self.contact_text("work", contact.work_phone)
        self.contact_text("fax", contact.fax)
        self.contact_text("email", contact.first_email)
        self.contact_text("email2", contact.second_email)
        self.contact_text("email3", contact.third_email)

    def contact_text(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()


    def delete_first_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # delete submission
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))