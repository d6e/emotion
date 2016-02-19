""" A simple CLI tool for quickly copying common emoticon/emoji to your
clipboard. """
import pyperclip
import argparse
import json
import sys
import os

def read_emote_mappings(json_obj_files=[]):
    """ Reads the contents of a list of files of json objects and combines
    them into one large json object. """
    super_json = {}
    for fname in json_obj_files:
        with open(fname) as f:
            super_json.update(json.loads(f.read().decode('utf-8')))
    return super_json

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
    emote_files = [
        os.path.join(os.path.dirname(__file__), 'mapping.json'),
        os.path.expanduser("~/.emotes.json")
    ]
    emotes = read_emote_mappings(emote_files)
    if args.list:
        list_emotes(emotes)
    if args.name:
        print_emote(args.name, emotes, silent=args.silent,
                    clipboard=args.no_clipboard)

if __name__ == "__main__":
    main()
