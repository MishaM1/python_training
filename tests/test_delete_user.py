from python_training.model.contacts import Contact
from random import randrange


def test_delete_first_user(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for deletion"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_user_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert len(old_contacts) == len(new_contacts)
