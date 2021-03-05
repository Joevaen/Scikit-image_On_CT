# 生成椭圆周长内的坐标
import numpy as np
from skimage.draw import ellipse_perimeter
img = np.zeros((10, 12), dtype=np.uint8)
rr, cc = ellipse_perimeter(5, 6, 3, 5)
img[rr, cc] = 1
print(img)









