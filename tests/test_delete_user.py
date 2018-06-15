from python_training.model.contacts import Contact

def test_delete_first_user(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(first_name="Created contact for deletion"))
    app.contact.delete_first_user()
