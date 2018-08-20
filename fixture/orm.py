from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:
    db = Database()
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        group_name = Optiona(str, column='group_name')
        group_header = Optiona(str, column='group_header')
        group_footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optiona(str, column='firstname')
        lastname = Optiona(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert():
            return Group(id=srt(group.id), group_name=group.group_name, group_header=group.group_header, group_footer=group.group_footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert():
            return Contact(id=srt(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))