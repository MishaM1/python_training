from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 all_phones_from_homepage=None, fax=None, first_email=None, second_email=None,
                 third_email=None):
        self.first_name = firstname
        self.last_name = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.fax = fax
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.id = id

    def __repr__(self):
        return "%s, %s" % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
