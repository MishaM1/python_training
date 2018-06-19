# -*- coding: utf-8 -*-
from python_training.model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Misha", last_name="New", address="New York",
                               home_phone="555555555555", mobile_phone="555555555555564", work_phone="45646465465465456", fax="none",
                               first_email="testye@gmail.com", second_email="sadasdas@gmail.com", third_email="sadasda@mail.ru")
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
