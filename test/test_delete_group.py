from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    app.group.delete_first()
    assert len(oldgroups) - 1 == app.group.count()
        #check, that list of oldgroup without first element is equal to the list of group after deletion first group
    newgroups = app.group.getgrouplist()
    oldgroups.pop(0)
    assert oldgroups == newgroups