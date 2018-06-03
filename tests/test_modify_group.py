from python_training.model.group import Group


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Created group for deletion"))
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Created group for deletion"))
    app.group.modify_first_group(Group(header="New header"))

