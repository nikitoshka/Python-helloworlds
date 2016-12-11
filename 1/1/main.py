#!/usr/bin/env python3
# pylint: disable=C0103

"""
A simple program for funny digit printing
"""

ZERO = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

ONE = ["   *   ",
       "  **   ",
       " * *   ",
       "   *   ",
       "   *   ",
       "   *   ",
       "  ***  "]

TWO = ["   **  ",
       "  *  * ",
       "  *  * ",
       "     * ",
       "   *   ",
       "   *   ",
       "  **** "]

THREE = ["   **  ",
         "  *  * ",
         "     * ",
         "    *  ",
         "     * ",
         "  *  * ",
         "   **  "]

FOUR = ["   **  ",
        "  * *  ",
        " *  *  ",
        " ***** ",
        "    *  ",
        "    *  ",
        "   *** "]

FIVE = ["   *** ",
        "  *    ",
        "  *    ",
        "  ***  ",
        "     * ",
        "    *  ",
        " ***   "]

SIX = ["  ***  ",
       " *   * ",
       " *     ",
       " ****  ",
       " *   * ",
       " *   * ",
       "  ***  "]

SEVEN = ["  ***  ",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         "  *    ",
         "  *    "]

EIGHT = ["  ***  ",
         " *   * ",
         "  * *  ",
         "   *   ",
         "  * *  ",
         " *   * ",
         "  ***  "]

NINE = ["   *** ",
        "  *   *",
        "  *   *",
        "   * * ",
        "     * ",
        "    *  ",
        "   *   "]

DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
ASTERISK = "*"


def getDigitedLine(line, placehodler, digit):
    """ A function that returns a line with all the occurances of
    the placeholder replaced with the digit """

    newLine = ""
    for ch in line:
        if ch == placehodler:
            try:
                newLine += str(digit)
            except ValueError:
                continue
        else:
            newLine += ch

    return newLine


def printFormatedDigits(digitsToPrint):
    """ A function to print digits in a funny way """

    rowNumber = 0
    rowsExhausted = False

    while not rowsExhausted:
        row = ""

        for singleDigit in digitsToPrint:
            try:
                intDigit = int(singleDigit)
            except ValueError:
                continue
            try:
                strDigit = DIGITS[intDigit]
            except IndexError:
                continue

            if len(strDigit) <= rowNumber:
                rowsExhausted = True
            else:
                row += getDigitedLine(strDigit[rowNumber],
                                      ASTERISK,
                                      intDigit) + " "

        rowNumber += 1

        if len(row):
            print(row)


inputDigits = input("enter some digits for format print: ")
print()
printFormatedDigits(inputDigits)
print()
