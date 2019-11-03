# usr/bin/env python

from random import randint as rand
from colorsys import rgb_to_hls, hls_to_rgb


class Color:
    def __init__(self, r, g, b):
        # Default values of a color
        self.red = r
        self.green = g
        self.blue = b
        self.hex = '{:02x}{:02x}{:02x}'.format(r, g, b)

    def darken(self, factor):
        # Convert to 0-1 coordinates
        red = self.red / 255.0
        green = self.blue / 255.0
        blue = self.blue / 255.0
        # Convert to hue lightness saturation model
        h, l, s = rgb_to_hls(red, green, blue)
        l = max(min(l * factor, 1.0), 0.0)
        # Convert back to rgb
        r, g, b = hls_to_rgb(h, l, s)
        darkened = Color(int(r * 255), int(g * 255), int(b * 255))
        return darkened.hex


base = Color(20, 200, 10)
shade = Color(0, 0, 0)

base.darken(shade)
print(base.hex)
print(shade.hex)


def adjust_color_lightness(r, g, b, factor):

    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)


def lighten_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 + factor)


def darken_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 - factor)
# def colorListFromSingleColor(url):
#     red = int(url[:2], 16)
#     green = int(url[2:4], 16)
#     blue = int(url[4:6], 16)
#     base = Color(red, green, blue)
#     list = [base.hex]
#     for tone in range(255):
#         grey = Color(tone, tone, tone)
#         base = Color(red, green, blue)
#         res = base.multiply(grey)
#         if (tone % 20 == 0):
#             list.append(res.hex)
#     return list


# colorListFromSingleColor(c.hex)


"""

# Create a random rgb value and store it as a Color object
color = Color(rand(0, 255), rand(0, 255), rand(0, 255))
print(color.hex)

newColor = color.unhex(color.hex)
# import colorsys
# colorsys.rgb_to_hls(r, g, b)


def map(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan) """
