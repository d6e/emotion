""" A simple CLI tool for quickly copying common emoticon/emoji to your
clipboard. """
import pyperclip
import json
import sys
import argparse

with open("mapping.json") as f:
    emotes = json.load(f)

def parse_arguments():
    parser = argparse.ArgumentParser(
            description=sys.modules[__name__].__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l','--list', action="store_true",
                        help="List all available emotes.")

    # Print help if no cli args are specified.
    if len(sys.argv) < 2:
        parser.print_help()
    return parser.parse_args()

def list_emotes():
    print [e for e in emotes.keys()]
    print [e for e in emotes.values()]

def main():
    args = parse_arguments()
    if args.list:
        list_emotes()


if __name__ == "__main__":
    main()
