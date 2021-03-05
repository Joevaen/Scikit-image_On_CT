# 生成圆内像素的坐标。
import numpy as np
from skimage.draw import disk
img = np.zeros((10, 10), dtype=np.uint8)
rr, cc = disk((4, 4), 5)
img[rr, cc] = 1
print(img)









