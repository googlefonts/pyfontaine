# -*- coding: utf-8 -*-

import re

from xml.dom.minidom import Document


class dict2xml(object):
    doc = Document()

    def __init__(self, structure):
        if len(structure) == 1:
            rootName = unicode(structure.keys()[0])
            self.root = self.doc.createElement(rootName)

            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
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
        print self.doc.toprettyxml(indent="  ")


class dict2txt(object):

    def __init__(self, structure, indent='  '):
        self.output = u''
        self.indent = indent
        if len(structure) == 1:
            rootName = unicode(structure.keys()[0])
            self.output += rootName + '\n'
            self.build(structure[rootName])

    def build(self, structure, indent=''):
        if isinstance(structure, dict):
            for k in structure.keys():
                if isinstance(structure[k], dict):
                    self.output += u'%s%s:' % (indent, k) + '\n'
                    self.build(structure[k], indent + self.indent)
                elif isinstance(structure[k], list):
                    self.output += u'%s%s:' % (indent, k) + '\n'
                    self.build(structure[k], indent + self.indent)
                elif structure[k]:
                    self.output += u'%s%s:' % (indent, k)
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
        print self.output
