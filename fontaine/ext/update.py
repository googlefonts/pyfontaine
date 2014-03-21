#!/usr/bin/env python
# coding: utf-8
# Only pyfontain developers should use this file to update files
import os
import requests


APPDATA_DIRNAME = 'pyfontaine'


def get_file(name, url):
    r = requests.get(url)
    if r.status_code == 200:
        with open(name, 'w') as f:
            f.write(r.content)


def get_from_cache(filename, url):
    try:
        #Windows code:
        directory = os.path.join(os.environ["APPDATA"], APPDATA_DIRNAME)
    except KeyError:
        #Linux and Mac code:
        directory = os.path.join(os.path.expanduser("~"), ".local", "share", APPDATA_DIRNAME)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        get_file(filename, url)
    return filepath


if __name__ == '__main__':
    get_file('Blocks.txt', 'http://www.unicode.org/Public/UNIDATA/Blocks.txt')
    get_file('languages.xml', 'https://raw.github.com/davelab6/extensis-languages/master/languages.xml')
