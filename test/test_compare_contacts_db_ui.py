from model.contact import Contact



def test_contacts_compare_home_page_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nikto"))
    contacts_from_db = sorted(db.get_stripped_mainpage_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_db) == len(contacts_from_home_page)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].all_emails_from_homepage == app.contact.merge_emails_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_homepage == app.contact.merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
