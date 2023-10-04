import random
from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if db.get_group_list() == 0:
        app.group.create(Group(name="New group"))
    groups_list_before = db.get_group_list()
    # index = randrange(0, len(groups_list_before))
    data_to_edit = Group(name="Commerce", header="All sales", footer="All sales")
    group = random.choice(groups_list_before)
    # group.id = groups_list_before[id].id
    app.group.modify_group_by_id(group.id, data_to_edit)
    groups_list_after = db.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)
    # groups_list_before[id] = group
    if check_ui:
        assert sorted(groups_list_before, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)
