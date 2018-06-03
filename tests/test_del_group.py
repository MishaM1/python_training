from python_training.model.group import Group

def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Created group for deletion"))
    app.group.delete_first_group()
