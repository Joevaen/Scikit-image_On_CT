# 基于ISODATA方法的返回阈值。
from skimage.data import coins
from skimage.filters import threshold_isodata
image = coins()
thresh = threshold_isodata(image)
binary = image > thresh
print(binary)

