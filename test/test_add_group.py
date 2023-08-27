# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    groups_list_before = app.group.get_group_list()
    group = Group(name="dfgdfgdg", header="dfgdfgdg", footer="dfgdfgdfg")
    app.group.create(group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)


def test_add_empty_group(app):
    groups_list_before = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
