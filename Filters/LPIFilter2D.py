# 线性位置不变滤波器（二维）
import numpy as np
from skimage.filters import LPIFilter2D
def filt_func(r, c, sigma = 1):
    return np.exp(-np.hypot(r, c)/sigma)
filter = LPIFilter2D(filt_func)