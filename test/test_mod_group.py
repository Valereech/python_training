from random import randrange
from model.group import Group


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    groups_list_before = app.group.get_group_list()
    index = randrange(0, len(groups_list_before))
    group = Group(name="Commerce", header="All sales", footer="All sales")
    group.id = groups_list_before[index].id
    app.group.modify_group_by_index(index, group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)
    groups_list_before[index] = group
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
