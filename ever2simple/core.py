from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
import os
import sys
from ever2simple.converter import EverConverter
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog=None,
        description="Convert Evernote.enex files to Markdown",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'enex-file',
        help="the path to the Evernote.enex file")
    parser.add_argument(
        '-o', '--output',
        help=("the path to the output file or directory, leave blank to "
              "output to the terminal (stdout)"))
    parser.add_argument(
        '-f', '--format',
        help="the output format, json, csv or a directory",
        choices=['json', 'csv', 'dir'],
        default='json')
    parser.add_argument(
        '--preserve_title',
        action="store_true",
        help="Try to preserve the note title as the file name",
        default=False)
    parser.add_argument(
        '-v', '--verbose',
        action="store_true",
        help="Increase output verbosity",
        default=False)
    args = parser.parse_args()
    enex_file = vars(args)['enex-file']
    output = args.output
    fmt = args.format
    preserve_title = args.preserve_title
    verbose = args.verbose
    filepath = os.path.expanduser(enex_file)

    if not os.path.exists(filepath):
        print('File does not exist: {}'.format(filepath))
        sys.exit(1)
    converter = EverConverter(filepath, simple_filename=output, fmt=fmt,
                              preserve_title=preserve_title, verbose=verbose)
    converter.convert()
    sys.exit()


if __name__ == '__main__':
    main()
