# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = app.contact.getcontactlist()
    contact = Contact(firstname="Edit", middlename="Editovich", lastname="Editov", nickname="EditedNick", title="edited title", company="edited company", address="edited address",
                               home_phone="edited home phone", mobile_phone="edited mobile phone", work_phone="edited work phone", fax="edited fax", main_email="edited main email", email_2="edited email 2",
                               email_3="edited email 3", homepage="edited homepage", birth_day="10", birth_month="5", birth_year="5000", ann_day="13", ann_month="12", ann_year="7000", group_number="3", address2="edited address 2",
                               phone2="edited phone 2", notes="edited notes")
    contact.id = oldcontacts[0].id
    app.contact.edit_first(contact)
    newcontacts = app.contact.getcontactlist()
        # check, that after editing contact count of contactss not changed
    assert len(oldcontacts) == len(newcontacts)
        # check, that list of contacts after editing contact is the same, as list of contacts before editing with first contact replaced
    oldcontacts[0] = contact
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)

def test_edit_first_contact_person(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    oldcontacts = app.contact.getcontactlist()
    contact = Contact(firstname="LEnin", middlename="Takoy", lastname="Molodoy", nickname="Yuniy Oktyabr Vperedi")
    contact.id = oldcontacts[0].id
    app.contact.edit_first(contact)
    newcontacts = app.contact.getcontactlist()
    # check, that after editing contact count of contactss not changed
    assert len(oldcontacts) == len(newcontacts)
    # check, that list of contacts after editing contact is the same, as list of contacts before editing with first contact replaced
    oldcontacts[0] = contact
    assert sorted(oldcontacts, key=Contact.id_or_max) == sorted(newcontacts, key=Contact.id_or_max)