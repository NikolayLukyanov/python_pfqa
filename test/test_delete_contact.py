# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_delete_random(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = app.contact.getcontactlist()
    index = randrange(len(oldcontacts))
    app.contact.delete_by_index(index)
       # check, that after deleting contact, count of contacts decreased by 1, comparing to state before deleting contact
    assert len(oldcontacts) - 1 == app.contact.count()
    newcontacts = app.contact.getcontactlist()
    oldcontacts.pop(index)
    assert oldcontacts == newcontacts

def test_delete_all_contacts(app):
    number_of_contacts = app.contact.count()
    if number_of_contacts == 0:
        app.contact.create(Contact(firstname="Nikto"))
    app.contact.delete_all()
    assert app.contact.count() == 0
