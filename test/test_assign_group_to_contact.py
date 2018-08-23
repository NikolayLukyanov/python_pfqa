from model.contact import Contact
from random import choice
from model.group import Group

def test_assign_random_group_to_random_contact(app, dbOrm, check_ui):

    if len(dbOrm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nikto"))   #if contact not exist - create new contact
    if len(dbOrm.get_group_list()) == 0:
        app.group.create(Group(group_name="zaglushka"))    #if group not exist - create new group
    contact = choice(dbOrm.get_contact_list())
    group = choice(dbOrm.get_group_list())
    old_contacts_in_group = dbOrm.get_contacts_in_group(group)
    app.contact.assign_group_by_id_to_contact(contact, group.id)
    new_contacts_in_group = dbOrm.get_contacts_in_group(group)
    if contact in old_contacts_in_group:
        assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    else:
        old_contacts_in_group.append(contact)
        assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group,
                                                                              key=Contact.id_or_max)
