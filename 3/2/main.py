#!/usr/bin/env python3


import collections
import sys


def read_file(filename, storage):
    """
    A function to read a file

    It opens a file with the given name and calculate
    occurances of the words in it
    """

    fh = None
    try:
        fh = open(filename, encoding="utf-8")

        for line in fh:
            words = line.split()

            for word in words:
                if word.isalpha():
                    storage[word.lower()] += 1
    except (IOError, OSError) as err:
        print("'{}' error: {}".format(filename, err))
    finally:
        if fh != None:
            fh.close()


def main():
    """
    A main function

    It reads all the file names given on the command line and
    call a helper function to calculate occurances of words in them
    """

    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("""program usage:
{} filename1 [filename2]...[filenameN]
""".format(sys.argv[0]))
        sys.exit()

    storage = collections.defaultdict(int)
    word_max_length = 10
    occurance_max_length = 5

    for filename in sys.argv[1:]:
        read_file(filename, storage)

    print("{:^{word_max_length}} {:^{occurance_max_length}}".format("word", "count", **locals()))
    print("{:-^{word_max_length}} {:-^{occurance_max_length}}".format("", "", **locals()))

    for k, v in sorted(storage.items(), key=lambda t: t[1], reverse=True):
        print("{:<{word_max_length}} {:>{occurance_max_length}}".format(
            k if len(k) < word_max_length else k[:word_max_length-3] + "...",
            v,
            **locals()))


main()
