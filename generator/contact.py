from python_training.model.contacts import Contact
import random
import string
import json
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
