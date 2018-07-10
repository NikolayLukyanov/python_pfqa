# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    app.contact.delete_first()

def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    app.contact.delete_all()