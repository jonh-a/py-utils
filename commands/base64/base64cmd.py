#!/usr/bin/env python3

import argparse
import sys
import base64
import textwrap

desc = "Base64 encode or decode FILE, or standard input, to standard output."

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('FILE', nargs='?',
                    help="Base64 encode or decode file contents")
parser.add_argument('-d', '--decode', action='store_true',
                    help="decode data")
parser.add_argument('-w', '--wrap', metavar="COLS",
                    help="wrap encoded lines after COLS character (default 76).  Use 0 to disable line wrapping")
args = parser.parse_args()


def read_file(filename: str) -> str:
    try:
        f = open(filename, 'r')
        return f.read()
    except:
        print("File not found.")
        exit()


def encode(file_content: str) -> str:
    try:
        return base64.b64encode(str.encode(file_content), altchars=b'+/').decode('utf-8')
    except:
        print("An error occurred while encoding the file.")
        sys.exit(1)


def decode(file_content: str, altchars=b'+/') -> str:
    #file_content = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', file_content)
    try:
        missing_padding = len(file_content) % 4
        if missing_padding:
            file_content += '=' * (4 - missing_padding)
        return base64.b64decode(str.encode(file_content)).decode('utf-8')
    except:
        print("An error occurred while decoding the file.")
        sys.exit(1)


def wrap_output(data: str, width: int) -> str:
    if width == 0:
        return data
    else:
        return "\n".join(textwrap.wrap(data, width=width))


def main() -> None:
    if args.wrap:
        try:
            width = int(args.wrap)
        except:
            print("Invalid wrap length provided (must be integer)")
            sys.exit(1)
    else:
        width = 76

    if args.FILE:
        file_content = read_file(args.FILE)
        if args.decode:
            decoded = decode(file_content)
            print(decoded[:decoded.rfind('\n')])
        else:
            print(wrap_output(encode(file_content), width))
        sys.exit(0)
    elif not sys.stdin.isatty():
        raw_text = sys.stdin.read()
        formatted_text = raw_text[:raw_text.rfind('\n')]
        if args.decode:
            decoded = decode(formatted_text)
            print(decoded[:decoded.rfind('\n')])
        else:
            print(wrap_output(encode(formatted_text), width))
        sys.exit(0)
    else:
        print("No input provided")
        sys.exit(1)


if __name__ == "__main__":
    main()
