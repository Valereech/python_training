from fixture.orm import ORMfixture
from model.group import Group


db = ORMfixture(host='localhost', name='addressbook', user='root', password='')

try:
    ls = db.get_users_in_group(Group(id='37'))
    for item in ls:
        print(item)
finally:
    pass  # db.destroy()
