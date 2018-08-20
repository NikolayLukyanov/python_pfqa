from model.contact import Contact
from random import randrange


def test_random_contact_compare_home_page_edit_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikto"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.getcontactlist()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_homepage == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address