import argparse
import sys

desc = "do nothing, unsuccessfully"

parser = argparse.ArgumentParser(description=desc)
parser.parse_args()


def main():
    sys.exit(1)


if __name__ == "__main__":
    main()
