import random
from model.user import User
from model.group import Group
from fixture.orm import ORMfixture


def test_delete_user_from_group(app):
    orm_db = ORMfixture(host='localhost', name='addressbook', user='root', password='')
    if orm_db.get_contact_list() == 0:
        app.user.create(User(firstname="New user"))
    if orm_db.get_group_list() == 0:
        app.group.create(Group(name="New group"))
    groups_list = orm_db.get_group_list()
    group = random.choice(groups_list)
    users_in_group_from_db = orm_db.get_users_in_group(group)
    if len(users_in_group_from_db) == 0:
        users_not_in_group_from_db = orm_db.get_users_not_in_group(group)
        user = random.choice(users_not_in_group_from_db)
        app.user.add_user_to_group(user.id, group.id)
        users_in_group_from_db = orm_db.get_users_in_group(group)
    user = random.choice(users_in_group_from_db)
    app.user.delete_user_from_group(user.id, group.id)
    assert user not in orm_db.get_users_in_group(group)
    assert user in orm_db.get_users_not_in_group(group)
