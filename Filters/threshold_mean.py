# 基于灰度值的平均值返回阈值。
from skimage.data import coins
from skimage.filters import threshold_mean
image = coins()
thresh = threshold_mean(image)
binary = image > thresh
print(binary)

