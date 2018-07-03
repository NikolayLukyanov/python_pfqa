# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_contact_page(wd)
        self.add_new_contact(wd, Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname", title="Der", company="Alien", address="ulPushkina, dom Kolotushkina",
                             home_phone="123", mobile_phone="9059999999999", work_phone="dvornik", fax="5555555555", main_email="main@email.com", email_2="sw@mail.ru",
                             email_3="last@last.fm", homepage="google.com", birth_day="3", birth_month="2", birth_year="0000", ann_day="3", ann_month="2", ann_year="2000", group_number="2", address2="nowhere",
                             phone2="palatka", notes="just some notes"))
        self.logout(wd)

    def test_test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_contact_page(wd)
        self.add_new_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                             home_phone="", mobile_phone="", work_phone="", fax="", main_email="", email_2="",
                             email_3="", homepage="", birth_day="1", birth_month="1", birth_year="", ann_day="1", ann_month="1", ann_year="", group_number="1", address2="",
                             phone2="", notes=""))
        self.logout(wd)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.main_email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # entering birth day, birth month, birth year
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birth_day).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.birth_day).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birth_month).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.birth_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % contact.birth_year)
        # entering annual day, annual month, annual year
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.ann_day).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % contact.ann_day).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.ann_month).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % contact.ann_month).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % contact.ann_year)
        # entering group by it`s number in list, as first element in list is none - offset by 1
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[%s]" % contact.group_number).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[%s]" % contact.group_number).click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submitting form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
