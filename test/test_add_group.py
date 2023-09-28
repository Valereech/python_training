# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    groups_list_before = app.group.get_group_list()
    app.group.create(group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
