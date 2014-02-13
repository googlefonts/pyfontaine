[pyfontaine](http://documentup.com/davelab6/pyfontaine)
===========

pyfontaine analyses fonts for their language and character set support. 

It has a straightforward pythonic character set definition format ([simple example](https://github.com/davelab6/pyfontaine/blob/master/fontaine/charmaps/africaan.py), [medium example](https://github.com/davelab6/pyfontaine/blob/master/fontaine/charmaps/armenian.py), [complex example](https://github.com/davelab6/pyfontaine/blob/master/fontaine/charmaps/polish.py))

To add new definitions, just add files to the [charmaps](https://github.com/davelab6/pyfontaine/tree/master/fontaine/charmaps) directory - they are autodetected!

It also downloads additional definitions from the Extensis, font-config and Unicode websites.


Installation
---------------

Install the latest release easily with the [pip installer](http://www.pip-installer.org):
```sh
pip install fontaine;
```
To install the latest development version:
```sh
git clone https://github.com/davelab6/pyfontaine.git;
cd pyfontaine;
pip install -r requirements.txt;
sudo python setup.py install;
```

Usage
-----

Given a font, it returns a report with some general metadata and th language support analysis. 
```sh
pyfontaine font.ttf;
```

Given a unicode character value, it returns a list of character sets that include that character.
```sh
pyfontaine 0x0061;
```

To output font reports in various formats:
```sh
pyfontaine --xml font.ttf;
pyfontaine --json font.ttf;
pyfontaine --csv font.ttf;
pyfontaine --wiki font.ttf;
```
The `--wiki` format produces a MediaWiki table ([example](https://en.wikipedia.org/wiki/DejaVu_fonts#Unicode_coverage))

To only show character sets from different collections:
```sh
pyfontaine --collections all font.ttf; # default
pyfontaine --collections pyfontaine font.ttf;
pyfontaine --collections uniblocks font.ttf;
pyfontaine --collections extensis font.ttf;
pyfontaine --collections fontconfig font.ttf;
```

To only show specific character sets:
```sh
pyfontaine --set African,'Basic Latin','GWF vietnamese' font.ttf;
```

To print a list of all the missing unicode values from each set:
```sh
pyfontaine --missing font.ttf;
```

To output visualisations of the coverage using [Hilbert curves](http://en.wikipedia.org/wiki/Hilbert_curve) (thanks for the idea, [Øyvind 'pippin' Kolås](http://github.com/hodefoting)!):
```sh
pyfontaine --coverage font.ttf;
ls -l coverage_pngs/;
```
(The PNG files are stored in a new directory, `coverage_pngs`, under the current directory.)

### Python Module

It has a python module. Here is an [example script](https://github.com/xen/fontbakery/blob/master/scripts/famchar.py) from the Font Bakery project.

Contributing
----------------

Your contributions under [the GPLv3](LICENSE.txt) are welcome!

pyfontaine is a python reimplementation of [Fontaine](http://fontaine.sf.net) by Ed Trager, and has been made by by [Vitaly Volkhov](http://github.com/hash3g), [Dave Crossland](http://github.com/davelab6) and [Mikhail Kashkin](http://github.com/xen). 

Thanks
--------

We would like to thank some upstream projects that make pyfontaine even more useful:
* [Thomas Phinney](http://www.thomasphinney.com/) for the [WebINK Character Sets](http://blog.webink.com/custom-font-subsetting-for-faster-websites/)
* [Behdad Esfabod](http://behdad.org) for the [font-config languages definitions](http://cgit.freedesktop.org/fontconfig/tree/fc-lang)
* Unicode Consortium for the [Unicode Blocks](http://www.unicode.org/Public/UNIDATA/Blocks.txt)

Dependencies
------------

* [fonttools](https://github.com/behdad/fonttools) (common) _or_ [freetype-py](http://code.google.com/p/freetype-py) (fast)
* [lxml](http://pypi.python.org/pypi/lxml)
* [simpleHilbertCurve](https://github.com/dentearl/simpleHilbertCurve)
* [matplotlib](https://pypi.python.org/pypi/matplotlib)

Related Projects
------------

* [fontaine](http://fontaine.sf.net)
* [fontbakery](https://github.com/xen/fontbakery)
* [libunicodenames](https://bitbucket.org/sortsmill/libunicodenames)
