# 根据局部像素邻域计算阈值蒙版图像。
from skimage.data import coins
from skimage.filters import threshold_local
image = coins()
thresh = threshold_local(image, 15, 'mean')
binary = image > thresh
print(binary)

