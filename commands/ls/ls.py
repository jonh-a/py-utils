import os
import sys
import pwd
import grp
import argparse
from datetime import datetime

desc = "list directory contents"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('FILE', nargs='*', help="file",
                    default=[os.getcwd()])
parser.add_argument('-a', '--all', action='store_true')
parser.add_argument('-l', '--long', action='store_true')
args = parser.parse_args()


class File:
    def __init__(self, path):
        absolute_path = self.convert_to_absolute_path(path)
        if self.determine_if_file(path) is False:
            contents = self.get_contents(absolute_path)
            long_data = self.check_if_long(path, contents)

    def convert_to_absolute_path(self, path):
        if os.path.isabs(path) is True:
            return path
        else:
            absolute_path = os.path.abspath(path)
            if os.path.isfile(absolute_path) is True or os.path.isdir(absolute_path) is True:
                return absolute_path
            else:
                print(f"ls: {path}: No such file or directory")
                sys.exit(1)

    def determine_if_file(self, path):
        return os.path.isfile(path)
    
    def get_contents(self, path):
        return os.listdir(path)

    def check_if_long(self, path, files):
        if args.long is True:
            long_data = []
            for file in files:
                if str(file).startswith('.') is False or args.all is True:
                    data = self.get_long_file_info(path, file)
                    long_data.append(data)
            for string in long_data:
                if string is not None:
                    print(f"{string}")
        else:
            for file in files:
                if str(file).startswith('.') is False or args.all is True:
                    print(file)
    
    def get_long_file_info(self, path, file):
        try:
            stat_info = os.stat(os.path.join(path, file))
            directory = os.path.isdir(os.path.join(path, file))
            permissions = self.octal_to_string_permissions(oct(stat_info.st_mode)[-3:], directory)
            n_links = stat_info.st_nlink
            size = stat_info.st_size
            user_owner = pwd.getpwuid(stat_info.st_uid).pw_name
            group_owner = grp.getgrgid(stat_info.st_gid).gr_name
            last_modified = datetime.utcfromtimestamp(stat_info.st_mtime).strftime("%b %d %H:%M")
            string = f"{permissions}\t{n_links}\t{user_owner}\t{group_owner}\t{size}\t{last_modified}\t{file}"
            return string
        except:
            return

    @staticmethod
    def octal_to_string_permissions(octal_value, directory):
        result = ""
        values = [(4, "r"), (2, "w"), (1, "x")]
        if directory is True:
            result += "d"
        else:
            result += "-"
        for digit in octal_value:
            digit = int(digit)
            for num, string in values:
                if digit >= num:
                    result += string
                    digit -= num
                else:
                    result += '-'
        return result


def main():
    if len(args.FILE) > 1:
        for file in args.FILE:
            print(f"{file}:")
            File(file)
            print("\n")
    else:
        File(args.FILE[0])


if __name__ == "__main__":
    main()