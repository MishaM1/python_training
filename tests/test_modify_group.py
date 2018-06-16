from python_training.model.group import Group


def test_modify_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Created group for deletion"))
    old_groups = app.group.get_group_list()
    group = Group(name="New Group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#    if app.group.count_groups() == 0:
#        app.group.create(Group(name="Created group for deletion"))
#    old_groups = app.group.get_group_list()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
