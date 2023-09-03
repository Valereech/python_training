"""test_delete_first_group"""
from model.group import Group
from random import randrange


def test_delete_some_group(app):
    """test_delete_first_group"""
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    groups_list_before = app.group.get_group_list()
    index = randrange(0, len(groups_list_before))
    app.group.delete_group_by_index(index)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) - 1 == len(groups_list_after)
    groups_list_before[index:index + 1] = []
    assert groups_list_before == groups_list_after
