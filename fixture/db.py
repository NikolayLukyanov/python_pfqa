import pymysql.cursors
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

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

    def destroy(self):
        self.connection.close()