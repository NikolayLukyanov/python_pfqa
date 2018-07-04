# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.group_create(Group(group_name="", group_header="", group_footer=""))
    app.logout()

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group_create(Group(group_name="first_group", group_header="first cool logo", group_footer="first group created for python for QA cource"))
    app.logout()

