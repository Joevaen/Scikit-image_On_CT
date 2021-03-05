from skimage.morphology import octagon
from skimage.feature import (corner_fast, corner_peaks,
                             corner_orientations)
import numpy as np
square = np.zeros((12, 12))
square[3:9, 3:9] = 1
square.astype(int)
corners = corner_peaks(corner_fast(square, 9), min_distance=1)
orientations = corner_orientations(square, corners, octagon(3, 2))
np.rad2deg(orientations)
