#!usr/bin/env python

from flask import Flask, render_template

from colortools import Color
from colortools import randomColor
from colortools import randomHexColorList
from colortools import randomHexColorList
from colortools import colorFromUrl


app = Flask(__name__)


@app.route('/')
def front_page():
    return render_template('index.html',
                           result=randomHexColorList(100))


@app.route('/<url>')
def color_page(url):
    base = colorFromUrl(url)
    return render_template('color.html',
                           color=url,
                           red=base.red,
                           green=base.green,
                           blue=base.blue,
                           hexadecimal=base.hex,
                           hue=base.hue,
                           lightness=base.lightness,
                           saturation=base.saturation,
                           huetable=randomHexColorList(10),
                           lightnesstable=randomHexColorList(10),
                           saturationtable=randomHexColorList(10),
                           result=randomHexColorList(30))


if __name__ == '__main__':
    app.run(debug=True)
