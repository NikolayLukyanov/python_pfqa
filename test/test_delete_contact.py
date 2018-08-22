# -*- coding: utf-8 -*-

from model.contact import Contact
import random


def test_delete_random(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = db.get_contact_list()
    contact = random.choice(oldcontacts)
    app.contact.delete_by_id(contact.id)
    newcontacts = db.get_contact_list()
    oldcontacts.remove(contact)
    assert oldcontacts == newcontacts
    if check_ui:
        assert sorted(db.get_stripped_contact_list(), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_delete_all_contacts(app, db, check_ui):
    number_of_contacts = len(db.get_contact_list())
    if number_of_contacts == 0:
        app.contact.create(Contact(firstname="Nikto"))
    app.contact.delete_all()
    assert len(db.get_contact_list()) == 0
    if check_ui:
        assert sorted(db.get_stripped_contact_list(), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
