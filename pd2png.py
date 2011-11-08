#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pd2pdf.py - converts a UT2025B scope screenshot to PNG
#
# Copyright (c) 2011 András Veres-Szentkirályi
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from __future__ import with_statement, division
from PIL import Image
import sys, os

if len(sys.argv) < 3:
    print >>sys.stderr, 'Usage: {0} <input.bin> <output.png> [colormaps/map.txt]'
    sys.exit(1)

colormap_fn = (os.path.join('colormaps', 'monochrome.txt')
        if len(sys.argv) < 4 else sys.argv[3])
with file(colormap_fn, 'r') as colormap_file:
    COLORMAP = [tuple(int(i) for i in row.split(',')) for row in colormap_file]

x, y = 0, 0
WIDTH, HEIGHT = 320, 240

img = Image.new('RGB', (WIDTH, HEIGHT))

try:
    with file(sys.argv[1], 'rb') as dump:
        for _ in xrange(WIDTH * HEIGHT // 4):
            value = dump.read(2)
            for binval in reversed([ord(ch) for ch in value]):
                for half in (binval >> 4, binval & 0x0f):
                    color = COLORMAP[half]
                    img.putpixel((x, y), color)
                    x += 1
                    if x == WIDTH:
                        x = 0
                        y += 1
finally:
    img.save(sys.argv[2])
