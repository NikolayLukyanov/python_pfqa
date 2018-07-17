from model.group import Group
from random import randrange

def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    index = randrange(len(oldgroups))
    app.group.delete_by_index(index)
    assert len(oldgroups) - 1 == app.group.count()
        #check, that list of oldgroup without deleted element is equal to the list of group after deletion random group
    newgroups = app.group.getgrouplist()
    oldgroups.pop(index)
    assert oldgroups == newgroups