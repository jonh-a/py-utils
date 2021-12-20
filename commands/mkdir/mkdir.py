import os
import sys
import argparse

desc = "make directories"

#TODO implement -m

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('DIRECTORY', nargs='*', help="file",
                    default=None)
parser.add_argument('-m', '--mode', nargs=1, help="""Set the file permission bits of the final created directory to
            the specified mode.  The mode argument can be in any of the for-
            mats specified to the chmod(1) command.  If a symbolic mode is
            specified, the operation characters ``+'' and ``-'' are inter-
            preted relative to an initial mode of ``a=rwx''.""")
parser.add_argument('-p', '--path', action='store_true', help="""Create intermediate directories as required.  If this option is
            not specified, the full path prefix of each operand must already
            exist.  On the other hand, with this option specified, no error
            will be reported if a directory given as an operand already
            exists.  Intermediate directories are created with permission
            bits of rwxrwxrwx (0777) as modified by the current umask, plus
            write and search permission for the owner.""")
args = parser.parse_args()

def make_directory(path):
    try:
        if args.path is True:
            os.makedirs(path)
        else:
            os.mkdir(path)
    except FileNotFoundError:
        print(f"mkdir: Use -p to create intermediate directories as required.")
        sys.exit(1)
    except Exception:
        print("mkdir: Something unexpected happened")

def main(args):
    if len(args.DIRECTORY) > 0:
        for dir in args.DIRECTORY:
            make_directory(dir)

if __name__ == '__main__':
    main(args)