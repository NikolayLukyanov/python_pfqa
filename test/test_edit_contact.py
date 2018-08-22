# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = db.get_contact_list()
    index = randrange(len(oldcontacts))
    contact = Contact(firstname="Edit", middlename="Editovich", lastname="Editov", nickname="EditedNick", title="edited title", company="edited company", address="edited address",
                               home_phone="edited home phone", mobile_phone="edited mobile phone", work_phone="edited work phone", fax="edited fax", main_email="edited main email", email_2="edited email 2",
                               email_3="edited email 3", homepage="edited homepage", birth_day="10", birth_month="5", birth_year="5000", ann_day="13", ann_month="12", ann_year="7000", group_number="3", address2="edited address 2",
                               phone2="edited phone 2", notes="edited notes")
    contact.id = oldcontacts[index].id
    app.contact.edit_by_index(contact, index)
        # check, that after editing contact count of contactss not changed
    assert len(oldcontacts) == len(db.get_contact_list())
        # check, that list of contacts after editing contact is the same, as list of contacts before editing with first contact replaced
    newcontacts = db.get_contact_list()
    oldcontacts[index] = contact
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(db.get_stripped_contact_list(), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

