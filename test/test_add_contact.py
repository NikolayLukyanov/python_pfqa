# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    oldcontacts = db.get_contact_list()
    app.contact.create(contact)
        # check, that after adding contact, count of contacts increased by 1, comparing to state before adding contact
    assert len(oldcontacts) + 1 == len(db.get_contact_list())
        # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newcontacts = db.get_contact_list()
    oldcontacts.append(contact)
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(db.get_stripped_contact_list(), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


