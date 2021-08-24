import argparse
import sys

desc = "do nothing, successfully"

parser = argparse.ArgumentParser(description=desc)
parser.parse_args()


def main():
    sys.exit(0)


if __name__ == "__main__":
    main()
