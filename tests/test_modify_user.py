from python_training.model.contacts import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Created contact for modify"))
    old_contacts = db.get_contact_list()
    contact_to_modify = random.choice(old_contacts)
    contact_info = Contact(firstname="New_name_modify")
    contact_info.id = contact_to_modify.id
    app.contact.modify_contact_by_id(contact_to_modify.id, contact_info)
    assert len(old_contacts) == app.contact.count_contacts()
    old_contacts.remove(contact_to_modify)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# def test_modify_contact_home_phone(app):
#    if app.contact.count_contacts() == 0:
#        app.contact.create(Contact(first_name="Created contact for modify"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(home_phone="88888888888888888888")
#    app.contact.modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


# def test_modify_contact_first_email(app):
#   if app.contact.count_contacts() == 0:
#        app.contact.create(Contact(first_name="Created contact for modify"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(first_email="new_mail@gmail.com")
#    app.contact.modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
