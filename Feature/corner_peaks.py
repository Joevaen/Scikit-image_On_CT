# 在拐点检测的输出图像中找到峰。
from skimage.feature import peak_local_max, corner_peaks
import numpy as np
response = np.zeros((5, 5))
response[2:4, 2:4] = 1
print(peak_local_max(response))
print(corner_peaks(response))
