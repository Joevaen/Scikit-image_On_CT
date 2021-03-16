# 基于otsu返回阈值。
from skimage.data import coins
from skimage.filters import threshold_otsu
image = coins()
thresh = threshold_otsu(image)
binary = image > thresh
print(binary)

