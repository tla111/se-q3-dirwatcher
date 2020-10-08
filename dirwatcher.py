#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Timothy La (tla111)"

import sys
import argparse
import signal
import time


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    # Step 1
    parser = argparse.ArgumentParser(
        description="Find magic word"
    )
    # parser.add_argument('-file', '--File',
    #                     help='Tell user to insert filename when running dirwatcher.py')
    # parser.add_argument('magicword', help='Tell user to look up magicword)

    return parser
    # python dirwatcher.py magic/file.txt bananas
    return


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    # Your code here
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
