#!usr/bin/env python


def printTestPage(base, hueVariants, lightnessVariants, saturationVariants):

    file = open('index.html', 'w+')
    file.write('<!DOCTYPE html>')
    file.write('<html lang="en">')
    file.write('<head>')
    file.write('<meta charset="UTF-8">')
    file.write('<link rel="stylesheet" href="static/style.css">')

    file.write('<body>')

    file.write('<header>')
    file.write('<h1>' + base.analyze() + '</h1>')
    file.write('<div class="base-color" style="background: #' +
               base.hex + ';"></div>')
    file.write('<p class="lead">' + base.log() + '</p>')
    file.write('</header>')

    file.write('<main>')

    file.write('<h2>Lightness scheme</h2>')
    file.write('<div class="color-suggestions">')
    for color in lightnessVariants:
        a = '<div class="color-suggestion" style="background-color: #'
        a += color.hex + '"></div>'
        file.write(a)
    file.write('</div>')

    file.write('<h2>Hue scheme</h2>')
    file.write('<div class="color-suggestions">')
    for color in hueVariants:
        a = '<div class="color-suggestion" style="background-color: #'
        a += color.hex + '"></div>'
        file.write(a)
    file.write('</div>')

    file.write('<h2>Saturation scheme</h2>')
    file.write('<div class="color-suggestions">')
    for color in saturationVariants:
        a = '<div class="color-suggestion" style="background-color: #'
        a += color.hex + '"></div>'
        file.write(a)
    file.write('</div>')

    file.write('</main>')
    file.write('<script src="static/randdomsize.js"></script>')

    file.write('</body>')
    file.write('</html>')
    file.close()
