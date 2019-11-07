#!usr/bin/env python

# Flask framework to handle the server
from flask import Flask, render_template

# Custom Functionality to handle colors
from src.colortools import Color
from src.colortools import randomColor
from src.colortools import colorFromUrl
from src.colortools import randomHexColorList
from src.colortools import hueHexColorList
from src.colortools import lightnessHexColorList
from src.colortools import saturationHexColorList

# Default folders 'static' & 'templates' exist
app = Flask(__name__)

# Index page route
@app.route('/')
def index():
    return render_template('index.html',
                           result=randomHexColorList(100))

# All other routes, no error checking!
@app.route('/<url>')
def single(url):
    base = colorFromUrl(url)
    return render_template('color.html',
                           color=base,
                           lightness=lightnessHexColorList(base),
                           hue=hueHexColorList(base),
                           saturation=saturationHexColorList(base),
                           footer=hueHexColorList(base))


# Runs the server in debug mode on http://127.0.0.1:5000/
if __name__ == '__main__':
    app.run(debug=True)
