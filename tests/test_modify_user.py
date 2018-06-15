from python_training.model.contacts import Contact


def test_modify_contact_name(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    app.contact.modify_first_contact(Contact(first_name="New name"))


def test_modify_contact_home_phone(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    app.contact.modify_first_contact(Contact(home_phone="88888888888888888888"))


def test_modify_contact_first_email(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for modify"))
    app.contact.modify_first_contact(Contact(first_email="new_mail@gmail.com"))