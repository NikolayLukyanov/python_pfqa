# -*- coding: utf-8 -*-

from model.group import Group


def test_add_empty_group(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))

def test_add_group(app):
    app.group.create(Group(group_name="first_group", group_header="first cool logo", group_footer="first group created for python for QA cource"))
