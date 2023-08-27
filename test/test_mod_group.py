from model.group import Group


def test_modify_first_group(app):
    groups_list_before = app.group.get_group_list()
    group = Group(name="Commerce", header="All sales", footer="All sales")
    group.id = groups_list_before[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify_first_group(group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)
    groups_list_before[0] = group
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
