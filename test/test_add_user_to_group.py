import random
from model.user import User
from model.group import Group
from fixture.orm import ORMfixture


def test_add_user_to_group(app):
    orm_db = ORMfixture(host='localhost', name='addressbook', user='root', password='')
    if len(orm_db.get_contact_list()) == 0:
        app.user.create(User(firstname="Alexey", middlename="Valeryevich", lastname="Trushin",
                             nickname="Valereech", title="", company="PT",
                             address="Tomsk", home="-", mobile="89231234567",
                             work="-", fax="", email="alex224a@yandex.ru",
                             email2="trushin88@gmail.com", email3="newmail_atrushin@mail.ru",
                             homepage="", bday="13", bmonth="September",
                             byear="1988", address2="-", phone2="-", notes=""))
    if len(orm_db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    groups_list = orm_db.get_group_list()
    group = random.choice(groups_list)
    users_not_in_group_from_db = orm_db.get_users_not_in_group(group)
    if len(users_not_in_group_from_db) == 0:
        app.user.create(User(firstname="New user"))
        users_not_in_group_from_db = orm_db.get_users_not_in_group(group)
    user = random.choice(users_not_in_group_from_db)
    app.user.add_user_to_group(user.id, group.id)
    assert user in orm_db.get_users_in_group(group)
    assert user not in orm_db.get_users_not_in_group(group)
