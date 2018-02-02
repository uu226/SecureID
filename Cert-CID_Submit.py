#!/usr/bin/python 
#alex.wen@canonical.com

import sys
import requests

if len(sys.argv) != 2:
    print "Bye"
    sys.exit()

r = requests.get("https://goo.gl/J1UuJJ")
print r.text
