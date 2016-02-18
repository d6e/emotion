""" A simple CLI tool for quickly copying common emoticon/emoji to your
clipboard. """
import pyperclip
import argparse
import json
import sys
import os

def read_emote_mappings(filename="mapping.json"):
    emotes = {}
    for fname in [filename, os.path.expanduser("~/.emotes.json")]:
        with open(fname) as f:
            emotes.update(json.loads(f.read().decode('utf-8')))
    return emotes

def parse_arguments():
    parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__)
    parser.add_argument('-l','--list', action="store_true",
                        help="List all available emotes.")
    parser.add_argument('-s','--silent', action="store_true",
                        help="Don't print to stdout.")
    parser.add_argument('--no-clipboard', action="store_false",
                        help="Don't copy to clipboard.")
    parser.add_argument("name", type=str, nargs='?',
                        help="The name of the emote.")
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)
    return parser.parse_args()

def list_emotes(emotes):
    for k, v in emotes.iteritems():
        whitespace = 30
        pad = whitespace - len(k)
        print "{}{}{}".format(k.encode('utf-8'), " "*pad, v.encode('utf-8'))

def print_emote(name, emotes, silent=False, clipboard=True):
    try:
        emote = emotes[name]
        if clipboard:
            pyperclip.copy(emote)
        if not silent:
            print emote
    except KeyError:
        print("That emote does not exist. You can see all existing emotes "
        "with the command: `emote -l`.")

def main():
    args = parse_arguments()
    emotes = read_emote_mappings()
    if args.list:
        list_emotes(emotes)
    if args.name:
        print_emote(args.name, emotes, silent=args.silent,
                    clipboard=args.no_clipboard)

if __name__ == "__main__":
    main()
