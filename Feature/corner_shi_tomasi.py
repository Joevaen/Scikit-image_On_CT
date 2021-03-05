from skimage.feature import corner_shi_tomasi, corner_peaks
import numpy as np
square = np.zeros([10, 10])
square[2:8, 2:8] = 1
square.astype(int)
corner_peaks(corner_shi_tomasi(square), min_distance=1)



