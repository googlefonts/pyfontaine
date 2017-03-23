"""Helper APIs for interaction with Google Fonts.

Provides APIs to interact with font subsets, codepoints for font or subset.

To run the tests:
$ cd fonts/tools
fonts/tools$ python util/google_fonts.py
# or do:
$ python path/to/fonts/tools/utilgoogle_fonts.py --nam_dir path/to/fonts/tools/encodings/

"""
from __future__ import print_function, unicode_literals

import os
import re
import sys
import codecs

if __name__ == '__main__':
  # some of the imports here wouldn't work otherwise
  sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Matches 4 or 5 hexadecimal digits that are uppercase at the beginning of the
# test string. The match is stored in group 0, e.g:
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234X').groups()[0]
# '1234'
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234A').groups()[0]
# '1234A'
_NAMELIST_CODEPOINT_REGEX = re.compile('^([A-F0-9]{4,5})')


class Error(Exception):
  """Base for Google Fonts errors."""


def warn(msg):
  print(msg, file=sys.stderr)


def _parseNamelistHeader(lines):
  includes = set()
  for line in lines:
    if not line.startswith('#$'):
      # not functional line, regular comment
      continue
    keyword, args = line.rstrip()[2:].lstrip().split(' ', 1)
    if keyword == 'include':
      includes.add(args)
  return {
      'lines': list(lines)
    , 'includes': includes
  }


def get_codepoint_from_line(line):
  assert line.startswith('0x')
  match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
  if match is None:
    match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7].upper())
    if match is not None:
      # Codepoints must be uppercase, it's documented
      warn('Found a codepoint with lowercase unicode hex value: 0x{0}'.format(match.groups()[0]))
    return None
  return int(match.groups()[0], 16)

def _parseNamelist(lines):
  cps = set()
  noncodes = set()
  headerLines = []
  readingHeader = True
  for line in lines:
    if readingHeader:
      if not line.startswith('#'):
        # first none comment line ends the header
        readingHeader = False
      else:
        headerLines.append(line)
        continue
    # reading the body, i.e. codepoints

    if line.startswith('0x'):
      codepoint = get_codepoint_from_line(line)
      if codepoint is None:
        # ignore all lines that we don't understand
        continue
      cps.add(codepoint)
      # description
      # line[(2+len(codepoint)),]
    elif line.startswith('      '):
      noncode = line.strip().rsplit(' ')[-1]
      if len(noncode):
        noncodes.add(noncode)

  header = _parseNamelistHeader(headerLines)
  return cps, header, noncodes

def parseNamelist(filename):
  """Parse filename as Namelist and return a tuple of
    (Codepoints set, header data dict)
  """
  with codecs.open(filename, encoding='utf-8') as namFile:
    return _parseNamelist(namFile)

def _loadNamelistIncludes(item, unique_glyphs, cache):
  """Load the includes of an encoding Namelist files.

  This is an implementation detail of readNamelist.
  """
  includes = item["includes"] = []
  charset = item["charset"] = set() | item["ownCharset"]

  noCharcode = item["noCharcode"] = set() | item["ownNoCharcode"]

  dirname =  os.path.dirname(item["fileName"])
  for include in item["header"]["includes"]:
    includeFile = os.path.join(dirname, include)
    try:
      includedItem = readNamelist(includeFile, unique_glyphs, cache)
    except NamelistRecursionError:
      continue
    if includedItem in includes:
      continue
    includes.append(includedItem)
    charset |= includedItem["charset"]
    noCharcode |= includedItem["ownNoCharcode"]
  return item

def __readNamelist(cache, filename, unique_glyphs):
  """Return a dict with the data of an encoding Namelist file.

  This is an implementation detail of readNamelist.
  """
  if filename in cache:
    item = cache[filename]
  else:
    cps, header, noncodes = parseNamelist(filename)
    item = {
      "fileName": filename
    , "ownCharset": cps
    , "header": header
    , "ownNoCharcode": noncodes
    , "includes": None # placeholder
    , "charset": None # placeholder
    , "noCharcode": None
    }
    cache[filename] = item

  if unique_glyphs or item["charset"] is not None:
    return item

  # full-charset/includes are requested and not cached yet
  _loadNamelistIncludes(item, unique_glyphs, cache)
  return item

class NamelistRecursionError(Error):
  """Exception to control infinite recursion in Namelist includes"""
  pass


def _readNamelist(currentlyIncluding, cache, namFilename, unique_glyphs):
  """ Detect infinite recursion and prevent it.

  This is an implementation detail of readNamelist.

  Raises NamelistRecursionError if namFilename is in the process of being included
  """
  # normalize
  filename = os.path.abspath(os.path.normcase(namFilename))
  if filename in currentlyIncluding:
    raise NamelistRecursionError(filename)
  currentlyIncluding.add(filename)
  try:
    result = __readNamelist(cache, filename, unique_glyphs)
  finally:
    currentlyIncluding.remove(filename)
  return result

def readNamelist(namFilename, unique_glyphs=False, cache=None):
  """
  Args:
    namFilename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
    cache: Optional, a dict used to cache loaded Namelist files

  Returns:
  A dict with following keys:
  "fileName": (string) absolut path to namFilename
  "ownCharset": (set) the set of codepoints defined by the file itself
  "header": (dict) the result of _parseNamelistHeader
  "includes":
      (set) if unique_glyphs=False, the resulting dicts of readNamelist
            for each of the include files
      (None) if unique_glyphs=True
  "charset":
      (set) if unique_glyphs=False, the union of "ownCharset" and all
            "charset" items of each included file
      (None) if unique_glyphs=True

  If you are using  unique_glyphs=True and an external cache, don't expect
  the keys "includes" and "charset" to have a specific value.
  Depending on the state of cache, if unique_glyphs=True the returned
  dict may have None values for its "includes" and "charset" keys.
  """
  currentlyIncluding = set()
  if not cache:
    cache = {}
  return _readNamelist(currentlyIncluding, cache, namFilename, unique_glyphs)

def codepointsInNamelist(namFilename, unique_glyphs=False, cache=None):
  """Returns the set of codepoints contained in a given Namelist file.

  This is a replacement CodepointsInSubset and implements the "#$ include"
  header format.

  Args:
    namFilename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
  Returns:
    A set containing the glyphs in the subset.
  """
  key = 'charset' if not unique_glyphs else 'ownCharset'

  internals_dir = os.path.dirname(os.path.abspath(__file__))
  target = os.path.join(internals_dir, namFilename)
  result = readNamelist(target, unique_glyphs, cache)
  return result[key]
