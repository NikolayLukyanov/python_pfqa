# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.application import Application

import pytest
import string
import random

def random_string(prefix, maxlength):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])

def get_groups_count(): #function, to get group count for generate random group number in Test data
    app = Application()
    app.session.ensure_login(username="admin", password="secret")
    group_count = app.group.count()
    app.session.close_browser()
    return group_count

length = get_groups_count()

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home_phone="", mobile_phone="", work_phone="", fax="", main_email="", email_2="",
                               email_3="", homepage="", birth_day="1", birth_month="1", birth_year="", ann_day="1", ann_month="1", ann_year="", group_number="1", address2="",
                               phone2="", notes="")] + \
                               [Contact(firstname=random_string("name", 10), middlename=random_string("middlenamename", 10),
                                lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                                title=random_string("title", 10), company=random_string("company", 10),
                                address=random_string("address", 10), home_phone=random_string("hphone", 10),
                                mobile_phone=random_string("mphone", 10), work_phone=random_string("wphone", 10),
                                fax=random_string("fax", 10), main_email=random_string("memail", 10),
                                email_2=random_string("2email", 10), email_3=random_string("3email", 10),
                                homepage=random_string("homepage", 10), birth_day=str(random.randint(1,31)),
                                birth_month=str(random.randint(1,12)), birth_year=str(str(random.randint(0,9999))),
                                ann_day=str(random.randint(1,31)), ann_month=str(random.randint(1,12)), ann_year=str(str(random.randint(0,9999))),
                                group_number=random.randrange(length), address2=random_string("address2", 10),
                               phone2=random_string("phone2", 10), notes=random_string("notes", 100)) for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    #if no groups exist - test will fail. in this case creating group
    group_count = app.group.count()
    if group_count == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldcontacts = app.contact.getcontactlist()
    app.contact.create(contact)
        # check, that after adding contact, count of contacts increased by 1, comparing to state before adding contact
    assert len(oldcontacts) + 1 == app.contact.count()
        # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newcontacts = app.contact.getcontactlist()
    oldcontacts.append(contact)
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)


