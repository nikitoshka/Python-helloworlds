#!/usr/bin/env python3

import collections
import sys


def parse_line(line):
    """
    A function for parseing a single line of a file

    The function walks through a file to get all the links it contains
    """

    prefixes = ("http://", "https://", "www.")
    links = set()

    for prefix in prefixes:
        i = 0
        while i < len(line):
            try:
                i = line.index(prefix, i)
                for pos in range(i + len(prefix), len(line)):
                    if not (line[pos].isalnum() or line[pos] in ".-"):
                        links.add(line[i:pos])
                        i = pos
                        break
            except ValueError:
                break

    return links


def read_file(filename, storage):
    """
    A function to read a single filename

    The function reads a given file and looks for any url in it
    """

    fh = None

    try:
        fh = open(filename, encoding="utf-8")

        for line in fh:
            for link in parse_line(line):
                storage[link].add(filename)

    except (IOError, OSError) as err:
        print("an error occured during reading '{}': {}".format(filename, err))
    finally:
        if fh is not None:
            fh.close()


def main():
    """
    The main fucntion

    Thise function opens all the given files and invoke a parsing functioin
    """

    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("""usage:
{} filename1 [filename2]...[filename3]""".format(sys.argv[0]))
        sys.exit()

    storage = collections.defaultdict(set)

    for filename in sys.argv[1:]:
        read_file(filename, storage)

    for url in sorted(storage):
        print(url, ":", sep="")
        for filename in sorted(storage[url]):
            print("\t", filename)


main()
