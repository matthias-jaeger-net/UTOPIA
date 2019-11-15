#!usr/bin/env python
from math import floor
from colortools import Color
from colortools import fromHls
from testtools import printTestPage
from colortools import randomColorList

printTestPage(randomColorList(100))

# names = [
#     "red", "orange", "yellow", "lime", "green", "turquoise", "cyan",
#     "azure", "blue", "purple", "magenta", "crimson"
# ]

# colors = []

# for i in range(0, len(names)):
#     m = str(i)
#     m += ": " + names[i]
#     m += ", value: " + str(i/len(names))
#     m += ", angle: " + str((i/len(names)*360))
#     color = fromHls(i/len(names), 0.5, 0.5)
#     colors.append(color)

# for color in colors:
#     print(color.log())

# printTestPage(colors)
