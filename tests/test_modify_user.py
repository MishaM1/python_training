from python_training.model.contacts import Contact


def test_modify_contact_name(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_home_phone(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(home_phone="88888888888888888888"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_first_email(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_email="new_mail@gmail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)