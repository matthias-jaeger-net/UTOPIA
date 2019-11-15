#!usr/bin/env python

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Testing palette
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from colortools import Color
from colortools import randomColor
from colortools import randomColorList
from colortools import fromHls
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from testtools import printTestPage
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from math import cos, sin, floor


def hueScheme(color):
    ret = []
    lig = color.getLightness()
    sat = color.getSaturation()

    angle = 1
    for _ in range(12):
        ret.append(fromHls(angle, lig, sat))
        angle -= (1.0 / 12)
    return ret


def lightnessScheme(color):
    ret = []
    hue = color.getHue()
    sat = color.getSaturation()

    angle = 0.9
    for _ in range(12):
        ret.append(fromHls(hue, angle, sat))
        angle -= (1.0 / 13)
    return ret


def saturationScheme(color):
    ret = []
    lig = color.getLightness()
    hue = color.getHue()

    angle = 1
    for _ in range(12):
        ret.append(fromHls(hue, lig, angle))
        angle -= (1.0 / 12)
    return ret


baseColor = randomColor()
printTestPage(baseColor,
              hueScheme(baseColor),
              lightnessScheme(baseColor),
              saturationScheme(baseColor))
