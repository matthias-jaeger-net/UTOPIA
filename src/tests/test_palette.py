#!usr/bin/env python
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Get a color palette from a given single color
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from colortools import Color
from colortools import randomColor
from colortools import randomColorList
from colortools import fromHls
from testtools import printTestPage

printTestPage([
    fromHls(0.0, 0.5, 0.5),
    fromHls(0.0, 0.5, 0.5),
    fromHls(0.2, 0.5, 0.5),
    fromHls(0.3, 0.5, 1)
])

c = fromHls(0.12, 0.1, 0.02)
print(c.analyze())
print(c.log())
# print(randomHexColorList(100))
# for color in palette(baseColor):
#    print(color.log())
