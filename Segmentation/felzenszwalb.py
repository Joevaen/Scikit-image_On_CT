# 计算Felsenszwalb基于图形的有效图像分割。
from skimage.segmentation import felzenszwalb
from skimage.data import coffee
img = coffee()
segments = felzenszwalb(img, scale=3.0, sigma=0.95, min_size=5)
print(segments)