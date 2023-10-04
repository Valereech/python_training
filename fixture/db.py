import pymysql.connections
from model.group import Group
from model.user import User


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          autocommit=True)

    def get_group_list(self):
        list_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list_groups.append(Group(id=str(id),
                                         name=name,
                                         header=header,
                                         footer=footer))
        finally:
            cursor.close()
        return list_groups

    def get_contacts_list(self):
        list_users = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, email from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, mobile, email) = row
                list_users.append(User(id=str(id),
                                       firstname=firstname,
                                       lastname=lastname,
                                       address=address,
                                       mobile=mobile,
                                       email=email))
        finally:
            cursor.close()
        return list_users

    def destroy(self):
        self.connection.close()
