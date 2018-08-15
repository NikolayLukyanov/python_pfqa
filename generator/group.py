from model.group import Group
import string
import random
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "/data/groups.json"

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


testdata = [Group(group_name="", group_header="", group_footer="")] + \
           [Group(group_name=random_string("name", 10), group_header=random_string("header", 19),
                  group_footer=random_string("footer", 30)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..%s" %f)
with open(file, "w") as fi:
    fi.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
