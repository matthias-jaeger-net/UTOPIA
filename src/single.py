#!usr/bin/env python
from colortools import Color
from colortools import randomColor
cols = 69
page_color = randomColor()
print('Test page running')
print('#'*cols)
page_color.analyze()
page_color.log()
print('#'*cols)
print('Expected similar colors')
print('#'*cols)
similar = page_color.similar_colors()
for color in similar:
    print('-'*cols)
    page_color.analyze()
    color.log()
print('#'*cols)
