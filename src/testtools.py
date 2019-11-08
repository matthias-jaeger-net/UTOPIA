#!usr/bin/env python


def printTestPage(base, colors):
    file = open('index.html', 'w+')
    file.write('<!DOCTYPE html>')
    file.write('<html lang="en">')
    file.write('<head>')
    file.write('<meta charset="UTF-8">')
    file.write('<link rel="stylesheet" href="static/style.css">')
    file.write('<body>')

    for color in colors:
        a = '<a class="color-suggestion"'
        a += ' style="background-color: #'
        a += color.hex
        a += ';" href="#">'
        a += color.analyze() + '<br>'
        a += color.log() + '<br>'
        a += '</a>'
        file.write(a)
    file.write('</body>')
    file.write('</html>')
    file.close()
