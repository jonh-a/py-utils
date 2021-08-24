#!/usr/bin/env python3

import argparse
import codecs

desc = "display a line of text"


def unescaped_string(string):
    return codecs.decode(str(string), 'unicode_escape')


parser = argparse.ArgumentParser()
parser.add_argument("STRING", nargs="*", type=unescaped_string,
                    help="string to display")
parser.add_argument("-s", dest="nospaces", action="store_true",
                    help="do not sepearate arguments with spaces")
parser.add_argument("-E", dest="noescapes", action="store_true",
                    help="disable interpretation of backslash escapes (default)")
parser.add_argument("-e", dest="escapes", action="store_true",
                    help="enable interpretation of backslash escapes")
args = parser.parse_args()


def main():
    if args.nospaces:
        separator = ""
    else:
        separator = " "
    string = separator.join(args.STRING)
    if args.escapes:
        print(string)
    else:
        string = string.replace("\n", "\\n")
        print(string)


if __name__ == "__main__":
    main()
