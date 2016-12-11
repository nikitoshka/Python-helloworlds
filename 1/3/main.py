#!/usr/bin/env python3
# pylint: disable=C0103

""" An awful poem generator """

import random
import sys


DEFAULT_MIN = 1
DEFAULT_MAX = 10
DEFAULT_NUMBER = 5

ARTICLES = ["a", "an", "the", "another", "some"]
NOUNS = ["girl", "boy", "cat", "dog", "chair", "tree", "sky"]
VERBS = ["run", "stand", "speak", "watch", "eat", "dance", "grow"]
ADVERBS = ["quickly", "badly", "well", "rudely", "honestly", "sadly", "deeply"]

try:
    poemsCount = int(sys.argv[1])
except:
    print("wrong usage, composing the default number of poems:",
          DEFAULT_NUMBER)
    poemsCount = DEFAULT_NUMBER

if not DEFAULT_MIN <= poemsCount <= DEFAULT_MAX:
    print("wrong number of poems entered, using the default value:",
          DEFAULT_NUMBER)
    poemsCount = DEFAULT_NUMBER

print()

poemNumber = 0
while poemNumber < poemsCount:
    poem = random.choice(ARTICLES) + " "
    poem += random.choice(NOUNS) + " "
    poem += random.choice(VERBS)

    if random.randint(0, 1):
        poem += " " + random.choice(ADVERBS)

    poemNumber += 1

    print(poem)

print()
