# -*- coding: utf-8 -*-
4
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_new_contact_page()
    app.add_new_contact(Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname", title="Der", company="Alien", address="ulPushkina, dom Kolotushkina",
                             home_phone="123", mobile_phone="9059999999999", work_phone="dvornik", fax="5555555555", main_email="main@email.com", email_2="sw@mail.ru",
                             email_3="last@last.fm", homepage="google.com", birth_day="3", birth_month="2", birth_year="0000", ann_day="3", ann_month="2", ann_year="2000", group_number="2", address2="nowhere",
                             phone2="palatka", notes="just some notes"))
    app.logout()

def test_test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_new_contact_page()
    app.add_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                             home_phone="", mobile_phone="", work_phone="", fax="", main_email="", email_2="",
                             email_3="", homepage="", birth_day="1", birth_month="1", birth_year="", ann_day="1", ann_month="1", ann_year="", group_number="1", address2="",
                             phone2="", notes=""))
    app.logout()
