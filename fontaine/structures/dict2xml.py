# -*- coding: utf-8 -*-
#
# dict2xml.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

from __future__ import print_function
from collections import OrderedDict
import re
import sys

from xml.dom.minidom import Document


class dict2xml(object):

    def __init__(self, structure):
        self.doc = Document()

        if len(structure) == 1:
            rootName = unicode(structure.keys()[0])
            self.root = self.doc.createElement(rootName)

            self.doc.appendChild(self.root)
            identical = structure[rootName].pop('identical', None)
            if identical is not None:
                itag = self.doc.createElement('identical')
                if identical:
                    textnode = self.doc.createTextNode(u'All fonts have the same character sets.')
                else:
                    textnode = self.doc.createTextNode(u'All fonts do NOT have the same character sets.')
                itag.appendChild(textnode)
                self.root.appendChild(itag)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == OrderedDict:
            for k in structure.keys():
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            tagName = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)

        else:
            data = unicode(structure)
            tag = self.doc.createTextNode(data)
            father.appendChild(tag)

    def display(self):
        sys.stdout.write(self.doc.toprettyxml(indent="  "))


class dict2txt(object):

    def __init__(self, structure, names=None, indent='  '):
        self.output = u''
        self.indent = indent
        self.names = names

        identical = structure.pop('identical', None)
        if len(structure) == 1:
            rootName = unicode(structure.keys()[0])
            self.output += self.name(rootName) + '\n'
            if rootName.lower() == 'fonts' and identical is not None:
                if identical:
                    self.output += u'%sAll fonts have the same character sets.\n' % indent
                else:
                    self.output += u'%sAll fonts do NOT have the same character sets.\n' % indent
            self.build(structure[rootName])

    def name(self, key):
        return self.names.get(key, key)

    def build(self, structure, indent=''):
        if isinstance(structure, OrderedDict):
            for k in structure.keys():
                if isinstance(structure[k], OrderedDict):
                    self.output += u'%s%s:' % (indent, self.name(k)) + '\n'
                    self.build(structure[k], indent + self.indent)
                elif isinstance(structure[k], list):
                    self.output += u'%s%s:' % (indent, self.name(k)) + '\n'
                    self.build(structure[k], indent + self.indent)
                elif structure[k]:
                    self.output += u'%s%s:' % (indent, self.name(k))
                    if k == 'missingValues':
                        self.build(re.sub(r'U\+',
                                          '%sU+' % (indent + self.indent * 2),
                                          structure[k]))
                    else:
                        self.build(structure[k], indent + self.indent)
        elif isinstance(structure, list):
            for k, l in enumerate(structure):
                self.build(structure[k], indent + self.indent)
        elif structure:
            self.output += u' %s' % unicode(structure) + '\n'

    def display(self):
        sys.stdout.write(self.output)
