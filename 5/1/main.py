#!/usr/bin/env python3
"""
A simple programm that acts like the ls command in Unix.
"""

import argparse
import os
import collections
import time

args = None
Entry_descr = collections.namedtuple('Entry_descr',
                                     'modified size name')


def main():
    """
    The main function of the programm.
    """

    parser = argparse.ArgumentParser(description='Get a list of files and directories')
    parser.add_argument('-H', '--hidden', dest='show_hidden', action='store_true',
                        help='show hidden files [default: off]')
    parser.add_argument('-m', '--modified', dest='modified', action='store_true',
                        help='show last modified date/time [default: off]')
    parser.add_argument('-o', '--order', dest='order', default=['name'], nargs=1,
                        type=str, choices=['name', 'n', 'modified', 'm', 'size', 's'],
                        help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
    parser.add_argument('-r', '--recursive', dest='recursive', action='store_true',
                        help='recurse into subdirectories [default: off]')
    parser.add_argument('-s', '--sizes', dest='sizes', action='store_true',
                        help='show sizes [default: off]')
    parser.add_argument(dest='paths', nargs='*', type=str, metavar='[path]',
                        help='path(s) to look into')

    global args
    args = parser.parse_args()

    func_to_walk = recursive_walk if args.recursive else linear_walk
    files_count, dirs_count = (0, 0)

    for dirname in args.paths:
        new_files_count, new_dirs_count = func_to_walk(dirname)
        files_count += new_files_count
        dirs_count += new_dirs_count
        print()

    print('{} file{}'.format(files_count,
                             's' if files_count == 0 or files_count > 1 else ''),
          end='')

    print(', {} {}'.format(dirs_count,
                           'directories' if dirs_count == 0 or dirs_count > 1 else 'directory'))


def recursive_walk(dirname):
    """
    A function that gets executed if a user wants to walk
    recursively through directories.
    Returns the total number of files and directories found.
    """

    files_count, dirs_count = (0, 0)

    for cur_dir, dirs, files in os.walk(dirname, onerror=print):
        content = get_dir_content(dirs, files)
        print_dir_content(cur_dir, content)

        if not args.show_hidden:
            dirs[:] = [single_dir for single_dir in dirs
                       if not single_dir.startswith(".")]

        print()

        new_files_count, new_dirs_count = get_entries_count(cur_dir, content)
        files_count += new_files_count
        dirs_count += new_dirs_count

    return (files_count, dirs_count)


def linear_walk(dirname):
    """
    A function that gets executed in a case of
    a simple linear walk through a directory.
    Returns the total number of files and directories found.
    """

    try:
        content = get_dir_content(os.listdir(dirname))
    except OSError as err:
        print(err)

    print_dir_content(dirname, content)
    return get_entries_count(dirname, content)


def print_dir_content(dirname, content):
    """
    A function for printing the content of a given directory.
    """

    described_content = []
    max_modified_width, max_size_width = (0, 0)

    for entry in content:
        modified, size = (0, 0)
        if args.modified or args.sizes:
            stat = os.stat(os.path.join(dirname, entry))
            if args.modified:
                modified = stat.st_mtime
                modified_str = time.ctime(modified)
                if len(modified_str) > max_modified_width:
                    max_modified_width = len(modified_str)
            if args.sizes:
                size = stat.st_size
                size_width = len('{:,}'.format(size))
                max_size_width = size_width if size_width > max_size_width else max_size_width

        described_content.append(Entry_descr(modified, size, entry))

    sort_key = None
    if args.order[0] in {'s', 'size'}:
        sort_key = lambda entry: entry.size
    elif args.order[0] in {'m', 'modified'}:
        sort_key = lambda entry: entry.modified
    else:
        sort_key = lambda entry: entry.name

    print('{}:'.format(dirname))

    for entry in sorted(described_content, key=sort_key):
        modified_patter = '{:<{}}'.format(time.ctime(entry.modified),
                                          max_modified_width)
        size_patter = '{:>{},}'.format(entry.size, max_size_width)
        print('{}{}{}{}{}'.format(modified_patter if args.modified else '',
                                  ' ' if args.modified else '',
                                  size_patter if args.sizes else '',
                                  ' ' if args.sizes else '',
                                  entry.name))


def get_dir_content(*lists_of_entries):
    """
    A function for accumulating the resulting list of
    a directory's content.
    """

    content = []

    for entries in lists_of_entries:
        content += entries if args.show_hidden else [entry for entry in entries
                                                     if not entry.startswith(".")]

    return content


def get_entries_count(dirname, content):
    """
    A function for calculating the number of files
    and directories in a given directory
    """

    files_count, dirs_count = (0, 0)

    for entry in content:
        if os.path.isfile(os.path.join(dirname, entry)):
            files_count += 1
        elif os.path.isdir(os.path.join(dirname, entry)):
            dirs_count += 1

    return (files_count, dirs_count)


main()
