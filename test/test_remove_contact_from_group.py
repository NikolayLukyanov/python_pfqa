from model.contact import Contact
from random import choice
from model.group import Group

def test_remove_random_contact_from_random_group(app, dbOrm):

    if len(dbOrm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nikto"))   #if contact not exist - create new contact
    if len(dbOrm.get_group_list()) == 0:
        app.group.create(Group(group_name="zaglushka"))    #if group not exist - create new group
    group = choice(dbOrm.get_group_list())
    if len(dbOrm.get_contacts_in_group(group)) == 0:    #if no contacts assigned to group - assigning random contact to group
        contact = choice(dbOrm.get_contact_list())
        app.contact.assign_group_by_id_to_contact(contact, group.id)
    else:
        contact = choice(dbOrm.get_contacts_in_group(group))    #selecting random contact in group to be removed


    old_contacts_in_group = dbOrm.get_contacts_in_group(group)
    app.group.remove_contact_by_id_from_group(group, contact.id)
    new_contacts_in_group = dbOrm.get_contacts_in_group(group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group,
                                                                              key=Contact.id_or_max)
