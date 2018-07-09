from python_training.model.group import Group
from python_training.model.contacts import Contact

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id.group.id, name=group.name.strip())
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                       address=contact.address, homephone=contact.homephone, mobilephone=contact.mobilephone,
                       workphone=contact.workphone, secondaryphone=contact.secondaryphone, first_email=contact.first_email, second_email=contact.second_email,
                       third_email=contact.third_email)
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
