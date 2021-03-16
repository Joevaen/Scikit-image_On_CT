# 通过李的迭代最小交叉熵方法计算阈值。
from skimage.data import coins
from skimage.filters import threshold_li
image = coins()
thresh = threshold_li(image)
binary = image > thresh
print(binary)

