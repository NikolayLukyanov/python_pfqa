from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    app.group.edit_first(Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="zaglushka"))
    app.group.edit_first(Group(group_name="o4en pustaya gruppa"))

