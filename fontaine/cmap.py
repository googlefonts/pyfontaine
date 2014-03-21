# -*- coding: utf-8 -*-
#
# cmap.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.
from importlib import import_module

import fontaine.ext
import fontaine.charmaps


class Library(object):

    def __init__(self):
        self._charmaps = []
        self.collections = ['all']

    def register(self, charmap):
        self._charmaps.append(charmap())

    @property
    def charmaps(self):
        if self._charmaps:
            return self._charmaps

        for ext in fontaine.ext.__all__:
            try:
                module = import_module('fontaine.ext.%s' % ext)
                extension_name = module.Extension.extension_name
            except (ImportError, AttributeError):
                continue

            if 'all' in self.collections or extension_name in self.collections:
                for charmap_klass in module.Extension.get_charmaps():
                    self.register(charmap_klass)

        if 'all' in self.collections or 'pyfontaine' in self.collections:
            for ext in fontaine.charmaps.__all__:
                try:
                    module = import_module('fontaine.charmaps.%s' % ext)
                    self.register(module.Charmap)
                except (ImportError, AttributeError):
                    continue
        return self._charmaps


library = Library()
