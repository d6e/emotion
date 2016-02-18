""" A simple CLI tool for quickly copying common emoticon/emoji to your
clipboard. """
import pyperclip
import json
import sys
import argparse

with open("mapping.json") as f:
    emotes = json.load(f)

def main():
    parser = argparse.ArgumentParser(
            description=sys.modules[__name__].__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p','--web_port')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
