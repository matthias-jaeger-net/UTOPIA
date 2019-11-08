#!usr/bin/env python
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Get a color palette from a given single color
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from colortools import Color
from colortools import randomColor
from colortools import randomColorList
from colortools import fromHls
from testtools import printTestPage

# Make a blueish base color
baseColor = fromHls(1, 0.5, 0.5)

# Set up colors from the base


def palette(color):
    ret = []
    hue = color.getHue()
    inc = 1 / 12
    for n in range(1, 12):
        h = hue + inc * n
        ret.append(fromHls(h, 1, 1))

    return ret


# Render a html test page
printTestPage(baseColor, palette(baseColor))

# print(randomHexColorList(100))
for color in palette(baseColor):
    print(color.log())

print(baseColor.log())
