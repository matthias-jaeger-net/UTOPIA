#!usr/bin/env python
from flask import Flask, render_template
from random import randint as rand
from colorsys import rgb_to_hls, hls_to_rgb


class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        self.hex = '{:02x}{:02x}{:02x}'.format(r, g, b)
        h, l, s = rgb_to_hls(r, g, b)
        self.hue = h
        self.lightness = l
        self.saturation = s


def darken(color, factor):
    # Convert to 0-1 coordinates
    red = color.red / 255.0
    green = color.blue / 255.0
    blue = color.blue / 255.0
    # Convert to hue lightness saturation model
    h, l, s = rgb_to_hls(red, green, blue)
    l = max(min(l * factor, 1.0), 0.0)
    # Convert back to rgb
    r, g, b = hls_to_rgb(h, l, s)
    return Color(int(r * 255), int(g * 255), int(b * 255))


def randomColor():
    return Color(rand(0, 255), rand(0, 255), rand(0, 255))


def randomHexColorList(size):
    ret = []
    for _ in range(size):
        ret.append(randomColor().hex)
    return ret


def urlToColor(url):
    red = int(url[:2], 16)
    green = int(url[2:4], 16)
    blue = int(url[4:6], 16)
    return Color(red, green, blue)


def lightnessTable(color):
    base = urlToColor(color)
    ret = []
    bright = 0
    while (bright < 255.0):
        res = darken(base, bright)
        ret.append(res.hex)
        bright = bright + 1
    return ret


app = Flask(__name__, static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def front_page():
    return render_template('index.html',
                           result=randomHexColorList(100))


@app.route('/<url>')
def color_page(url):
    base = urlToColor(url)

    return render_template('color.html',
                           color=url,
                           red=base.red,
                           green=base.green,
                           blue=base.blue,
                           hexadecimal=base.hex,
                           hue=base.hue,
                           lightness=base.lightness,
                           saturation=base.saturation,
                           lightnesstable=lightnessTable(base.hex),
                           result=randomHexColorList(100))


if __name__ == '__main__':
    app.run(debug=True)
