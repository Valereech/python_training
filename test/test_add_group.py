# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name - ", 10), header=random_string("header - ",
                                                                  20), footer=random_string("footer - ", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    groups_list_before = app.group.get_group_list()
    app.group.create(group)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
