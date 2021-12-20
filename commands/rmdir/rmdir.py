import os
import sys
import argparse

desc = "remove directories"


parser = argparse.ArgumentParser(description=desc)
parser.add_argument('DIRECTORY', nargs='*', help="file",
                    default=None)
parser.add_argument('-p', '--path', action='store_true', help="""Each directory argument is treated as a pathname of which all
            components will be removed, if they are empty, starting with the
            last most component.  (See rm(1) for fully non-discriminant
            recursive removal.)""")
args = parser.parse_args()

def rm_directory(path):
    try:
        if args.path is True:
            os.removedirs(path)
        else:
            os.rmdir(path)
    except FileNotFoundError:
        print(f"rmdir: Use -p to remove intermediate directories as required.")
        sys.exit(1)
    except Exception as e:
        print("rmdir: Something unexpected happened")
        print(e)

def main(args):
    if len(args.DIRECTORY) > 0:
        for dir in args.DIRECTORY:
            rm_directory(dir)

if __name__ == '__main__':
    main(args)