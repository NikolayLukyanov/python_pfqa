from model.group import Group
import sys


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group data
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()


    def delete_first(self, index):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        # select group by index , need to add check if index is more than number of groups
        self.select_group_by_index(index)
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        # select group by index , need to add check if index is more than number of groups
        self.select_group_by_id(id)
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_index(self, new_group_data, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit group deletion
        wd.find_element_by_name("edit").click()
        # fill group data
        self.fill_group_form(new_group_data)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_id(self, new_group_data, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        # submit group deletion
        wd.find_element_by_name("edit").click()
        # fill group data
        self.fill_group_form(new_group_data)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_first(self, new_group_data):
        self.edit_group_by_index(new_group_data, 0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        groupcount = len(self.get_group_list())
        if groupcount <= index:
            sys.exit("Index value is %d bigger than number of groups %d" % (index, groupcount))

        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if  self.group_cache == None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, id=id))
        return list(self.group_cache)

    def remove_contact_by_id_from_group(self, group, contact_id):
        wd = self.app.wd
        self.app.open_group_page_by_id(group.id)    #open group page with assigned contacts
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()    #select contact by id
        wd.find_element_by_name("remove").click()



