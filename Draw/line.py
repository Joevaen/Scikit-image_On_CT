# 生成两端点所连直线上的点的坐标
from skimage.draw import line
import numpy as np
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc = line(1, 1, 8, 8)
img[rr, cc] = 1
print(img)









