#!/usr/bin/env python2.7
"""
simpleHilbertCurve
dent earl, dent.earl (a) gmail dot com

**simpleHilbertCurve** is a Python script that uses matplotlib to create 
[Hilbert curve](http://en.wikipedia.org/wiki/Hilbert_curve) plots. Hilbert 
curves are space filling fractals that can be used to map a one dimensional 
set into two dimensions. Hilbert curves mostly maintain locality meaning 
that clusters in the 2D representation are most likely close together in 
the 1D scale too. Hilbert curves can be a useful way of visualy summarizing 
and comparing large time series or large linear maps (like genomic data).

"""
##############################
# Copyright (C) 2009-2011 by 
# Dent Earl (dearl@soe.ucsc.edu, dent.earl@gmail.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##############################
import matplotlib
matplotlib.use('Agg')
import matplotlib.backends.backend_pdf as pltBack
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy
from optparse import OptionParser
import os
import sys

colorMaps = [m for m in plt.cm.datad if not m.endswith("_r")]

def initOptions(parser):
    parser.add_option('-n', '--level', dest='level', default=6,
                      type='int',
                      help=('determines the length of one side of the square by '
                            '2^LEVEL. There is a restriction that LEVEL <= 8. Using large level '
                            'values can take a long time or create enormous / resource '
                            'intensive plots. default=%default'))
    parser.add_option('--override', dest='override', default=False,
                      action='store_true',
                      help=('overrides the restrition for --level > 8. Using large level '
                            'values can take a long time or create enormous / resource '
                            'intensive plots. default=%default'))
    parser.add_option('--normalize', dest='normalize', default=False,
                      action='store_true',
                      help=('subtracts off the mean and divides by the std dev. '
                            'default=%default'))
    parser.add_option('--cmap', dest='cmap', default='binary',
                      help=('The colormap to be used. default=%default Possible values:'
                            + '%s' % ', '.join(colorMaps)))
    parser.add_option('--demo', dest='demo', default=False,
                      action='store_true',
                      help=('creates a demonstration image based on the --level parameter. '
                            'default=%default'))
    parser.add_option('--matshow', dest='matshow', default=False,
                      action='store_true',
                      help=('switches the drawing call from pcolor() to matshow(). matshow() '
                            'produces rasters whereas pcolor() can produce vectors. For pdf '
                            'or eps output pcolor() looks much crisper but at very large --level '
                            'values the image can take a long time to draw on screen. '
                            'default=%default'))
    parser.add_option('--dpi', dest='dpi', default=300,
                      type='int',
                      help='dots per inch of raster outputs, i.e. if --outFormat is all '
                      'or png. default=%default')
    parser.add_option('--outFormat', dest='outFormat', default='pdf',
                      type='string',
                      help='output format [pdf|png|eps|all]. default=%default')
    parser.add_option('--out', dest='out', default='myPlot',
                      type='string',
                      help=('path/filename where figure will be created. No '
                            'extension needed. default=%default'))

def checkOptions(options, args, parser):
    options.max = 0
    if options.level < 1:
        parser.error('--level must by greater than 0')
    if options.level > 8 and not options.override:
        parser.error('--level > 8 and --override not engaged. (2^%d)^2 is a big number.' 
                     % options.level)
    if options.cmap not in colorMaps:
        parser.error('--cmap %s not a valid option. Pick from %s' 
                     % (options.cmap, ', '.join(colorMaps)))
    if len(args) > 0:
        for a in args:
            if not os.path.exists(a):
                parser.error('File %s does not exist.\n' % a)
    if options.dpi < 72:
        parser.error('--dpi %d less than screen res, 72. Must be >= 72.' % options.dpi)
    if options.outFormat not in ('pdf', 'png', 'eps', 'all'):
        parser.error('Unrecognized output format: %s. Choose one from: pdf png eps all.' 
                     % options.outFormat)
    if (options.out.endswith('.png') or options.out.endswith('.pdf') or 
        options.out.endswith('.eps')):
        options.out = options.out[:-4]

def initImage(width, height, options):
    """
    initImage takes a width and height and returns
    both a fig and pdf object. options must contain outFormat,
    and dpi
    """
    pdf = None
    if options.outFormat == 'pdf' or options.outFormat == 'all':
        pdf = pltBack.PdfPages(options.out + '.pdf')
    fig = plt.figure(figsize=(width, height), dpi=options.dpi, facecolor='w')
    return (fig, pdf)

def establishAxis(fig, options):
    """ create one axes per chromosome
    """
    options.axLeft = 0.05
    options.axWidth = 0.9
    options.axBottom = 0.05
    options.axHeight = 0.9
    ax = fig.add_axes([options.axLeft, options.axBottom,
                       options.axWidth, options.axHeight])
    return ax

def writeImage(fig, pdf, options):
    """
    writeImage assumes options contains outFormat and dpi.
    """
    if options.outFormat == 'pdf':
        fig.savefig(pdf, format = 'pdf')
        pdf.close()
    elif options.outFormat == 'png':
        fig.savefig(options.out + '.png', format='png', dpi=options.dpi)
    elif options.outFormat == 'all':
        fig.savefig(pdf, format='pdf')
        pdf.close()
        fig.savefig(options.out + '.png', format='png', dpi=options.dpi)
        fig.savefig(options.out + '.eps', format='eps')
    elif options.outFormat == 'eps':
        fig.savefig(options.out + '.eps', format='eps')

def processFile(filename, options):
    """
    read in the input and return the corresponding matrix 
    input is two column, whitespace separated data. col1 is
    a position along the scale and col2 is a value. 
    """
    n = 1 << options.level
    m = numpy.zeros((n, n))
    x = []
    y = []
    f = open(filename, 'r')
    for lineno, line in enumerate(f, 1):
        if line.startswith('#'):
            continue
        line = line.strip()
        vals = line.split()
        if len(vals) < 2:
            continue
        if options.max < float(vals[0]):
            options.max = float(vals[0])
        x.append(float(vals[0]))
        y.append(float(vals[1]))
    x = numpy.array(x)
    y = numpy.array(y)
    if options.normalize:
        y -= numpy.average(y)
        y /= numpy.std(y)
    for i in xrange(0, len(x)):
        c, r = d2xy(n, int(round((n**2 - 1) * x[i] / options.max)))
        m[r][c] += y[i]
    return m

def drawData(ax, data, options):
    if options.matshow:
        plt.matshow(data, fignum=False, origin='upper', cmap=plt.get_cmap(options.cmap))
    else:
        data = data[ ::-1,:] # reverse row order
        plt.pcolor(data, cmap=plt.get_cmap(options.cmap))
    ax.set_xticks([])
    ax.set_yticks([])
    
########################################
# These functions refactored from those available at 
# wikipedia for Hilbert curves http://en.wikipedia.org/wiki/Hilbert_curve
def d2xy(n, d):
    """
    take a d value in [0, n**2 - 1] and map it to
    an x, y value (e.g. c, r).
    """
    assert(d <= n**2 - 1)
    t = d
    x = y = 0
    s = 1
    while (s < n):
        rx = 1 & (t / 2)
        ry = 1 & (t ^ rx)
        x, y = rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t /= 4
        s *= 2
    return x, y
def rot(n, x, y, rx, ry):
    """
    rotate/flip a quadrant appropriately
    """
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y
        return y, x
    return x, y
#
########################################

def genericCurve(options):
    x, y = generateVectors(options.level)
    fig, pdf = initImage(8, 8, options)
    ax = establishAxis(fig, options)
    ax.set_aspect('equal')
    plt.plot(x, y)
    ax.set_xlim([-0.5, (1 << options.level) - .5])
    ax.set_ylim([-(1 << options.level) + .5, 0.5])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.box(on=False)
    writeImage(fig, pdf, options)

def hilbert(args, options):
    if len(args) > 0:
        data = processFile(args[0], options)
    else:
        data = generateDemo(options)
    fig, pdf = initImage(8, 8, options)
    ax = establishAxis(fig, options)
    ax.set_aspect('equal')
    plt.box(on=False)
    drawData(ax, data, options)
    writeImage(fig, pdf, options)

def generateVectors(level):
    """
    Given a level, this will generate x and y vectors that
    can be used to plot the hilbert curve path for that level.
    Useful for explaining HCs.
    """
    n = (1 << level)
    x = numpy.zeros(n**2, dtype=numpy.int16)
    y = numpy.zeros(n**2, dtype=numpy.int16)
    for i in xrange(0, n**2):
        x[i], y[i] = d2xy(n, i)
    return x, -y

def generateDemo(options):
    n = 1 << options.level
    m = numpy.zeros((n, n))
    for i in xrange(0, n**2):
        x, y = d2xy(n, i)
        m[y][x] = i
    return m

def main():
    usage = ('usage: %prog --max=MAX --level=LEVEL [options] inputFile\n\n'
             '%prog takes a two column input, col1 is a position long a\n'
             'scale with values in [0, MAX] and col2 is a value in (-inf, inf).\n'
             'The LEVEL determines the length of the side of the square by\n'
             '2**LEVEL. By default levels greater than 10 are disallowed, though\n'
             'this restriction may be overrided.')
    parser = OptionParser(usage=usage)
    initOptions(parser)
    options, args = parser.parse_args()
    checkOptions(options, args, parser)
    
    if len(args) == 0 and not options.demo:
        genericCurve(options)
    else:
        hilbert(args, options)

if __name__ == '__main__':
    main()
