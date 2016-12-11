#!/usr/bin/env python3
# pylint: disable=C0103

""" It's like a real helloworld
but operating with numbers """


numbers = []

while True:
    inputStr = input("enter a number: ")
    if not len(inputStr):
        break

    try:
        number = numbers.append(int(inputStr))
    except ValueError:
        continue

print(numbers)

if len(numbers):
    print("len =", len(numbers), " sum =", sum(numbers), " lowest =",
          min(numbers), " highest =", max(numbers), " mean =",
          sum(numbers)/len(numbers))
