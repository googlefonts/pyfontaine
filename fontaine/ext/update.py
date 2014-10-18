#!/usr/bin/env python
# coding: utf-8
# Only pyfontaine developers should use this file to update files
import logging
import os
import os.path as op
import requests
import shutil


APPDATA_DIRNAME = 'pyfontaine'


def get_data_directory():
    try:
        #Windows code:
        d = op.join(os.environ["APPDATA"], APPDATA_DIRNAME)
    except KeyError:
        #Linux and Mac code:
        d = op.join(op.expanduser("~"), ".local", "share", APPDATA_DIRNAME)
    if not op.exists(d):
        os.makedirs(d)
    return d


def get_file(name, url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException:
        logging.warn(('Please run pyfontaine with an active internet '
                      'connection to download all character maps'))
        return False
    if r.status_code == 200:
        logging.warn('Updating {}'.format(name))
        directory = get_data_directory()
        filepath = op.join(directory, name)
        with open(filepath, 'w') as f:
            f.write(r.content)
        return True


def get_from_cache(filename, url):
    directory = get_data_directory()
    filepath = op.join(directory, filename)
    if not op.exists(filepath) and not get_file(filepath, url):
        shutil.copy(op.join(os.path.dirname(__file__), 'data', filename),
                    filepath)
    return filepath


def bulkupdate():
    get_file('Blocks.txt', 'http://www.unicode.org/Public/UNIDATA/Blocks.txt')
    get_file('languages.xml', 'https://raw.github.com/davelab6/extensis-languages/master/languages.xml')
    get_file('AdobeSourceSansDevanagariGlyphOrderAndAliasDB.txt', 'https://raw.githubusercontent.com/pauldhunt/source-devanagari-sans/master/GlyphOrderAndAliasDB')
