#!/usr/bin/env python3

import os
import sys


EXTENSION = ".lst"


def get_string(input_prompt, *, permissible=None, mandatory=False):
    """
    A function for getting a string from a user
    """

    while True:
        entered_string = input(input_prompt)

        if not entered_string and not mandatory:
            return entered_string

        if permissible is not None:
            if entered_string in permissible:
                return entered_string
            else:
                print("{} is not permitted, try again".format(entered_string))
                continue

        return entered_string


def get_int(input_prompt, min_value=0, max_value=100):
    """
    A functiion for getting an int value from a user
    """

    while True:
        try:
            value = int(input(input_prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print("the value is out of range")
        except ValueError:
            print("a wrong value")


def print_string_enumeration(strs):
    """
    A function for printing enumeration of strings
    """

    if not strs:
        return

    ind_width = len(str(len(strs)))
    for ind, single_string in enumerate(strs, start=1):
        print("{ind:>{ind_width}}: {single_string}".format(**locals()))


def handle_file_list(files):
    """
    A function for showing a menu when some files already exist
    """

    if not files:
        return

    print_string_enumeration(files)
    answer = get_string("[N]ew [L]oad [Q]uit: ", permissible=tuple("nNlLqQ"),
                        mandatory=True)

    if answer in set("nN"):
        handle_new_file(files)
    elif answer in set("lL"):
        handle_existing_file(files)
    elif answer in set("qQ"):
        sys.exit()


def get_file_name(existing_files=None):
    """
    A function for getting an available file name
    """

    while True:
        file_name = get_string("enter a file name: ", mandatory=True)

        if not file_name.isalnum():
            print("a wrong file name")
            continue

        if not file_name.endswith(EXTENSION):
            file_name += EXTENSION

        if existing_files and file_name in existing_files:
            print("the file already exists")
            continue

        return file_name


def handle_new_file(existing_files=None):
    """
    A function for starting a life of a new file
    """

    file_name = get_file_name(existing_files)
    print()
    edit_file(file_name, True)


def handle_existing_file(files):
    """
    A function for editting an existing file
    """

    input_prompt = "enter a file number to edit (0 to cancel): "
    file_number = get_int(input_prompt, 0, len(files))

    if file_number == 0:
        return

    print()
    edit_file(files[file_number - 1], False)


def add_file_entry(file_content):
    """
    A function for adding an entry to a file's content
    """

    entry = get_string("enter an entry: ")
    if entry:
        file_content.append(entry)


def del_file_entry(file_content):
    """
    A function for deleting an entry from a file's content
    """

    input_prompt = "enter a string number to delete (0 to cancel): "
    line_number = get_int(input_prompt, 0, len(file_content))

    if line_number == 0:
        return

    file_content.pop(line_number - 1)


def save_file(file_name, file_content):
    """
    A function for writing saving a file
    """

    file_handler = None
    try:
        file_handler = open(file_name, "w", encoding="utf-8")
        for line in file_content:
            file_handler.write(line + "\n")
        return True
    except (IOError, OSError) as err:
        print("failed to save '{}': {}", file_name, err)
        return False
    finally:
        if file_handler:
            file_handler.close()


def read_file_content(file_name):
    """
    A function for getting a file content as a list
    """

    file_content = []
    file_handler = None

    try:
        file_handler = open(file_name, "r", encoding="utf-8")
        for line in file_handler:
            file_content.append(line.strip())
    except (IOError, OSError) as err:
        print("failed to open '{}': {}".format(file_name, err))
    finally:
        file_handler.close()

    return file_content


def handle_quit_editing(file_name, file_content, dirty):
    """
    A function for quiting from file edit
    """

    if not dirty:
        return

    input_prompt = "[S]ave and quit [Q]uit without saving: "
    answer = get_string(input_prompt, permissible=tuple("sSqQ"),
                        mandatory=True)

    if answer in set("sS"):
        save_file(file_name, file_content)


def edit_file(file_name, new_file):
    """
    A function for editing a single file
    """

    dirty = False
    file_content = []

    if not new_file:
        file_content = read_file_content(file_name)
        file_content[:] = sorted(file_content)

    while True:
        print_string_enumeration(file_content)

        choices = list("aA")
        input_prompt = "[A]dd"

        if file_content:
            input_prompt += " [D]elete"
            choices += "dD"
        if dirty:
            input_prompt += " [S]ave"
            choices += "sS"
        input_prompt += " [Q]uit"
        choices += "qQ"

        answer = get_string(input_prompt + ": ", permissible=choices,
                            mandatory=True)

        if answer in set("aA"):
            add_file_entry(file_content)
            file_content[:] = sorted(file_content)
            dirty = True
        elif answer in set("dD"):
            del_file_entry(file_content)
            file_content[:] = sorted(file_content)
            dirty = True
        elif answer in set("sS"):
            if save_file(file_name, file_content):
                dirty = False
        elif answer in set("qQ"):
            handle_quit_editing(file_name, file_content, dirty)
            return

        print()


def main():
    """
The main function looping over a user's iteractions.
    """

    while True:
        files = [file for file in os.listdir(".") if file and
                 file.endswith(EXTENSION)]

        if not files:
            handle_new_file()
            print()
            continue

        files[:] = sorted(files)
        handle_file_list(files)
        print()


main()
