#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

import os
import time
import signal
import argparse
import sys
__author__ = "Timothy La (tla111)"
'Received help from Joseph'


exit_flag = False


def search_for_magic(filename, start_line, magic_string):
    # file_dict = {}
    # with open(filename, 'r') as file:
    #     file.read()
    return


def watch_directory(path, magic_string, extension, interval):
    file_dict = {}
    while not exit_flag:
        time.sleep(interval)
        directories = os.listdir(os.path.abspath(path))
        for files in directories:
            file_dict[files] = 0
        # Check if there is a key already in file_dict
        #   Delete key is there already is
        print(file_dict)


def create_parser():
    # Your code here
    # Step 1
    parser = argparse.ArgumentParser(
        description="Find magic word"
    )
    parser.add_argument(
        '-file', help='adds file extension to end of file', default='.txt')
    parser.add_argument('dir', help='Specifies directory')
    parser.add_argument('magicword', help='Tell user to look up magicword')
    parser.add_argument(
        '-interval', help='Determines processing speed', type=float, default=1)
    return parser


def signal_handler(sig_num, frame):
    global exit_flag
    exit_flag = True
    return


def main(args):
    # Your code here
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)

     # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            watch_directory(ns.dir, ns.magicword, ns.file, ns.interval)
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        # time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start
    return


if __name__ == '__main__':
    main(sys.argv[1:])
