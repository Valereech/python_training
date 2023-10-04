import random
from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if db.get_group_list() == 0:
        app.group.create(Group(name="New group"))
    groups_list_before = db.get_group_list()
    data_to_edit = Group(name="Commerce", header="All sales", footer="All sales")
    group = random.choice(groups_list_before)
    app.group.modify_group_by_id(group.id, data_to_edit)
    assert len(groups_list_before) == len(db.get_group_list())
    groups_list_after = db.get_group_list()
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
    if check_ui:
        assert sorted(groups_list_before, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)
