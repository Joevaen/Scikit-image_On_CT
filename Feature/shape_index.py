from skimage.feature import shape_index
import numpy as np
square = np.zeros((5, 5))
square[2, 2] = 4
s = shape_index(square, sigma=0.1)
print(s)




