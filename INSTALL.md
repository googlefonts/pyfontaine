# Install instructions under OSX

Recomended way is using brew project. Following instructions can be changed over time. But may provide enough clues how to get full install of `pyfontain` project:

- Get Homebrew http://brew.sh
- Install XCode and Command Line Tools 
- More information https://github.com/mxcl/homebrew/wiki/Installation

Make sure that brew is fresh and updated:

$ brew doctor

Fix errors

$ brew update
$ brew upgrade

Install needed python libraries:

$ pip-2.7 install --upgrade nose python-dateutil pyparsing

Install numpy:

$ brew tap homebrew/science
$ brew install samueljohn/python/numpy

This part takes even more time to download and compile all `numpy` dependencies. Up to 1 hour... or 2.

Now you can install `matplotlib` dependency (prefereable way is inside of `virtualenv`, but it is out of the scope of this tutorial). 

$ pip install matplotlib

Now your system is ready to install pyfontaine:

$ python setup.py install
