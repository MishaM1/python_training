from python_training.model.contacts import Contact
import random
import string

constant = [
    Contact(firstname="", lastname="11", address="11",
                      homephone="11", workphone="11",
                      mobilephone="11", secondaryphone="11",
                      fax="11", first_email="11",
                      second_email="11", third_email="11"),
    Contact(firstname="22", lastname="22", address="22",
                      homephone="22", workphone="22",
                      mobilephone="22", secondaryphone="22",
                      fax="22", first_email="22",
                      second_email="22", third_email="22")
]

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