# -*- coding: utf-8 -*-
from python_training.model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mishka", lastname="New", address="New York",
                      homephone="home222", workphone="work333",
                      mobilephone="mobile5564", secondaryphone="secondary11",
                      fax="none", first_email="testye@gmail.com",
                      second_email="sadasdas@gmail.com", third_email="sadasda@mail.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="",
#                                work_phone="", fax="", first_email="", second_email="", third_email="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
