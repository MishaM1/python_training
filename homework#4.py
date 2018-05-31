import pytest
from telephone import Telephones_class
from application_4 import Application4


@pytest.fixture
def app(request):
    fixture = Application4()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_valid_user_creation(app):
    app.user_login("admin", "secret")
    app.name_and_address("a1", "b2", "c3", "d4", "mr.", "Addressbook co.", "test", "test test 2")
    app.telephones(Telephones_class("456", "4568", "45689", "456688"))
    app.email("test1@co", "test333@dd", "test444@asa", "asd32")
    app.birth_date("//div[@id='content']/form/select[1]//option[3]",
                        "//div[@id='content']/form/select[2]//option[2]", "1998")
    app.anniversary_date("2010", "//div[@id='content']/form/select[3]//option[5]",
                              "//div[@id='content']/form/select[4]//option[6]")
    app.secondary_data("12312", "13231231231", "312312312")
    app.logout()
