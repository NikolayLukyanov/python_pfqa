# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = app.contact.getcontactlist()
    app.contact.delete_first()
    newcontacts = app.contact.getcontactlist()
    # check, that after deleting contact, count of contacts decreased by 1, comparing to state before deleting contact
    assert len(oldcontacts) - 1 == len(newcontacts)
    oldcontacts.pop(0)
    assert oldcontacts == newcontacts

def test_delete_all_contacts(app):
    number_of_contacts = app.contact.count()
    if number_of_contacts == 0:
        app.contact.create(Contact(firstname="Nikto"))
        number_of_contacts = 1
    oldcontacts = app.contact.getcontactlist()
    app.contact.delete_all()
    newcontacts = app.contact.getcontactlist()
    assert len(oldcontacts) - len(newcontacts) == number_of_contacts