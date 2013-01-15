class Library(object):

    _charmaps = []

    def register(self, charmap):
        self._charmaps.append(charmap)

    @property
    def charmaps(self):
        return self._charmaps


library = Library()

from fontaine.charmaps import *