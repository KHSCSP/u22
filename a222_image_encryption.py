'''
converts plain text into
black & white 'encypted' image
using ascii, then binary
'''

import math
from PIL import Image 
import numpy as np

mess = "PLTW AP Computer Science Principles. We are learning about data."

# convert to list of ascii
# ex: PLTW AP -> [72, 101, 108...]
# TODO

# print("debug list of ascii values:", asclist)
# ^^^ uncomment and run to see what it looks like so far




# convert to list of binary, removing '0b' prefix
# ex: [72, 101, 108...] -> ['1001000', '1100101', '1101100'...]
# TODO

# print("debug list of binary nums:", binlist)
# ^^^ uncomment and run to see what it looks like so far



# optional: fill each to 8 bits (add leading zeros)
# this would assist with decryption




# convert to long string
# ex: ['1001000', '1100101', '1101100'...] -> 100100011001011101100...
s = ''
# TODO

# print("debug long string:", s)




# Question: in theory, how many bits 
# will be required for our image?
# hint: what is the length of s?





# length of list, square root, round up
# this will be the size of the 2D list
size = 0
mat = []
# print("debug zeros 2d list:", mat)

# convert to square 2d list
# ex: 100100011001011101100 -> [[(255,255,255), (0,0,0), (0,0,0)...]
# 'count' will keep track of which bit we are on
# TODO

# print("debug 2d list:", mat)





# save to image, magic!
# result = Image.fromarray(np.uint8(mat))
# result.save("bw_encryption.png")
# ^^^ uncomment and check out the image!!
