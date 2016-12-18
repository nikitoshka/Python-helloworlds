#!/usr/bin/env python3
# pylint: disable=C0103

import sys
import unicodedata


def printTable(words):
    """ A function for printing characters unicode names """

    print("{:^9} {:^6} {:^4} {:^30}".format("decimal", "hex", "char", "name"))
    print("{0:=^9} {0:=^6} {0:=^4} {0:=^30}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        ch = chr(code)
        charName = unicodedata.name(ch, "*** unknown ***")

        matches = 0
        if words is not None:
            for word in words:
                if word.lower() in charName.lower():
                    matches += 1

        if words is None or matches == len(words):
            try:
                print("{0:>9} {0:>6x} {0:>4c} {1:>30.30}".format(code, charName.title()))
            except:
                pass

        code += 1


words = sys.argv

if len(words) == 1:
    print("wrong usage")
    exit

printTable(words[1:])
