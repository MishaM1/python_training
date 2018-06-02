# -*- coding: utf-8 -*-
import pytest
from python_training.model.group import Group
from python_training.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test group2", header="test", footer="test_r"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group( Group(name="", header="", footer=""))
    app.logout()