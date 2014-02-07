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
from fontaine.ext.fontconfig import Fontconfig

glyphs = {}

for ext in Extensis.get_codepoints():

    parent_name = ext.getparent().attrib.get('parent')

    common_name = u'Extensis %s' % ext.getparent().attrib['name']
    unicodes = []
    if parent_name:
        common_name += u' + ' + parent_name
        unicodes = glyphs.get(parent_name, [])
    unicodes += Extensis.get_unicodes(ext)
    glyphs[ext.getparent().attrib['name']] = unicodes

    Charmap = type('Charmap', (object,),
                   dict(glyphs=unicodes, common_name=common_name,
                        native_name=''))

    library.register(Charmap)


for ext in Fontconfig.iterate_orth():
    unicodes, common_name = Fontconfig.get_orth_charmap(ext)

    if not common_name:
        continue

    Charmap = type('Charmap', (object,),
                   dict(glyphs=unicodes, common_name=common_name,
                        native_name=''))

    library.register(Charmap)
