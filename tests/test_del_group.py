from python_training.model.group import Group

def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Created group for deletion"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert len(old_groups) == len(new_groups)
