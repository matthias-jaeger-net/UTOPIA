# Color Tools
#
# Author: Matthias Jaeger
# Licence MIT
#

from colorsys import rgb_to_hls, hls_to_rgb
from random import randint as rand

# A Color(r, g, b) is assigned with rgb values ranging from 0 to 255
# The Color calculates it's own hue, lightness and saturation vector
# based on the given rgb values.


class Color:

    def __init__(self, r, g, b):
        # Basic values of a Color
        self.red = r
        self.green = g
        self.blue = b
        self.hex = self.getHex()
        self.hue = self.getHue()
        self.lightness = self.getLightness()
        self.saturation = self.getSaturation()

    def getHex(self):
        # Using a format string to create a css like hex-color
        return '{:02x}{:02x}{:02x}'.format(self.red, self.green, self.blue)

    def getHue(self):
        # Returns the current hue in a range from 0 to 1
        hue, lightness, saturation = rgb_to_hls(
            self.red / 255.0, self.green / 255.0, self.blue / 255.0)
        return hue

    def getLightness(self):
        # Returns the current lightness in a range from 0 to 1
        hue, lightness, saturation = rgb_to_hls(
            self.red / 255.0, self.green / 255.0, self.blue / 255.0)
        return lightness

    def getSaturation(self):
        # Returns the current saturation in a range from 0 to 1
        hue, lightness, saturation = rgb_to_hls(
            self.red / 255.0, self.green / 255.0, self.blue / 255.0)
        return saturation

    def log(self):
        # Prints the data of this color to the console
        log = 'rgb: ' + str([self.red, self.green, self.blue]) + '\n'
        log += 'hex: ' + str(self.hex) + '\n'
        log += 'hls: ' + \
            str([self.hue, self.lightness, self.saturation]) + '\n'
        return log

    def analyze(self):

        # Procedural test of the colors values (Work in progress)
        message = 'Hello, my name is #' + str(self.hex) + ' and I am a '

        # Saturation test
        if (self.saturation >= 0.0 and self.saturation <= 0.3):
            message += 'desaturated '
        if (self.saturation >= 0.3 and self.saturation <= 0.6):
            message += 'saturated '
        if (self.saturation >= 0.6 and self.saturation <= 1.0):
            message += 'very saturated '

        # Lightness test
        if (self.lightness >= 0.0 and self.lightness <= 0.3):
            message += 'dark '
        if (self.lightness >= 0.3 and self.lightness <= 0.6):
            message += 'light '
        if (self.lightness >= 0.6 and self.lightness <= 1.0):
            message += 'brighter '

        # Tonal test
        if (self.hue >= 0.0 and self.hue <= 0.3):
            message += 'red color '
        if (self.hue >= 0.3 and self.hue <= 0.6):
            message += 'green color '
        if (self.hue >= 0.6 and self.hue <= 1.0):
            message += 'blue color'

        return message


# Tools for creating Color instances.
# Those are outside of the Color class and used by
# the template engine I want to create later on...

def fromHls(hue, lightness, saturation):
    r, g, b = hls_to_rgb(hue, lightness, saturation)
    return Color(int(r * 255), int(g * 255), int(b * 255))


def colorFromUrl(url):
    # Excpecting a valid url string like 'FFFFFF'
    red = int(url[:2], 16)
    green = int(url[2:4], 16)
    blue = int(url[4:6], 16)
    return Color(red, green, blue)


def lightnessHexColorList(colorObj):
    ret = []
    for num in range(10):
        factor = num * 0.1
        lightness = abs(colorObj.lightness - factor)
        newColor = fromHls(colorObj.hue, lightness, colorObj.saturation)
        ret.append(newColor.hex)
    return ret


def hueHexColorList(colorObj):
    ret = []
    for num in range(10):
        factor = num * 0.01
        newHue = abs(colorObj.hue - factor)
        newColor = fromHls(newHue, colorObj.lightness, colorObj.saturation)
        ret.append(newColor.hex)
    return ret


def saturationHexColorList(colorObj):
    ret = []
    for num in range(10):
        factor = num * 0.1
        newSaturation = abs(colorObj.saturation - factor)
        newColor = fromHls(colorObj.hue, colorObj.lightness, newSaturation)
        ret.append(newColor.hex)
    return ret


def randomColor():
    # Returns a new Color object with random values
    return Color(rand(0, 255), rand(0, 255), rand(0, 255))


def randomColorList(numItems):
    # Returns a list of random color objects
    ret = []
    for index in range(numItems):
        ret.append(randomColor())
    return ret


def randomHexColorList(numItems):
    # Returns a list of random hex color strings
    ret = []
    for index in range(numItems):
        ret.append(randomColor().hex)
    return ret
