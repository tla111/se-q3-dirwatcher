#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

import os
import time
import signal
import argparse
import sys
import logging
__author__ = "Timothy La (tla111)"
'Received help from Joseph & Coach John W'

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
exit_flag = False
master_dict = {}


def search_for_magic(ns):
    try:
        for file in master_dict:
            with open(ns.dir + "/" + file, 'r') as f:
                lines = f.readlines()
                for index, line in enumerate(lines):
                    if ns.magicword in line:
                        if index not in master_dict[file]:
                            master_dict[file].append(index)
                            logger.info(
                                "The magic word, " +
                                ns.magicword.upper() + " was found on line "
                                + str(index + 1) + " in " + file)
                        if ns.magicword not in line:
                            logger.info(
                                "The magic word, " +
                                ns.magicword.upper() + " is not found")
    except Exception as e:
        logger.info(e)


def watch_directory(ns):
    file_dict = {}
    # while not exit_flag:
    # time.sleep(interval)
    try:
        if os.path.isdir(ns.dir):
            directories = os.listdir(os.path.abspath(ns.dir))
            for files in directories:
                if files.endswith(ns.file):
                    file_dict.setdefault(files, [])
        else:
            logger.info('No directory found')
    except Exception as e:
        logger.info(e)
    detect_dir_changes(file_dict, ns)


def detect_dir_changes(file_dict, ns):
    try:
        for files in file_dict:
            if files not in master_dict:
                logger.info(files + " has been added to " + ns.dir)
                master_dict[files] = []
        for files in master_dict:
            if files not in file_dict:
                logger.info(files + " has been removed from " + ns.dir)
                del master_dict[files]
    except Exception as e:
        logger.info(e)
    search_for_magic(ns)


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
            watch_directory(ns)
        except Exception as e:
            logger.info(e)

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        # time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start
    return


if __name__ == '__main__':
    main(sys.argv[1:])
