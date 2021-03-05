# Brief（二进制鲁棒独立基本特征）是一种有效的特征点描述符。 即使使用相对较少的位，也具有很高的判别力，并且使用简单的强度差测试进行计算。

from skimage.feature import (corner_harris, corner_peaks, BRIEF,
                             match_descriptors)
import numpy as np
square1 = np.zeros((8, 8), dtype=np.int32)
square1[2:6, 2:6] = 1
print(square1)

square2 = np.zeros((9, 9), dtype=np.int32)
square2[2:7, 2:7] = 1
print(square2)

keypoints1 = corner_peaks(corner_harris(square1), min_distance=1)
keypoints2 = corner_peaks(corner_harris(square2), min_distance=1)
extractor = BRIEF(patch_size=5)
extractor.extract(square1, keypoints1)
descriptors1 = extractor.descriptors
extractor.extract(square2, keypoints2)
descriptors2 = extractor.descriptors
matches = match_descriptors(descriptors1, descriptors2)
print(matches)

print(keypoints1[matches[:, 0]])

print(keypoints2[matches[:, 1]])



