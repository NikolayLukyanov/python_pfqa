from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "/data/contacts.json"

safechars = string.ascii_letters + string.digits + "~ -_." + "/"

for o, a in opts:
    if o == "-n":
        try:
            n = int(a) -1
        except ValueError:
            print("-n not a number")
            sys.exit()
    elif o == "-f":
        f = a



def random_string(prefix, maxlength):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home_phone="", mobile_phone="", work_phone="", fax="", main_email="", email_2="",
                               email_3="", homepage="", birth_day="1", birth_month="1", birth_year="", ann_day="1", ann_month="1", ann_year="", address2="",
                               phone2="", notes="")] + \
                               [Contact(firstname=random_string("name", 5), middlename=random_string("middlenamename", 5),
                                lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
                                title=random_string("title", 5), company=random_string("company", 5),
                                address=random_string("address", 5), home_phone=random_string("hphone", 5),
                                mobile_phone=random_string("mphone", 5), work_phone=random_string("wphone", 5),
                                fax=random_string("fax", 5), main_email=random_string("memail", 5),
                                email_2=random_string("2email", 5), email_3=random_string("3email", 10),
                                homepage=random_string("homepage", 5), birth_day=str(random.randint(1,31)),
                                birth_month=str(random.randint(1,12)), birth_year=str(str(random.randint(0,9999))),
                                ann_day=str(random.randint(1,31)), ann_month=str(random.randint(1,12)),
                                ann_year=str(str(random.randint(0,9999))), address2=random_string("address2", 5),
                                phone2=random_string("phone2", 5), notes=random_string("notes", 5)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..%s" %f)
with open(file, "w") as fi:
    jsonpickle.set_encoder_options("json", indent=2)
    fi.write(jsonpickle.encode(testdata))
