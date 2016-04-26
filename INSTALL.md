# Install instructions

## OS X

Recomended way is using brew and pip.

- Get Homebrew http://brew.sh
- Install XCode and Command Line Tools 
- More information https://github.com/mxcl/homebrew/wiki/Installation

Make sure that brew is fresh and updated:
```
$ brew doctor
```
Fix errors
```
$ brew update
$ brew upgrade
$ brew install python icu4c
```
Install needed python libraries:
```
$ pip-2.7 install --upgrade nose python-dateutil pyparsing
```
Install numpy:
```
$ brew tap homebrew/science
$ brew install samueljohn/python/numpy
```
This part takes even more time to download and compile all `numpy` dependencies. It can take a while.

Now you can install `matplotlib` dependency (prefereable way is inside of `virtualenv`, but it is out of the scope of this tutorial.)
```
$ ln -s /usr/local/opt/freetype/include/freetype2 /usr/local/include/freetype
$ pip install matplotlib
```
Now your system is ready to install pyfontaine:
```
$ pip install fontaine
```
At this stage you can also download the github source and run
```
$ python setup.py install
```

## From Source

```sh
mkdir ~/src;
cd ~/src;
git clone git://github.com/davelab6/pyfontaine'
cd pyfontaine'
git submodule init;
git submodule update;
# then setup
sudo python setup.py install;
```
