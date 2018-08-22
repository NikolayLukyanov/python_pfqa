from model.group import Group
from random import randrange

def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = db.get_group_list()
    index = randrange(len(oldgroups))
    group = Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource")
    group.id = oldgroups[index].id
    app.group.edit_group_by_index(group, index)
    # check, that after editing group count of groups not changed
    assert len(oldgroups) == len(db.get_group_list())
    # check, that list of groups after editing group is the same, as list of groups before editing with first group replaced
    newgroups = db.get_group_list()
    oldgroups[index] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_stripped_group_list(), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




