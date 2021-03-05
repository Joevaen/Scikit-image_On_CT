from skimage.feature import corner_foerstner, corner_peaks
import numpy as np
square = np.zeros([10, 10])
square[2:8, 2:8] = 1
square.astype(int)
w, q = corner_foerstner(square)
accuracy_thresh = 0.5
roundness_thresh = 0.3
foerstner = (q > roundness_thresh) * (w > accuracy_thresh) * w
corner_peaks(foerstner, min_distance=1)



