#!/usr/bin/env python
# coding: utf-8
# Only pyfontain developers should use this file to update files

import requests


def get_file(name, url):
    r = requests.get(url)
    if r.status_code == 200:
        with open(name, 'w') as f:
            f.write(r.content)

if __name__ == '__main__':
    get_file('Blocks.txt', 'http://www.unicode.org/Public/UNIDATA/Blocks.txt')
    get_file('languages.xml', 'https://raw.github.com/davelab6/extensis-languages/master/languages.xml')
