import grp
import pwd
import os
import getpass
import sys
import argparse

desc = "Print user and group information for the specified USER, or (when USER omitted) for the current user."

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('USER', nargs='*', help="username",
                    default=[getpass.getuser()])
parser.add_argument('-g', '--group', action='store_true',
                    help="print only the effective group ID")
parser.add_argument('-G', '--groups', action='store_true',
                    help="print all group IDs")
parser.add_argument('-u', '--user', action='store_true',
                    help="print only the effective user ID")
args = parser.parse_args()


class User:
    def __init__(self, username):
        try:
            self.username = username
            self.uid = pwd.getpwnam(username).pw_uid
            self.group = grp.getgrnam(self.username).gr_name
            self.gid = grp.getgrnam(self.username).gr_gid
            self.member_grps = [
                g.gr_name for g in grp.getgrall() if self.username in g.gr_mem]
            self.member_gids = [
                grp.getgrnam(g).gr_gid for g in self.member_grps]
            self.full_string = f"uid={self.uid}({username}) gid={self.gid}({self.group}) groups={self.parse_grps()}"
            self.print_output()
        except:
            print("something unexpected happened.")
            sys.exit(1)

    def parse_grps(self):
        parsed_groups_list = [f"{self.gid}({self.group})"]
        try:
            i = 0
            while i < len(self.member_grps):
                parsed_groups_list.append(
                    f"{self.member_gids[i]}({self.member_grps[i]})")
                i += 1
            return ",".join(parsed_groups_list)
        except:
            print("something unexpected happened.")
            sys.exit(1)

    def print_output(self):
        if not args.group and not args.groups and not args.user:
            print(self.full_string)
        if args.group:
            print(self.gid)
        if args.groups:
            print(" ".join(str(g) for g in self.member_gids))
        if args.user:
            print(self.uid)


def main():
    User(args.USER[0])


if __name__ == "__main__":
    main()
