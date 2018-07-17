from model.group import Group
from random import randrange

def test_edit_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    index = randrange(len(oldgroups))
    group = Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource")
    group.id = oldgroups[index].id
    app.group.edit_group_by_index(group, index)
    # check, that after editing group count of groups not changed
    assert len(oldgroups) == app.group.count()
    # check, that list of groups after editing group is the same, as list of groups before editing with first group replaced
    newgroups = app.group.getgrouplist()
    oldgroups[index] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)




