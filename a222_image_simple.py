import math
from PIL import Image 
import numpy as np

# a multi-dimensional list
mat = [
        [(0,0,0), (255,255,255), (0,0,0)],
        [(255,255,255), (0,0,0), (255,255,255)],
        [(0,0,0), (255,255,255), (0,0,0)]
]



print("what is this?", mat[0])
print("what is this?", mat[0][0])
print("what is this?", mat[0][0][0])


# magic!!
# result = Image.fromarray(np.uint8(mat))
# result.save("u22inProgressUnsynced/bw.png")