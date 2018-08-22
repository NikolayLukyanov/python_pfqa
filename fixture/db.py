import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        #self.connection.autocommit = True

    def get_group_list(self):
        connect = self.connection.cursor()
        result = []
        with connect as cursor:  # connection.__enter__ executes at this line
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            self.connection.commit()
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                result.append(Group(id=str(id), group_name=name, group_header=header, group_footer=footer))

        return result

    def get_stripped_group_list(self):
        connect = self.connection.cursor()
        result = []
        with connect as cursor:  # connection.__enter__ executes at this line
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            self.connection.commit()
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                result.append(Group(id=str(id), group_name=name.strip(), group_header=header, group_footer=footer))

        return result

    def get_contact_list(self):
        connect = self.connection.cursor()
        result = []
        with connect as cursor:  # connection.__enter__ executes at this line
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            self.connection.commit()
            for row in cursor.fetchall():
                (id, firstname, lastname) = row
                result.append(Contact(id=str(id), firstname=firstname, lastname=lastname))

        return result

    def get_stripped_contact_list(self):
        connect = self.connection.cursor()
        result = []
        with connect as cursor:  # connection.__enter__ executes at this line
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            self.connection.commit()
            for row in cursor.fetchall():
                (id, firstname, lastname) = row
                result.append(Contact(id=str(id), firstname=firstname.strip(), lastname=lastname.strip()))

        return result

    def destroy(self):
        self.connection.close()