# -*- coding: utf-8 -*-
from python_training.model.contacts import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Misha", last_name="New", address="New York",
                               home_phone="555555555555", mobile_phone="555555555555564", work_phone="45646465465465456", fax="none",
                               first_email="testye@gmail.com", second_email="sadasdas@gmail.com", third_email="sadasda@mail.ru"))
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", first_email="", second_email="", third_email=""))
    app.session.logout()