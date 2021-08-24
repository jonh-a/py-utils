import grp
import pwd
import getpass
import sys
import argparse

desc = "print the groups a user is in"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('USER', nargs='*', help="username",
                    default=[getpass.getuser()])
args = parser.parse_args()


class User:
    def __init__(self, username):
        try:
            self.username = username
            self.uid = pwd.getpwnam(username).pw_uid
            self.member_grps = [
                g.gr_name for g in grp.getgrall() if self.username in g.gr_mem]
            print(f"{username} : {username} {' '.join(self.member_grps)}")
        except:
            print("something unexpected happened.")
            sys.exit(1)


def main():
    User(args.USER[0])


if __name__ == "__main__":
    main()
