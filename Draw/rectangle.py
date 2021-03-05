# 生成矩形内的所有点坐标，可以用于多维图像，可以根据起点和终点来画也可以根据起点和延展方向来画
import numpy as np
from skimage.draw import rectangle
img = np.zeros((5, 5), dtype=np.uint8)
start = (1, 1)
extent = (3, 3)
rr, cc = rectangle(start, extent=extent, shape=img.shape)
img[rr, cc] = 1
print(img)

img = np.zeros((6, 6), dtype=np.uint8)
start = (3, 3)

rr, cc = rectangle(start, extent=(2, 2))
img[rr, cc] = 1
rr, cc = rectangle(start, extent=(-2, 2))
img[rr, cc] = 2
rr, cc = rectangle(start, extent=(-2, -2))
img[rr, cc] = 3
rr, cc = rectangle(start, extent=(2, -2))
img[rr, cc] = 4
print(img)






