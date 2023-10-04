# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    groups_list_before = db.get_group_list()
    app.group.create(group)
    groups_list_after = db.get_group_list()
    groups_list_before.append(group)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
