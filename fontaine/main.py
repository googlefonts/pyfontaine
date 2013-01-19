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
import os
import sys

sys.path.append(os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)
import argparse

from flinfo import Fonts


def usage():
    parser = argparse.ArgumentParser(description='Output information about fonts in different formats')
    parser.add_argument('font', metavar='font', type=str, nargs='+')
    parser.add_argument('--disable-unames', action='store_true', help='If libunicodenames is installed this will prevent using it')
    parser.add_argument('--text', action='store_true', help='Output information in plain text')
    parser.add_argument('--xml', action='store_true', help='Output information into XML')
    parser.add_argument('--json', action='store_true', help='Output information in JSON')
    parser.add_argument('--csv', action='store_true', help='Output font coverage information in CSV')
    return parser.parse_args()


def main(*argv):
    args = usage()

    fonts = Fonts()
    for _fontname in args.font:
        fonts.add_font(_fontname)

    if args.disable_unames:
        os.environ['DISABLE_UNAMES'] = 'disable'

    if args.xml:
        fonts.print_xml()
    elif args.csv:
        fonts.print_csv()
    else:
        fonts.print_plain_text()

    if not os.environ.get('UNAMES_INSTALLED'):
        print
        print 'Warning: package `libunicodenames` is not installed'
main()
