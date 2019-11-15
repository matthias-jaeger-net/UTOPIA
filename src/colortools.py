# Color Tools
#
# Author: Matthias Jaeger
# Licence MIT
#
from math import floor
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
    """
    Procedural test of the colors values (Work in progress)

    """

    def analyze(self):
        # String to be returned
        welcome = ['Hi there, I\'m a', 'Hello, I assume I\'m a', 'Hey, I\'m a']
        message = welcome[int(self.saturation * len(welcome))] + ' '
        # Describe saturation ...
        saturation = ['pale', 'desaturated', 'saturated']
        message += saturation[int(self.saturation * len(saturation))] + ' '

        # Describe lightness ...
        lightness = ['dark', 'light', 'bright']
        message += lightness[int(self.lightness*len(lightness))] + ' '

        # Describe hue, seems to work now
        hue = ['red', 'orange', 'yellow', 'lime', 'green',
               'turquoise', 'cyan', 'azure', 'blue',
               'purple', 'magenta', 'rose']
        message += hue[int(self.hue * len(hue))] + ' color.'

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


def randomColor():
    # Returns a new Color object with random values
    return Color(rand(0, 255), rand(0, 255), rand(0, 255))


# BUGGY below ...

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


def lightnessHexColorList(colorObj):
    ret = []
    hue = colorObj.getHue()
    sat = colorObj.getSaturation()

    angle = 0.9
    for _ in range(12):
        ret.append(fromHls(hue, angle, sat).hex)
        angle -= (1.0 / 13)
    return ret


def hueHexColorList(colorObj):
    ret = []
    lig = colorObj.getLightness()
    sat = colorObj.getSaturation()

    angle = colorObj.getHue()
    for _ in range(12):
        ret.append(fromHls(angle, lig, sat).hex)
        angle = abs(angle - (1.0 / 12))
    return ret


def saturationHexColorList(colorObj):
    ret = []
    lig = colorObj.getLightness()
    hue = colorObj.getHue()

    angle = 1
    for _ in range(12):
        ret.append(fromHls(hue, lig, angle).hex)
        angle -= (1.0 / 12)
    return ret
