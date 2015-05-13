from __future__ import print_function
import logging

from lxml import etree

import re
import unicodedata

from fontaine.ext.base import BaseExt
from fontaine.ext.update import get_from_cache


EXTENSIS_LANG_XML = 'https://raw.github.com/davelab6/extensis-languages/master/languages.xml'


class Extension(BaseExt):

    extension_name = 'extensis'
    description = 'Extensis collection'

    @staticmethod
    def __getcharsets__():
        glyphs = {}
        for ext in Extension.get_codepoints():
            parent_name = ext.getparent().attrib.get('parent')

            common_name = ext.getparent().attrib['name']
            unicodes = []
            if parent_name:
                common_name += u' + ' + parent_name
                unicodes = glyphs.get(parent_name, [])
            unicodes += Extension.get_unicodes(ext)
            glyphs[ext.getparent().attrib['name']] = unicodes

            abbr = ext.getparent().attrib['abbreviated-name']

            yield type('Charset', (object,),
                       dict(glyphs=unicodes, common_name=u'Extensis {}'.format(common_name),
                            native_name='', abbreviation=abbr,
                            short_name=unicodedata.normalize('NFKD', u'extensis-{}'.format(common_name.lower().replace(' ', '-').replace('-+-', '+')))))

    @staticmethod
    def get_codepoints():
        """ Return all XML <scanning-codepoints> in received XML """
        # response = requests.get(EXTENSIS_LANG_XML)
        # if response.status_code != 200:
        #     return []

        path = get_from_cache('languages.xml', EXTENSIS_LANG_XML)

        try:
            xml_content = open(path, 'r').read()
        except IOError:
            logging.error('Could not read languages.xml from cache')
            xml_content = ''

        content = re.sub('<!--.[^>]*-->', '', xml_content)
        doc = etree.fromstring(content.lstrip('`'))

        return doc.findall('.//scanning-codepoints')

    @staticmethod
    def get_unicodes(codepoint):
        """ Return list of unicodes for <scanning-codepoints> """
        result = re.sub('\s', '', codepoint.text)
        return Extension.convert_to_list_of_unicodes(result)
