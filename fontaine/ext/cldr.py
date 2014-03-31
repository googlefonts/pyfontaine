# -*- coding utf-8 -*-
try:
    from icu import Locale
except ImportError:
    package = "[PyICU](https://pypi.python.org/pypi/PyICU)"
    raise Exception('Please install %s' % package)

import os
import os.path as op
import re
try:
    import ujson as pfjson
except ImportError:
    import json as pfjson
import zipfile

from fontaine.ext.base import BaseExt
from fontaine.ext.update import get_data_directory, get_from_cache


JSON_DATA_URL = 'http://www.unicode.org/Public/cldr/latest/json.zip'


def to_ordinal(value):
    try:
        return ord(value)
    except TypeError:
        pass


class Extension(BaseExt):

    extension_name = 'cldr'

    @staticmethod
    def to_charmap(json, language):
        # collect all glyphs from json data
        characters = json['main'][language]['characters']
        exemplar = characters['exemplarCharacters']
        auxiliary = characters.get('auxiliary')
        index = characters.get('index')
        punctuation = characters.get('punctuation')
        unicodes = []
        unicodes += re.sub(r'^\[|\]$', '', exemplar).split()
        if auxiliary:
            unicodes += re.sub(r'^\[|\]$', '', auxiliary).split()
        if index:
            unicodes += re.sub(r'^\[|\]$', '', index).split()
        if punctuation:
            unicodes += re.sub(r'^\[|\]$', '', punctuation).split()

        glyphs = []
        for uni in unicodes:
            uni = to_ordinal(uni)
            if not uni:
                continue
            glyphs.append(uni)
        return glyphs

    @staticmethod
    def __getcharmaps__():
        pyfontaine_datadir = get_data_directory()
        cldr_data_directory = op.join(pyfontaine_datadir, 'cldr')
        # check that we have cldr directory
        if not op.exists(cldr_data_directory):
            # if we do not have it then download new or copy existed cldr data
            # from package and extract it to destination directory
            filepath = get_from_cache('json.zip', JSON_DATA_URL)
            zf = zipfile.ZipFile(filepath)
            zf.extractall(cldr_data_directory)

        for ch in os.listdir(op.join(cldr_data_directory, 'main')):
            jsonf = op.join(cldr_data_directory, 'main', ch, 'characters.json')
            jsondata = pfjson.load(open(jsonf))

            locale, ext = op.splitext(ch)

            yield type('Charmap', (object,),
                       dict(glyphs=Extension.to_charmap(jsondata, locale),
                            common_name='CLDR ' + Locale(locale).getDisplayName(),
                            native_name='', abbreviation=locale))
