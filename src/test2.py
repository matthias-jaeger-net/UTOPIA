#!usr/bin/env python
import numpy
from random import randint as rand
from colorsys import rgb_to_hls, hls_to_rgb

# COLOR CODE


class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        self.hex = '{:02x}{:02x}{:02x}'.format(r, g, b)
        self.hue, self.lightness, self.saturation = rgb_to_hls(
            r/255, g/255, b/255)


def randomColor():
    return Color(rand(0, 255), rand(0, 255), rand(0, 255))


def colorFromUrlParam(url):
    red = int(url[:2], 16)
    green = int(url[2:4], 16)
    blue = int(url[4:6], 16)
    return Color(red, green, blue)


def randomColorList(numItems):
    colors = []
    for n in range(numItems):
        colors.append(randomColor())
    return colors


def randomHexColorList(numItems):
    ret = []
    for index in range(numItems):
        ret.append(randomColor().hex)
    return ret


def colorToHLS(color):
    return rgb_to_hls(color.red / 255, color.green / 255, color.blue / 255)


def colorFromHLS(hue, lightness, saturation):
    r, g, b = hls_to_rgb(hue, lightness, saturation)
    return Color(int(r * 255), int(g * 255), int(b * 255))


def changeHue(color, factor):
    hue, lightness, saturation = colorToHLS(color)
    hue = hue * factor
    return colorFromHLS(hue, lightness, saturation)


def changeLightness(color, factor):
    hue, lightness, saturation = colorToHLS(color)
    lightness = lightness * factor
    return colorFromHLS(hue, lightness, saturation)


def changeSaturation(color, factor):
    hue, lightness, saturation = colorToHLS(color)
    saturation = saturation * factor
    return colorFromHLS(hue, lightness, saturation)


# TEMPLATE CODE
def printColorObj(obj):
    print('rgb: ', [obj.red, obj.green, obj.blue])
    print('hex: ', obj.hex)
    print('hls: ', [obj.hue, obj.lightness, obj.saturation])


def hueTable(color, numItems):
    ret = []
    for factor in numpy.arange(-0.5, 0.5, 0.1):
        color = changeHue(color, factor)
        ret.append(color)
    return ret


test = Color(200, 100, 20)
table = hueTable(test, 10)

for t in table:
    printColorObj(t)
