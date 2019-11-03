# Color Tools
#
# Author: Matthias Jaeger
# Licence MIT
# Dependencies:
from colorsys import rgb_to_hls, hls_to_rgb
from random import randint as rand

# A Color(r, g, b) is created in the rgb space with regular values
# ranging from 0 to 255 for each red, green and blue, like in Adobe...
# The color calculates it's own hue, lightness and saturation vector
# based on the given rgb values. Once initialized a log()
# method is available for printing the values in the console.


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

    def fromHls(self, hue, lightness, saturation):
        r, g, b = hls_to_rgb(hue, lightness, saturation)
        return Color(int(r * 255), int(g * 255), int(b * 255))

    def log(self):
        # Prints the data of this color to the console
        print('rgb: ', [self.red, self.green, self.blue])
        print('hex: ', self.hex)
        print('hls: ', [self.hue, self.lightness, self.saturation])

    def analyze(self):
        # Procedural test of the colors values (Work in progress)
        message = 'Hello, my name is #' + str(self.hex) + ' and I am a '
        # Saturation test
        if (self.saturation > 0.0 and self.saturation < 0.3):
            message += 'desaturated '
        if (self.saturation > 0.3 and self.saturation < 0.6):
            message += 'saturated '
        if (self.saturation > 0.6 and self.saturation < 0.9):
            message += 'very saturated '
        # Lightness test
        if (self.lightness < 0.5):
            message += 'dark '
        if (self.lightness > 0.5):
            message += 'bright '
        # Tonal test
        if (self.red > self.green and self.red > self.blue):
            message += 'red color.'
        if (self.green > self.red and self.green > self.blue):
            message += 'green color.'
        if (self.blue > self.green and self.blue > self.red):
            message += 'blue color.'
        # Later return message print for now
        print(message)

    def similar_colors(self):
        ret = []
        for num in range(10):
            factor = num * 0.1
            newHue = abs(self.hue - factor)
            ret.append(self.fromHls(newHue, self.lightness, self.saturation))
        return ret


# Tools for creating Color instances. Those are outside of the Color class
# and used by the template engine I want to create later on...


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
    # Returns a list with hex color strings
    ret = []
    for index in range(numItems):
        ret.append(randomColor().hex)
    return ret
