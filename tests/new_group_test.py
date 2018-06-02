# -*- coding: utf-8 -*-
from python_training.model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test group2", header="test", footer="test_r"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()