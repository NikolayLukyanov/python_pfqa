# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    #if no groups exist - test will fail. in this case creating group
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldcontacts = app.contact.getcontactlist()
    contact = Contact(firstname="First", middlename="Middle", lastname="Last", nickname="Nickname", title="Der", company="Alien", address="ulPushkina, dom Kolotushkina",
                               home_phone="123", mobile_phone="9059999999999", work_phone="dvornik", fax="5555555555", main_email="main@email.com", email_2="sw@mail.ru",
                               email_3="last@last.fm", homepage="google.com", birth_day="3", birth_month="2", birth_year="0000", ann_day="3", ann_month="2", ann_year="2000", group_number="2", address2="nowhere",
                               phone2="palatka", notes="just some notes")
    app.contact.create(contact)
        # check, that after adding contact, count of contacts increased by 1, comparing to state before adding contact
    assert len(oldcontacts) + 1 == app.contact.count()
        # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newcontacts = app.contact.getcontactlist()
    oldcontacts.append(contact)
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    oldcontacts = app.contact.getcontactlist()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home_phone="", mobile_phone="", work_phone="", fax="", main_email="", email_2="",
                               email_3="", homepage="", birth_day="1", birth_month="1", birth_year="", ann_day="1", ann_month="1", ann_year="", group_number="1", address2="",
                               phone2="", notes="")
    app.contact.create(contact)
        # check, that after adding contact, count of contacts increased by 1, comparing to state before adding contact
    assert len(oldcontacts) + 1 == app.contact.count()
        # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newcontacts = app.contact.getcontactlist()
    oldcontacts.append(contact)
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)

