
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
        wd.find_element_by_link_text("add new").click()

    def delete_first(self):
        self.app.open_home_page()
        self.select_first()
        self.submit_contact_deletion()
        self.app.open_home_page()

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        #click on select all contacts
        wd.find_element_by_xpath("//div/div[4]/form[2]/input[2]").click()
        self.submit_contact_deletion()
        self.app.open_home_page()

    def submit_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    # method to edit first contact. group editing not included in this method
    def edit_first(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        #click on first contact edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_edit_contact_form(new_contact_data)
        # submitting form
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

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
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))