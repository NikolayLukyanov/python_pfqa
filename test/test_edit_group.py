from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(group_name="edited_group", group_header="edited cool logo", group_footer="edited group for python for QA cource"))
    app.session.logout()
