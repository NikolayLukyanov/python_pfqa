from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    group = Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource")
    group.id = oldgroups[0].id
    app.group.edit_first(group)
    newgroups = app.group.getgrouplist()
    # check, that after editing group count of groups not changed
    assert len(oldgroups) == len(newgroups)
    # check, that list of groups after editing group is the same, as list of groups before editing with first group replaced
    oldgroups[0] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    oldgroups = app.group.getgrouplist()
    group = Group(group_name="only name")
    group.id = oldgroups[0].id
    app.group.edit_first(group)
    newgroups = app.group.getgrouplist()
    # check, that after editing group count of groups not changed
    assert len(oldgroups) == len(newgroups)
    # check, that list of groups after editing group is the same, as list of groups before editing with first group replaced
    oldgroups[0] = group
    assert sorted(oldgroups, key=Group.id_or_max) == sorted(newgroups, key=Group.id_or_max)

