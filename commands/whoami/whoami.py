#!/usr/bin/env python3

import argparse
import getpass

desc = "print effective userid"

parser = argparse.ArgumentParser(description=desc)
args = parser.parse_args()


def main():
    username = getpass.getuser()
    print(username)


if __name__ == "__main__":
    main()
