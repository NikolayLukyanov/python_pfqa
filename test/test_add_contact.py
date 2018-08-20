# -*- coding: utf-8 -*-
from model.contact import Contact






def test_add_contact(app, json_contacts):
    contact = json_contacts
    oldcontacts = app.contact.getcontactlist()
    app.contact.create(contact)
        # check, that after adding contact, count of contacts increased by 1, comparing to state before adding contact
    assert len(oldcontacts) + 1 == app.contact.count()
        # check, that list of groups after adding group is the same, as list of groups before adding + new added group
    newcontacts = app.contact.getcontactlist()
    oldcontacts.append(contact)
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)


