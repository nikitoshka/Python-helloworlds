#!/usr/bin/env python3
# pylint: disable=C0103

import math
import cmath
import sys


def getValue(variableName, mandatory):
    """ A function to prompt a user enter a variable's value """

    while True:
        sVal = input("input " + variableName + ": ")
        if len(sVal) == 0 and not mandatory:
            return 0

        try:
            val = float(sVal)
        except ValueError:
            continue

        return val


a = getValue("a", True)
b = getValue("b", False)
c = getValue("c", False)

discr = b**2 - 4*a*c
discrSqrt = None

if discr < 0:
    discrSqrt = cmath.sqrt(discr)
else:
    discrSqrt = math.sqrt(discr)

x1 = (-b + discrSqrt)/(2*a)
x2 = (-b - discrSqrt)/(2*a)

equationStr = ""

if a.is_integer:
    equationStr += str((int(a)))
else:
    equationStr += str(a)

equationStr += "x\N{SUPERSCRIPT TWO}"

if not abs(b - 0) <= sys.float_info.epsilon:
    if b.is_integer():
        equationStr += "{:+}".format(int(b))
    else:
        equationStr += "{:+}".format(b)
    equationStr += "x"

if not abs(c - 0) <= sys.float_info.epsilon:
    if c.is_integer():
        equationStr += "{:+}".format(int(c))
    else:
        equationStr += "{:+}".format(c)

equationStr += "=0"

roots = ""
if abs(x1 - x2) <= sys.float_info.epsilon:
    roots = "x = {}".format(x1)
else:
    roots = "x\N{SUBSCRIPT ONE} = {x1}, x\N{SUBSCRIPT TWO} = {x2}".format(**locals())

print("\n{} \U0001f87a {}".format(equationStr, roots))
