from skimage.feature import corner_harris, corner_peaks, corner_subpix
import numpy as np
img = np.zeros((10, 10))
img[:5, :5] = 1
img[5:, 5:] = 1
img.astype(int)
coords = corner_peaks(corner_harris(img), min_distance=2)
coords_subpix = corner_subpix(img, coords, window_size=7)
