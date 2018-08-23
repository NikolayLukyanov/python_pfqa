from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, baseUrl):
        if (browser == "firefox"):
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif (browser == "chrome"):
            self.wd = webdriver.Chrome()
        elif (browser == "ie"):
            self.wd = webdriver.Ie()
        else:
            raise ValueError("unrecognised browser %s" %browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl=baseUrl


    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.get(self.baseUrl)

    def open_group_page_by_id(self, id):
        wd = self.wd
        wd.get(self.baseUrl+'/?group=%s' %id)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):

        try:
            self.wd.current_url
            return True
        except:
            return False

