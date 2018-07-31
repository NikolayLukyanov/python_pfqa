from model.contact import Contact
import sys
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_add_contact_form(contact)
        # submitting form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_add_contact_form(self, contact):
        self.change_field_value_by_name("firstname", contact.firstname)
        self.change_field_value_by_name("middlename", contact.middlename)
        self.change_field_value_by_name("lastname", contact.lastname)
        self.change_field_value_by_name("nickname", contact.nickname)
        self.change_field_value_by_name("title", contact.title)
        self.change_field_value_by_name("company", contact.company)
        self.change_field_value_by_name("address", contact.address)
        self.change_field_value_by_name("home", contact.home_phone)
        self.change_field_value_by_name("mobile", contact.mobile_phone)
        self.change_field_value_by_name("work", contact.work_phone)
        self.change_field_value_by_name("fax", contact.fax)
        self.change_field_value_by_name("email", contact.main_email)
        self.change_field_value_by_name("email2", contact.email_2)
        self.change_field_value_by_name("email3", contact.email_3)
        self.change_field_value_by_name("homepage", contact.homepage)
        # entering birth day, birth month, birth year
        self.change_field_value_by_xpath("//div[@id='content']/form/select[1]//option[%s]", contact.birth_day)
        self.change_field_value_by_xpath("//div[@id='content']/form/select[2]//option[%s]", contact.birth_month)
        self.change_field_value_by_name("byear", contact.birth_year)
        # entering annual day, annual month, annual year
        self.change_field_value_by_xpath("//div[@id='content']/form/select[3]//option[%s]", contact.ann_day)
        self.change_field_value_by_xpath("//div[@id='content']/form/select[4]//option[%s]", contact.ann_month)
        self.change_field_value_by_name("ayear", contact.ann_year)
        # entering group by it`s number in list, as first element in list is none - offset by 1
        self.change_field_value_by_xpath("//div[@id='content']/form/select[5]//option[%s]", contact.group_number)
        self.change_field_value_by_name("address2", contact.address2)
        self.change_field_value_by_name("phone2", contact.phone2)
        self.change_field_value_by_name("notes", contact.notes)


    def open_new_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//*[contains(text(), 'add address book entry')]")) > 0:
            return
        wd.find_element_by_link_text("add new").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.app.open_home_page()
        self.select_by_index(index)
        self.submit_contact_deletion()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        #click on select all contacts
        wd.find_element_by_xpath("//div/div[4]/form[2]/input[2]").click()
        self.submit_contact_deletion()
        self.app.open_home_page()
        self.contact_cache = None

    def submit_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    # method to edit first contact. group editing not included in this method
    def edit_first(self, new_contact_data):
        self.edit_by_index(new_contact_data, 0)

    def edit_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_edit_contact_form(new_contact_data)
        # submitting form
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # click on contact edit icon
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # click on contact edit icon
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def fill_edit_contact_form(self, contact):
        self.change_field_value_by_name("firstname", contact.firstname)
        self.change_field_value_by_name("middlename", contact.middlename)
        self.change_field_value_by_name("lastname", contact.lastname)
        self.change_field_value_by_name("nickname", contact.nickname)
        self.change_field_value_by_name("title", contact.title)
        self.change_field_value_by_name("company", contact.company)
        self.change_field_value_by_name("address", contact.address)
        self.change_field_value_by_name("home", contact.home_phone)
        self.change_field_value_by_name("mobile", contact.mobile_phone)
        self.change_field_value_by_name("work", contact.work_phone)
        self.change_field_value_by_name("fax", contact.fax)
        self.change_field_value_by_name("email", contact.main_email)
        self.change_field_value_by_name("email2", contact.email_2)
        self.change_field_value_by_name("email3", contact.email_3)
        self.change_field_value_by_name("homepage", contact.homepage)
        # entering birth day, birth month, birth year
        self.change_field_value_by_xpath("//div[@id='content']/form/select[1]//option[%s]", contact.birth_day)
        self.change_field_value_by_xpath("//div[@id='content']/form/select[2]//option[%s]", contact.birth_month)
        self.change_field_value_by_name("byear", contact.birth_year)
        # entering annual day, annual month, annual year
        self.change_field_value_by_xpath("//div[@id='content']/form/select[3]//option[%s]", contact.ann_day)
        self.change_field_value_by_xpath("//div[@id='content']/form/select[4]//option[%s]", contact.ann_month)
        self.change_field_value_by_name("ayear", contact.ann_year)
        self.change_field_value_by_name("address2", contact.address2)
        self.change_field_value_by_name("phone2", contact.phone2)
        self.change_field_value_by_name("notes", contact.notes)

    def change_field_value_by_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_by_xpath(self, xpath, text):
        wd = self.app.wd
        if text is not None:
            if not wd.find_element_by_xpath(
                    xpath % text).is_selected():
                wd.find_element_by_xpath(xpath % text).click()

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        contactcount = len(self.getcontactlist())
        if contactcount <= index:
            sys.exit("Index value is %d bigger than number of contacts %d" % (index, contactcount))
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def getcontactlist(self):
        if self.contact_cache == None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                person = element.find_elements_by_tag_name("td")
                firstname = person[2].text
                lastname = person[1].text
                allphones = person[5].text
                allemails = person[4].text
                address = person[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_homepage=allphones, all_emails_from_homepage=allemails, address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2, main_email=email, email_2=email2, email_3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.phone2]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                      [contact.main_email, contact.email_2, contact.email_3])))