#!usr/bin/env python
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Get a color palette from a given single color
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from colortools import Color
from colortools import randomColor
from colortools import fromHls
from testtools import printTestPage

# Make a blueish base color
baseColor = randomColor()

# Set up colors from the base


def palette(color):
    ret = []
    hue = color.getHue()
    lightness = color.getLightness()
    saturation = color.getSaturation()
    for n in range(1, 10):
        hue = (hue * n) % 1
        ret.append(fromHls(hue, lightness * 0.5, saturation))
    return ret


# Render a html test page
printTestPage(baseColor, palette(baseColor))

for color in palette(baseColor):
    print("#"*20)
    print(color.analyze())
    print(color.log())
