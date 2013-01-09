#!/usr/bin/env python
#
# fontaine.py
#
# Copyright (c) 2013, 
# Виталий Волков <hash.3g@gmail.com> 
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

import argparse

from flinfo import Fonts


def usage():
    parser = argparse.ArgumentParser(description='Output information about fonts in different formats')
    parser.add_argument('font', metavar='font', type=str, nargs='+')
    parser.add_argument('--text', action='store_true', help='Output information in plain text')
    parser.add_argument('--xml', action='store_true', help='Output information into XML')
    parser.add_argument('--json', action='store_true', help='Output information in JSON')
    return parser.parse_args()


def main(*argv):
    args = usage()

    fonts = Fonts()
    for _fontname in args.font:
        fonts.add_font(_fontname)

    if args.text:
        fonts.print_plain_text()
    elif args.xml:
        fonts.print_xml()


if __name__ == '__main__':
    main()
