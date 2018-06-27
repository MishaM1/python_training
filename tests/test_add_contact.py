# -*- coding: utf-8 -*-
from python_training.model.contacts import Contact
import pytest
import random
import string


def random_string_contacts(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join ([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="",
                      homephone="", workphone="",
                      mobilephone="", secondaryphone="",
                      fax="", first_email="",
                      second_email="", third_email="")
] + [
    Contact(firstname=random_string_contacts("firstname", 10), lastname=random_string_contacts("lasttname", 10),
            address=random_string_contacts("address", 10), homephone=random_string_contacts("homephone", 10),
            workphone=random_string_contacts("workphone", 10), mobilephone=random_string_contacts("mobilephone", 10),
            secondaryphone=random_string_contacts("secondaryphone", 10), fax=random_string_contacts("fax", 10),
            first_email=random_string_contacts("first_email", 10), second_email=random_string_contacts("second_email", 10),
            third_email=random_string_contacts("third_email", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
