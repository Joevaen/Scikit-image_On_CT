# 根据原图和原图上多边形的几个顶点来确定多边形的区域，生成mask
import numpy as np
from skimage.draw import polygon2mask
image_shape = (128, 128)
polygon = np.array([[60, 100], [100, 40], [40, 40]])
mask = polygon2mask(image_shape, polygon)
print(mask.shape)
print(mask)
