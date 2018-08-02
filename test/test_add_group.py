# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import string
import random

def random_string(prefix, maxlength):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])

testdata = [Group(group_name="", group_header="", group_footer="")] + \
           [Group(group_name=random_string("name", 10), group_header=random_string("header", 19),
                  group_footer=random_string("footer", 30)) for i in range(5)]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata ])
def test_add_group(app, group):
    oldgroups = app.group.getgrouplist()
    app.group.create(group)
    # check, that after adding group count of groups increased by 1, comparing to state before adding group
    assert len(oldgroups) + 1 == app.group.count()
    # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newgroups = app.group.getgrouplist()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)