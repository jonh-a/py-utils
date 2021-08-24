#!/usr/bin/env python3

import argparse
import os
import sys

desc = "concatenate files and print on the standard output"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("FILE", nargs='*',
                    help="concatenate FILE(s) to standard output.")
parser.add_argument('-E', '--show-ends', action='store_true', dest='showends',
                    help="display $ at the end of each line")
parser.add_argument('-n', '--number', action='store_true', dest='number',
                    help="number all output lines")
parser.add_argument('-T', '--show-tabs', action='store_true', dest='showtabs',
                    help="display TAB characters as ^I")
args = parser.parse_args()


def read_file(filename: str) -> str:
    try:
        file = open(filename, 'r')
        return file.read()
    except:
        print("Invalid file was provided.")
        sys.exit(1)


def show_ends(file_content: str) -> str:
    modified_content = []
    for line in file_content.split('\n'):
        modified_content.append(line + "$")
    return "\n".join(modified_content)


def show_numbers(file_content: str) -> str:
    modified_content = []
    for index, line in enumerate(file_content.split('\n')):
        modified_content.append(str(index) + "\t" + str(line))
    return "\n".join(modified_content)


def show_tabs(file_content: str) -> str:
    return file_content.replace("\t", "^I")


def structure_output(file_content):
    if args.showends:
        file_content = show_ends(file_content)
    if args.showtabs:
        file_content = show_tabs(file_content)
    if args.number:
        file_content = show_numbers(file_content)
    return file_content


def main():
    if len(args.FILE) == 0:
        print("Filename is required.")
        exit()
    file_content = ""
    for file in args.FILE:
        file_content += read_file(file)
    output = structure_output(file_content[:file_content.rfind('\n')])
    print(output)


if __name__ == "__main__":
    main()
