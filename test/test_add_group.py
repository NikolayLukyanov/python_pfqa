# -*- coding: utf-8 -*-

from model.group import Group


def test_add_empty_group(app):
    oldgroups = app.group.getgrouplist()
    group = Group(group_name="", group_header="", group_footer="")
    app.group.create(group)
        #check, that after adding group count of groups increased by 1, comparing to state before adding group
    assert  len(oldgroups) + 1 == app.group.count()
        #check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newgroups = app.group.getgrouplist()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)

def test_add_group(app):
    oldgroups = app.group.getgrouplist()
    group = Group(group_name="first_group", group_header="first cool logo", group_footer="first group created for python for QA cource")
    app.group.create(group)
    # check, that after adding group count of groups increased by 1, comparing to state before adding group
    assert len(oldgroups) + 1 == app.group.count()
    # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newgroups = app.group.getgrouplist()
    oldgroups.append(group)
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)