# 生成矩形的周长上的坐标
import numpy as np
from skimage.draw import rectangle_perimeter
img = np.zeros((5, 6), dtype=np.uint8)
start = (2, 3)
end = (3, 4)
rr, cc = rectangle_perimeter(start, end=end, shape=img.shape)
img[rr, cc] = 1
print(img)




