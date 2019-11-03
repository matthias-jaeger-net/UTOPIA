#!usr/bin/env python
from flask import Flask, render_template
from random import randint as rand
from colorsys import rgb_to_hls, hls_to_rgb
import numpy


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


def hueTable(color, numItems):
    ret = []
    factor = 1
    for n in range(10):
        color = changeHue(color, factor)
        ret.append(color.hex)
        factor += 0.01
    return ret


def lightnessTable(color, numItems):
    ret = []
    factor = 1.0
    for n in range(numItems):
        color = changeLightness(color, factor)
        factor -= (1.0 / numItems)
        ret.append(color.hex)
    return ret


def saturationTable(color, numItems):
    ret = []
    factor = 1.0
    for n in range(numItems):
        color = changeSaturation(color, factor)
        factor -= (1.0 / numItems)
        ret.append(color.hex)
    return ret


# SERVER CODE


app = Flask(__name__, static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def front_page():
    return render_template('index.html',
                           result=randomHexColorList(100))


@app.route('/<url>')
def color_page(url):
    base = colorFromUrlParam(url)
    return render_template('color.html',
                           color=url,
                           red=base.red,
                           green=base.green,
                           blue=base.blue,
                           hexadecimal=base.hex,
                           hue=base.hue,
                           lightness=base.lightness,
                           saturation=base.saturation,
                           huetable=hueTable(base, 10),
                           lightnesstable=lightnessTable(base, 10),
                           saturationtable=saturationTable(base, 10),
                           result=randomHexColorList(30))


if __name__ == '__main__':
    app.run(debug=True)
