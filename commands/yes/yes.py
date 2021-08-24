import argparse

desc = "output a string repeatedly until killed"

parser = argparse.ArgumentParser()
parser.add_argument('STRING', nargs="*", default=['y'],
                    help="optional string, else 'y'")
args = parser.parse_args()


def main():
    while True:
        print(" ".join(args.STRING))


if __name__ == "__main__":
    main()
