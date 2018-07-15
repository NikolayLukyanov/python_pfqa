# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = app.contact.getcontactlist()
    app.contact.delete_first()
       # check, that after deleting contact, count of contacts decreased by 1, comparing to state before deleting contact
    assert len(oldcontacts) - 1 == app.contact.count()
    newcontacts = app.contact.getcontactlist()
    oldcontacts.pop(0)
    assert oldcontacts == newcontacts

def test_delete_all_contacts(app):
    number_of_contacts = app.contact.count()
    if number_of_contacts == 0:
        app.contact.create(Contact(firstname="Nikto"))
    app.contact.delete_all()
    assert app.contact.count() == 0
