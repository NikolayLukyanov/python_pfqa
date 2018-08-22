from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = db.get_group_list()
    group = random.choice(oldgroups)
    app.group.delete_by_id(group.id)
    newgroups = db.get_group_list()
        #check, that list of oldgroup without deleted element is equal to the list of group after deletion random group
    oldgroups.remove(group)
    assert oldgroups == newgroups
    if check_ui:
        assert sorted(db.get_stripped_group_list(), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)