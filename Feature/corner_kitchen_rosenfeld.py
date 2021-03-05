from skimage.feature import corner_moravec
import numpy as np
square = np.zeros([7, 7])
square[3, 3] = 1
square.astype(int)
corner_moravec(square).astype(int)






