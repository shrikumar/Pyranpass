#!/usr/bin/env python
import string
import sys
from random import *
if len(sys.argv) >= 2:
    pass_strength = int(sys.argv[1])
else:
    pass_strength = 16
characters = string.ascii_letters + string.digits + '!#$%&*+-=?@^_'
password =  "".join(choice(characters) for x in range(pass_strength))
print(password)