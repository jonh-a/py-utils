#!/usr/bin/env python3

import argparse
import sys
import os


desc = "print newline, word, and byte counts for each file"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-c', '--bytes', action='store_true',
                    help="print the byte count")
parser.add_argument('-m', '--chars', action='store_true',
                    help="print the character count")
parser.add_argument('-l', '--lines', action='store_true',
                    help="print the line count")
parser.add_argument('-w', '--words', action='store_true',
                    help="print the word count")
parser.add_argument('-f', '--file',
                    help="read input from the files specified by NUL-terminated names in file F; If F is - then read names from standard input")
parser.add_argument('-L', '--max-line-length', action='store_true',
                    help="print the maximum display width")
args = parser.parse_args()


class Text:
    def __init__(self: object, text: str) -> None:
        self.text = text
        try:
            self.newline_count = self.get_newline_count()
            self.word_count = self.get_word_count()
            self.byte_count = self.get_byte_count()
            if not args.bytes and not args.lines and not args.words and not args.chars:
                print(f"{self.newline_count}\t{self.word_count}\t{self.byte_count}")
            else:
                print(str(self.newline_count) + "\t" if args.lines else '',
                      str(self.word_count) + "\t" if args.words else '',
                      str(self.byte_count) if args.bytes else '')
            return
        except:
            print("An error occurred.")
            sys.exit(1)

    def get_newline_count(self: object) -> int:
        newline_count = 0
        split_text = self.text.split("\n")
        for newline in split_text:
            newline_count += 1
        return newline_count

    def get_word_count(self: object) -> int:
        word_count = 0
        text_words = self.text.split()
        for word in text_words:
            word_count += 1
        return word_count

    def get_byte_count(self: object) -> int:
        return len(self.text.encode('utf-8')) + 1


def read_file(filename: str) -> str:
    try:
        file = open(filename, 'r')
        return file.read()
    except:
        print("An error occurred")
        sys.exit(1)


def main() -> None:
    if args.file:
        Text(read_file(args.file))
        return

    if not sys.stdin.isatty():
        raw_text = sys.stdin.read()
        formatted_text = raw_text[:raw_text.rfind('\n')]
        Text(formatted_text)
        return
    else:
        print("An error occurred.")
        sys.exit(1)


if __name__ == "__main__":
    main()
