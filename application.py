from selenium.webdriver.firefox.webdriver import WebDriver


class Application():

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def group_page_open(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def submit_group(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def filling_group_form(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def new_group(self):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        wd.find_element_by_css_selector("html").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


