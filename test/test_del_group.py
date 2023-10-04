"""test_delete_first_group"""
import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    if db.get_group_list() == 0:
        app.group.create(Group(name="New group"))
    groups_list_before = db.get_group_list()
    group = random.choice(groups_list_before)
    app.group.delete_group_by_id(group.id)
    groups_list_after = db.get_group_list()
    assert len(groups_list_before) - 1 == len(groups_list_after)
    groups_list_before.remove(group)
    assert groups_list_before == groups_list_after
    if check_ui:
        assert sorted(groups_list_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
