# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_second_test(app):
    app.login(username="admin", password="secret")
    app.new_group()
    app.filling_group_form(Group(name="test group2", header="test", footer="test_r"))
    app.submit_group()
    app.group_page_open()
    app.logout(wd)

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.new_group()
    app.filling_group_form( Group(name="", header="", footer=""))
    app.submit_group()
    app.group_page_open()
    app.logout(wd)
