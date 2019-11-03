# usr/bin/env python

from random import randint as rand
from colorsys import rgb_to_hls, hls_to_rgb


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


def randomColorList(numItems):
    colors = []
    for n in range(numItems):
        colors.append(randomColor())
    return colors


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
    lightness = lightness * factor
    return colorFromHLS(hue, lightness, saturation)


def printTestPage(data):
    file = open('test.html', 'w+')
    file.write('<html><body>')
    for color in data:
        file.write('<div style="background-color: #' + color.hex + ';">')
        file.write('red: ' + str(color.red) + '<br>')
        file.write('green: ' + str(color.green) + '<br>')
        file.write('blue: ' + str(color.blue) + '<br>')
        file.write('hex: ' + str(color.hex) + '<br>')
        file.write('hue: ' + str(color.hue) + '<br>')
        file.write('lightness: ' + str(color.lightness) + '<br>')
        file.write('saturation: ' + str(color.saturation) + '<br>')
        file.write('</div>')
    file.write('<body></html>')
    file.close()


base = randomColorList(1)
newBase = []

for item in base:
    newBase.append(item)
    factor = 1
    for n in range(10):
        color = changeHue(item, factor)
        factor -= 0.1
        newBase.append(color)
    factor = 1
    for n in range(10):
        color = changeLightness(item, factor)
        factor -= 0.1
        newBase.append(color)
    factor = 1
    for n in range(10):
        color = changeSaturation(item, factor)
        factor -= 0.1
        newBase.append(color)
printTestPage(newBase)
print("-"*50)


"""
def printColorObj(obj):
    print('rgb: ', [obj.red, obj.green, obj.blue])
    print('hex: ', obj.hex)
    print('hls: ', [obj.hue, obj.lightness, obj.saturation]) """


# test = randomColorList(100)

# for item in test:
#     len = 39
#     print("* "*len)
#     printColorObj(item)

"""
    red = self.red / 255.0
    green = self.blue / 255.0
    blue = self.blue / 255.0
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    darkened = Color(int(r * 255), int(g * 255), int(b * 255))
"""
