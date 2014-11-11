#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import fontaine
from fontaine.ext.base import BaseExt
from fontaine.ext.update import get_from_cache


from collections import OrderedDict
import fnmatch
import os


def get_targets(directory):
    targets = []
    for root, dirs, files in os.walk(directory):
        for f in fnmatch.filter(files, '*.txt'):
            targets.append(dict(name=os.path.splitext(f)[0],
                                path=os.path.join(root, f)))
    return targets


class Extension(BaseExt):
    extension_name = 'glyphlists'
    description = 'Glyph Lists'

    @staticmethod
    def __getcharmaps__():
        charmaps = []
        target_directory = os.path.join(os.path.dirname(fontaine.__file__),
                                        'glyphlists')
        for target in get_targets(target_directory):
            glyphnames = []
            with open(target['path'], 'r') as f:
                for line in f:
                    glyphnames.append(re.sub(r'\s+', ' ', line).split())
            charmap_dict = dict(glyphnames=glyphnames,
                                common_name=target['name'],
                                # short_name=target['name'].lower().replace(' ', '_'),
                                short_name=target['name'],
                                native_name='')
            charmaps.append(type('Charmap', (object,), charmap_dict))
        return charmaps