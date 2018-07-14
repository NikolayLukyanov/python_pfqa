from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    app.group.delete_first()
    newgroups = app.group.getgrouplist()
    assert len(oldgroups) - 1 == len(newgroups)
        #check, that list of oldgroup without first element is equal to the list of group after deletion first group
    oldgroups.pop(0)
    assert oldgroups == newgroups