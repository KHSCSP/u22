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
asclist = [ord(item) for item in mess]
# print("debug list of ascii values:", asclist)



# convert to list of binary, removing '0b' prefix
# ex: [72, 101, 108...] -> ['1001000', '1100101', '1101100'...]
binlist = [bin(item)[2:] for item in asclist]
# print("debug list of binary nums:", binlist)




# optional: fill each to 8 bits (add leading zeros)
# this would assist with decryption




# convert to long string
# ex: ['1001000', '1100101', '1101100'...] -> 100100011001011101100...
s = ''
for item in binlist:
    s += item
# print("debug long string:", s)

# Question: in theory, how many bits 
# will be required for our image?
# hint: what is the length of s?




# convert to square 2d list
# ex: 100100011001011101100 -> [[(255,255,255), (0,0,0), (0,0,0)...]
# length of list, square root, round up
size = int(math.ceil((len(s))**0.5))
mat = [[(0,0,0)]*size for _ in range(size)]
# print("debug zeros 2d list:", mat)
count = 0
for row in range(size):
    for col in range(size):
        # protect against 'running out' of items in s
        # before reaching the end of the 2D list
        if count < len(s):
            # the 2D list is filled with (0,0,0)
            # only need to change '1' to (255,255,255)
            if s[count] == '1':
                mat[row][col] = (255,255,255)
        count += 1
# print("debug 2d list:", mat)



# save to image, magic!
result = Image.fromarray(np.uint8(mat))
result.save("u22inProgressUnsynced/bw_encryption.png")