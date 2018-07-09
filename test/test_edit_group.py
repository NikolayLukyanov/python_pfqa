from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource"))

def test_edit_first_group_name(app):
    app.group.edit_first(Group(group_name="edited_group"))

