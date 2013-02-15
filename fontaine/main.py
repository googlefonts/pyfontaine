# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# main.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.
from __future__ import print_function
import argparse
import codecs
import os
import sys

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.realpath(path))

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from fontaine.font import Font
from fontaine.builder import Builder, Director


def usage():
    parser = argparse.ArgumentParser(description='Output information about fonts in different formats')
    parser.add_argument('font', metavar='font', type=str, nargs='+')
    parser.add_argument('--disable-unames', action='store_true',
                        help='If libunicodenames is installed this will prevent using it')
    parser.add_argument('--text', action='store_true',
                        help='Output information in plain text')
    parser.add_argument('--xml', action='store_true',
                        help='Output information into XML')
    parser.add_argument('--json', action='store_true',
                        help='Output information in JSON')
    parser.add_argument('--csv', action='store_true',
                        help='Output font coverage information in CSV')
    return parser.parse_args()


def main(*argv):
    args = usage()

    fonts = []
    for filename in args.font:
        fonts.append(Font(filename))

    if args.disable_unames:
        os.environ['DISABLE_UNAMES'] = 'disable'

    director = Director()
    if args.xml:
        tree = director.construct_tree(fonts)
        Builder.xml_(tree).display()
    elif args.csv:
        sys.stdout.write(Builder.csv_(fonts))
    elif args.json:
        tree = director.construct_tree(fonts)
        Builder.json_(tree)
    else:
        tree = director.construct_tree(fonts)
        Builder.text_(tree).display()

    if not os.environ.get('UNAMES_INSTALLED'):
        print('Warning: package `libunicodenames` is not installed',
              file=sys.stderr)


if __name__ == '__main__':
    main()
