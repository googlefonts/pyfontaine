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


class Library(object):

    _charmaps = []

    def register(self, charmap):
        self._charmaps.append(charmap())

    @property
    def charmaps(self):
        return self._charmaps


library = Library()

from fontaine.charmaps import *
from fontaine.ext.extensis import Extensis


for ext in Extensis.get_codepoints():

    class Charmap:
        common_name = u'Extensis %s' % ext.getparent().attrib['name']
        native_name = u''
        glyphs = Extensis.get_unicodes(ext)

    library.register(Charmap)
