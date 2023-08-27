"""test_delete_first_group"""
from model.group import Group

def test_delete_first_group(app):
    """test_delete_first_group"""
    groups_list_before = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.delete_first_group()
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) - 1 == len(groups_list_after)
    groups_list_before[0:1] = []
    assert groups_list_before == groups_list_after
