import os
import sys
import argparse

desc = """Print  the  first  10  lines of each FILE to standard output.  With more than one FILE, precede each with a header
       giving the file name.

       With no FILE, or when FILE is -, read standard input.

       Mandatory arguments to long options are mandatory for short options too."""

parser = argparse.ArgumentParser(description=desc)
parser.add_argument(
    'FILE', nargs="*", help="file to read"
)
parser.add_argument(
    '-n', '--lines', help="print the first NUM lines instead of the first 10", default=10, type=int)
args = parser.parse_args()


class Text:
    def __init__(self: object, text: str) -> None:
        self.text = text
        self.nlines = self.get_first_n_lines(args.lines)

    def get_first_n_lines(self, n) -> str:
        self.text_split = self.text.split('\n')
        return "\n".join(self.text_split[:n])


def read_file(filename: str) -> str:
    try:
        file = open(filename, 'r')
        return file.read()
    except:
        print("head: file does not exist or could not be read.")
        sys.exit(1)


def main() -> None:
    if args.FILE:
        file_content = read_file(args.FILE[0])
        text = Text(file_content[:file_content.rfind('\n')])
        print(text.nlines)
        return

    elif not sys.stdin.isatty():
        raw_text = sys.stdin.read()
        formatted_text = raw_text[:raw_text.rfind('\n')]
        text = Text(formatted_text)
        print(text.nlines)
    else:
        print("An error occurred.")
        sys.exit(1)


if __name__ == "__main__":
    main()
